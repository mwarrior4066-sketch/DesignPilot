---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/pantone-production-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/Technical Reference Framework for Pantone Systems and Production-Aware Design Operations.md
  - knowledge-base/source-docs/pantone_color_chart.pdf
---
# Pantone Production Summary Runtime Summary

## Decision rules
- treat Pantone spot color, CMYK, RGB, and Hex as related but not interchangeable systems
- keep Pantone as the print anchor when brand-critical fidelity matters
- treat coated and uncoated targets as separate visual outcomes, not just paper finishes
- prefer Lab*-based conversion logic over static bridge numbers when print fidelity matters
- use CMYK bridge values as approximations, not guarantees
- require substrate context before making high-confidence Pantone recommendations
- metallics: keep as spot-only unless a specific packaging metallic system is supported
- neons: treat as spot-only; do not pretend CMYK or RGB can reproduce them accurately
- pastels: safer in print than neons, but still check contrast and small-type performance
- uncoated stocks mute and soften color; compensate by selecting an appropriate uncoated target, not by assuming coated behavior

## Failure traps
- picking Pantone without substrate context
- treating RGB or Hex as exact Pantone truth
- using bright yellow or lime for small text on white
- specifying metallic or neon as if process-only output can match it
- using static Bridge values without acknowledging the press/profile condition
- forcing one Pantone to act identically across coated, uncoated, digital, and PDF contexts

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/pantone-production-summary.md`
- `knowledge-base/source-docs/Technical Reference Framework for Pantone Systems and Production-Aware Design Operations.md`
- `knowledge-base/source-docs/pantone_color_chart.pdf`