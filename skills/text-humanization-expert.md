---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/text-humanization-summary.md
  - knowledge-base/source-docs/Humanizing Writing Protocol.md
last_updated: 2026-04-11
synchronized: true
canonical_owner: true
domain: writing-quality
---

# Text Humanization Expert

## Purpose
Use this skill to revise prose so it sounds authored, readable, and natural without changing meaning, adding claims, or flattening the writer’s voice.

## Activate when
- the user asks to humanize, naturalize, de-mechanize, or make writing sound less AI-shaped
- the output is prose-heavy and clearly sounds formulaic, repetitive, or over-scaffolded
- routed expert output is technically correct but still stiff after explanation filtering

## Do not activate when
- the artifact is code, a schema, a validator report, a route file, or a strict implementation spec
- the task is only structural diagnosis with no prose rewrite

## Read these first
- `knowledge-base/summaries/text-humanization-summary.md`
- `knowledge-base/summaries/writing-and-case-study-summary.md`
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
