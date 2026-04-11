---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/backend-planning-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/Back-End Aware Planner for DesignPilot.md
  - knowledge-base/source-docs/Back-End Systems Architecture Knowledge Base.md
  - knowledge-base/source-docs/API Reliability and Security Research Report.md
---
# Backend Planning Summary Runtime Summary

## Decision rules
- resolve actors, resources, operations, permissions, and data ownership before promising a feature
- non-public data requires server-side authorization and deny-by-default admin behavior
- if source-of-truth or freshness is unclear, the request is underspecified
- heavy work should default to async paths unless an interactive budget is plausible
- hand off to deeper architecture or API reliability when system shape or reliability contracts become central

## Failure traps
- visually simple ask, architecturally expensive reality
- undefined ownership, revocation, or tenant boundaries
- synchronous fantasy for heavy generation or export
- security or reliability language with no actual contract

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/backend-planning-summary.md`
- `knowledge-base/source-docs/Back-End Aware Planner for DesignPilot.md`
- `knowledge-base/source-docs/Back-End Systems Architecture Knowledge Base.md`
- `knowledge-base/source-docs/API Reliability and Security Research Report.md`