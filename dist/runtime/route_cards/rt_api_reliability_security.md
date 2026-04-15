# rt_api_reliability_security

**Task:** API Reliability and Security Review

## Route fit
- Role: governing
- Lightweight eligible: no
- Governing route or helper: governing route

## Use when
- Use when the governing decision is failure, retry, authorization, or resilience semantics for APIs or tools.

## Startup recommendation
- Recommended mode: profile or full
- Default contract: `dist/runtime/contracts_lite/api_reliability_security_review.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: no

## Governing skills
- `dist/runtime/skills/api-reliability-security-expert.md` - Use this skill when the answer depends on structured failures, authorization perimeters, retry safety, async job lifecycles, resilience patterns, quotas, or telemetry across API and tool boundaries.
- `dist/runtime/skills/back-end-systems-architect.md` - Use this skill for deeper system-architecture work beyond feasibility: authority boundaries, authorization model, consistency stance, pagination, async events, webhooks, multi-tenancy, and observability.
- `dist/runtime/skills/back-end-aware-planner.md` - Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.

## Optional supporting skills
- `dist/runtime/skills/front-end-handoff-expert.md` - Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.
- `dist/runtime/skills/document-accessibility-expert.md` - Use this skill to preserve or restore document accessibility: tagging, reading order, artifacts, Unicode mapping, OCR remediation, and extraction fidelity.

## Runtime summaries
- `dist/runtime/summaries/api-reliability-security-summary.md`
- `dist/runtime/summaries/back-end-systems-architecture-summary.md`
- `dist/runtime/summaries/backend-planning-summary.md`
- `dist/runtime/summaries/front-end-handoff-summary.md`
- `dist/runtime/summaries/front-end-architecture-summary.md`
- `dist/runtime/summaries/pdf-document-accessibility-summary.md`

## Contract shape
- Failure semantics
- Authorization and resource protection
- Idempotency and async lifecycle
- Resilience and observability

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_backend_systems_architecture`
- Canonical routing fallback: `src/schemas/routing_registry.json`
