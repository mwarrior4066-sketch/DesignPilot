---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/accessibility-and-feedback-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: accessibility-feedback
---

# Accessibility Feedback Expert

## Purpose
Use this skill to make production-level decisions about interaction states, focus, keyboard behavior, hover/focus content, touch targets, motion safety, and user feedback.

## Activate when
- the task involves interactive UI
- focus, keyboard, hover/focus content, touch target sizing, reduced motion, or state visibility matter
- a component needs real feedback logic rather than visual polish alone

## Do not activate when
- the request is only about static visual hierarchy with no interactivity
- the task is only about PDF tagging or document structure

## Read these first
- `knowledge-base/summaries/accessibility-and-feedback-summary.md`

## Decision rules
- every interactive element needs a visible and reachable interaction model
- state visibility beats visual minimalism
- focus must stay visible and keyboard flow must stay logical
- color is never the only signal for state or meaning
- motion is an enhancement, not a requirement
- preferred touch-target guidance beats legal minimums when there is room to do it right

## Default actions
- define required states for the component or interface
- specify focus behavior and keyboard path
- ensure hover behavior has a focus/touch equivalent when relevant
- require reduced-motion behavior for non-essential motion
- require clear error, success, or loading feedback when user action needs confirmation

## Exception rules
- native controls may keep user-agent focus styles when custom styles would be weaker
- hover-only states do not apply on touch-only contexts, but pressed/selected/focus feedback still does
- essential motion may remain if understanding depends on it, but the reduced-motion path must still exist

## Fallback logic
- if a custom focus treatment fails contrast, fall back to a stronger two-layer or user-agent-visible ring
- if a target cannot grow, use spacing separation and a larger hit area
- if motion preferences are unknown, assume the reduced-motion path must exist
- if state design is missing, at minimum define rest, focus, active, disabled, and loading

## Failure traps
- removing focus styles without replacement
- hover-only interactions
- keyboard traps
- hidden or obscured focus
- tiny adjacent targets
- flashing or unbounded motion
- state meaning carried only by color
- error messages that do not provide a next step

## Evidence required
Use some combination of:
- required state list
- focus rule
- keyboard rule
- non-text contrast threshold
- touch-target threshold
- reduced-motion rule
- error/success/loading feedback rule

## Handoff to other skills
- hand off to `color-system-expert.md` for contrast pairs and palette decisions
- hand off to `component-systems-expert.md` for required state coverage by component type
- hand off to `front-end-handoff-expert.md` for code implementation details
- hand off to `ui-system-expert.md` when the real problem is task flow or hierarchy, not state treatment

## Output expectations
- concrete interaction logic
- visible accessibility guardrails
- no aesthetic shortcuts that erase feedback
