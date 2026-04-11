---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/back-end-systems-architecture-summary.md
last_updated: 2026-04-11
synchronized: true
canonical_owner: true
domain: backend-systems-architecture
---

# Back-End Systems Architect

## Purpose
Use this skill for deeper system-architecture work beyond feasibility: authority boundaries, authorization model, consistency stance, pagination, async events, webhooks, multi-tenancy, and observability.

## Activate when
- the request needs a real system shape, not only a go or no-go verdict
- consistency, multi-tenancy, pagination, events, or system authority boundaries are central to the answer
- the architecture must make tradeoffs between speed, correctness, and operational complexity explicit

## Do not activate when
- the task only needs a feasibility verdict or a hidden-risk gate
- the question is purely front-end or purely visual

## Read these first
- `knowledge-base/summaries/back-end-systems-architecture-summary.md`
- `knowledge-base/summaries/backend-planning-summary.md`
- `knowledge-base/summaries/api-reliability-security-summary.md`

## Decision rules
- actors, resources, relations, and actions before implementation detail
- source-of-truth before cache or replica discussion
- object-level authorization before role decoration
- consistency stance before real-time promises
- deterministic ordering before pagination claims
- outbox or replay posture before webhook optimism
- observability before production-readiness language

## Default actions
- define the actor/resource/action model
- choose the authority and authorization model
- state the consistency or freshness contract
- choose delivery patterns for queries, events, or webhooks
- define pagination and search consistency rules
- add observability and operational tax notes

## Exception rules
- low-risk single-tenant tools may use simpler policies if the simplification is stated explicitly
- small datasets can use offset pagination only when growth risk is low and the choice is labelled provisional
- read-heavy views may tolerate bounded staleness if the route names the safety boundary

## Fallback logic
- if the exact architecture is still fluid, fall back to a minimum safe authority model plus clear unknowns
- if real-time is overkill, fall back to polling or micro-batch freshness with explicit stale indicators
- if event delivery is risky, fall back to outbox-backed asynchronous delivery rather than inline fan-out

## Failure traps
- RBAC-only thinking where relationships govern access
- hidden tenant boundaries
- unstable pagination order
- real-time theater
- webhook delivery with no outbox or ordering model
- observability hand waving

## Evidence required
Use some combination of:
- actor/resource/action map
- source-of-truth note
- authorization model
- consistency or freshness stance
- delivery pattern
- observability note

## Handoff to other skills
- hand off to `back-end-aware-planner.md` when the user first needs a feasibility verdict or safer scope cut
- hand off to `api-reliability-security-expert.md` when error envelopes, idempotency, async jobs, quotas, or resilience are central
- hand off to `front-end-handoff-expert.md` when the UI contract for progress, freshness, or degraded states must be defined

## Output expectations
- system-architecture specific
- explicit authority and consistency language
- no fake simplicity
