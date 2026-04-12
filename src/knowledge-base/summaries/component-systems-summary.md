---
summary_version: 1.0.0
source_reference:
  - src/knowledge-base/source-docs/Component Systems Expert Research.md
last_updated: 2026-04-09
synchronized: true
domain: component-systems
---

# Component Systems Summary

## Purpose
Canonical summary for component inventories, variants, required states, sizes, reuse, governance, and “new component vs reuse” decisions.

## Use when
- the task is about component creation, registry checks, variants, design-system coverage, or governance

## Default rules
- prefer reuse and composition before new components
- every component should document purpose, when to use, when not to use, variants, sizes, states, accessibility rules, and implementation status
- stable components beat local custom reinventions
- every interactive component needs state coverage, not just a rest state

## Key thresholds
- inventory completeness target: near-total coverage of purpose, variants, sizes, states, accessibility, and implementation fields
- every new component should prove it is behaviorally distinct, not just visually different
- governance should have a clear path for proposal, review, and deprecation

## Exceptions
- product-specific local components are allowed only when the behavior is genuinely unique
- incubating components can exist, but they should not be the default recommendation

## Failure patterns
- phantom components with no real spec
- duplicate components solving the same task
- unstable variants used as if they were core system primitives
- visual variants added without new behavior or semantic need
- component docs missing “when not to use”

## Hand off to
- `accessibility-feedback-expert.md` for state and interaction requirements
- `front-end-handoff-expert.md` for code-ready handoff
- `ui-system-expert.md` when the issue is actually flow/structure, not component choice
