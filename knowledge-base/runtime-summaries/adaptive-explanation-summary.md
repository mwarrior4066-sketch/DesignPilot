---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/adaptive-explanation-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/Adaptive Explanation Design Report.md
---
# Adaptive Explanation Summary Runtime Summary

## Decision rules
- explanation depth is a live session variable
- use a light startup calibration first
- allow temporary local overrides
- change scaffolding without weakening constraints
- preserve critical technical terms when they carry decision weight

## Failure traps
- No extracted failure traps; fall back to the canonical summary.

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/adaptive-explanation-summary.md`
- `knowledge-base/source-docs/Adaptive Explanation Design Report.md`