---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/typography-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/Global Typography Intelligence Index.md
  - src/knowledge-base/source-docs/The Global Typographic Landscape of 2026.md
  - src/knowledge-base/source-docs/Comprehensive Typeface Database and Systematic Engineering Report for Design Systems.md
---
# Typography Summary Runtime Summary

## Decision rules
- body text for digital UI starts at 16px by default
- body leading defaults around 1.5x font size
- display leading tightens to about 1.1–1.25
- target 45–75 characters per line for continuous reading, with about 66 CPL as a strong default
- choose by role before taste, and by script coverage before tone when the system is multilingual
- for small text, prioritize open counters, higher x-height, and enough weight before chasing stylistic purity
- variable fonts are preferred when they reduce file overhead and increase control
- use high-level CSS controls before reaching for low-level `font-variation-settings`
- avoid pairing two fonts from the same broad category unless there is strong contrast in proportion, x-height, rhythm, width, or tone

## Failure traps
- No extracted failure traps; fall back to the canonical summary.

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/typography-summary.md`
- `src/knowledge-base/source-docs/Global Typography Intelligence Index.md`
- `src/knowledge-base/source-docs/The Global Typographic Landscape of 2026.md`
- `src/knowledge-base/source-docs/Comprehensive Typeface Database and Systematic Engineering Report for Design Systems.md`