# rt_backend_feasibility

**Task:** Back-End Feasibility Review

## Route fit
- Role: governing
- Lightweight eligible: no
- Governing route or helper: governing route

## Use when
- Reveal back-end implications before treating the request as visual-only.

## Startup recommendation
- Recommended mode: profile or full
- Default contract: `dist/runtime/contracts_lite/backend_feasibility_review.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: no

## Governing skills
- `dist/runtime/skills/back-end-aware-planner.md` - Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.
- `dist/runtime/skills/front-end-handoff-expert.md` - Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.

## Optional supporting skills
- `dist/runtime/skills/component-systems-expert.md` - Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.

## Runtime summaries
- `dist/runtime/summaries/backend-planning-summary.md`
- `dist/runtime/summaries/back-end-systems-architecture-summary.md`
- `dist/runtime/summaries/api-reliability-security-summary.md`
- `dist/runtime/summaries/front-end-handoff-summary.md`
- `dist/runtime/summaries/front-end-architecture-summary.md`
- `dist/runtime/summaries/component-systems-summary.md`

## Contract shape
- Requested capability
- Hidden system requirements
- Feasibility assessment
- Safer implementation path

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_component_spec`
- Canonical routing fallback: `src/schemas/routing_registry.json`
