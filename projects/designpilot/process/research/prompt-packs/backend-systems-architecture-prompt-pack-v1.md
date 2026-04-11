# Back-End Systems Architecture Prompt Pack v1

## Research goal
Strengthen the backend systems architecture route with deeper evidence on authority models, consistency, pagination, eventing, and observability.

## What is already known
- ReBAC, consistency-token logic, cursor/keyset pagination, and transactional outbox are already in scope
- the route now exists and has example coverage

## What is missing
- more production-adjacent patterns for tenant isolation and event delivery at scale
- additional comparative material on consistency choices in user-facing SaaS systems

## Prompt 1
Research high-quality production guidance for choosing RBAC, ABAC, and ReBAC in collaborative multi-tenant SaaS products.

## Prompt 2
Collect decision rules for linearizable, bounded-staleness, and read-your-writes consistency in user-facing workflow and approval systems.

## Prompt 3
Find evidence-backed patterns for cursor pagination, stable ordering, and search consistency in event-heavy feeds.

## Prompt 4
Compile operational guidance on transactional outbox, webhook replay, per-key ordering, and queue-observability metrics.
