---
runtime_card_version: 1.0.0
canonical_skill: src/skills/pdf-layout-expert.md
last_generated: 2026-04-11
overlay: true
---
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