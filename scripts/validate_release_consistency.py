#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
sys.dont_write_bytecode = True
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from _validation import build_report, exit_code_for, issues_from_legacy, print_report, write_report

CURRENT_RELEASE_LINE = 'v3.0'
CURRENT_RELEASE_TEXT = 'Current release line: v3.0'
STALE_RELEASE_LINE = 'v' + '2.7'
STALE_RELEASE_NUMBER = '2' + '.7'

SCAN_FILES = [
    'README.md',
    'HOWTO.md',
    'HANDOFF_README.md',
    'HANDOFF_MANIFEST.json',
    'PACK_MANIFEST.json',
    'PATCH_SUMMARY.json',
    'RELEASE_STATUS.json',
    'proof/PROOF_STATUS.md',
    'proof/CLAIM_TO_EVIDENCE_MAP.md',
    'proof/status.json',
    'proof/receipts/README.md',
    'projects/designpilot/context/PROJECT_OVERVIEW.md',
    'projects/designpilot/context/ACTIVE_STATE.md',
    'projects/designpilot/context/CASE_STUDY_ROADMAP.md',
    'projects/designpilot/context/state/release_state.json',
    'projects/designpilot/handoff/DOWNLOAD_BUNDLE_MANIFEST.md',
    'tests/regression_suite.json',
    'tests/README.md',
    'scripts/README.md',
]

PROOF_HANDOFF_DIRS = [
    ROOT / 'proof',
    ROOT / 'projects' / 'designpilot' / 'handoff',
]

CURRENT_PATTERNS = [
    re.compile(r'Current stable release:\s*(v\d+(?:\.\d+)*)', re.I),
    re.compile(r'Current release line:\s*(v\d+(?:\.\d+)*)', re.I),
    re.compile(r'Current release:\s*(v\d+(?:\.\d+)*)', re.I),
    re.compile(r'This bundle is .* release for\s*(v\d+(?:\.\d+)*)', re.I),
]

STALE_CURRENT_PATTERNS = [
    re.compile(r'Current stable release:\s*' + re.escape(STALE_RELEASE_LINE), re.I),
    re.compile(r'Current release line:\s*' + re.escape(STALE_RELEASE_LINE), re.I),
    re.compile(r'Current release:\s*' + re.escape(STALE_RELEASE_LINE), re.I),
    re.compile(r'This bundle is .* release for\s*' + re.escape(STALE_RELEASE_LINE), re.I),
    re.compile(r'"(?:version|pack_version|suite_version|current_release)"\s*:\s*"' + re.escape(STALE_RELEASE_NUMBER) + r'"', re.I),
]


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='ignore')


def check_json_version(path: Path, errors: list[str], keys: tuple[str, ...]) -> None:
    try:
        data = json.loads(read(path))
    except Exception as exc:
        errors.append(f'{path.relative_to(ROOT)} is not valid JSON: {exc}')
        return
    for key in keys:
        if key in data and str(data[key]) != '3.0':
            errors.append(f'{path.relative_to(ROOT)} has {key}={data[key]!r}, expected "3.0"')


def validate_release_consistency(root: Path = ROOT) -> dict:
    root = Path(root).resolve()
    errors: list[str] = []
    warnings: list[str] = []
    metrics: dict[str, int | str] = {'current_release_line': CURRENT_RELEASE_LINE}

    status_path = root / 'RELEASE_STATUS.json'
    if not status_path.exists():
        errors.append('missing RELEASE_STATUS.json')
    else:
        try:
            status = json.loads(status_path.read_text(encoding='utf-8'))
            expected = {
                'current_release_line': 'v3.0',
                'pack_version': '3.0',
                'suite_version': '3.0',
                'proof_status': 'v3.0-aligned',
                'handoff_status': 'v3.0-aligned',
            }
            for key, value in expected.items():
                if status.get(key) != value:
                    errors.append(f'RELEASE_STATUS.json {key}={status.get(key)!r}, expected {value!r}')
        except Exception as exc:
            errors.append(f'RELEASE_STATUS.json is not valid JSON: {exc}')

    for rel in SCAN_FILES:
        path = root / rel
        if not path.exists():
            warnings.append(f'missing scanned release surface: {rel}')
            continue
        text = read(path)
        for rx in STALE_CURRENT_PATTERNS:
            if rx.search(text):
                errors.append(f'stale current-release reference in {rel}: {rx.pattern}')
        for line_no, line in enumerate(text.splitlines(), start=1):
            if STALE_RELEASE_LINE in line and rel.startswith(('HANDOFF', 'proof/', 'projects/designpilot/context', 'projects/designpilot/handoff')):
                errors.append(f'v2.7 reference in proof/handoff/continuity surface {rel}:{line_no}')

    manifest = root / 'PACK_MANIFEST.json'
    if manifest.exists():
        check_json_version(manifest, errors, ('version',))
    regression = root / 'tests' / 'regression_suite.json'
    if regression.exists():
        check_json_version(regression, errors, ('pack_version', 'suite_version'))
    release_state = root / 'projects' / 'designpilot' / 'context' / 'state' / 'release_state.json'
    if release_state.exists():
        check_json_version(release_state, errors, ('current_release',))

    proof_handoff_files = []
    for directory in PROOF_HANDOFF_DIRS:
        if directory.exists():
            proof_handoff_files.extend(p for p in directory.rglob('*') if p.is_file())
    metrics['proof_handoff_files_scanned'] = len(proof_handoff_files)
    for path in proof_handoff_files:
        rel = str(path.relative_to(root))
        if '__pycache__' in path.parts or path.suffix in {'.pyc', '.pyo'}:
            continue
        if STALE_RELEASE_LINE in read(path):
            errors.append(f'v2.7 reference remains in proof/handoff artifact: {rel}')
        if ('integrity_pass_report_' + STALE_RELEASE_LINE) in rel:
            errors.append(f'stale v2.7 artifact filename remains: {rel}')

    # Changelog may retain the stale release string as explicit history, but current status lines may not.
    changelog = root / 'CHANGELOG.md'
    if changelog.exists():
        for line_no, line in enumerate(read(changelog).splitlines(), start=1):
            if re.search(r'Current .*v2\.7|release line.*v2\.7', line, re.I):
                errors.append(f'stale current release language in CHANGELOG.md:{line_no}')

    report = build_report(
        'validate_release_consistency',
        issues_from_legacy(errors=errors, warnings=warnings, source='scripts/validate_release_consistency.py'),
        metrics=metrics,
    )
    write_report(root / 'dist' / 'release_consistency_report.json', report)
    return report


def main() -> None:
    report = validate_release_consistency()
    print_report(report)
    raise SystemExit(exit_code_for(report))


if __name__ == '__main__':
    main()
