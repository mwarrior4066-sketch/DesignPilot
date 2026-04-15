#!/usr/bin/env python3
"""
check_alias_drift.py

Periodic alias drift monitor. Runs a small set of canary prompts against
a model, detects section headings not covered by current aliases, and writes
candidate entries to vocab_calibration_log.json for human review.

Run monthly or after any major model version release.

Usage:
    python scripts/check_alias_drift.py --provider openai --model gpt-4.1
    python scripts/check_alias_drift.py --provider anthropic --model claude-sonnet-4-6 --tasks ui_structure_critique layout_reconstruction_plan
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

ALIASES_PATH = ROOT / 'src' / 'schemas' / 'section_aliases.json'
CONTRACTS_PATH = ROOT / 'src' / 'schemas' / 'task_contracts.json'
CALIB_LOG_PATH = ROOT / 'src' / 'schemas' / 'vocab_calibration_log.json'
DEPLOY_PATH = ROOT / 'dist' / 'DESIGNPILOT_DEPLOY.md'

# Canary prompts per task — short enough to be cheap, substantive enough to produce headings
CANARY_PROMPTS = {
    'ui_structure_critique': 'Audit a SaaS dashboard login page. It has a centered form with email and password fields, a "Sign In" button, and a "Forgot password?" link. The button has low contrast and the form has no visible labels.',
    'layout_reconstruction_plan': 'Reconstruct the layout system from a 2019 brand PDF. The PDF has a 12-column grid, specific type scales, and a navy/gold palette. Some pages are scanned.',
    'frontend_implementation_review': 'Review a front-end plan for a permissions dashboard. It uses client-side rendering and boolean flags for access control.',
    'api_reliability_security_review': 'Audit a POST /reports endpoint that generates PDFs synchronously, has no idempotency key, and returns 200 even on failure.',
    'brand_positioning_pass': 'Brand positioning for a fintech startup targeting freelancers. Competitors: Stripe, Mercury, Relay. Goal: trustworthy but approachable.',
}


def parse_headings(text: str) -> list[str]:
    """Extract all section headings from output text."""
    headings = []
    for line in text.splitlines():
        m = re.match(r'^(#{1,4})\s+(.+)$', line.strip())
        if m:
            headings.append(m.group(2).strip().lower())
        m2 = re.match(r'^\*\*([^*]+?)(?::\*\*|\*\*)\s*$', line.strip())
        if m2:
            headings.append(m2.group(1).strip().lower())
    return headings


def required_sections_for_task(task_id: str) -> list[str]:
    contracts = json.loads(CONTRACTS_PATH.read_text())
    for task in contracts['tasks']:
        if task['task_id'] == task_id:
            return [s['name'].lower() for s in task.get('required_sections', [])]
    return []


def current_aliases() -> dict[str, set[str]]:
    data = json.loads(ALIASES_PATH.read_text())
    return {k: set(v) for k, v in data['aliases'].items()}


def heading_matches(heading: str, required: str, aliases: dict[str, set[str]]) -> bool:
    """True if `heading` satisfies `required` via exact, prefix, or alias match."""
    req_low = required.lower()
    if req_low in heading or heading in req_low:
        return True
    req_words = [w for w in req_low.split() if len(w) >= 5]
    req_stems = [w[:5] for w in req_words]
    head_words = heading.split()
    if any(hw.startswith(stem) for stem in req_stems for hw in head_words):
        return True
    for alias in aliases.get(req_low, set()):
        if alias in heading or heading in alias:
            return True
    return False


def call_api(prompt: str, system: str | None, provider: str, model: str) -> str:
    if provider == 'anthropic':
        import anthropic
        c = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
        kw = {'model': model, 'max_tokens': 1500, 'messages': [{'role': 'user', 'content': prompt}]}
        if system:
            kw['system'] = system
        msg = c.messages.create(**kw)
        return ''.join(b.text for b in msg.content if hasattr(b, 'text'))
    elif provider == 'openai':
        from openai import OpenAI
        c = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
        msgs = [{'role': 'system', 'content': system}] if system else []
        msgs.append({'role': 'user', 'content': prompt})
        r = c.chat.completions.create(model=model, messages=msgs, max_tokens=1500)
        return r.choices[0].message.content or ''
    elif provider == 'google':
        import google.generativeai as genai
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
        m = genai.GenerativeModel(model, system_instruction=system or '')
        return m.generate_content(prompt).text
    elif provider == 'mistral':
        from mistralai.client import MistralClient
        from mistralai.models.chat_completion import ChatMessage
        c = MistralClient(api_key=os.environ['MISTRAL_API_KEY'])
        msgs = []
        if system:
            msgs.append(ChatMessage(role='system', content=system))
        msgs.append(ChatMessage(role='user', content=prompt))
        return c.chat(model=model, messages=msgs, max_tokens=1500).choices[0].message.content
    else:
        raise ValueError(f'Unsupported provider: {provider}')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--provider', required=True, choices=['anthropic', 'openai', 'google', 'mistral'])
    parser.add_argument('--model', required=True)
    parser.add_argument('--tasks', nargs='*', default=list(CANARY_PROMPTS.keys()))
    parser.add_argument('--dry-run', action='store_true', help='Print candidates but do not write to calibration log')
    args = parser.parse_args()

    system = DEPLOY_PATH.read_text(encoding='utf-8') if DEPLOY_PATH.exists() else None
    aliases = current_aliases()

    candidates: list[dict] = []
    for task_id in args.tasks:
        prompt = CANARY_PROMPTS.get(task_id)
        if not prompt:
            print(f'  No canary prompt for {task_id}, skipping')
            continue
        required = required_sections_for_task(task_id)
        if not required:
            print(f'  No required sections for {task_id}, skipping')
            continue

        print(f'\nRunning {task_id}...', flush=True)
        try:
            response = call_api(prompt, system, args.provider, args.model)
            time.sleep(10)
        except Exception as e:
            print(f'  API error: {e}')
            continue

        headings = parse_headings(response)
        print(f'  Detected {len(headings)} headings: {headings[:8]}')

        for req in required:
            matched = any(heading_matches(h, req, aliases) for h in headings)
            if not matched:
                # Find closest actual heading (for the candidate entry)
                closest = headings[0] if headings else '(no headings detected)'
                print(f'  DRIFT: "{req}" not matched. Actual headings: {headings[:5]}')
                candidates.append({
                    'date': datetime.now(timezone.utc).strftime('%Y-%m-%d'),
                    'target_type': 'section_alias',
                    'target_id': req,
                    'tokens_added': headings[:3],  # Top 3 actual headings as candidates
                    'observed_in_task': task_id,
                    'observed_in_output': f'drift check {args.provider}/{args.model}',
                    'run_id': f'drift-{args.provider}-{datetime.now(timezone.utc).strftime("%Y%m%d")}',
                    'reason': f'{args.model} used different vocabulary for "{req}". Review and add the correct alias.',
                    'status': 'CANDIDATE — requires human review before adding to section_aliases.json',
                })

    if not candidates:
        print('\nNo alias drift detected. All section headings matched.')
        return

    print(f'\n{len(candidates)} drift candidate(s) found.')
    if args.dry_run:
        print('\nDRY RUN — candidates (not written):')
        print(json.dumps(candidates, indent=2))
        return

    log = json.loads(CALIB_LOG_PATH.read_text())
    log['entries'].extend(candidates)
    CALIB_LOG_PATH.write_text(json.dumps(log, indent=2))
    print(f'Written to {CALIB_LOG_PATH}')
    print('Review CANDIDATE entries and promote to section_aliases.json after verification.')


if __name__ == '__main__':
    main()
