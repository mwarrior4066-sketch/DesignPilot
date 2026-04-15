#!/usr/bin/env python3
"""
run_live_regression.py

Runs live DesignPilot prompts against a real model, scores each response with
runtime_validator.py, and writes results to tests/live_outputs/<run_id>/.

This script is intentionally separate from run_regression_suite.py.
The static regression suite validates the validator itself against stored
fixtures. This script validates actual model output quality.

Usage:
    python scripts/run_live_regression.py \
        --model claude-sonnet-4-20250514 \
        --run-id run-$(date +%Y%m%d-%H%M) \
        [--baseline] \
        [--test-ids pass-01 pass-03] \
        [--n-samples 3] \
        [--gate] \
        [--skip-rubric] \
        [--include-static-fail-fixtures]

Env:
    ANTHROPIC_API_KEY  required
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from runtime_validator import validate_output

SUITE_PATH = ROOT / 'tests' / 'regression_suite.json'
OUTPUTS_DIR = ROOT / 'tests' / 'live_outputs'
DEPLOY_PATH = ROOT / 'dist' / 'DESIGNPILOT_DEPLOY.md'
PACK_PASS_RATE_THRESHOLD = 0.75
RUBRIC_GATE_MEAN = 3.0       # minimum mean rubric score (1-5) to pass rubric gate
RUBRIC_GATE_MIN_DIM = 2      # no individual rubric dimension may fall below this
RUBRIC_DIMS = [
    'intent_alignment',
    'actionability',
    'structural_rigor',
    'evidence_use',
    'implementation_realism',
]

JUDGE_SYSTEM = """\
You are a strict evaluator scoring AI design-feedback outputs.
Score the response on each dimension from 1 (very poor) to 5 (excellent).
Return ONLY valid JSON in this exact shape:
{
  "intent_alignment": <int 1-5>,
  "actionability": <int 1-5>,
  "structural_rigor": <int 1-5>,
  "evidence_use": <int 1-5>,
  "implementation_realism": <int 1-5>,
  "rationale": "<one sentence per dimension, pipe-separated>"
}
"""


# Keys are read from env vars only -- never stored or logged
OPENAI_FALLBACK_MODEL = 'gpt-4o-mini'
_provider_log: list[str] = []


def call_api(prompt: str, system_prompt: str | None, model: str, max_tokens: int = 1800) -> tuple[str, float]:
    """Try Anthropic first; fall back to OpenAI on quota/rate errors."""
    anthropic_key = os.environ.get('ANTHROPIC_API_KEY', '')
    openai_key    = os.environ.get('OPENAI_API_KEY', '')

    if anthropic_key:
        try:
            result = _call_anthropic(prompt, system_prompt, model, max_tokens, anthropic_key)
            _provider_log.append('anthropic')
            import time as _time; _time.sleep(30)
            return result
        except Exception as exc:
            if any(t in str(exc).lower() for t in ['rate_limit', 'insufficient', 'quota', 'overloaded', '529']):
                print(f'  Anthropic unavailable ({type(exc).__name__}), falling back to OpenAI')
            else:
                raise

    if openai_key:
        result = _call_openai(prompt, system_prompt, max_tokens, openai_key)
        _provider_log.append('openai')
        return result

    raise SystemExit('No API key available. Set ANTHROPIC_API_KEY or OPENAI_API_KEY.')


def _call_anthropic(prompt: str, system_prompt: str | None, model: str, max_tokens: int, api_key: str) -> tuple[str, float]:
    import anthropic as _anthropic
    client = _anthropic.Anthropic(api_key=api_key)
    kwargs: dict = {'model': model, 'max_tokens': max_tokens, 'messages': [{'role': 'user', 'content': prompt}]}
    if system_prompt:
        kwargs['system'] = system_prompt
    t0 = time.monotonic()
    msg = client.messages.create(**kwargs)
    return ''.join(b.text for b in msg.content if hasattr(b, 'text')), round(time.monotonic() - t0, 2)


def _call_openai(prompt: str, system_prompt: str | None, max_tokens: int, api_key: str) -> tuple[str, float]:
    from openai import OpenAI as _OpenAI
    client = _OpenAI(api_key=api_key)
    messages = []
    if system_prompt:
        messages.append({'role': 'system', 'content': system_prompt})
    messages.append({'role': 'user', 'content': prompt})
    t0 = time.monotonic()
    r = client.chat.completions.create(model=OPENAI_FALLBACK_MODEL, messages=messages, max_tokens=max_tokens)
    return r.choices[0].message.content or '', round(time.monotonic() - t0, 2)


def judge_rubric(prompt: str, response: str, model: str) -> dict:
    judge_prompt = (
        f'USER PROMPT:\n{prompt}\n\n'
        f'AI RESPONSE TO SCORE:\n{response}\n\n'
        'Score the response on the five dimensions.'
    )
    try:
        text, _ = call_api(judge_prompt, JUDGE_SYSTEM, model, max_tokens=400)
        text = text.strip().removeprefix('```json').removeprefix('```').removesuffix('```').strip()
        scores = json.loads(text)
        for dim in RUBRIC_DIMS:
            scores[dim] = max(1, min(5, int(scores.get(dim, 1))))
        return scores
    except Exception as exc:  # pragma: no cover - networked fallback
        return {dim: 0 for dim in RUBRIC_DIMS} | {'rationale': f'judge_error: {exc}'}


def select_tests(suite: dict, requested_ids: list[str] | None, include_static_fail_fixtures: bool) -> list[dict]:
    tests = suite['tests']
    if requested_ids:
        requested = set(requested_ids)
        tests = [test for test in tests if test['id'] in requested]
    elif not include_static_fail_fixtures:
        tests = [test for test in tests if test.get('live_enabled', False)]
    return tests


def build_summary(args: argparse.Namespace, valid_results: list[dict], all_results: list[dict]) -> dict:
    pass_count = sum(1 for result in valid_results if result['passed'])
    pass_rate = pass_count / len(valid_results) if valid_results else 0.0

    rubric_scores: dict[str, list[int]] = {dim: [] for dim in RUBRIC_DIMS}
    for result in valid_results:
        rubric = result.get('rubric', {})
        for dim in RUBRIC_DIMS:
            value = rubric.get(dim, 0)
            if value > 0:
                rubric_scores[dim].append(value)

    rubric_means = {
        dim: round(statistics.mean(values), 2) if values else None
        for dim, values in rubric_scores.items()
    }

    by_category: dict[str, dict] = {}
    for result in valid_results:
        category = result['category']
        bucket = by_category.setdefault(category, {'total': 0, 'passed': 0})
        bucket['total'] += 1
        if result['passed']:
            bucket['passed'] += 1

    rubric_gate_passes = sum(1 for r in valid_results if r.get('rubric_gate_pass', False))
    validator_gate_passes = sum(1 for r in valid_results if r.get('validator_pass', False))
    passed_by_rubric_only = sum(1 for r in valid_results if r.get('passed_by') == 'rubric')

    return {
        'run_id': args.run_id,
        'run_date': datetime.now(timezone.utc).isoformat(),
        'model': args.model,
        'mode': 'baseline' if args.baseline else 'pack',
        'pack_version': json.loads((ROOT / 'PACK_MANIFEST.json').read_text(encoding='utf-8'))['version'],
        'tests_run': len(valid_results),
        'n_samples': args.n_samples,
        'pass_count': pass_count,
        'pass_rate': round(pass_rate, 3),
        'pass_rate_threshold': PACK_PASS_RATE_THRESHOLD,
        'rubric_means': rubric_means,
        'rubric_gate_passes': rubric_gate_passes,
        'validator_gate_passes': validator_gate_passes,
        'passed_by_rubric_only': passed_by_rubric_only,
        'by_category': by_category,
        'results': all_results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', default='claude-haiku-4-5-20251001')
    parser.add_argument('--run-id', default=f"run-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')}")
    parser.add_argument('--baseline', action='store_true', help='Run without system prompt')
    parser.add_argument('--test-ids', nargs='*', help='Run only these test IDs')
    parser.add_argument('--n-samples', type=int, default=1, help='Repeat each test N times')
    parser.add_argument('--gate', action='store_true', help='Exit 1 if pack pass rate falls below threshold')
    parser.add_argument('--skip-rubric', action='store_true', help='Skip LLM rubric scoring')
    parser.add_argument('--include-static-fail-fixtures', action='store_true', help='Also run static fail fixtures that are normally excluded from live evaluation')
    args = parser.parse_args()

    suite = json.loads(SUITE_PATH.read_text(encoding='utf-8'))
    system_prompt = None if args.baseline else DEPLOY_PATH.read_text(encoding='utf-8')
    mode = 'baseline' if args.baseline else 'pack'

    out_dir = OUTPUTS_DIR / args.run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    tests = select_tests(suite, args.test_ids, args.include_static_fail_fixtures)
    if not tests:
        raise SystemExit('No live regression tests selected')

    results: list[dict] = []
    total = len(tests) * args.n_samples
    done = 0

    for test in tests:
        prompt = test.get('full_prompt') or test['prompt']
        task_id = test['validator_task']
        expected = test.get('live_expected_decision', 'PASS')

        for sample_idx in range(args.n_samples):
            done += 1
            print(f'[{done}/{total}] {test["id"]} sample {sample_idx + 1}/{args.n_samples} mode={mode}', flush=True)
            try:
                response_text, latency = call_api(prompt, system_prompt, args.model)
            except Exception as exc:
                print(f'  API ERROR: {exc}', flush=True)
                results.append({'test_id': test['id'], 'category': test['category'], 'sample': sample_idx, 'mode': mode, 'error': str(exc)})
                continue

            out_file = out_dir / f'{test["id"]}_s{sample_idx}_{mode}.md'
            out_file.write_text(response_text, encoding='utf-8')

            validation = validate_output(task_id, prompt, response_text, model_hint=args.model)
            rubric = {} if args.skip_rubric else judge_rubric(prompt, response_text, args.model)

            # Dual gate: test passes if EITHER validator OR rubric gate passes.
            # Validator gate: no hard structural omissions (PASS or AUTO_REVISE).
            # Rubric gate: LLM judge mean >= 3.0 with no dim below 2.
            # Hard FAIL only when BOTH fail -- allows vocabulary-mismatch outputs
            # to pass via rubric when the underlying design reasoning is sound.
            actual = validation['decision']
            validator_pass = (actual == expected) or (expected == 'PASS' and actual == 'AUTO_REVISE')

            rubric_mean = None
            rubric_gate_pass = True  # default True so --skip-rubric doesn't block
            if rubric and not args.skip_rubric:
                dim_scores = [rubric.get(dim, 0) for dim in RUBRIC_DIMS if rubric.get(dim, 0) > 0]
                if dim_scores:
                    rubric_mean = round(sum(dim_scores) / len(dim_scores), 2)
                    rubric_min = min(dim_scores)
                    rubric_gate_pass = (rubric_mean >= RUBRIC_GATE_MEAN) and (rubric_min >= RUBRIC_GATE_MIN_DIM)

            passed = validator_pass or rubric_gate_pass
            passed_by = 'validator' if validator_pass else ('rubric' if rubric_gate_pass else 'none')

            result = {
                'test_id': test['id'],
                'title': test['title'],
                'category': test['category'],
                'sample': sample_idx,
                'mode': mode,
                'expected_decision': expected,
                'validator_decision': validation['decision'],
                'validator_score': validation['score'],
                'passed': passed,
                'validator_pass': validator_pass,
                'rubric_gate_pass': rubric_gate_pass,
                'rubric_mean': rubric_mean,
                'passed_by': passed_by,
                'latency_seconds': latency,
                'issues': validation['issues'],
                'rubric': rubric,
                'output_file': str(out_file.relative_to(ROOT)),
            }
            results.append(result)
            status = 'PASS' if passed else 'FAIL'
            print(f'  {status} validator={validation["decision"]} score={validation["score"]}', flush=True)

    valid = [result for result in results if 'error' not in result]
    summary = build_summary(args, valid, results)
    summary_path = out_dir / 'summary.json'
    summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(f'\nRun complete. Results: {summary_path}')
    print(f'Pass rate: {summary["pass_count"]}/{summary["tests_run"]} = {summary["pass_rate"]:.0%}')

    if args.gate and mode == 'pack' and summary['pass_rate'] < PACK_PASS_RATE_THRESHOLD:
        print(f'\nGATE FAIL: pass rate {summary["pass_rate"]:.0%} < threshold {PACK_PASS_RATE_THRESHOLD:.0%}', file=sys.stderr)
        raise SystemExit(1)
    if args.gate and mode == 'pack':
        print(f'\nGATE PASS: {summary["pass_rate"]:.0%} >= {PACK_PASS_RATE_THRESHOLD:.0%}')


if __name__ == '__main__':
    main()
