---
runtime_card_version: 1.0.0
canonical_skill: skills/type-system-expert.md
last_generated: 2026-04-11
overlay: true
---
# type-system-expert.md

## Activation conditions
- the task involves font choice, pairing, hierarchy, readability, measure, leading, variable fonts, optical sizing, script coverage, fallback stacks, or licensing-aware substitutes
- typography affects implementation, contrast, or dense-data clarity
- the task is only broad brand strategy with no typographic decision
- the task is only a generic layout skeleton with no text hierarchy

## Non-activation conditions
- the task is only broad brand strategy with no typographic decision
- the task is only a generic layout skeleton with no text hierarchy

## Core decision rules
- assign type by role before by taste: display, heading, body, caption, mono, accent
- readability and role fit beat novelty
- check script coverage before tone when the system is multilingual
- prefer measurable defaults for measure and leading
- prefer families with explicit numeric/data features for dashboards and dense tables
- use variable font logic when it improves performance or optical control
- use high-level CSS controls before low-level `font-variation-settings`
- licensing, platform support, and fallback quality matter in real systems

## Failure traps
- shrinking type to solve layout problems
- pairing fonts with overlapping jobs and no role distinction
- using decorative display faces for sustained reading
- ignoring fallback stacks, script coverage, and platform support
- recommending premium fonts without naming viable open-source or system substitutes when needed
- using `font-variation-settings` as a default hammer when higher-level CSS properties would do the job

## Summary dependencies
- typography-summary.md
- typeface-database-summary.md

## Escalation triggers
- footnotes, labels, or narrow UI may justify a tighter measure
- CJK or multilingual contexts may need different line-length, fallback, and optical-balance logic
- branding work may justify more expressive faces if they do not undermine legibility in actual use
- accessibility-sensitive work may justify Atkinson Hyperlegible Next, Hyperlegible Mono, Lexend, Luciole, or similar families when readability value is real
- if a requested font is unavailable, offer a named structural substitute rather than a generic `sans-serif`
- if the chosen family lacks the needed script support, switch to a script-capable family before tuning tone
- if variable fonts are unsupported, fall back to discrete weights and keep the stack explicit
- if licensing is unclear, prefer known-safe open-source or system alternatives until the licensing risk is resolved

## Adjacent handoff rules
- hand off to `grid-system-expert.md` when the issue is really measure vs layout width
- hand off to `color-system-expert.md` when contrast depends on weight or size
- hand off to `front-end-handoff-expert.md` when font loading and deployment matter
- hand off to `dashboard-data-expert.md` when dense-data typography needs special treatment

## Canonical fallback
- `skills/type-system-expert.md`
- `knowledge-base/summaries/typography-summary.md`
- `knowledge-base/summaries/typeface-database-summary.md`