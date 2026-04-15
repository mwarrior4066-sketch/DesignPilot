#!/usr/bin/env python3
"""
run_comparative.py

Runs live pack versus baseline comparisons, stores blinded evaluations in
tests/live_evals/<run_id>/, and prints a summary.

Usage:
    python scripts/run_comparative.py \
        --model claude-sonnet-4-20250514 \
        --run-id comparative-$(date +%Y%m%d) \
        [--test-ids pass-01 pass-03]

Env:
    ANTHROPIC_API_KEY  required
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from runtime_validator import validate_output

SUITE_PATH = ROOT / 'tests' / 'regression_suite.json'
LIVE_EVALS_DIR = ROOT / 'tests' / 'live_evals'
DEPLOY_PATH = ROOT / 'dist' / 'DESIGNPILOT_DEPLOY.md'
SCHEMA_PATH = LIVE_EVALS_DIR / 'schema.json'

JUDGE_SYSTEM = """\
You are a strict blind evaluator comparing two AI responses to a design task.
Return ONLY valid JSON in this shape:
{
  "response_a_score": <int 1-5>,
  "response_b_score": <int 1-5>,
  "overall_preference": "A" | "B" | "tie",
  "response_a_strengths": "<one sentence>",
  "response_b_strengths": "<one sentence>",
  "notes": "<one sentence on the deciding factor>"
}
"""


OPENAI_FALLBACK_MODEL = 'gpt-4o-mini'


def call_api(prompt: str, system_prompt: str | None, model: str, max_tokens: int = 1800) -> tuple[str, float]:
    """Try Anthropic first; fall back to OpenAI on quota/rate errors. Keys from env only."""
    anthropic_key = os.environ.get('ANTHROPIC_API_KEY', '')
    openai_key    = os.environ.get('OPENAI_API_KEY', '')

    if anthropic_key:
        try:
            import anthropic as _anthropic
            client = _anthropic.Anthropic(api_key=anthropic_key)
            kwargs: dict = {'model': model, 'max_tokens': max_tokens, 'messages': [{'role': 'user', 'content': prompt}]}
            if system_prompt:
                kwargs['system'] = system_prompt
            t0 = time.monotonic()
            msg = client.messages.create(**kwargs)
            return ''.join(b.text for b in msg.content if hasattr(b, 'text')), round(time.monotonic() - t0, 2)
        except Exception as exc:
            if any(t in str(exc).lower() for t in ['rate_limit', 'insufficient', 'quota', 'overloaded', '529']):
                print(f'  Anthropic unavailable ({type(exc).__name__}), falling back to OpenAI')
            else:
                raise

    if openai_key:
        from openai import OpenAI as _OpenAI
        client = _OpenAI(api_key=openai_key)
        messages = []
        if system_prompt:
            messages.append({'role': 'system', 'content': system_prompt})
        messages.append({'role': 'user', 'content': prompt})
        t0 = time.monotonic()
        r = client.chat.completions.create(model=OPENAI_FALLBACK_MODEL, messages=messages, max_tokens=max_tokens)
        return r.choices[0].message.content or '', round(time.monotonic() - t0, 2)

    raise SystemExit('No API key available. Set ANTHROPIC_API_KEY or OPENAI_API_KEY.')


def blind_judge(prompt: str, pack_response: str, baseline_response: str, model: str, seed: str) -> tuple[dict, dict]:
    rng = random.Random(seed)
    order = [('pack', pack_response), ('baseline', baseline_response)]
    rng.shuffle(order)
    response_a_label, response_a = order[0]
    response_b_label, response_b = order[1]

    judge_prompt = (
        f'TASK:\n{prompt}\n\n'
        f'RESPONSE A:\n{response_a}\n\n'
        f'RESPONSE B:\n{response_b}\n\n'
        'Score and compare these two responses.'
    )
    text, _ = call_api(judge_prompt, JUDGE_SYSTEM, model, max_tokens=500)
    text = text.strip().removeprefix('```json').removeprefix('```').removesuffix('```').strip()
    result = json.loads(text)

    preference = result.get('overall_preference', 'tie')
    if preference == 'A':
        mapped_preference = response_a_label
    elif preference == 'B':
        mapped_preference = response_b_label
    else:
        mapped_preference = 'tie'

    mapped = {
        'pack_score': result.get('response_a_score') if response_a_label == 'pack' else result.get('response_b_score'),
        'baseline_score': result.get('response_b_score') if response_a_label == 'pack' else result.get('response_a_score'),
        'overall_preference': mapped_preference,
        'pack_strengths': result.get('response_a_strengths') if response_a_label == 'pack' else result.get('response_b_strengths'),
        'baseline_strengths': result.get('response_b_strengths') if response_a_label == 'pack' else result.get('response_a_strengths'),
        'notes': result.get('notes', ''),
    }
    blind_metadata = {
        'response_a_source': response_a_label,
        'response_b_source': response_b_label,
        'raw_judge_result': result,
    }
    return mapped, blind_metadata


def validate_live_eval_record(record: dict, schema: dict) -> None:
    missing = [field for field in schema['required_fields'] if field not in record]
    if missing:
        raise ValueError(f'missing live eval fields: {missing}')
    if record['overall_preference'] not in {'pack', 'baseline', 'tie'}:
        raise ValueError('overall_preference must be pack, baseline, or tie')
    if record['evidence_mode'] not in {'live', 'proxy'}:
        raise ValueError('evidence_mode must be live or proxy')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='claude-haiku-4-5-20251001')
    parser.add_argument('--run-id', default=f"comparative-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')}")
    parser.add_argument('--test-ids', nargs='*')
    args = parser.parse_args()

    suite = json.loads(SUITE_PATH.read_text(encoding='utf-8'))
    tests = [test for test in suite['tests'] if test.get('live_enabled', False)]
    if args.test_ids:
        requested = set(args.test_ids)
        tests = [test for test in tests if test['id'] in requested]
    if not tests:
        raise SystemExit('No comparative tests selected')

    system_prompt = DEPLOY_PATH.read_text(encoding='utf-8')
    schema = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))

    LIVE_EVALS_DIR.mkdir(exist_ok=True)
    run_dir = LIVE_EVALS_DIR / args.run_id
    run_dir.mkdir(exist_ok=True)

    pack_wins = 0
    baseline_wins = 0
    ties = 0
    validator_deltas: list[int] = []

    for test in tests:
        prompt = test.get('full_prompt') or test['prompt']
        task_id = test['validator_task']
        print(f'Running comparative: {test["id"]} {task_id}', flush=True)

        pack_response, pack_latency = call_api(prompt, system_prompt, args.model)
        baseline_response, baseline_latency = call_api(prompt, None, args.model)

        pack_validation = validate_output(task_id, prompt, pack_response)
        baseline_validation = validate_output(task_id, prompt, baseline_response)
        judge_result, blind_metadata = blind_judge(prompt, pack_response, baseline_response, args.model, seed=f'{args.run_id}:{test["id"]}')

        preference = judge_result['overall_preference']
        if preference == 'pack':
            pack_wins += 1
        elif preference == 'baseline':
            baseline_wins += 1
        else:
            ties += 1

        score_delta = pack_validation['score'] - baseline_validation['score']
        validator_deltas.append(score_delta)

        live_result = {
            'run_id': f'{args.run_id}_{test["id"]}',
            'pack_version': json.loads((ROOT / 'PACK_MANIFEST.json').read_text(encoding='utf-8'))['version'],
            'baseline_label': 'bare_model_no_system_prompt',
            'prompt_id': test['id'],
            'run_date': datetime.now(timezone.utc).date().isoformat(),
            'evaluator_label': f'llm_judge_{args.model}',
            'evidence_mode': 'live',
            'scores': {
                'pack_validator': pack_validation['score'],
                'baseline_validator': baseline_validation['score'],
                'validator_delta': score_delta,
                'pack_judge': judge_result.get('pack_score'),
                'baseline_judge': judge_result.get('baseline_score'),
            },
            'overall_preference': preference,
            'notes': judge_result.get('notes', ''),
            'task_id': task_id,
            'pack_latency_seconds': pack_latency,
            'baseline_latency_seconds': baseline_latency,
            'pack_output_file': f'{test["id"]}_pack.md',
            'baseline_output_file': f'{test["id"]}_baseline.md',
            'judge_detail': judge_result,
            'blind_metadata': blind_metadata,
        }
        validate_live_eval_record(live_result, schema)

        (run_dir / f'{test["id"]}_pack.md').write_text(pack_response, encoding='utf-8')
        (run_dir / f'{test["id"]}_baseline.md').write_text(baseline_response, encoding='utf-8')
        (run_dir / f'{test["id"]}.json').write_text(json.dumps(live_result, indent=2), encoding='utf-8')
        print(f'  validator delta={score_delta:+d} preference={preference}', flush=True)

    total = pack_wins + baseline_wins + ties
    summary = {
        'run_id': args.run_id,
        'model': args.model,
        'total_tasks': total,
        'pack_wins': pack_wins,
        'baseline_wins': baseline_wins,
        'ties': ties,
        'pack_win_rate': round(pack_wins / total, 3) if total else 0,
        'mean_validator_delta': round(sum(validator_deltas) / len(validator_deltas), 1) if validator_deltas else 0,
    }
    (run_dir / 'summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print('\nComparative run complete.')
    print(f'Pack wins: {pack_wins}/{total} Baseline wins: {baseline_wins}/{total} Ties: {ties}')
    print(f'Mean validator score delta (pack - baseline): {summary["mean_validator_delta"]:+.1f}')


if __name__ == '__main__':
    main()
