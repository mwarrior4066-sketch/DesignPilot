# Runtime Validation Layer

> Generated from `schemas/validation_rules.json` and implemented by `runtime_validator.py`.

The runtime validator is the executable rulebook for the pack. Global structure checks fire first, task-contract checks fire second, route-specific semantic checks fire third, and integrity checks fire last. This is meant to block outputs that are polished, dense, or specific-sounding but still weak.

## Hard Rules

| Rule ID | Applies to | Failure trigger | Human remediation |
|---|---|---|---|
| `hr_accessibility_floor` | ui_structure_critique, dashboard_audit, component_spec, pdf_remediation_plan, frontend_implementation_review, accessibility_feedback_audit | Response recommends unreadable text, inaccessible color, missing keyboard coverage, or destructive PDF repair as the primary solution. | Replace with a structurally safe alternative and name the violated floor. |
| `hr_wrong_mode` | all | Audit requested but answer rebuilds only, or rebuild requested but answer diagnoses only. | Reroute and regenerate under the correct mode. |
| `hr_unsupported_superlative` | all | Uses validated, proven, certified, best-in-class, compliant, or similar proof language without the required evidence class. | Either add evidence or downgrade the claim to hypothesis language. |
| `hr_missing_route_decision` | all | The output omits one of the route-specific decisions that the task contract says must be made. | Add the missing governing decision instead of broadening the response. |
| `hr_continuity_stale` | project_bundle | Roadmap or project-specific errors file is stale compared with project artifacts. | Refresh roadmap and error log before export. |
| `hr_below_minimum_viable_load` | all | Required startup or canonical routing authority is missing and the system continues as if fully hydrated. | Stop routing and request reload or the missing files. |

## Semantic Rules

| Rule ID | Applies to | Failure trigger | Human remediation |
|---|---|---|---|
| `sr_information_density` | all | Required headings exist but section substance or information density falls below contract threshold. | Add decisions, thresholds, rationale, and evidence. |
| `sr_prompt_restatement` | all | Output mostly repeats the prompt with minimal transformation or decision-making. | Force explicit recommendations, tradeoffs, or routed constraints. |
| `sr_tradeoff_visibility` | ui_structure_critique, dashboard_audit, backend_feasibility_review, pdf_remediation_plan, brand_positioning_pass, case_study_rewrite, frontend_implementation_review, backend_architecture_spec, api_reliability_security_review, accessibility_feedback_audit | Recommendation picks a direction without naming what is preserved, sacrificed, or constrained. | Add one tradeoff node and ranked intervention order. |
| `sr_typed_evidence_coverage` | all | The output names proof or certainty but does not cover the evidence classes required by the contract. | Add the missing evidence class instead of repeating generic proof language. |
| `sr_false_specificity` | all | The output introduces thresholds, scores, or precise-seeming numbers without a source, standard, receipt, or explicit inference label. | Tie the number to a standard, artifact, or clearly label it as an assumption or inference. |
| `sr_route_bleed` | all | The output drifts into styling, brand, or implementation language without satisfying the governing route decisions. | Bring the answer back to the governing route and keep adjacent domains in support only. |
| `sr_frontend_boundary_visibility` | frontend_implementation_review | The answer discusses implementation but never chooses rendering, state ownership, or server/client boundary posture. | Add the missing architecture choice before offering framework tips. |
| `sr_backend_authority_visibility` | backend_architecture_spec | The answer names technologies or endpoints without making authority, source-of-truth, and consistency posture explicit. | Add the authority model, consistency stance, and delivery pattern. |
| `sr_api_contract_visibility` | api_reliability_security_review | The answer talks about reliability or security without naming problem details, idempotency, or async lifecycle behavior. | Define the explicit API contract rather than generic best practices. |
| `sr_tier_compliance` | all | Functional outputs use dense unexplained jargon, Integrative outputs hide cross-functional rationale, or Strategic outputs overexplain obvious material. | Re-shape the explanation surface using the active tier without changing route ownership. |
| `sr_missing_next_step_guidance` | all | The answer explains the issue but never directs the user toward the next practical move when the tier expects guidance. | Add the next useful move at the right depth for the active tier. |
| `sr_filter_faithfulness` | all | The answer becomes easier to read by removing constraints, implementation realism, or proof boundaries that still matter. | Restore the hidden constraint and re-filter the wording instead of simplifying the substance. |
| `sr_meaning_guard_visibility` | text_humanization_revision | The rewrite claims to sound more human but never states what meaning, claims, or voice boundaries were preserved. | Add an explicit meaning-preservation guard and drift-risk note before presenting the revision. |
| `sr_hollow_compliance` | all | Recommendations do not map back to named failures, or tradeoff language is decorative rather than real. | Reconnect each recommendation to a named problem and state the real gain and sacrifice. |
| `sr_visual_boundary_honesty` | ui_structure_critique, dashboard_audit, layout_reconstruction_plan, pdf_remediation_plan, graphic_critique, accessibility_feedback_audit | The answer implies certainty about unseen interaction, semantics, or structure from a static visual artifact alone. | Downgrade the claim to observation, inference, or unknown and state confidence. |

## Integrity Rules

| Rule ID | Applies to | Failure trigger | Human remediation |
|---|---|---|---|
| `ir_contradiction` | all | Output carries mutually exclusive recommendations forward without deciding which wins. | Resolve the conflict and state the governing rule. |
| `ir_route_traceability` | all | Task type, phase, route, or loaded skills are hidden in a way that makes debugging difficult. | Expose route metadata in the visible header block or route section. |
| `ir_release_gate` | release | Examples, mirrors, source registry, or benchmark coverage are incomplete. | Fix blockers before packaging. |

## Validator order of operations

1. required sections and density
2. tradeoff, rationale, and alternative coverage
3. required task decisions
4. required evidence-class coverage
5. forbidden shortcuts and overclaim patterns
6. unsupported specificity and contradiction checks
7. route traceability and release integrity checks

## Failure exception report
| Failure family | Typical signal | First recovery move |
|---|---|---|
| Missing route decision | The answer sounds thoughtful but never makes the route-owning call | Add the missing governing decision instead of adding more polish |
| Typed evidence gap | The answer says “proof” or sounds certain without the required evidence class | Name the missing evidence class and add the receipt or rule |
| Unsupported specificity | Precise numbers appear without standards, artifacts, or inference labels | Tie the number to a standard, artifact, or explicit assumption |
| Route bleed | Styling, brand, or implementation language overtakes the governing task | Pull the answer back to the route that owns the failure |
| Stale continuity | Roadmap or error log older than the changed artifacts | Refresh project continuity before export |
