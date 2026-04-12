# ui_structure_critique

**Title:** UI Structure Critique

## Required sections
- Problem framing
- Findings
- Recommendations
- Tradeoffs

## Required evidence types
- task logic
- hierarchy rule
- layout constraint

## Required decisions
- structural_failure
- hierarchy_winner
- intervention_order
- tradeoff_resolution
- visual_confidence_boundary

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- looks great as-is
- just make it prettier
- finalize the UI now

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- could maybe
- might want to consider

## Execution boundaries
- Lightweight supported: yes
- Default weight: `standard`
- Allowed modes: AUDIT, PEER
- Allowed phases: structure, ui

## Canonical source
- `src/schemas/task_contracts.json#ui_structure_critique`
