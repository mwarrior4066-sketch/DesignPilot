#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
DIST.mkdir(exist_ok=True)
manifest = json.loads((ROOT/'PACK_MANIFEST.json').read_text(encoding='utf-8'))
version = manifest['version']

checks = [
    ['python3','generate_runtime_overlay.py'],
    ['python3','generate_human_mirrors.py'],
    ['python3','refresh_source_registry.py'],
    ['python3','refresh_project_continuity.py'],
    ['python3','validate_examples.py'],
    ['python3','lint_pack.py','.','--strict'],
    ['python3','run_regression_suite.py'],
    ['python3','validate_project_workspace.py'],
]


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))



def collect_continuity_failures(version: str):
    failures = []
    roadmap = (ROOT / 'projects' / 'designpilot' / 'context' / 'CASE_STUDY_ROADMAP.md').read_text(encoding='utf-8')
    active = (ROOT / 'projects' / 'designpilot' / 'context' / 'ACTIVE_STATE.md').read_text(encoding='utf-8')
    queue = (ROOT / 'projects' / 'designpilot' / 'context' / 'TASK_QUEUE.md').read_text(encoding='utf-8')
    if f'- Current release line: v{version}' not in roadmap:
        failures.append('roadmap_release_line_mismatch')
    if f'- Current release: v{version}' not in active:
        failures.append('active_state_release_mismatch')
    if f'synchronize v{version} release authority' not in queue:
        failures.append('task_queue_release_mismatch')
    for rel in [
        'knowledge-base/indices/source_doc_sections.json',
        'knowledge-base/indices/source_section_map.json',
        'knowledge-base/indices/runtime_summary_map.json',
    ]:
        data = load_json(ROOT / rel)
        if data.get('pack_version') != version:
            failures.append(f'index_pack_version_mismatch:{rel}')
    return failures

def collect_metrics():
    tasks = load_json(ROOT / 'schemas' / 'task_contracts.json')['tasks']
    active_skills = manifest['active_skills']
    evals = list((ROOT / 'tests' / 'evals').glob('*.json'))
    regression = load_json(ROOT / 'tests' / 'regression_suite.json')['tests']
    benchmarks = list((ROOT / 'projects' / 'designpilot' / 'process' / 'reviews' / 'benchmarks').glob('*.json'))
    external_conf = [p for p in (ROOT / 'projects' / 'designpilot' / 'process' / 'reviews' / 'external_signals').glob('*.md') if p.name != 'TRUST_SIGNAL_LOG.md']
    examples = list((ROOT / 'examples').glob('*.md'))
    route_cards = list((ROOT / 'runtime' / 'cards' / 'routes').glob('*.json'))
    contract_cards = list((ROOT / 'runtime' / 'cards' / 'contracts').glob('*.json'))
    skill_cards = list((ROOT / 'runtime' / 'cards' / 'skills').glob('*.md'))
    runtime_summaries = list((ROOT / 'knowledge-base' / 'runtime-summaries').glob('*.md'))
    direct_example_tasks = set()
    rubric_signatures = set()
    for path in evals:
        data = load_json(path)
        direct_example_tasks.add(data.get('task_contract'))
        scores = data.get('rubric_scores', {})
        rubric_signatures.add(tuple(sorted(scores.items())))
    active_skill_bases = {Path(x).stem for x in active_skills}
    covered_skill_bases = set()
    example_text = '\n'.join(p.read_text(encoding='utf-8', errors='ignore') for p in examples if p.name != 'README.md')
    for skill in active_skill_bases:
        if skill in example_text:
            covered_skill_bases.add(skill)
    roadmap = (ROOT / 'projects' / 'designpilot' / 'context' / 'CASE_STUDY_ROADMAP.md').read_text(encoding='utf-8')
    stale_flagship_continuity_count = 0 if 'Workspace freshness: current' in roadmap else 1
    metrics = {
        'active_skill_count': len(active_skills),
        'skills_with_direct_example_signal': len(covered_skill_bases),
        'task_contract_count': len(tasks),
        'direct_example_task_count': len(direct_example_tasks),
        'regression_count': len(regression),
        'fail_case_count': sum(1 for t in regression if t['expected_decision'] == 'FAIL'),
        'benchmark_artifact_count': len(benchmarks),
        'external_confidence_artifact_count': len(external_conf),
        'eval_signature_count': len(rubric_signatures),
        'stale_flagship_continuity_count': stale_flagship_continuity_count,
        'example_coverage_ratio': round(len(direct_example_tasks) / max(len(tasks), 1), 3),
        'runtime_route_card_count': len(route_cards),
        'runtime_contract_card_count': len(contract_cards),
        'runtime_skill_card_count': len(skill_cards),
        'runtime_summary_count': len(runtime_summaries),
    }
    return metrics


def evaluate_gates(metrics):
    failures = []
    if metrics['regression_count'] < 20:
        failures.append('regression_count_below_threshold')
    if metrics['fail_case_count'] < 8:
        failures.append('fail_case_count_below_threshold')
    if metrics['eval_signature_count'] <= 1:
        failures.append('eval_variance_missing')
    if metrics['example_coverage_ratio'] < 0.75:
        failures.append('example_coverage_ratio_below_threshold')
    if metrics['benchmark_artifact_count'] < 3:
        failures.append('benchmark_artifact_count_below_threshold')
    if metrics['external_confidence_artifact_count'] < 2:
        failures.append('external_confidence_artifact_count_below_threshold')
    if metrics['stale_flagship_continuity_count'] > 0:
        failures.append('flagship_continuity_stale')
    if metrics['runtime_route_card_count'] < metrics['task_contract_count']:
        failures.append('runtime_route_cards_incomplete')
    if metrics['runtime_contract_card_count'] < metrics['task_contract_count']:
        failures.append('runtime_contract_cards_incomplete')
    if metrics['runtime_skill_card_count'] < metrics['active_skill_count']:
        failures.append('runtime_skill_cards_incomplete')
    if metrics['runtime_summary_count'] < 20:
        failures.append('runtime_summaries_incomplete')
    return failures


results = []
for cmd in checks:
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    results.append({'cmd':' '.join(cmd),'returncode':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr})
    if proc.returncode != 0:
        report = {'version':version,'decision':'HOLD','gate_failures':['preflight_check_failed'],'metrics':collect_metrics(),'results':results}
        (DIST/f'release_quality_report_v{version}.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
        print(json.dumps(report, indent=2))
        raise SystemExit(1)

metrics = collect_metrics()
gate_failures = evaluate_gates(metrics)
gate_failures.extend(collect_continuity_failures(version))
decision = 'PROMOTE' if not gate_failures else 'HOLD'
report = {'version':version,'decision':decision,'gate_failures':gate_failures,'metrics':metrics,'results':results}
(DIST/f'release_quality_report_v{version}.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
if gate_failures:
    raise SystemExit(1)
