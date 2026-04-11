# Layout Reconstruction Plan Example
Fixture: tests/fixtures/layout-reconstruction-pass.prompt.md
Validation result: tests/evals/layout-reconstruction-pass.eval.json

## Input Prompt
Create a reconstruction plan for a legacy brochure spread where the original working files are gone. Preserve the current image placements and caption order, but recover a clean grid and verify that the rebuilt layout still matches the source.

## Selected Route and Loaded Skills
- Route: `rt_layout_reconstruction_plan`
- Task contract: `layout_reconstruction_plan`
- Mode: REBUILD
- Phase: implementation
- Skills: `layout-reconstruction-expert.md`, `grid-system-expert.md`
- Known tensions: exact preservation vs practical reconstruction, speed vs verification rigor

## Final Output
### Source constraints
The source spread is the truth for image placements, caption order, and overall reading sequence. Those elements should remain locked. The reconstruction can clarify the grid, but it should not quietly redesign the artifact or normalize geometry that belongs to the original composition.

### Reconstruction assumptions
- The original file likely used a repeated underlying column structure even though guides are gone.
- Gutter width and baseline spacing will need to be inferred from repeated edge relationships. That is an estimate, not a certainty.
- Any alignment that cannot be supported by multiple repeated anchors should be labeled as an inference rather than source truth.

### Rebuild sequence
- First, capture measurements from the source and place an overlay so preserved elements can be compared later.
- Then infer the likely grid from repeated image edges, caption starts, and margin intervals.
- Next, rebuild the spread using locked image boxes and caption order before touching any secondary cleanup.
- After that, normalize only the gaps that can be justified by the inferred grid. The tradeoff is geometric neatness versus preservation. Preservation should win whenever the source and the inferred system disagree.
- Finally, document every estimated spacing rule so later edits do not mistake inference for exact source truth.

### Verification checkpoints
Verify the rebuilt spread with an overlay comparison, measurement checks on preserved elements, and an extraction check for caption order. The obvious alternative is to adjust gaps by feel until the spread looks cleaner, but that would break the reconstruction brief and hide whether preservation actually survived.

## Why This Passed
- It distinguishes source truth from inferred structure.
- It gives a measured reconstruction sequence instead of redrawing from scratch.
- It uses overlay, measurement, and comparison as verification methods.
- It resolves the tradeoff in favor of preservation when the grid inference conflicts with the original artifact.

## What Would Have Failed
- Treating the spread as a redesign opportunity.
- Claiming an exact match without a comparison method.
- Hiding assumptions about the inferred grid.

## Revision Pass
The weak draft proposed rebuilding the spread on a cleaner modern grid and adjusting image sizes by intuition. The corrected version protected the source artifact first and labeled inference explicitly.
