# DesignPilot-Specific Thinking and Implementation Errors

This file tracks mistakes that were specific to this project and updates them as the case study gets rebuilt.
It is not a generic design-mistakes list.
It is a running record of where DesignPilot-specific thinking, proof, and implementation drifted.

## Error 1 — the project framed the system as the proof
- Error ID: DP-ERR-001
- Classification: overclaim_error
- Context: early DesignPilot case-study framing
- What went wrong: the project treated the system document itself as if it proved the product value
- Why it happened: internal rigor was easier to produce quickly than external evidence or comparative proof
- Missing or violated rule: system description is not the same as user or outcome proof
- Fix applied: separated source-of-truth system artifacts from the case-study proof layer and claim map
- Prevention rule: keep every major claim tied to a named proof class and wording limit
- Pack-level or project-level: project-level
- Status: partially corrected

## Error 2 — evidence-first was expressed as tone rather than an evidence chain
- Error ID: DP-ERR-002
- Classification: evidence_error
- Context: case-study structure and outcome writing
- What went wrong: the writing said the pack was evidence-first before the case-study layer actually showed the full evidence chain
- Why it happened: design rationale and proof receipts were built in separate passes
- Missing or violated rule: proof-heavy claims must show their evidence class directly in the case-study layer
- Fix applied: added claim-to-proof mapping, benchmark receipts, and proof-stack summary artifacts
- Prevention rule: any proof-forward claim must name its proof class and current evidence weakness
- Pack-level or project-level: project-level
- Status: improved, not finished

## Error 3 — continuity was treated as documentation rather than synchronization
- Error ID: DP-ERR-003
- Classification: continuity_error
- Context: flagship workspace maintenance before v2.3.0
- What went wrong: roadmap and state files existed, but they could drift behind changed proof artifacts
- Why it happened: continuity was protocol-driven before it was validator-driven
- Missing or violated rule: continuity files must refresh when meaningful artifacts change
- Fix applied: added artifact freshness anchors, stored counts, refresh automation, and workspace validation
- Prevention rule: run refresh_project_continuity.py before release and after meaningful artifact changes
- Pack-level or project-level: project-level
- Status: corrected

## Error 4 — the first comparison could still feel staged
- Error ID: DP-ERR-004
- Classification: validation_error
- Context: comparative proof design
- What went wrong: the generic baseline comparison risked reading as a performance piece rather than a fair test
- Why it happened: authored comparison artifacts are easier to control than live tests
- Missing or violated rule: comparative proof must keep prompt, rubric, and interpretation limits visible
- Fix applied: kept fixed prompts, stored benchmark receipts, and recorded wording limits in the claim map
- Prevention rule: future comparisons must use visible prompts, the same rubric, and explicit interpretation limits
- Pack-level or project-level: project-level
- Status: risk reduced, still open

## Error 5 — production outcome proof is still absent
- Error ID: DP-ERR-005
- Classification: implementation_realism_error
- Context: current proof stack
- What went wrong: the project still cannot claim shipped outcome improvement or live production benefit
- Why it happened: the pack has not yet been tied to a production-adjacent implementation receipt or measured live usage
- Missing or violated rule: production claims require production receipts
- Fix applied: none yet beyond keeping the gap explicit in the roadmap and proof stack summary
- Prevention rule: do not use production-outcome language until a live artifact review or implementation receipt exists
- Pack-level or project-level: project-level
- Status: open

## Error 6 — accessibility risk was treated too much like feedback styling
- Error ID: DP-ERR-006
- Classification: evidence_error
- Context: v2.4.0 capability expansion
- What went wrong: the older accessibility layer captured feedback and state visibility well, but it under-owned focus architecture, widget interaction contracts, and async announcement behavior
- Why it happened: the route was originally proven as an audit layer before the deeper accessible interaction research was loaded into the pack
- Missing or violated rule: behavior-first accessibility needs explicit ownership of focus, key maps, overlays, and live-region timing
- Fix applied: upgraded the accessibility skill and summary with native-first, focus architecture, widget behavior, live-region, and anti-pattern logic
- Prevention rule: do not leave sequential interaction behavior implicit when accessibility is the governing route
- Pack-level or project-level: project-level
- Status: corrected


## Error 7 — comprehension behavior could have been bolted on as tone instead of system state
- Error ID: DP-ERR-007
- Classification: template_misuse_error
- Context: v2.4.2 Designer Comprehension Layer
- What went wrong: the first draft risked treating adaptive explanation and response filtering as loose style changes instead of explicit session state and runtime transformation rules
- Why it happened: prose-quality improvements are easy to frame as writing polish even when they should be controlled like system behavior
- Missing or violated rule: comprehension behavior must live in session state and response protocols, not only inside prompts or ad hoc wording choices
- Fix applied: added adaptive explanation protocol, response filter protocol, session-state fields, and a dedicated text humanization route
- Prevention rule: new cross-cutting delivery behavior must declare its state model, override logic, and validation surface before release
- Pack-level or project-level: project-level
- Status: corrected
