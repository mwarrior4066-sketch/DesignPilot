---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/design-token-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/AI Design Operator Pack Research.md
  - src/knowledge-base/source-docs/AI Design Operator Pack Improvement Brief.md
---
# Design Token Summary Runtime Summary

## Decision rules
- use primitive -> semantic -> component layers
- prefer flat human-readable names
- semantic aliases should shield components from raw values
- do not name tokens by value
- stateful components need stateful token or rule coverage

## Failure traps
- No extracted failure traps; fall back to the canonical summary.

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/design-token-summary.md`
- `src/knowledge-base/source-docs/AI Design Operator Pack Research.md`
- `src/knowledge-base/source-docs/AI Design Operator Pack Improvement Brief.md`