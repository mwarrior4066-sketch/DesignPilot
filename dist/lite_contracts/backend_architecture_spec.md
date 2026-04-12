# backend_architecture_spec

**Title:** Back-End Architecture Spec

## Required sections
- System framing
- Core model and authority boundaries
- Data, consistency, and delivery design
- Observability and failure posture

## Required evidence types
- authority model
- consistency stance
- delivery pattern

## Required decisions
- actor_resource_action
- source_of_truth
- authorization_model
- consistency_stance
- delivery_pattern
- observability_tax

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- just add an endpoint
- make it realtime
- use uuid and it is secure

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- should scale fine
- probably okay

## Execution boundaries
- Lightweight supported: no
- Default weight: `compound`
- Allowed modes: STRUCTURE, PEER, REBUILD
- Allowed phases: strategy, specs, implementation

## Canonical source
- `src/schemas/task_contracts.json#backend_architecture_spec`
