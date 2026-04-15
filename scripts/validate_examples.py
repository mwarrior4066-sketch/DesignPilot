#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from _validation import build_report, exit_code_for, issue, print_report, write_report
from runtime_validator import validate_runtime_overlay_assets

EXAMPLES = ROOT / 'examples'
REQ_SECTIONS = [
    '## Input Prompt',
    '## Selected Route and Loaded Skills',
    '## Final Output',
    '## Why This Passed',
    '## What Would Have Failed',
    '## Revision Pass'
]
PLACEHOLDER = ['placeholder', 'tbd', 'route is explicit', 'required sections are visible', 'evidence burden is named']
MIN_LINES = 45
REQUIRED_EXAMPLES = {
    'ui-structure-critique.md',
    'component-spec.md',
    'dashboard-audit.md',
    'backend-feasibility-review.md',
    'pdf-remediation-plan.md',
    'brand-positioning-pass.md',
    'case-study-rewrite.md',
    'accessibility-feedback-pass.md',
    'color-system-pass.md',
    'graphic-critique-pass.md',
    'layout-reconstruction-pass.md',
    'type-system-pass.md',
    'ux-research-pass.md',
    'frontend-implementation-review.md',
    'backend-architecture-spec.md',
    'api-reliability-security-review.md',
    'adaptive-explanation-tiered-response.md'
}
REQUIRED_EVAL_FIELDS = {
    'example',
    'task_contract',
    'validator_decision',
    'rubric_scores',
    'strongest_dimension',
    'weakest_dimension',
    'pass_justification',
    'residual_reviewer_doubt'
}


def validate_examples(root: Path = ROOT) -> dict:
    root = Path(root).resolve()
    examples = root / 'examples'
    issues = []
    # Files in examples/ that are golden outputs for regression tests, not structured example docs
    GOLDEN_OUTPUT_EXEMPTIONS = {'designer-response-filter-pass.md', 'text-humanization-pass.md', 'startup-helper-tone-pass.md'}
    overlay_report = validate_runtime_overlay_assets(root)
    if overlay_report['decision'] == 'FAIL':
        for error in overlay_report['errors']:
            issues.append(issue('ERROR', error, source='runtime_overlay'))
    else:
        for warning in overlay_report.get('warnings', []):
            issues.append(issue('WARN', warning, source='runtime_overlay'))

    found = {p.name for p in examples.glob('*.md') if p.name != 'README.md'}
    missing = sorted(REQUIRED_EXAMPLES - found)
    if missing:
        issues.append(issue('ERROR', 'missing required examples: ' + ', '.join(missing), source='examples'))

    checked = 0
    for path in sorted(examples.glob('*.md')):
        if path.name == 'README.md':
            continue
        if path.name in GOLDEN_OUTPUT_EXEMPTIONS:
            continue  # raw model output used as regression golden file, not a structured example doc
        checked += 1
        text = path.read_text(encoding='utf-8')
        local_errors = []
        if len(text.splitlines()) < MIN_LINES:
            local_errors.append(f'under minimum line count {MIN_LINES}')
        for sec in REQ_SECTIONS:
            if sec not in text:
                local_errors.append(f'missing section {sec}')
        if 'Fixture:' not in text or 'Validation result:' not in text:
            local_errors.append('missing fixture or validation-result references')
        eval_path = None
        for phrase in PLACEHOLDER:
            if phrase in text.lower():
                local_errors.append(f'placeholder phrase present: {phrase}')
        for marker in ['Fixture:', 'Validation result:']:
            for line in [ln for ln in text.splitlines() if ln.startswith(marker)]:
                ref = line.split(':', 1)[1].strip()
                ref_path = (root / ref).resolve()
                if not ref_path.exists():
                    local_errors.append(f'missing referenced artifact {ref}')
                if marker == 'Validation result:' and ref_path.exists():
                    eval_path = ref_path
        if eval_path:
            try:
                eval_data = json.loads(eval_path.read_text(encoding='utf-8'))
                missing_fields = sorted(REQUIRED_EVAL_FIELDS - set(eval_data.keys()))
                if missing_fields:
                    local_errors.append('eval missing fields: ' + ', '.join(missing_fields))
                scores = eval_data.get('rubric_scores', {})
                if len(set(scores.values())) <= 1:
                    local_errors.append('eval score variance too low')
            except Exception as exc:
                local_errors.append(f'could not parse eval json: {exc}')
        for err in local_errors:
            issues.append(issue('ERROR', f'{path.name}: {err}', source='scripts/validate_examples.py'))

    report = build_report(
        'validate_examples',
        issues,
        metrics={'checked_examples': checked, 'required_examples': len(REQUIRED_EXAMPLES)},
    )
    write_report(root / 'dist' / 'examples_validation_report.json', report)
    return report


def main() -> None:
    report = validate_examples()
    print_report(report)
    raise SystemExit(exit_code_for(report))


if __name__ == '__main__':
    main()
