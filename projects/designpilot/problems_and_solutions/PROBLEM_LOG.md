# Problem Log

## 2026-04-10 10:00 — architecture stronger than proven surface
- Error ID: DP-PROB-001
- Classification: evidence_error
- Context: pack-level credibility review during v2.2.0 planning
- Artifact(s): examples/, tests/evals/, projects/designpilot/process/reviews/
- Severity: high
- Surfaced by: merged pack critique and proof review
- What went wrong: the pack could describe rigor and routing discipline better than it could prove breadth and trustworthiness
- Why it happened: the contract and control layer matured faster than the example, benchmark, and reviewer-confidence surface
- Missing or violated rule: claimed capability breadth should be supported by examples, evals, regressions, and proof artifacts
- Fix applied: expanded direct task coverage, proof artifacts, eval realism, and regression depth in v2.2.0
- Prevention rule: do not widen the public capability surface without adding the proving bundle for the same task
- Pack-level or project-level: pack-level
- Status: fixed

## 2026-04-10 16:30 — continuity policy was ahead of enforcement
- Error ID: DP-PROB-002
- Classification: continuity_error
- Context: v2.3.0 continuity hardening
- Artifact(s): PROJECT_STATE_PROTOCOL.md, validate_project_workspace.py, refresh_project_continuity.py
- Severity: high
- Surfaced by: flagship workspace audit
- What went wrong: the workspace had continuity files, but freshness was still mostly inferred from file presence rather than artifact-backed counts and anchors
- Why it happened: the protocols described refresh behavior, but the validator was not comparing roadmap state against changed proof artifacts
- Missing or violated rule: continuity files must stay synchronized with the newest meaningful artifacts
- Fix applied: added artifact freshness anchors, stored counts, structured roadmap sections, and workspace validation against actual artifact state
- Prevention rule: any new proof artifact or stored prompt pack must trigger continuity refresh before release
- Pack-level or project-level: pack-level
- Status: fixed

## 2026-04-11 05:10 — gateway skills were carrying deeper architecture than they owned
- Error ID: DP-PROB-003
- Classification: template_misuse_error
- Context: v2.4.0 capability expansion planning
- Artifact(s): skills/front-end-handoff-expert.md, skills/back-end-aware-planner.md, skills/accessibility-feedback-expert.md
- Severity: medium
- Surfaced by: revision plan plus new architecture research
- What went wrong: gateway skills were doing more architectural and behavior-system ownership than their names and proof surface justified
- Why it happened: the pack expanded capability through broad gateway skills before it had dedicated deep architecture and API routes
- Missing or violated rule: gateway translation layers should escalate when a deeper specialist decision is the actual work
- Fix applied: added front-end architecture, backend systems architecture, and API reliability/security skills and routes; upgraded accessibility to behavior-first ownership
- Prevention rule: when a gateway skill starts carrying system-shape or reliability-contract logic, split the deep capability into its own route and proof bundle
- Pack-level or project-level: pack-level
- Status: fixed
