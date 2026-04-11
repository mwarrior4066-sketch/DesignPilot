---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/layout-reconstruction-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: layout-reconstruction
---

# Layout Reconstruction Expert

## Purpose
Use this skill to infer, reconstruct, normalize, and extend existing layouts from screenshots, PDFs, and legacy designs.

## Activate when
- the task is about extending an existing layout
- the user wants a new section added to an established structure
- the grid must be inferred from a source rather than chosen fresh
- the source is dirty or inconsistent and needs normalization

## Do not activate when
- the task is clearly a new layout with no source structure to preserve
- the request is only abstract grid education

## Read these first
- `knowledge-base/summaries/layout-reconstruction-summary.md`
- `knowledge-base/summaries/grid-mediums-summary.md`
- `knowledge-base/summaries/pdf-layout-summary.md` when PDFs are involved

## Decision rules
- infer the latent layout model before placing anything new
- preserve the stable structure and normalize the dirt
- treat explicit off-grid exceptions as exceptions, not the default logic
- state confidence when inference is ambiguous

## Default actions
- identify margins, columns, gutters, and repeated modules
- identify possible baseline or vertical rhythm
- identify exception zones such as full-bleed media or pull quotes
- normalize inconsistent spacing to the nearest defensible rhythm
- extend the layout using the inferred model, not generic placement

## Exception rules
- posters or rotated layouts may require oriented inference rather than rectangular column logic
- some legacy layouts are better treated as manuscript systems with local subgrids than as strict multi-column systems

## Fallback logic
- if inference is weak, choose the smallest safe model and state the fallback
- if the source clearly fights itself, normalize the core rhythm before extending it
- if no stable grid can be inferred, hand off to `grid-system-expert.md` for a new-layout recommendation

## Failure traps
- absolute-position imitation with no inferred system
- preserving accidental dirt as if it were intentional design logic
- applying a generic 12-column system when the source clearly does not support it
- extending a layout without a confidence note when the inference is weak

## Evidence required
Use some combination of:
- inferred grid or manuscript model
- normalization rule
- tolerance or alignment rule
- exception-zone note
- confidence or fallback note

## Handoff to other skills
- hand off to `grid-system-expert.md` for fresh grid design
- hand off to `pdf-layout-expert.md` when frame logic or PDF editing is involved
- hand off to `document-accessibility-expert.md` when structural semantics must survive the edit

## Output expectations
- source-preserving logic
- normalized extension, not guessy imitation
- confidence made explicit when needed

## Added document/presentation rules
- infer page-role architecture in decks and report PDFs: cover, TOC, divider, content, close
- recover the content box, header/footer gap contract, and vertical-fill logic before extending cards or rows
- normalize overshoot lines, floating content, and duplicated chrome labels as structural defects rather than stylistic quirks
- if patching would require repeated manual overrides across many pages, recommend rebuild from a clean grid/token base
