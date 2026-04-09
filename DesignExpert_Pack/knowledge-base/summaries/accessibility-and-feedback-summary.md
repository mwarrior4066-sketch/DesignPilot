---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/Accessibility and Feedback Expert Research.md
last_updated: 2026-04-09
synchronized: true
domain: accessibility-feedback
---

# Accessibility and Feedback Summary

## Purpose
Canonical summary for interaction states, focus visibility, keyboard behavior, hover/focus content, touch targets, reduced motion, and feedback messaging.

## Use when
- the task involves interactive UI
- state visibility, focus, motion, hover/focus behavior, or target sizing matter
- a component or interface must remain accessible under real interaction

## Default rules
- every interactive control needs a clear rest/default state plus focus, active, disabled, and other relevant states
- focus indicators must remain visible and must not be removed without a compliant replacement
- keyboard order should follow visible logic
- hover-only behavior is not enough; focus and touch paths must still work
- honor reduced motion and keep flashes below seizure-risk thresholds
- touch targets should prefer 44x44 or 48x48 size guidance even when the minimum legal threshold is lower

## Key thresholds
- normal text contrast: 4.5:1 minimum
- large text contrast: 3:1 minimum
- non-text contrast for focus indicators and key UI parts: 3:1 minimum
- WCAG 2.2 target size minimum: 24x24 CSS px absolute floor
- preferred touch targets: 44x44 to 48x48
- hover/focus persistence buffer for menus/tooltips: roughly 150 to 300 ms
- flashes: never more than 3 per second
- focus indicator must remain visible and not be obscured

## Exceptions
- native browser controls may keep default focus styles when custom styling would degrade accessibility
- hover states do not apply on pure touch contexts, but pressed/focus/selected feedback still matters
- essential motion may remain when it is truly required for understanding, but a reduced-motion path is still needed

## Failure patterns
- outline removed with no replacement
- state shown by color alone
- tooltips or menus that disappear too quickly
- small adjacent targets that create accidental taps
- focus trapped or hidden under sticky UI
- motion that cannot be reduced or stopped
- disabled states that vanish into the background

## Hand off to
- `color-system-expert.md` for contrast pair decisions
- `component-systems-expert.md` for required state coverage by component type
- `front-end-handoff-expert.md` for code implementation details
- `document-accessibility-expert.md` only when the task is document/PDF accessibility, not UI
