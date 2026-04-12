---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/dashboard-and-density-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/Dashboard Expert Research.md
---
# Dashboard And Density Summary Runtime Summary

## Decision rules
- every metric should map to a real decision or action
- keep the summary plane decision-oriented, not exhaustive
- top-left carries the most critical KPI/status information
- use bar charts for categorical comparison, line charts for time series, and simple numeric KPI blocks for single top metrics
- use drill-down and progressive disclosure instead of packing everything into one plane

## Failure traps
- graveyard of KPIs
- decorative chart junk
- wrong chart for the data type
- filters with no mental model
- no drill-down path
- empty states that explain nothing
- dashboard looks minimal but hides essential decisions

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/dashboard-and-density-summary.md`
- `src/knowledge-base/source-docs/Dashboard Expert Research.md`