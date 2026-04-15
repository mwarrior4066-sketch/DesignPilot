---
skill_version: 1.0.0
source_reference:
  - src/knowledge-base/summaries/pdf-layout-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: pdf-layout
---

# PDF Layout Expert

## Purpose
Use this skill to edit, repair, or rebuild PDFs while preserving frame logic, baseline rhythm, visual hierarchy, and layout integrity.

## Activate when
- the task involves PDF editing, text replacement, spreads, footers, frame logic, baseline rhythm, or visual document fidelity
- visual edits could damage layout structure if handled casually

## Do not activate when
- the task is only a web page layout discussion
- the request is only about abstract print branding with no document handling
- the main problem is tagging, reading order, artifacts, or OCR remediation

## Read these first
- `src/knowledge-base/summaries/pdf-layout-summary.md`
- `src/knowledge-base/summaries/grid-mediums-summary.md`
- `src/knowledge-base/summaries/typography-summary.md`

## Decision rules
- treat PDFs as structured pages, not screenshots
- preserve frame logic before broad reflow
- respect baseline rhythm where the layout depends on it
- prefer structural fixes over masking fixes
- let document accessibility own tags, artifacts, and extraction rules

## Default actions
- preserve or infer frame relationships before replacing text
- preserve local text boxes instead of collapsing them into one generic region
- keep text selectable when required
- respect baseline rhythm and the source layout before inventing new logic
- use measured preservation for legacy layouts

## Exception rules
- visual-only deliverables may relax extraction requirements only if the user clearly accepts the tradeoff
- legacy layouts can justify measured preservation over generic grid defaults

## Fallback logic
- if the PDF lacks a stable grid or frame logic, hand off to `layout-reconstruction-expert.md`
- if tags, artifacts, or reading order matter, bring in `document-accessibility-expert.md`
- if a ligature or font mapping issue affects visible fit, bring in `type-system-expert.md`

## Failure traps
- patching with white boxes as a shortcut
- rasterizing to avoid hard layout work
- merging multiple local text regions into one generic box
- ignoring baseline drift
- solving a semantic accessibility problem with only visual edits

## Evidence required
Use some combination of:
- frame logic
- baseline note
- local-region preservation rule
- rasterization rule
- legacy-layout note

## Handoff to other skills
- hand off to `layout-reconstruction-expert.md` for inferred legacy structure
- hand off to `document-accessibility-expert.md` for tags, artifacts, reading order, and OCR
- hand off to `color-system-expert.md` when print or contrast logic affects output

## Output expectations
- explicit layout-preservation logic
- no fake fixes presented as structural fixes

## Added document/presentation rules
- for presentation PDFs and structured reports, preserve or re-establish page-role architecture and wayfinding landmarks
- keep footer and header spacing contracts symmetrical when the design system expects them
- treat overshoot lines, floating blocks, and ghost markers as layout integrity failures
- escalate from patching to rebuild when structural debt keeps forcing repeated full-page adjustments

## Runtime summary

<!-- Auto-generated runtime overlay. Edit src/skills/pdf-layout-expert.md -- not this section. -->

# pdf-layout-expert.md

## Activation conditions
- the task involves PDF editing, text replacement, spreads, footers, frame logic, baseline rhythm, or visual document fidelity
- visual edits could damage layout structure if handled casually
- the task is only a web page layout discussion
- the request is only about abstract print branding with no document handling
- the main problem is tagging, reading order, artifacts, or OCR remediation

## Non-activation conditions
- the task is only a web page layout discussion
- the request is only about abstract print branding with no document handling
- the main problem is tagging, reading order, artifacts, or OCR remediation

## Core decision rules
- treat PDFs as structured pages, not screenshots
- preserve frame logic before broad reflow
- respect baseline rhythm where the layout depends on it
- prefer structural fixes over masking fixes
- let document accessibility own tags, artifacts, and extraction rules

## Failure traps
- patching with white boxes as a shortcut
- rasterizing to avoid hard layout work
- merging multiple local text regions into one generic box
- ignoring baseline drift
- solving a semantic accessibility problem with only visual edits

## Summary dependencies
- pdf-layout-summary.md

## Escalation triggers
- visual-only deliverables may relax extraction requirements only if the user clearly accepts the tradeoff
- legacy layouts can justify measured preservation over generic grid defaults
- if the PDF lacks a stable grid or frame logic, hand off to `layout-reconstruction-expert.md`
- if tags, artifacts, or reading order matter, bring in `document-accessibility-expert.md`
- if a ligature or font mapping issue affects visible fit, bring in `type-system-expert.md`
- frame logic
- baseline note
- local-region preservation rule

## Adjacent handoff rules
- hand off to `layout-reconstruction-expert.md` for inferred legacy structure
- hand off to `document-accessibility-expert.md` for tags, artifacts, reading order, and OCR
- hand off to `color-system-expert.md` when print or contrast logic affects output

## Canonical fallback
- `src/skills/pdf-layout-expert.md`
- `src/knowledge-base/summaries/pdf-layout-summary.md`
