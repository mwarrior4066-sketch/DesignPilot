---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/Color Expert Agent Research.md
  - knowledge-base/source-docs/Technical Reference Framework for Pantone Systems and Production-Aware Design Operations.md
  - knowledge-base/source-docs/pantone_color_chart.pdf
last_updated: 2026-04-09
synchronized: true
domain: color-system
---

# Color System Summary

## Purpose
Canonical summary for palette roles, contrast, APCA/WCAG behavior, dark mode, print-aware color, and when brand color must defer to usability.

## Use when
- the task involves palette design, color roles, APCA/WCAG checks, dark mode, status colors, or print-aware color planning

## Default rules
- assign colors by role before style: text, surface, border, action, accent, status
- use WCAG as the baseline and APCA when perceptual contrast meaningfully changes the decision
- dark mode should use softened lights and lifted dark surfaces instead of pure white on pure black
- brand colors are not automatically body UI colors
- color must never be the only carrier of meaning

## Key thresholds
- WCAG body text: 4.5:1 minimum
- WCAG large text: 3:1 minimum
- non-text UI contrast: 3:1 minimum
- APCA: aim around Lc 75+ for body text, Lc 60+ for large/bold headings, higher for critical reading
- dark mode long-form reading should avoid pure #FFFFFF on pure #000000

## Exceptions
- logos and decorative marks may tolerate non-body-text exceptions
- dashboards often need more restrained and safer palettes than brand systems alone provide
- print-aware jobs should use the Pantone production summary and Pantone library rather than pure RGB logic

## Failure patterns
- mathematically compliant but perceptually weak pairs
- oversaturated accents used everywhere
- brand color forced into inaccessible roles
- too many competing accents
- muddy neutrals with weak hierarchy
- state meaning carried by color alone

## Hand off to
- `pantone-production-summary.md` and `libraries/PANTONE_LIBRARY.json`, `libraries/PANTONE_LIBRARY.md` when print-aware color selection, substrate choice, or process fallback matters
- `accessibility-feedback-expert.md` when the problem is state visibility, motion, or target size
- `type-system-expert.md` when contrast depends on weight or size
- `dashboard-data-expert.md` for chart and dense-data palette rules
- `pdf-layout-expert.md` or `document-accessibility-expert.md` for document-specific color constraints
