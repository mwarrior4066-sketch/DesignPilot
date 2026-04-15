# Claim to Evidence Map

Current release line: v3.0.

This map keeps public claims tied to the strongest evidence that currently supports them. It should be updated whenever README, HOWTO, proof language, or validation claims change.

| Public claim | Evidence tier | Strongest supporting artifact | Weakest link | What would upgrade it |
|---|---:|---|---|---|
| DesignPilot is a modular AI design operator for structured design work. | Tier 1 | `dist/runtime/START_HERE.md`, `dist/runtime/TASK_CHOOSER.md`, runtime route and contract cards | Structure exists, but structure alone is not outcome quality | Independent use on real briefs with retained project decisions |
| It routes different design jobs through different decision layers. | Tier 1 | `src/schemas/routing_registry.json`, `src/schemas/task_contracts.json`, `dist/runtime/task_launchers/` | Routing quality is inferred from schema coverage | Human review comparing route choice against expert task triage |
| It improves structural clarity and resistance to generic filler. | Tier 2 | `tests/regression_suite.json`, `examples/`, `tests/evals/` | Static fixtures are partly tuned to the validator | Blinded comparison against unpacked prompts on unseen briefs |
| It is implementation-aware for front-end, back-end, API, component, and dashboard tasks. | Tier 2 | `examples/backend-feasibility-review.md`, `examples/frontend-implementation-review.md`, `examples/api-reliability-security-review.md`, `examples/component-spec.md` | Some evaluation is still model-mediated and fixture-based | Real engineering handoff review with accepted and rejected recommendations |
| It improves brand, graphic, prose, and case-study work through stronger rationale and claim discipline. | Tier 2 | `examples/brand-positioning-pass.md`, `examples/graphic-critique-pass.md`, `examples/case-study-rewrite.md`, `examples/text-humanization-pass.md` | These routes are more judgment-dependent and harder to validate by regex | Human rubric review from multiple design reviewers |
| The pack is release-checkable and internally validated. | Tier 1 | `scripts/run_validation_suite.py`, `dist/validation_suite_report.json`, `scripts/run_regression_suite.py` | Passing validators only prove internal consistency | Public CI run or third-party reproduction from a clean checkout |
| The proof layer distinguishes validation from outcome proof. | Tier 1 | `proof/PROOF_STATUS.md`, `docs/proof/CLAIM_BOUNDARIES.md` | The distinction is documented, not externally audited | External review confirming public claims stay within evidence limits |
| DesignPilot has not proven real-world designer outcome impact yet. | Tier 3 open | `proof/PROOF_STATUS.md`, this file | This is an absence-of-proof statement, not a metric | Longitudinal project receipts, user studies, or production artifact reviews |
