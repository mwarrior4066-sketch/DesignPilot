#!/usr/bin/env python3
import json
import re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
DIST_RUNTIME = DIST / 'runtime'
DIST_TASK_LAUNCHERS = DIST_RUNTIME / 'task_launchers'
DIST_RUNTIME_SUMMARIES = DIST_RUNTIME / 'summaries'
DOCS_OPERATOR = ROOT / 'docs' / 'operator'
EXAMPLES_LIGHT = ROOT / 'examples' / 'lightweight'
CONFIG = ROOT / 'config' / 'deploy_manifest.yaml'
PROFILE_CONFIG = ROOT / 'config' / 'profile_map.yaml'

for path in [DIST, DIST_RUNTIME, DIST_TASK_LAUNCHERS, DIST_RUNTIME_SUMMARIES, DOCS_OPERATOR, EXAMPLES_LIGHT, DIST / 'runtime' / 'route_cards', DIST / 'runtime' / 'contracts_lite', DIST / 'runtime' / 'starters', DIST / 'runtime' / 'contracts', DIST / 'runtime' / 'routes', DIST / 'runtime' / 'skills', DIST / 'runtime' / 'loading']:
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


def slug_title(value: str) -> str:
    value = value.replace('rt_', '').replace('.md', '').replace('_', ' ').replace('-', ' ').strip()
    return ' '.join(part.capitalize() for part in value.split())


def bullet_list(items):
    def _label(item):
        if isinstance(item, dict):
            return item.get('name') or item.get('id') or str(item)
        return item
    return [f'- {_label(item)}' for item in items] if items else ['- none']


def extract_runtime_summary(skill_path: Path) -> str:
    """Extract the ## Runtime summary section from a canonical skill file,
    or return the full file content if no section exists."""
    content = read(skill_path)
    if '## Runtime summary' in content:
        idx = content.index('## Runtime summary')
        section = content[idx:].strip()
        # Remove auto-generated comment
        import re as _re
        section = _re.sub(r'<!--[^>]*-->\n\n', '', section)
        return section
    return content


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



def runtime_summary_operator_path(summary_ref: str) -> str:
    return f"dist/runtime/summaries/{Path(summary_ref).name}"


def runtime_summary_display(summary_ref: str) -> str:
    return f"`{runtime_summary_operator_path(summary_ref)}`"


def build_runtime_summary_doc(summary_name: str) -> str:
    source_path = ROOT / 'src' / 'knowledge-base' / 'summaries' / summary_name
    text = read(source_path)
    _, body = parse_frontmatter(text)
    sections = parse_sections(body)

    title = None
    for line in body.splitlines():
        if line.startswith('# '):
            title = line[2:].strip()
            break
    if not title:
        title = slug_title(summary_name)

    def section_bullets(name: str, fallback: list[str]) -> list[str]:
        content = sections.get(name, '').strip()
        bullets = []
        if content:
            for line in content.splitlines():
                line = line.strip()
                if re.match(r'^[-*]\s+', line):
                    bullets.append(re.sub(r'^[-*]\s+', '', line).strip())
        return bullets or fallback

    decision_rules = section_bullets('Decision rules', ['No extracted decision rules; escalate to a profile or the full kernel when thresholds or exact source detail matter.'])
    failure_traps = section_bullets('Failure traps', ['No extracted failure traps; escalate if the runtime summary is not specific enough for the task.'])
    escalate_when = section_bullets('Escalate when', [
        'exact thresholds, standards wording, or measurable criteria are required',
        'the governing route conflicts with other evidence or another route',
        'the task becomes proof-sensitive, standards-grade, or release-sensitive',
        'you need deeper canonical evidence beyond the compiled runtime layer',
    ])

    lines = [
        f"# {title}",
        '',
        'This is the operator-safe compiled mirror of a runtime summary.',
        'Use it for quick runtime context. Escalate to a profile or `dist/DESIGNPILOT_DEPLOY.md` when deeper canonical evidence is needed.',
        '',
        '## Decision rules',
        *[f"- {item}" for item in decision_rules],
        '',
        '## Failure traps',
        *[f"- {item}" for item in failure_traps],
        '',
        '## Escalate when',
        *[f"- {item}" for item in escalate_when],
        '',
        '## Deeper fallback',
        '- `dist/DESIGNPILOT_DEPLOY.md` for full compiled authority',
        '- the recommended profile launcher when the task widens inside one domain',
    ]
    return '\n'.join(lines).strip() + '\n'


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
    route_dir = ROOT / 'dist' / 'runtime' / 'routes'
    return sorted([json.loads(p.read_text(encoding='utf-8')) for p in route_dir.glob('*.json')], key=lambda x: x['route_id'])


def load_runtime_contracts() -> list[dict]:
    contract_dir = ROOT / 'dist' / 'runtime' / 'contracts'
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
    # Auto-generate required output headings table from task contracts
    # This block is regenerated every compile — do not edit DESIGNPILOT_DEPLOY.md by hand
    try:
        contracts_data = json.loads((ROOT / 'src' / 'schemas' / 'task_contracts.json').read_text())
        lines.append('')
        lines.append('## Required output headings by task')
        lines.append('When you identify the governing task from the user prompt, use these section headings exactly.')
        lines.append('These headings are required for automated validation. Do not rename, merge, or skip them.')
        lines.append('')
        for task in contracts_data.get('tasks', []):
            tid = task['task_id']
            secs = task.get('required_sections', [])
            heading_names = [s['name'] if isinstance(s, dict) else s for s in secs]
            if heading_names:
                lines.append(f"**{tid}:** " + ' | '.join(heading_names))
    except Exception as e:
        lines.append(f'<!-- heading table generation failed: {e} -->')

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
        '## Preferred operator path',
        '1. `dist/runtime/START_HERE.md` if you are starting fresh',
        '2. one single-file launcher from `dist/runtime/task_launchers/` when the task type is known',
        '3. `dist/SESSION_ZERO.md`',
        '',
        '## Manual fallback load order',
        'Use this only when you are maintaining the pack or debugging a launcher.',
        '1. `dist/DEPLOY_LITE.md`',
        '2. one route card from `dist/runtime/route_cards/`',
        '3. the matching contract card from `dist/runtime/contracts_lite/`',
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
    return '''# SESSION_ZERO

You are starting a DesignPilot session.

Before answering in depth:
1. acknowledge the task naturally in plain language
2. infer the likely governing job internally instead of foregrounding routing language
3. begin useful work immediately unless one missing detail would materially change the answer
4. ask for only the minimum missing context that affects structure, implementation realism, or proof honesty
5. do not front-load internal architecture, startup modes, route IDs, or profile logic unless the user asks
6. sound like a capable helper: direct, calm, useful, and not sycophantic
7. keep internal rigor internal unless surfacing it materially improves trust or clarity
8. use the exact section headings listed in the launcher Output expectations -- do not rename them or invent alternatives
9. each required section must have substantive content -- at least two paragraphs of original analysis, not a heading with a single sentence underneath
10. do not begin your response with Mode, Phase, Route, or Skills lines. Your first output
    token must be substantive content. Operator metadata belongs in the [SESSION_STATE] block
    at the end of your response only. Never in visible output.
11. every recommendation must name one explicit tradeoff -- what is preserved and what is
    sacrificed. Use at least one of: "rather than", "instead of", "at the cost of",
    "this means accepting", "one downside is", "the risk is", "you sacrifice X to gain Y."
    A direction without a named tradeoff will fail validation.
12. every claim of necessity, constraint, or cause must be expressed with explicit causal
    grounding. Use at least one of: "because", "without which", "this requires",
    "the constraint is", "by doing so", "if you skip this", "the reason is",
    "this enables", "this prevents."
    A conclusion without causal grounding will fail rationale validation.

If the task is ambiguous, use one short clarifying question.
If it is not ambiguous, do not turn startup into intake ceremony.
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
        f"- Default contract: `dist/runtime/contracts_lite/{route['task_id']}.md`" if is_contract_backed else '- Default contract: no dedicated task contract; treat this as a pre-pass helper and escalate quickly',
        f"- Recommended profile if you escalate: `dist/DEPLOY_{recommended_profile.upper()}.md`",
        f"- Visual input supported: {'yes' if route.get('visual_input_supported') else 'no'}",
        '',
        '## Governing skills',
    ]
    for skill_file in route.get('governing_skills', []):
        _, purpose = skill_purpose(ROOT / 'src' / 'skills' / skill_file)
        lines.append(f"- `dist/runtime/skills/{skill_file}` - {purpose}")
    lines.extend(['', '## Optional supporting skills'])
    for skill_file in route.get('supporting_skills', []):
        _, purpose = skill_purpose(ROOT / 'src' / 'skills' / skill_file)
        lines.append(f"- `dist/runtime/skills/{skill_file}` - {purpose}")
    lines.extend(['', '## Runtime summaries'])
    lines.extend(bullet_list([runtime_summary_display(summary) for summary in route.get('required_summary_ids', [])]))
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
    total += words(read(DIST / 'runtime' / 'route_cards' / f"{route['route_id']}.md"))
    total += words(read(DIST / 'runtime' / 'contracts_lite' / f"{route['task_id']}.md"))
    for skill in route.get('governing_skills', []):
        total += words(read(ROOT / 'dist' / 'runtime' / 'skills' / skill))
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
        f"- `dist/runtime/route_cards/{route['route_id']}.md`",
        f"- `dist/runtime/contracts_lite/{route['task_id']}.md`",
        *[f"- `dist/runtime/skills/{skill}`" for skill in route.get('governing_skills', [])],
        *[f"- optional: `dist/runtime/skills/{skill}`" for skill in route.get('supporting_skills', [])[:2]],
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
            'route_doc': f'dist/runtime/route_cards/{route["route_id"]}.md',
            'contract_doc': f'dist/runtime/contracts_lite/{task_id}.md' if task_id in contract_map else '',
            'starter_doc': f'dist/runtime/starters/{task_id}.md' if lightweight_ok else '',
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

Normal operator path:
- `dist/runtime/START_HERE.md`
- one launcher from `dist/runtime/task_launchers/`
- `dist/SESSION_ZERO.md`

Advanced manual path only:
- `dist/DEPLOY_LITE.md`
- one route card from `dist/runtime/route_cards/`
- one contract card from `dist/runtime/contracts_lite/`
- only the needed runtime skill cards
- `dist/SESSION_ZERO.md`

Use lightweight mode when:
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
    return f'''# Lightweight Quickstart

Use this path when the task is narrow enough that one route can govern it honestly.
Start broad, then narrow.

## 1. Prefer the launcher-first path
Normal operators should start with a single-file launcher rather than assembling route, contract, and skill cards by hand.

Load:
- `dist/runtime/START_HERE.md`
- `dist/runtime/task_launchers/{example_contract['task_id']}.md` or another matching launcher
- `dist/SESSION_ZERO.md`

## 2. Confirm the task is a lightweight fit
Use lightweight mode when:
- one route clearly governs the task
- the output shape is bounded
- the job is not architecture-heavy, remediation-heavy, or release-sensitive

If that is not true, use a profile or the full kernel instead.

## 3. Pick the launcher from the task type
Start with `dist/runtime/TASK_CHOOSER.md`.
Choose the launcher that best matches the governing job.

Example launcher:
- `dist/runtime/task_launchers/{example_contract['task_id']}.md`

## 4. Use manual runtime assembly only as a fallback
If you are debugging, maintaining, or checking launcher internals, the manual path is:
- `dist/DEPLOY_LITE.md`
- `dist/runtime/route_cards/{example_route['route_id']}.md`
- `dist/runtime/contracts_lite/{example_contract['task_id']}.md`
- the needed runtime skill cards
- `dist/SESSION_ZERO.md`

## 5. Start with session zero
Send the prompt in `dist/SESSION_ZERO.md`.

## 6. Escalate early instead of patching around missing logic
Switch to a profile or the kernel when:
- more than one route could govern the task
- architecture or proof sensitivity becomes central
- the route or contract explicitly says lightweight is unsafe
- the answer would otherwise depend on hidden assumptions
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
    lines = ['# Route Picker', '', 'Use this file to choose the right launcher without reading internal architecture.', '', 'Start broad, then narrow:', '- first choose the task cluster that matches the job', '- then choose the launcher inside that cluster', '- then load the launcher plus `dist/SESSION_ZERO.md`', '', 'Manual route + contract + skill assembly is a maintainer/debug path only.', '']
    for cluster in ['UI and system structure', 'Brand and communication', 'Research and planning', 'Other specialized routes']:
        items = grouped.get(cluster, [])
        if not items:
            continue
        lines.extend([f'## {cluster}', ''])
        for route, contract in items:
            use_when = route.get('trigger_summary') or f"Use when {contract.get('title', slug_title(route['task_id'])).lower()} is the governing job."
            lines.append(f"### {contract.get('title', slug_title(route['task_id']))}")
            lines.append(f"- Single-file launcher: `dist/runtime/task_launchers/{route['task_id']}.md`")
            lines.append(f"- Manual route card: `dist/runtime/route_cards/{route['route_id']}.md`")
            lines.append(f"- Manual contract card: `dist/runtime/contracts_lite/{route['task_id']}.md`")
            lines.append(f"- Best fit: {use_when}")
            lines.append('')
    lines.extend(['## Routes that should usually escalate', ''])
    for route in heavy_routes:
        contract = contract_for_route(route, contract_map)
        profile = recommend_profile(route, profiles)
        use_when = route.get('trigger_summary') or f"Use when {contract.get('title', slug_title(route['task_id'])).lower()} is the governing job."
        if route.get('role') == 'prepass':
            use_when = 'Use when you need visual evidence extraction before deciding the real governing route.'
        lines.append(f"### {contract.get('title', slug_title(route['task_id']))}")
        lines.append(f"- Launcher: `dist/runtime/task_launchers/{route['task_id']}.md`")
        lines.append(f"- Recommended startup: `dist/DEPLOY_{profile.upper()}.md` or full kernel")
        lines.append(f"- Best fit: {use_when}")
        lines.append('')
    return '\n'.join(lines).strip() + '\n'


def build_operator_quickstart():
    return '''# Operator Quickstart

Start with `dist/runtime/START_HERE.md`.
Choose the narrowest honest startup mode for the task.

## Startup selector
- **Fastest normal path**: `dist/runtime/START_HERE.md` -> one launcher in `dist/runtime/task_launchers/` -> `dist/SESSION_ZERO.md`
- **Full mode**: `dist/DESIGNPILOT_DEPLOY.md` + one profile + `dist/SESSION_ZERO.md`
- **Profile-only mode**: one profile + `dist/SESSION_ZERO.md`
- **Manual lightweight mode**: `dist/DEPLOY_LITE.md` + one route card + one contract card + only the needed runtime skill cards + `dist/SESSION_ZERO.md`

## Read next
- `dist/runtime/START_HERE.md`
- `dist/runtime/TASK_CHOOSER.md`
- `docs/operator/DEPLOYMENT_GUIDE.md`
- `docs/operator/PROFILE_GUIDE.md`
- `docs/operator/ROUTE_PICKER.md`

## Startup authority
- Operator entrypoint: `dist/runtime/START_HERE.md`
- Compiled full-kernel authority: `dist/DESIGNPILOT_DEPLOY.md`
- Source startup authority for maintainers: `src/operator/core/MASTER_CHAT_OPERATOR.md`

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
            lines.append(f"- `{skill}` - {purpose}")
        lines.append('')
    lines.append('Escalate to the full kernel when more than one domain is central or proof sensitivity rises.')
    return '\n'.join(lines).strip() + '\n'




def build_start_here() -> str:
    return '''# START_HERE

This is the simplest runtime front door for normal use.

## Fastest normal path
1. Open `dist/runtime/TASK_CHOOSER.md` if the task type is not obvious.
2. Load one launcher from `dist/runtime/task_launchers/`.
3. Start with `dist/SESSION_ZERO.md`.

## What this is for
Use this path when you want DesignPilot to help with a real task without manually assembling the system.

## Escalate only when needed
- Use a profile file from `dist/` when the job is clearly inside one domain but grows beyond a lightweight pass.
- Use `dist/DESIGNPILOT_DEPLOY.md` when multiple domains compete or proof-sensitive conflicts matter.
- Use manual lightweight assembly only for debugging, maintenance, or runtime inspection.

## Guardrails
- Do not manually assemble route + contract + skills for normal use.
- Prefer the smallest correct startup path.
- If the task widens, escalate instead of patching around ambiguity.
- DesignPilot improves structure and decision quality, but it does not replace research, engineering review, accessibility testing, or real-world validation.
'''

def build_task_chooser(routes, contracts, profiles) -> str:
    contract_map = {c['task_id']: c for c in contracts}
    lite_routes = [r for r in routes if r['task_id'] in contract_map]
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
    lines = [
        '# TASK_CHOOSER',
        '',
        'Use this file to pick the launcher that best matches the main job you need done.',
        '',
        'Start with the user-level question, not the internal route:',
        '- what are you trying to do',
        '- what is the main failure, decision, or deliverable',
        '- which launcher best fits that job',
        '',
        'Use launcher-first startup whenever possible.',
    ]
    for cluster in ['UI and system structure', 'Brand and communication', 'Research and planning', 'Other specialized routes']:
        items = grouped.get(cluster, [])
        if not items:
            continue
        lines.extend(['', f'## {cluster}', ''])
        for route, contract in items:
            profile = recommend_profile(route, profiles)
            use_when = route.get('trigger_summary') or f"Use when {contract.get('title', slug_title(route['task_id'])).lower()} is the governing job."
            lines.append(f"### {contract.get('title', slug_title(route['task_id']))}")
            lines.append(f"- Launcher: `dist/runtime/task_launchers/{route['task_id']}.md`")
            lines.append(f"- Default mode: {'lightweight' if route.get('lightweight_eligible', False) else 'profile-only or full'}")
            lines.append(f"- Recommended profile on escalation: `dist/DEPLOY_{profile.upper()}.md`")
            lines.append(f"- Best fit: {use_when}")
            lines.append('')
    return '\n'.join(lines).strip() + '\n'


def build_task_launcher(route: dict, contract: dict, profiles: dict) -> str:
    recommended_profile = recommend_profile(route, profiles)
    route_title = contract.get('title', slug_title(route['task_id']))
    lightweight_ok = bool(route.get('lightweight_eligible', False) and contract.get('required_sections'))
    mode = 'lightweight' if lightweight_ok else 'profile-only or full'
    skills = []
    for skill_file in route.get('governing_skills', []):
        _, purpose = skill_purpose(ROOT / 'src' / 'skills' / skill_file)
        skills.append(f"- Governing: `{skill_file}` - {purpose}")
    for skill_file in route.get('supporting_skills', [])[:3]:
        _, purpose = skill_purpose(ROOT / 'src' / 'skills' / skill_file)
        skills.append(f"- Optional support: `{skill_file}` - {purpose}")
    required_secs = contract.get('required_sections', [])
    output_expectations = []
    if required_secs:
        # Explicit format block: model must use these exact headings for automated validation
        output_expectations.append('Use these section headings exactly -- matching them enables automated validation:')
        for section in required_secs:
            name = section if isinstance(section, str) else section.get('name', str(section))
            rationale = section.get('rationale', '') if isinstance(section, dict) else ''
            if rationale:
                output_expectations.append(f'  ## {name}  ({rationale})')
            else:
                output_expectations.append(f'  ## {name}')
        output_expectations.append('')
    output_expectations.extend([f"- Required section: {section if isinstance(section,str) else section.get('name',section)}" for section in required_secs] or ['- Required sections are not explicitly codified; escalate if the deliverable shape becomes ambiguous.'])
    output_expectations.extend([f"- Required evidence: {item}" for item in contract.get('required_evidence_types', [])])
    output_expectations.extend([f"- Required decision: {item}" for item in contract.get('required_decisions', [])])
    output_expectations.extend([f"- Hard fail signal: {item}" for item in contract.get('hard_fail_patterns', [])])
    output_expectations.extend([f"- Soft fail signal: {item}" for item in contract.get('soft_fail_patterns', [])])
    lines = [
        f"# LAUNCH_{route['task_id'].upper()}",
        '',
        f"Use this as the single-file launcher for **{route_title}**.",
        '',
        '## Startup path',
        f"- Default mode: {mode}",
        '- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.',
        '- Manual runtime assembly is not needed for normal use.',
        f"- Escalate to `dist/DEPLOY_{recommended_profile.upper()}.md` if the task stays in one domain but grows beyond a lightweight pass.",
        '- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.',
        '',
        '## Route logic',
        f"- Governing route: `{route['route_id']}`",
        f"- Use when: {route.get('trigger_summary', 'This is the governing task type.')}",
        f"- Visual input supported: {'yes' if route.get('visual_input_supported') else 'no'}",
        *[f"- Known tension: {item}" for item in route.get('known_tensions', [])],
        *[f"- Escalate when: {item}" for item in route.get('escalation_conditions', [])],
        f"- Fallback route: `{route.get('fallback_route')}`" if route.get('fallback_route') else '- Fallback route: none',
        '',
        '## Included skill logic',
        *skills,
        '',
        '## Runtime summaries',
        *([f"- {runtime_summary_display(summary)}" for summary in route.get('required_summary_ids', [])] or ['- none']),
        '',
        '## Output expectations',
        *output_expectations,
        '',
        '## Kickoff behavior',
        '- After loading this launcher, start with `dist/SESSION_ZERO.md`.',
        '- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.',
        '- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.',
        '- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.',
        '- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.',
        f"- Suggested kickoff prompt: I am starting a DesignPilot session for {route_title}. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.",
    ]
    return '\n'.join(lines).strip() + '\n'


def build_runtime_index(routes: list[dict], contracts: list[dict], profiles: dict) -> dict:
    contract_map = {c['task_id']: c for c in contracts}
    launchers = {}
    for route in routes:
        contract = contract_for_route(route, contract_map)
        launchers[route['task_id']] = {
            'title': contract.get('title', slug_title(route['task_id'])),
            'launcher': f'dist/runtime/task_launchers/{route["task_id"]}.md',
            'route_doc': f'dist/runtime/route_cards/{route["route_id"]}.md',
            'contract_doc': f'dist/runtime/contracts_lite/{route["task_id"]}.md' if route['task_id'] in contract_map else '',
            'recommended_profile': f'dist/DEPLOY_{recommend_profile(route, profiles).upper()}.md',
            'lightweight_eligible': bool(route.get('lightweight_eligible', False) and contract.get('required_sections')),
            'governing_skills': route.get('governing_skills', []),
        }
    return {'version': '1.0', 'launchers': launchers}

def build_example_file(task_id: str, title: str) -> str:
    return f'''# Lightweight Example - {title}

Use starter pack:
- `dist/runtime/starters/{task_id}.md`

Then start with:
> I am starting a lightweight DesignPilot session for {title}. Ask only for the minimum missing context and keep the route narrow unless the task clearly needs escalation.
'''



def _build_readme_health_badge(root: Path) -> str:
    """Generate a pack health section from the latest batch run."""
    import glob, os
    batch_dir = root / 'tests' / 'live_outputs' / 'batch'
    if not batch_dir.exists():
        return ''
    valid_runs = []
    for run_dir in sorted(batch_dir.iterdir(), reverse=True):
        if not run_dir.is_dir(): continue
        ctx_file = run_dir / 'run_context.json'
        cr_file = run_dir / 'comparative_report.json'
        if not cr_file.exists(): continue
        ctx = json.loads(ctx_file.read_text()) if ctx_file.exists() else {}
        if ctx.get('is_valid_quality_signal', True):
            valid_runs.append((run_dir.name, cr_file))
            break
    if not valid_runs:
        return ''
    run_id, cr_file = valid_runs[0]
    report = json.loads(cr_file.read_text())
    rows = []
    for r in report.get('ranking', []):
        comp = r.get('avg_composite')
        comp_str = f"{comp:.0f}" if comp else '—'
        gate = '✓' if r.get('gate_passed') else '✗'
        rows.append(f"| {r['provider']:12} | {comp_str:9} | {r.get('pass_rate', 0):.0%}       | {gate}    |")
    table = '\n'.join(rows)
    return f"""
## Pack health

Latest validated run: `{run_id}`

| Provider     | Composite | Pass rate | Gate |
|-------------|-----------|-----------|------|
{table}

*Composite = 60% validator + 40% rubric judge, 0–100. Gate = ≥ 70% pass rate.*  
Full history: `tests/reports/v2-tests/MASTER_SUMMARY.html`
"""



def _build_task_index(root: Path) -> None:
    """Compile route + contract data into a single TASK_INDEX.json/md."""
    tasks_raw = json.loads((root / 'src/schemas/task_contracts.json').read_text())['tasks']
    routes_raw = json.loads((root / 'src/schemas/routing_registry.json').read_text())
    route_by_task = {r.get('task_id', ''): r for r in routes_raw.get('routes', [])}
    idx = {'version': '1.0', 'generated_from': ['src/schemas/task_contracts.json', 'src/schemas/routing_registry.json'], 'tasks': {}}
    for task in tasks_raw:
        tid = task['task_id']
        route = route_by_task.get(tid, {})
        idx['tasks'][tid] = {
            'title': task['title'], 'task_group': task.get('task_group', ''),
            'lightweight_eligible': route.get('lightweight_eligible', False),
            'governing_skills': route.get('governing_skills', []),
            'supporting_skills': route.get('supporting_skills', []),
            'runtime_summaries': route.get('runtime_summaries', []),
            'required_sections': [s['name'] for s in task.get('required_sections', [])],
            'required_decisions': [d['id'] for d in task.get('required_decisions', [])],
            'require_tradeoff': task.get('require_tradeoff', False),
            'require_rationale': task.get('require_rationale', False),
            'launcher': f'dist/runtime/task_launchers/{tid}.md',
            'route_id': route.get('route_id', f'rt_{tid}'),
        }
    (root / 'dist/runtime/TASK_INDEX.json').write_text(json.dumps(idx, indent=2))
    lines = ['# Task Index\n\n']
    for tid, t in idx['tasks'].items():
        lines.append(f"## {t['title']}\n**ID:** `{tid}` | **Group:** {t['task_group']} | **Lightweight:** {'yes' if t['lightweight_eligible'] else 'no'}\n\n")
        if t['required_sections']:
            lines.append(f"**Sections:** {', '.join(t['required_sections'])}\n\n")
        lines.append('---\n\n')
    (root / 'dist/runtime/TASK_INDEX.md').write_text(''.join(lines))


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
        route_path = DIST / 'runtime' / 'route_cards' / f"{route['route_id']}.md"
        write(route_path, route_text)
        manifest['artifacts'][f'dist/runtime/route_cards/{route_path.name}'] = {'word_count': words(route_text), 'path': f'dist/runtime/route_cards/{route_path.name}', 'token_estimate': token_estimate(route_text)}

    for contract in contracts:
        contract_text = build_contract_doc(contract)
        contract_path = DIST / 'runtime' / 'contracts_lite' / f"{contract['task_id']}.md"
        write(contract_path, contract_text)
        manifest['artifacts'][f'dist/runtime/contracts_lite/{contract_path.name}'] = {'word_count': words(contract_text), 'path': f'dist/runtime/contracts_lite/{contract_path.name}', 'token_estimate': token_estimate(contract_text)}

    for route in routes:
        if route.get('lightweight_eligible', False) and route['task_id'] in contract_map:
            contract = contract_for_route(route, contract_map)
            starter_text = build_starter_doc(route, contract, profiles)
            starter_path = DIST / 'runtime' / 'starters' / f"{route['task_id']}.md"
            write(starter_path, starter_text)
            manifest['artifacts'][f'dist/runtime/starters/{starter_path.name}'] = {'word_count': words(starter_text), 'path': f'dist/runtime/starters/{starter_path.name}', 'token_estimate': token_estimate(starter_text)}

    lite_index = build_lite_index(routes, contracts, profiles)
    write(DIST / 'runtime' / 'lite_index.json', json.dumps(lite_index, indent=2))
    manifest['artifacts']['dist/runtime/lite_index.json'] = {'word_count': 0, 'path': 'dist/runtime/lite_index.json'}

    runtime_docs = {
        DIST_RUNTIME / 'START_HERE.md': build_start_here(),
        DIST_RUNTIME / 'TASK_CHOOSER.md': build_task_chooser(routes, contracts, profiles),
    }

    runtime_summary_index = {'version': '1.0', 'summaries': {}}
    summary_names = sorted({Path(summary).name for route in routes for summary in route.get('required_summary_ids', [])})
    for summary_name in summary_names:
        summary_text = build_runtime_summary_doc(summary_name)
        summary_path = DIST_RUNTIME_SUMMARIES / summary_name
        write(summary_path, summary_text)
        rel = summary_path.relative_to(DIST).as_posix()
        manifest['artifacts'][rel] = {'word_count': words(summary_text), 'path': f'dist/{rel}', 'token_estimate': token_estimate(summary_text)}
        runtime_summary_index['summaries'][summary_name] = {
            'compiled_path': f'dist/runtime/summaries/{summary_name}',
            'source_runtime_summary': f'src/knowledge-base/summaries/{summary_name}',
        }

    write(DIST_RUNTIME / 'summaries_index.json', json.dumps(runtime_summary_index, indent=2))
    manifest['artifacts']['runtime/summaries_index.json'] = {'word_count': 0, 'path': 'dist/runtime/summaries_index.json'}
    for path, text in runtime_docs.items():
        write(path, text)
        rel = path.relative_to(DIST).as_posix()
        manifest['artifacts'][rel] = {'word_count': words(text), 'path': f'dist/{rel}', 'token_estimate': token_estimate(text)}

    runtime_index = build_runtime_index(routes, contracts, profiles)
    write(DIST_RUNTIME / 'launchers_index.json', json.dumps(runtime_index, indent=2))
    manifest['artifacts']['runtime/launchers_index.json'] = {'word_count': 0, 'path': 'dist/runtime/launchers_index.json'}

    for route in routes:
        contract = contract_for_route(route, contract_map)
        launcher_text = build_task_launcher(route, contract, profiles)
        launcher_path = DIST_TASK_LAUNCHERS / f"{route['task_id']}.md"
        write(launcher_path, launcher_text)
        manifest['artifacts'][f'runtime/task_launchers/{launcher_path.name}'] = {'word_count': words(launcher_text), 'path': f'dist/runtime/task_launchers/{launcher_path.name}', 'token_estimate': token_estimate(launcher_text)}

    docs = {
        ROOT / 'docs' / 'operator' / 'DEPLOYMENT_GUIDE.md': build_startup_modes_doc(routes, contracts),
        ROOT / 'docs' / 'operator' / 'DEPLOYMENT_GUIDE.md': build_lightweight_quickstart(routes, contracts),
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
        'route_doc_count': len(list((DIST / 'runtime' / 'route_cards').glob('*.md'))),
        'contract_doc_count': len(list((DIST / 'runtime' / 'contracts_lite').glob('*.md'))),
        'starter_doc_count': len(list((DIST / 'runtime' / 'starters').glob('*.md'))),
    }
    validation_report['checks'].append({
        'artifact': 'DEPLOY_LITE.md',
        'word_count': words(outputs['DEPLOY_LITE.md']),
        'status': 'ok' if words(outputs['DEPLOY_LITE.md']) < 1200 else 'warn',
        'mode': 'lightweight'
    })
    validation_report['checks'].append({
        'artifact': 'lite_overlay_docs',
        'route_docs': len(list((DIST / 'runtime' / 'route_cards').glob('*.md'))),
        'contract_docs': len(list((DIST / 'runtime' / 'contracts_lite').glob('*.md'))),
        'starter_docs': len(list((DIST / 'runtime' / 'starters').glob('*.md'))),
        'status': 'ok'
    })
    validation_report['checks'].append({
        'artifact': 'runtime_launchers',
        'launcher_docs': len(list(DIST_TASK_LAUNCHERS.glob('*.md'))),
        'status': 'ok'
    })

    write(DIST / 'manifest.json', json.dumps(manifest, indent=2))
    write(DIST / 'tier_profile.yaml', yaml.safe_dump(tier_profile, sort_keys=False))
    write(DIST / 'validation_report.json', json.dumps(validation_report, indent=2))
    # Build unified TASK_INDEX.json
    _build_task_index(ROOT)

    # Update README.md with health badge
    readme_path = ROOT / 'README.md'
    if readme_path.exists():
        badge = _build_readme_health_badge(ROOT)
        if badge:
            readme_txt = readme_path.read_text()
            marker = '## Pack health'
            if marker in readme_txt:
                start = readme_txt.index(marker)
                rest = readme_txt[start + len(marker):]
                next_sec = rest.find('\n## ')
                readme_txt = (readme_txt[:start] + badge.strip() + '\n\n' + readme_txt[start + len(marker) + next_sec + 1:]) if next_sec >= 0 else (readme_txt[:start] + badge.strip() + '\n')
            else:
                readme_txt = readme_txt.rstrip() + '\n\n' + badge.strip() + '\n'
            readme_path.write_text(readme_txt)

    manifest['artifacts']['TASK_INDEX.json'] = {'path': 'dist/runtime/TASK_INDEX.json', 'type': 'compiled_index'}
    manifest['artifacts']['TASK_INDEX.md'] = {'path': 'dist/runtime/TASK_INDEX.md', 'type': 'compiled_index'}

    print(json.dumps({'generated_artifact_count': len(manifest['artifacts'])}, indent=2))


if __name__ == '__main__':
    main()
