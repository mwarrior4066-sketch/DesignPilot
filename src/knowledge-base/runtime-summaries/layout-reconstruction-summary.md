---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/layout-reconstruction-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/Layout Reconstruction Expert Research.md
---
# Layout Reconstruction Summary Runtime Summary

## Decision rules
- in slide decks and report pages, infer not only margins and columns but also page-role architecture, header/footer contracts, and vertical fill rules
- normalize floating-card layouts by clustering internal content and recalculating card height from the content box instead of copying arbitrary heights
- preserve section-divider logic, TOC logic, and chapter wayfinding if they are part of the recovered structure
- infer the latent layout model first: margins, columns, gutters, baseline, repeated modules
- preserve the source layout when it is stable enough to extend
- normalize dirty layouts to the nearest defensible spacing rhythm rather than copying every inconsistency
- if inference is ambiguous, choose the smallest safe model and state the confidence

## Failure traps
- fake reconstruction through absolute one-off placement
- treating legacy dirt as intentional system logic
- extending a broken layout without normalizing it
- applying a generic 12-column default when the source clearly dictates a different structure

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/layout-reconstruction-summary.md`
- `src/knowledge-base/source-docs/Layout Reconstruction Expert Research.md`