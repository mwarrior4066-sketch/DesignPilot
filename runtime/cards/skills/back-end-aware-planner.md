---
runtime_card_version: 1.0.0
canonical_skill: skills/back-end-aware-planner.md
last_generated: 2026-04-11
overlay: true
---
# back-end-aware-planner.md

## Activation conditions
- the request implies non-public data, multi-user workflows, admin surfaces, sharing, approvals, uploads, exports, dashboards, templates, live data, or document generation
- the visual or UX decision cannot be separated from auth, source-of-truth, freshness, storage, or reliability behavior
- a simple UI may hide significant architectural work
- the task is purely visual, editorial, or presentational with no implementation consequences
- the answer can stay entirely at the composition, writing, or token level without data, permission, or operational implications
- the user already clearly needs a deep backend architecture or API reliability review rather than a feasibility gate

## Non-activation conditions
- the task is purely visual, editorial, or presentational with no implementation consequences
- the answer can stay entirely at the composition, writing, or token level without data, permission, or operational implications
- the user already clearly needs a deep backend architecture or API reliability review rather than a feasibility gate

## Core decision rules
- feasibility beats fantasy
- every serious feature must resolve actors, resources, operations, permissions, and data ownership
- authorization is not optional for non-public data
- heavy work defaults to async jobs unless an interactive budget is explicitly plausible
- undefined source-of-truth, freshness, or tenant boundaries are architecture blockers, not minor details
- escalate to deeper architecture or API reliability when the system shape itself becomes the work

## Failure traps
- assuming live data, uploads, auth, or export behavior is trivial
- recommending cross-tenant or shareable data flows with no policy model
- promising synchronous heavy generation where async work is required
- bluffing certainty when source-of-truth, freshness, or failure behavior is unknown
- treating degraded modes as optional instead of part of the product contract
- letting a visual request bypass object-level, property-level, or function-level authorization implications

## Summary dependencies
- backend-planning-summary.md
- back-end-systems-architecture-summary.md
- api-reliability-security-summary.md
- Back-End Aware Planner for DesignPilot.md

## Escalation triggers
- low-risk prototypes may omit deeper infrastructure detail only if the answer explicitly labels the output prototype-only and blocks later extrapolation
- single-tenant or read-only mocks may reduce auth complexity, but the simplification must be stated as a decision, not assumed silently
- polling may replace real-time when update frequency is modest and the user does not require live coordination
- if roles are unclear, fall back to a minimum safe model like owner / collaborator / viewer with deny-by-default admin behavior
- if real-time is unjustified, fall back to polling plus stale-data indicators
- if instant export is unrealistic, fall back to async jobs, queue buffering, and status/progress UI
- if sharing is unsafe, fall back to authenticated access or expiring signed URLs rather than anyone-with-the-link
- if the full data model is too early, fall back to a minimal operational model plus an audit/change log instead of bluffing completeness

## Adjacent handoff rules
- hand off to `back-end-systems-architect.md` for authority boundaries, consistency, pagination, events, webhooks, or multi-tenancy design
- hand off to `api-reliability-security-expert.md` for structured failures, idempotency, quotas, async jobs, or resilience posture
- hand off to `front-end-handoff-expert.md` for loading/progress/error/degraded UI and implementation-safe contracts
- hand off to `dashboard-data-expert.md` for freshness, permissions, and drill-down implications in dashboards
- hand off to `document-accessibility-expert.md` or `pdf-layout-expert.md` for exports, templates, and document workflows

## Canonical fallback
- `skills/back-end-aware-planner.md`
- `knowledge-base/summaries/backend-planning-summary.md`
- `knowledge-base/summaries/back-end-systems-architecture-summary.md`
- `knowledge-base/summaries/api-reliability-security-summary.md`
- `knowledge-base/summaries/Back-End Aware Planner for DesignPilot.md`