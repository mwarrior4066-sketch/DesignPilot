# Runtime Validation Layer

This file defines the mandatory validation gate that runs after drafting and before final output.

## Purpose
Turn the pack from a reasoning system into a checked-output system.
Do not trust a draft just because the reasoning path looked plausible.

## Run order
Run this after:
1. mode detection
2. phase detection
3. task routing
4. draft generation

Run this before:
1. final user-facing output
2. artifact export
3. high-risk implementation guidance

## Validation flow
### Gate 1. mode validation
Check that the output matches the active mode.
- AUDIT must diagnose, not rebuild
- REBUILD must rebuild, not only critique
- EXPAND must deepen without replacing the core logic
- STRUCTURE must reorganize first
- STYLE GUIDE must output rules, constraints, usage notes, and exceptions
- RAPID ITERATION must stay short and must exit if the task becomes strategic, structural, or risky

Hard fail if the mode is clearly wrong.

### Gate 2. phase validation
Check that the output does not skip the roadmap without naming the risk.
Hard fail if the output presents final production work as valid when the necessary upstream phase is missing.
Soft fail if the output can be salvaged by adding a gate warning and constraining the recommendation.

### Gate 3. pathway validation
Check that the loaded pathway is the smallest correct one.
Hard fail if the answer ignores an essential specialist domain.
Examples:
- dashboard answer without dashboard skill logic
- PDF answer without document accessibility when tags/extraction matter
- front-end answer without accessibility/state implementation when interactive behavior is involved

### Gate 4. output contract validation
Validate against `OUTPUT_CONTRACTS_BY_TASK.md`.
Hard fail if required sections are missing.
Soft fail if the answer is structurally correct but underspecified.

### Gate 5. domain validation
Run the relevant domain validator from `DOMAIN_VALIDATORS.md`.
Hard fail on accessibility, document integrity, impossible feasibility, or unreadable typography/color.
Soft fail on weak hierarchy, thin evidence, or under-specified implementation.

### Gate 6. evidence and provenance validation
Check that the output contains the minimum evidence artifact for the task.
- strategy: positioning logic, audience logic, trust burden, or explicit hypothesis language
- technical: thresholds, rules, constraints, or feasibility rationale
- case study: problem, process, solution, outcome, and rationale/evidence links
Hard fail if the output makes strong claims without support in a high-stakes context.

### Gate 7. contradiction validation
Check for internal contradictions.
Examples:
- minimal dashboard + 40 metrics on one view
- brand color + inaccessible contrast
- luxury styling + institutional trust requirement
- shrink text to fit + readability floor
Hard fail if the output carries both sides forward without resolving them.

### Gate 8. pass / revise / escalate decision
- PASS: all hard gates pass and weighted score meets threshold
- AUTO-REVISE: no hard fail, but score is below target or one or more soft fails exist
- ESCALATE: hard fail involving irreversible, regulated, destructive, or materially ambiguous work

## Auto-revision rules
A draft may self-revise up to 2 times.
After 2 failed revisions:
- downgrade scope
- state the blocker clearly
- ask only the smallest necessary clarification if needed

Do not enter infinite critic loops.

## Hard-fail triggers
Always hard fail when the output:
- violates accessibility minimums by default
- destroys PDF/document structure when document behavior matters
- recommends unreadable text or inaccessible color as the primary solution
- invents implementation precision with missing system context
- makes unsupported compliance, security, medical, financial, or superiority claims
- ignores a clear roadmap gate
- uses the wrong mode for the user’s request

## Output of the validator
The validator should produce an internal object with:
- mode_status
- phase_status
- pathway_status
- contract_status
- domain_status
- evidence_status
- contradiction_status
- score
- decision
- revision_notes

Do not show the full object to the user unless explicitly asked.
