---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/color-and-accessibility-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/Color Intelligence Systems for Global Production Libraries.md
  - knowledge-base/source-docs/Color Expert Agent Research.md
  - knowledge-base/source-docs/Technical Reference Framework for Pantone Systems and Production-Aware Design Operations.md
  - knowledge-base/source-docs/pantone_color_chart.pdf
---
# Color And Accessibility Summary Runtime Summary

## Decision rules
- assign colors by role before style: text, surface, border, action, accent, status, chart
- choose the neutral strategy before choosing the accent family
- use WCAG as the baseline and APCA when perceptual contrast meaningfully changes the decision
- separate brand-expressive colors from interface-safe colors when semantics conflict
- dark mode should use softened lights, lifted dark surfaces, and theme-aware remapping instead of simple inversion
- color must never be the only carrier of meaning
- data visualization palettes must match the data relationship: categorical, sequential, diverging, or alert

## Failure traps
- mathematically compliant but perceptually weak pairs
- oversaturated accents used everywhere
- brand color forced into inaccessible or semantically conflicting roles
- too many competing accents in dense UI
- muddy neutrals with weak hierarchy
- rainbow scales used for ordered data
- state meaning carried by color alone

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/color-and-accessibility-summary.md`
- `knowledge-base/source-docs/Color Intelligence Systems for Global Production Libraries.md`
- `knowledge-base/source-docs/Color Expert Agent Research.md`
- `knowledge-base/source-docs/Technical Reference Framework for Pantone Systems and Production-Aware Design Operations.md`
- `knowledge-base/source-docs/pantone_color_chart.pdf`