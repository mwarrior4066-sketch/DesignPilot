# component_spec

**Title:** Component Specification

## Required sections
- Purpose and scope
- Anatomy
- State matrix
- Accessibility and implementation notes

## Required evidence types
- state rule
- aria or keyboard rule
- implementation boundary

## Required decisions
- component_boundary
- state_coverage
- accessibility_behavior
- implementation_boundary

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- states TBD
- accessibility later

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- basic component
- simple usage

## Execution boundaries
- Lightweight supported: yes
- Default weight: `standard`
- Allowed modes: REBUILD, PEER
- Allowed phases: specs, ui

## Canonical source
- `src/schemas/task_contracts.json#component_spec`
