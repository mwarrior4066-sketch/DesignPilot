---
runtime_card_version: 1.0.0
canonical_skill: src/skills/back-end-systems-architect.md
last_generated: 2026-04-11
overlay: true
---
# back-end-systems-architect.md

## Activation conditions
- the request needs a real system shape, not only a go or no-go verdict
- consistency, multi-tenancy, pagination, events, or system authority boundaries are central to the answer
- the architecture must make tradeoffs between speed, correctness, and operational complexity explicit
- the task only needs a feasibility verdict or a hidden-risk gate
- the question is purely front-end or purely visual

## Non-activation conditions
- the task only needs a feasibility verdict or a hidden-risk gate
- the question is purely front-end or purely visual

## Core decision rules
- actors, resources, relations, and actions before implementation detail
- source-of-truth before cache or replica discussion
- object-level authorization before role decoration
- consistency stance before real-time promises
- deterministic ordering before pagination claims
- outbox or replay posture before webhook optimism
- observability before production-readiness language

## Failure traps
- RBAC-only thinking where relationships govern access
- hidden tenant boundaries
- unstable pagination order
- real-time theater
- webhook delivery with no outbox or ordering model
- observability hand waving

## Summary dependencies
- back-end-systems-architecture-summary.md

## Escalation triggers
- low-risk single-tenant tools may use simpler policies if the simplification is stated explicitly
- small datasets can use offset pagination only when growth risk is low and the choice is labelled provisional
- read-heavy views may tolerate bounded staleness if the route names the safety boundary
- if the exact architecture is still fluid, fall back to a minimum safe authority model plus clear unknowns
- if real-time is overkill, fall back to polling or micro-batch freshness with explicit stale indicators
- if event delivery is risky, fall back to outbox-backed asynchronous delivery rather than inline fan-out
- actor/resource/action map
- source-of-truth note

## Adjacent handoff rules
- hand off to `back-end-aware-planner.md` when the user first needs a feasibility verdict or safer scope cut
- hand off to `api-reliability-security-expert.md` when error envelopes, idempotency, async jobs, quotas, or resilience are central
- hand off to `front-end-handoff-expert.md` when the UI contract for progress, freshness, or degraded states must be defined

## Canonical fallback
- `src/skills/back-end-systems-architect.md`
- `src/knowledge-base/summaries/back-end-systems-architecture-summary.md`