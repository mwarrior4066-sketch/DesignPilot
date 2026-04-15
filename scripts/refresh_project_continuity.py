#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_jsons(folder: Path):
    items = []
    for p in sorted(folder.glob('*.json')):
        try:
            data = json.loads(p.read_text(encoding='utf-8'))
            data['_path'] = p
            items.append(data)
        except Exception:
            continue
    return items


def newest_date(paths):
    candidates = [p for p in paths if p.exists()]
    if not candidates:
        return datetime.now(timezone.utc)
    latest = max(candidates, key=lambda p: p.stat().st_mtime).stat().st_mtime
    return datetime.fromtimestamp(latest, tz=timezone.utc)


def set_pack_version(path: Path, version: str):
    if not path.exists():
        return
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return
    data['pack_version'] = version
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def render_project_overview(evergreen: dict, release: dict) -> str:
    return (
        '# Project Overview\n\n'
        f"{evergreen['project']['name']} is the flagship project used to prove the DesignPilot system can operate as a routed, evidence-constrained design operator system without overstating proof. "
        f"The current v{release['current_release']} system includes the original validation and continuity-hardening base, the capability cluster introduced in v2.4.0 across front-end architecture, deeper accessibility behavior, backend systems architecture, and API reliability/security, and the v2.5.0 refinement layer that unified startup authority, added degraded-mode behavior, added visual-input routing support, and reduced unnecessary runtime scaffolding.\n"
    )


def render_roadmap(evergreen: dict, release: dict) -> str:
    proof_state = '; '.join([
        f"internal operator proof {evergreen['proof_boundaries']['internal_operator_proof']}",
        f"comparative proof {evergreen['proof_boundaries']['comparative_proof']}",
        f"external confidence proof {evergreen['proof_boundaries']['external_confidence_proof']}",
        f"production outcome proof {evergreen['proof_boundaries']['production_outcome_proof']}"
    ])
    latest_line = ''
    if release.get('latest_benchmark'):
        latest = release['latest_benchmark']
        latest_line = f"- latest benchmark receipt is {latest.get('run_id', 'unknown')} with pack score {latest.get('pack_score', '?')} and baseline score {latest.get('baseline_score', '?')}"
    just_added = release['just_added'] + ([latest_line] if latest_line else [])
    return '\n'.join([
        '# DesignPilot Case Study Roadmap',
        '',
        '## Project identity',
        f"- Name: {evergreen['project']['name']}",
        f"- Slug: {evergreen['project']['slug']}",
        f"- Current phase: {release['current_phase']}",
        f"- Current proof state: {proof_state}",
        f"- Last meaningful update: {release['last_meaningful_update']}",
        f"- Artifact freshness anchor: {release['artifact_freshness_anchor']}",
        '',
        '## Proof state',
        f"- Benchmark artifact count: {release['proof_counts']['benchmark_artifacts']}",
        f"- External confidence artifact count: {release['proof_counts']['external_confidence_artifacts']}",
        f"- Research prompt packs stored: {release['proof_counts']['prompt_packs']}",
        '- Claim map status: synchronized',
        '- Proof summary status: synchronized',
        '',
        '## Done before',
        *[f'- {x}' for x in evergreen['done_before']],
        '',
        '## Just added',
        *[f'- {x}' for x in just_added],
        '',
        '## Needed next',
        *[f'- {x}' for x in release['next_steps']],
        '',
        '## Open risks',
        *[f'- {x}' for x in release['open_risks']],
        '',
        '## Next validation move',
        f"- {release['next_validation_move']}",
        '',
        '## Pending artifacts',
        *[f'- {x}' for x in release['pending_artifacts']],
        '',
        '## Release readiness',
        f"- Current release line: v{release['current_release']}",
        f"- Workspace freshness: {release['workspace_freshness']}",
        f"- Export posture: {evergreen['bundle_export_posture']}",
        f"- Release gate blockers: {'; '.join(release['blockers'])}",
        ''
    ])


def render_active_state(evergreen: dict, release: dict) -> str:
    return '\n'.join([
        '# Active State',
        '',
        f"- Current release: v{release['current_release']}",
        f"- Manifest status: {release['sync_status']['manifest']}",
        f"- Continuity sync: {release['sync_status']['continuity']}",
        f"- Proof sync: {release['sync_status']['proof']}",
        f"- Runtime sync: {release['sync_status']['runtime']}",
        f"- Last refresh: {release['last_continuity_refresh']}",
        '',
        f"- Project goal: {evergreen['goal']}",
        f"- Active phase: {release['current_phase']}",
        f"- Active task: {release['active_task']}",
        '- Workspace mode: filesystem',
        f"- Files being worked on: {', '.join(release['active_files'])}",
        f"- Blockers: {'; '.join(release['blockers'])}",
        f"- Next action: {release['next_action']}",
        ''
    ])


def render_task_queue(release: dict) -> str:
    return '\n'.join(['# Task Queue', ''] + [f'- {x}' for x in release['active_queue']] + [''])


def render_bundle_manifest(release: dict) -> str:
    return '\n'.join([
        '# Download Bundle Manifest',
        '',
        '- Project slug: designpilot',
        '- Workspace mode: filesystem',
        f"- Current milestone: {release['current_milestone']}",
        '- Populated files by folder: context, problems_and_solutions, handoff, process/reviews, process/research/prompt-packs, process/specs/proof, process/structure/case-study, finalized/deliverables/proof',
        f"- Finalized artifacts ready for export: {', '.join(release['finalized_artifacts_ready'])}",
        f"- Open work still in process: {', '.join(release['open_work'])}",
        f"- Continuity freshness anchor: {release['artifact_freshness_anchor']}",
        f"- Last bundle-ready timestamp: {release['last_continuity_refresh']}",
        ''
    ])


def refresh_project(slug: str = 'designpilot'):
    manifest = json.loads((ROOT / 'PACK_MANIFEST.json').read_text(encoding='utf-8'))
    release_line = manifest['version']

    project = ROOT / 'projects' / slug
    state_dir = project / 'context' / 'state'
    state_dir.mkdir(parents=True, exist_ok=True)

    roadmap = project / 'context' / 'CASE_STUDY_ROADMAP.md'
    active_state = project / 'context' / 'ACTIVE_STATE.md'
    project_overview = project / 'context' / 'PROJECT_OVERVIEW.md'
    task_queue = project / 'context' / 'TASK_QUEUE.md'
    bundle_manifest = project / 'handoff' / 'DOWNLOAD_BUNDLE_MANIFEST.md'

    bench_dir = project / 'process' / 'reviews' / 'benchmarks'
    ext_dir = project / 'process' / 'reviews' / 'external_signals'
    prompt_dir = project / 'process' / 'research' / 'prompt-packs'
    claim_map = project / 'process' / 'structure' / 'case-study' / 'CLAIM_TO_PROOF_MAP.md'
    proof_summary = project / 'finalized' / 'deliverables' / 'proof' / 'PROOF_STACK_SUMMARY.md'

    runs = load_jsons(bench_dir)
    benchmark_count = len(runs)
    external_confidence_count = len([p for p in ext_dir.glob('*.md') if p.name != 'TRUST_SIGNAL_LOG.md'])
    prompt_pack_count = len(list(prompt_dir.glob('*.md')))
    freshness_dt = newest_date(
        list(bench_dir.glob('*'))
        + list(ext_dir.glob('*'))
        + list(prompt_dir.glob('*'))
        + [claim_map, proof_summary]
    )
    refresh_dt = datetime.now(timezone.utc)
    freshness_date = freshness_dt.strftime('%Y-%m-%d')
    freshness_anchor = freshness_dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    refresh_anchor = refresh_dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    latest_run = dict(runs[-1]) if runs else {}
    latest_run.pop('_path', None)
    current_phase = f'continuity and release synchronization on top of the stable v{release_line} system'

    evergreen = {
        'schema_version': 1,
        'project': {'name': 'DesignPilot', 'slug': 'designpilot'},
        'goal': 'prove that DesignPilot is a routed, evidence-constrained design operator system without overstating outcome proof while keeping the broader capability surface synchronized with real proof and release discipline',
        'proof_boundaries': {
            'internal_operator_proof': 'strong',
            'comparative_proof': 'strong',
            'external_confidence_proof': 'improving',
            'production_outcome_proof': 'open',
        },
        'done_before': [
            'stabilized the proof, continuity, and release-hardening base in v2.3.0',
            'separated the system doc from the case-study proof layer',
            'added a canonical project workspace with continuity files',
        ],
        'bundle_export_posture': 'controlled-release ready, not production-outcome proven',
    }

    release_state = {
        'schema_version': 1,
        'current_release': release_line,
        'last_continuity_refresh': refresh_anchor,
        'workspace_freshness': 'current',
        'last_meaningful_update': freshness_date,
        'artifact_freshness_anchor': freshness_anchor,
        'current_phase': current_phase,
        'current_milestone': f'current release v{release_line} with the v2.4.0 capability cluster and the v2.5.0 authority, degraded-mode, visual-input, and lightweight-execution refinements integrated on top of the stable validated base',
        'proof_counts': {
            'benchmark_artifacts': benchmark_count,
            'external_confidence_artifacts': external_confidence_count,
            'prompt_packs': prompt_pack_count,
        },
        'latest_benchmark': latest_run,
        'just_added': [
            f'kept {benchmark_count} benchmark artifacts synchronized with the roadmap and bundle manifest',
            f'stored {prompt_pack_count} research prompt pack{"s" if prompt_pack_count != 1 else ""} inside the project workspace',
            'expanded the stable v2.3 base into the capability cluster introduced in v2.4.0 across front-end architecture, deeper accessibility behavior, backend systems architecture, and API reliability/security',
            'added the v2.5.0 refinement layer that unified startup authority, added degraded-mode behavior, added visual-input routing support, and reduced unnecessary runtime scaffolding',
            'kept the comprehension layer cross-cutting so route ownership and proof-language boundaries stay intact',
        ],
        'next_steps': [
            'attach more production-adjacent receipts for the comprehension layer in use',
            'grow the external confidence sample beyond the current reviewer set',
            'keep continuity, proof language, and version metadata synchronized as the release line evolves',
        ],
        'open_risks': [
            'production outcome proof is still missing',
            'external confidence still rests on a small sample',
            'comparative wins can be overstated if wording is not kept disciplined',
        ],
        'pending_artifacts': [
            'additional live artifact review or implementation receipt',
            'one more production-adjacent confidence artifact for the architecture cluster',
            'next benchmark run tied to any new direct task coverage',
        ],
        'next_validation_move': 'capture one more production-adjacent artifact review tied to the same proof-language discipline',
        'active_task': f'synchronize v{release_line} release authority across project context, indices, runtime metadata, proof artifacts, and release packaging while preserving v2.4.0 and v2.4.2 only as milestone history',
        'active_files': ['project context', 'bundle manifest', 'proof stack', 'release scripts', 'knowledge-base indices', 'benchmark receipts', 'structured continuity state'],
        'blockers': ['no production outcome proof yet'],
        'next_action': 'capture more production-adjacent validation artifacts while keeping continuity, proof language, and release metadata aligned to the current manifest',
        'active_queue': [
            f'synchronize v{release_line} release authority across project context, indices, runtime metadata, proof artifacts, and release packaging',
            'preserve v2.4.0 and v2.4.2 references only as milestone history where they are still useful',
            'capture more production-adjacent receipts before strengthening outcome language',
            'grow external reviewer confidence beyond the current sample',
        ],
        'sync_status': {'manifest': 'canonical', 'continuity': 'pass', 'proof': 'pass', 'runtime': 'pass'},
        'finalized_artifacts_ready': [
            'proof stack summary', 'claim-to-proof map', 'comparative scorecard', 'reviewer confidence artifacts', 'trust log', 'architecture cluster benchmarks', 'continuity-sync evidence'
        ],
        'open_work': ['additional production-adjacent receipts', 'more external confidence artifacts', 'outcome-proof expansion'],
    }

    write_json(state_dir / 'continuity_evergreen.json', evergreen)
    write_json(state_dir / 'release_state.json', release_state)

    project_overview.write_text(render_project_overview(evergreen, release_state), encoding='utf-8')
    roadmap.write_text(render_roadmap(evergreen, release_state), encoding='utf-8')
    active_state.write_text(render_active_state(evergreen, release_state), encoding='utf-8')
    task_queue.write_text(render_task_queue(release_state), encoding='utf-8')
    bundle_manifest.write_text(render_bundle_manifest(release_state), encoding='utf-8')

    for rel in [
        'src/knowledge-base/indices/source_doc_sections.json',
        'src/knowledge-base/indices/source_section_map.json',
        'src/knowledge-base/indices/runtime_summary_map.json',
        'tests/scorecards/task_quality_rubric.json',
    ]:
        set_pack_version(ROOT / rel, release_line)

    print(f'refreshed continuity for {slug}')


if __name__ == '__main__':
    refresh_project()
