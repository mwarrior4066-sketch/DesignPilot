---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/text-humanization-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/Humanizing Writing Protocol.md
---
# Text Humanization Summary Runtime Summary

## Decision rules
- preserve meaning before voice
- repair logic before rhythm
- reduce repeated sentence frames
- prune transitions that only simulate polish
- keep the writer’s actual tone instead of replacing it

## Failure traps
- No extracted failure traps; fall back to the canonical summary.

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/text-humanization-summary.md`
- `src/knowledge-base/source-docs/Humanizing Writing Protocol.md`