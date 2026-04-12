# backend_feasibility_review

**Title:** Back-End Feasibility Review

## Required sections
- Requested capability
- Hidden system requirements
- Feasibility assessment
- Safer implementation path

## Required evidence types
- auth rule
- data model need
- integration risk

## Required decisions
- data_dependency
- permissions_dependency
- system_surface_dependency
- blocking_constraint

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- purely visual change
- no backend impact

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- should be straightforward

## Execution boundaries
- Lightweight supported: no
- Default weight: `compound`
- Allowed modes: AUDIT, PEER, STRUCTURE
- Allowed phases: strategy, specs

## Canonical source
- `src/schemas/task_contracts.json#backend_feasibility_review`
