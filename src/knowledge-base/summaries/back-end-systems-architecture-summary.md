---
summary_version: 1.0.0
source_reference:
  - src/knowledge-base/source-docs/Back-End Systems Architecture Knowledge Base.md
last_updated: 2026-04-11
synchronized: true
domain: backend-systems-architecture
---

# Back-End Systems Architecture Summary

## Purpose
Canonical summary for deeper back-end system design decisions beyond feasibility: authority boundaries, authorization model, consistency stance, pagination, events, webhooks, multi-tenancy, and observability.

## Use when
- the feature or workflow requires a system architecture, not only a feasibility verdict
- permissions, consistency, pagination, real-time delivery, or eventing shape the product contract
- multi-tenant or global-scale behavior needs explicit rules

## Default rules
- name actors, resources, relations, and actions before proposing system shape
- object-level authorization is mandatory for client-supplied identifiers
- source-of-truth and freshness stance must be explicit
- cursor or keyset pagination should replace offset pagination once datasets grow
- event delivery should prefer outbox-driven reliability over dual writes
- near-real-time often beats fragile true real-time
- observability must expose metrics, logs, traces, and queue or replica behavior

## Key outputs
- actor/resource/action model
- authority and ownership model
- consistency and freshness stance
- delivery or event pattern
- pagination/search posture
- observability and operations note

## Failure patterns
- hidden ownership model
- role language with no object-level checks
- real-time hand waving with no replay or failure posture
- pagination with unstable ordering
- webhook systems with no outbox or ordering guarantee
- architecture claims that never name the tax they introduce

## Hand off to
- `back-end-aware-planner.md` for feasibility gating and release-safe scope reduction
- `api-reliability-security-expert.md` when failure semantics, retries, quotas, or async jobs are central
- `front-end-handoff-expert.md` when the UI must expose freshness, progress, or degraded modes correctly
