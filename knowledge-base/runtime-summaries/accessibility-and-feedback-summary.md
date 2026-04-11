---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/accessibility-and-feedback-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/Accessibility and Feedback Expert Research.md
  - knowledge-base/source-docs/Accessible Component Behavior Deep Dive.md
---
# Accessibility And Feedback Summary Runtime Summary

## Decision rules
- native first and no ARIA is better than bad ARIA
- focus must stay visible, reachable, and restorable
- the tab sequence should expose widgets, not every internal item
- composite widgets need roving tabindex or `aria-activedescendant` logic when appropriate
- dialogs need initial focus, inert background behavior, escape, and focus return
- live regions should exist in the initial DOM and use the right politeness level
- async loading should expose `aria-busy`, status messaging, and completion behavior
- reduced-motion and touch-target rules remain implementation requirements, not optional polish

## Failure traps
- div-soup buttons and click-only controls
- focus traps or focus reset to page top
- silent loading and unannounced error changes
- hover-only disclosure logic
- label overrides that disagree with visible names
- grid, combobox, or modal behavior with no key map or focus-return rule

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/accessibility-and-feedback-summary.md`
- `knowledge-base/source-docs/Accessibility and Feedback Expert Research.md`
- `knowledge-base/source-docs/Accessible Component Behavior Deep Dive.md`