#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / 'proof'
PROJECT = ROOT / 'projects' / 'designpilot'


def load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def newest_timestamp(paths):
    existing = [p for p in paths if p.exists()]
    if not existing:
        return 'unknown'
    latest = max(existing, key=lambda p: p.stat().st_mtime)
    return datetime.fromtimestamp(latest.stat().st_mtime, timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def main():
    manifest = load_json(ROOT / 'PACK_MANIFEST.json')
    version = manifest['version']
    benchmark_dir = PROJECT / 'process' / 'reviews' / 'benchmarks'
    review_dir = PROJECT / 'process' / 'reviews' / 'external_signals'
    receipt_dir = PROOF / 'artifacts'
    eval_benchmark_dir = ROOT / 'evals' / 'internal_benchmarks'
    eval_review_dir = ROOT / 'evals' / 'external_reviews'

    benchmark_runs = sorted(benchmark_dir.glob('*.json'))
    benchmark_metrics = sorted((ROOT / 'evals' / 'metrics').glob('*.json'))
    internal_eval_specs = sorted(eval_benchmark_dir.glob('*.eval.json'))
    reviewer_confidence = sorted(review_dir.glob('reviewer-confidence-*.md'))
    production_adjacent = sorted(review_dir.glob('production-adjacent-artifact-review-*.md'))
    trust_logs = [review_dir / 'TRUST_SIGNAL_LOG.md', review_dir / 'user-confidence-log.md']
    receipt_reports = sorted(receipt_dir.glob('*.md'))
    release_reports = sorted((ROOT / 'dist').glob('release_quality_report_v*.json'))
    integrity_reports = sorted((ROOT / 'proof' / 'artifacts').glob('integrity_pass_report_v*.md'))
    handoff_files = [ROOT / 'HANDOFF_MANIFEST.json', ROOT / 'HANDOFF_README.md']

    layer_summary = {
        'schema_version': 1,
        'version': version,
        'generated_at': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'layers': {
            'internal_consistency_regression': {
                'meaning': 'Self-checks that the operator system compiles, validates, and resists known failure cases.',
                'status': 'present',
                'artifacts': {
                    'validation_reports': [
                        'dist/validation_suite_report.json',
                        'dist/lightweight_validation_report.json',
                        'dist/workspace_validation_report.json',
                        'dist/examples_validation_report.json',
                        'dist/integrity_validation_report.json'
                    ],
                    'regression_suite': 'tests/regression_suite.json',
                    'regression_runner': 'scripts/run_regression_suite.py',
                    'live_regression_runner': 'scripts/run_live_regression.py'
                }
            },
            'comparative_benchmarks': {
                'meaning': 'Internal A/B or baseline comparisons using the same prompt and a shared rubric.',
                'status': 'present' if benchmark_runs else 'missing',
                'artifact_count': len(benchmark_runs),
                'eval_spec_count': len(internal_eval_specs),
                'metric_run_count': len(benchmark_metrics),
                'canonical_source': 'projects/designpilot/process/reviews/benchmarks/'
            },
            'external_or_blinded_reviews': {
                'meaning': 'Reviewer confidence signals and any blinded comparison work that is independent from internal self-scoring.',
                'status': 'present' if (reviewer_confidence or production_adjacent) else 'missing',
                'reviewer_confidence_count': len(reviewer_confidence),
                'production_adjacent_count': len(production_adjacent),
                'blind_review_protocol_only': True,
                'comparative_runner': 'scripts/run_comparative.py',
                'live_eval_storage': 'tests/live_evals/',
                'canonical_source': 'projects/designpilot/process/reviews/external_signals/'
            },
            'downstream_artifact_receipts': {
                'meaning': 'Release receipts, handoff manifests, and generated integrity artifacts that prove what the repo produced and shipped.',
                'status': 'present' if (receipt_reports or release_reports) else 'missing',
                'artifact_count': len(receipt_reports) + len(release_reports) + len(integrity_reports),
                'canonical_source': 'proof/artifacts/'
            }
        },
        'what_the_repo_currently_demonstrates': [
            'compiled operator runtime with launcher-first startup',
            'release-gated validation and regression discipline',
            'live output scoring against real model responses when the live runner is executed',
            'internal comparative benchmarking on multiple routed task types',
            'a modest external-confidence layer with reviewer notes and one production-adjacent artifact review',
            'artifact receipts for build integrity, handoff, and release packaging'
        ],
        'what_the_repo_does_not_yet_demonstrate': [
            'blinded independent comparison results executed at scale',
            'longitudinal production outcome proof',
            'causal business impact or ROI evidence',
            'broad external review coverage across all supported task families'
        ],
        'freshness': {
            'benchmarks_last_updated': newest_timestamp(benchmark_runs + benchmark_metrics + internal_eval_specs),
            'reviews_last_updated': newest_timestamp(reviewer_confidence + production_adjacent + trust_logs),
            'receipts_last_updated': newest_timestamp(receipt_reports + release_reports + integrity_reports + handoff_files)
        }
    }

    (PROOF / 'status.json').write_text(json.dumps(layer_summary, indent=2), encoding='utf-8')

    proof_status = f'''# Proof Status

Current release line: v{version}

DesignPilot keeps proof as a layered system instead of one undifferentiated claim bucket.
That means different artifacts support different kinds of trust, and the repo must stay explicit about what each layer can and cannot prove.

## Proof layers

### 1. Internal consistency and regression proof
What it means:
- the compiled runtime, validators, schemas, and regression suite agree with each other
- known bad cases can still be rejected by the current system
- release packaging is gated by validation, regression, continuity, and integrity checks

Current evidence:
- validation reports in `dist/`
- regression fixtures in `tests/regression_suite.json`
- live output runner in `scripts/run_live_regression.py`
- release gating via `scripts/package_release.py`

What this does **not** prove:
- real-world product outcomes
- independent external superiority
- universal correctness

### 2. Comparative benchmark proof
What it means:
- the repo contains internal A/B or baseline comparisons on routed tasks using a shared rubric
- benchmark artifacts are inspectable instead of implied

Current evidence:
- {len(benchmark_runs)} benchmark run artifacts in `projects/designpilot/process/reviews/benchmarks/`
- {len(internal_eval_specs)} internal benchmark specs in `evals/internal_benchmarks/`
- {len(benchmark_metrics)} benchmark metric snapshots in `evals/metrics/`

What this currently demonstrates:
- stronger internal comparative evidence than a generic prompt-only pack
- clearer route-specific decision quality on the benchmarked tasks

What this does **not** prove:
- blinded independent wins
- broad downstream adoption success
- production KPI impact

### 3. External or blinded review proof
What it means:
- trust signals from people or processes outside the repo's internal self-scoring loop
- the repo distinguishes existing review artifacts from protocols that are only prepared for future use

Current evidence:
- {len(reviewer_confidence)} reviewer-confidence artifacts in `projects/designpilot/process/reviews/external_signals/`
- {len(production_adjacent)} production-adjacent artifact review{'s' if len(production_adjacent) != 1 else ''}
- blind-comparison protocol in `docs/proof/BLIND_COMPARISON_PROTOCOL.md`
- live comparative runner in `scripts/run_comparative.py` with storage in `tests/live_evals/`

What this currently demonstrates:
- some external confidence beyond internal benchmarking alone
- a documented path toward more serious blinded review

What this does **not** prove:
- scaled independent review coverage
- blinded comparison results already completed
- production outcome proof

### 4. Downstream artifact receipt proof
What it means:
- the repo can show what it actually compiled, validated, packaged, and handed off
- release artifacts and integrity receipts are easy to inspect

Current evidence:
- release report in `dist/release_quality_report_v{version}.json`
- handoff manifests in `HANDOFF_MANIFEST.json` and `HANDOFF_README.md`
- integrity and release receipts in `proof/artifacts/`

What this currently demonstrates:
- reproducible release packaging discipline
- inspectable build receipts and artifact manifests

What this does **not** prove:
- whether downstream teams shipped the outputs successfully
- whether users preferred the outputs in production

## What the repo currently demonstrates
- DesignPilot is a structured design operator system with route logic, contracts, proof boundaries, validation, and continuity.
- The runtime and release surfaces are now aligned enough to support a launcher-first operator workflow.
- The repo contains static validator regression, live output scoring, benchmark, review, and receipt surfaces rather than claiming trust without artifacts.

## What the repo does not yet demonstrate
- longitudinal production outcomes
- ROI or business impact attribution
- large-scale blinded external comparison results
- independent verification across every supported task type

## Where to inspect the layers
- Internal consistency and regression: `dist/`, `tests/`, `scripts/run_validation_suite.py`, `scripts/run_regression_suite.py`, `scripts/run_live_regression.py`
- Comparative benchmarks: `proof/benchmarks/README.md`
- External or blinded reviews: `proof/reviews/README.md`, `scripts/run_comparative.py`, `tests/live_evals/`
- Artifact receipts: `proof/receipts/README.md`
- Claim boundaries: `docs/proof/CLAIM_BOUNDARIES.md`
- Evidence hierarchy: `docs/proof/EVIDENCE_HIERARCHY.md`
'''
    write(PROOF / 'PROOF_STATUS.md', proof_status)

    write(PROOF / 'README.md', f'''# Proof Surface

Start with `proof/PROOF_STATUS.md`.

This folder is the evaluator-facing front door for DesignPilot's credibility surfaces.

## Main lanes
- `proof/PROOF_STATUS.md` - what each proof layer means, what the repo currently demonstrates, and what it does not
- `proof/benchmarks/README.md` - internal consistency and comparative benchmark surfaces
- `proof/reviews/README.md` - reviewer-confidence and blinded-review surfaces
- `proof/receipts/README.md` - release receipts, handoff manifests, and artifact proofs
- `docs/proof/CLAIM_BOUNDARIES.md` - language ceilings for public claims
- `docs/proof/EVIDENCE_HIERARCHY.md` - evidence classes in order
''')

    write(PROOF / 'benchmarks' / 'README.md', f'''# Benchmarks

This layer covers **internal consistency** and **comparative benchmark** proof.

## Canonical sources
- routed benchmark runs: `projects/designpilot/process/reviews/benchmarks/`
- eval specs: `evals/internal_benchmarks/`
- metric summaries: `evals/metrics/`
- regression fixtures: `tests/regression_suite.json`

## Current snapshot
- benchmark runs: {len(benchmark_runs)}
- internal benchmark specs: {len(internal_eval_specs)}
- metric snapshots: {len(benchmark_metrics)}

## Interpretation rule
Use this layer to judge whether DesignPilot is internally more disciplined and more explicit than a looser baseline on benchmarked tasks.
Do **not** use this layer alone to claim production outcomes or independent external superiority.
''')

    write(PROOF / 'reviews' / 'README.md', f'''# Reviews

This layer covers **external confidence** and the prepared path toward **blinded review**.

## Canonical sources
- reviewer-confidence artifacts: `projects/designpilot/process/reviews/external_signals/`
- mirrored evaluator-facing copies: `evals/external_reviews/`
- blind-comparison protocol: `docs/proof/BLIND_COMPARISON_PROTOCOL.md`
- MVEC placeholder: `proof/trust_notes/mvec_round_01.md`

## Current snapshot
- reviewer-confidence artifacts: {len(reviewer_confidence)}
- production-adjacent artifact reviews: {len(production_adjacent)}
- blind comparison results present: no, protocol only

## Interpretation rule
Use this layer to judge whether DesignPilot has credible outside-facing trust signals beyond internal self-scoring.
Do **not** present the blind-comparison protocol as completed evidence until blinded results actually exist.
''')

    write(PROOF / 'receipts' / 'README.md', f'''# Receipts

This layer covers **downstream artifact receipt proof**.
It shows what the repo actually compiled, validated, packaged, and handed off.

## Canonical sources
- release reports: `dist/release_quality_report_v{version}.json`
- validation suite outputs: `dist/validation_suite_report.json` and related reports in `dist/`
- integrity receipts: `proof/artifacts/`
- handoff manifests: `HANDOFF_MANIFEST.json`, `HANDOFF_README.md`
- build manifests: `dist/build_metrics.json`, `dist/manifest.json`

## Interpretation rule
Use this layer to verify what shipped and what checks passed.
Do **not** treat build receipts as proof of downstream product success.
''')

    print(json.dumps({'version': version, 'benchmark_runs': len(benchmark_runs), 'reviewer_confidence': len(reviewer_confidence), 'production_adjacent': len(production_adjacent)}, indent=2))


if __name__ == '__main__':
    main()
