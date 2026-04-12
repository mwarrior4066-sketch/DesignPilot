---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/architecture-optimization-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/Architectural Optimization and Structural Synthesis of DesignPilot v8.1 Operator Pack.md
---
# Architecture Optimization Summary Runtime Summary

## Decision rules
- Startup should load only `MASTER_CHAT_OPERATOR.md`, `TASK_ROUTER.md`, and `SESSION_CONTEXT.md`.
- Skills, summaries, and templates should hydrate on demand.
- `README.md` is for humans; `CHAT_BOOTSTRAP_PROMPT.md` is for the runtime entry point.
- The knowledge base needs explicit ownership and readiness rules.
- Skills and summaries need a synchronization protocol when source logic changes.

## Failure traps
- No extracted failure traps; fall back to the canonical summary.

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/architecture-optimization-summary.md`
- `src/knowledge-base/source-docs/Architectural Optimization and Structural Synthesis of DesignPilot v8.1 Operator Pack.md`