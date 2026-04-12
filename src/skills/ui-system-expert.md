---
skill_version: 1.0.0
source_reference:
  - src/knowledge-base/summaries/ui-system-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: ui-system
---

# UI System Expert

## Purpose
Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.

## Activate when
- the task is about screens, flows, navigation, IA, page hierarchy, action placement, or system structure
- the user needs system logic before polish or code

## Do not activate when
- the task is only a font choice
- the task is only a print-specific PDF repair
- the issue is purely about chart logic or dense-data rules

## Read these first
- `src/knowledge-base/summaries/ui-system-summary.md`
- `src/knowledge-base/summaries/ux-cognition-summary.md`

## Decision rules
- solve the primary task path first
- solve hierarchy second
- solve navigation and action placement third
- hand off specialist concerns instead of restating their rules
- visual polish happens after the system is coherent

## Default actions
- name the primary user action
- define the screen or page hierarchy
- identify major structural states
- separate global structure from local styling
- keep hierarchy legible before component detail

## Exception rules
- if the user asks for a tiny component change, keep system notes brief
- if the system is already established, preserve it before introducing new patterns

## Fallback logic
- if the flow is unclear, define the minimum viable path instead of designing every edge case
- if a request is actually dashboard-specific, hand off to `dashboard-data-expert.md`
- if state requirements dominate the task, hand off to `accessibility-feedback-expert.md`

## Failure traps
- hiding broken UX under polished components
- designing screens without naming the main action
- overfitting local components while the flow is still broken
- solving dashboard density or accessibility issues with generic UI advice

## Evidence required
Use some combination of:
- primary action
- hierarchy map
- navigation logic
- structural state note
- dependency on grid or type system

## Handoff to other skills
- hand off to `grid-system-expert.md` for layout scaffolding
- hand off to `type-system-expert.md` when hierarchy depends on typography
- hand off to `dashboard-data-expert.md` when metrics/charts dominate the problem
- hand off to `accessibility-feedback-expert.md` when state, motion, or keyboard logic matters
- hand off to `front-end-handoff-expert.md` when the system is ready for implementation

## Output expectations
- structure first
- action logic clear
- no specialist duplication
