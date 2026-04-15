#!/usr/bin/env python3
from __future__ import annotations

import sys
sys.dont_write_bytecode = True  # must be set before any local imports to prevent __pycache__ creation

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from _validation import aggregate_reports, exit_code_for, print_report, write_report
from clean_distribution_noise import clean_distribution_noise
from lint_pack import lint_pack
from validate_examples import validate_examples
from validate_integrity_sync import validate_integrity_sync
from validate_lightweight_path import validate_lightweight_path
from validate_project_workspace import validate_project_workspace
from validate_release_consistency import validate_release_consistency

VALIDATORS = {
    'lint_pack': lambda root: lint_pack(root),
    'lightweight_path': lambda root: validate_lightweight_path(root),
    'examples': lambda root: validate_examples(root),
    'workspace': lambda root: validate_project_workspace(root),
    'integrity_sync': lambda root: validate_integrity_sync(root),
    'release_consistency': lambda root: validate_release_consistency(root),
}


def main() -> None:
    # Clean any cache artifacts before running validators so the integrity check
    # does not fail on __pycache__ directories created by this script's own imports.
    clean_distribution_noise(ROOT)

    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='.')
    parser.add_argument('--skip', action='append', default=[])
    parser.add_argument('--fast', action='store_true', help='Skip integrity_sync for a faster local pass.')
    parser.add_argument('--include-integrity', action='store_true', help='Deprecated no-op; integrity runs by default.')
    parser.add_argument('--report-path', default='dist/validation_suite_report.json')
    args = parser.parse_args()

    root = Path(args.root).resolve()
    reports = []
    executed = []
    skip = set(args.skip)
    if args.fast:
        skip.add('integrity_sync')
    for name, fn in VALIDATORS.items():
        if name in skip:
            continue
        report = fn(root)
        reports.append(report)
        executed.append(name)
    suite = aggregate_reports('validation_suite', reports, metadata={'executed': executed, 'skipped': sorted(skip), 'fast_mode': bool(args.fast)})
    write_report(root / args.report_path, suite)
    print_report(suite)
    raise SystemExit(exit_code_for(suite))


if __name__ == '__main__':
    main()
