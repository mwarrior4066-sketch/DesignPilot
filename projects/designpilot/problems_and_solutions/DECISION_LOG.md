# Decision Log

## 2026-04-10 11:00 — separate pack-level proof from product-value proof
- Decision ID: DP-DEC-001
- Classification: overclaim_error
- Context: DesignPilot case-study proof architecture
- Options considered: keep one blended proof stack; separate internal operator proof from product-value proof
- Decision: separate internal operator proof, comparative proof, external confidence proof, and production outcome proof
- Why: the project needed proof honesty and clearer wording limits
- Files affected: PROJECT_STATE_PROTOCOL.md, PROOF_STACK_SUMMARY.md, CLAIM_TO_PROOF_MAP.md
- Validation impact: reduces unsupported-proof language and makes open gaps inspectable
- Follow-up: capture one production-adjacent validation artifact

## 2026-04-10 17:00 — gate release on pack health, not only clean file presence
- Decision ID: DP-DEC-002
- Classification: validation_error
- Context: v2.3.0 release hardening
- Options considered: keep preflight-only packaging; add pack-health metrics and promotion gates
- Decision: add pack-health metrics, continuity refresh, and promotion gates to package_release.py
- Why: a clean pack can still be thin, stale, or insufficiently proven
- Files affected: package_release.py, validate_project_workspace.py, refresh_project_continuity.py, README.md
- Validation impact: blocks release when coverage, continuity freshness, or proof counts are below threshold
- Follow-up: keep thresholds aligned with the actual direct task surface as the pack grows

## 2026-04-11 05:20 — ship the architecture expansion as v2.4.0, not another generic hardening pass
- Decision ID: DP-DEC-003
- Classification: routing_error
- Context: DesignPilot capability-growth release planning
- Options considered: keep expanding gateway skills only; add separate deep architecture and API reliability routes on the stable v2.3 base
- Decision: add separate deep skills, routes, contracts, examples, and proof artifacts for the front-end/back-end capability cluster
- Why: the stable v2.3 base already solved the generic hardening layer, so the next credible move was breadth with ownership and proof discipline
- Files affected: skills/, schemas/, templates/, examples/, tests/, projects/designpilot/
- Validation impact: wider capability surface with explicit route ownership and new benchmark coverage
- Follow-up: add more production-adjacent receipts before strengthening outcome language
