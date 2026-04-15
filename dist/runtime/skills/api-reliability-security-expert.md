---
runtime_card_version: 1.0.0
canonical_skill: src/skills/api-reliability-security-expert.md
last_generated: 2026-04-11
overlay: true
---
# api-reliability-security-expert.md

## Activation conditions
- the request mentions APIs, gateways, webhooks, idempotency, retries, background jobs, quotas, or security posture
- an AI or tool workflow could duplicate work, expose data, or fail opaquely without explicit operational contracts
- the task only needs broad backend feasibility or system shape without deeper failure or security semantics
- the request is only about front-end behavior

## Non-activation conditions
- the task only needs broad backend feasibility or system shape without deeper failure or security semantics
- the request is only about front-end behavior

## Core decision rules
- structured failure before ad hoc error strings
  *(use RFC 9457 fields: type · title · status · detail - not generic error strings)*
- authorization before identifier trust
  *(use: "object-level authorization" · "BOLA check required" · "deny by default" ·
  "only the resource owner may..." · "gated by [permission check]")*
- idempotency before retry advice
  *(use: "idempotency-key header" · "409 on duplicate" · "store-and-replay" · "idempotency contract")*
- async lifecycle before long-request optimism
  *(use: "202 Accepted + status URL" · "terminal states: queued → running → completed | failed" ·
  "job lifecycle" · "polling interval" · "long-running job" · "async job model")*
- resilience before production-ready language
  *(use: "circuit breaker" · "exponential backoff with jitter" · "graceful degradation" ·
  "rate limit + quota enforcement" · "trace_id on all error responses" · "resilience strategy")*
- quotas and timeouts before cost-blind scale claims
- trace propagation before observability claims

## Required vocabulary
Name async lifecycle: `202 Accepted` · `terminal states` · `job lifecycle` · `queued → running → completed`
Name resilience posture: `circuit breaker` · `exponential backoff` · `trace_id` · `graceful degradation`
Name auth checks: `object-level authorization` · `BOLA` · `deny by default` · `authorization perimeter`

## Failure traps
- 200-with-error-field responses
- UUID-only security theater
- retries with no deduplication contract
- long-running work forced through synchronous requests
- resilience language with no actual policy
- “secure” claims with no object-level authorization

## Summary dependencies
- api-reliability-security-summary.md

## Escalation triggers
- read-only endpoints may not need idempotency, but they still need structured failure semantics if they can fail materially
- low-risk internal tools may simplify quotas, but the risk boundary must be named explicitly
- if the route lacks operational detail, fall back to a minimum safe API contract instead of generic reliability language
- if work exceeds an interactive budget, fall back to `202 Accepted` plus status tracking
- if a downstream tool is unstable, fall back to circuit breaking and cache-safe degraded modes rather than endless retries
- RFC 9457 or problem-details note
- authorization rule
- idempotency contract

## Adjacent handoff rules
- hand off to `back-end-systems-architect.md` when broader system shape and consistency decisions drive the route
- hand off to `back-end-aware-planner.md` when the user first needs feasibility and scope control
- hand off to `front-end-handoff-expert.md` when errors, progress, or degraded states must be reflected safely in the UI

## Canonical fallback
- `src/skills/api-reliability-security-expert.md`
- `src/knowledge-base/summaries/api-reliability-security-summary.md`