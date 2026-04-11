#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from runtime_validator import validate_runtime_overlay_assets

ROOT = Path(__file__).resolve().parent
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


def main():
    failures = 0
    overlay_report = validate_runtime_overlay_assets(ROOT)
    if overlay_report['decision'] == 'FAIL':
        failures += 1
        print('FAIL capability preservation overlay check')
        for error in overlay_report['errors']:
            print('  ERROR ' + error)
    else:
        for warning in overlay_report.get('warnings', []):
            print('WARN capability preservation: ' + warning)
    found = {p.name for p in EXAMPLES.glob('*.md') if p.name != 'README.md'}
    missing = sorted(REQUIRED_EXAMPLES - found)
    if missing:
        failures += 1
        print('FAIL missing required examples: ' + ', '.join(missing))
    for path in sorted(EXAMPLES.glob('*.md')):
        if path.name == 'README.md':
            continue
        text = path.read_text(encoding='utf-8')
        errors = []
        if len(text.splitlines()) < MIN_LINES:
            errors.append(f'under minimum line count {MIN_LINES}')
        for sec in REQ_SECTIONS:
            if sec not in text:
                errors.append(f'missing section {sec}')
        if 'Fixture:' not in text or 'Validation result:' not in text:
            errors.append('missing fixture or validation-result references')
        eval_path = None
        for phrase in PLACEHOLDER:
            if phrase in text.lower():
                errors.append(f'placeholder phrase present: {phrase}')
        for marker in ['Fixture:', 'Validation result:']:
            for line in [ln for ln in text.splitlines() if ln.startswith(marker)]:
                ref = line.split(':', 1)[1].strip()
                ref_path = (ROOT / ref).resolve()
                if not ref_path.exists():
                    errors.append(f'missing referenced artifact {ref}')
                if marker == 'Validation result:' and ref_path.exists():
                    eval_path = ref_path
        if eval_path:
            try:
                eval_data = json.loads(eval_path.read_text(encoding='utf-8'))
                missing_fields = sorted(REQUIRED_EVAL_FIELDS - set(eval_data.keys()))
                if missing_fields:
                    errors.append('eval missing fields: ' + ', '.join(missing_fields))
                scores = eval_data.get('rubric_scores', {})
                if len(set(scores.values())) <= 1:
                    errors.append('eval score variance too low')
            except Exception as exc:
                errors.append(f'could not parse eval json: {exc}')
        if errors:
            failures += 1
            print(f'FAIL {path.name}')
            for error in errors:
                print(f'  ERROR {error}')
        else:
            print(f'PASS {path.name}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
