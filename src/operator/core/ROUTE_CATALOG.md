# Route Catalog

> Generated from `src/schemas/routing_registry.json`, example evals, and the regression suite.

This catalog explains how the pack chooses a governing route, which skills it loads in support, where route confusion usually happens, and what artifacts currently prove the route.

## Compound route policy

Choose one governing route based on the primary failure, decision burden, or risk surface. Supporting skills may widen the lens, but they must not replace the governing evidence burden.

### Selection order
- Name the user-facing failure or decision that must be solved first.
- Choose the route whose contract owns that failure.
- Load supporting skills only when they sharpen the governing route.
- Keep one evidence burden owned by the governing route.
- State why adjacent routes are support, not the main task, when the ask is compound.

### Conflict rules
| Rule ID | When it applies | Winner | Loser | Why |
|---|---|---|---|---|
| `cr_existing_layout_beats_new_grid` | The task infers or extends an existing artifact rather than creating a new scaffold. | layout reconstruction pathway | new-layout grid pathway | Preservation and inference rules matter more than fresh grid invention. |
| `cr_backend_risk_forces_support` | Permissions, exports, live data, storage, uploads, automation, or APIs appear. | rt_backend_feasibility | purely visual routes | Hidden system constraints must be exposed before UI promises harden. |
| `cr_pdf_semantics_beats_visual_cleanup` | The artifact is a PDF or document whose tags, reading order, or extraction fidelity are at risk. | rt_pdf_remediation | generic layout or styling critique | Semantic preservation outranks surface cleanup. |
| `cr_case_study_proof_beats_brand_tone` | The user is rebuilding a narrative artifact whose truthfulness depends on proof calibration. | rt_case_study_rewrite | rt_brand_positioning | Proof order and claim calibration are the governing risk. |
| `cr_dashboard_governs_accessibility_support` | A dashboard ask also contains chart readability, density, or interaction problems. | rt_dashboard_audit | standalone accessibility route | Dashboard type and KPI logic remain the governing frame; accessibility supports it. |
| `cf_frontend_architecture_over_handoff` | rendering, hydration, state ownership, or server/client boundary placement is the real issue | rt_frontend_architecture | rt_component_spec / handoff-style treatment | translation cannot replace architecture decisions |
| `cf_api_reliability_over_backend_feasibility` | RFC 9457, idempotency, retries, quotas, or async job semantics are central to the ask | rt_api_reliability_security | rt_backend_feasibility | feasibility gating does not own reliability contract detail |
| `cf_backend_architecture_over_feasibility` | multi-tenancy, consistency, pagination, eventing, or observability shape the solution itself | rt_backend_systems_architecture | rt_backend_feasibility | the route must specify system shape, not only hidden risk |

## rt_ui_structure_critique

- Task ID: `ui_structure_critique`
- Primary mode: AUDIT
- Primary phase: structure
- Loaded skills: ui-system-expert.md, grid-system-expert.md
- Fallback route: rt_case_study_rewrite

### Trigger conditions
- user asks for critique of a UI, layout, flow, or hierarchy problem
- request mentions confusion, clutter, weak hierarchy, or unclear primary action

### Preconditions
- problem artifact or description is available
- task is diagnostic rather than full build

### Selection logic
Prefer this route when the user wants structural diagnosis before polish.

### Supporting skill policy
- type-system-expert.md when hierarchy or readability is the structural bottleneck
- accessibility-feedback-expert.md when state visibility or focus behavior contributes to the failure

### Common adjacent-route confusions
- graphic styling critique when the real issue is decorative treatment, not task structure
- brand positioning when the user is actually asking who the screen is for

### Compound-task notes
- Can govern compound UI critiques when hierarchy and action clarity are the core failure.
- Should yield to rt_backend_feasibility when permissions, exports, live data, or storage constraints drive the screen.

### Example coverage
- ui-structure-critique

### Regression references
- pass-01 (smoke)
- fail-23 (fail-hollow-compliance)

### Known tensions
- density vs readability
- brand expression vs task clarity

### Exit conditions
- user receives ranked findings and a safe rebuild order

## rt_component_spec

- Task ID: `component_spec`
- Primary mode: REBUILD
- Primary phase: specs
- Loaded skills: component-systems-expert.md, front-end-handoff-expert.md
- Fallback route: rt_ui_structure_critique

### Trigger conditions
- user asks for a component spec, state matrix, anatomy, props, or implementation handoff

### Preconditions
- component scope is known or can be bounded

### Selection logic
Use when a reusable system component needs state-safe documentation.

### Supporting skill policy
- accessibility-feedback-expert.md when keyboard, focus, or motion states need explicit rules
- color-system-expert.md when semantic color roles are intrinsic to state behavior

### Common adjacent-route confusions
- UI critique that never becomes reusable component logic
- front-end implementation advice with no component governance

### Compound-task notes
- Can govern when the artifact must become a reusable system component.
- Should yield to rt_backend_feasibility when the component promise depends on permissions, exports, or system-owned data.

### Example coverage
- component-spec

### Regression references
- pass-02 (smoke)

### Known tensions
- flexibility vs implementation simplicity
- expressiveness vs token consistency

### Exit conditions
- component purpose, anatomy, states, and accessibility expectations are explicit

## rt_dashboard_audit

- Task ID: `dashboard_audit`
- Primary mode: AUDIT
- Primary phase: strategy
- Loaded skills: dashboard-data-expert.md, ui-system-expert.md
- Fallback route: rt_ui_structure_critique

### Trigger conditions
- user asks about dashboard layout, KPI order, chart choice, or density

### Preconditions
- dashboard type or usage context is known

### Selection logic
Use for KPI hierarchy and chart-logic evaluation, not generic screen cleanup.

### Supporting skill policy
- accessibility-feedback-expert.md when chart readability or focus interaction matters
- color-system-expert.md when status or series colors affect comprehension

### Common adjacent-route confusions
- generic UI cleanup that ignores dashboard type
- brand or presentation critique that never resolves KPI order

### Compound-task notes
- Govern dashboard + accessibility asks when KPI hierarchy and scan time remain central.
- Should yield to rt_backend_feasibility when live data, permissions, or export rules govern the dashboard promise.

### Example coverage
- dashboard-audit

### Regression references
- pass-03 (smoke)
- fail-01 (fail-depth)

### Known tensions
- information richness vs scan time
- executive overview vs operational drill-down

### Exit conditions
- dashboard role, failure points, and rebuild order are explicit

## rt_backend_feasibility

- Task ID: `backend_feasibility_review`
- Primary mode: PEER
- Primary phase: strategy
- Loaded skills: back-end-aware-planner.md, front-end-handoff-expert.md
- Fallback route: rt_component_spec

### Trigger conditions
- request includes sharing, permissions, exports, live data, APIs, uploads, automation, or storage

### Preconditions
- feature request implies hidden system behavior

### Selection logic
Reveal back-end implications before treating the request as visual-only.

### Supporting skill policy
- front-end-handoff-expert.md when a release-safe UI boundary must be defined
- component-systems-expert.md when the technical constraint changes reusable state coverage

### Common adjacent-route confusions
- UI critique that treats system risk as a visual issue
- product strategy writing that never maps the feature to auth, data, or storage

### Compound-task notes
- Govern compound asks whenever hidden system behavior determines what can honestly be promised.
- Often supports rt_component_spec or rt_dashboard_audit after the feasibility surface is exposed.

### Example coverage
- backend-feasibility-review

### Regression references
- pass-04 (smoke)

### Known tensions
- speed vs correctness
- frontend promise vs backend feasibility

### Exit conditions
- hidden dependencies and safer sequencing are visible

## rt_pdf_remediation

- Task ID: `pdf_remediation_plan`
- Primary mode: REBUILD
- Primary phase: implementation
- Loaded skills: document-accessibility-expert.md, pdf-layout-expert.md
- Fallback route: rt_ui_structure_critique

### Trigger conditions
- request involves fixing PDFs, tags, reading order, extraction, copy-paste, OCR, or accessibility

### Preconditions
- document file or described failure state exists

### Selection logic
Prioritize semantic preservation and verification over surface patching.

### Supporting skill policy
- layout-reconstruction-expert.md when legacy structure must be inferred safely
- color-system-expert.md when contrast or print behavior affects remediation decisions

### Common adjacent-route confusions
- visual cleanup advice that ignores tagging or reading order
- OCR-only suggestions that destroy recoverable structure

### Compound-task notes
- Govern PDF + accessibility asks when semantic integrity is at risk.
- Should not be replaced by generic layout critique once extraction or tagging is part of the failure.

### Example coverage
- pdf-remediation-plan

### Regression references
- pass-05 (compound)

### Known tensions
- visual fidelity vs semantic repair
- speed vs safe preservation

### Exit conditions
- remediation sequence and verification rules are explicit

## rt_brand_positioning

- Task ID: `brand_positioning_pass`
- Primary mode: PEER
- Primary phase: strategy
- Loaded skills: brand-strategy-expert.md, content-and-case-study-expert.md
- Fallback route: rt_case_study_rewrite

### Trigger conditions
- user asks for positioning, audience fit, tone, trust signals, or differentiation

### Preconditions
- brand question is strategic rather than purely visual

### Selection logic
Use when the system must decide who the brand is for and how it earns trust.

### Supporting skill policy
- ux-research-expert.md when audience or market evidence is thin
- content-and-case-study-expert.md when the positioning must translate into message behavior

### Common adjacent-route confusions
- case-study rewriting where proof order matters more than tone
- graphic styling advice with no audience or trust logic

### Compound-task notes
- Govern when the main decision is who the offer is for and how it earns trust.
- Should yield to rt_case_study_rewrite when the artifact is a narrative proof object rather than a strategic frame.

### Example coverage
- brand-positioning-pass

### Regression references
- pass-06 (smoke)
- fail-02 (fail-depth)

### Known tensions
- distinctiveness vs usability
- expressive tone vs credibility

### Exit conditions
- audience, frame of reference, and proof burden are explicit

## rt_case_study_rewrite

- Task ID: `case_study_rewrite`
- Primary mode: REBUILD
- Primary phase: communication
- Loaded skills: content-and-case-study-expert.md
- Fallback route: rt_brand_positioning

### Trigger conditions
- user asks to rewrite a case study, project explanation, rationale doc, or portfolio narrative

### Preconditions
- existing project material or proof state exists

### Selection logic
Use when communication quality depends on narrative order and proof clarity, not just editing.

### Supporting skill policy
- brand-strategy-expert.md when audience framing changes the case-study emphasis
- ux-research-expert.md when the proof story depends on research framing

### Common adjacent-route confusions
- brand messaging critique that never rebuilds narrative order
- portfolio polish advice that never calibrates claims to proof

### Compound-task notes
- Govern when the artifact is a case study, rationale doc, or proof-sensitive narrative.
- Can absorb brand or strategy context, but proof honesty and ordering remain the governing burden.

### Example coverage
- case-study-rewrite

### Regression references
- pass-07 (compound)
- fail-03 (fail-proof)

### Known tensions
- story flow vs proof density
- confidence vs honesty about open gaps

### Exit conditions
- problem, process, solution, and outcome are rebuilt with evidence links

## rt_accessibility_feedback_audit

- Task ID: `accessibility_feedback_audit`
- Primary mode: AUDIT
- Primary phase: accessibility
- Loaded skills: accessibility-feedback-expert.md, ui-system-expert.md
- Fallback route: rt_ui_structure_critique

### Trigger conditions
- user asks for an accessibility review, focus/keyboard audit, screen-reader behavior review, or error-state accessibility critique

### Preconditions
- the artifact or interaction pattern is known or described

### Selection logic
Use when a user task is blocked or degraded by semantic, focus, keyboard, or announcement failures.

### Supporting skill policy
- color-system-expert.md when contrast or status color rules are part of the failure
- component-systems-expert.md when the issue belongs to a reusable state pattern

### Common adjacent-route confusions
- generic usability feedback that never names semantic or keyboard failure
- color contrast comments with no behavior diagnosis

### Compound-task notes
- Govern compound UI + accessibility asks when blocked behavior is the highest-risk issue.
- Should yield to rt_pdf_remediation when the failure lives inside a PDF/document workflow.

### Example coverage
- accessibility-feedback-pass

### Regression references
- pass-08 (smoke)
- fail-04 (fail-accessibility)

### Known tensions
- strict repair vs release speed
- visual cleanliness vs semantic clarity

### Exit conditions
- blocked behaviors, repair order, and verification steps are explicit

## rt_color_system_spec

- Task ID: `color_system_spec`
- Primary mode: REBUILD
- Primary phase: tokens
- Loaded skills: color-system-expert.md, accessibility-feedback-expert.md
- Fallback route: rt_component_spec

### Trigger conditions
- user asks for a semantic color system, palette-to-token mapping, status colors, or theme-safe color roles

### Preconditions
- the artifact needs more than one-off palette advice

### Selection logic
Use when the job is to define roles, tokens, and state behavior for color rather than pick nicer hues.

### Supporting skill policy
- component-systems-expert.md when state tokens are component-owned
- brand-strategy-expert.md when brand constraints drive token tradeoffs

### Common adjacent-route confusions
- graphic styling feedback with no role model
- brand palette advice that never defines UI behavior

### Compound-task notes
- Can support accessibility or component work, but should govern when the core deliverable is a semantic color system.

### Example coverage
- color-system-pass

### Regression references
- pass-09 (smoke)
- fail-05 (fail-color)

### Known tensions
- brand expression vs semantic clarity
- vividness vs contrast safety

### Exit conditions
- semantic roles, contrast boundaries, and migration rules are explicit

## rt_graphic_critique

- Task ID: `graphic_critique`
- Primary mode: AUDIT
- Primary phase: communication
- Loaded skills: graphic-design-expert.md, type-system-expert.md
- Fallback route: rt_brand_positioning

### Trigger conditions
- user asks for a poster, campaign graphic, presentation slide, or editorial layout critique

### Preconditions
- the artifact is communication-led rather than interaction-led

### Selection logic
Use when the key problem is focal structure, type/image balance, or distance legibility.

### Supporting skill policy
- brand-strategy-expert.md when audience trust signals drive the composition
- color-system-expert.md when color hierarchy is the real structural lever

### Common adjacent-route confusions
- UI critique for interactive screens
- brand strategy advice with no compositional diagnosis

### Compound-task notes
- Govern when the artifact is primarily visual communication, not system interaction.

### Example coverage
- graphic-critique-pass

### Regression references
- pass-10 (smoke)
- fail-06 (fail-graphic)

### Known tensions
- expressiveness vs legibility
- brand tone vs message clarity

### Exit conditions
- communication goal, focal winner, and rebuild moves are explicit

## rt_layout_reconstruction_plan

- Task ID: `layout_reconstruction_plan`
- Primary mode: REBUILD
- Primary phase: implementation
- Loaded skills: layout-reconstruction-expert.md, grid-system-expert.md
- Fallback route: rt_pdf_remediation

### Trigger conditions
- user asks to rebuild or recover a layout from an existing artifact, screenshot, PDF, or legacy file

### Preconditions
- source artifact exists and preservation matters

### Selection logic
Use when structure must be inferred from an existing artifact instead of redesigned from scratch.

### Supporting skill policy
- pdf-layout-expert.md when the source is PDF-bound
- document-accessibility-expert.md when reconstruction must preserve semantics

### Common adjacent-route confusions
- new-grid design advice when preservation is required
- visual cleanup that never labels inference

### Compound-task notes
- Beats new-grid or generic layout advice whenever the user is reconstructing from a source artifact.

### Example coverage
- layout-reconstruction-pass

### Regression references
- pass-11 (compound)
- fail-07 (fail-layout)
- fail-24 (fail-visual-boundary)

### Known tensions
- exact preservation vs practical reconstruction
- speed vs verification rigor

### Exit conditions
- preservation boundaries, inference labels, and verification checkpoints are explicit

## rt_type_system_recommendation

- Task ID: `type_system_recommendation`
- Primary mode: REBUILD
- Primary phase: tokens
- Loaded skills: type-system-expert.md, accessibility-feedback-expert.md
- Fallback route: rt_ui_structure_critique

### Trigger conditions
- user asks for a type scale, typography system, reading hierarchy, or readability-driven type recommendation

### Preconditions
- reading context or artifact type is known

### Selection logic
Use when the job is to define a repeatable type system instead of suggest a single font.

### Supporting skill policy
- graphic-design-expert.md when expressive editorial hierarchy is the main concern
- ui-system-expert.md when the type system must support dense interface flows

### Common adjacent-route confusions
- graphic critique that never becomes a reusable type rule set
- brand font advice with no reading-context logic

### Compound-task notes
- Govern when live readability and role hierarchy are the primary deliverable.

### Example coverage
- type-system-pass

### Regression references
- pass-12 (smoke)
- fail-08 (fail-specificity)

### Known tensions
- brand personality vs reading efficiency
- density vs legibility

### Exit conditions
- reading context, role map, and readability rules are explicit

## rt_ux_research_gap_map

- Task ID: `ux_research_gap_map`
- Primary mode: PEER
- Primary phase: research
- Loaded skills: ux-research-expert.md, content-and-case-study-expert.md
- Fallback route: rt_brand_positioning

### Trigger conditions
- user asks what research is missing, what to validate next, or how to map evidence gaps before design decisions

### Preconditions
- project scope or audience assumption exists

### Selection logic
Use when the answer must separate known evidence from assumptions and map the next studies.

### Supporting skill policy
- brand-strategy-expert.md when audience fit is the core unknown
- content-and-case-study-expert.md when narrative proof limits must be explained

### Common adjacent-route confusions
- generic research advice that never ranks gaps
- strategy writing that pretends evidence already exists

### Compound-task notes
- Govern when the main deliverable is a ranked research gap map rather than a finished design recommendation.

### Example coverage
- ux-research-pass

### Regression references
- pass-13 (smoke)
- fail-09 (fail-research)

### Known tensions
- research depth vs team speed
- breadth of curiosity vs decision-critical unknowns

### Exit conditions
- known evidence, critical gaps, and study-to-decision links are explicit

## rt_frontend_architecture

- Task ID: `frontend_implementation_review`
- Primary mode: AUDIT
- Primary phase: implementation
- Loaded skills: front-end-architecture-expert.md, front-end-handoff-expert.md, accessibility-feedback-expert.md
- Fallback route: rt_component_spec

### Trigger conditions
- request asks for front-end architecture, rendering model, state ownership, server/client boundary, or implementation review
- screen or component is failing structurally because state, hydration, or mutation logic is weak

### Preconditions
- some product, screen, component, or architecture context is available

### Selection logic
Use when the governing decision is front-end architecture rather than generic handoff or UI critique.

### Supporting skill policy
- component-systems-expert.md when the answer must become a reusable component contract
- back-end-aware-planner.md when data, auth, or async system constraints drive the implementation

### Common adjacent-route confusions
- front-end handoff when the real issue is architecture rather than translation
- UI structure critique when the real failure is state ownership or rendering strategy

### Compound-task notes
- Can govern compound UI + implementation asks when state architecture and boundary placement are the real bottleneck.
- Should yield to rt_api_reliability_security when the core risk is API failure semantics, retries, or long-running job behavior.

### Example coverage
- adaptive-explanation-tiered-response
- frontend-implementation-review

### Regression references
- pass-14 (smoke)
- fail-10 (fail-frontend-architecture)
- pass-17 (comprehension)
- fail-17 (tier-boundary)
- fail-22 (filter-bloat)

### Known tensions
- server-first performance vs client-side flexibility
- semantic integrity vs custom-widget ambition
- optimistic speed vs rollback safety

### Exit conditions
- rendering, boundary, and state decisions are explicit and the safer implementation path is named

## rt_backend_systems_architecture

- Task ID: `backend_architecture_spec`
- Primary mode: STRUCTURE
- Primary phase: specs
- Loaded skills: back-end-systems-architect.md, back-end-aware-planner.md, api-reliability-security-expert.md
- Fallback route: rt_backend_feasibility

### Trigger conditions
- request asks for backend architecture, authority boundaries, consistency, multi-tenancy, pagination, events, or webhook design
- the answer must specify system shape rather than only feasibility

### Preconditions
- workflow, product, or system scope is known enough to model actors and resources

### Selection logic
Use when the governing decision is the structure of the backend system itself.

### Supporting skill policy
- dashboard-data-expert.md when analytics freshness or real-time reporting is central
- front-end-handoff-expert.md when the UI must expose freshness, progress, or degraded-state rules

### Common adjacent-route confusions
- backend feasibility review when the user actually needs a system spec
- API reliability review when the system shape is central and failure semantics are only one part of it

### Compound-task notes
- Can govern compound backend + dashboard + eventing asks when system shape is the main decision.
- Should yield to rt_api_reliability_security when structured errors, retries, or async job contracts are the primary failure.

### Example coverage
- backend-architecture-spec
- designer-response-filter-pass

### Regression references
- pass-15 (smoke)
- fail-11 (fail-backend-architecture)
- pass-18 (comprehension)
- fail-18 (tier-boundary)
- fail-19 (actionability)

### Known tensions
- consistency vs latency
- real-time freshness vs replayable sanity
- authority precision vs implementation complexity

### Exit conditions
- authority model, consistency stance, delivery pattern, and observability posture are explicit

## rt_api_reliability_security

- Task ID: `api_reliability_security_review`
- Primary mode: AUDIT
- Primary phase: implementation
- Loaded skills: api-reliability-security-expert.md, back-end-systems-architect.md, back-end-aware-planner.md
- Fallback route: rt_backend_systems_architecture

### Trigger conditions
- request asks for API reliability, RFC 9457, idempotency, retries, async jobs, quotas, BOLA/BFLA, or resilience
- agentic or API workflow risks duplicate work, opaque failures, or unauthorized access

### Preconditions
- api, tool, gateway, or job semantics are part of the request

### Selection logic
Use when the governing decision is failure, retry, authorization, or resilience semantics for APIs or tools.

### Supporting skill policy
- front-end-handoff-expert.md when the client must express problem details, progress, or degraded states safely
- document-accessibility-expert.md when document-export jobs create additional accessibility or extraction constraints

### Common adjacent-route confusions
- backend systems architecture when the real risk is API contract behavior
- backend feasibility review when the user actually needs explicit failure and retry semantics

### Compound-task notes
- Govern API + tool + queue asks when reliability and security semantics are the central risk.
- Should support rt_backend_systems_architecture when authority and storage architecture are primary and API behavior is downstream.

### Example coverage
- api-reliability-security-review

### Regression references
- pass-16 (smoke)
- fail-12 (fail-api-reliability)

### Known tensions
- strict safety vs fast delivery
- synchronous convenience vs retry-safe async workflows
- graceful degradation vs exact freshness

### Exit conditions
- problem-details, authorization, idempotency, async lifecycle, and resilience posture are explicit

## rt_text_humanization

- Task ID: `text_humanization_revision`
- Primary mode: REBUILD
- Primary phase: communication
- Loaded skills: text-humanization-expert.md, content-and-case-study-expert.md
- Fallback route: rt_case_study_rewrite

### Trigger conditions
- user asks to humanize, naturalize, de-mechanize, or make writing sound less AI-shaped
- prose-heavy output is structurally correct but still reads formulaically or mechanically

### Preconditions
- source prose exists

### Selection logic
Use when the governing need is prose-quality revision rather than structural rewriting or route-level diagnosis.

### Supporting skill policy
- brand-strategy-expert.md when tone must align to a named brand voice

### Common adjacent-route confusions
- case-study rewrite when the real need is prose quality only
- copy polish that changes the argument instead of the texture

### Compound-task notes
- Should support the designer response filter when prose still feels stiff after explanation shaping.
- Should not govern code, schema, or strict spec artifacts.

### Example coverage
- text-humanization-pass

### Regression references
- pass-19 (comprehension)
- fail-20 (humanization)
- fail-21 (humanization)

### Known tensions
- natural texture vs semantic drift
- voice preservation vs generic polish

### Exit conditions
- revised prose reads more authored while meaning and claims remain stable
