# PDF Remediation Plan Example
Fixture: tests/fixtures/pdf-remediation-plan.prompt.md
Validation result: tests/evals/pdf-remediation-plan.eval.json

## Input Prompt
Create a remediation plan for a styled report PDF that looks correct visually but fails reading order, table tagging, and copy-paste extraction.

## Selected Route and Loaded Skills
- Route: `rt_pdf_remediation`
- Task contract: `pdf_remediation_plan`
- Mode: REBUILD
- Phase: implementation
- Skills: `document-accessibility-expert.md`, `pdf-layout-expert.md`

## Final Output
### Current failure state
The document is visually coherent but semantically broken. Screen readers will encounter the wrong order, tables will not expose headers correctly, and copied text will degrade because the text layer and structure tree are not aligned. The current failure is structural, not cosmetic, and that means remediation has to protect semantics before appearance.

### Remediation sequence
1. Preserve the current file as the visual reference and work on a controlled copy.
2. Rebuild reading order at the structure-tree level before touching cosmetic layout edits.
3. Correct table scope, header associations, and cell tagging.
4. Repair text extraction fidelity and unicode mapping before adding fallback OCR only where source text is actually missing.
5. Re-run document checks after each major structural correction instead of doing one blind end-of-process pass.

### Verification checks
- Reading order matches the intended narrative sequence.
- Tables expose headers and row relationships.
- Copy-paste output preserves punctuation, ligatures, and line logic.
- Tags reflect artifacts versus real content correctly.
- The visible file remains materially unchanged aside from necessary semantic repair.

### Risk controls
Do not convert the document into a flat image, rasterize pages, or use OCR as the first move because those actions can destroy the recoverable text layer. The tradeoff is speed versus safe preservation. Safe preservation wins because a fast destructive fix would erase the very semantics we need to verify.

## Why This Passed
- The plan separates semantic from cosmetic repair.
- Verification is explicit, not implied.
- Risk controls block destructive shortcuts.
- It includes an explicit tradeoff.

## What Would Have Failed
- “Just OCR the file.”
- Making visual tweaks before fixing the structure tree.
- Calling the file accessible without extraction checks.

## Revision Pass
The weak draft treated clipped extraction as a cosmetic cleanup item. The revision reclassified it as a semantic integrity problem and reordered the remediation sequence around that truth.
