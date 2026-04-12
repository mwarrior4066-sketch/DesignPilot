---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/api-reliability-security-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/API Reliability and Security Research Report.md
---
# Api Reliability Security Summary Runtime Summary

## Decision rules
- prefer RFC 9457 Problem Details for structured errors
- never trust client-supplied IDs without object-level authorization checks
- use client-generated idempotency keys plus fingerprints for retry-safe writes
- use `202 Accepted` plus a status resource or signed webhook for long-running jobs
- apply quotas, timeouts, and rate or concurrency controls to costly endpoints
- use circuit breakers, backoff with jitter, load shedding, and graceful degradation
- propagate trace identifiers across every service and tool boundary
- problem-details contract
- authorization and resource-protection model
- idempotency contract
- async job lifecycle
- resilience strategy

## Failure traps
- 200 success envelopes that hide failures
- UUID-only security theater
- mutating retries with no idempotency plan
- long-running jobs forced through synchronous request windows
- “reliable” claims with no timeout, retry, quota, or trace posture

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/api-reliability-security-summary.md`
- `src/knowledge-base/source-docs/API Reliability and Security Research Report.md`