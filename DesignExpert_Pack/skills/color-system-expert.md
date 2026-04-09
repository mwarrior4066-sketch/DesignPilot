---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/color-and-accessibility-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: color-system
---

# Color System Expert

## Purpose
Use this skill to build or evaluate palettes by role, contrast, dark-mode behavior, dashboard safety, and print-awareness.

## Activate when
- the task involves palettes, contrast, dark mode, APCA, WCAG, Pantone, state colors, or print-aware color mapping
- color affects readability, state communication, or brand behavior

## Do not activate when
- the task is only about static layout skeletons with no color decisions yet
- the request is only a local text rewrite

## Read these first
- `knowledge-base/summaries/color-and-accessibility-summary.md`
- `knowledge-base/summaries/pantone-production-summary.md` when print-aware
- `libraries/PANTONE_LIBRARY.json`, `libraries/PANTONE_LIBRARY.md` when print-aware

## Decision rules
- build palettes by role first: text, surface, border, action, accent, status, chart categories
- readability and recognition beat “brand purity”
- use WCAG as the baseline and APCA when perceptual contrast materially changes the decision
- dark mode should prefer softened lights and lifted darks over pure white on pure black
- color must not be the only carrier of meaning
- dashboard and dense-data contexts need stricter color restraint than expressive brand systems

## Default actions
- define role mapping before proposing swatches
- check body-text and non-text contrast
- check dark-mode transformation logic when a mode switch exists
- separate brand colors from interface colors when needed
- reserve the highest-saturation color for actions, alerts, or the strongest emphasis
- use Pantone only when the job is explicitly print-aware
- require substrate and process context before making high-confidence Pantone claims

## Exception rules
- logos or decorative brand marks may tolerate non-body-text exceptions
- dense data visualizations may require a safer and narrower palette than the brand system alone suggests
- if the source system already defines a palette, preserve roles before inventing new ones

## Fallback logic
- if a brand color fails contrast, change its role, adjust its value/saturation, or pair it with stronger neutrals
- if WCAG passes but APCA is perceptually weak, increase weight/size or adjust the pair
- if the print color is uncertain, state the Pantone/CMYK/RGB tradeoff rather than pretending they are identical
- if spot-to-process mismatch risk is high, recommend ECG, Lab*-based conversion, or a process-safer nearby Pantone

## Failure traps
- using color without role mapping
- mathematically compliant but perceptually weak pairs
- pure white on pure black for long dark-mode reading
- using color as the only signal for state or meaning
- treating Pantone, RGB, and CMYK as interchangeable
- choosing Pantone without coated/uncoated or substrate context
- using too many accents or chart colors in dense UI

## Evidence required
Use some combination of:
- role map
- WCAG threshold
- APCA threshold when relevant
- non-text contrast rule
- dark-mode rule
- dashboard color rule when relevant
- print/Pantone note when relevant
- substrate/process note when relevant

## Handoff to other skills
- hand off to `type-system-expert.md` when contrast depends on weight or size
- hand off to `accessibility-feedback-expert.md` when the issue is state visibility rather than palette choice
- hand off to `dashboard-data-expert.md` for chart palette logic
- hand off to `pdf-layout-expert.md` or `document-accessibility-expert.md` when document accessibility or print fidelity matters

## Output expectations
- color by role, not by taste
- readable defaults
- explicit fallback when brand color and accessibility conflict
