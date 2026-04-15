# color_system_spec

**Title:** Color System Specification

## Required sections
- Role model
- Token map
- Contrast and state rules
- Migration notes

## Required evidence types
- semantic role
- contrast threshold
- state rule

## Required decisions
- semantic_roles
- state_mapping
- contrast_boundary
- migration_strategy

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- pick nicer colors
- brand color everywhere
- palette only

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- could feel fresher
- more vibrant maybe

## Execution boundaries
- Lightweight supported: yes
- Default weight: `standard`
- Allowed modes: REBUILD, PEER
- Allowed phases: tokens, ui

## Canonical source
- `src/schemas/task_contracts.json#color_system_spec`
