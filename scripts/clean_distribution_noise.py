#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'


def clean_distribution_noise(root: Path = ROOT, version: str | None = None) -> dict:
    root = Path(root).resolve()
    dist = root / 'dist'
    removed = {
        'pycache_dirs': [],
        'pyc_files': [],
        'stale_release_reports': [],
        'stale_release_attempts': [],
        'stale_integrity_reports': [],
    }

    for path in sorted(root.rglob('__pycache__')):
        if path.is_dir():
            removed['pycache_dirs'].append(str(path.relative_to(root)))
            shutil.rmtree(path, ignore_errors=True)

    for path in sorted(root.rglob('*.pyc')):
        if path.is_file():
            removed['pyc_files'].append(str(path.relative_to(root)))
            path.unlink()

    if version:
        current_report = dist / f'release_quality_report_v{version}.json'
        for path in sorted(dist.glob('release_quality_report_v*.json')):
            if path != current_report:
                removed['stale_release_reports'].append(str(path.relative_to(root)))
                path.unlink()
    for path in sorted(dist.glob('release_attempt_v*.json')):
        removed['stale_release_attempts'].append(str(path.relative_to(root)))
        path.unlink()

    proof_artifacts = root / 'proof' / 'artifacts'
    if version and proof_artifacts.exists():
        current_integrity = proof_artifacts / f'integrity_pass_report_v{version}.md'
        for path in sorted(proof_artifacts.glob('integrity_pass_report_v*.md')):
            if path != current_integrity:
                removed['stale_integrity_reports'].append(str(path.relative_to(root)))
                path.unlink()

    removed['counts'] = {k: len(v) for k, v in removed.items() if isinstance(v, list)}
    return removed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='.')
    parser.add_argument('--version', default=None)
    args = parser.parse_args()
    report = clean_distribution_noise(Path(args.root), version=args.version)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
