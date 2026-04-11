---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/PDF Document Accessibility Expert Research.md
last_updated: 2026-04-09
synchronized: true
domain: document-accessibility
---

# PDF Document Accessibility Summary

## Purpose
Canonical summary for PDF/UA-style document accessibility: tags, reading order, artifacts, Unicode mapping, OCR fallback, and extraction-safe remediation.

## Use when
- the PDF must remain a document, not just a visual artifact
- tagging, reading order, extraction, or OCR remediation matter

## Default rules
- every page object must be real content, an artifact, or removed
- reading order follows logical structure, not paint order
- meaningful graphics need alt text
- decorative headers, footers, and borders should be artifacts when appropriate
- text must remain Unicode-recoverable if extraction matters

## Key concerns
- tagging and structure tree integrity
- reading order across multi-column pages
- artifact handling
- alt text and table semantics
- ligature and Unicode mapping
- OCR fallback for scanned or broken documents

## Failure patterns
- visual-only fixes that break semantics
- untagged content
- decorative clutter read as content
- ligatures or glyphs that extract incorrectly
- OCR text left uncorrected
- multi-column reading order broken

## Hand off to
- `pdf-layout-expert.md` for frame and visual/layout decisions
- `layout-reconstruction-expert.md` when legacy page structure must be inferred
- `type-system-expert.md` when readable fit or rag handling matters
