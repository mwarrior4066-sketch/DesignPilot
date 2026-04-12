---
summary_version: 1.0.0
source_reference:
  - src/knowledge-base/source-docs/AI Design Operator Pack Research.md
  - src/knowledge-base/source-docs/AI Operator Pack Validation & Stress Testing.md
last_updated: 2026-04-09
synchronized: true
domain: implementation-failover
---

# Implementation and Failover Summary

## Purpose
Canonical summary for degraded modes, failure handling, retry/backoff logic, stale-data behavior, export resiliency, and implementation-safe fallbacks.

## Use when
- the request involves live data, exports, queues, async jobs, network fragility, or any feature that can partially fail
- the answer needs graceful degradation rather than all-or-nothing behavior

## Default rules
- graceful degradation beats feature collapse
- define what happens when data is stale, slow, unavailable, or partial
- heavy generation and exports should default to async work plus progress/status feedback
- polling is safer than real-time when guarantees are weak
- retries, backoff, and fallback states must not be implied silently

## Useful thresholds
- interactive requests should stay in the “feels responsive” range; heavier work needs async treatment
- if the user cannot tell whether data is current, stale-data indicators are required
- if a background task can exceed a normal user wait, use a queued/status model rather than a blocking request

## Failure patterns
- unscoped technical ambition
- live-data features without stale or degraded paths
- “instant export” promises with no queue or worker model
- retry logic assumed, not named
- export or document workflows treated as trivial

## Hand off to
- `back-end-aware-planner.md` when the risk is architectural or permission-heavy
- `front-end-handoff-expert.md` when the UI needs error, loading, progress, or degraded states
- `dashboard-data-expert.md` when freshness and stale-data behavior affect analytics surfaces
