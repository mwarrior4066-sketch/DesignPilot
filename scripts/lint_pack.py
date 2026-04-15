#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from _validation import build_report, exit_code_for, issues_from_legacy, print_report, write_report

VERSION_RE = re.compile(r'^\d+\.\d+(?:\.\d+)?$')
MIRROR_DOCS = {
    'src/operator/governance/OUTPUT_CONTRACTS_BY_TASK.md': 120,
    'src/operator/governance/RUNTIME_VALIDATION_LAYER.md': 35,
    'src/operator/core/ROUTE_CATALOG.md': 80,
    'src/operator/governance/PACK_QUALITY_RUBRIC.md': 12,
}
PLACEHOLDER_PATTERNS = ['placeholder', 'tbd', 'lorem ipsum', 'route is explicit', 'required sections are visible']

EM_DASH_SCAN_PATHS = [
    'QUICKSTART.md',
    'README.md',
    'src/operator/**/*.md',
    'src/skills/*.md',
    'docs/operator/**/*.md',
    'dist/**/*.md',
]


def check_frontmatter(path: Path, required_fields):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return [f'{path.relative_to(ROOT)} missing frontmatter'], []
    end = text.find('\n---', 3)
    if end == -1:
        return [f'{path.relative_to(ROOT)} frontmatter not closed'], []
    raw = text[3:end]
    errors, warnings = [], []
    for field in required_fields:
        if f'{field}:' not in raw:
            errors.append(f'{path.relative_to(ROOT)} missing {field}')
    m = re.search(r'last_updated:\s*(\d{4}-\d{2}-\d{2})', raw)
    if not m:
        errors.append(f'{path.relative_to(ROOT)} missing valid last_updated')
    else:
        age = (date.today() - datetime.strptime(m.group(1), '%Y-%m-%d').date()).days
        if age > 365:
            warnings.append(f'{path.relative_to(ROOT)} last_updated is older than 365 days')
    return errors, warnings


def startup_conflict_checks(pack_root: Path):
    errors = []
    mco = (pack_root / 'src' / 'operator' / 'core' / 'MASTER_CHAT_OPERATOR.md').read_text(encoding='utf-8').lower()
    sp = (pack_root / 'src' / 'operator' / 'governance' / 'SYSTEM_PRECEDENCE.md').read_text(encoding='utf-8').lower()
    boot = (pack_root / 'src' / 'runtime' / 'boot' / 'core_bootstrap.md').read_text(encoding='utf-8').lower()
    if 'single startup authority' not in mco:
        errors.append('MASTER_CHAT_OPERATOR.md does not declare single startup authority')
    forbidden_sp = ['startup load boundary', 'cold start sequence', 'minimum viable bootstrap set should be active']
    for phrase in forbidden_sp:
        if phrase in sp:
            errors.append(f'SYSTEM_PRECEDENCE.md still contains startup language: {phrase}')
    if 'master_chat_operator.md' not in boot:
        errors.append('runtime boot file does not point back to MASTER_CHAT_OPERATOR.md')
    return errors


def continuity_version_checks(pack_root: Path, version: str):
    errors = []
    current_files = {
        'projects/designpilot/context/ACTIVE_STATE.md': [f'- Current release: v{version}', 'Manifest status: canonical'],
        'projects/designpilot/context/TASK_QUEUE.md': [f'synchronize v{version} release authority'],
        'projects/designpilot/context/CASE_STUDY_ROADMAP.md': [f'- Current release line: v{version}'],
    }
    for rel, required_snippets in current_files.items():
        text = (pack_root / rel).read_text(encoding='utf-8')
        for snippet in required_snippets:
            if snippet not in text:
                errors.append(f'continuity file out of sync: {rel} missing {snippet}')
    index_files = [
        'src/knowledge-base/indices/source_doc_sections.json',
        'src/knowledge-base/indices/runtime_summary_map.json',
    ]
    for rel in index_files:
        data = json.loads((pack_root / rel).read_text(encoding='utf-8'))
        if data.get('pack_version') != version:
            errors.append(f'index metadata version mismatch: {rel}')
    return errors


def lint_pack(pack_root: Path | str = ROOT) -> dict:
    pack_root = Path(pack_root).resolve()
    errors, warnings, infos = [], [], []

    manifest = json.loads((pack_root / 'PACK_MANIFEST.json').read_text(encoding='utf-8'))
    version = manifest.get('version')
    if not VERSION_RE.match(str(version or '')):
        errors.append(f'manifest version invalid: {version}')
    readme = (pack_root / 'README.md').read_text(encoding='utf-8')
    if f'v{version}' not in readme:
        errors.append('README version mismatch')
    changelog = (pack_root / 'CHANGELOG.md').read_text(encoding='utf-8')
    if f'## v{version}' not in changelog:
        errors.append('CHANGELOG missing current version entry')
    if manifest.get('canonical_entrypoint') not in {'dist/DESIGNPILOT_DEPLOY.md', 'src/operator/core/MASTER_CHAT_OPERATOR.md'}:
        errors.append('manifest canonical_entrypoint should point to dist/DESIGNPILOT_DEPLOY.md or src/operator/core/MASTER_CHAT_OPERATOR.md')

    registry_path = pack_root / 'src' / 'operator' / 'reference' / 'SOURCE_REFERENCE_REGISTRY.json'
    if not registry_path.exists():
        errors.append('SOURCE_REFERENCE_REGISTRY.json missing')
    else:
        registry = json.loads(registry_path.read_text(encoding='utf-8'))
        registered = {e['path'] for e in registry.get('entries', [])}
        must_cover = []
        for pattern in ['src/schemas/*.json', 'src/skills/*.md', 'src/templates/*.md', 'src/knowledge-base/summaries/*.md', 'src/knowledge-base/source-docs/*']:
            must_cover.extend([p.relative_to(pack_root).as_posix() for p in pack_root.glob(pattern) if p.is_file()])
        missing_registry = sorted([p for p in must_cover if p not in registered])
        if missing_registry:
            errors.append('source registry incomplete: ' + ', '.join(missing_registry[:10]))

    for rel, min_lines in MIRROR_DOCS.items():
        path = pack_root / rel
        if not path.exists():
            errors.append(f'mirror doc missing: {rel}')
            continue
        lines = len(path.read_text(encoding='utf-8').splitlines())
        if lines < min_lines:
            errors.append(f'mirror doc too thin: {rel} ({lines} < {min_lines})')

    for folder, required in [
        ('src/skills', ['skill_version', 'source_reference', 'last_updated', 'synchronized', 'canonical_owner', 'domain']),
        ('src/knowledge-base/summaries', ['summary_version', 'source_reference', 'last_updated', 'synchronized', 'domain'])
    ]:
        for path in (pack_root / folder).glob('*.md'):
            e, w = check_frontmatter(path, required)
            errors.extend(e)
            warnings.extend(w)

    for pattern in EM_DASH_SCAN_PATHS:
        for path in pack_root.glob(pattern):
            if not path.is_file():
                continue
            text = path.read_text(encoding='utf-8', errors='ignore')
            if '—' in text:
                errors.append(f'em dash found in AI-facing file: {path.relative_to(pack_root)}')

    for folder in ['examples', 'projects/designpilot', 'tests/evals']:
        for path in (pack_root / folder).rglob('*'):
            if not path.is_file() or path.suffix not in {'.md', '.json'}:
                continue
            text = path.read_text(encoding='utf-8', errors='ignore').lower()
            for pat in PLACEHOLDER_PATTERNS:
                if pat in text:
                    errors.append(f'placeholder-like text found in {path.relative_to(pack_root)}: {pat}')
                    break

    required_examples = set(manifest.get('example_registry', []))
    missing_examples = [rel for rel in required_examples if not (pack_root / rel).exists()]
    if missing_examples:
        errors.append('example coverage incomplete: ' + ', '.join(missing_examples))

    for rel in [
        'projects/designpilot/process/reviews/benchmarks/benchmark-run-001.json',
        'projects/designpilot/finalized/deliverables/proof/PROOF_STACK_SUMMARY.md'
    ]:
        if not (pack_root / rel).exists():
            errors.append(f'missing flagship proof artifact: {rel}')

    for rel in ['src/operator/protocols/DEGRADED_MODE_PROTOCOL.md', 'src/operator/protocols/VISUAL_INPUT_PROTOCOL.md', 'src/operator/protocols/LIGHTWEIGHT_RESPONSE_PROTOCOL.md', 'QUICKSTART.md', 'src/operator/core/SESSION_CONTEXT_DEFAULTS.md']:
        if not (pack_root / rel).exists():
            errors.append(f'missing v2.5.0 control file: {rel}')

    # V4: Warn on decisions with fewer than 4 any_of tokens -- likely undetectable
    contracts_path = pack_root / 'src' / 'schemas' / 'task_contracts.json'
    if contracts_path.exists():
        contracts = json.loads(contracts_path.read_text(encoding='utf-8'))
        for task in contracts.get('tasks', []):
            for dec in task.get('required_decisions', []):
                n = len(dec.get('any_of', []))
                if n < 4:
                    warnings.append(
                        f"decision '{dec['id']}' in '{task['task_id']}' has {n} any_of token(s) "
                        f"(minimum 4 recommended) -- may not be reliably detectable"
                    )

    # V5: Warn if section_aliases.json is missing or doesn't cover all required sections
    aliases_path = pack_root / 'src' / 'schemas' / 'section_aliases.json'
    if not aliases_path.exists():
        errors.append('section_aliases.json missing -- add src/schemas/section_aliases.json')
    else:
        aliases = json.loads(aliases_path.read_text(encoding='utf-8')).get('aliases', {})
        if contracts_path.exists():
            for task in contracts.get('tasks', []):
                for sec in task.get('required_sections', []):
                    name = sec.get('name', sec) if isinstance(sec, dict) else sec
                    if name.lower() not in aliases:
                        warnings.append(
                            f"required section '{name}' in '{task['task_id']}' has no entry in "
                            f"section_aliases.json -- add aliases to improve model heading matching"
                        )

    errors.extend(startup_conflict_checks(pack_root))
    errors.extend(continuity_version_checks(pack_root, version))

    pyc = list(pack_root.rglob('*.pyc'))
    if pyc:
        warnings.append(f'compiled artifacts present: {len(pyc)} .pyc files')
    if (pack_root / '__pycache__').exists():
        warnings.append('__pycache__ directory present')

    report = build_report(
        'lint_pack',
        issues_from_legacy(errors=errors, warnings=warnings, infos=infos, source='scripts/lint_pack.py'),
        metrics={'version': version, 'required_examples': len(required_examples), 'missing_examples': len(missing_examples)},
    )
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('pack_root', nargs='?', default='.')
    parser.add_argument('--strict', action='store_true', help='Deprecated; errors already fail by default. Kept for compatibility.')
    args = parser.parse_args()
    report = lint_pack(Path(args.pack_root))
    write_report(Path(args.pack_root).resolve() / 'dist' / 'lint_pack_report.json', report)
    print_report(report)
    raise SystemExit(exit_code_for(report))


if __name__ == '__main__':
    main()
