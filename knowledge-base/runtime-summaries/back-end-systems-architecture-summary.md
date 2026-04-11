---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/back-end-systems-architecture-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/Back-End Systems Architecture Knowledge Base.md
---
# Back End Systems Architecture Summary Runtime Summary

## Decision rules
- name actors, resources, relations, and actions before proposing system shape
- object-level authorization is mandatory for client-supplied identifiers
- source-of-truth and freshness stance must be explicit
- cursor or keyset pagination should replace offset pagination once datasets grow
- event delivery should prefer outbox-driven reliability over dual writes
- near-real-time often beats fragile true real-time
- observability must expose metrics, logs, traces, and queue or replica behavior
- actor/resource/action model
- authority and ownership model
- consistency and freshness stance
- delivery or event pattern
- pagination/search posture

## Failure traps
- hidden ownership model
- role language with no object-level checks
- real-time hand waving with no replay or failure posture
- pagination with unstable ordering
- webhook systems with no outbox or ordering guarantee
- architecture claims that never name the tax they introduce

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/back-end-systems-architecture-summary.md`
- `knowledge-base/source-docs/Back-End Systems Architecture Knowledge Base.md`