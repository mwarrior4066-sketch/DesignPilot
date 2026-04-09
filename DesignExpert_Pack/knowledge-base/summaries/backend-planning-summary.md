---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/Back-End Aware Planner for a Modular AI Design Operator Pack.md
last_updated: 2026-04-09
synchronized: true
domain: backend-planning
---

# Backend Planning Summary

## Purpose
Canonical summary for turning product/design requests into explicit backend implications: actors, permissions, source-of-truth, APIs, storage, exports, jobs, observability, and feasibility gating.

## Use when
- the request involves non-public data, multi-user workflows, dashboards, live data, uploads, exports, document generation, or operational risk

## Default rules
- every serious request should resolve actors, resources, operations, permissions, and data ownership
- non-public data requires server-side authorization; deny by default
- collection APIs need pagination from the outset
- heavy generation, bulk updates, and exports should default to async jobs, not long blocking requests
- if freshness matters, the UI must know the freshness contract
- if source-of-truth is unknown, the feature is under-specified

## Canonical output objects
- feasibility verdict: feasible / feasible_with_constraints / not_feasible
- backend implication map: identity, authorization, data model/source-of-truth, API surface, storage/assets, exports/jobs, reliability/degraded modes, observability
- assumptions and unknowns ledger
- risk note: what makes the ask expensive, unsafe, or underspecified

## Useful thresholds
- three or more critical unknowns around roles, source-of-truth, or freshness usually drop the request below fully feasible
- cross-tenant sharing, unrestricted export, or real-time fanout raise risk immediately
- if a background task can exceed a normal user wait, use a queued/status model rather than a blocking request

## Failure patterns
- visually simple ask, architecturally heavy reality
- undefined sharing or revocation rules
- source-of-truth not named
- “real-time” requested with no update/fanout/failure model
- export or PDF generation treated as free and instant

## Hand off to
- `back-end-aware-planner.md` for verdicts and hard blockers
- `front-end-handoff-expert.md` for loading/progress/error/degraded UI
- `dashboard-data-expert.md` for freshness and permission implications in analytics
- `document-accessibility-expert.md` and `pdf-layout-expert.md` for export/document constraints
