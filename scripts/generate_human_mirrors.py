#!/usr/bin/env python3
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contracts = json.loads((ROOT / 'src' / 'schemas' / 'task_contracts.json').read_text(encoding='utf-8'))
routes = json.loads((ROOT / 'src' / 'schemas' / 'routing_registry.json').read_text(encoding='utf-8'))
rules = json.loads((ROOT / 'src' / 'schemas' / 'validation_rules.json').read_text(encoding='utf-8'))
scorecard = {}
regression = json.loads((ROOT / 'tests' / 'regression_suite.json').read_text(encoding='utf-8'))

example_map = defaultdict(list)
for eval_path in sorted((ROOT / 'tests' / 'evals').glob('*.json')):
    try:
        data = json.loads(eval_path.read_text(encoding='utf-8'))
    except Exception:
        continue
    example_map[data.get('task_contract')].append(data.get('example', eval_path.stem))

regression_map = defaultdict(list)
for test in regression.get('tests', []):
    regression_map[test.get('validator_task')].append(f"{test['id']} ({test['category']})")

out = [
    '# Output Contracts by Task',
    '',
    '> Generated from `src/schemas/task_contracts.json`, stored evals, and `tests/regression_suite.json`. Add contract changes in the schema first, then regenerate.',
    '',
    'This is the human-readable contract catalog for the pack. Each contract entry shows the required sections, the named decisions the task must make, the evidence classes that must appear, the shortcut/overclaim patterns that should fail, and the example / regression artifacts that currently prove the route.',
    ''
]
for task in contracts['tasks']:
    out += [
        f"## {task['title']}",
        '',
        f"- Task ID: `{task['task_id']}`",
        f"- Task group: {task['task_group']}",
        f"- Allowed modes: {', '.join(task['allowed_modes'])}",
        f"- Allowed phases: {', '.join(task['allowed_phases'])}",
        f"- Required skills: {', '.join(task['required_skills'])}",
        f"- Data owner: {task['data_owner']}",
        f"- Risk tier: {task['risk_tier']}",
        f"- SLA freshness: {task['freshness_expectation']}",
        '',
        '### Why this contract exists',
        f"`{task['task_id']}` must make the governing route visible. A compliant answer needs the right decisions, the right evidence classes, and the right proof language for this task.",
        '',
        '### Required sections',
        '| Section | Minimum substance | Why it exists |',
        '|---|---:|---|'
    ]
    for sec in task['required_sections']:
        out.append(f"| {sec['name']} | {sec['min_words']} words | {sec.get('purpose', sec.get('rationale', ''))} |")
    out += [
        '',
        '### Required decisions',
        *[f"- {x}" for x in task.get('required_decisions', [])],
        '',
        '### Required evidence classes',
        *[f"- {x}" for x in task.get('required_evidence_classes', [])],
        '',
        '### Example coverage',
        *[f"- {x}" for x in (example_map.get(task['task_id']) or ['no stored example linked yet'])],
        '',
        '### Regression references',
        *[f"- {x}" for x in (regression_map.get(task['task_id']) or ['no regression references linked yet'])],
        '',
        '### Forbidden shortcuts',
    ]
    for item in task.get('forbidden_shortcuts', []):
        out.append(f"- `{item['id']}` — {item['description']}")
        out.extend([f"  - signal: {p}" for p in item['patterns']])
    out += ['', '### Overclaim rules']
    for item in task.get('overclaim_rules', []):
        out.append(f"- `{item['id']}` — {item['description']}")
        out.append(f"  - blocked terms: {', '.join(item['forbidden_terms'])}")
        out.append(f"  - evidence escape hatch: {', '.join(item['allowed_if_any'])}")
    out += ['', '### Legacy fail patterns']
    out.extend([f"- hard fail: {p}" for p in task['hard_fail_patterns']])
    out.extend([f"- soft fail: {p}" for p in task['soft_fail_patterns']])
    out.append('')
(ROOT / 'src' / 'operator' / 'governance' / 'OUTPUT_CONTRACTS_BY_TASK.md').write_text('\n'.join(out), encoding='utf-8')

rulebook = [
    '# Runtime Validation Layer',
    '',
    '> Generated from `src/schemas/validation_rules.json` and implemented by `runtime_validator.py`.',
    '',
    'The runtime validator is the executable rulebook for the pack. Global structure checks fire first, task-contract checks fire second, route-specific semantic checks fire third, and integrity checks fire last. This is meant to block outputs that are polished, dense, or specific-sounding but still weak.',
    ''
]
for category, title in [('hard_rules', 'Hard Rules'), ('semantic_rules', 'Semantic Rules'), ('integrity_rules', 'Integrity Rules')]:
    rulebook += [
        f'## {title}',
        '',
        '| Rule ID | Applies to | Failure trigger | Human remediation |',
        '|---|---|---|---|'
    ]
    for rule in rules[category]:
        rulebook.append(
            f"| `{rule['rule_id']}` | {', '.join(rule['applies_to'])} | {rule['failure_trigger']} | {rule['remediation']} |"
        )
    rulebook.append('')
rulebook += [
    '## Validator order of operations',
    '',
    '1. required sections and density',
    '2. tradeoff, rationale, and alternative coverage',
    '3. required task decisions',
    '4. required evidence-class coverage',
    '5. forbidden shortcuts and overclaim patterns',
    '6. unsupported specificity and contradiction checks',
    '7. route traceability and release integrity checks',
    '',
    '## Failure exception report',
    '| Failure family | Typical signal | First recovery move |',
    '|---|---|---|',
    '| Missing route decision | The answer sounds thoughtful but never makes the route-owning call | Add the missing governing decision instead of adding more polish |',
    '| Typed evidence gap | The answer says “proof” or sounds certain without the required evidence class | Name the missing evidence class and add the receipt or rule |',
    '| Unsupported specificity | Precise numbers appear without standards, artifacts, or inference labels | Tie the number to a standard, artifact, or explicit assumption |',
    '| Route bleed | Styling, brand, or implementation language overtakes the governing task | Pull the answer back to the route that owns the failure |',
    '| Stale continuity | Roadmap or error log older than the changed artifacts | Refresh project continuity before export |',
    ''
]
(ROOT / 'src' / 'operator' / 'governance' / 'RUNTIME_VALIDATION_LAYER.md').write_text('\n'.join(rulebook), encoding='utf-8')

catalog = [
    '# Route Catalog',
    '',
    '> Generated from `src/schemas/routing_registry.json`, example evals, and the regression suite.',
    '',
    'This catalog explains how the pack chooses a governing route, which skills it loads in support, where route confusion usually happens, and what artifacts currently prove the route.',
    '',
    '## Compound route policy',
    '',
    routes['compound_route_policy']['governing_route_rule'],
    '',
    '### Selection order',
    *[f"- {x}" for x in routes['compound_route_policy']['selection_order']],
    '',
    '### Conflict rules',
    '| Rule ID | When it applies | Winner | Loser | Why |',
    '|---|---|---|---|---|'
]
for rule in routes['compound_route_policy']['conflict_rules']:
    catalog.append(f"| `{rule['rule_id']}` | {rule['when']} | {rule['winner']} | {rule['loser']} | {rule['reason']} |")
catalog.append('')
for route in routes['routes']:
    catalog += [
        f"## {route['route_id']}",
        '',
        f"- Task ID: `{route['task_id']}`",
        f"- Primary mode: {route['primary_mode']}",
        f"- Primary phase: {route['primary_phase']}",
        f"- Loaded skills: {', '.join(route['loaded_skills'])}",
        f"- Fallback route: {route['fallback_route_id']}",
        '',
        '### Trigger conditions',
        *[f'- {x}' for x in route['trigger_conditions']],
        '',
        '### Preconditions',
        *[f'- {x}' for x in route['preconditions']],
        '',
        '### Selection logic',
        route['selection_logic'],
        '',
        '### Supporting skill policy',
        *[f'- {x}' for x in route.get('supporting_skills', [])],
        '',
        '### Common adjacent-route confusions',
        *[f'- {x}' for x in route.get('adjacent_route_confusions', [])],
        '',
        '### Compound-task notes',
        *[f'- {x}' for x in route.get('compound_notes', [])],
        '',
        '### Example coverage',
        *[f"- {x}" for x in (example_map.get(route['task_id']) or ['no stored example linked yet'])],
        '',
        '### Regression references',
        *[f"- {x}" for x in (regression_map.get(route['task_id']) or ['no regression references linked yet'])],
        '',
        '### Known tensions',
        *[f'- {x}' for x in route['known_tensions']],
        '',
        '### Exit conditions',
        *[f'- {x}' for x in route['exit_conditions']],
        ''
    ]
(ROOT / 'src' / 'operator' / 'core' / 'ROUTE_CATALOG.md').write_text('\n'.join(catalog), encoding='utf-8')

rubric = [
    '# Pack Quality Rubric',
    '',
    '> Generated from `tests/scorecards/task_quality_rubric.json`.',
    '',
    'This readable mirror exists so a human maintainer can inspect the operational scoring logic without reading the raw JSON scorecard.',
    '',
    '| Criterion | Weight | Pass threshold | Judge question |',
    '|---|---:|---:|---|'
]
for c in scorecard['criteria']:
    rubric.append(f"| {c['id']} | {c['weight']} | {c['pass_threshold']} | {c['question']} |")
rubric += ['', '## Bias controls', *[f'- {x}' for x in scorecard['bias_controls']], '']
(ROOT / 'src' / 'operator' / 'governance' / 'PACK_QUALITY_RUBRIC.md').write_text('\n'.join(rubric), encoding='utf-8')
print('generated human-readable mirrors')
