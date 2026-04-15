#!/usr/bin/env python3
"""
run_batch_parallel.py

Runs the cross-model regression suite against all 6 providers simultaneously
using one thread per provider. Results stream as they arrive.

Providers: Claude (Anthropic) · Gemini (Google) · ChatGPT (OpenAI) ·
           Grok (xAI) · Mistral · DeepSeek

Usage:
    # Full run — all 6 providers, all 5 tests
    python scripts/run_batch_parallel.py

    # Specific tests only
    python scripts/run_batch_parallel.py --test-ids cm-01 cm-03

    # Skip rubric scoring (faster, validator-only)
    python scripts/run_batch_parallel.py --skip-rubric

    # Specific providers only
    python scripts/run_batch_parallel.py --providers claude gemini openai

    # Baseline mode (no DesignPilot system prompt)
    python scripts/run_batch_parallel.py --baseline

Required env vars (only needed for the providers you run):
    ANTHROPIC_API_KEY    — Claude
    GOOGLE_API_KEY       — Gemini
    OPENAI_API_KEY       — ChatGPT
    XAI_API_KEY          — Grok (xAI OpenAI-compatible endpoint)
    MISTRAL_API_KEY      — Mistral
    DEEPSEEK_API_KEY     — DeepSeek (OpenAI-compatible endpoint)

Optional env vars:
    JUDGE_MODEL          — Anthropic model to use as rubric judge (default: claude-haiku-4-5-20251001)
                           Always uses Anthropic for scoring consistency across providers.
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
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

# Default judge model — always Anthropic for consistent rubric scoring across providers
DEFAULT_JUDGE_MODEL = os.environ.get('JUDGE_MODEL', 'claude-haiku-4-5-20251001')

JUDGE_SYSTEM = """\
You are a strict evaluator scoring AI design-feedback outputs. Do not reward verbosity.
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
  "rationale": "<one sentence per dimension, pipe-separated>"
}
"""

# Per-provider rate-limit delays (seconds between calls within the same provider thread)
PROVIDER_DELAYS = {
    'claude':   12,   # Anthropic: conservative
    'gemini':   30,   # Google: longer delay to avoid 503 overload errors
    'openai':   8,    # OpenAI: generous limits on gpt-4 class
    'xai':      10,   # xAI Grok: moderate
    'mistral':  30,   # Mistral: strict rate limits — do not lower
    'deepseek': 15,   # DeepSeek: conservative (lower rate limits)
}

# Per-provider output token limits.
# Gemini MUST be 8192: the system-prompt prepend adds ~150 tokens of routing preamble
# before the actual answer content starts. With max_tokens=2000, Gemini runs out
# after the preamble and truncates mid-sentence. All 9 truncated outputs in the
# batch run were caused by this.
PROVIDER_MAX_TOKENS = {
    'claude':   4096,
    'gemini':   8192,  # High — system-prompt prepend eats ~150 preamble tokens
    'openai':   4096,
    'xai':      4096,
    'mistral':  4096,
    'deepseek': 4096,
}

# Default models per provider
DEFAULT_MODELS = {
    'claude':   'claude-sonnet-4-6',
    'gemini':   'gemini-2.5-flash',  # Flash is reliable; use --models gemini=gemini-2.5-pro-preview-05-06 for Pro
                                       # NOTE: gemini-2.5-pro requires thinking_budget=0 or responses score near-zero
    'openai':   'gpt-4.1',
    'xai':      'grok-3-fast',
    'mistral':  'mistral-large-latest',
    'deepseek': 'deepseek-chat',   # requires balance at platform.deepseek.com
}


# ── Thread-safe progress printer ──────────────────────────────────────────

_print_lock = threading.Lock()

def tprint(*args, **kwargs):
    """Thread-safe print."""
    with _print_lock:
        print(*args, **kwargs, flush=True)


# ── Provider adapters ──────────────────────────────────────────────────────

def call_anthropic(prompt: str, system: str | None, model: str, max_tokens: int = 4096,
                   max_retries: int = 6) -> tuple[str, float]:
    """Anthropic adapter with exponential backoff for rate-limit (429) and overload (529) errors.

    HTTP 402 (real billing error) is re-raised immediately without retry so the
    caller can distinguish genuine credit exhaustion from a transient rate limit.
    Using explicit anthropic exception types avoids the false-positive that
    'billing' in str(exc).lower() caused -- Anthropic 429 messages sometimes
    say 'billing tier' and were wrongly classified as credit failures.
    """
    import anthropic
    import random
    client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
    kw: dict = {'model': model, 'max_tokens': max_tokens, 'messages': [{'role': 'user', 'content': prompt}]}
    if system:
        kw['system'] = system
    t0 = time.monotonic()
    last_exc: Exception | None = None
    for attempt in range(max_retries):
        try:
            msg = client.messages.create(**kw)
            return ''.join(b.text for b in msg.content if hasattr(b, 'text')), round(time.monotonic() - t0, 2)
        except anthropic.RateLimitError as exc:
            # 429 -- backoff and retry; do NOT treat as billing error
            last_exc = exc
            if attempt < max_retries - 1:
                wait = (2 ** (attempt + 1)) + random.random()
                tprint(f'    [claude rate limited] backing off {wait:.1f}s (attempt {attempt+1}/{max_retries})...')
                time.sleep(wait)
                continue
            raise
        except anthropic.APIStatusError as exc:
            last_exc = exc
            if exc.status_code == 402:
                raise  # Real billing error -- re-raise immediately, no retry
            if exc.status_code in (500, 529) and attempt < max_retries - 1:
                wait = (2 ** (attempt + 1)) + random.random()
                label = 'overloaded' if exc.status_code == 529 else 'server error'
                tprint(f'    [claude {label}] backing off {wait:.1f}s (attempt {attempt+1}/{max_retries})...')
                time.sleep(wait)
                continue
            raise
    raise last_exc  # type: ignore[misc]


def _openai_compat(prompt: str, system: str | None, model: str, max_tokens: int,
                   api_key: str, base_url: str | None = None,
                   max_retries: int = 6) -> tuple[str, float]:
    """Shared adapter for any OpenAI-compatible API (OpenAI, xAI, DeepSeek).

    Includes retry logic with exponential backoff for transient JSON parse errors
    (HTTP 400) and rate-limit errors (HTTP 429). Large system prompts are
    sanitised to plain UTF-8 before sending to avoid serialisation edge cases.
    """
    from openai import OpenAI, APIStatusError, APIConnectionError
    kw: dict = {'api_key': api_key, 'max_retries': 0}  # handle retries ourselves
    if base_url:
        kw['base_url'] = base_url
    client = OpenAI(**kw)
    messages = []
    if system:
        # Sanitise: encode to UTF-8 and back to strip surrogate chars that break JSON
        safe_system = system.encode('utf-8', errors='replace').decode('utf-8')
        messages.append({'role': 'system', 'content': safe_system})
    messages.append({'role': 'user', 'content': prompt})
    t0 = time.monotonic()
    import random

    last_exc = None
    for attempt in range(max_retries):
        try:
            r = client.chat.completions.create(model=model, messages=messages, max_tokens=max_tokens)
            return r.choices[0].message.content or '', round(time.monotonic() - t0, 2)
        except APIStatusError as exc:
            last_exc = exc
            code = exc.status_code

            if code == 402:
                raise RuntimeError(
                    f"Billing error ({code}): insufficient balance. "
                    "Top up credits at the provider dashboard and retry."
                ) from exc

            # Randomized exponential backoff for all retryable errors.
            # Formula: 2^attempt seconds + random jitter (0.0–1.0s)
            # Attempt 0 → ~2s, attempt 1 → ~4s, attempt 2 → ~8s, attempt 3 → ~16s
            # Jitter prevents all threads hitting the server at the same moment.
            if code in (400, 422, 429, 500, 503) and attempt < max_retries - 1:
                wait = (2 ** (attempt + 1)) + random.random()
                label = {429: 'rate limited', 503: 'overloaded', 500: 'server error'}.get(code, f'error {code}')
                tprint(f"    [{label}] backing off {wait:.1f}s (attempt {attempt+1}/{max_retries})...")
                time.sleep(wait)
                continue

            raise
        except APIConnectionError as exc:
            last_exc = exc
            if attempt < max_retries - 1:
                wait = (2 ** (attempt + 1)) + random.random()
                tprint(f"    [connection error] backing off {wait:.1f}s (attempt {attempt+1}/{max_retries})...")
                time.sleep(wait)
                continue
            raise
    raise last_exc


def call_openai(prompt: str, system: str | None, model: str, max_tokens: int = 4096) -> tuple[str, float]:
    return _openai_compat(prompt, system, model, max_tokens, os.environ['OPENAI_API_KEY'])


def call_xai(prompt: str, system: str | None, model: str, max_tokens: int = 4096) -> tuple[str, float]:
    return _openai_compat(prompt, system, model, max_tokens,
                          os.environ['XAI_API_KEY'], base_url='https://api.x.ai/v1')


def call_deepseek(prompt: str, system: str | None, model: str, max_tokens: int = 4096) -> tuple[str, float]:
    return _openai_compat(prompt, system, model, max_tokens,
                          os.environ['DEEPSEEK_API_KEY'], base_url='https://api.deepseek.com/v1')


# Gemini is called via Google's official OpenAI-compatible endpoint.
# This is simpler, more reliable, and avoids two critical issues with the google SDK:
#   1. google.generativeai SDK version incompatibilities with newer models
#   2. gemini-2.5-pro has thinking mode ON by default — the old SDK returns thinking
#      tokens mixed into r.text, producing near-zero validator scores because the
#      response is chain-of-thought instead of the actual answer.
# The OpenAI-compat endpoint returns only the final text in choices[0].message.content,
# handles system prompts natively (no size limit workaround needed), and uses the
# same retry/error logic already in _openai_compat.
GEMINI_OPENAI_BASE = 'https://generativelanguage.googleapis.com/v1beta/openai/'

def call_gemini(prompt: str, system: str | None, model: str, max_tokens: int = 8192) -> tuple[str, float]:
    # Uses Google's OpenAI-compatible endpoint — no google-generativeai SDK needed.
    # thinking_config is NOT supported on this endpoint (native SDK only), so we
    # don't pass it. Flash models don't think by default; Pro models return thinking
    # in a separate field that doesn't appear in choices[0].message.content.
    from openai import OpenAI
    client = OpenAI(
        api_key=os.environ['GOOGLE_API_KEY'],
        base_url=GEMINI_OPENAI_BASE,
    )
    messages = []
    if system:
        safe_system = system.encode('utf-8', errors='replace').decode('utf-8')
        messages.append({'role': 'system', 'content': safe_system})
    messages.append({'role': 'user', 'content': prompt})
    t0 = time.monotonic()
    try:
        r = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
        )
        return r.choices[0].message.content or '', round(time.monotonic() - t0, 2)
    except Exception as exc:
        err = str(exc)
        if '404' in err or 'not found' in err.lower() or 'NOT_FOUND' in err:
            raise RuntimeError(
                f"Gemini model '{model}' not found. Try one of these known-good names:\n"
                f"  gemini-2.5-flash\n"
                f"  gemini-2.5-flash-preview-04-17\n"
                f"  gemini-2.0-flash\n"
                f"Override with: --models gemini=<model-name>"
            ) from exc
        raise


def call_mistral(prompt: str, system: str | None, model: str, max_tokens: int = 4096) -> tuple[str, float]:
    # Mistral exposes a fully OpenAI-compatible endpoint at api.mistral.ai/v1.
    # Using the openai package directly is more reliable than the mistralai SDK,
    # which has breaking changes across versions.
    return _openai_compat(
        prompt, system, model, max_tokens,
        api_key=os.environ['MISTRAL_API_KEY'],
        base_url='https://api.mistral.ai/v1',
    )


CALL_FN = {
    'claude':   call_anthropic,
    'gemini':   call_gemini,
    'openai':   call_openai,
    'xai':      call_xai,
    'mistral':  call_mistral,
    'deepseek': call_deepseek,
}

REQUIRED_ENV = {
    'claude':   'ANTHROPIC_API_KEY',
    'gemini':   'GOOGLE_API_KEY',
    'openai':   'OPENAI_API_KEY',
    'xai':      'XAI_API_KEY',
    'mistral':  'MISTRAL_API_KEY',
    'deepseek': 'DEEPSEEK_API_KEY',
}


# ── Rubric judge (always Anthropic for consistency) ───────────────────────

def judge_rubric(prompt: str, response: str) -> dict:
    judge_prompt = (
        f'USER PROMPT:\n{prompt}\n\n'
        f'AI RESPONSE TO SCORE:\n{response}\n\n'
        'Score the response on the five dimensions.'
    )
    try:
        text, _ = call_anthropic(judge_prompt, JUDGE_SYSTEM, DEFAULT_JUDGE_MODEL, max_tokens=400)
        text = text.strip().removeprefix('```json').removeprefix('```').removesuffix('```').strip()
        scores = json.loads(text)
        for dim in RUBRIC_DIMS:
            scores[dim] = max(1, min(5, int(scores.get(dim, 1))))
        return scores
    except Exception as exc:
        return {dim: 0 for dim in RUBRIC_DIMS} | {'rationale': f'judge_error: {exc}'}


def gate_rubric(rubric: dict) -> tuple[bool, float | None]:
    dim_scores = [rubric.get(d, 0) for d in RUBRIC_DIMS if rubric.get(d, 0) > 0]
    if not dim_scores:
        return True, None  # No rubric data — don't penalise
    mean = round(sum(dim_scores) / len(dim_scores), 2)
    passed = (mean >= RUBRIC_GATE_MEAN) and (min(dim_scores) >= RUBRIC_GATE_MIN_DIM)
    return passed, mean


def compute_composite(validator_score: int | None, rubric_mean: float | None) -> tuple[float, bool]:
    """Compute a single composite score (0-100) from validator and rubric scores.

    Formula: composite = (validator_score * 0.60) + (rubric_mean * 20 * 0.40)
    - validator_score: 0-100 (structural compliance)
    - rubric_mean: 0-5, scaled to 0-100 by * 20 (holistic quality)
    - 60/40 split: validator carries more weight (contract compliance)
    - Pass threshold: composite >= 70

    Fallback: if rubric_mean is None, composite = validator_score only.
    Returns (composite_score, composite_pass).
    """
    COMPOSITE_PASS_THRESHOLD = 70.0
    if validator_score is None:
        return 0.0, False
    if rubric_mean is None:
        # No rubric data — use validator score alone, marked with partial flag
        composite = float(validator_score)
    else:
        composite = round((validator_score * 0.60) + (rubric_mean * 20.0 * 0.40), 1)
    return composite, composite >= COMPOSITE_PASS_THRESHOLD


# ── Per-provider worker ───────────────────────────────────────────────────

def run_provider(
    provider_id: str,
    model: str,
    tests: list[dict],
    system_prompt: str | None,
    out_dir: Path,
    skip_rubric: bool,
    mode: str,
) -> dict:
    """
    Run all tests for one provider sequentially.
    Designed to be called in a thread — one thread per provider.
    Returns a summary dict for this provider.
    """
    call_fn = CALL_FN[provider_id]
    delay = PROVIDER_DELAYS.get(provider_id, 12)
    provider_dir = out_dir / provider_id
    provider_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []
    total = len(tests)

    for i, test in enumerate(tests, 1):
        # Resolve prompt text -- tests may use inline full_prompt or a prompt_file reference
        if 'full_prompt' in test:
            prompt = test['full_prompt']
        elif 'prompt_file' in test:
            prompt_path = ROOT / test['prompt_file']
            if not prompt_path.exists():
                tprint(f'  [{provider_id:9}] SKIP {test["id"]}: prompt_file not found: {prompt_path}')
                results.append({'test_id': test['id'], 'task': test.get('task', ''),
                                 'error': f'prompt_file not found: {test["prompt_file"]}'})
                continue
            prompt = prompt_path.read_text(encoding='utf-8').strip()
        else:
            tprint(f'  [{provider_id:9}] SKIP {test["id"]}: no full_prompt or prompt_file key')
            results.append({'test_id': test['id'], 'task': test.get('task', ''),
                             'error': 'missing full_prompt and prompt_file'})
            continue
        task_id = test['task']
        tprint(f'  [{provider_id:9}] {i}/{total} {test["id"]}…')

        # API call with error handling — use per-provider token limit
        max_tok = PROVIDER_MAX_TOKENS.get(provider_id, 4096)
        try:
            response, latency = call_fn(prompt, system_prompt, model, max_tok)
        except Exception as exc:
            err_msg = str(exc)
            # Detect genuine billing/credit errors without false-positives.
            # The old 'billing' in err_msg.lower() check triggered on Anthropic
            # 429 rate-limit messages that say "billing tier" -- those are rate
            # limits, not credit failures. Now we check the HTTP status code
            # directly (402) or the provider-specific error text only.
            is_billing_error = (
                '402' in err_msg
                or 'Insufficient Balance' in err_msg
                or 'credit balance is too low' in err_msg.lower()
                or 'insufficient_quota' in err_msg.lower()
            )
            if is_billing_error:
                tprint(f'  [{provider_id:9}] BILLING ERROR on {test["id"]}: '
                       f'Account has insufficient credits. Add balance at the {provider_id} dashboard.')
                # Stop all tests for this provider — all will fail the same way
                for remaining in tests[i-1:]:
                    results.append({
                        'test_id': remaining['id'], 'task': remaining['task'],
                        'error': f'Skipped: billing error on {provider_id}. Add credits and retry.'
                    })
                break
            elif '401' in err_msg or 'Unauthorized' in err_msg or 'invalid_api_key' in err_msg.lower():
                tprint(f'  [{provider_id:9}] AUTH ERROR on {test["id"]}: '
                       f'API key rejected. Check {REQUIRED_ENV[provider_id]} is correct.')
                for remaining in tests[i-1:]:
                    results.append({
                        'test_id': remaining['id'], 'task': remaining['task'],
                        'error': f'Skipped: auth error on {provider_id}. Check API key.'
                    })
                break
            else:
                tprint(f'  [{provider_id:9}] ERROR on {test["id"]}: {exc}')
                results.append({'test_id': test['id'], 'task': task_id, 'error': str(exc)})
                time.sleep(delay)
                continue

        # Save raw response
        out_file = provider_dir / f'{test["id"]}_{mode}.md'
        out_file.write_text(response, encoding='utf-8')

        # Static validation
        validation = validate_output(task_id, prompt, response, model_hint=model)
        validator_pass = validation['decision'] in ('PASS', 'AUTO_REVISE')

        # Rubric scoring (always via Anthropic judge for cross-provider comparability)
        rubric = {}
        rubric_gate_pass = True
        rubric_mean = None
        if not skip_rubric:
            try:
                rubric = judge_rubric(prompt, response)
                rubric_gate_pass, rubric_mean = gate_rubric(rubric)
            except Exception as exc:
                tprint(f'  [{provider_id:9}] rubric error on {test["id"]}: {exc}')

        passed = validator_pass or rubric_gate_pass
        passed_by = 'validator' if validator_pass else ('rubric' if rubric_gate_pass else 'none')

        # Detect headings that didn't match for alias drift analysis
        unmatched_headings = [
            iss['detail'] for iss in validation['issues']
            if iss['id'] == 'missing_section'
        ]
        vocab_warnings = [
            w['detail'] for w in validation.get('warnings', [])
            if w['id'] == 'missing_section_heading'
        ]

        composite_score, composite_pass = compute_composite(validation['score'], rubric_mean)
        passed = composite_pass
        passed_by = (
            'validator' if validator_pass and rubric_gate_pass else
            'validator' if validator_pass and not rubric_gate_pass else
            'rubric'    if not validator_pass and rubric_gate_pass else
            'composite' if composite_pass else
            'none'
        )
        rubric_decisive = (not validator_pass) and composite_pass

        status = 'PASS' if passed else 'FAIL'
        rub_flag = ' [RUB]' if rubric_decisive else ''
        tprint(
            f'  [{provider_id:9}] {status} {test["id"]}  '
            f'composite={composite_score:.0f}  val={validation["score"]}  rub={rubric_mean or "-"}{rub_flag}'
        )

        results.append({
            'test_id':          test['id'],
            'title':            test['title'],
            'task':             task_id,
            'mode':             mode,
            'validator_decision': validation['decision'],
            'validator_score':  validation['score'],
            'validator_pass':   validator_pass,
            'rubric_mean':      rubric_mean,
            'rubric_gate_pass': rubric_gate_pass,
            'composite_score':  composite_score,
            'composite_pass':   composite_pass,
            'rubric_decisive':  rubric_decisive,
            'passed':           passed,
            'passed_by':        passed_by,
            'latency_seconds':  latency,
            'issues':           validation['issues'],
            'warnings':         validation.get('warnings', []),
            'unmatched_sections': unmatched_headings,
            'vocab_warnings':   vocab_warnings,
            'rubric':           rubric,
            'output_file':      str(out_file.relative_to(ROOT)),
        })

        time.sleep(delay)

    # Build provider summary
    valid = [r for r in results if 'error' not in r]
    pass_count = sum(1 for r in valid if r['passed'])
    pass_rate = round(pass_count / len(valid), 3) if valid else 0.0

    composites = [r['composite_score'] for r in valid if r.get('composite_score') is not None]
    avg_composite = round(statistics.mean(composites), 1) if composites else None

    rubric_means_agg: dict[str, float | None] = {}
    for dim in RUBRIC_DIMS:
        vals = [r['rubric'].get(dim, 0) for r in valid if r.get('rubric') and r['rubric'].get(dim, 0) > 0]
        rubric_means_agg[dim] = round(statistics.mean(vals), 2) if vals else None

    provider_summary = {
        'provider':          provider_id,
        'model':             model,
        'mode':              mode,
        'tests_run':         len(valid),
        'errors':            len(results) - len(valid),
        'pass_count':        pass_count,
        'pass_rate':         pass_rate,
        'gate_passed':           pass_rate >= CROSS_MODEL_GATE,
        'avg_composite':         avg_composite,
        'rubric_means':          rubric_means_agg,
        'passed_by_rubric_only': sum(1 for r in valid if r.get('passed_by') == 'rubric'),
        'rubric_decisive_count': sum(1 for r in valid if r.get('rubric_decisive')),
        'results':           results,
    }

    summary_path = provider_dir / 'summary.json'
    summary_path.write_text(json.dumps(provider_summary, indent=2))
    return provider_summary


# ── Comparative report ────────────────────────────────────────────────────

def build_comparative_report(
    run_id: str,
    providers: list[str],
    summaries: dict[str, dict],
    tests: list[dict],
    mode: str,
) -> dict:
    """Build a cross-provider comparison report."""

    # Per-test breakdown
    test_comparison = []
    for test in tests:
        tid = test['id']
        row = {'test_id': tid, 'title': test['title'], 'task': test['task'], 'providers': {}}
        for p in providers:
            summary = summaries.get(p, {})
            result = next((r for r in summary.get('results', []) if r.get('test_id') == tid and 'error' not in r), None)
            if result:
                row['providers'][p] = {
                    'passed':           result['passed'],
                    'passed_by':        result['passed_by'],
                    'composite_score':  result.get('composite_score'),
                    'rubric_decisive':  result.get('rubric_decisive', False),
                    'validator_score':  result['validator_score'],
                    'validator_decision': result['validator_decision'],
                    'rubric_mean':      result['rubric_mean'],
                    'latency_seconds':  result['latency_seconds'],
                    'issues':           [i['id'] for i in result.get('issues', [])],
                }
            else:
                row['providers'][p] = {'passed': None, 'error': True}

        passed_providers = [p for p in providers if row['providers'].get(p, {}).get('passed') is True]
        failed_providers = [p for p in providers if row['providers'].get(p, {}).get('passed') is False]
        row['all_passed'] = len(passed_providers) == len(providers)
        row['all_failed'] = len(failed_providers) == len(providers)
        row['split'] = not row['all_passed'] and not row['all_failed']
        row['passed_count'] = len(passed_providers)
        test_comparison.append(row)

    # Ranking by pass rate
    ranking = sorted(
        [{'provider': p, **{k: v for k, v in summaries[p].items() if k != 'results'}}
         for p in providers if p in summaries],
        key=lambda x: (x.get('avg_composite') or 0, x['pass_rate']),
        reverse=True,
    )

    # Alias drift candidates — sections that hard-failed across 2+ providers
    alias_candidates: dict[str, list[str]] = {}
    for p in providers:
        for r in summaries.get(p, {}).get('results', []):
            for section_detail in r.get('unmatched_sections', []):
                # Extract section name from "missing section: X"
                if 'missing section: ' in section_detail:
                    sec = section_detail.split('missing section: ', 1)[1]
                    alias_candidates.setdefault(sec, [])
                    if p not in alias_candidates[sec]:
                        alias_candidates[sec].append(p)

    persistent_gaps = {sec: provs for sec, provs in alias_candidates.items() if len(provs) >= 2}

    # Cross-provider rubric comparison
    rubric_comparison: dict[str, dict[str, float | None]] = {}
    for dim in RUBRIC_DIMS:
        rubric_comparison[dim] = {}
        for p in providers:
            rubric_comparison[dim][p] = summaries.get(p, {}).get('rubric_means', {}).get(dim)

    return {
        'run_id':           run_id,
        'run_date':         datetime.now(timezone.utc).isoformat(),
        'mode':             mode,
        'providers_tested': providers,
        'tests_run':        len(tests),
        'cross_model_gate': CROSS_MODEL_GATE,
        'ranking':          ranking,
        'test_comparison':  test_comparison,
        'rubric_comparison': rubric_comparison,
        'alias_drift_candidates': persistent_gaps,
        'consistency': {
            'all_passed':  sum(1 for t in test_comparison if t['all_passed']),
            'all_failed':  sum(1 for t in test_comparison if t['all_failed']),
            'split':       sum(1 for t in test_comparison if t['split']),
        },
    }


def render_html_report(report: dict, path: Path) -> None:
    """Render the comparative report as a self-contained HTML file.

    Scoring display uses composite_score (0-100) from 60/40 validator+rubric blend.
    Color is a 5-level gradient — never binary — so a 22/100 is always red regardless
    of how it passed. Rubric-decisive results show a RUB badge (no emojis).
    """
    providers = report["providers_tested"]
    tests = report["test_comparison"]
    ranking = report["ranking"]

    def pct(v):
        return f"{v:.0%}" if v is not None else "—"

    def score_color(score):
        """Return CSS class for 5-level gradient based on composite score."""
        if score is None:
            return "c-unknown"
        if score >= 90:
            return "c-great"
        if score >= 75:
            return "c-good"
        if score >= 70:
            return "c-marginal"
        if score >= 55:
            return "c-weak"
        return "c-fail"

    def composite_cell(row, provider):
        pd = row["providers"].get(provider, {})
        if pd.get("error") or pd.get("passed") is None:
            return "<td class=\"c-err\">ERR</td>"
        comp = pd.get("composite_score")
        val = pd.get("validator_score", "")
        rub = pd.get("rubric_mean")
        decisive = pd.get("rubric_decisive", False)
        partial = (rub is None)

        score_str = f"{comp:.0f}" if comp is not None else "—"
        color_cls = score_color(comp)

        # Sub-line: val and rub breakdown
        rub_str = f"{rub:.1f}" if rub is not None else "—"
        sub = f"v{val} · r{rub_str}"
        if partial:
            sub += " †"

        # RUB badge — text pill, no emoji
        badge = '<span class=\"rub-badge\">RUB</span>' if decisive else ""

        return (
            f"<td class=\"{color_cls}\">"
            f"<span class=\"comp-score\">{score_str}</span>"
            f"{badge}"
            f"<br><span class=\"sub-scores\">{sub}</span>"
            f"</td>"
        )

    provider_headers = "".join(f"<th>{p}</th>" for p in providers)
    test_rows = ""
    for t in tests:
        cells = "".join(composite_cell(t, p) for p in providers)
        all_pass = t.get("all_passed")
        all_fail = t.get("all_failed")
        consistency = "all" if all_pass else ("none" if all_fail else "split")
        con_label = "✓" if all_pass else ("✗" if all_fail else "~")
        test_rows += (
            f"<tr>"
            f"<td class=\"task\">{t['test_id']}<br><small>{t['task']}</small></td>"
            f"{cells}"
            f"<td class=\"con con-{consistency}\">{con_label}</td>"
            f"</tr>\n"
        )

    ranking_rows = ""
    for i, r in enumerate(ranking, 1):
        gate = "PASS" if r.get("gate_passed") else "FAIL"
        comp = f"{r['avg_composite']:.0f}" if r.get("avg_composite") else "—"
        decisive = r.get("rubric_decisive_count", 0)
        ranking_rows += (
            f"<tr>"
            f"<td>{i}</td>"
            f"<td><strong>{r['provider']}</strong></td>"
            f"<td>{r['model']}</td>"
            f"<td class=\"comp-col\">{comp}</td>"
            f"<td>{pct(r.get('pass_rate'))} ({r.get('pass_count','—')}/{r.get('tests_run','—')})</td>"
            f"<td>{decisive}</td>"
            f"<td class=\"gate-{'pass' if r.get('gate_passed') else 'fail'}\">{gate}</td>"
            f"</tr>\n"
        )

    alias_rows = ""
    for sec, provs in report.get("alias_drift_candidates", {}).items():
        alias_rows += f"<tr><td><code>{sec}</code></td><td>{', '.join(provs)}</td><td>{len(provs)}</td></tr>\n"
    if not alias_rows:
        alias_rows = "<tr><td colspan=\"3\"><em>No persistent gaps found</em></td></tr>"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DesignPilot Batch Report — {report["run_id"]}</title>
<style>
  :root {{
    --great:    #d4f4e2; --great-fg:   #0a5c2e;
    --good:     #e6f4ea; --good-fg:    #1a7a3a;
    --marginal: #fef9e7; --marginal-fg:#7d6008;
    --weak:     #fdebd0; --weak-fg:    #935116;
    --fail:     #fdf0f0; --fail-fg:    #b33333;
    --err:      #fffbe6; --err-fg:     #856404;
    --border:   #e0e0e0;
  }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: system-ui, -apple-system, sans-serif; margin: 2rem auto;
         max-width: 1200px; color: #1a1a1a; font-size: 13px; line-height: 1.4; }}
  h1 {{ font-size: 1.35rem; margin: 0 0 0.2rem; }}
  h2 {{ font-size: 1rem; margin: 2rem 0 0.6rem; border-bottom: 1px solid var(--border);
        padding-bottom: 0.3rem; text-transform: uppercase; letter-spacing: 0.04em; color: #444; }}
  .meta {{ color: #777; font-size: 0.82rem; margin-bottom: 1.5rem; }}
  table {{ border-collapse: collapse; width: 100%; margin-bottom: 1.5rem; }}
  th, td {{ padding: 0.4rem 0.55rem; border: 1px solid var(--border); text-align: center; vertical-align: top; }}
  th {{ background: #f8f8f8; font-weight: 600; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.03em; }}
  td.task {{ text-align: left; min-width: 130px; font-size: 0.82rem; }}
  td.task small {{ color: #888; display: block; }}
  /* Composite score gradient cells */
  td.c-great   {{ background: var(--great);    color: var(--great-fg); }}
  td.c-good    {{ background: var(--good);     color: var(--good-fg); }}
  td.c-marginal{{ background: var(--marginal); color: var(--marginal-fg); }}
  td.c-weak    {{ background: var(--weak);     color: var(--weak-fg); }}
  td.c-fail    {{ background: var(--fail);     color: var(--fail-fg); }}
  td.c-err     {{ background: var(--err);      color: var(--err-fg); }}
  td.c-unknown {{ background: #f5f5f5; color: #999; }}
  .comp-score {{ font-size: 1.1rem; font-weight: 700; display: block; line-height: 1.2; }}
  .sub-scores {{ font-size: 0.7rem; opacity: 0.75; display: block; margin-top: 1px; }}
  .rub-badge {{
    display: inline-block; font-size: 0.6rem; font-family: monospace;
    font-weight: 700; letter-spacing: 0.06em; color: #555;
    background: rgba(0,0,0,0.08); border-radius: 3px;
    padding: 0 3px; margin-left: 3px; vertical-align: middle;
  }}
  /* Consistency column */
  td.con {{ font-weight: 700; }}
  td.con-all  {{ color: var(--great-fg); }}
  td.con-none {{ color: var(--fail-fg); }}
  td.con-split{{ color: #777; }}
  /* Ranking table */
  td.comp-col {{ font-weight: 700; font-size: 1rem; }}
  td.gate-pass {{ color: var(--great-fg); font-weight: 700; }}
  td.gate-fail {{ color: var(--fail-fg); font-weight: 700; }}
  /* Legend */
  .legend {{ display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 0.75rem; font-size: 0.8rem; }}
  .legend-item {{ display: flex; align-items: center; gap: 0.3rem; }}
  .legend-swatch {{ width: 14px; height: 14px; border-radius: 3px; border: 1px solid rgba(0,0,0,0.1); }}
  .note {{ font-size: 0.78rem; color: #888; margin-bottom: 0.5rem; }}
  .gap-table td {{ text-align: left; }}
  .summary-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem; margin-bottom: 1.5rem; }}
  .stat-card {{ border: 1px solid var(--border); border-radius: 6px; padding: 0.75rem 1rem; }}
  .stat-card .number {{ font-size: 1.8rem; font-weight: 700; line-height: 1; }}
  .stat-card .label {{ color: #777; font-size: 0.78rem; margin-top: 0.2rem; }}
</style>
</head>
<body>
<h1>DesignPilot Cross-Model Batch Report</h1>
<div class="meta">
  Run: <strong>{report["run_id"]}</strong> &nbsp;|&nbsp;
  {report["run_date"][:19].replace("T"," ")} UTC &nbsp;|&nbsp;
  Mode: {report["mode"]} &nbsp;|&nbsp;
  Gate: {pct(report["cross_model_gate"])}
</div>

<div class="summary-grid">
  <div class="stat-card">
    <div class="number">{report["consistency"]["all_passed"]}/{report["tests_run"]}</div>
    <div class="label">Tests all providers passed</div>
  </div>
  <div class="stat-card">
    <div class="number">{report["consistency"]["split"]}/{report["tests_run"]}</div>
    <div class="label">Tests with split results</div>
  </div>
  <div class="stat-card">
    <div class="number">{len(report.get("alias_drift_candidates", {}))}</div>
    <div class="label">Alias gaps (2+ providers)</div>
  </div>
</div>

<h2>Provider Ranking</h2>
<table>
  <tr><th>#</th><th>Provider</th><th>Model</th><th>Composite avg</th><th>Pass rate</th><th>RUB-decisive</th><th>Gate</th></tr>
  {ranking_rows}
</table>

<h2>Per-Test Results</h2>
<div class="legend">
  <div class="legend-item"><div class="legend-swatch" style="background:var(--great)"></div> 90–100 strong pass</div>
  <div class="legend-item"><div class="legend-swatch" style="background:var(--good)"></div> 75–89 pass</div>
  <div class="legend-item"><div class="legend-swatch" style="background:var(--marginal)"></div> 70–74 marginal pass</div>
  <div class="legend-item"><div class="legend-swatch" style="background:var(--weak)"></div> 55–69 weak fail</div>
  <div class="legend-item"><div class="legend-swatch" style="background:var(--fail)"></div> 0–54 fail</div>
</div>
<p class="note">Score = composite (60% validator + 40% rubric). Sub-line: v=validator score, r=rubric mean. <strong>RUB</strong> badge = rubric was the decisive factor. † = rubric unavailable, validator score used alone.</p>
<table>
  <tr><th>Test</th>{provider_headers}<th>All</th></tr>
  {test_rows}
</table>

<h2>Persistent Alias Gaps</h2>
<p class="note">Sections that hard-failed on 2+ providers — candidates for section_aliases.json update.</p>
<table class="gap-table">
  <tr><th>Section name</th><th>Failed providers</th><th>Count</th></tr>
  {alias_rows}
</table>

<h2>Raw data</h2>
<p class="note">Full structured data in <code>comparative_report.json</code> alongside this file.</p>
</body>
</html>"""

    path.write_text(html, encoding="utf-8")
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--providers', nargs='*', default=list(DEFAULT_MODELS.keys()),
                        help='Providers to run (default: all). Options: claude gemini openai xai mistral deepseek')
    parser.add_argument('--models', nargs='*', metavar='PROVIDER=MODEL',
                        help='Override model per provider, e.g. --models claude=claude-opus-4-6 openai=gpt-4o')
    parser.add_argument('--test-ids', nargs='*', help='Run only these test IDs (e.g. cm-01 cm-03)')
    parser.add_argument('--run-id', default=f"batch-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M')}")
    parser.add_argument('--skip-rubric', action='store_true', help='Skip rubric scoring (faster)')
    parser.add_argument('--baseline', action='store_true', help='Run without DesignPilot system prompt')
    parser.add_argument('--max-workers', type=int, default=6, help='Max parallel threads (default: 6 = one per provider)')
    parser.add_argument('--gate', action='store_true', help='Exit 1 if any provider falls below cross-model gate')
    parser.add_argument('--context', default='', help='Brief description of what this run is testing')
    parser.add_argument('--known-issues', default='', help='Comma-separated list of known infrastructure issues that may affect scores')
    parser.add_argument('--diagnostic', action='store_true', help='Mark this as a diagnostic run (not a quality signal)')
    args = parser.parse_args()

    # Resolve model overrides
    models = dict(DEFAULT_MODELS)
    if args.models:
        for spec in args.models:
            if '=' in spec:
                p, m = spec.split('=', 1)
                models[p] = m

    # Check API keys and filter providers
    providers_to_run: list[str] = []
    skipped: list[str] = []
    for p in args.providers:
        if p not in CALL_FN:
            print(f'WARNING: Unknown provider "{p}", skipping.')
            continue
        env_key = REQUIRED_ENV[p]
        if not os.environ.get(env_key):
            skipped.append(f'{p} (missing {env_key})')
        else:
            providers_to_run.append(p)

    if not providers_to_run:
        print('ERROR: No providers have API keys configured. Set at least one of:')
        for p, k in REQUIRED_ENV.items():
            print(f'  {k}  ({p})')
        raise SystemExit(1)

    if skipped:
        print(f'Skipping providers with no API key: {", ".join(skipped)}')

    # Judge key check
    if not args.skip_rubric and not os.environ.get('ANTHROPIC_API_KEY'):
        print('WARNING: ANTHROPIC_API_KEY not set. Rubric scoring requires Anthropic. Using --skip-rubric.')
        args.skip_rubric = True

    # Load suite and system prompt
    suite = json.loads(SUITE_PATH.read_text())
    tests = suite['tests']
    if args.test_ids:
        tests = [t for t in tests if t['id'] in set(args.test_ids)]
    if not tests:
        raise SystemExit('No tests selected.')

    system_prompt = None if args.baseline else DEPLOY_PATH.read_text(encoding='utf-8')
    mode = 'baseline' if args.baseline else 'pack'

    out_dir = OUTPUTS_DIR / args.run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    # Print run header
    print(f'\n{"─" * 60}')
    print(f'DesignPilot Parallel Batch Run')
    print(f'Run ID:    {args.run_id}')
    print(f'Providers: {", ".join(providers_to_run)}')
    print(f'Tests:     {", ".join(t["id"] for t in tests)}')
    print(f'Rubric:    {"enabled (Anthropic judge)" if not args.skip_rubric else "disabled"}')
    print(f'Mode:      {mode}')
    print(f'{"─" * 60}\n')

    start = time.monotonic()

    # Launch all providers in parallel
    summaries: dict[str, dict] = {}
    max_workers = min(args.max_workers, len(providers_to_run))

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {
            pool.submit(
                run_provider,
                provider_id=p,
                model=models[p],
                tests=tests,
                system_prompt=system_prompt,
                out_dir=out_dir,
                skip_rubric=args.skip_rubric,
                mode=mode,
            ): p
            for p in providers_to_run
        }

        for future in as_completed(futures):
            provider_id = futures[future]
            try:
                summary = future.result()
                summaries[provider_id] = summary
                gate_str = 'PASS' if summary['gate_passed'] else 'FAIL'
                tprint(
                    f'\n  ✓ [{provider_id}] finished — '
                    f'{summary["pass_count"]}/{summary["tests_run"]} passed '
                    f'({summary["pass_rate"]:.0%}) — gate: {gate_str}'
                )
            except Exception as exc:
                tprint(f'\n  ✗ [{provider_id}] thread crashed: {exc}')

    elapsed = round(time.monotonic() - start, 1)

    # Build and save comparative report
    report = build_comparative_report(args.run_id, providers_to_run, summaries, tests, mode)
    report_path = out_dir / 'comparative_report.json'
    report_path.write_text(json.dumps(report, indent=2))

    html_path = out_dir / 'comparative_report.html'
    try:
        render_html_report(report, html_path)
        html_str = f'  HTML report: {html_path}'
    except Exception as exc:
        html_str = f'  HTML report: failed ({exc})'

    # Print final summary table
    print(f'\n{"─" * 60}')
    print(f'BATCH COMPLETE  ({elapsed}s elapsed)')
    print(f'{"─" * 60}')
    print(f'  {"Provider":<12} {"Model":<28} {"Pass rate":<12} {"Gate"}')
    print(f'  {"─" * 58}')
    for r in report['ranking']:
        gate = '✓ PASS' if r.get('gate_passed') else '✗ FAIL'
        comp = f'{r["avg_composite"]:.0f}' if r.get('avg_composite') else '--'
        print(f'  {r["provider"]:<12} {r["model"]:<28} composite={comp:<5} {r.get("pass_rate", 0):.0%} ({r.get("pass_count","?")}/{r.get("tests_run","?")})  {gate}')

    print(f'\n  Consistency:')
    print(f'    All providers passed: {report["consistency"]["all_passed"]}/{report["tests_run"]} tests')
    print(f'    Split results:        {report["consistency"]["split"]}/{report["tests_run"]} tests')
    print(f'    All providers failed: {report["consistency"]["all_failed"]}/{report["tests_run"]} tests')

    if report.get('alias_drift_candidates'):
        print(f'\n  Alias gaps (2+ providers failed same section):')
        for sec, provs in report['alias_drift_candidates'].items():
            print(f'    "{sec}"  →  {", ".join(provs)}')

    print(f'\n  JSON report: {report_path}')
    print(f'{html_str}')
    print(f'{"─" * 60}\n')

    if args.gate:
        failed_providers = [r['provider'] for r in report['ranking'] if not r.get('gate_passed')]
        if failed_providers:
            print(f'GATE FAIL: {", ".join(failed_providers)} below {CROSS_MODEL_GATE:.0%} threshold', file=sys.stderr)
            raise SystemExit(1)
        print('GATE PASS: all providers met the cross-model threshold.')

    # Write run_context.json for batch history tracking
    pack_version = json.loads((ROOT / 'PACK_MANIFEST.json').read_text())['version']
    ctx = {
        'run_id': args.run_id,
        'written_at': datetime.now(timezone.utc).isoformat(),
        'purpose': args.context or f'Batch run {args.run_id}',
        'pack_version': pack_version,
        'is_diagnostic': args.diagnostic,
        'is_valid_quality_signal': not args.diagnostic,
        'known_issues': [i.strip() for i in args.known_issues.split(',') if i.strip()],
        'note': args.context,
    }
    run_out_dir = OUTPUTS_DIR / args.run_id
    (run_out_dir / 'run_context.json').write_text(json.dumps(ctx, indent=2))
    tprint(f'  Context: {run_out_dir / "run_context.json"}')

    # Write proof/benchmarks entry for release gate
    try:
        bench_dir = ROOT / 'proof' / 'benchmarks'
        bench_dir.mkdir(parents=True, exist_ok=True)
        bench_entry = {
            'run_id': args.run_id,
            'run_date': report.get('run_date', ''),
            'pack_version': pack_version,
            'providers_tested': report.get('providers_tested', []),
            'ranking': [
                {
                    'provider': r['provider'],
                    'avg_composite': r.get('avg_composite'),
                    'pass_rate': r.get('pass_rate'),
                    'gate_passed': r.get('gate_passed'),
                }
                for r in report.get('ranking', [])
            ],
            'tests_run': report.get('tests_run', 0),
            'cross_model_gate': report.get('cross_model_gate'),
        }
        bench_path = bench_dir / f'{args.run_id}-summary.json'
        bench_path.write_text(json.dumps(bench_entry, indent=2))
        tprint(f'  Benchmark: proof/benchmarks/{bench_path.name}')
        # Keep only last 10 benchmark files
        bench_files = sorted(bench_dir.glob('batch-*-summary.json'), reverse=True)
        for old_file in bench_files[10:]:
            old_file.unlink()
    except Exception as e:
        tprint(f'  Benchmark write skipped: {e}')

    # Auto-archive: promote older runs to compressed/minimal storage
    try:
        import subprocess
        archive_script = ROOT / 'scripts' / 'archive_batch_runs.py'
        if archive_script.exists():
            subprocess.run([sys.executable, str(archive_script)], check=False, capture_output=True)
            tprint('  Archive: older runs promoted to compressed storage.')
    except Exception:
        pass  # archiving is best-effort


if __name__ == '__main__':
    main()
