---
skill_version: 1.0.0
source_reference:
  - src/knowledge-base/summaries/text-humanization-summary.md
  - src/knowledge-base/source-docs/Humanizing Writing Protocol.md
last_updated: 2026-04-11
synchronized: true
canonical_owner: true
domain: writing-quality
---

# Text Humanization Expert

## Purpose
Use this skill to revise prose so it sounds authored, readable, and natural without changing meaning, adding claims, or flattening the writer’s voice.

## Cross-cutting surface role
This skill is not only a standalone rewrite route.
It is also the default finishing pass for user-visible prose across the pack.

Use it when:
- startup wording feels machine-shaped
- task framing is correct but cold
- explanation text is structurally sound but stiff
- guidance text sounds infrastructural instead of helpful
- the response filter preserved truth but not naturalness

When used as a cross-cutting pass, preserve the governing route’s evidence burden and decision logic.

## Activate when
- the user asks to humanize, naturalize, de-mechanize, or make writing sound less AI-shaped
- the task is a rewrite where prose quality is the governing need
- startup wording, task framing, explanation text, next-step text, or user-facing guidance sounds machine-shaped
- a response is technically correct but still stiff after explanation filtering

## Do not activate when
- the artifact is code, a schema, a validator report, a route file, or a strict implementation spec
- the task is only structural diagnosis with no prose rewrite

## Never use this to
- add claims
- soften hard constraints
- hide proof gaps
- inject fake warmth
- replace the voice with generic polished AI copy
- casualize precise writing by default
- leave em dashes in user-facing prose when the same thought would read better with simpler punctuation


## Read these first
- `src/knowledge-base/summaries/text-humanization-summary.md`
- `src/knowledge-base/summaries/writing-and-case-study-summary.md`
- `DESIGNER_RESPONSE_FILTER_PROTOCOL.md`

## Decision rules
- meaning before voice polish
- the job of the piece before sentence-level edits
- logic and cohesion before texture
- reduce pattern repetition without rewriting for difference only
- preserve the user’s tone where it exists

## Default actions
- identify the job of the piece
- mark repeated machine-shaped patterns
- repair grammar, verb logic, and sentence transitions
- rebalance rhythm and clause length
- translate machine-shaped helper language into steady, natural operator language without changing the meaning
- replace em dashes in user-facing prose with cleaner sentence breaks, commas, colons, parentheses, or simple hyphens where needed
- run a realism pass that removes generic polish language
- state any residual drift risk

## Failure traps
- adding claims
- changing the argument
- casualizing by default
- replacing the voice with generic clean copy
- pruning so aggressively that the text becomes vague

## Evidence required
Use some combination of:
- meaning-preservation note
- pattern scan note
- revised passage
- drift-risk note
- voice-preservation note

## Handoff to other skills
- hand off to `content-and-case-study-expert.md` when structure, mode, or proof language must change before prose quality work
- hand off to `brand-strategy-expert.md` when tone must track a brand system instead of only sounding more natural

## Runtime summary

<!-- Auto-generated runtime overlay. Edit src/skills/text-humanization-expert.md -- not this section. -->

# text-humanization-expert.md

## Activation conditions
- the user asks to humanize, naturalize, de-mechanize, or make writing sound less AI-shaped
- the task is a rewrite where prose quality is the governing need
- startup wording, task framing, explanation text, next-step text, or user-facing guidance sounds machine-shaped
- a response is technically correct but still stiff after explanation filtering
- the artifact is code, a schema, a validator report, a route file, or a strict implementation spec
- the task is only structural diagnosis with no prose rewrite

## Non-activation conditions
- the artifact is code, a schema, a validator report, a route file, or a strict implementation spec
- the task is only structural diagnosis with no prose rewrite

## Core decision rules
- meaning before voice polish
- the job of the piece before sentence-level edits
- logic and cohesion before texture
- reduce pattern repetition without rewriting for difference only
- preserve the user’s tone where it exists

## Failure traps
- adding claims
- changing the argument
- casualizing by default
- replacing the voice with generic clean copy
- pruning so aggressively that the text becomes vague

## Summary dependencies
- text-humanization-summary.md
- Humanizing Writing Protocol.md

## Escalation triggers
- meaning-preservation note
- pattern scan note
- revised passage
- drift-risk note
- voice-preservation note

## Adjacent handoff rules
- hand off to `content-and-case-study-expert.md` when structure, mode, or proof language must change before prose quality work
- hand off to `brand-strategy-expert.md` when tone must track a brand system instead of only sounding more natural

## Canonical fallback
- `src/skills/text-humanization-expert.md`
- `src/knowledge-base/summaries/text-humanization-summary.md`
- `src/knowledge-base/summaries/Humanizing Writing Protocol.md`
