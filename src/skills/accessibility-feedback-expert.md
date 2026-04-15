---
skill_version: 1.1.0
source_reference:
  - src/knowledge-base/summaries/accessibility-and-feedback-summary.md
last_updated: 2026-04-11
synchronized: true
canonical_owner: true
domain: accessibility-feedback
---

# Accessibility Feedback Expert

## Purpose
Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.

## Activate when
- the task involves interactive UI
- focus, keyboard behavior, overlay logic, live announcements, touch target sizing, reduced motion, or state visibility matter
- a component needs real behavior logic rather than visual polish alone

## Do not activate when
- the request is only about static visual hierarchy with no interactivity
- the task is only about PDF tagging or document structure

## Read these first
- `src/knowledge-base/summaries/accessibility-and-feedback-summary.md`

## Decision rules
- native first
- no ARIA is better than bad ARIA
- every interactive element needs a visible and reachable interaction model
- focus must stay visible, restorable, and logically ordered
- color is never the only signal for state or meaning
- motion is an enhancement, not a requirement
- async updates must be announced, not silently swapped into the page

## Default actions
- define required states for the component or interface
- specify focus behavior, keyboard path, and activation model
- choose native vs custom widget posture and justify custom roles when used
- require live-region or status behavior for async updates and validation messages
- require reduced-motion behavior for non-essential motion
- require clear error, success, or loading feedback when user action needs confirmation
- name modal, tab, grid, combobox, or disclosure behavior when relevant

## Exception rules
- native controls may keep user-agent focus styles when custom styles would be weaker
- hover-only states do not apply on touch-only contexts, but pressed and focus feedback still do
- essential motion may remain if understanding depends on it, but the reduced-motion path must still exist

## Fallback logic
- if a custom focus treatment fails contrast, fall back to a stronger visible ring
- if a target cannot grow, use spacing separation and a larger hit area
- if motion preferences are unknown, assume the reduced-motion path must exist
- if a composite widget is too dense for normal tab order, use roving tabindex or `aria-activedescendant` logic instead of tabbing every item
- if an overlay opens, make background content inert and restore focus on close

## Failure traps
- removing focus styles without replacement
- hover-only interactions
- keyboard traps
- hidden or obscured focus
- tiny adjacent targets
- flashing or unbounded motion
- state meaning carried only by color
- silent loading or error changes
- fake ARIA depth on generic containers
- focus reset to the top of the page

## Evidence required
Use some combination of:
- required state list
- focus rule
- keyboard rule or key map
- native vs custom justification
- live-region or async announcement rule
- touch-target threshold
- reduced-motion rule
- verification note

## Handoff to other skills
- hand off to `front-end-handoff-expert.md` for code implementation details
- hand off to `front-end-architecture-expert.md` when state architecture and widget behavior interact
- hand off to `color-system-expert.md` for contrast pairs and palette decisions
- hand off to `component-systems-expert.md` for required state coverage by component type
- hand off to `ui-system-expert.md` when the real problem is task flow or hierarchy, not state treatment

## Output expectations
- concrete interaction logic
- visible accessibility guardrails
- no aesthetic shortcuts that erase behavior

## Runtime summary

<!-- Auto-generated runtime overlay. Edit src/skills/accessibility-feedback-expert.md -- not this section. -->

# accessibility-feedback-expert.md

## Activation conditions
- the task involves interactive UI
- focus, keyboard behavior, overlay logic, live announcements, touch target sizing, reduced motion, or state visibility matter
- a component needs real behavior logic rather than visual polish alone
- the request is only about static visual hierarchy with no interactivity
- the task is only about PDF tagging or document structure

## Non-activation conditions
- the request is only about static visual hierarchy with no interactivity
- the task is only about PDF tagging or document structure

## Core decision rules
- native first
- no ARIA is better than bad ARIA
- every interactive element needs a visible and reachable interaction model
- focus must stay visible, restorable, and logically ordered
- color is never the only signal for state or meaning
- motion is an enhancement, not a requirement
- async updates must be announced, not silently swapped into the page

## Failure traps
- removing focus styles without replacement
- hover-only interactions
- keyboard traps
- hidden or obscured focus
- tiny adjacent targets
- flashing or unbounded motion
- state meaning carried only by color
- silent loading or error changes

## Summary dependencies
- accessibility-and-feedback-summary.md

## Escalation triggers
- native controls may keep user-agent focus styles when custom styles would be weaker
- hover-only states do not apply on touch-only contexts, but pressed and focus feedback still do
- essential motion may remain if understanding depends on it, but the reduced-motion path must still exist
- if a custom focus treatment fails contrast, fall back to a stronger visible ring
- if a target cannot grow, use spacing separation and a larger hit area
- if motion preferences are unknown, assume the reduced-motion path must exist
- if a composite widget is too dense for normal tab order, use roving tabindex or `aria-activedescendant` logic instead of tabbing every item
- if an overlay opens, make background content inert and restore focus on close

## Adjacent handoff rules
- hand off to `front-end-handoff-expert.md` for code implementation details
- hand off to `front-end-architecture-expert.md` when state architecture and widget behavior interact
- hand off to `color-system-expert.md` for contrast pairs and palette decisions
- hand off to `component-systems-expert.md` for required state coverage by component type
- hand off to `ui-system-expert.md` when the real problem is task flow or hierarchy, not state treatment

## Canonical fallback
- `src/skills/accessibility-feedback-expert.md`
- `src/knowledge-base/summaries/accessibility-and-feedback-summary.md`
