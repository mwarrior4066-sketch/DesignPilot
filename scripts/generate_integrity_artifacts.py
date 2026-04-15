#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def words(path: Path) -> int:
    try:
        return len(path.read_text(encoding='utf-8').split())
    except Exception:
        return 0


def tokens(path: Path) -> int:
    try:
        return max(1, round(len(path.read_text(encoding='utf-8')) / 4))
    except Exception:
        return 0


def collect_files():
    files = []
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        if '__pycache__' in path.parts or path.suffix == '.pyc':
            continue
        rel = path.relative_to(ROOT).as_posix()
        files.append({'path': rel, 'bytes': path.stat().st_size, 'sha256': sha(path)})
    return files


def main():
    manifest = json.loads((ROOT / 'PACK_MANIFEST.json').read_text(encoding='utf-8'))
    version = manifest['version']
    build_metrics = {
        'version': version,
        'artifacts': {
            'dist/DEPLOY_LITE.md': {'word_count': words(DIST / 'DEPLOY_LITE.md'), 'token_estimate': tokens(DIST / 'DEPLOY_LITE.md'), 'sha256': sha(DIST / 'DEPLOY_LITE.md')},
            'dist/runtime/START_HERE.md': {'word_count': words(DIST / 'runtime' / 'START_HERE.md'), 'token_estimate': tokens(DIST / 'runtime' / 'START_HERE.md'), 'sha256': sha(DIST / 'runtime' / 'START_HERE.md')},
            'dist/runtime/TASK_CHOOSER.md': {'word_count': words(DIST / 'runtime' / 'TASK_CHOOSER.md'), 'token_estimate': tokens(DIST / 'runtime' / 'TASK_CHOOSER.md'), 'sha256': sha(DIST / 'runtime' / 'TASK_CHOOSER.md')},
            'docs/operator/DEPLOYMENT_GUIDE.md': {'word_count': words(ROOT / 'docs/operator/DEPLOYMENT_GUIDE.md'), 'token_estimate': tokens(ROOT / 'docs/operator/DEPLOYMENT_GUIDE.md'), 'sha256': sha(ROOT / 'docs/operator/DEPLOYMENT_GUIDE.md')},
            'docs/operator/DEPLOYMENT_GUIDE.md': {'word_count': words(ROOT / 'docs/operator/DEPLOYMENT_GUIDE.md'), 'token_estimate': tokens(ROOT / 'docs/operator/DEPLOYMENT_GUIDE.md'), 'sha256': sha(ROOT / 'docs/operator/DEPLOYMENT_GUIDE.md')},
            'docs/operator/ROUTE_PICKER.md': {'word_count': words(ROOT / 'docs/operator/ROUTE_PICKER.md'), 'token_estimate': tokens(ROOT / 'docs/operator/ROUTE_PICKER.md'), 'sha256': sha(ROOT / 'docs/operator/ROUTE_PICKER.md')},
            'proof/PROOF_STATUS.md': {'word_count': words(ROOT / 'proof/PROOF_STATUS.md'), 'token_estimate': tokens(ROOT / 'proof/PROOF_STATUS.md'), 'sha256': sha(ROOT / 'proof/PROOF_STATUS.md')},
            'proof/status.json': {'word_count': 0, 'token_estimate': 0, 'sha256': sha(ROOT / 'proof/status.json')},
        },
        'summary': {
            'lite_route_docs': len(list((DIST / 'runtime' / 'route_cards').glob('*.md'))),
            'lite_contract_docs': len(list((DIST / 'runtime' / 'contracts_lite').glob('*.md'))),
            'lite_starter_docs': len(list((DIST / 'runtime' / 'starters').glob('*.md'))),
            'task_launchers': len(list((DIST / 'runtime' / 'task_launchers').glob('*.md'))),
        }
    }
    (DIST / 'build_metrics.json').write_text(json.dumps(build_metrics, indent=2), encoding='utf-8')
    full_build = {'bundle': f'DesignPilot v{version} Integrity Pass', 'version': version, 'generated_at': '2026-04-12', 'file_count': 0, 'files': collect_files()}
    full_build['file_count'] = len(full_build['files'])
    (DIST / 'manifest.json').write_text(json.dumps(full_build, indent=2), encoding='utf-8')
    key_files = [
        'dist/runtime/START_HERE.md',
        'dist/runtime/TASK_CHOOSER.md',
        'dist/DEPLOY_LITE.md',
        'docs/operator/DEPLOYMENT_GUIDE.md',
        'docs/operator/DEPLOYMENT_GUIDE.md',
        'docs/operator/ROUTE_PICKER.md',
        'dist/lightweight_validation_report.json',
        'dist/integrity_validation_report.json',
        'dist/validation_suite_report.json',
        'dist/build_metrics.json',
        'dist/manifest.json',
        'proof/PROOF_STATUS.md',
        'proof/status.json',
        'proof/benchmarks/README.md',
        'proof/reviews/README.md',
        'proof/receipts/README.md',
        f'proof/artifacts/integrity_pass_report_v{version}.md'
    ]
    handoff = {'bundle': 'DesignPilot_Integrity_Pass', 'version': version, 'generated_at': '2026-04-12', 'full_build_manifest': 'dist/manifest.json', 'artifacts': []}
    for rel in key_files:
        path = ROOT / rel
        if path.exists():
            handoff['artifacts'].append({'path': rel, 'bytes': path.stat().st_size, 'sha256': sha(path)})
    (ROOT / 'HANDOFF_MANIFEST.json').write_text(json.dumps(handoff, indent=2), encoding='utf-8')
    handoff_readme = f'''# DesignPilot Integrity Pass Handoff

This bundle is the integrity-hardened DesignPilot release for v{version}.

Use `HANDOFF_MANIFEST.json` for key artifact verification and `dist/manifest.json` for full bundle verification.

Primary operator files:
- `dist/runtime/START_HERE.md`
- `dist/runtime/TASK_CHOOSER.md`
- `dist/DEPLOY_LITE.md`
- `docs/operator/DEPLOYMENT_GUIDE.md`

Credibility files:
- `proof/PROOF_STATUS.md`
- `proof/benchmarks/README.md`
- `proof/reviews/README.md`
- `proof/receipts/README.md`

Validation files:
- `dist/lightweight_validation_report.json`
- `dist/integrity_validation_report.json`
- `dist/validation_suite_report.json`
- `dist/build_metrics.json`
- `dist/manifest.json`
'''
    (ROOT / 'HANDOFF_README.md').write_text(handoff_readme, encoding='utf-8')
    report = f'''# Integrity Pass Report v{version}

## Goal
Harden DesignPilot against consistency slips, stale metrics, version ambiguity, launcher/runtime drift, and continuity-state drift.

## Implemented
- unified the operator startup path around a compiled runtime front door and task launchers
- tightened metadata and continuity synchronization around the canonical release manifest
- added a shared validation suite and severity-based validator reports
- added structured continuity state rendered into human-readable continuity docs
- normalized a layered proof surface with explicit status, benchmark, review, and receipt indices
- regenerated handoff artifacts from current files only

## Current metrics
- `DEPLOY_LITE.md`: {words(DIST / 'DEPLOY_LITE.md')} words / ~{tokens(DIST / 'DEPLOY_LITE.md')} tokens
- Task launchers: {len(list((DIST / 'runtime' / 'task_launchers').glob('*.md')))}
- Lite route docs: {len(list((DIST / 'runtime' / 'route_cards').glob('*.md')))}
- Lite contract docs: {len(list((DIST / 'runtime' / 'contracts_lite').glob('*.md')))}
- Lite starter packs: {len(list((DIST / 'runtime' / 'starters').glob('*.md')))}

## Validation
- lightweight validation: generated by release pipeline
- integrity validation: generated by release pipeline
- release decision: generated by `scripts/package_release.py`

## Proof boundary note
This pass strengthens evidence organization and release receipts. It does not turn internal validation into production outcome proof.

## Notes
This pass focuses on structural consistency and release discipline rather than new task-domain expansion.
'''
    (ROOT / 'proof/artifacts' / f'integrity_pass_report_v{version}.md').write_text(report, encoding='utf-8')
    print(json.dumps({'version': version, 'file_count': full_build['file_count']}, indent=2))


if __name__ == '__main__':
    main()
