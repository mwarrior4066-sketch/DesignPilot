# rt_backend_systems_architecture

**Task:** Back-End Architecture Spec

## Route fit
- Role: governing
- Lightweight eligible: no
- Governing route or helper: governing route

## Use when
- Use when the governing decision is the structure of the backend system itself.

## Startup recommendation
- Recommended mode: profile or full
- Default contract: `dist/runtime/contracts_lite/backend_architecture_spec.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: no

## Governing skills
- `dist/runtime/skills/back-end-systems-architect.md` - Use this skill for deeper system-architecture work beyond feasibility: authority boundaries, authorization model, consistency stance, pagination, async events, webhooks, multi-tenancy, and observability.
- `dist/runtime/skills/back-end-aware-planner.md` - Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.
- `dist/runtime/skills/api-reliability-security-expert.md` - Use this skill when the answer depends on structured failures, authorization perimeters, retry safety, async job lifecycles, resilience patterns, quotas, or telemetry across API and tool boundaries.

## Optional supporting skills
- `dist/runtime/skills/dashboard-data-expert.md` - Use this skill to make production-level decisions about dashboard type, KPI hierarchy, chart choice, density, filters, drill-down, and dense-data readability.
- `dist/runtime/skills/front-end-handoff-expert.md` - Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.

## Runtime summaries
- `dist/runtime/summaries/back-end-systems-architecture-summary.md`
- `dist/runtime/summaries/backend-planning-summary.md`
- `dist/runtime/summaries/api-reliability-security-summary.md`
- `dist/runtime/summaries/dashboard-and-density-summary.md`
- `dist/runtime/summaries/front-end-handoff-summary.md`
- `dist/runtime/summaries/front-end-architecture-summary.md`

## Contract shape
- System framing
- Core model and authority boundaries
- Data, consistency, and delivery design
- Observability and failure posture

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_backend_feasibility`
- Canonical routing fallback: `src/schemas/routing_registry.json`
