# Proof Status

Current release line: v3.0

DesignPilot uses a tiered proof model. Each claim should point to the level of evidence that actually supports it. Structural compliance, output quality, and real designer outcomes are not the same kind of proof.

## Tier 1 - Structural compliance

What it measures:
- whether compiled runtime assets, routes, contracts, starters, launchers, examples, and validators agree with each other
- whether known pass and fail fixtures still behave as expected
- whether release and continuity files are synchronized enough to trust the bundle

Current evidence:
- `python3 scripts/run_validation_suite.py` passes all five validators: lint, lightweight path, examples, project workspace, and integrity sync
- `python3 scripts/run_regression_suite.py` passes all 45 static regression tests
- `validate_integrity_sync.py` now runs cleanly after stale path fixes and confirms the compiled runtime summary layer is present
- batch evidence cited in the v3.0 plan reports 87-88% pass-rate strength across six providers on `batch-20260415-0008`

Interpretation:
Tier 1 evidence is strong. It supports the claim that the pack is internally organized, contract-driven, and release-checkable. It does not prove real-world design outcomes.

## Tier 2 - Output quality

What it measures:
- whether outputs contain grounded recommendations instead of only matching headings
- whether recommendations include rationale, tradeoffs, evidence classes, and actionability
- whether task contracts improve decision shape across supported design and implementation routes

Current evidence:
- rubric composite scores reported for v3.0 range from 84-91% across providers
- strongest rubric grounding is in backend feasibility, backend architecture, API reliability and security, frontend implementation review, component specification, and dashboard audits
- weaker rubric grounding remains in brand, case-study, prose, and graphic critique routes because those depend more on human judgment, visual taste, and context-specific communication goals
- regression tests now prevent evidence-class credit from being earned by headings alone

Interpretation:
Tier 2 evidence supports a credible quality claim for structured outputs, especially implementation-aware tasks. It should not be described as independent superiority proof.

## Tier 3 - Designer outcome

What it would measure:
- whether designers using the pack make better product, UI, brand, or implementation decisions
- whether shipped artifacts improve usability, accessibility, engineering handoff, portfolio clarity, or production quality
- whether independent reviewers or real project teams prefer DesignPilot outputs under blinded conditions

Current evidence:
- no Tier 3 claim is made in this release
- existing reviewer and benchmark artifacts are useful signals, but they are not longitudinal outcome proof

Interpretation:
Tier 3 is intentionally open. The honest current claim is that DesignPilot improves structure and decision discipline in tested outputs, not that it has proven real-world product impact.

## Path references updated for v3.0

Older proof notes referenced live-run folders under `tests/live_outputs/live-run-2026-04-13/`. The current archived locations are:
- `tests/reports/v2-tests/single-model/live-run-v2.8-sonnet/`
- `tests/reports/v2-tests/single-model/live-run-v2.8-haiku/`

## What the repo currently demonstrates

DesignPilot is a structured design operator system with route logic, contracts, proof boundaries, validation, and continuity. The v3.0 state demonstrates clean internal validation, a passing 45-test static regression suite, and an explicit claim boundary between structural compliance, output quality, and real designer outcomes.

## What the repo does not yet demonstrate

- longitudinal production outcomes
- ROI or business-impact attribution
- scaled blinded external comparison results
- independent verification across every supported task type
- Tier 3 designer outcome proof

## Where to inspect the layers

- Structural compliance: `dist/`, `tests/`, `scripts/run_validation_suite.py`, `scripts/run_regression_suite.py`
- Output quality: `tests/evals/`, `tests/regression_suite.json`, `examples/`
- Claim boundaries: `docs/proof/CLAIM_BOUNDARIES.md`, `proof/CLAIM_TO_EVIDENCE_MAP.md`
- Artifact receipts: `proof/receipts/README.md`, `proof/artifacts/`
- Comparative and review surfaces: `proof/benchmarks/README.md`, `proof/reviews/README.md`
