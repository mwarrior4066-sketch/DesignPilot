---
runtime_card_version: 1.0.0
canonical_skill: skills/content-and-case-study-expert.md
last_generated: 2026-04-11
overlay: true
---
# content-and-case-study-expert.md

## Activation conditions
- the task is a rewrite, simplification, UX copy pass, CTA/error message pass, rationale rewrite, documentation pass, or case-study narrative
- the answer must be clearer, better structured, more evidence-based, or better matched to its writing mode
- the task is mainly visual hierarchy, layout, or composition
- the request is only abstract brand strategy with no writing output
- the task is only a tiny label tweak that can be answered inside another specialist skill without broader writing decisions

## Non-activation conditions
- the task is mainly visual hierarchy, layout, or composition
- the request is only abstract brand strategy with no writing output
- the task is only a tiny label tweak that can be answered inside another specialist skill without broader writing decisions

## Core decision rules
- clarity beats inflated language
- mode fit beats stylistic flourish
- problem before solution in case-study and rationale writing
- evidence beats adjectives
- UX copy, documentation, audits, rebuilds, and portfolio writing are different modes, not cosmetic variants of the same tone
- artifacts should never appear without narrative function

## Failure traps
- writing a rebuild answer like an audit
- writing a case study like marketing copy
- writing documentation like a personal story
- error messages with no recovery step
- design claims with no rationale or evidence
- artifacts/screenshots dropped in with no caption or narrative function
- portfolio writing that hides role, decision logic, or outcomes behind pretty language

## Summary dependencies
- writing-and-case-study-summary.md
- Case-Study Structure and Narrative Order.md

## Escalation triggers
- specialist audiences may need necessary domain terms, but explain them if they create friction
- long-form case studies may be richer, but still need a front-loaded structure and visible outcomes
- brand tone can add character, but not at the cost of comprehension or actionability
- exploratory concept work may rely on logic and hypothesis rather than hard metrics, but the uncertainty must be named
- if the mode is unclear, infer it from the request and make the choice explicit in the response structure
- if the audience is unclear, default to plain language
- if the text is too dense, chunk it instead of merely shortening it
- if evidence is weak, mark the claim as inference or hypothesis instead of pretending certainty

## Adjacent handoff rules
- hand off to `ux-research-expert.md` when claims must tie back to research
- hand off to `brand-strategy-expert.md` when tone, audience fit, or claim burden depends on strategy
- hand off to `graphic-design-expert.md` when captions, slide copy, or poster text must respond to distance or format logic
- hand off to `text-humanization-expert.md` when the structure is right but the prose still sounds formulaic or machine-shaped

## Canonical fallback
- `skills/content-and-case-study-expert.md`
- `knowledge-base/summaries/writing-and-case-study-summary.md`
- `knowledge-base/summaries/Case-Study Structure and Narrative Order.md`