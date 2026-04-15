# rt_frontend_architecture

**Task:** Front-End Implementation Review

## Route fit
- Role: governing
- Lightweight eligible: no
- Governing route or helper: governing route

## Use when
- Use when the governing decision is front-end architecture rather than generic handoff or UI critique.

## Startup recommendation
- Recommended mode: profile or full
- Default contract: `dist/runtime/contracts_lite/frontend_implementation_review.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: no

## Governing skills
- `dist/runtime/skills/front-end-architecture-expert.md` - Use this skill for production-level front-end architecture decisions: rendering model, server and client boundaries, state ownership, mutation strategy, semantic structure, accessibility behavior at the system layer, and performance cost.
- `dist/runtime/skills/front-end-handoff-expert.md` - Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.
- `dist/runtime/skills/accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.

## Optional supporting skills
- `dist/runtime/skills/component-systems-expert.md` - Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.
- `dist/runtime/skills/back-end-aware-planner.md` - Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.

## Runtime summaries
- `dist/runtime/summaries/front-end-architecture-summary.md`
- `dist/runtime/summaries/front-end-handoff-summary.md`
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`
- `dist/runtime/summaries/component-systems-summary.md`
- `dist/runtime/summaries/backend-planning-summary.md`
- `dist/runtime/summaries/back-end-systems-architecture-summary.md`
- `dist/runtime/summaries/api-reliability-security-summary.md`

## Contract shape
- Architectural framing
- Boundary and state model
- Rendering and mutation strategy
- Risks and safer path

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_component_spec`
- Canonical routing fallback: `src/schemas/routing_registry.json`
