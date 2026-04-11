---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/Layout Reconstruction Expert Research.md
last_updated: 2026-04-09
synchronized: true
domain: layout-reconstruction
---

# Layout Reconstruction Summary

## Purpose
Canonical summary for inferring, reconstructing, normalizing, and extending existing layouts from screenshots, PDFs, and legacy designs.

## Use when
- the user wants to extend or repair an existing layout
- the structure must be inferred rather than invented
- the layout is inconsistent and needs normalization

## Default rules
- in slide decks and report pages, infer not only margins and columns but also page-role architecture, header/footer contracts, and vertical fill rules
- normalize floating-card layouts by clustering internal content and recalculating card height from the content box instead of copying arbitrary heights
- preserve section-divider logic, TOC logic, and chapter wayfinding if they are part of the recovered structure
- infer the latent layout model first: margins, columns, gutters, baseline, repeated modules
- preserve the source layout when it is stable enough to extend
- normalize dirty layouts to the nearest defensible spacing rhythm rather than copying every inconsistency
- if inference is ambiguous, choose the smallest safe model and state the confidence

## Typical outputs
- inferred grid or manuscript model
- preserved exception zones
- normalized gutter/margin rule
- baseline or vertical rhythm note
- confidence and fallback note

## Exceptions
- posters, rotated type, or deliberately non-Manhattan layouts may require looser or oriented inference
- full-bleed media and pull quotes may break the base grid but should be treated as explicit exceptions, not noise

## Failure patterns
- fake reconstruction through absolute one-off placement
- treating legacy dirt as intentional system logic
- extending a broken layout without normalizing it
- applying a generic 12-column default when the source clearly dictates a different structure

## Hand off to
- `grid-system-expert.md` for fresh layout systems
- `pdf-layout-expert.md` when the source is a PDF
- `document-accessibility-expert.md` when structure/extraction must survive editing
