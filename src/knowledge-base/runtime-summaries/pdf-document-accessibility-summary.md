---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/pdf-document-accessibility-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/PDF Document Accessibility Expert Research.md
---
# Pdf Document Accessibility Summary Runtime Summary

## Decision rules
- every page object must be real content, an artifact, or removed
- reading order follows logical structure, not paint order
- meaningful graphics need alt text
- decorative headers, footers, and borders should be artifacts when appropriate
- text must remain Unicode-recoverable if extraction matters

## Failure traps
- visual-only fixes that break semantics
- untagged content
- decorative clutter read as content
- ligatures or glyphs that extract incorrectly
- OCR text left uncorrected
- multi-column reading order broken

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/pdf-document-accessibility-summary.md`
- `src/knowledge-base/source-docs/PDF Document Accessibility Expert Research.md`