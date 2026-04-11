---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/api-reliability-security-summary.md
last_updated: 2026-04-11
synchronized: true
canonical_owner: true
domain: api-reliability-security
---

# API Reliability and Security Expert

## Purpose
Use this skill when the answer depends on structured failures, authorization perimeters, retry safety, async job lifecycles, resilience patterns, quotas, or telemetry across API and tool boundaries.

## Activate when
- the request mentions APIs, gateways, webhooks, idempotency, retries, background jobs, quotas, or security posture
- an AI or tool workflow could duplicate work, expose data, or fail opaquely without explicit operational contracts

## Do not activate when
- the task only needs broad backend feasibility or system shape without deeper failure or security semantics
- the request is only about front-end behavior

## Read these first
- `knowledge-base/summaries/api-reliability-security-summary.md`
- `knowledge-base/summaries/back-end-systems-architecture-summary.md`
- `knowledge-base/summaries/backend-planning-summary.md`

## Decision rules
- structured failure before ad hoc error strings
- authorization before identifier trust
- idempotency before retry advice
- async lifecycle before long-request optimism
- resilience before production-ready language
- quotas and timeouts before cost-blind scale claims
- trace propagation before observability claims

## Default actions
- define the problem-details contract
- name the authorization perimeter and the relevant OWASP-style failure class
- define idempotency-key ownership, fingerprinting, and mismatch behavior
- choose sync vs async lifecycle with polling or webhook status behavior
- add resilience and degraded-mode strategy
- add observability and resource-protection notes

## Exception rules
- read-only endpoints may not need idempotency, but they still need structured failure semantics if they can fail materially
- low-risk internal tools may simplify quotas, but the risk boundary must be named explicitly

## Fallback logic
- if the route lacks operational detail, fall back to a minimum safe API contract instead of generic reliability language
- if work exceeds an interactive budget, fall back to `202 Accepted` plus status tracking
- if a downstream tool is unstable, fall back to circuit breaking and cache-safe degraded modes rather than endless retries

## Failure traps
- 200-with-error-field responses
- UUID-only security theater
- retries with no deduplication contract
- long-running work forced through synchronous requests
- resilience language with no actual policy
- “secure” claims with no object-level authorization

## Evidence required
Use some combination of:
- RFC 9457 or problem-details note
- authorization rule
- idempotency contract
- async job lifecycle
- resilience pattern
- quota or timeout note
- trace and observability note

## Handoff to other skills
- hand off to `back-end-systems-architect.md` when broader system shape and consistency decisions drive the route
- hand off to `back-end-aware-planner.md` when the user first needs feasibility and scope control
- hand off to `front-end-handoff-expert.md` when errors, progress, or degraded states must be reflected safely in the UI

## Output expectations
- production-oriented operational logic
- explicit failure and recovery semantics
- no compliance theater
