#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
DIST.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT / 'scripts'))

from _authority import load_authority_manifest, load_pack_manifest
from clean_distribution_noise import clean_distribution_noise


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def sync_release_metadata(version: str):
    readme_path = ROOT / 'README.md'
    text = readme_path.read_text(encoding='utf-8')
    text = re.sub(r'^Current stable release:\s+v[^\n]+\.$', f'Current stable release: v{version}.', text, flags=re.M)
    readme_path.write_text(text, encoding='utf-8')


def run_cmd(cmd: list[str]) -> dict:
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'},
    )
    return {
        'cmd': ' '.join(cmd),
        'returncode': proc.returncode,
        'stdout': proc.stdout,
        'stderr': proc.stderr,
    }


def collect_metrics(version: str) -> dict:
    manifest = load_pack_manifest()
    tasks = load_json(ROOT / 'src' / 'schemas' / 'task_contracts.json')['tasks']
    active_skills = manifest['active_skills']
    evals = list((ROOT / 'tests' / 'evals').glob('*.json'))
    regression = load_json(ROOT / 'tests' / 'regression_suite.json')['tests']
    benchmarks = list((ROOT / 'projects' / 'designpilot' / 'process' / 'reviews' / 'benchmarks').glob('*.json'))
    external_conf = [p for p in (ROOT / 'proof' / 'reviews' / 'external_signals').glob('*.md') if p.name != 'TRUST_SIGNAL_LOG.md']
    route_cards = list((ROOT / 'dist' / 'runtime' / 'routes').glob('*.json'))
    contract_cards = list((ROOT / 'dist' / 'runtime' / 'contracts').glob('*.json'))
    skill_cards = list((ROOT / 'dist' / 'runtime' / 'skills').glob('*.md'))
    runtime_summaries = list((ROOT / 'src' / 'knowledge-base' / 'runtime-summaries').glob('*.md'))
    lite_route_docs = list((ROOT / 'dist' / 'runtime' / 'route_cards').glob('*.md'))
    lite_contract_docs = list((ROOT / 'dist' / 'runtime' / 'contracts_lite').glob('*.md'))
    lite_starters = list((ROOT / 'dist' / 'runtime' / 'starters').glob('*.md'))
    launchers = list((ROOT / 'dist' / 'runtime' / 'task_launchers').glob('*.md'))
    structured_state = ROOT / 'projects' / 'designpilot' / 'context' / 'state' / 'release_state.json'
    proof_status = ROOT / 'proof' / 'PROOF_STATUS.md'
    proof_status_json = ROOT / 'proof' / 'status.json'
    proof_benchmark_index = ROOT / 'proof' / 'benchmarks' / 'README.md'
    proof_review_index = ROOT / 'proof' / 'reviews' / 'README.md'
    proof_receipt_index = ROOT / 'proof' / 'receipts' / 'README.md'
    blind_protocol = ROOT / 'docs' / 'proof' / 'MVEC_PROTOCOL.md'  # merged from BLIND_COMPARISON_PROTOCOL
    receipt_reports = list((ROOT / 'proof' / 'artifacts').glob('*.md'))
    compiled_manifest = load_json(ROOT / 'dist' / 'manifest.json') if (ROOT / 'dist' / 'manifest.json').exists() else {'artifacts': {}}
    validation_suite = load_json(ROOT / 'dist' / 'validation_suite_report.json') if (ROOT / 'dist' / 'validation_suite_report.json').exists() else {'decision': 'FAIL'}
    validation_suite_metadata = validation_suite.get('metadata', {})
    lite_validation = load_json(ROOT / 'dist' / 'lightweight_validation_report.json') if (ROOT / 'dist' / 'lightweight_validation_report.json').exists() else {'decision': 'FAIL'}
    integrity_validation = load_json(ROOT / 'dist' / 'integrity_validation_report.json') if (ROOT / 'dist' / 'integrity_validation_report.json').exists() else {'decision': 'FAIL'}
    return {
        'version': version,
        'active_skill_count': len(active_skills),
        'task_contract_count': len(tasks),
        'regression_count': len(regression),
        'fail_case_count': sum(1 for t in regression if t['expected_decision'] == 'FAIL'),
        'benchmark_artifact_count': len(benchmarks),
        'external_confidence_artifact_count': len(external_conf),
        'runtime_route_card_count': len(route_cards),
        'runtime_contract_card_count': len(contract_cards),
        'runtime_skill_card_count': len(skill_cards),
        'runtime_summary_count': len(runtime_summaries),
        'compiled_artifact_count': len(compiled_manifest.get('artifacts', {})),
        'lite_route_doc_count': len(lite_route_docs),
        'lite_contract_doc_count': len(lite_contract_docs),
        'lite_starter_count': len(lite_starters),
        'task_launcher_count': len(launchers),
        'compiled_runtime_summary_count': len(list((ROOT / 'dist' / 'runtime' / 'summaries').glob('*.md'))),
        'structured_release_state_present': structured_state.exists(),
        'proof_status_present': proof_status.exists(),
        'proof_status_json_present': proof_status_json.exists(),
        'proof_benchmark_index_present': proof_benchmark_index.exists(),
        'proof_review_index_present': proof_review_index.exists(),
        'proof_receipt_index_present': proof_receipt_index.exists(),
        'blind_protocol_present': blind_protocol.exists(),
        'receipt_artifact_count': len(receipt_reports),
        'validation_suite_decision': validation_suite.get('decision'),
        'validation_suite_integrity_executed': ('integrity_sync' in validation_suite_metadata.get('executed', []) and not validation_suite_metadata.get('fast_mode', False)),
        'lightweight_validation_decision': lite_validation.get('decision'),
        'integrity_validation_decision': integrity_validation.get('decision'),
    }


def collect_continuity_failures(version: str):
    failures = []
    release_state_path = ROOT / 'projects' / 'designpilot' / 'context' / 'state' / 'release_state.json'
    if not release_state_path.exists():
        failures.append('structured_release_state_missing')
        return failures
    release_state = load_json(release_state_path)
    if release_state.get('current_release') != version:
        failures.append('structured_release_state_version_mismatch')
    roadmap = (ROOT / 'projects' / 'designpilot' / 'context' / 'CASE_STUDY_ROADMAP.md').read_text(encoding='utf-8')
    active = (ROOT / 'projects' / 'designpilot' / 'context' / 'ACTIVE_STATE.md').read_text(encoding='utf-8')
    queue = (ROOT / 'projects' / 'designpilot' / 'context' / 'TASK_QUEUE.md').read_text(encoding='utf-8')
    if f'- Current release line: v{version}' not in roadmap:
        failures.append('roadmap_release_line_mismatch')
    if f'- Current release: v{version}' not in active:
        failures.append('active_state_release_mismatch')
    if f'synchronize v{version} release authority' not in queue:
        failures.append('task_queue_release_mismatch')
    return failures


def evaluate_gates(metrics: dict):
    failures = []
    if metrics['validation_suite_decision'] != 'PASS':
        failures.append('validation_suite_failed')
    if metrics['lightweight_validation_decision'] != 'PASS':
        failures.append('lightweight_validation_failed')
    if not metrics.get('validation_suite_integrity_executed', False):
        failures.append('validation_suite_missing_integrity_execution')
    if metrics['integrity_validation_decision'] != 'PASS':
        failures.append('integrity_validation_failed')
    if metrics['regression_count'] < 19:  # suite has 20 tests (pass-01..pass-20)
        failures.append('regression_count_below_threshold')
    if metrics['fail_case_count'] < 8:
        failures.append('fail_case_count_below_threshold')
    if metrics['benchmark_artifact_count'] < 3:
        failures.append('benchmark_artifact_count_below_threshold')
    if metrics['external_confidence_artifact_count'] < 2:
        failures.append('external_confidence_artifact_count_below_threshold')
    if metrics['runtime_route_card_count'] < metrics['task_contract_count']:
        failures.append('runtime_route_cards_incomplete')
    if metrics['runtime_contract_card_count'] < metrics['task_contract_count']:
        failures.append('runtime_contract_cards_incomplete')
    if metrics['runtime_skill_card_count'] < metrics['active_skill_count']:
        failures.append('runtime_skill_cards_incomplete')
    if metrics['runtime_summary_count'] < 20:
        failures.append('runtime_summaries_incomplete')
    if metrics['compiled_artifact_count'] < 20:
        failures.append('compiled_artifacts_incomplete')
    if metrics['lite_route_doc_count'] < metrics['runtime_route_card_count']:
        failures.append('lite_route_docs_incomplete')
    if metrics['lite_contract_doc_count'] < metrics['task_contract_count']:
        failures.append('lite_contract_docs_incomplete')
    if metrics['lite_starter_count'] < max(5, metrics['task_contract_count'] // 2):
        failures.append('lite_starters_incomplete')
    if metrics['task_launcher_count'] < metrics['task_contract_count']:
        failures.append('task_launchers_incomplete')
    if not metrics['structured_release_state_present']:
        failures.append('structured_release_state_missing')
    if not metrics['proof_status_present']:
        failures.append('proof_status_missing')
    if not metrics['proof_status_json_present']:
        failures.append('proof_status_json_missing')
    if not metrics['proof_benchmark_index_present']:
        failures.append('proof_benchmark_index_missing')
    if not metrics['proof_review_index_present']:
        failures.append('proof_review_index_missing')
    if not metrics['proof_receipt_index_present']:
        failures.append('proof_receipt_index_missing')
    if not metrics['blind_protocol_present']:
        failures.append('blind_protocol_missing')
    if metrics['receipt_artifact_count'] < 1:
        failures.append('receipt_artifact_count_below_threshold')
    return failures


def write_attempt_report(version: str, decision: str, gate_failures: list[str], metrics: dict, results: list[dict]):
    report = {
        'version': version,
        'decision': decision,
        'gate_failures': gate_failures,
        'metrics': metrics,
        'results': results,
    }
    path = DIST / f'release_attempt_v{version}.json'
    path.write_text(json.dumps(report, indent=2), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--skip-live-regression', action='store_true', help='Skip the live regression gate. Use only for offline local checks, not for final release promotion.')
    parser.add_argument('--live-model', default='claude-sonnet-4-20250514')
    args = parser.parse_args()

    authority = load_authority_manifest()
    version = load_pack_manifest()['version']
    clean_distribution_noise(ROOT, version=version)
    sync_release_metadata(version)

    pipeline = [
        ['python3', 'scripts/generate_runtime_overlay.py'],
        ['python3', 'scripts/compile_designpilot.py'],
        ['python3', 'scripts/refresh_source_registry.py'],
        ['python3', 'scripts/refresh_project_continuity.py'],
        ['python3', 'scripts/refresh_proof_status.py'],
        ['python3', 'scripts/run_validation_suite.py'],
        ['python3', 'scripts/run_regression_suite.py'],
    ]
    if not args.skip_live_regression:
        pipeline.append(['python3', 'scripts/run_live_regression.py', '--model', args.live_model, '--run-id', f'release-{version}', '--gate'])
    pipeline.extend([
        ['python3', 'scripts/generate_integrity_artifacts.py'],
        ['python3', 'scripts/validate_integrity_sync.py'],
    ])

    results = []
    for cmd in pipeline:
        result = run_cmd(cmd)
        results.append(result)
        if result['returncode'] != 0:
            metrics = collect_metrics(version)
            write_attempt_report(version, 'HOLD', ['pipeline_step_failed'], metrics, results)
            print(json.dumps({'decision': 'HOLD', 'failed_step': result['cmd'], 'report': f'dist/release_attempt_v{version}.json'}, indent=2))
            raise SystemExit(1)

    metrics = collect_metrics(version)
    gate_failures = evaluate_gates(metrics)
    gate_failures.extend(collect_continuity_failures(version))
    if gate_failures:
        write_attempt_report(version, 'HOLD', gate_failures, metrics, results)
        print(json.dumps({'decision': 'HOLD', 'gate_failures': gate_failures, 'report': f'dist/release_attempt_v{version}.json'}, indent=2))
        raise SystemExit(1)

    final_report = {
        'version': version,
        'decision': 'PROMOTE',
        'gate_failures': [],
        'metrics': metrics,
        'results': results,
        'authority_registry': 'config/authority_manifest.yaml',
        'release_authority': authority['authorities']['release']['packaging_script'],
    }
    report_path = DIST / f'release_quality_report_v{version}.json'
    report_path.write_text(json.dumps(final_report, indent=2), encoding='utf-8')
    print(json.dumps(final_report, indent=2))


if __name__ == '__main__':
    main()
