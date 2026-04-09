---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/typography-summary.md
  - knowledge-base/summaries/typeface-database-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: type-system
---

# Type System Expert

## Purpose
Use this skill to choose, compare, pair, substitute, and deploy typefaces intelligently across UI, editorial, brand, dashboards, presentations, print, and multilingual systems.

## Activate when
- the task involves font choice, pairing, hierarchy, readability, measure, leading, variable fonts, opsz, fallback stacks, or licensing-aware substitutes
- typography affects implementation, contrast, or dense-data clarity

## Do not activate when
- the task is only broad brand strategy with no typographic decision
- the task is only a generic layout skeleton with no text hierarchy

## Read these first
- `knowledge-base/summaries/typography-summary.md`
- `knowledge-base/summaries/typeface-database-summary.md`
- `libraries/FONT_LIBRARY.json`, `libraries/FONT_LIBRARY.md`

## Decision rules
- assign type by role before by taste: display, heading, body, caption, mono, accent
- readability and role fit beat novelty
- prefer measurable defaults for measure and leading
- use variable font logic when it improves performance or optical control
- licensing, platform support, and fallback quality matter in real systems

## Default actions
- define role assignment
- set body/display/caption logic
- specify measure and leading
- note opsz or variable-font use when relevant
- propose fallback or substitute stacks when the requested face is unavailable or risky

## Default thresholds
- body text should usually target roughly 45 to 75 characters per line, with around 66 as a strong default
- body leading should usually start around 1.5x font size
- large headings can run tighter than body copy
- smaller text may need stronger weight, spacing, or opsz support

## Exception rules
- footnotes, labels, or narrow UI may justify a tighter measure
- CJK or multilingual contexts may need different line-length and fallback logic
- branding work may justify more expressive faces if they do not undermine legibility in actual use

## Fallback logic
- if a requested font is unavailable, offer a named structural substitute rather than a generic “sans-serif”
- if variable fonts are unsupported, fall back to discrete weights and keep the stack explicit
- if licensing is unclear, prefer known-safe open-source or system alternatives until the licensing risk is resolved

## Failure traps
- shrinking type to solve layout problems
- pairing fonts with overlapping jobs and no role distinction
- using decorative display faces for sustained reading
- ignoring fallback stacks and platform support
- recommending premium fonts without naming viable open-source or system substitutes when needed

## Evidence required
Use some combination of:
- role map
- measure target
- leading ratio
- variable-font / opsz rule
- fallback stack
- substitute logic
- licensing or deployment note when relevant

## Handoff to other skills
- hand off to `grid-system-expert.md` when the issue is really measure vs layout width
- hand off to `color-system-expert.md` when contrast depends on weight or size
- hand off to `front-end-handoff-expert.md` when font loading and deployment matter
- hand off to `dashboard-data-expert.md` when dense-data typography needs special treatment

## Output expectations
- type by role
- readable defaults
- explicit substitutes and fallbacks
- implementation-aware recommendations when relevant
