---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/front-end-handoff-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/Front-End Handoff Expert Research.md
  - src/knowledge-base/source-docs/Front-End Architecture Expert Knowledge Base.md
---
# Front End Handoff Summary Runtime Summary

## Decision rules
- preserve semantics before styling
- preserve tokens before hard-coded values
- define component boundaries before page-wide hacks
- preserve required states, accessibility behavior, and reduced-motion logic
- keep font deployment, fallbacks, and loading safe for the actual medium
- surface when the problem has crossed from handoff into deeper front-end architecture
- component boundary
- token and state map
- semantic and accessibility notes
- mutation/loading/error UI contract
- font loading or fallback logic
- escalation note when architecture risk appears

## Failure traps
- code translation that loses the original system logic
- token drift
- missing states or degraded paths
- implementation detail that ignores semantics
- handoff advice pretending to solve rendering or state architecture questions it does not own

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/front-end-handoff-summary.md`
- `src/knowledge-base/source-docs/Front-End Handoff Expert Research.md`
- `src/knowledge-base/source-docs/Front-End Architecture Expert Knowledge Base.md`