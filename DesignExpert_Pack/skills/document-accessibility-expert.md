---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/pdf-document-accessibility-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: document-accessibility
---

# Document Accessibility Expert

## Purpose
Use this skill to preserve or restore document accessibility: tagging, reading order, artifacts, Unicode mapping, OCR remediation, and extraction fidelity.

## Activate when
- the task involves accessible PDFs or other structured documents
- the document must remain machine-readable and usable with assistive technology
- tagging, artifacts, OCR, alt text, tables, or extraction fidelity matter

## Do not activate when
- the task is only static page styling with no structural document requirement
- the request is purely about fresh UI, not documents

## Read these first
- `knowledge-base/summaries/pdf-document-accessibility-summary.md`

## Decision rules
- treat every page object as real content, artifact, or removable noise
- logical order beats paint order
- text should remain Unicode-recoverable when extraction matters
- fixes must preserve or restore semantics, not only visuals
- a PDF that must stay accessible cannot be “fixed” as a flat image

## Default actions
- classify content vs artifacts
- verify or restore reading order
- verify tagging expectations for headings, lists, tables, figures, and forms when relevant
- verify alt text for meaningful graphics
- verify extraction-safe text mapping
- trigger OCR remediation before structural edits when the source is scanned or broken

## Exception rules
- purely decorative output can relax document semantics only if the user explicitly accepts a visual-only artifact
- flexible heading behavior may vary by standard/version, but logical structure still matters

## Fallback logic
- if the structure tree is missing, reconstruct the most defensible structure before claiming accessibility
- if OCR is the only way to recover text, repair OCR output before layout refinement
- if a footer or border is decorative, artifact it instead of leaving it as noisy content

## Failure traps
- rasterizing a document to avoid semantic work
- leaving decorative clutter in the reading order
- ligatures or glyphs that extract incorrectly
- multi-column reading order handled visually but not logically
- alt text missing for meaningful graphics

## Evidence required
Use some combination of:
- tag/artifact rule
- reading-order rule
- extraction rule
- OCR fallback rule
- alt-text or table-structure note

## Handoff to other skills
- hand off to `pdf-layout-expert.md` for frame and visual/layout logic
- hand off to `layout-reconstruction-expert.md` when legacy structure must be inferred
- hand off to `type-system-expert.md` when readable fit or rag handling matters

## Output expectations
- semantics explicit
- document behavior preserved
- no visual-only fixes presented as accessibility work
