#!/usr/bin/env python3
"""Parallel live regression runner — Claude-only quick check.

For cross-model testing (Claude + OpenAI + Gemini + xAI + Mistral + DeepSeek),
use run_batch_parallel.py instead. This script is a fast single-provider check
against the full 44-test regression_suite.json.
"""
from __future__ import annotations
import sys
sys.dont_write_bytecode = True

import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from runtime_validator import validate_output

SUITE_PATH = ROOT / 'tests' / 'regression_suite.json'
OUTPUTS_DIR = ROOT / 'tests' / 'live_outputs'
DEPLOY_PATH = ROOT / 'dist' / 'DESIGNPILOT_DEPLOY.md'

def call_claude(prompt, system_prompt, model, max_tokens=1200, retries=5):
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
    kwargs = dict(model=model, max_tokens=max_tokens,
                  messages=[{'role': 'user', 'content': prompt}])
    if system_prompt:
        kwargs['system'] = system_prompt
    for attempt in range(retries):
        t0 = time.monotonic()
        try:
            msg = client.messages.create(**kwargs)
            return ''.join(b.text for b in msg.content if hasattr(b, 'text')), round(time.monotonic()-t0, 2)
        except Exception as e:
            if '429' in str(e) and attempt < retries - 1:
                wait = 65 * (attempt + 1)   # 65s, 130s, 195s ...
                print(f"  rate limited, waiting {wait}s (attempt {attempt+1}/{retries})", flush=True)
                time.sleep(wait)
            else:
                raise

def run_one(test, system_prompt, model, out_dir, mode):
    prompt = test.get('full_prompt') or test['prompt']
    task_id = test['validator_task']
    expected = test['expected_decision']
    try:
        response, latency = call_claude(prompt, system_prompt, model)
    except Exception as e:
        return {'test_id': test['id'], 'error': str(e), 'passed': False}
    (out_dir / f"{test['id']}_{mode}.md").write_text(response, encoding='utf-8')
    val = validate_output(task_id, prompt, response)
    passed = val['decision'] == expected
    return {
        'test_id': test['id'], 'category': test['category'],
        'mode': mode, 'expected_decision': expected,
        'validator_decision': val['decision'], 'validator_score': val['score'],
        'passed': passed, 'latency_seconds': latency,
        'issues': val['issues'], 'warnings': val['warnings'],
    }

def run_all(model, mode, run_id, workers=4, test_ids=None):
    suite = json.loads(SUITE_PATH.read_text())
    tests = suite['tests']
    if test_ids:
        tests = [t for t in tests if t['id'] in test_ids]
    system_prompt = DEPLOY_PATH.read_text() if mode == 'pack' else None
    out_dir = OUTPUTS_DIR / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    results = []
    done = 0
    total = len(tests)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(run_one, t, system_prompt, model, out_dir, mode): t for t in tests}
        for f in as_completed(futures):
            done += 1
            r = f.result()
            results.append(r)
            status = 'PASS' if r.get('passed') else 'FAIL'
            err = r.get('error', '')
            score = r.get('validator_score', '-')
            print(f"[{done}/{total}] {status}  {r['test_id']}  score={score}"
                  + (f"  ERROR:{err}" if err else ''), flush=True)

    valid = [r for r in results if 'error' not in r]
    pass_count = sum(1 for r in valid if r['passed'])
    summary = {
        'run_id': run_id, 'model': model, 'mode': mode,
        'run_date': datetime.now(timezone.utc).isoformat(),
        'pack_version': json.loads((ROOT/'PACK_MANIFEST.json').read_text())['version'],
        'tests_run': len(valid), 'pass_count': pass_count,
        'pass_rate': round(pass_count/len(valid), 3) if valid else 0,
        'mean_score': round(sum(r['validator_score'] for r in valid)/len(valid), 1) if valid else 0,
        'by_category': {},
        'results': sorted(results, key=lambda r: r['test_id']),
    }
    for r in valid:
        cat = r['category']
        summary['by_category'].setdefault(cat, {'total': 0, 'passed': 0})
        summary['by_category'][cat]['total'] += 1
        if r['passed']:
            summary['by_category'][cat]['passed'] += 1
    (out_dir / 'summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    return summary

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--model', default='claude-sonnet-4-6')
    p.add_argument('--run-id', required=True)
    p.add_argument('--mode', choices=['pack', 'baseline'], default='pack')
    p.add_argument('--workers', type=int, default=4)
    p.add_argument('--test-ids', nargs='*')
    args = p.parse_args()
    s = run_all(args.model, args.mode, args.run_id, args.workers, args.test_ids)
    print(f"\n{'='*50}")
    print(f"Mode: {args.mode} | Model: {args.model}")
    print(f"Pass rate: {s['pass_count']}/{s['tests_run']} = {s['pass_rate']:.0%}")
    print(f"Mean score: {s['mean_score']}")
    print(f"Results: tests/live_outputs/{args.run_id}/summary.json")
