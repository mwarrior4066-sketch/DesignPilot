# text_humanization_revision

**Title:** Text Humanization Revision

## Required sections
- Job of the piece
- Pattern scan
- Meaning-preservation guard
- Revised passage
- Why this reads more human

## Required evidence types
- meaning guard
- pattern note
- before/after revision rationale

## Required decisions
- job_of_piece
- pattern_scan
- meaning_guard
- revision_sequence
- voice_guard

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- rewrite for difference only
- casualize it more
- make it sound human somehow

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- a bit more natural
- less robotic

## Execution boundaries
- Lightweight supported: yes
- Default weight: `lightweight`
- Allowed modes: REBUILD, PEER, STRUCTURE
- Allowed phases: communication, case-study, implementation

## Canonical source
- `src/schemas/task_contracts.json#text_humanization_revision`
