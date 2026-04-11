---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/pdf-layout-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/AI PDF Creation_ Grid and Typography.md
---
# Pdf Layout Summary Runtime Summary

## Decision rules
- for report decks and presentation PDFs, maintain explicit page roles (cover, TOC, divider, content, close) when navigation matters
- preserve symmetric top/bottom spacing contracts and a known content box before tuning component heights
- lines, guides, and decorative indicators must stop exactly at their intended section bounds
- repeated chrome labels should not be duplicated above local page titles
- if spacing debt, density debt, and narrative debt keep recurring together, escalate from patching to structured rebuild
- treat PDFs as documents, not screenshots
- preserve text frames, reading order, and extraction when required
- decorative material should be marked as artifacts when structure matters
- fonts should be embedded and mapped to Unicode when possible
- tagged structure matters for accessible PDFs

## Failure traps
- No extracted failure traps; fall back to the canonical summary.

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/pdf-layout-summary.md`
- `knowledge-base/source-docs/AI PDF Creation_ Grid and Typography.md`