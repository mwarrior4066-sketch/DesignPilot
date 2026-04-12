# type_system_recommendation

**Title:** Type System Recommendation

## Required sections
- Reading context
- Scale and role map
- Readability rules
- Adoption guidance

## Required evidence types
- readability rule
- role map
- adoption boundary

## Required decisions
- reading_context
- role_hierarchy
- readability_boundary
- adoption_sequence

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- use inter at 12px
- just tighten tracking
- pick a nicer font

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- feels too loose
- could be sharper

## Execution boundaries
- Lightweight supported: yes
- Default weight: `standard`
- Allowed modes: REBUILD, PEER
- Allowed phases: tokens, communication, ui

## Canonical source
- `src/schemas/task_contracts.json#type_system_recommendation`
