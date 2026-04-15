#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from _validation import build_report, exit_code_for, issues_from_legacy, print_report, write_report


def validate_lightweight_path(root: Path = ROOT) -> dict:
    root = Path(root).resolve()
    dist = root / 'dist'
    errors = []
    warnings = []
    metrics = {}

    required_files = [
        dist / 'DEPLOY_LITE.md',
        dist / 'SESSION_ZERO.md',
        dist / 'runtime' / 'START_HERE.md',
        dist / 'runtime' / 'TASK_CHOOSER.md',
        dist / 'runtime' / 'launchers_index.json',
        root / 'docs' / 'operator' / 'DEPLOYMENT_GUIDE.md',
        root / 'docs' / 'operator' / 'DEPLOYMENT_GUIDE.md',
        root / 'docs' / 'operator' / 'ROUTE_PICKER.md',
    ]
    for path in required_files:
        if not path.exists():
            errors.append(f'missing required lightweight/runtime artifact: {path.relative_to(root)}')

    lite_text = (dist / 'DEPLOY_LITE.md').read_text(encoding='utf-8') if (dist / 'DEPLOY_LITE.md').exists() else ''
    lite_words = len(lite_text.split())
    metrics['lite_word_count'] = lite_words
    if lite_words < 120:
        errors.append('DEPLOY_LITE.md is too thin to be a meaningful bootstrap')
    if lite_words > 1400:
        warnings.append('DEPLOY_LITE.md is heavier than expected for lightweight startup')

    route_jsons = sorted((root / 'dist' / 'runtime' / 'routes').glob('*.json'))
    contract_jsons = sorted((root / 'dist' / 'runtime' / 'contracts').glob('*.json'))
    route_docs = sorted((dist / 'runtime' / 'route_cards').glob('*.md'))
    contract_docs = sorted((dist / 'runtime' / 'contracts_lite').glob('*.md'))
    starter_docs = sorted((dist / 'runtime' / 'starters').glob('*.md'))
    launcher_docs = sorted((dist / 'runtime' / 'task_launchers').glob('*.md'))

    metrics['route_json_count'] = len(route_jsons)
    metrics['contract_json_count'] = len(contract_jsons)
    metrics['route_doc_count'] = len(route_docs)
    metrics['contract_doc_count'] = len(contract_docs)
    metrics['starter_doc_count'] = len(starter_docs)
    metrics['launcher_doc_count'] = len(launcher_docs)

    if len(route_docs) < len(route_jsons):
        errors.append('lightweight route docs are incomplete')
    if len(contract_docs) < len(contract_jsons):
        errors.append('lightweight contract docs are incomplete')

    contract_ids = {json.loads(path.read_text(encoding='utf-8'))['task_id'] for path in contract_jsons}
    launcher_titles = set()

    for path in route_jsons:
        data = json.loads(path.read_text(encoding='utf-8'))
        doc_path = dist / 'runtime' / 'route_cards' / f"{data['route_id']}.md"
        if not doc_path.exists():
            errors.append(f'missing lightweight route doc: {doc_path.relative_to(root)}')
            continue
        doc_text = doc_path.read_text(encoding='utf-8')
        if '## Route fit' not in doc_text:
            errors.append(f'route doc missing route-fit section: {doc_path.name}')
        if data['task_id'] in contract_ids and f"dist/runtime/contracts_lite/{data['task_id']}.md" not in doc_text:
            errors.append(f'route doc missing contract pointer: {doc_path.name}')
        if re.search(r'^- Use when:\s*$', doc_text, flags=re.M):
            errors.append(f'route doc contains empty use-when text: {doc_path.name}')
        for skill in data.get('governing_skills', []):
            if skill not in doc_text:
                warnings.append(f'route doc may not surface governing skill clearly: {doc_path.name} -> {skill}')
        if data.get('lightweight_eligible', False) and data['task_id'] in contract_ids:
            starter_path = dist / 'runtime' / 'starters' / f"{data['task_id']}.md"
            launcher_path = dist / 'runtime' / 'task_launchers' / f"{data['task_id']}.md"
            if not starter_path.exists():
                errors.append(f'missing lightweight starter pack: {starter_path.relative_to(root)}')
            if not launcher_path.exists():
                errors.append(f'missing single-file task launcher: {launcher_path.relative_to(root)}')
            else:
                launcher_text = launcher_path.read_text(encoding='utf-8')
                launcher_titles.add(data['task_id'])
                for required in ['## Startup path', '## Route logic', '## Output expectations', '## Kickoff behavior']:
                    if required not in launcher_text:
                        errors.append(f'launcher missing {required}: {launcher_path.name}')
                if 'SESSION_ZERO' not in launcher_text:
                    errors.append(f'launcher missing session-zero behavior: {launcher_path.name}')

    for path in contract_jsons:
        data = json.loads(path.read_text(encoding='utf-8'))
        doc_path = dist / 'runtime' / 'contracts_lite' / f"{data['task_id']}.md"
        if not doc_path.exists():
            errors.append(f'missing lightweight contract doc: {doc_path.relative_to(root)}')
            continue
        doc_text = doc_path.read_text(encoding='utf-8')
        for section in data.get('required_sections', [])[:2]:
            sec_name = section.get('name', section) if isinstance(section, dict) else section
            if sec_name not in doc_text:
                warnings.append(f'contract doc may not surface required sections clearly: {doc_path.name}')
                break

    lite_index = dist / 'runtime' / 'lite_index.json'
    if not lite_index.exists():
        errors.append('missing dist/runtime/lite_index.json')
    else:
        index = json.loads(lite_index.read_text(encoding='utf-8'))
        metrics['lite_index_route_count'] = len(index.get('routes', {}))
        if metrics['lite_index_route_count'] != len(route_jsons):
            errors.append('lite_index route count does not match runtime route count')

    launchers_index = dist / 'runtime' / 'launchers_index.json'
    if launchers_index.exists():
        launcher_index = json.loads(launchers_index.read_text(encoding='utf-8'))
        metrics['launchers_index_count'] = len(launcher_index.get('launchers', {}))
        if metrics['launchers_index_count'] < len(launcher_titles):
            errors.append('launchers_index count does not match generated launcher count')
    else:
        errors.append('missing dist/runtime/launchers_index.json')

    op_quick = (root / 'docs' / 'operator' / 'OPERATOR_QUICKSTART.md').read_text(encoding='utf-8') if (root / 'docs' / 'operator' / 'OPERATOR_QUICKSTART.md').exists() else ''
    if 'dist/runtime/START_HERE.md' not in op_quick:
        errors.append('operator quickstart does not mention dist/runtime/START_HERE.md')

    route_picker = (root / 'docs' / 'operator' / 'ROUTE_PICKER.md').read_text(encoding='utf-8') if (root / 'docs' / 'operator' / 'ROUTE_PICKER.md').exists() else ''
    if re.search(r'^- Use when:\s*$', route_picker, flags=re.M):
        errors.append('route picker contains an empty use-when line')
    if 'dist/runtime/task_launchers/' not in route_picker:
        errors.append('route picker does not point operators to single-file task launchers')

    quickstart = (root / 'docs' / 'operator' / 'DEPLOYMENT_GUIDE.md').read_text(encoding='utf-8') if (root / 'docs' / 'operator' / 'DEPLOYMENT_GUIDE.md').exists() else ''
    if 'Start broad, then narrow.' not in quickstart:
        errors.append('lightweight quickstart does not frame route selection from broad to specialized')
    if 'single-file launcher' not in quickstart.lower():
        errors.append('lightweight quickstart does not teach launcher-first startup')
    if 'dist/runtime/skills/' in quickstart:
        errors.append('lightweight quickstart still sends normal operators into raw runtime skill card paths')

    report = build_report(
        'validate_lightweight_path',
        issues_from_legacy(errors=errors, warnings=warnings, source='scripts/validate_lightweight_path.py'),
        metrics=metrics,
    )
    write_report(dist / 'lightweight_validation_report.json', report)
    return report



def main() -> None:
    report = validate_lightweight_path()
    print_report(report)
    raise SystemExit(exit_code_for(report))


if __name__ == '__main__':
    main()
