---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/API Reliability and Security Research Report.md
last_updated: 2026-04-11
synchronized: true
domain: api-reliability-security
---

# API Reliability and Security Summary

## Purpose
Canonical summary for structured failure semantics, authorization perimeters, retry safety, async lifecycles, resilience patterns, quotas, and observability in production API and tool systems.

## Use when
- the request involves APIs, tools, gateways, background jobs, or expensive AI operations
- retry behavior, long-running work, or authorization mistakes could cause duplication or data exposure
- reliability and security claims need concrete operational contracts

## Default rules
- prefer RFC 9457 Problem Details for structured errors
- never trust client-supplied IDs without object-level authorization checks
- use client-generated idempotency keys plus fingerprints for retry-safe writes
- use `202 Accepted` plus a status resource or signed webhook for long-running jobs
- apply quotas, timeouts, and rate or concurrency controls to costly endpoints
- use circuit breakers, backoff with jitter, load shedding, and graceful degradation
- propagate trace identifiers across every service and tool boundary

## Key outputs
- problem-details contract
- authorization and resource-protection model
- idempotency contract
- async job lifecycle
- resilience strategy
- observability and trace propagation note

## Failure patterns
- 200 success envelopes that hide failures
- UUID-only security theater
- mutating retries with no idempotency plan
- long-running jobs forced through synchronous request windows
- “reliable” claims with no timeout, retry, quota, or trace posture

## Hand off to
- `back-end-systems-architect.md` for broader system structure and consistency decisions
- `back-end-aware-planner.md` for scope reduction and feasibility gating
- `front-end-handoff-expert.md` when the UI must express problem details, progress, or degraded states safely
