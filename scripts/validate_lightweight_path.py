#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'


def validate_lightweight_path(root: Path = ROOT) -> dict:
    dist = root / 'dist'
    errors = []
    warnings = []
    metrics = {}

    required_files = [
        dist / 'DEPLOY_LITE.md',
        dist / 'SESSION_ZERO.md',
        root / 'docs' / 'operator' / 'LIGHTWEIGHT_QUICKSTART.md',
        root / 'docs' / 'operator' / 'STARTUP_MODES.md',
        root / 'docs' / 'operator' / 'ROUTE_PICKER.md',
    ]
    for path in required_files:
        if not path.exists():
            errors.append(f'missing required lightweight artifact: {path.relative_to(root)}')

    lite_text = (dist / 'DEPLOY_LITE.md').read_text(encoding='utf-8') if (dist / 'DEPLOY_LITE.md').exists() else ''
    lite_words = len(lite_text.split())
    metrics['lite_word_count'] = lite_words
    if lite_words < 120:
        errors.append('DEPLOY_LITE.md is too thin to be a meaningful bootstrap')
    if lite_words > 1400:
        warnings.append('DEPLOY_LITE.md is heavier than expected for lightweight startup')

    route_jsons = sorted((root / 'src' / 'runtime' / 'cards' / 'routes').glob('*.json'))
    contract_jsons = sorted((root / 'src' / 'runtime' / 'cards' / 'contracts').glob('*.json'))
    route_docs = sorted((dist / 'lite_routes').glob('*.md'))
    contract_docs = sorted((dist / 'lite_contracts').glob('*.md'))
    starter_docs = sorted((dist / 'lite_starters').glob('*.md'))

    metrics['route_json_count'] = len(route_jsons)
    metrics['contract_json_count'] = len(contract_jsons)
    metrics['route_doc_count'] = len(route_docs)
    metrics['contract_doc_count'] = len(contract_docs)
    metrics['starter_doc_count'] = len(starter_docs)

    if len(route_docs) < len(route_jsons):
        errors.append('lightweight route docs are incomplete')
    if len(contract_docs) < len(contract_jsons):
        errors.append('lightweight contract docs are incomplete')

    contract_ids = {json.loads(path.read_text(encoding='utf-8'))['task_id'] for path in contract_jsons}

    for path in route_jsons:
        data = json.loads(path.read_text(encoding='utf-8'))
        doc_path = dist / 'lite_routes' / f"{data['route_id']}.md"
        if not doc_path.exists():
            errors.append(f'missing lightweight route doc: {doc_path.relative_to(root)}')
            continue
        doc_text = doc_path.read_text(encoding='utf-8')
        if '## Route fit' not in doc_text:
            errors.append(f'route doc missing route-fit section: {doc_path.name}')
        if data['task_id'] in contract_ids and f"dist/lite_contracts/{data['task_id']}.md" not in doc_text:
            errors.append(f'route doc missing contract pointer: {doc_path.name}')
        if re.search(r'^- Use when:\s*$', doc_text, flags=re.M):
            errors.append(f'route picker or route doc contains empty use-when text: {doc_path.name}')
        if '## Use when' in doc_text and '- Use this route when its task is the real governing failure.' in doc_text:
            warnings.append(f'route doc uses fallback placeholder wording: {doc_path.name}')
        for skill in data.get('governing_skills', []):
            if skill not in doc_text:
                warnings.append(f'route doc may not surface governing skill clearly: {doc_path.name} -> {skill}')
        if data.get('lightweight_eligible', False) and data['task_id'] in contract_ids:
            starter_path = dist / 'lite_starters' / f"{data['task_id']}.md"
            if not starter_path.exists():
                errors.append(f'missing lightweight starter pack: {starter_path.relative_to(root)}')

    for path in contract_jsons:
        data = json.loads(path.read_text(encoding='utf-8'))
        doc_path = dist / 'lite_contracts' / f"{data['task_id']}.md"
        if not doc_path.exists():
            errors.append(f'missing lightweight contract doc: {doc_path.relative_to(root)}')
            continue
        doc_text = doc_path.read_text(encoding='utf-8')
        for section in data.get('required_sections', [])[:2]:
            if section not in doc_text:
                warnings.append(f'contract doc may not surface required sections clearly: {doc_path.name}')
                break

    lite_index = dist / 'lite_index.json'
    if not lite_index.exists():
        errors.append('missing dist/lite_index.json')
    else:
        index = json.loads(lite_index.read_text(encoding='utf-8'))
        metrics['lite_index_route_count'] = len(index.get('routes', {}))
        if metrics['lite_index_route_count'] != len(route_jsons):
            errors.append('lite_index route count does not match runtime route count')

    op_quick = (root / 'docs' / 'operator' / 'OPERATOR_QUICKSTART.md').read_text(encoding='utf-8') if (root / 'docs' / 'operator' / 'OPERATOR_QUICKSTART.md').exists() else ''
    if 'DEPLOY_LITE.md' not in op_quick:
        errors.append('operator quickstart does not mention DEPLOY_LITE.md')

    route_picker = (root / 'docs' / 'operator' / 'ROUTE_PICKER.md').read_text(encoding='utf-8') if (root / 'docs' / 'operator' / 'ROUTE_PICKER.md').exists() else ''
    if re.search(r'^- Use when:\s*$', route_picker, flags=re.M):
        errors.append('route picker contains an empty use-when line')
    if 'Start broad, then narrow:' not in route_picker:
        errors.append('route picker does not surface broad-to-specialized selection guidance')

    quickstart = (root / 'docs' / 'operator' / 'LIGHTWEIGHT_QUICKSTART.md').read_text(encoding='utf-8') if (root / 'docs' / 'operator' / 'LIGHTWEIGHT_QUICKSTART.md').exists() else ''
    if 'Start broad, then narrow.' not in quickstart:
        errors.append('lightweight quickstart does not frame route selection from broad to specialized')

    decision = 'FAIL' if errors else 'PASS'
    report = {'decision': decision, 'errors': errors, 'warnings': warnings, 'metrics': metrics}
    report_path = dist / 'lightweight_validation_report.json'
    report_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    return report


def main():
    report = validate_lightweight_path()
    print(json.dumps(report, indent=2))
    if report['decision'] == 'FAIL':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
