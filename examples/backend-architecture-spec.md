# Back-End Architecture Spec Example
Fixture: tests/fixtures/backend-architecture-spec.prompt.md
Validation result: tests/evals/backend-architecture-spec.eval.json

## Input Prompt
Write a backend architecture spec for a multi-tenant scheduling platform with team workspaces, cursor-based activity feeds, approval workflows, and outbound webhooks to customer systems.

## Selected Route and Loaded Skills
- Route: `rt_backend_systems_architecture`
- Task contract: `backend_architecture_spec`
- Mode: STRUCTURE
- Phase: specs
- Skills: `back-end-systems-architect.md`, `back-end-aware-planner.md`, `api-reliability-security-expert.md`
- Known tensions: consistency vs latency, real-time freshness vs replayable sanity, authority precision vs implementation complexity

## Final Output
### System framing
The system is not only a scheduling app. It is a multi-tenant authority graph with workspace membership, approval actions, activity feeds, and external event delivery. The architecture therefore has to start with actors, resources, and actions rather than endpoint lists.

Primary actors are workspace owners, schedulers, approvers, standard members, and external subscriber systems. Primary resources are workspaces, schedules, approval requests, activity events, and webhook subscriptions. Primary actions are create, edit, approve, revoke, subscribe, and replay.

### Core model and authority boundaries
The source-of-truth should live in the primary relational store. Workspace, schedule, approval, and subscription records should all carry tenant ownership and actor attribution. Authorization should be deny by default and should not rely only on flat role checks. A ReBAC-style relation model is safer here because access depends on membership and resource relationship, not only a global role tag.

That means object-level authorization is required on every record fetch and mutation. An approver can act on an approval request only if that request belongs to a workspace where the actor has the approval relation. Property-level controls also matter. The API should not leak internal admin or billing fields just because the schedule object is otherwise visible.

### Data, consistency, and delivery design
The activity feed should use cursor or keyset pagination with stable ordering such as `created_at, id`. Offset pagination will decay under growth and can create duplicate or skipped records as inserts happen between page views. The cursor contract should be explicit so search and feed clients preserve deterministic ordering.

For approval workflows, read-your-writes or revision-token behavior is the safer consistency stance. A user who approves an item should immediately see the new state in subsequent checks, even if follower reads exist elsewhere. If relation updates and permission checks are distributed, return a revision token and pass it into subsequent checks so the system reflects the latest authority state.

Outbound webhooks should not be sent inline from the primary mutation path. Use a transactional outbox so business changes and event publication share one durable write. A relay process can then deliver webhook events with ordering guarantees per subscription key and replay support for failed deliveries.

### Observability and failure posture
Trace every approval mutation, feed query, and webhook delivery with a `trace_id`. Observe queue lag, delivery success rate, replay volume, and authorization-denial counts. The tradeoff is more operational surface area, but the system needs that tax named because multi-tenant approval and event delivery are impossible to debug credibly without it.

The simpler alternative would be flat roles, offset pagination, and inline webhook delivery. That path is faster to start but weaker on authority precision, replayability, and growth. The safer architecture is more explicit now and less fragile later.

## Why This Passed
- It defines actors, resources, and actions instead of jumping to technology.
- It names source-of-truth, authorization model, consistency stance, pagination, and webhook delivery.
- It exposes the architecture tax and observability posture.
- It keeps feasibility support subordinate to the governing architecture route.

## What Would Have Failed
- Listing tables and endpoints with no authority model.
- Calling UUIDs or roles sufficient security on their own.
- Recommending offset pagination and inline webhooks for convenience.

## Revision Pass
The weak draft described a standard CRUD backend. The corrected version turned the ask into a real architecture spec with explicit authority boundaries, consistency posture, delivery patterns, and observability requirements.
