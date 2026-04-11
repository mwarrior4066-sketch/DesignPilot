---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/ux-roadmap-summary.md
  - knowledge-base/summaries/ux-cognition-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: ux-research
---

# UX Research Expert

## Purpose
Use this skill to frame the problem, identify the user, surface cognitive/ergonomic constraints, and keep work tied to real needs instead of surface styling.

## Activate when
- the task is about problem framing, audience behavior, market gap, research synthesis, validation, or human constraints
- the user needs to understand what problem is actually being solved

## Do not activate when
- the task is a narrow, already-scoped implementation detail with no research implication

## Read these first
- `knowledge-base/summaries/ux-roadmap-summary.md`
- `knowledge-base/summaries/ux-cognition-summary.md`
- `knowledge-base/summaries/audience-and-industry-summary.md`

## Decision rules
- define the problem before solving the interface
- use audience logic before stylistic assumptions
- cognitive and ergonomic constraints are part of the problem, not a late QA pass

## Default actions
- define the problem statement
- define the target audience and behavior logic
- identify the main friction or task failure
- identify what the user must accomplish and what blocks them
- if reusable handoff research is needed, ask whether the user wants deep-research prompts
- if yes, generate at most 4 prompts with distinct evidence goals

## Exception rules
- if the task is already deep in implementation, keep the research note brief and relevant

## Fallback logic
- if research is thin, use the most defensible low-assumption framing and state the uncertainty

## Failure traps
- solving cosmetic drift instead of the actual problem
- designing for everyone
- claiming validation without evidence

## Evidence required
Use some combination of:
- problem frame
- audience logic
- main friction
- success condition

## Handoff to other skills
- hand off to `brand-strategy-expert.md` for positioning and tone
- hand off to `ui-system-expert.md` once the problem and user are clear
- hand off to `content-and-case-study-expert.md` when the task becomes communication

## Output expectations
- clear problem framing
- clear user framing
- no surface-level drift presented as research
