---
runtime_card_version: 1.0.0
canonical_skill: src/skills/text-humanization-expert.md
last_generated: 2026-04-11
overlay: true
---
# text-humanization-expert.md

## Activation conditions
- the user asks to humanize, naturalize, de-mechanize, or make writing sound less AI-shaped
- the output is prose-heavy and clearly sounds formulaic, repetitive, or over-scaffolded
- routed expert output is technically correct but still stiff after explanation filtering
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