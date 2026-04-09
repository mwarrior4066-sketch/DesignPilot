---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/backend-planning-summary.md
  - knowledge-base/source-docs/Back-End Aware Planner for a Modular AI Design Operator Pack.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: back-end-aware
---

# Back-End-Aware Planner

## Purpose
Use this skill as a strict feasibility control plane between product/design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes.

## Activate when
- the request implies non-public data, multi-user workflows, admin surfaces, sharing, approvals, uploads, exports, dashboards, templates, live data, or document generation
- the visual or UX decision cannot be separated from auth, source-of-truth, freshness, storage, or reliability behavior
- a “simple UI” may hide significant architectural work

## Do not activate when
- the task is purely visual, editorial, or presentational with no implementation consequences
- the answer can stay entirely at the composition, writing, or token level without data, permission, or operational implications

## Read these first
- `knowledge-base/summaries/backend-planning-summary.md`
- `knowledge-base/summaries/implementation-and-failover-summary.md`
- `knowledge-base/summaries/ux-roadmap-summary.md` when the request may be off-phase

## Decision rules
- feasibility beats fantasy
- every serious feature must resolve actors, resources, operations, permissions, and data ownership
- authorization is not optional for non-public data
- heavy work defaults to async jobs unless an interactive budget is explicitly plausible
- undefined source-of-truth, freshness, or tenant boundaries are architecture blockers, not minor details
- use MUST / SHOULD / MAY language when the constraint is structural rather than stylistic

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
- if sharing is unsafe, fall back to authenticated access or expiring signed URLs rather than “anyone with the link”
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
- hand off to `front-end-handoff-expert.md` for loading/progress/error/degraded UI and implementation-safe contracts
- hand off to `dashboard-data-expert.md` for freshness, permissions, and drill-down implications in dashboards
- hand off to `document-accessibility-expert.md` or `pdf-layout-expert.md` for exports, templates, and document workflows
- hand off to `component-systems-expert.md` when permission states or async states affect component inventories

## Output expectations
- concise but explicit technical realism
- one verdict, one rationale chain, one safest path forward
- no invented certainty
- no architecture poetry without concrete constraints
