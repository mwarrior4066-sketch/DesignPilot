---
summary_version: 1.1.0
source_reference:
  - src/knowledge-base/source-docs/Color Intelligence Systems for Global Production Libraries.md
  - src/knowledge-base/source-docs/Color Expert Agent Research.md
  - src/knowledge-base/source-docs/Technical Reference Framework for Pantone Systems and Production-Aware Design Operations.md
  - src/knowledge-base/source-docs/pantone_color_chart.pdf
last_updated: 2026-04-11
synchronized: true
domain: color-system
---

# Color System Summary

## Purpose
Canonical summary for **digital color systems**: semantic roles, contrast, theme behavior, domain fit, chart logic, and the boundary between UI color and print color.

## Use when
- the task involves palette design, semantic roles, APCA/WCAG checks, dark mode, data-vis palettes, status colors, or print-aware color planning

## Load order
- `src/libraries/COLOR_LIBRARY.json` then `src/libraries/COLOR_LIBRARY.md` for digital/system work
- `pantone-production-summary.md` and `src/libraries/PANTONE_LIBRARY.*` only when print awareness or Pantone matching is actually in scope

## Default rules
- assign colors by role before style: text, surface, border, action, accent, status, chart
- choose the neutral strategy before choosing the accent family
- use WCAG as the baseline and APCA when perceptual contrast meaningfully changes the decision
- separate brand-expressive colors from interface-safe colors when semantics conflict
- dark mode should use softened lights, lifted dark surfaces, and theme-aware remapping instead of simple inversion
- color must never be the only carrier of meaning
- data visualization palettes must match the data relationship: categorical, sequential, diverging, or alert

## Key thresholds
- WCAG body text: 4.5:1 minimum
- WCAG large text: 3:1 minimum
- non-text UI contrast: 3:1 minimum
- APCA: aim around Lc 75+ for body text, Lc 60+ for large or bold headings, and push higher for critical reading or tiny labels
- dark-mode long-form reading should avoid pure `#FFFFFF` on pure `#000000`

## Core production logic
### Distinct system test
A distinct system is not just a hue change. It should differ in neutral strategy, semantic role mapping, contrast posture, domain fit, or data-mapping logic.

### State intelligence
Use one explicit state model:
- value-shift
- alpha-overlay
- mutable-token remap

### Domain clusters
The pack should distinguish between:
- public sector / institutional
- enterprise SaaS / B2B
- fintech / security
- healthcare / wellness
- industrial HMI / SCADA / operations
- aviation / cockpit / glare-heavy operational
- AI / technical infrastructure
- luxury / premium
- editorial / creative
- data visualization

## Best-in-class references
- USWDS for role-based government tokens and grade-based structure
- GOV.UK for functional color discipline and maintainable system usage
- Radix Colors for 12-step scales, semantic aliasing, and neutral swapping
- Primer for semantic roles across multiple themes
- Atlassian for theme-aware tokens, alpha colors, and light/dark symmetry
- Carbon for categorical, sequential, diverging, and alert chart logic
- Material 3 for paired container and on-color roles
- Tailwind CSS v4 for OKLCH-based utility primitives

## Exceptions
- logos and decorative marks may tolerate non-body-text exceptions
- dashboards and operational tools often need more restrained and safer palettes than brand systems alone provide
- high-stakes HMI and aviation work should not be treated like ordinary web UI
- print-aware jobs should use the Pantone production summary and Pantone library rather than RGB logic alone

## Failure patterns
- mathematically compliant but perceptually weak pairs
- oversaturated accents used everywhere
- brand color forced into inaccessible or semantically conflicting roles
- too many competing accents in dense UI
- muddy neutrals with weak hierarchy
- rainbow scales used for ordered data
- state meaning carried by color alone

## Hand off to
- `src/libraries/COLOR_LIBRARY.json`, `src/libraries/COLOR_LIBRARY.md` for digital palette retrieval and domain fit
- `pantone-production-summary.md` and `src/libraries/PANTONE_LIBRARY.json`, `src/libraries/PANTONE_LIBRARY.md` when print-aware color selection, substrate choice, or process fallback matters
- `accessibility-feedback-expert.md` when the problem is state visibility, motion, or target size
- `type-system-expert.md` when contrast depends on weight or size
- `dashboard-data-expert.md` for chart and dense-data palette rules
- `pdf-layout-expert.md` or `document-accessibility-expert.md` for document-specific color constraints
