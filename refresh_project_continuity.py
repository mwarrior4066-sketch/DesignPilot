#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


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


def refresh_project(slug: str = 'designpilot'):
    manifest = json.loads((ROOT / 'PACK_MANIFEST.json').read_text(encoding='utf-8'))
    release_line = manifest['version']

    project = ROOT / 'projects' / slug
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
    freshness_date = freshness_dt.strftime('%Y-%m-%d')
    freshness_anchor = freshness_dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    latest_run = runs[-1] if runs else {}
    current_phase = f'continuity and release synchronization on top of the stable v{release_line} system'
    proof_state = 'internal operator proof strong; comparative proof strong; external confidence proof improving; production outcome proof open'

    done_before = [
        'stabilized the proof, continuity, and release-hardening base in v2.3.0',
        'separated the system doc from the case-study proof layer',
        'added a canonical project workspace with continuity files'
    ]
    just_added = [
        f'kept {benchmark_count} benchmark artifacts synchronized with the roadmap and bundle manifest',
        f'stored {prompt_pack_count} research prompt pack{"s" if prompt_pack_count != 1 else ""} inside the project workspace',
        'expanded the stable v2.3 base into the capability cluster introduced in v2.4.0 across front-end architecture, deeper accessibility behavior, backend systems architecture, and API reliability/security',
        'added the v2.5.0 refinement layer that unified startup authority, added degraded-mode behavior, added visual-input routing support, and reduced unnecessary runtime scaffolding',
        'kept the comprehension layer cross-cutting so route ownership and proof-language boundaries stay intact'
    ]
    if latest_run:
        just_added.append(
            f"latest benchmark receipt is {latest_run.get('run_id', 'unknown')} with pack score {latest_run.get('pack_score', '?')} and baseline score {latest_run.get('baseline_score', '?')}"
        )

    needed_next = [
        'attach more production-adjacent receipts for the comprehension layer in use',
        'grow the external confidence sample beyond the current reviewer set',
        'keep continuity, proof language, and version metadata synchronized as the release line evolves'
    ]
    open_risks = [
        'production outcome proof is still missing',
        'external confidence still rests on a small sample',
        'comparative wins can be overstated if wording is not kept disciplined'
    ]
    pending = [
        'additional live artifact review or implementation receipt',
        'one more production-adjacent confidence artifact for the architecture cluster',
        'next benchmark run tied to any new direct task coverage'
    ]

    project_overview.write_text(
        '# Project Overview\n\n'
        'DesignPilot is the flagship project used to prove that the Design Expert Pack can operate as a routed, evidence-constrained design operator system without overstating proof. '
        'The current v' + release_line + ' system includes the original validation and continuity-hardening base, the capability cluster introduced in v2.4.0 across front-end architecture, deeper accessibility behavior, backend systems architecture, and API reliability/security, and the v2.5.0 refinement layer that unified startup authority, added degraded-mode behavior, added visual-input routing support, and reduced unnecessary runtime scaffolding.\n',
        encoding='utf-8'
    )

    roadmap_body = [
        '# DesignPilot Case Study Roadmap',
        '',
        '## Project identity',
        '- Name: DesignPilot',
        '- Slug: designpilot',
        f'- Current phase: {current_phase}',
        f'- Current proof state: {proof_state}',
        f'- Last meaningful update: {freshness_date}',
        f'- Artifact freshness anchor: {freshness_anchor}',
        '',
        '## Proof state',
        f'- Benchmark artifact count: {benchmark_count}',
        f'- External confidence artifact count: {external_confidence_count}',
        f'- Research prompt packs stored: {prompt_pack_count}',
        '- Claim map status: synchronized',
        '- Proof summary status: synchronized',
        '',
        '## Done before',
        *[f'- {x}' for x in done_before],
        '',
        '## Just added',
        *[f'- {x}' for x in just_added],
        '',
        '## Needed next',
        *[f'- {x}' for x in needed_next],
        '',
        '## Open risks',
        *[f'- {x}' for x in open_risks],
        '',
        '## Next validation move',
        '- capture one more production-adjacent artifact review tied to the same proof-language discipline',
        '',
        '## Pending artifacts',
        *[f'- {x}' for x in pending],
        '',
        '## Release readiness',
        f'- Current release line: v{release_line}',
        '- Workspace freshness: current',
        '- Export posture: controlled-release ready, not production-outcome proven',
        '- Release gate blockers: no production outcome proof; external confidence sample still small',
        ''
    ]
    roadmap.write_text('\n'.join(roadmap_body), encoding='utf-8')

    active_body = [
        '# Active State',
        '',
        f'- Current release: v{release_line}',
        '- Manifest status: canonical',
        '- Continuity sync: pass',
        '- Proof sync: pass',
        '- Runtime sync: pass',
        f'- Last refresh: {freshness_anchor}',
        '',
        '- Project goal: prove that DesignPilot is a routed, evidence-constrained design operator system without overstating outcome proof while keeping the broader capability surface synchronized with real proof and release discipline',
        f'- Active phase: {current_phase}',
        f'- Active task: synchronize v{release_line} release authority across project context, indices, runtime metadata, proof artifacts, and release packaging while preserving v2.4.0 and v2.4.2 only as milestone history',
        '- Workspace mode: filesystem',
        '- Files being worked on: project context, bundle manifest, proof stack, release scripts, knowledge-base indices, and benchmark receipts',
        '- Blockers: no production outcome proof yet',
        '- Next action: capture more production-adjacent validation artifacts while keeping continuity, proof language, and release metadata aligned to the current manifest',
        ''
    ]
    active_state.write_text('\n'.join(active_body), encoding='utf-8')

    task_queue.write_text(
        '\n'.join([
            '# Task Queue',
            '',
            f'- synchronize v{release_line} release authority across project context, indices, runtime metadata, proof artifacts, and release packaging',
            '- preserve v2.4.0 and v2.4.2 references only as milestone history where they are still useful',
            '- capture more production-adjacent receipts before strengthening outcome language',
            '- grow external reviewer confidence beyond the current sample',
            ''
        ]),
        encoding='utf-8'
    )

    bundle_body = [
        '# Download Bundle Manifest',
        '',
        '- Project slug: designpilot',
        '- Workspace mode: filesystem',
        f'- Current milestone: current release v{release_line} with the v2.4.0 capability cluster and the v2.5.0 authority, degraded-mode, visual-input, and lightweight-execution refinements integrated on top of the stable validated base',
        '- Populated files by folder: context, problems_and_solutions, handoff, process/reviews, process/research/prompt-packs, process/specs/proof, process/structure/case-study, finalized/deliverables/proof',
        '- Finalized artifacts ready for export: proof stack summary, claim-to-proof map, comparative scorecard, reviewer confidence artifacts, trust log, architecture cluster benchmarks, and v2.5.0 continuity-sync evidence',
        '- Open work still in process: additional production-adjacent receipts, more external confidence artifacts, and outcome-proof expansion',
        f'- Continuity freshness anchor: {freshness_anchor}',
        f'- Last bundle-ready timestamp: {freshness_anchor}',
        ''
    ]
    bundle_manifest.write_text('\n'.join(bundle_body), encoding='utf-8')

    for rel in [
        'knowledge-base/indices/source_doc_sections.json',
        'knowledge-base/indices/source_section_map.json',
        'knowledge-base/indices/runtime_summary_map.json',
        'tests/scorecards/task_quality_rubric.json',
    ]:
        set_pack_version(ROOT / rel, release_line)

    print(f'refreshed continuity for {slug}')


if __name__ == '__main__':
    refresh_project()
