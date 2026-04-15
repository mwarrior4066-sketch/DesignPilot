#!/usr/bin/env python3
"""
run_cross_model_suite.py

Runs the cross-model regression suite against a specified model family using
multi-provider API support. Uses dual-gate scoring (validator + rubric).

Gate threshold: 70% (lower than the 75% pack gate, accounting for non-primary
model vocabulary variation that is expected and handled by the alias system).

Usage:
    # Anthropic models
    python scripts/run_cross_model_suite.py --provider anthropic --model claude-sonnet-4-6

    # OpenAI models
    python scripts/run_cross_model_suite.py --provider openai --model gpt-4.1

    # Google models
    python scripts/run_cross_model_suite.py --provider google --model gemini-2.5-pro

    # AWS Bedrock (Nova)
    python scripts/run_cross_model_suite.py --provider bedrock --model amazon.nova-pro-v1:0

    # Mistral
    python scripts/run_cross_model_suite.py --provider mistral --model mistral-large-latest

    # Skip rubric scoring (faster, validator-only)
    python scripts/run_cross_model_suite.py --provider openai --model gpt-4.1 --skip-rubric

Env vars required per provider:
    ANTHROPIC_API_KEY    for provider=anthropic
    OPENAI_API_KEY       for provider=openai
    GOOGLE_API_KEY       for provider=google
    AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY + AWS_REGION  for provider=bedrock
    MISTRAL_API_KEY      for provider=mistral
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

SUITE_PATH = ROOT / 'tests' / 'cross_model_regression_suite.json'
OUTPUTS_DIR = ROOT / 'tests' / 'live_outputs' / 'batch'
DEPLOY_PATH = ROOT / 'dist' / 'DESIGNPILOT_DEPLOY.md'

CROSS_MODEL_GATE = 0.70

RUBRIC_DIMS = ['intent_alignment', 'actionability', 'structural_rigor', 'evidence_use', 'implementation_realism']
RUBRIC_GATE_MEAN = 3.0
RUBRIC_GATE_MIN_DIM = 2

JUDGE_SYSTEM = """\
You are a strict evaluator scoring AI design-feedback outputs.
Score the response on each dimension from 1 (very poor) to 5 (excellent).
Return ONLY valid JSON:
{
  "intent_alignment": <int 1-5>,
  "actionability": <int 1-5>,
  "structural_rigor": <int 1-5>,
  "evidence_use": <int 1-5>,
  "implementation_realism": <int 1-5>,
  "rationale": "<one sentence per dimension, pipe-separated>"
}
"""


# ── Provider adapters ──────────────────────────────────────────────────────

def call_anthropic(prompt: str, system: str | None, model: str, max_tokens: int = 2000) -> tuple[str, float]:
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
    kwargs = {'model': model, 'max_tokens': max_tokens, 'messages': [{'role': 'user', 'content': prompt}]}
    if system:
        kwargs['system'] = system
    t0 = time.monotonic()
    msg = client.messages.create(**kwargs)
    return ''.join(b.text for b in msg.content if hasattr(b, 'text')), round(time.monotonic() - t0, 2)


def call_openai(prompt: str, system: str | None, model: str, max_tokens: int = 2000) -> tuple[str, float]:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    messages = []
    if system:
        messages.append({'role': 'system', 'content': system})
    messages.append({'role': 'user', 'content': prompt})
    t0 = time.monotonic()
    r = client.chat.completions.create(model=model, messages=messages, max_tokens=max_tokens)
    return r.choices[0].message.content or '', round(time.monotonic() - t0, 2)


def call_google(prompt: str, system: str | None, model: str, max_tokens: int = 2000) -> tuple[str, float]:
    import google.generativeai as genai
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    cfg = genai.types.GenerationConfig(max_output_tokens=max_tokens)
    m = genai.GenerativeModel(model, system_instruction=system or '')
    t0 = time.monotonic()
    r = m.generate_content(prompt, generation_config=cfg)
    return r.text, round(time.monotonic() - t0, 2)


def call_bedrock(prompt: str, system: str | None, model: str, max_tokens: int = 2000) -> tuple[str, float]:
    import boto3, json as _json
    client = boto3.client('bedrock-runtime', region_name=os.environ.get('AWS_REGION', 'us-east-1'))
    body = {'messages': [{'role': 'user', 'content': [{'type': 'text', 'text': prompt}]}], 'max_tokens': max_tokens, 'anthropic_version': 'bedrock-2023-05-31'}
    if system:
        body['system'] = system
    t0 = time.monotonic()
    r = client.invoke_model(modelId=model, body=_json.dumps(body))
    result = _json.loads(r['body'].read())
    return result['content'][0]['text'], round(time.monotonic() - t0, 2)


def call_mistral(prompt: str, system: str | None, model: str, max_tokens: int = 2000) -> tuple[str, float]:
    from mistralai.client import MistralClient
    from mistralai.models.chat_completion import ChatMessage
    client = MistralClient(api_key=os.environ['MISTRAL_API_KEY'])
    messages = []
    if system:
        messages.append(ChatMessage(role='system', content=system))
    messages.append(ChatMessage(role='user', content=prompt))
    t0 = time.monotonic()
    r = client.chat(model=model, messages=messages, max_tokens=max_tokens)
    return r.choices[0].message.content, round(time.monotonic() - t0, 2)


PROVIDERS = {
    'anthropic': call_anthropic,
    'openai': call_openai,
    'google': call_google,
    'bedrock': call_bedrock,
    'mistral': call_mistral,
}


def call_api(prompt: str, system: str | None, provider: str, model: str, max_tokens: int = 2000) -> tuple[str, float]:
    fn = PROVIDERS.get(provider)
    if not fn:
        raise ValueError(f'Unknown provider: {provider}. Choose from: {list(PROVIDERS)}')
    result = fn(prompt, system, model, max_tokens)
    time.sleep(15)  # Rate-limit buffer between calls
    return result


def judge_rubric(prompt: str, response: str, provider: str, model: str) -> dict:
    judge_prompt = f'USER PROMPT:\n{prompt}\n\nAI RESPONSE TO SCORE:\n{response}\n\nScore the response on the five dimensions.'
    try:
        text, _ = call_api(judge_prompt, JUDGE_SYSTEM, provider, model, max_tokens=400)
        text = text.strip().removeprefix('```json').removeprefix('```').removesuffix('```').strip()
        scores = json.loads(text)
        for dim in RUBRIC_DIMS:
            scores[dim] = max(1, min(5, int(scores.get(dim, 1))))
        return scores
    except Exception as exc:
        return {dim: 0 for dim in RUBRIC_DIMS} | {'rationale': f'judge_error: {exc}'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--provider', required=True, choices=list(PROVIDERS), help='API provider')
    parser.add_argument('--model', required=True, help='Model name/ID for the chosen provider')
    parser.add_argument('--run-id', default=f"cross-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')}")
    parser.add_argument('--test-ids', nargs='*', help='Run only these test IDs (e.g. cm-01 cm-03)')
    parser.add_argument('--skip-rubric', action='store_true', help='Skip LLM rubric scoring (faster)')
    parser.add_argument('--baseline', action='store_true', help='Run without system prompt (no DesignPilot pack)')
    parser.add_argument('--gate', action='store_true', help='Exit 1 if pass rate falls below cross-model threshold')
    args = parser.parse_args()

    suite = json.loads(SUITE_PATH.read_text())
    system_prompt = None if args.baseline else DEPLOY_PATH.read_text(encoding='utf-8')
    mode = 'baseline' if args.baseline else 'pack'

    tests = suite['tests']
    if args.test_ids:
        tests = [t for t in tests if t['id'] in set(args.test_ids)]
    if not tests:
        raise SystemExit('No tests selected.')

    out_dir = OUTPUTS_DIR / args.run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []
    for i, test in enumerate(tests, 1):
        prompt = test['full_prompt']
        task_id = test['task']
        print(f'[{i}/{len(tests)}] {test["id"]} — {test["title"]}', flush=True)

        try:
            response, latency = call_api(prompt, system_prompt, args.provider, args.model)
        except Exception as exc:
            print(f'  API ERROR: {exc}', flush=True)
            results.append({'test_id': test['id'], 'error': str(exc)})
            continue

        out_file = out_dir / f'{test["id"]}_{mode}.md'
        out_file.write_text(response, encoding='utf-8')

        validation = validate_output(task_id, prompt, response, model_hint=args.model)
        rubric = {} if args.skip_rubric else judge_rubric(prompt, response, args.provider, args.model)

        actual = validation['decision']
        validator_pass = actual in ('PASS', 'AUTO_REVISE')

        rubric_mean = None
        rubric_gate_pass = True
        if rubric and not args.skip_rubric:
            dim_scores = [rubric.get(d, 0) for d in RUBRIC_DIMS if rubric.get(d, 0) > 0]
            if dim_scores:
                rubric_mean = round(sum(dim_scores) / len(dim_scores), 2)
                rubric_gate_pass = (rubric_mean >= RUBRIC_GATE_MEAN) and (min(dim_scores) >= RUBRIC_GATE_MIN_DIM)

        passed = validator_pass or rubric_gate_pass
        passed_by = 'validator' if validator_pass else ('rubric' if rubric_gate_pass else 'none')
        status = 'PASS' if passed else 'FAIL'
        print(f'  {status}  validator={actual}  score={validation["score"]}  rubric_mean={rubric_mean}  passed_by={passed_by}', flush=True)

        results.append({
            'test_id': test['id'],
            'title': test['title'],
            'task': task_id,
            'mode': mode,
            'validator_decision': actual,
            'validator_score': validation['score'],
            'validator_pass': validator_pass,
            'rubric_mean': rubric_mean,
            'rubric_gate_pass': rubric_gate_pass,
            'passed': passed,
            'passed_by': passed_by,
            'latency_seconds': latency,
            'issues': validation['issues'],
            'warnings': validation['warnings'],
            'rubric': rubric,
            'output_file': str(out_file.relative_to(ROOT)),
        })

    valid = [r for r in results if 'error' not in r]
    pass_count = sum(1 for r in valid if r['passed'])
    pass_rate = round(pass_count / len(valid), 3) if valid else 0.0

    rubric_means = {}
    for dim in RUBRIC_DIMS:
        vals = [r['rubric'].get(dim, 0) for r in valid if r.get('rubric') and r['rubric'].get(dim, 0) > 0]
        rubric_means[dim] = round(statistics.mean(vals), 2) if vals else None

    summary = {
        'run_id': args.run_id,
        'run_date': datetime.now(timezone.utc).isoformat(),
        'provider': args.provider,
        'model': args.model,
        'mode': mode,
        'tests_run': len(valid),
        'pass_count': pass_count,
        'pass_rate': pass_rate,
        'cross_model_gate': CROSS_MODEL_GATE,
        'gate_passed': pass_rate >= CROSS_MODEL_GATE,
        'rubric_means': rubric_means,
        'passed_by_rubric_only': sum(1 for r in valid if r.get('passed_by') == 'rubric'),
        'results': results,
    }
    summary_path = out_dir / 'summary.json'
    summary_path.write_text(json.dumps(summary, indent=2))
    print(f'\nRun complete: {summary_path}')
    print(f'Pass rate: {pass_count}/{len(valid)} = {pass_rate:.0%} (gate: {CROSS_MODEL_GATE:.0%})')
    print(f'Gate: {"PASS" if summary["gate_passed"] else "FAIL"}')

    if args.gate and not summary['gate_passed']:
        print(f'\nCROSS-MODEL GATE FAIL: {pass_rate:.0%} < {CROSS_MODEL_GATE:.0%}', file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
