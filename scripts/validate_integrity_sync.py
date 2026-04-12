#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'

def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def count_words(path: Path) -> int:
    return len(path.read_text(encoding='utf-8').split())

def main():
    errors = []
    warnings = []
    metrics = {}

    manifest = read_json(ROOT / 'PACK_MANIFEST.json')
    version = manifest['version']
    metrics['version'] = version

    if f'v{version}' not in (ROOT / 'README.md').read_text(encoding='utf-8').splitlines()[0]:
        errors.append('README title version mismatch')

    current_report = DIST / f'release_quality_report_v{version}.json'
    if not current_report.exists():
        warnings.append('current release report missing before packaging')
    stale_reports = [p.name for p in DIST.glob('release_quality_report_v*.json') if p.name != current_report.name]
    if stale_reports:
        errors.append('stale release reports remain in dist')

    cache_artifacts = list(ROOT.rglob('*.pyc')) + list(ROOT.rglob('__pycache__'))
    if cache_artifacts:
        errors.append('python cache artifacts remain in bundle')

    quick = (ROOT / 'QUICKSTART.md').read_text(encoding='utf-8')
    for needle in ['Full mode', 'Profile-only mode', 'Lightweight mode']:
        if needle not in quick:
            errors.append(f'QUICKSTART missing {needle}')

    profile_guide = (ROOT / 'docs/operator/PROFILE_GUIDE.md').read_text(encoding='utf-8')
    if 'Use the full kernel for true cross-domain coordination' not in profile_guide:
        errors.append('PROFILE_GUIDE missing full-kernel cross-domain escalation rule')

    lite_report = read_json(DIST / 'lightweight_validation_report.json')
    actual = {
        'lite_word_count': count_words(DIST / 'DEPLOY_LITE.md'),
        'route_json_count': len(list((ROOT / 'src/runtime/cards/routes').glob('*.json'))),
        'contract_json_count': len(list((ROOT / 'src/runtime/cards/contracts').glob('*.json'))),
        'route_doc_count': len(list((DIST / 'lite_routes').glob('*.md'))),
        'contract_doc_count': len(list((DIST / 'lite_contracts').glob('*.md'))),
        'starter_doc_count': len(list((DIST / 'lite_starters').glob('*.md'))),
        'lite_index_route_count': len(read_json(DIST / 'lite_index.json')['routes']),
    }
    metrics.update(actual)
    for key, value in actual.items():
        if lite_report['metrics'].get(key) != value:
            errors.append(f'lightweight report metric mismatch: {key}')

    build_metrics_path = DIST / 'build_metrics.json'
    if build_metrics_path.exists():
        build_metrics = read_json(build_metrics_path)
        art = build_metrics.get('artifacts', {}).get('dist/DEPLOY_LITE.md', {})
        if art.get('word_count') != actual['lite_word_count']:
            errors.append('build_metrics out of sync for DEPLOY_LITE')
    else:
        warnings.append('build_metrics.json missing before integrity artifact generation')

    route_cards = {p.stem: read_json(p) for p in (ROOT / 'src/runtime/cards/routes').glob('*.json')}
    contract_cards = {p.stem: read_json(p) for p in (ROOT / 'src/runtime/cards/contracts').glob('*.json')}
    for route_id, route in route_cards.items():
        route_doc = DIST / 'lite_routes' / f'{route_id}.md'
        if not route_doc.exists():
            errors.append(f'missing route doc: {route_id}')
            continue
        txt = route_doc.read_text(encoding='utf-8')
        task_contract = route.get('task_contract')
        if task_contract and task_contract in contract_cards:
            expected = f'`dist/lite_contracts/{task_contract}.md`'
            if expected not in txt:
                errors.append(f'route doc contract mismatch: {route_id}')
        for skill in route.get('governing_skills', []):
            if skill not in txt:
                errors.append(f'route doc missing governing skill {skill}: {route_id}')
    for task_id, contract in contract_cards.items():
        cdoc = DIST / 'lite_contracts' / f'{task_id}.md'
        if not cdoc.exists():
            errors.append(f'missing contract doc: {task_id}')
            continue
        txt = cdoc.read_text(encoding='utf-8')
        for section in contract.get('required_sections', []):
            if section not in txt:
                errors.append(f'contract doc missing required section {section}: {task_id}')
    lite_index = read_json(DIST / 'lite_index.json')
    for route_id, rec in lite_index['routes'].items():
        if rec['lightweight_eligible']:
            starter = DIST / 'lite_starters' / f"{rec['task_id']}.md"
            if not starter.exists():
                errors.append(f'missing starter doc: {route_id}')
                continue
            txt = starter.read_text(encoding='utf-8')
            if rec['route_doc'] not in txt or rec['contract_doc'] not in txt:
                errors.append(f'starter doc route/contract mismatch: {route_id}')
            if 'tokens' not in txt.lower():
                errors.append(f'starter doc missing token estimate: {route_id}')
            for skill in rec.get('governing_skills', []):
                if skill not in txt:
                    errors.append(f'starter doc missing governing skill {skill}: {route_id}')

    handoff = read_json(ROOT / 'HANDOFF_MANIFEST.json') if (ROOT / 'HANDOFF_MANIFEST.json').exists() else {}
    if handoff and 'full_build_manifest' not in handoff:
        warnings.append('handoff manifest missing full_build_manifest pointer before regeneration')

    report = {'decision': 'FAIL' if errors else 'PASS', 'errors': errors, 'warnings': warnings, 'metrics': metrics}
    (DIST / 'integrity_validation_report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))
    if report['decision'] == 'FAIL':
        raise SystemExit(1)

if __name__ == '__main__':
    main()
