#!/usr/bin/env python3
"""
run_rubric_eval.py

Standalone rubric scorer. Scores saved model output files against the
task_quality_rubric.json using an LLM judge. Does NOT run the static
validator -- this is a pure semantic quality check.

Useful for diagnosing whether a failure is a vocabulary issue (validator
hard-failed but rubric passes) or a genuine quality gap (both fail).

Usage:
    python scripts/run_rubric_eval.py \
        --run-dir tests/live_outputs/single-model/live-run-v2.8-sonnet \
        --model claude-haiku-4-5-20251001 \
        --out tests/live_outputs/single-model/live-run-v2.8-sonnet/rubric_report.json

    # Score a specific test
    python scripts/run_rubric_eval.py \
        --run-dir tests/live_outputs/single-model/live-run-v2.8-sonnet \
        --test-ids pass-01 pass-11 pass-17
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUBRIC_PATH = ROOT / 'tests' / 'scorecards' / 'task_quality_rubric.json'
SUITE_PATH = ROOT / 'tests' / 'regression_suite.json'

RUBRIC_DIMS = ['intent_alignment', 'actionability', 'structural_rigor', 'evidence_use', 'implementation_realism']
PASS_MEAN = 3.0
PASS_MIN_DIM = 2

JUDGE_SYSTEM = """\
You are a strict evaluator scoring AI design-feedback outputs. Do not reward verbosity.
Penalize outputs that restate the prompt without transformation.
Penalize outputs that describe solutions without concrete, actionable structure.
Score the response on each dimension from 1 (very poor) to 5 (excellent):

- intent_alignment: Did the response resolve the actual ask without drifting?
- actionability: Can a designer or developer act on this immediately?
- structural_rigor: Does the answer show hierarchy, sequence, and decision logic?
- evidence_use: Are claims linked to thresholds, constraints, or explicit proof types?
- implementation_realism: Is the proposal technically and operationally believable?

Return ONLY valid JSON:
{
  "intent_alignment": <int 1-5>,
  "actionability": <int 1-5>,
  "structural_rigor": <int 1-5>,
  "evidence_use": <int 1-5>,
  "implementation_realism": <int 1-5>,
  "rationale": "<one concise sentence per dimension, pipe-separated>"
}
"""


def call_judge(prompt: str, response: str, model: str) -> dict:
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
    judge_prompt = f'USER PROMPT:\n{prompt}\n\nAI RESPONSE TO SCORE:\n{response}\n\nScore the response on the five dimensions.'
    t0 = time.monotonic()
    msg = client.messages.create(
        model=model, max_tokens=400, system=JUDGE_SYSTEM,
        messages=[{'role': 'user', 'content': judge_prompt}]
    )
    text = ''.join(b.text for b in msg.content if hasattr(b, 'text'))
    text = text.strip().removeprefix('```json').removeprefix('```').removesuffix('```').strip()
    scores = json.loads(text)
    for dim in RUBRIC_DIMS:
        scores[dim] = max(1, min(5, int(scores.get(dim, 1))))
    scores['latency'] = round(time.monotonic() - t0, 2)
    return scores


def gate_result(scores: dict) -> dict:
    dim_scores = [scores.get(d, 0) for d in RUBRIC_DIMS]
    mean = round(statistics.mean(dim_scores), 2)
    min_dim = min(dim_scores)
    return {
        'mean': mean,
        'min_dim': min_dim,
        'passed': mean >= PASS_MEAN and min_dim >= PASS_MIN_DIM,
        'weakest': RUBRIC_DIMS[dim_scores.index(min_dim)],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--run-dir', required=True, help='Directory containing pass-NN_s0_*.md output files')
    parser.add_argument('--suite', default=str(SUITE_PATH))
    parser.add_argument('--model', default='claude-haiku-4-5-20251001', help='Judge model (Anthropic only)')
    parser.add_argument('--out', help='Output JSON path (default: <run-dir>/rubric_report.json)')
    parser.add_argument('--test-ids', nargs='*', help='Score only these test IDs')
    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    suite = json.loads(Path(args.suite).read_text())
    tests_by_id = {t['id']: t for t in suite['tests']}

    output_files = sorted(run_dir.glob('pass-*_s0_*.md'))
    results = []

    for output_file in output_files:
        test_id = output_file.name.split('_')[0]
        if args.test_ids and test_id not in args.test_ids:
            continue
        test = tests_by_id.get(test_id)
        if not test:
            print(f'  WARNING: no test found for {test_id}')
            continue
        prompt = test.get('full_prompt') or test['prompt']
        response = output_file.read_text(encoding='utf-8')
        print(f'Scoring {test_id} ({output_file.name})...', flush=True)
        try:
            scores = call_judge(prompt, response, args.model)
            gate = gate_result(scores)
            print(f'  mean={gate["mean"]} passed={gate["passed"]} weakest={gate["weakest"]}')
            results.append({
                'test_id': test_id,
                'output_file': str(output_file.relative_to(ROOT)),
                'scores': {d: scores[d] for d in RUBRIC_DIMS},
                'rationale': scores.get('rationale', ''),
                'gate': gate,
                'latency': scores.get('latency'),
            })
        except Exception as e:
            print(f'  ERROR: {e}')
            results.append({'test_id': test_id, 'error': str(e)})
        time.sleep(15)

    valid = [r for r in results if 'error' not in r]
    pass_count = sum(1 for r in valid if r.get('gate', {}).get('passed'))
    summary = {
        'run_dir': str(run_dir),
        'model_judge': args.model,
        'tests_scored': len(valid),
        'pass_count': pass_count,
        'pass_rate': round(pass_count / len(valid), 3) if valid else 0,
        'gate_threshold_mean': PASS_MEAN,
        'gate_threshold_min_dim': PASS_MIN_DIM,
        'results': results,
    }
    out_path = Path(args.out) if args.out else run_dir / 'rubric_report.json'
    out_path.write_text(json.dumps(summary, indent=2))
    print(f'\nRubric report: {out_path}')
    print(f'Pass rate: {pass_count}/{len(valid)}')


if __name__ == '__main__':
    main()
