# pdf_remediation_plan

**Title:** PDF Remediation Plan

## Required sections
- Current failure state
- Remediation sequence
- Verification checks
- Risk controls

## Required evidence types
- tagging rule
- reading-order rule
- verification method

## Required decisions
- semantic_failure
- reading_order_or_extraction
- verification_method
- destructive_shortcut_rejected

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- flatten the pdf
- rasterize the page
- just use OCR only

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- make it accessible somehow

## Execution boundaries
- Lightweight supported: no
- Default weight: `compound`
- Allowed modes: AUDIT, REBUILD, PEER
- Allowed phases: structure, specs, implementation

## Canonical source
- `src/schemas/task_contracts.json#pdf_remediation_plan`
