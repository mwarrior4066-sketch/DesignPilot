# layout_reconstruction_plan

**Title:** Layout Reconstruction Plan

## Required sections
- Source constraints
- Reconstruction assumptions
- Rebuild sequence
- Verification checkpoints

## Required evidence types
- grid inference
- preservation boundary
- verification checkpoint

## Required decisions
- preserved_elements
- inference_boundary
- reconstruction_order
- verification_method
- visual_confidence_boundary

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- redraw it from scratch
- eyeball the spacing
- just clean it up

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- approximate it
- close enough

## Execution boundaries
- Lightweight supported: no
- Default weight: `compound`
- Allowed modes: REBUILD, PEER
- Allowed phases: implementation, structure

## Canonical source
- `src/schemas/task_contracts.json#layout_reconstruction_plan`
