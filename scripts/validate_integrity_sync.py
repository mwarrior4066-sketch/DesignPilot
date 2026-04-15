#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True  # direct invocation must not create __pycache__ noise

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
sys.path.insert(0, str(ROOT / 'scripts'))

from _validation import build_report, exit_code_for, issues_from_legacy, print_report, write_report

IGNORED_DIRS = {'__pycache__', '.pytest_cache', '.mypy_cache'}
IGNORED_SUFFIXES = {'.pyc', '.pyo'}


def is_runtime_artifact(path: Path) -> bool:
    return bool(set(path.parts) & IGNORED_DIRS) or path.suffix in IGNORED_SUFFIXES



def read_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def count_words(path: Path) -> int:
    return len(path.read_text(encoding='utf-8').split())


def validate_integrity_sync(root: Path = ROOT) -> dict:
    root = Path(root).resolve()
    dist = root / 'dist'
    errors = []
    warnings = []
    metrics = {}

    manifest = read_json(root / 'PACK_MANIFEST.json')
    version = manifest['version']
    metrics['version'] = version

    readme_lines = (root / 'README.md').read_text(encoding='utf-8').splitlines()
    stable_line = readme_lines[2] if len(readme_lines) > 2 else ''
    if f'v{version}' not in stable_line:
        errors.append('README stable release line version mismatch')

    current_report = dist / f'release_quality_report_v{version}.json'
    stale_reports = [p.name for p in dist.glob('release_quality_report_v*.json') if p.name != current_report.name]
    if stale_reports:
        errors.append('stale release reports remain in dist')

    # Python may create cache files during direct script execution. Treat them
    # as runtime noise rather than release drift so this validator is idempotent.
    cache_artifacts = [p for p in root.rglob('*') if is_runtime_artifact(p)]
    if cache_artifacts:
        metrics['ignored_runtime_artifacts'] = len(cache_artifacts)

    quick = (root / 'QUICKSTART.md').read_text(encoding='utf-8')
    for needle in ['Full mode', 'Profile-only mode', 'Lightweight mode']:
        if needle not in quick:
            errors.append(f'QUICKSTART missing {needle}')

    profile_guide = (root / 'docs/operator/PROFILE_GUIDE.md').read_text(encoding='utf-8')
    if 'Use the full kernel for true cross-domain coordination' not in profile_guide:
        errors.append('PROFILE_GUIDE missing full-kernel cross-domain escalation rule')

    lite_report = read_json(dist / 'lightweight_validation_report.json')
    actual = {
        'lite_word_count': count_words(dist / 'DEPLOY_LITE.md'),
        'route_json_count': len(list((root / 'dist/runtime/routes').glob('*.json'))),
        'contract_json_count': len(list((root / 'dist/runtime/contracts').glob('*.json'))),
        'route_doc_count': len(list((dist / 'runtime' / 'route_cards').glob('*.md'))),
        'contract_doc_count': len(list((dist / 'runtime' / 'contracts_lite').glob('*.md'))),
        'starter_doc_count': len(list((dist / 'runtime' / 'starters').glob('*.md'))),
        'launcher_doc_count': len(list((dist / 'runtime' / 'task_launchers').glob('*.md'))),
        'lite_index_route_count': len(read_json(dist / 'runtime' / 'lite_index.json')['routes']),
    }
    metrics.update(actual)
    for key, value in actual.items():
        if lite_report['metrics'].get(key) != value:
            errors.append(f'lightweight report metric mismatch: {key}')

    build_metrics_path = dist / 'build_metrics.json'
    if build_metrics_path.exists():
        build_metrics = read_json(build_metrics_path)
        art = build_metrics.get('artifacts', {}).get('dist/DEPLOY_LITE.md', {})
        if art.get('word_count') != actual['lite_word_count']:
            errors.append('build_metrics out of sync for DEPLOY_LITE')
        if 'dist/runtime/START_HERE.md' not in build_metrics.get('artifacts', {}):
            errors.append('build_metrics missing START_HERE runtime artifact')
    else:
        warnings.append('build_metrics.json missing before integrity artifact generation')

    route_cards = {p.stem: read_json(p) for p in (root / 'dist/runtime/routes').glob('*.json')}
    contract_cards = {p.stem: read_json(p) for p in (root / 'dist/runtime/contracts').glob('*.json')}
    for route_id, route in route_cards.items():
        route_doc = dist / 'runtime' / 'route_cards' / f'{route_id}.md'
        if not route_doc.exists():
            errors.append(f'missing route doc: {route_id}')
            continue
        txt = route_doc.read_text(encoding='utf-8')
        task_contract = route.get('task_contract')
        if task_contract and task_contract in contract_cards:
            expected = f'`dist/runtime/contracts_lite/{task_contract}.md`'
            if expected not in txt:
                errors.append(f'route doc contract mismatch: {route_id}')
        for skill in route.get('governing_skills', []):
            if skill not in txt:
                errors.append(f'route doc missing governing skill {skill}: {route_id}')
        launcher = dist / 'runtime' / 'task_launchers' / f"{route['task_id']}.md"
        if route.get('lightweight_eligible') and task_contract in contract_cards and not launcher.exists():
            errors.append(f'missing launcher for lightweight route: {route_id}')
    for task_id, contract in contract_cards.items():
        cdoc = dist / 'runtime' / 'contracts_lite' / f'{task_id}.md'
        if not cdoc.exists():
            errors.append(f'missing contract doc: {task_id}')
            continue
        txt = cdoc.read_text(encoding='utf-8')
        for section in contract.get('required_sections', []):
            sec_name = section.get('name', section) if isinstance(section, dict) else section
            if sec_name not in txt:
                errors.append(f'contract doc missing required section {section}: {task_id}')

    compiled_summary_dir = dist / 'runtime' / 'summaries'
    if not compiled_summary_dir.exists():
        errors.append('missing compiled runtime summaries directory')
    else:
        compiled_summaries = {p.name for p in compiled_summary_dir.glob('*.md')}
        metrics['compiled_runtime_summary_count'] = len(compiled_summaries)
        for route_id, route in route_cards.items():
            for summary in route.get('required_summary_ids', []):
                summary_name = Path(summary).name
                if summary_name not in compiled_summaries:
                    errors.append(f'missing compiled runtime summary: {summary_name}')
        for doc_path in list((dist / 'runtime' / 'task_launchers').glob('*.md')) + list((dist / 'runtime' / 'route_cards').glob('*.md')):
            txt = doc_path.read_text(encoding='utf-8')
            if 'src/knowledge-base/summaries/' in txt:
                errors.append(f'operator-facing doc leaks source runtime summary path: {doc_path.relative_to(root)}')

    runtime_index_path = dist / 'runtime' / 'launchers_index.json'
    if runtime_index_path.exists():
        runtime_index = read_json(runtime_index_path)
        for route_id, rec in read_json(dist / 'runtime' / 'lite_index.json')['routes'].items():
            if rec['lightweight_eligible']:
                launcher_path = dist / 'runtime' / 'task_launchers' / f"{rec['task_id']}.md"
                if not launcher_path.exists():
                    errors.append(f'missing launcher doc: {route_id}')
                    continue
                txt = launcher_path.read_text(encoding='utf-8')
                if rec['task_id'] not in runtime_index.get('launchers', {}):
                    errors.append(f'launcher missing from index: {rec["task_id"]}')
                if 'Output expectations' not in txt or 'Route logic' not in txt:
                    errors.append(f'launcher missing core sections: {rec["task_id"]}')
    else:
        errors.append('missing runtime launchers index')


    session_schema_path = root / 'src' / 'schemas' / 'session_state_schema.json'
    if not session_schema_path.exists():
        errors.append('missing session state schema: src/schemas/session_state_schema.json')
    else:
        try:
            session_schema = read_json(session_schema_path)
            required = {'schema_version', 'required_fields', 'field_types', 'valid_escalation_levels'}
            missing_keys = required - set(session_schema.keys())
            if missing_keys:
                errors.append(f'session_state_schema.json missing keys: {sorted(missing_keys)}')
        except Exception as exc:
            errors.append(f'session_state_schema.json unparseable: {exc}')

    for protocol_file in [
        'src/operator/protocols/SESSION_STATE_TRACKING_PROTOCOL.md',
        'src/operator/protocols/CONTEXT_REMINDER_PROTOCOL.md',
    ]:
        protocol_path = root / protocol_file
        if not protocol_path.exists():
            errors.append(f'missing session tracking protocol: {protocol_file}')
        else:
            content = protocol_path.read_text(encoding='utf-8')
            if 'SESSION_STATE' not in content:
                warnings.append(f'session protocol missing SESSION_STATE marker: {protocol_file}')

    deploy_path = dist / 'DESIGNPILOT_DEPLOY.md'
    if deploy_path.exists():
        deploy_text = deploy_path.read_text(encoding='utf-8')
        for protocol_anchor in [
            'SESSION_STATE_TRACKING_PROTOCOL',
            'CONTEXT_REMINDER_PROTOCOL',
        ]:
            if protocol_anchor not in deploy_text:
                errors.append(f'DESIGNPILOT_DEPLOY.md missing compiled protocol: {protocol_anchor}')

    handoff = read_json(root / 'HANDOFF_MANIFEST.json') if (root / 'HANDOFF_MANIFEST.json').exists() else {}
    if handoff and 'full_build_manifest' not in handoff:
        warnings.append('handoff manifest missing full_build_manifest pointer before regeneration')

    # V5: Check that section_aliases.json exists and covers all required sections
    aliases_path = root / 'src' / 'schemas' / 'section_aliases.json'
    if not aliases_path.exists():
        errors.append('section_aliases.json missing -- required for section heading matching')
    else:
        aliases = json.loads(aliases_path.read_text(encoding='utf-8')).get('aliases', {})
        contracts_path = root / 'src' / 'schemas' / 'task_contracts.json'
        if contracts_path.exists():
            contracts_data = json.loads(contracts_path.read_text(encoding='utf-8'))
            uncovered = []
            for task in contracts_data.get('tasks', []):
                for sec in task.get('required_sections', []):
                    name = sec.get('name', sec) if isinstance(sec, dict) else sec
                    if name.lower() not in aliases:
                        uncovered.append(f"{task['task_id']}/{name}")
            if uncovered:
                warnings.append(
                    f"section_aliases.json missing coverage for {len(uncovered)} required section(s): "
                    + ', '.join(uncovered[:8])
                    + (f' (+{len(uncovered)-8} more)' if len(uncovered) > 8 else '')
                )

    report = build_report(
        'validate_integrity_sync',
        issues_from_legacy(errors=errors, warnings=warnings, source='scripts/validate_integrity_sync.py'),
        metrics=metrics,
    )
    write_report(dist / 'integrity_validation_report.json', report)
    return report


def main() -> None:
    report = validate_integrity_sync()
    print_report(report)
    raise SystemExit(exit_code_for(report))


if __name__ == '__main__':
    main()
