---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/writing-and-case-study-summary.md
  - knowledge-base/source-docs/Case-Study Structure and Narrative Order.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: content-and-case-study
---

# Content and Case Study Expert

## Purpose
Use this skill to audit, rewrite, expand, or structure UX copy, design rationale, documentation, and case-study writing without losing clarity, mode control, or evidence.

## Activate when
- the task is a rewrite, simplification, UX copy pass, CTA/error message pass, rationale rewrite, documentation pass, or case-study narrative
- the answer must be clearer, better structured, more evidence-based, or better matched to its writing mode

## Do not activate when
- the task is mainly visual hierarchy, layout, or composition
- the request is only abstract brand strategy with no writing output
- the task is only a tiny label tweak that can be answered inside another specialist skill without broader writing decisions

## Read these first
- `knowledge-base/summaries/writing-and-case-study-summary.md`
- `knowledge-base/summaries/ux-roadmap-summary.md` when the reasoning must track the project phase

## Decision rules
- clarity beats inflated language
- mode fit beats stylistic flourish
- problem before solution in case-study and rationale writing
- evidence beats adjectives
- UX copy, documentation, audits, rebuilds, and portfolio writing are different modes, not cosmetic variants of the same tone
- artifacts should never appear without narrative function

## Default actions
- identify the writing mode first: case study, audit, rebuild plan, expand proposal, UX copy, or documentation
- identify the audience before choosing tone
- simplify wording before adding tone
- respect the active explanation tier before increasing explanation density
- split dense instructions into steps or chunks when needed
- add rationale and evidence wherever the text makes design claims
- annotate or caption visuals if they are referenced in a narrative
- keep the case-study backbone visible: problem → process → solution → outcome
- for project continuity, keep roadmap sections legible as done before → just added → needed next when meaningful progress is reported

## Useful thresholds
- aim below roughly 20 to 25 words per sentence when possible
- one main idea per paragraph
- case studies should foreground role, problem framing, decisions, and outcomes
- rebuild mode should sound directive and ordered, not diagnostic
- audits should clearly separate issue, impact, and recommendation
- if outcomes lack metrics, say so and use the strongest available qualitative proof without inventing certainty

## Exception rules
- specialist audiences may need necessary domain terms, but explain them if they create friction
- long-form case studies may be richer, but still need a front-loaded structure and visible outcomes
- brand tone can add character, but not at the cost of comprehension or actionability
- exploratory concept work may rely on logic and hypothesis rather than hard metrics, but the uncertainty must be named

## Fallback logic
- if the mode is unclear, infer it from the request and make the choice explicit in the response structure
- if the audience is unclear, default to plain language
- if the text is too dense, chunk it instead of merely shortening it
- if evidence is weak, mark the claim as inference or hypothesis instead of pretending certainty
- if a case study is under-structured, fall back to Hero / Overview / Problem / Process / Solution / Outcome / Learnings

## Failure traps
- writing a rebuild answer like an audit
- writing a case study like marketing copy
- writing documentation like a personal story
- error messages with no recovery step
- design claims with no rationale or evidence
- artifacts/screenshots dropped in with no caption or narrative function
- portfolio writing that hides role, decision logic, or outcomes behind pretty language

## Evidence required
Use some combination of:
- writing mode note
- audience note
- clarity pass
- rationale/evidence note
- case-study structure choice
- outcome or validation framing

## Handoff to other skills
- hand off to `ux-research-expert.md` when claims must tie back to research
- hand off to `brand-strategy-expert.md` when tone, audience fit, or claim burden depends on strategy
- hand off to `graphic-design-expert.md` when captions, slide copy, or poster text must respond to distance or format logic
- hand off to `text-humanization-expert.md` when the structure is right but the prose still sounds formulaic or machine-shaped

## Output expectations
- mode-correct writing
- plain but not dull language
- clearer than the source
- grounded in audience, decision logic, and evidence
- explicit when proof is absent instead of fake-certainty language
