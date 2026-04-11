#!/usr/bin/env python3
import json, os, re
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent
TODAY = "2026-04-11"

def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')

def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')

def parse_frontmatter(text: str):
    if not text.startswith('---'):
        return {}, text
    end = text.find('\n---', 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip()
    body = text[end+4:].lstrip('\n')
    meta = {}
    current_key = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if re.match(r'^\s*-\s+', line) and current_key:
            meta.setdefault(current_key, []).append(re.sub(r'^\s*-\s+', '', line).strip())
            continue
        if ':' in line:
            k, v = line.split(':', 1)
            current_key = k.strip()
            v = v.strip()
            if not v:
                meta[current_key] = []
            elif v.lower() == 'true':
                meta[current_key] = True
            elif v.lower() == 'false':
                meta[current_key] = False
            else:
                meta[current_key] = v.strip(' "\'')
    return meta, body

def parse_sections(body: str):
    sections = {}
    current = '_root'
    buf = []
    for line in body.splitlines():
        m = re.match(r'^(#{1,6})\s+(.+?)\s*$', line)
        if m:
            sections[current] = '\n'.join(buf).strip()
            current = m.group(2).strip()
            buf = []
        else:
            buf.append(line)
    sections[current] = '\n'.join(buf).strip()
    return sections

def bullets_from_sections(sections, heading_keywords):
    items = []
    for sec_name, content in sections.items():
        if any(key.lower() in sec_name.lower() for key in heading_keywords):
            for line in content.splitlines():
                line = line.strip()
                if re.match(r'^[-*]\s+', line):
                    item = re.sub(r'^[-*]\s+', '', line).strip()
                    if item and item not in items:
                        items.append(item)
            if not items and content.strip():
                for sentence in re.split(r'(?<=[.!?])\s+', content.strip()):
                    sentence = sentence.strip()
                    if sentence and sentence not in items:
                        items.append(sentence)
    return items

def infer_section_type(heading: str) -> str:
    h = heading.lower()
    if any(x in h for x in ['threshold', 'metric', 'score', 'ratio', 'budget']):
        return 'threshold'
    if any(x in h for x in ['anti-pattern', 'failure', 'trap', 'risk', 'error']):
        return 'anti-pattern'
    if any(x in h for x in ['implement', 'workflow', 'logic', 'pattern', 'architecture', 'contract', 'model', 'interaction', 'behavior']):
        return 'implementation'
    if any(x in h for x in ['example', 'case', 'scenario', 'transformation']):
        return 'example'
    if any(x in h for x in ['compare', 'comparison', 'tradeoff', 'trade-off', 'versus', 'matrix']):
        return 'comparison'
    if any(x in h for x in ['validate', 'validator', 'regression', 'criteria']):
        return 'validation'
    return 'principle'

def extract_skill_refs(text: str):
    return sorted(set(re.findall(r'([a-z0-9][a-z0-9\-]+\.md)', text.lower())))

def ensure_list(v):
    if isinstance(v, list):
        return v
    if v is None:
        return []
    return [v]

def main():
    manifest = json.loads(read(ROOT / 'PACK_MANIFEST.json'))
    routes = json.loads(read(ROOT / 'schemas' / 'routing_registry.json'))
    contracts = json.loads(read(ROOT / 'schemas' / 'task_contracts.json'))

    skill_info = {}
    for p in sorted((ROOT / 'skills').glob('*.md')):
        meta, body = parse_frontmatter(read(p))
        sections = parse_sections(body)
        skill_info[p.name] = {'meta': meta, 'sections': sections, 'path': p}

    summary_info = {}
    for p in sorted((ROOT / 'knowledge-base' / 'summaries').glob('*.md')):
        meta, body = parse_frontmatter(read(p))
        sections = parse_sections(body)
        summary_info[p.name] = {'meta': meta, 'sections': sections, 'path': p}

    doc_to_summaries = {}
    for sname, info in summary_info.items():
        refs = [r for r in ensure_list(info['meta'].get('source_reference')) if 'knowledge-base/source-docs/' in r]
        for ref in refs:
            doc_to_summaries.setdefault(os.path.basename(ref), []).append(sname)

    # runtime boot
    write(ROOT / 'runtime' / 'boot' / 'core_bootstrap.md', '\n'.join([
        '# Core Runtime Bootstrap',
        '',
        'This is the thin runtime aide for the pack.',
        'It is not a competing startup authority.',
        'The single startup authority remains `MASTER_CHAT_OPERATOR.md`.',
        '',
        '## Default startup chain',
        '1. `runtime/boot/core_bootstrap.md`',
        '2. `runtime/boot/runtime_precedence.md`',
        '3. selected route card in `runtime/cards/routes/`',
        '4. selected contract card in `runtime/cards/contracts/`',
        '5. required skill cards in `runtime/cards/skills/`',
        '6. required runtime summaries in `knowledge-base/runtime-summaries/`',
        '',
        '## Safe fallback',
        'If any runtime overlay artifact is missing, stale, or ambiguous, fall back immediately to the canonical authority:',
        '- routing: `schemas/routing_registry.json`',
        '- contracts: `schemas/task_contracts.json`',
        '- skills: `skills/*.md`',
        '- summaries: `knowledge-base/summaries/*.md`',
        '- source docs: `knowledge-base/source-docs/*`',
        '',
        '## Runtime promises',
        '- no capability loss',
        '- no source-doc deletion',
        '- no summary deletion',
        '- mirrors are debug-only unless explicitly requested',
    ]))
    write(ROOT / 'runtime' / 'boot' / 'runtime_precedence.md', '\n'.join([
        '# Runtime Precedence',
        '',
        '## Runtime-first overlay',
        'Use the generated runtime overlay as the first hop for token-efficient execution:',
        '1. route card',
        '2. contract card',
        '3. skill cards',
        '4. runtime summary',
        '5. full summary only on escalation',
        '6. indexed source-doc section before full source-doc load',
        '',
        '## Canonical fallback rule',
        'The runtime overlay is an optimization layer only. It is never the sole source of truth.',
        '',
        'If the overlay conflicts with a canonical source, the canonical source wins.',
        '',
        '## Debug-only files',
        'Do not load these at runtime unless debugging, maintaining, or explaining the pack itself:',
        '- `ROUTE_CATALOG.md`',
        '- `OUTPUT_CONTRACTS_BY_TASK.md`',
        '- `SKILL_REFERENCE_MAP.md`',
        '- `RUNTIME_VALIDATION_LAYER.md` as prose explanation only',
        '- `PACK_QUALITY_RUBRIC.md`',
        '- `VALIDATION_RUBRICS.md`',
    ]))

    # route cards + runtime summary map
    runtime_summary_map = {'version': '1.1.0', 'pack_version': manifest['version'], 'routes': {}}
    for route in routes['routes']:
        all_skill_refs = list(route.get('loaded_skills', []))
        for line in route.get('supporting_skills', []):
            for ref in extract_skill_refs(line):
                if ref not in all_skill_refs:
                    all_skill_refs.append(ref)
        primary_summaries = []
        secondary_summaries = []
        for idx, skill_name in enumerate(all_skill_refs):
            if skill_name not in skill_info:
                continue
            refs = ensure_list(skill_info[skill_name]['meta'].get('source_reference'))
            summary_bases = [os.path.basename(r) for r in refs if 'knowledge-base/summaries/' in r]
            if idx < len(route.get('loaded_skills', [])):
                for s in summary_bases:
                    if s not in primary_summaries:
                        primary_summaries.append(s)
            else:
                for s in summary_bases:
                    if s not in primary_summaries and s not in secondary_summaries:
                        secondary_summaries.append(s)
        summary_ids = [f'knowledge-base/runtime-summaries/{s}' for s in primary_summaries + secondary_summaries]
        route_card = {
            'route_id': route['route_id'],
            'task_id': route['task_id'],
            'trigger_summary': route['selection_logic'],
            'governing_skills': route.get('loaded_skills', []),
            'supporting_skills': all_skill_refs[len(route.get('loaded_skills', [])):],
            'required_summary_ids': summary_ids,
            'escalation_conditions': [
                'runtime summary lacks measurable thresholds',
                'validator flags insufficient evidence',
                'high-stakes or standards-grade task',
                'user explicitly requests deeper source synthesis',
                'route conflict or canonical ambiguity appears'
            ],
            'fallback_route': route.get('fallback_route_id'),
            'known_tensions': route.get('known_tensions', []),
            'handoff_targets': sorted(set([route.get('fallback_route_id')] + [r['task_id'] for r in contracts['tasks'] if any(skill in r.get('required_skills', []) for skill in route.get('loaded_skills', []))]))[:12],
            'overlay_safe_fallback': {
                'routing': 'schemas/routing_registry.json',
                'skills': route.get('loaded_skills', []),
                'summaries': primary_summaries + secondary_summaries,
            },
            'task_weight_default': next((t.get('task_weight_default', 'standard') for t in contracts['tasks'] if t['task_id'] == route['task_id']), 'standard'),
            'lightweight_eligible': next((t.get('supports_lightweight_response', True) for t in contracts['tasks'] if t['task_id'] == route['task_id']), True),
            'visual_input_supported': route.get('visual_input_supported', False),
        }
        write(ROOT / 'runtime' / 'cards' / 'routes' / f"{route['route_id']}.json", json.dumps(route_card, indent=2))
        runtime_summary_map['routes'][route['route_id']] = {
            'primary_runtime_summaries': [f'knowledge-base/runtime-summaries/{s}' for s in primary_summaries],
            'secondary_runtime_summaries': [f'knowledge-base/runtime-summaries/{s}' for s in secondary_summaries],
            'forbidden_unrelated_summaries': [],
            'escalation_fallback': {
                'full_summaries': [f'knowledge-base/summaries/{s}' for s in primary_summaries + secondary_summaries],
                'canonical_route': 'schemas/routing_registry.json'
            }
        }

    # contract cards
    for task in contracts['tasks']:
        card = {
            'task_id': task['task_id'],
            'title': task['title'],
            'required_sections': [sec['name'] for sec in task.get('required_sections', [])],
            'required_evidence_types': task.get('required_evidence_types', []),
            'required_decisions': [d['id'] if isinstance(d, dict) else d for d in task.get('required_decisions', [])],
            'hard_fail_patterns': task.get('hard_fail_patterns', []),
            'soft_fail_patterns': task.get('soft_fail_patterns', []),
            'required_skills': task.get('required_skills', []),
            'allowed_modes': task.get('allowed_modes', []),
            'allowed_phases': task.get('allowed_phases', []),
            'canonical_contract': f"schemas/task_contracts.json#{task['task_id']}",
            'task_weight_default': task.get('task_weight_default', 'standard'),
            'supports_lightweight_response': task.get('supports_lightweight_response', True),
            'trace_visibility_default': task.get('trace_visibility_default', 'recoverable'),
        }
        write(ROOT / 'runtime' / 'cards' / 'contracts' / f"{task['task_id']}.json", json.dumps(card, indent=2))

    # skill cards
    for skill_name, info in skill_info.items():
        sections = info['sections']
        refs = ensure_list(info['meta'].get('source_reference'))
        text = '\n'.join([
            '---',
            f"runtime_card_version: 1.0.0",
            f"canonical_skill: skills/{skill_name}",
            f"last_generated: {TODAY}",
            "overlay: true",
            '---',
            f"# {skill_name}",
            '',
            '## Activation conditions',
            *[f"- {x}" for x in bullets_from_sections(sections, ['Activate when'])[:8]],
            '',
            '## Non-activation conditions',
            *[f"- {x}" for x in bullets_from_sections(sections, ['Do not activate when'])[:8]],
            '',
            '## Core decision rules',
            *[f"- {x}" for x in bullets_from_sections(sections, ['Decision rules'])[:10]],
            '',
            '## Failure traps',
            *[f"- {x}" for x in bullets_from_sections(sections, ['Failure traps'])[:8]],
            '',
            '## Summary dependencies',
            *[f"- {os.path.basename(x)}" for x in refs],
            '',
            '## Escalation triggers',
            *[f"- {x}" for x in bullets_from_sections(sections, ['Fallback logic', 'Exception rules', 'Evidence required'])[:8]],
            '',
            '## Adjacent handoff rules',
            *[f"- {x}" for x in bullets_from_sections(sections, ['Handoff to other skills'])[:10]],
            '',
            '## Canonical fallback',
            f"- `skills/{skill_name}`",
            *[f"- `knowledge-base/summaries/{os.path.basename(x)}`" for x in refs],
        ])
        write(ROOT / 'runtime' / 'cards' / 'skills' / skill_name, text)

    # runtime summaries
    for sname, info in summary_info.items():
        sections = info['sections']
        refs = ensure_list(info['meta'].get('source_reference'))
        decision_rules = bullets_from_sections(sections, ['Default rules', 'Decision rules', 'Rules', 'Key outputs'])[:12]
        failure_traps = bullets_from_sections(sections, ['Failure patterns', 'Failure traps', 'Anti-patterns'])[:8]
        use_when = bullets_from_sections(sections, ['Use when'])[:6]
        escalate_when = [
            'the runtime summary lacks exact thresholds, standards wording, or measurable criteria',
            'two summaries or skills conflict and the governing rule is unclear',
            'the validator flags missing evidence classes or insufficient evidence',
            'the task is high-stakes, standards-grade, or audit-sensitive',
            'the user explicitly asks for deep rationale or full-source synthesis'
        ]
        if not decision_rules:
            decision_rules = [x for x in use_when[:6]]
        rt_text = '\n'.join([
            '---',
            'runtime_summary_version: 1.0.0',
            f'canonical_summary: knowledge-base/summaries/{sname}',
            f'last_generated: {TODAY}',
            'overlay: true',
            'source_reference:',
            *[f'  - {x}' for x in refs],
            '---',
            f"# {sname.replace('.md','').replace('-', ' ').title()} Runtime Summary",
            '',
            '## Decision rules',
            *[f"- {x}" for x in (decision_rules or ['No extracted decision rules; fall back to the canonical summary.'])],
            '',
            '## Failure traps',
            *[f"- {x}" for x in (failure_traps or ['No extracted failure traps; fall back to the canonical summary.'])],
            '',
            '## Escalate when',
            *[f"- {x}" for x in escalate_when],
            '',
            '## Canonical fallback',
            f"- `knowledge-base/summaries/{sname}`",
            *[f"- `knowledge-base/source-docs/{os.path.basename(x)}`" for x in refs],
        ])
        write(ROOT / 'knowledge-base' / 'runtime-summaries' / sname, rt_text)

    # source doc sections index
    source_index = {'version': '1.0.0', 'pack_version': manifest['version'], 'documents': []}
    for p in sorted((ROOT / 'knowledge-base' / 'source-docs').iterdir()):
        if p.suffix.lower() == '.pdf':
            doc_entry = {
                'file_name': p.name,
                'linked_summaries': doc_to_summaries.get(p.name, []),
                'sections': [{
                    'heading': p.name,
                    'short_description': 'Binary source media. Load only when the task explicitly needs the PDF asset.',
                    'linked_summary': doc_to_summaries.get(p.name, []),
                    'linked_routes': [],
                    'linked_skills': [],
                    'estimated_token_count': 0,
                    'section_type': 'reference'
                }]
            }
            source_index['documents'].append(doc_entry)
            continue
        meta, body = parse_frontmatter(read(p))
        lines = body.splitlines()
        sections = []
        current_heading = None
        buf = []
        def flush():
            if current_heading is None:
                return
            content = '\n'.join(buf).strip()
            desc = ''
            for line in content.splitlines():
                line = line.strip()
                if line:
                    desc = re.sub(r'^\W+', '', line)[:180]
                    break
            word_count = len(re.findall(r'\w+', content))
            linked_summaries = doc_to_summaries.get(p.name, [])
            linked_skills = []
            linked_routes = []
            for skill_name, sinfo in skill_info.items():
                refs = ensure_list(sinfo['meta'].get('source_reference'))
                if any(os.path.basename(r) in linked_summaries for r in refs):
                    linked_skills.append(skill_name)
            for route in routes['routes']:
                if any(skill in linked_skills for skill in route.get('loaded_skills', [])):
                    linked_routes.append(route['route_id'])
            sections.append({
                'heading': current_heading,
                'short_description': desc or f'Section from {p.name}.',
                'linked_summary': linked_summaries,
                'linked_routes': sorted(set(linked_routes)),
                'linked_skills': sorted(set(linked_skills)),
                'estimated_token_count': max(1, round(word_count * 1.3)),
                'section_type': infer_section_type(current_heading)
            })
        for line in lines:
            m = re.match(r'^(#{1,6})\s+(.+?)\s*$', line)
            if m:
                flush()
                current_heading = m.group(2).strip()
                buf = []
            else:
                buf.append(line)
        flush()
        if not sections:
            sections = [{
                'heading': 'Overview',
                'short_description': body.strip()[:180] or f'Overview for {p.name}.',
                'linked_summary': doc_to_summaries.get(p.name, []),
                'linked_routes': [],
                'linked_skills': [],
                'estimated_token_count': max(1, round(len(re.findall(r'\w+', body)) * 1.3)),
                'section_type': 'principle'
            }]
        source_index['documents'].append({
            'file_name': p.name,
            'linked_summaries': doc_to_summaries.get(p.name, []),
            'sections': sections
        })

    write(ROOT / 'knowledge-base' / 'indices' / 'source_doc_sections.json', json.dumps(source_index, indent=2))
    write(ROOT / 'knowledge-base' / 'indices' / 'source_section_map.json', json.dumps(source_index, indent=2))
    write(ROOT / 'knowledge-base' / 'indices' / 'runtime_summary_map.json', json.dumps(runtime_summary_map, indent=2))

    token_budget = {
        'version': '1.0.0',
        'pack_version': manifest['version'],
        'layer_budgets': {
            'boot': {'max_files': 2, 'preferred': ['runtime/boot/core_bootstrap.md', 'runtime/boot/runtime_precedence.md']},
            'route_contract': {'max_files': 2, 'rule': 'load one route card and one contract card'},
            'skill_cards': {'max_files': 3, 'rule': 'load only required skill cards unless a justification note exists'},
            'runtime_summaries': {'max_files': 2, 'rule': 'load the mapped runtime summaries first'},
            'deep_summaries': {'max_files': 2, 'rule': 'load only on escalation'},
            'source_sections': {'max_files': 2, 'rule': 'prefer indexed sections over full source docs'},
            'full_source_docs': {'max_files': 1, 'rule': 'rare, explicit, or high-stakes only'}
        },
        'flag_conditions': [
            'full summary loaded when runtime summary would have sufficed',
            'full source doc loaded when a section was available',
            'human-readable mirror loaded when schema or card would have sufficed',
            'more than three skill cards loaded without justification',
            'unrelated summaries loaded just in case'
        ]
    }
    write(ROOT / 'runtime' / 'loading' / 'token_budget_registry.json', json.dumps(token_budget, indent=2))

    hydration_schema = {
        'schema_version': '1.0.0',
        'description': 'Records runtime hydration choices by layer so the overlay can be audited for token efficiency.',
        'required_fields': [
            'task_id',
            'route_card',
            'contract_card',
            'skill_cards',
            'runtime_summaries',
            'deep_summaries_loaded',
            'source_doc_sections_loaded',
            'full_source_docs_loaded',
            'estimated_token_budget',
            'justification_notes'
        ],
        'field_types': {
            'task_id': 'string',
            'route_card': 'string',
            'contract_card': 'string',
            'skill_cards': 'array[string]',
            'runtime_summaries': 'array[string]',
            'deep_summaries_loaded': 'array[string]',
            'source_doc_sections_loaded': 'array[object]',
            'full_source_docs_loaded': 'array[string]',
            'estimated_token_budget': 'object',
            'justification_notes': 'array[string]'
        }
    }
    write(ROOT / 'runtime' / 'loading' / 'hydration_trace_schema.json', json.dumps(hydration_schema, indent=2))

    print('generated runtime overlay artifacts')

if __name__ == '__main__':
    main()
