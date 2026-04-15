---
runtime_card_version: 1.0.0
canonical_skill: src/skills/color-system-expert.md
last_generated: 2026-04-11
overlay: true
---
# color-system-expert.md

## Activation conditions
- the task involves palettes, contrast, dark mode, APCA, WCAG, semantic roles, data-vis palette types, Pantone, state colors, or print-aware color mapping
- color affects readability, state communication, chart interpretation, or brand behavior
- the task is only about static layout skeletons with no color decisions yet
- the request is only a local text rewrite

## Non-activation conditions
- the task is only about static layout skeletons with no color decisions yet
- the request is only a local text rewrite

## Core decision rules
- build palettes by role first: text, surface, border, action, accent, status, chart categories
- choose the neutral strategy before the accent family
- readability and recognition beat brand purity
- use WCAG as the baseline and APCA when perceptual contrast materially changes the decision
- separate brand-expressive colors from interface-safe colors when semantics conflict
- dark mode should prefer softened lights and lifted darks over pure white on pure black
- use one explicit state model: value shift, alpha overlay, or mutable token remap
- choose chart palettes by data relationship: categorical, sequential, diverging, or alert
- dashboard and dense-data contexts need stricter color restraint than expressive brand systems
- use Pantone only when the job is explicitly print-aware

## Failure traps
- using color without role mapping
- mathematically compliant but perceptually weak pairs
- pure white on pure black for long dark-mode reading
- using color as the only signal for state or meaning
- treating Pantone, RGB, and CMYK as interchangeable
- choosing Pantone without coated/uncoated or substrate context
- using too many accents or chart colors in dense UI
- using rainbow scales for ordered data

## Summary dependencies
- color-and-accessibility-summary.md

## Escalation triggers
- logos or decorative brand marks may tolerate non-body-text exceptions
- dense data visualizations may require a safer and narrower palette than the brand system alone suggests
- HMI, aviation, and healthcare should not be treated as ordinary SaaS color problems
- if the source system already defines a palette, preserve roles before inventing new ones
- if a brand color fails contrast, change its role, adjust its value/saturation, or pair it with stronger neutrals
- if WCAG passes but APCA is perceptually weak, increase weight/size or adjust the pair
- if the chart palette type is wrong, fix the palette type before tuning individual swatches
- if the print color is uncertain, state the Pantone/CMYK/RGB tradeoff rather than pretending they are identical

## Adjacent handoff rules
- hand off to `type-system-expert.md` when contrast depends on weight or size
- hand off to `accessibility-feedback-expert.md` when the issue is state visibility rather than palette choice
- hand off to `dashboard-data-expert.md` for chart palette logic
- hand off to `pdf-layout-expert.md` or `document-accessibility-expert.md` when document accessibility or print fidelity matters

## Canonical fallback
- `src/skills/color-system-expert.md`
- `src/knowledge-base/summaries/color-and-accessibility-summary.md`