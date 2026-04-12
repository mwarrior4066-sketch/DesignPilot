---
runtime_card_version: 1.0.0
canonical_skill: src/skills/document-accessibility-expert.md
last_generated: 2026-04-11
overlay: true
---
# document-accessibility-expert.md

## Activation conditions
- the task involves accessible PDFs or other structured documents
- the document must remain machine-readable and usable with assistive technology
- tagging, artifacts, OCR, alt text, tables, or extraction fidelity matter
- the task is only static page styling with no structural document requirement
- the request is purely about fresh UI, not documents

## Non-activation conditions
- the task is only static page styling with no structural document requirement
- the request is purely about fresh UI, not documents

## Core decision rules
- treat every page object as real content, artifact, or removable noise
- logical order beats paint order
- text should remain Unicode-recoverable when extraction matters
- fixes must preserve or restore semantics, not only visuals
- a PDF that must stay accessible cannot be “fixed” as a flat image

## Failure traps
- rasterizing a document to avoid semantic work
- leaving decorative clutter in the reading order
- ligatures or glyphs that extract incorrectly
- multi-column reading order handled visually but not logically
- alt text missing for meaningful graphics

## Summary dependencies
- pdf-document-accessibility-summary.md

## Escalation triggers
- purely decorative output can relax document semantics only if the user explicitly accepts a visual-only artifact
- flexible heading behavior may vary by standard/version, but logical structure still matters
- if the structure tree is missing, reconstruct the most defensible structure before claiming accessibility
- if OCR is the only way to recover text, repair OCR output before layout refinement
- if a footer or border is decorative, artifact it instead of leaving it as noisy content
- tag/artifact rule
- reading-order rule
- extraction rule

## Adjacent handoff rules
- hand off to `pdf-layout-expert.md` for frame and visual/layout logic
- hand off to `layout-reconstruction-expert.md` when legacy structure must be inferred
- hand off to `type-system-expert.md` when readable fit or rag handling matters

## Canonical fallback
- `src/skills/document-accessibility-expert.md`
- `src/knowledge-base/summaries/pdf-document-accessibility-summary.md`