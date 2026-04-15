---
skill_version: 1.1.0
source_reference:
  - src/knowledge-base/summaries/backend-planning-summary.md
  - src/knowledge-base/summaries/back-end-systems-architecture-summary.md
  - src/knowledge-base/summaries/api-reliability-security-summary.md
  - src/knowledge-base/source-docs/Back-End Aware Planner for DesignPilot.md
last_updated: 2026-04-11
synchronized: true
canonical_owner: true
domain: back-end-aware
---

# Back-End-Aware Planner

## Purpose
Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.

## Activate when
- the request implies non-public data, multi-user workflows, admin surfaces, sharing, approvals, uploads, exports, dashboards, templates, live data, or document generation
- the visual or UX decision cannot be separated from auth, source-of-truth, freshness, storage, or reliability behavior
- a simple UI may hide significant architectural work

## Do not activate when
- the task is purely visual, editorial, or presentational with no implementation consequences
- the answer can stay entirely at the composition, writing, or token level without data, permission, or operational implications
- the user already clearly needs a deep backend architecture or API reliability review rather than a feasibility gate

## Read these first
- `src/knowledge-base/summaries/backend-planning-summary.md`
- `src/knowledge-base/summaries/back-end-systems-architecture-summary.md`
- `src/knowledge-base/summaries/api-reliability-security-summary.md`
- `src/knowledge-base/summaries/implementation-and-failover-summary.md`
- `src/knowledge-base/summaries/ux-roadmap-summary.md` when the request may be off-phase

## Decision rules
- feasibility beats fantasy
- every serious feature must resolve actors, resources, operations, permissions, and data ownership
- authorization is not optional for non-public data
- heavy work defaults to async jobs unless an interactive budget is explicitly plausible
- undefined source-of-truth, freshness, or tenant boundaries are architecture blockers, not minor details
- escalate to deeper architecture or API reliability when the system shape itself becomes the work

## Canonical output objects
Always produce these in compact form:
- **Feasibility verdict:** `feasible`, `feasible_with_constraints`, or `not_feasible`
- **Backend implication map:** identity/auth, authorization/policy, data model/source-of-truth, API surface, storage/assets, exports/jobs, reliability/degraded modes, observability
- **Assumptions and unknowns ledger:** what is known, assumed, or still missing
- **Risk scorecard:** where the request becomes expensive, unsafe, or underspecified
- **Skill handoff payloads:** what downstream UI, dashboard, document, or front-end work must now obey

## Default actions
- parse the ask into actors, resources, actions, and relationships
- infer the access-control surface before discussing implementation detail
- name canonical entities and field ownership when persistence is implied
- classify the work as synchronous or asynchronous
- state the safest degraded mode if the ideal request is too heavy or uncertain
- separate hard blockers from manageable constraints
- route deeper system-shape questions to `back-end-systems-architect.md` or `api-reliability-security-expert.md`

## Useful thresholds
- three or more critical unknowns around actors, permissions, source-of-truth, or freshness usually drop the request below `feasible_with_constraints`
- collection APIs should assume pagination from the outset if growth is plausible
- any task likely to exceed a normal interactive wait should not stay synchronous
- cross-tenant sharing, unrestricted export, or real-time fanout raise risk immediately
- editable entities generally need timestamps, ownership, and revision awareness even in early planning

## Exception rules
- low-risk prototypes may omit deeper infrastructure detail only if the answer explicitly labels the output prototype-only and blocks later extrapolation
- single-tenant or read-only mocks may reduce auth complexity, but the simplification must be stated as a decision, not assumed silently
- polling may replace real-time when update frequency is modest and the user does not require live coordination

## Fallback logic
- if roles are unclear, fall back to a minimum safe model like owner / collaborator / viewer with deny-by-default admin behavior
- if real-time is unjustified, fall back to polling plus stale-data indicators
- if instant export is unrealistic, fall back to async jobs, queue buffering, and status/progress UI
- if sharing is unsafe, fall back to authenticated access or expiring signed URLs rather than anyone-with-the-link
- if the full data model is too early, fall back to a minimal operational model plus an audit/change log instead of bluffing completeness

## Failure traps
- assuming live data, uploads, auth, or export behavior is trivial
- recommending cross-tenant or shareable data flows with no policy model
- promising synchronous heavy generation where async work is required
- bluffing certainty when source-of-truth, freshness, or failure behavior is unknown
- treating degraded modes as optional instead of part of the product contract
- letting a visual request bypass object-level, property-level, or function-level authorization implications

## Evidence required
Use some combination of:
- feasibility verdict
- hard blocker list
- backend implication map
- assumptions and unknowns ledger
- risk note or score
- degraded-mode note
- source-of-truth or auth dependency note

## Handoff to other skills
- hand off to `back-end-systems-architect.md` for authority boundaries, consistency, pagination, events, webhooks, or multi-tenancy design
- hand off to `api-reliability-security-expert.md` for structured failures, idempotency, quotas, async jobs, or resilience posture
- hand off to `front-end-handoff-expert.md` for loading/progress/error/degraded UI and implementation-safe contracts
- hand off to `dashboard-data-expert.md` for freshness, permissions, and drill-down implications in dashboards
- hand off to `document-accessibility-expert.md` or `pdf-layout-expert.md` for exports, templates, and document workflows

## Output expectations
- concise but explicit technical realism
- one verdict, one rationale chain, one safest path forward
- no invented certainty
- no architecture poetry without concrete constraints

## Runtime summary

<!-- Auto-generated runtime overlay. Edit src/skills/back-end-aware-planner.md -- not this section. -->

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

## Required vocabulary
Express permission rules: `only [role] may` · `session owner required` · `gated by` · `deny by default` · `object-level check`
Express sequencing: `must come before` · `cannot proceed until` · `step N before step N+1` · `if you skip this` · `permissions dependency`
Express blockers: `blocking constraint` · `system surface dependency` · `this gates` · `cannot proceed without`

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
- `src/skills/back-end-aware-planner.md`
- `src/knowledge-base/summaries/backend-planning-summary.md`
- `src/knowledge-base/summaries/back-end-systems-architecture-summary.md`
- `src/knowledge-base/summaries/api-reliability-security-summary.md`
- `src/knowledge-base/summaries/Back-End Aware Planner for DesignPilot.md`
