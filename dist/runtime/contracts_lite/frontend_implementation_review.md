# frontend_implementation_review

**Title:** Front-End Implementation Review

## Required sections
- Architectural framing
- Boundary and state model
- Rendering and mutation strategy
- Risks and safer path

## Required evidence types
- rendering rule
- state model
- implementation constraint

## Required decisions
- rendering_model
- state_ownership
- boundary_placement
- semantic_contract
- cost_or_degraded_path

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- just convert it to react
- componentize it later
- use more hooks

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- should be simple
- probably fine

## Execution boundaries
- Lightweight supported: no
- Default weight: `compound`
- Allowed modes: AUDIT, PEER, STRUCTURE
- Allowed phases: implementation, ui, specs

## Canonical source
- `src/schemas/task_contracts.json#frontend_implementation_review`
