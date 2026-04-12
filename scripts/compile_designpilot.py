#!/usr/bin/env python3
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
DOCS_OPERATOR = ROOT / 'docs' / 'operator'
EXAMPLES_LIGHT = ROOT / 'examples' / 'lightweight'
CONFIG = ROOT / 'config' / 'deploy_manifest.yaml'
PROFILE_CONFIG = ROOT / 'config' / 'profile_map.yaml'

for path in [DIST, DOCS_OPERATOR, EXAMPLES_LIGHT, DIST / 'lite_routes', DIST / 'lite_contracts', DIST / 'lite_starters']:
    path.mkdir(parents=True, exist_ok=True)


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def words(text: str) -> int:
    return len(text.split())


def token_estimate(text: str) -> int:
    return max(1, round(len(text) / 4))


def parse_frontmatter(text: str):
    if not text.startswith('---'):
        return {}, text
    end = text.find('\n---', 3)
    if end == -1:
        return {}, text
    raw = text[3:end]
    body = text[end + 4:].lstrip('\n')
    try:
        meta = yaml.safe_load(raw) or {}
        if not isinstance(meta, dict):
            meta = {}
    except Exception:
        meta = {}
    return meta, body


def slug_title(value: str) -> str:
    value = value.replace('rt_', '').replace('.md', '').replace('_', ' ').replace('-', ' ').strip()
    return ' '.join(part.capitalize() for part in value.split())


def bullet_list(items):
    return [f'- {item}' for item in items] if items else ['- none']


def skill_purpose(path: Path):
    text = read(path)
    meta, body = parse_frontmatter(text)
    purpose = ''
    lines = body.splitlines()
    for idx, line in enumerate(lines):
        if line.strip().lower() == '## purpose':
            for j in range(idx + 1, len(lines)):
                if lines[j].startswith('## '):
                    break
                if lines[j].strip():
                    purpose = lines[j].strip()
                    break
            break
    if not purpose:
        purpose = str(meta.get('domain', path.stem)).replace('-', ' ')
    return path.stem, purpose


def excerpt_from_file(rel_path: str) -> str:
    path = ROOT / rel_path
    text = read(path)
    _, body = parse_frontmatter(text)
    return f"### Source: `{rel_path}`\n\n{body.strip()}\n"


def compact_protocol_summary(rel_path: str) -> list[str]:
    path = ROOT / rel_path
    text = read(path)
    _, body = parse_frontmatter(text)
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    out = []
    for line in lines:
        if line.startswith('#'):
            continue
        if line.startswith('- '):
            out.append(line[2:].strip())
        elif line[:2].isdigit() and '. ' in line:
            out.append(line)
        else:
            out.append(line)
        if len(out) >= 5:
            break
    return out


def load_runtime_routes() -> list[dict]:
    route_dir = ROOT / 'src' / 'runtime' / 'cards' / 'routes'
    return sorted([json.loads(p.read_text(encoding='utf-8')) for p in route_dir.glob('*.json')], key=lambda x: x['route_id'])


def load_runtime_contracts() -> list[dict]:
    contract_dir = ROOT / 'src' / 'runtime' / 'cards' / 'contracts'
    return sorted([json.loads(p.read_text(encoding='utf-8')) for p in contract_dir.glob('*.json')], key=lambda x: x['task_id'])


def recommend_profile(route: dict, profiles: dict) -> str:
    governing = set(route.get('governing_skills', []) + route.get('supporting_skills', []))
    scores = []
    for name, profile in profiles.items():
        overlap = len(governing & set(profile.get('skill_files', [])))
        scores.append((overlap, name))
    scores.sort(reverse=True)
    return scores[0][1] if scores and scores[0][0] else 'core'


def build_kernel(config, profiles):
    lines = [
        '# DESIGNPILOT_DEPLOY',
        '',
        'This is the compiled DesignPilot deployment kernel.',
        'It is the operator-facing constitution, routing spine, and fallback surface.',
        '',
        '## Startup modes',
        '- Full mode: load this kernel, add one profile, then start with `dist/SESSION_ZERO.md`.',
        '- Profile-only mode: skip the kernel for narrow single-domain work and load one profile plus `dist/SESSION_ZERO.md`.',
        '- Lightweight mode: use `dist/DEPLOY_LITE.md` plus one route card, one contract card, the needed skill cards, and `dist/SESSION_ZERO.md`.',
        '',
        '## Stable rules',
        '- one governing route per substantial task',
        '- supporting skills sharpen the answer but do not replace the governing evidence burden',
        '- fail closed when ambiguity affects proof honesty, feasibility, or safety',
        '- use the narrowest correct startup mode for the task',
        '- escalate from lite to profile to kernel when the task stops being safely bounded',
        '',
        '## Included source anchors',
        ''
    ]
    for rel in config['kernel_files']:
        lines.append(excerpt_from_file(rel))
    lines.append('## Skill registry')
    lines.append('')
    for profile_name, profile in profiles.items():
        lines.append(f"### {profile_name.upper()}")
        lines.append(profile.get('description', '').strip())
        lines.append('')
        for skill_file in profile.get('skill_files', []):
            _, purpose = skill_purpose(ROOT / 'src' / 'skills' / skill_file)
            lines.append(f"- `{skill_file}` - {purpose}")
        lines.append('')
    return '\n'.join(lines).strip() + '\n'


def build_profile(name, profile):
    header = [
        f"# DEPLOY_{name.upper()}",
        '',
        profile.get('description', '').strip(),
        '',
        '## Supported use',
        '- full mode: load this profile with `dist/DESIGNPILOT_DEPLOY.md` for compound work inside this domain',
        '- profile-only mode: load just this profile with `dist/SESSION_ZERO.md` for focused single-domain work',
        '',
        '## Profile rules',
        '- keep one governing route visible',
        '- do not load another profile unless the task truly spans domains',
        '- switch to the kernel when cross-domain coordination, proof sensitivity, or competing constraints rise',
        '',
        '## Included skills',
        ''
    ]
    for skill_file in profile.get('skill_files', []):
        title, purpose = skill_purpose(ROOT / 'src' / 'skills' / skill_file)
        header.append(f"### {title}")
        header.append('')
        header.append(f"- Source: `src/skills/{skill_file}`")
        header.append(f"- Purpose: {purpose}")
        header.append('')
    if profile.get('extra_sources'):
        header.extend(['## Supporting source anchors', ''])
        for rel in profile['extra_sources']:
            header.append(excerpt_from_file(rel))
    return '\n'.join(header).strip() + '\n'


def build_lite(config):
    lines = [
        '# DEPLOY_LITE',
        '',
        'DesignPilot lite mode is the narrow startup path for bounded single-route work.',
        'Use it when one route clearly governs the task and loading a full profile or the kernel would be unnecessary overhead.',
        '',
        '## What lite mode is for',
        '- single-domain tasks with one honest governing route',
        '- low-to-medium risk work where the output shape is already known',
        '- sessions where you want DesignPilot discipline without loading the whole package',
        '',
        '## What to load',
        '1. `dist/DEPLOY_LITE.md`',
        '2. one route card from `dist/lite_routes/`',
        '3. the matching contract card from `dist/lite_contracts/`',
        '4. only the governing skill cards and truly needed supporting skill cards',
        '5. `dist/SESSION_ZERO.md`',
        '',
        '## What lite mode keeps',
        '- DesignPilot identity and claim-boundary honesty',
        '- one-governing-route discipline',
        '- explicit escalation when the task stops being safely bounded',
        '- canonical fallback to source schemas, source skills, and full summaries',
        '',
        '## What lite mode does not try to do',
        '- replace the kernel for compound work',
        '- settle cross-domain routing conflicts by itself',
        '- carry the full governance surface for remediation, architecture, or release-sensitive work',
        '- hide uncertainty when the correct answer is to escalate',
        '',
        '## Lite operating rules',
        '- stay inside one honest route',
        '- use the route card to decide the task fit before loading extra skills',
        '- use the contract card to define what done looks like',
        '- add supporting skills only when they materially change the answer',
        '- fail closed and escalate rather than improvising missing logic',
        '',
        '## Escalate to a profile or the kernel when',
        '- more than one route could honestly govern the task',
        '- architecture, remediation, release readiness, or proof sensitivity becomes central',
        '- accessibility semantics, PDF structure, or back-end feasibility are high-stakes',
        '- the route card or contract card marks the task as unsafe for lightweight execution',
        '- the answer would otherwise hide uncertainty or overclaim confidence',
        '',
        '## Canonical fallback sources',
        '- routing: `src/schemas/routing_registry.json`',
        '- contracts: `src/schemas/task_contracts.json`',
        '- skills: `src/skills/*.md`',
        '- summaries: `src/knowledge-base/summaries/*.md`',
        '',
        '## Source anchors behind lite mode',
        *[f'- `{rel}`' for rel in config.get('lite_files', [])],
    ]
    return '\n'.join(lines).strip() + '\n'


def build_session_zero(profiles):
    profile_list = ', '.join(f"`{p}`" for p in profiles)
    return f'''# SESSION_ZERO

I am starting a DesignPilot session.

Please do the following before answering in depth:
1. confirm what deploy files appear to be loaded
2. identify the most likely work type and governing route
3. tell me whether this looks like a `lightweight`, `profile-only`, or `full` startup
4. tell me whether the active profile should be one of {profile_list}
5. ask only for the minimum missing context that would materially change routing, proof honesty, or implementation realism
6. do not explain internal architecture unless I ask for it
'''


def contract_for_route(route: dict, contract_map: dict) -> dict:
    return contract_map.get(route['task_id'], {
        'task_id': route['task_id'],
        'title': slug_title(route.get('task_id') or route['route_id']),
        'required_sections': [],
        'required_evidence_types': [],
        'required_decisions': [],
        'hard_fail_patterns': [],
        'soft_fail_patterns': [],
        'supports_lightweight_response': False,
        'task_weight_default': route.get('task_weight_default', 'standard'),
        'allowed_modes': [],
        'allowed_phases': [],
        'canonical_contract': 'src/schemas/task_contracts.json',
    })


def build_route_doc(route: dict, contract: dict, profiles: dict) -> str:
    route_title = contract.get('title') or slug_title(route['route_id'])
    recommended_profile = recommend_profile(route, profiles)
    use_when = route.get('trigger_summary') or f"Use when {route_title.lower()} is the governing job."
    if route.get('role') == 'prepass':
        use_when = 'Use this route only to extract visual evidence before selecting the real governing route.'
    is_contract_backed = bool(contract.get('required_sections'))
    recommended_mode = 'lightweight' if route.get('lightweight_eligible', False) and is_contract_backed else 'profile or full'
    lines = [
        f"# {route['route_id']}",
        '',
        f"**Task:** {route_title}",
        '',
        '## Route fit',
        f"- Role: {route.get('role', 'governing')}",
        f"- Lightweight eligible: {'yes' if route.get('lightweight_eligible', False) and is_contract_backed else 'no'}",
        f"- Governing route or helper: {'helper / pre-pass' if route.get('role') == 'prepass' else 'governing route'}",
        '',
        '## Use when',
        f"- {use_when}",
        '',
        '## Startup recommendation',
        f"- Recommended mode: {recommended_mode}",
        f"- Default contract: `dist/lite_contracts/{route['task_id']}.md`" if is_contract_backed else '- Default contract: no dedicated task contract; treat this as a pre-pass helper and escalate quickly',
        f"- Recommended profile if you escalate: `dist/DEPLOY_{recommended_profile.upper()}.md`",
        f"- Visual input supported: {'yes' if route.get('visual_input_supported') else 'no'}",
        '',
        '## Governing skills',
    ]
    for skill_file in route.get('governing_skills', []):
        _, purpose = skill_purpose(ROOT / 'src' / 'skills' / skill_file)
        lines.append(f"- `src/runtime/cards/skills/{skill_file}` — {purpose}")
    lines.extend(['', '## Optional supporting skills'])
    for skill_file in route.get('supporting_skills', []):
        _, purpose = skill_purpose(ROOT / 'src' / 'skills' / skill_file)
        lines.append(f"- `src/runtime/cards/skills/{skill_file}` — {purpose}")
    lines.extend(['', '## Runtime summaries'])
    lines.extend(bullet_list([f"`{summary}`" for summary in route.get('required_summary_ids', [])]))
    lines.extend(['', '## Contract shape'])
    lines.extend(bullet_list(contract.get('required_sections', [])))
    lines.extend(['', '## Escalate when'])
    lines.extend(bullet_list(route.get('escalation_conditions', [])))
    lines.extend(['', '## Fallback'])
    lines.append(f"- Route fallback: `{route.get('fallback_route')}`" if route.get('fallback_route') else '- Route fallback: none')
    lines.append(f"- Canonical routing fallback: `{route.get('overlay_safe_fallback', {}).get('routing', 'src/schemas/routing_registry.json')}`")
    return '\n'.join(lines).strip() + '\n'


def build_contract_doc(contract: dict) -> str:
    lines = [
        f"# {contract['task_id']}",
        '',
        f"**Title:** {contract.get('title', slug_title(contract['task_id']))}",
        '',
        '## Required sections',
    ]
    lines.extend(bullet_list(contract.get('required_sections', [])))
    lines.extend(['', '## Required evidence types'])
    lines.extend(bullet_list(contract.get('required_evidence_types', [])))
    lines.extend(['', '## Required decisions'])
    lines.extend(bullet_list(contract.get('required_decisions', [])))
    lines.extend(['', '## Hard-fail signals'])
    lines.append('- These are output patterns that mean the task is not done yet or is unsafe to accept.')
    lines.extend(bullet_list(contract.get('hard_fail_patterns', [])))
    lines.extend(['', '## Soft-fail signals'])
    lines.append('- These are weak-output signs that usually require revision, specificity, or escalation.')
    lines.extend(bullet_list(contract.get('soft_fail_patterns', [])))
    lines.extend(['', '## Execution boundaries'])
    lines.append(f"- Lightweight supported: {'yes' if contract.get('supports_lightweight_response') else 'no'}")
    lines.append(f"- Default weight: `{contract.get('task_weight_default', 'standard')}`")
    lines.append(f"- Allowed modes: {', '.join(contract.get('allowed_modes', [])) or 'any'}")
    lines.append(f"- Allowed phases: {', '.join(contract.get('allowed_phases', [])) or 'any'}")
    lines.extend(['', '## Canonical source'])
    lines.append(f"- `{contract.get('canonical_contract')}`")
    return '\n'.join(lines).strip() + '\n'


def estimate_lite_words(route: dict) -> int:
    total = words(read(DIST / 'DEPLOY_LITE.md')) + words(read(DIST / 'SESSION_ZERO.md'))
    total += words(read(DIST / 'lite_routes' / f"{route['route_id']}.md"))
    total += words(read(DIST / 'lite_contracts' / f"{route['task_id']}.md"))
    for skill in route.get('governing_skills', []):
        total += words(read(ROOT / 'src' / 'runtime' / 'cards' / 'skills' / skill))
    return total


def build_starter_doc(route: dict, contract: dict, profiles: dict) -> str:
    recommended_profile = recommend_profile(route, profiles)
    starter_words = estimate_lite_words(route)
    prompt = f"I am starting a lightweight DesignPilot session for {contract.get('title', slug_title(route['task_id']))}. Use the loaded lite bootstrap, this route, and this contract. Ask only for the missing context that would materially change routing or output quality."
    lines = [
        f"# STARTER_{route['task_id'].upper()}",
        '',
        f"Use this starter for **{contract.get('title', slug_title(route['task_id']))}**.",
        '',
        '## Load order',
        '- `dist/DEPLOY_LITE.md`',
        f"- `dist/lite_routes/{route['route_id']}.md`",
        f"- `dist/lite_contracts/{route['task_id']}.md`",
        *[f"- `src/runtime/cards/skills/{skill}`" for skill in route.get('governing_skills', [])],
        *[f"- optional: `src/runtime/cards/skills/{skill}`" for skill in route.get('supporting_skills', [])[:2]],
        '- `dist/SESSION_ZERO.md`',
        '',
        '## Best for',
        f"- {route.get('trigger_summary', 'A bounded single-route task.')}",
        '',
        '## Estimated footprint',
        f"- Approximate startup size with governing skills: ~{starter_words} words / ~{max(1, round(starter_words * 1.33))} tokens",
        '',
        '## Escalate instead to',
        f"- `dist/DEPLOY_{recommended_profile.upper()}.md` when the task widens inside one domain",
        '- `dist/DESIGNPILOT_DEPLOY.md` when multiple domains or proof-sensitive conflicts are central',
        '',
        '## Suggested kickoff prompt',
        prompt,
    ]
    return '\n'.join(lines).strip() + '\n'


def build_lite_index(routes: list[dict], contracts: list[dict], profiles: dict) -> dict:
    contract_map = {c['task_id']: c for c in contracts}
    data = {
        'version': '1.0',
        'artifact': 'dist/DEPLOY_LITE.md',
        'routes': {},
        'lightweight_eligible_routes': [],
        'escalation_only_routes': []
    }
    for route in routes:
        task_id = route['task_id']
        contract = contract_for_route(route, contract_map)
        lightweight_ok = bool(route.get('lightweight_eligible', False) and task_id in contract_map)
        record = {
            'task_id': task_id,
            'title': contract.get('title', slug_title(task_id)),
            'route_doc': f'dist/lite_routes/{route["route_id"]}.md',
            'contract_doc': f'dist/lite_contracts/{task_id}.md' if task_id in contract_map else '',
            'starter_doc': f'dist/lite_starters/{task_id}.md' if lightweight_ok else '',
            'recommended_profile': f'dist/DEPLOY_{recommend_profile(route, profiles).upper()}.md',
            'lightweight_eligible': lightweight_ok,
            'visual_input_supported': bool(route.get('visual_input_supported', False)),
            'governing_skills': route.get('governing_skills', []),
        }
        data['routes'][route['route_id']] = record
        if record['lightweight_eligible']:
            data['lightweight_eligible_routes'].append(route['route_id'])
        else:
            data['escalation_only_routes'].append(route['route_id'])
    return data


def build_startup_modes_doc(routes, contracts):
    eligible = sum(1 for route in routes if route.get('lightweight_eligible', False) and route.get('task_id') in {c['task_id'] for c in contracts})
    total = len(routes)
    return f'''# Startup Modes

DesignPilot now supports three official startup modes.

## 1. Full mode
Use for compound or cross-domain work.

Load:
- `dist/DESIGNPILOT_DEPLOY.md`
- one profile file from `dist/`
- `dist/SESSION_ZERO.md`

Use this when:
- multiple domains compete
- proof sensitivity is high
- the task changes release readiness, remediation posture, or architecture direction

## 2. Profile-only mode
Use for focused single-domain work.

Load:
- one of `dist/DEPLOY_CORE.md`, `dist/DEPLOY_UI.md`, or `dist/DEPLOY_BRAND.md`
- `dist/SESSION_ZERO.md`

Use this when:
- the task is clearly inside one domain
- you want stronger domain coverage than lite mode
- you do not need the full kernel body or true cross-domain arbitration

## 3. Lightweight mode
Use for bounded route-specific work.

Load:
- `dist/DEPLOY_LITE.md`
- one route card from `dist/lite_routes/`
- one contract card from `dist/lite_contracts/`
- only the needed skill cards from `src/runtime/cards/skills/`
- `dist/SESSION_ZERO.md`

Use this when:
- the task has one clear governing route
- the output is bounded and low-to-medium risk
- the task does not need deep cross-domain coordination

## Current route coverage
- lightweight-eligible routes: {eligible}
- total routes: {total}
- routes that should escalate immediately: {total - eligible}
'''


def build_lightweight_quickstart(routes, contracts):
    contract_map = {c['task_id']: c for c in contracts}
    example_route = next((r for r in routes if r.get('route_id') == 'rt_ui_structure_critique'), routes[0])
    example_contract = contract_for_route(example_route, contract_map)
    governing = '\n'.join(f'- `src/runtime/cards/skills/{skill}`' for skill in example_route.get('governing_skills', []))
    optional = '\n'.join(f'- `src/runtime/cards/skills/{skill}`' for skill in example_route.get('supporting_skills', [])[:2]) or '- none'
    return f'''# Lightweight Quickstart

Use this path when the task is narrow enough that one route can govern it honestly.
Start broad, then narrow.

## 1. Confirm the task is a lightweight fit
Use lightweight mode when:
- one route clearly governs the task
- the output shape is bounded
- the job is not architecture-heavy, remediation-heavy, or release-sensitive

If that is not true, use a profile or the full kernel instead.

## 2. Pick the route from the task type
Start with `docs/operator/ROUTE_PICKER.md`.
Choose the route that best matches the governing job.

Example route:
- `dist/lite_routes/{example_route['route_id']}.md`

## 3. Load the lite bootstrap and matching contract
Load:
- `dist/DEPLOY_LITE.md`
- `dist/lite_routes/{example_route['route_id']}.md`
- `dist/lite_contracts/{example_contract['task_id']}.md`

## 4. Add only the skill cards that materially matter
Governing cards for `{example_route['route_id']}`:
{governing}

Optional supporting cards:
{optional}

## 5. Start with session zero
Send the prompt in `dist/SESSION_ZERO.md`.

## 6. Escalate early instead of patching around missing logic
Switch to a profile or the kernel when:
- more than one route could govern the task
- architecture or proof sensitivity becomes central
- the route or contract explicitly says lightweight is unsafe
- the answer would otherwise depend on hidden assumptions

## Shortcut
Use a prebuilt starter from `dist/lite_starters/` if one matches your task.
'''


def build_route_picker(routes, contracts, profiles):
    contract_map = {c['task_id']: c for c in contracts}
    lite_routes = [r for r in routes if r.get('lightweight_eligible', False) and r['task_id'] in contract_map]
    heavy_routes = [r for r in routes if not (r.get('lightweight_eligible', False) and r['task_id'] in contract_map)]
    cluster_map = [
        ('UI and system structure', ['ui', 'layout', 'dashboard', 'component', 'type', 'color', 'accessibility']),
        ('Brand and communication', ['brand', 'case study', 'text humanization']),
        ('Research and planning', ['research gap']),
    ]
    def classify(route, contract):
        hay = f"{contract.get('title', '')} {route.get('trigger_summary', '')}".lower()
        for label, keys in cluster_map:
            if any(k in hay for k in keys):
                return label
        return 'Other specialized routes'
    grouped = {}
    for route in lite_routes:
        contract = contract_for_route(route, contract_map)
        grouped.setdefault(classify(route, contract), []).append((route, contract))
    lines = ['# Route Picker', '', 'Use this file to choose the right startup path without reading internal architecture.', '', 'Start broad, then narrow:', '- first choose the task cluster that matches the job', '- then choose the route inside that cluster', '- then load the matching contract and only the needed skill cards', '']
    for cluster in ['UI and system structure', 'Brand and communication', 'Research and planning', 'Other specialized routes']:
        items = grouped.get(cluster, [])
        if not items:
            continue
        lines.extend([f'## {cluster}', ''])
        for route, contract in items:
            use_when = route.get('trigger_summary') or f"Use when {contract.get('title', slug_title(route['task_id'])).lower()} is the governing job."
            lines.append(f"### {contract.get('title', slug_title(route['task_id']))}")
            lines.append(f"- Route card: `dist/lite_routes/{route['route_id']}.md`")
            lines.append(f"- Contract card: `dist/lite_contracts/{route['task_id']}.md`")
            lines.append(f"- Starter pack: `dist/lite_starters/{route['task_id']}.md`")
            lines.append(f"- Use when: {use_when}")
            lines.append('')
    lines.extend(['## Routes that should usually escalate', ''])
    for route in heavy_routes:
        contract = contract_for_route(route, contract_map)
        profile = recommend_profile(route, profiles)
        use_when = route.get('trigger_summary') or f"Use when {contract.get('title', slug_title(route['task_id'])).lower()} is the governing job."
        if route.get('role') == 'prepass':
            use_when = 'Use when you need visual evidence extraction before deciding the real governing route.'
        lines.append(f"### {contract.get('title', slug_title(route['task_id']))}")
        lines.append(f"- Recommended startup: `dist/DEPLOY_{profile.upper()}.md` or full kernel")
        lines.append(f"- Route card: `dist/lite_routes/{route['route_id']}.md`")
        lines.append(f"- Use when: {use_when}")
        lines.append('')
    return '\n'.join(lines).strip() + '\n'


def build_operator_quickstart():
    return '''# Operator Quickstart

Start with `docs/operator/STARTUP_MODES.md`.
Choose the narrowest honest startup mode for the task.

## Startup selector
- **Full mode**: `dist/DESIGNPILOT_DEPLOY.md` + one profile + `dist/SESSION_ZERO.md`
- **Profile-only mode**: one profile + `dist/SESSION_ZERO.md`
- **Lightweight mode**: `dist/DEPLOY_LITE.md` + one route card + one contract card + only the needed skill cards + `dist/SESSION_ZERO.md`

## Read next
- `docs/operator/STARTUP_MODES.md`
- `docs/operator/LIGHTWEIGHT_QUICKSTART.md`
- `docs/operator/PROFILE_GUIDE.md`
- `docs/operator/ROUTE_PICKER.md`

## Guardrail
Do not default to the full kernel unless the task is truly compound, cross-domain, remediation-heavy, or proof-sensitive.
'''


def build_profile_guide(profiles):
    lines = ['# Profile Guide', '', 'Use profile-only mode when the task is clearly inside one domain and the kernel would be unnecessary.', '', 'Use the full kernel for true cross-domain coordination, route conflict resolution, release-sensitive work, or proof-heavy decisions.', '']
    for name, profile in profiles.items():
        lines.append(f"## {name.upper()}")
        lines.append(profile.get('description', '').strip())
        lines.append('')
        lines.append('Best for:')
        for skill in profile.get('skill_files', [])[:5]:
            _, purpose = skill_purpose(ROOT / 'src' / 'skills' / skill)
            lines.append(f"- `{skill}` — {purpose}")
        lines.append('')
    lines.append('Escalate to the full kernel when more than one domain is central or proof sensitivity rises.')
    return '\n'.join(lines).strip() + '\n'


def build_example_file(task_id: str, title: str) -> str:
    return f'''# Lightweight Example — {title}

Use starter pack:
- `dist/lite_starters/{task_id}.md`

Then start with:
> I am starting a lightweight DesignPilot session for {title}. Ask only for the minimum missing context and keep the route narrow unless the task clearly needs escalation.
'''


def main():
    config = yaml.safe_load(read(CONFIG))
    profiles = yaml.safe_load(read(PROFILE_CONFIG))
    routes = load_runtime_routes()
    contracts = load_runtime_contracts()
    contract_map = {c['task_id']: c for c in contracts}

    outputs = {
        'DESIGNPILOT_DEPLOY.md': build_kernel(config, profiles),
        'DEPLOY_CORE.md': build_profile('core', profiles['core']),
        'DEPLOY_UI.md': build_profile('ui', profiles['ui']),
        'DEPLOY_BRAND.md': build_profile('brand', profiles['brand']),
        'DEPLOY_LITE.md': build_lite(config),
        'SESSION_ZERO.md': build_session_zero(profiles),
    }

    manifest = {'artifacts': {}, 'generated_from': ['config/deploy_manifest.yaml', 'config/profile_map.yaml'], 'status': 'ok'}
    tier_profile = {}
    validation_report = {'status': 'ok', 'checks': []}

    for name, text in outputs.items():
        path = DIST / name
        write(path, text)
        manifest['artifacts'][name] = {'word_count': words(text), 'path': f'dist/{name}', 'token_estimate': token_estimate(text)}
        tier_profile[name] = {'word_count': words(text)}
        validation_report['checks'].append({'artifact': name, 'word_count': words(text), 'status': 'ok' if words(text) > 40 else 'warn'})

    for route in routes:
        contract = contract_for_route(route, contract_map)
        route_text = build_route_doc(route, contract, profiles)
        route_path = DIST / 'lite_routes' / f"{route['route_id']}.md"
        write(route_path, route_text)
        manifest['artifacts'][f'lite_routes/{route_path.name}'] = {'word_count': words(route_text), 'path': f'dist/lite_routes/{route_path.name}', 'token_estimate': token_estimate(route_text)}

    for contract in contracts:
        contract_text = build_contract_doc(contract)
        contract_path = DIST / 'lite_contracts' / f"{contract['task_id']}.md"
        write(contract_path, contract_text)
        manifest['artifacts'][f'lite_contracts/{contract_path.name}'] = {'word_count': words(contract_text), 'path': f'dist/lite_contracts/{contract_path.name}', 'token_estimate': token_estimate(contract_text)}

    for route in routes:
        if route.get('lightweight_eligible', False) and route['task_id'] in contract_map:
            contract = contract_for_route(route, contract_map)
            starter_text = build_starter_doc(route, contract, profiles)
            starter_path = DIST / 'lite_starters' / f"{route['task_id']}.md"
            write(starter_path, starter_text)
            manifest['artifacts'][f'lite_starters/{starter_path.name}'] = {'word_count': words(starter_text), 'path': f'dist/lite_starters/{starter_path.name}', 'token_estimate': token_estimate(starter_text)}

    lite_index = build_lite_index(routes, contracts, profiles)
    write(DIST / 'lite_index.json', json.dumps(lite_index, indent=2))
    manifest['artifacts']['lite_index.json'] = {'word_count': 0, 'path': 'dist/lite_index.json'}

    docs = {
        ROOT / 'docs' / 'operator' / 'STARTUP_MODES.md': build_startup_modes_doc(routes, contracts),
        ROOT / 'docs' / 'operator' / 'LIGHTWEIGHT_QUICKSTART.md': build_lightweight_quickstart(routes, contracts),
        ROOT / 'docs' / 'operator' / 'ROUTE_PICKER.md': build_route_picker(routes, contracts, profiles),
        ROOT / 'docs' / 'operator' / 'OPERATOR_QUICKSTART.md': build_operator_quickstart(),
        ROOT / 'docs' / 'operator' / 'PROFILE_GUIDE.md': build_profile_guide(profiles),
    }
    for path, text in docs.items():
        write(path, text)

    example_map = {
        'ui_structure_critique': 'UI Structure Critique',
        'component_spec': 'Component Specification',
        'brand_positioning_pass': 'Brand Positioning Pass',
        'case_study_rewrite': 'Case Study Rewrite',
        'type_system_recommendation': 'Type System Recommendation',
    }
    write(EXAMPLES_LIGHT / 'README.md', '# Lightweight Examples\n\nThese examples point to the prebuilt lite starter packs for common DesignPilot tasks.\n')
    for task_id, title in example_map.items():
        write(EXAMPLES_LIGHT / f'{task_id}.md', build_example_file(task_id, title))

    tier_profile['DEPLOY_LITE.md'] = {
        'word_count': words(outputs['DEPLOY_LITE.md']),
        'route_doc_count': len(list((DIST / 'lite_routes').glob('*.md'))),
        'contract_doc_count': len(list((DIST / 'lite_contracts').glob('*.md'))),
        'starter_doc_count': len(list((DIST / 'lite_starters').glob('*.md'))),
    }
    validation_report['checks'].append({
        'artifact': 'DEPLOY_LITE.md',
        'word_count': words(outputs['DEPLOY_LITE.md']),
        'status': 'ok' if words(outputs['DEPLOY_LITE.md']) < 1200 else 'warn',
        'mode': 'lightweight'
    })
    validation_report['checks'].append({
        'artifact': 'lite_overlay_docs',
        'route_docs': len(list((DIST / 'lite_routes').glob('*.md'))),
        'contract_docs': len(list((DIST / 'lite_contracts').glob('*.md'))),
        'starter_docs': len(list((DIST / 'lite_starters').glob('*.md'))),
        'status': 'ok'
    })

    write(DIST / 'manifest.json', json.dumps(manifest, indent=2))
    write(DIST / 'tier_profile.yaml', yaml.safe_dump(tier_profile, sort_keys=False))
    write(DIST / 'validation_report.json', json.dumps(validation_report, indent=2))
    print(json.dumps({'generated_artifact_count': len(manifest['artifacts'])}, indent=2))


if __name__ == '__main__':
    main()
