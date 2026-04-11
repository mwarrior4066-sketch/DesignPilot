---
runtime_card_version: 1.0.0
canonical_skill: skills/layout-reconstruction-expert.md
last_generated: 2026-04-11
overlay: true
---
# layout-reconstruction-expert.md

## Activation conditions
- the task is about extending an existing layout
- the user wants a new section added to an established structure
- the grid must be inferred from a source rather than chosen fresh
- the source is dirty or inconsistent and needs normalization
- the task is clearly a new layout with no source structure to preserve
- the request is only abstract grid education

## Non-activation conditions
- the task is clearly a new layout with no source structure to preserve
- the request is only abstract grid education

## Core decision rules
- infer the latent layout model before placing anything new
- preserve the stable structure and normalize the dirt
- treat explicit off-grid exceptions as exceptions, not the default logic
- state confidence when inference is ambiguous

## Failure traps
- absolute-position imitation with no inferred system
- preserving accidental dirt as if it were intentional design logic
- applying a generic 12-column system when the source clearly does not support it
- extending a layout without a confidence note when the inference is weak

## Summary dependencies
- layout-reconstruction-summary.md

## Escalation triggers
- posters or rotated layouts may require oriented inference rather than rectangular column logic
- some legacy layouts are better treated as manuscript systems with local subgrids than as strict multi-column systems
- if inference is weak, choose the smallest safe model and state the fallback
- if the source clearly fights itself, normalize the core rhythm before extending it
- if no stable grid can be inferred, hand off to `grid-system-expert.md` for a new-layout recommendation
- inferred grid or manuscript model
- normalization rule
- tolerance or alignment rule

## Adjacent handoff rules
- hand off to `grid-system-expert.md` for fresh grid design
- hand off to `pdf-layout-expert.md` when frame logic or PDF editing is involved
- hand off to `document-accessibility-expert.md` when structural semantics must survive the edit

## Canonical fallback
- `skills/layout-reconstruction-expert.md`
- `knowledge-base/summaries/layout-reconstruction-summary.md`