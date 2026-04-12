---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/ai-to-designer-filter-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/AI-to-Designer Response Filter Report.md
---
# Ai To Designer Filter Summary Runtime Summary

## Decision rules
- the routed answer is technically correct but too dense
- the active explanation tier is Functional or Integrative
- the user needs both truth and actionability

## Failure traps
- No extracted failure traps; fall back to the canonical summary.

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/ai-to-designer-filter-summary.md`
- `src/knowledge-base/source-docs/AI-to-Designer Response Filter Report.md`