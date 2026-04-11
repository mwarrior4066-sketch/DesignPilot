# Task Router

Route automatically.
Do not ask the user which skill to use.

## Authority
Use `schemas/routing_registry.json` as the formal routing source.
Use `runtime/cards/routes/*.json` as the runtime-first route layer.
Use this file as the human-readable routing guide.
If the runtime route cards ever diverge, regenerate them from the schema.
If the schema and this file diverge, fix the schema first and regenerate the mirrors.

## Routing model
Classify every substantial task by:
- trigger
- governing route
- supporting skills
- evidence artifact
- risk flag
- task weight
- visual-input status

Use the smallest correct governing route.
Do not load a specialist skill if the ask does not need it.
Do not let supporting skills replace the governing evidence burden.
Use this runtime handoff chain by default: route card -> contract card -> required skill cards -> required runtime summaries -> validation -> escalation only if blocked.

## Load-state gate
Before routing:
1. classify the session with `DEGRADED_MODE_PROTOCOL.md`
2. stop if the session is below minimum viable bootstrap
3. continue with canonical fallback if runtime cards are missing but canonical sources are intact
4. restore session assumptions from `SESSION_CONTEXT_DEFAULTS.md` when session state is missing

## Task-weight gate
Classify each ask as:
- `lightweight` when the ask is bounded, low-risk, and answerable without full heavy scaffolding
- `standard` when normal routed behavior is appropriate
- `compound` when multiple constraints, proofs, or architecture layers must stay visible

Use `LIGHTWEIGHT_RESPONSE_PROTOCOL.md` to decide which validation and explanation layers may be skipped.

## Visual pre-pass
Run `VISUAL_INPUT_PROTOCOL.md` before route selection when the task includes:
- screenshots
- mockups
- image-based PDFs
- page images
- photos of interfaces or documents

Extract at minimum:
- layout type
- visible components
- hierarchy cues
- probable grid structure
- approximate type scale
- state cues if visible
- mismatch between user description and visible evidence
- confidence level

Then choose the governing route using both:
- user intent
- extracted visual evidence

## Compound route policy
When a task spans multiple domains:
1. identify the user-facing failure or decision that must be solved first
2. choose the route whose contract owns that failure
3. add supporting skills only when they sharpen the governing route
4. keep one evidence burden owned by the governing route
5. state a governing rule when two recommendations are in tension

### Conflict priorities
- if the task extends or infers an existing artifact, layout reconstruction beats new-grid invention
- if permissions, exports, uploads, live data, storage, automation, or APIs appear, back-end feasibility must govern or support the answer
- if rendering, hydration, state ownership, or server/client boundaries are the real failure, front-end architecture beats generic handoff
- if RFC 9457, retries, idempotency, async jobs, quotas, or resilience semantics are central, API reliability/security beats generic backend feasibility
- if multi-tenancy, consistency, pagination, events, or webhooks shape the system itself, backend systems architecture beats a narrow feasibility pass
- if the artifact is a PDF or document whose semantics are at risk, PDF/document remediation beats generic visual cleanup
- if the artifact is a case study or rationale doc whose credibility depends on proof language, case-study rewrite beats brand-tone polishing
- if a dashboard ask also includes accessibility problems, dashboard audit governs and accessibility supports

## Project workspace support
If a task clearly becomes a real project with multiple substantial artifacts, iterations, or fixes:
- load `PROJECT_FILE_SYSTEM_PROTOCOL.md` for workspace shape
- load `PROJECT_STATE_PROTOCOL.md` for roadmap and project-specific error continuity
- load `PROJECT_PORTABLE_WORKSPACE_PROTOCOL.md` only when filesystem access is unavailable
- load `PROJECT_LOGGING_PROTOCOL.md` when meaningful problems, fixes, or decisions should be preserved

## Research prompt support
If the user asks for research, research gaps, or a deep-search handoff:
- first determine whether direct research synthesis is needed, or whether the user wants reusable deep-research prompts
- ask if they want deep-research prompts before generating them
- cap prompt packs at 4 prompts maximum
- if the research is part of a longer-running project, store the prompt pack in the project workspace

## Designer comprehension layer
This layer sits on top of the existing route system.
It does not replace route selection.

Use it to control:
- explanation depth
- jargon handling
- contextual framing
- next-step guidance
- prose humanization when needed

### Activation rules
- if the user’s explanation preference is unknown and the task becomes substantial, calibrate using `ADAPTIVE_EXPLANATION_PROTOCOL.md`
- if the answer is technically dense, run the designer response filter before final validation
- if the output is prose-heavy and clearly machine-shaped, route or support with `rt_text_humanization`
- do not use humanization to rewrite code, schemas, or strict spec artifacts

## Primary pathways
Use the schema and route cards as the authoritative per-route map.
This mirror exists to explain the routing posture, not to duplicate every route definition.

### Key reminders
- UI structure critique governs layout and hierarchy failures before polish
- Dashboard audit governs KPI order, scan cost, and data density
- Layout reconstruction governs extension or recovery of an existing artifact
- Back-end feasibility governs hidden system implications before visual promises are locked
- PDF remediation governs when semantics, extraction, or reading order are at risk
- Case-study rewrite governs proof-sensitive writing where credibility matters more than tone polish
