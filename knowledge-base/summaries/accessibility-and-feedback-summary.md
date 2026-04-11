---
summary_version: 1.1.0
source_reference:
  - knowledge-base/source-docs/Accessibility and Feedback Expert Research.md
  - knowledge-base/source-docs/Accessible Component Behavior Deep Dive.md
last_updated: 2026-04-11
synchronized: true
domain: accessibility-feedback
---

# Accessibility and Feedback Summary

## Purpose
Canonical summary for behavior-first accessibility decisions around focus architecture, keyboard completeness, live announcements, dialog and widget behavior, motion safety, touch targets, and state visibility.

## Use when
- the task involves interactive UI, composite widgets, overlays, or async states
- the right answer depends on how focus moves, how screen readers are informed, or how keyboard users complete the task
- a route needs behavior contracts, not only contrast or label advice

## Default rules
- native first and no ARIA is better than bad ARIA
- focus must stay visible, reachable, and restorable
- the tab sequence should expose widgets, not every internal item
- composite widgets need roving tabindex or `aria-activedescendant` logic when appropriate
- dialogs need initial focus, inert background behavior, escape, and focus return
- live regions should exist in the initial DOM and use the right politeness level
- async loading should expose `aria-busy`, status messaging, and completion behavior
- reduced-motion and touch-target rules remain implementation requirements, not optional polish

## Key thresholds
- normal text contrast: 4.5:1 minimum
- non-text contrast: 3:1 minimum
- target size floor: 24x24 CSS px
- preferred target size: 44x44 to 48x48 CSS px
- flashes: never more than 3 per second
- latency-sensitive tabs should prefer manual activation when content switching is not instant

## Failure patterns
- div-soup buttons and click-only controls
- focus traps or focus reset to page top
- silent loading and unannounced error changes
- hover-only disclosure logic
- label overrides that disagree with visible names
- grid, combobox, or modal behavior with no key map or focus-return rule

## Hand off to
- `front-end-handoff-expert.md` for code-safe implementation detail
- `front-end-architecture-expert.md` when widget behavior and state architecture interact
- `color-system-expert.md` for contrast pairs and semantic state color
- `document-accessibility-expert.md` only when the task is document or PDF accessibility rather than UI behavior
