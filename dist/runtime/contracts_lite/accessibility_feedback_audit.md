# accessibility_feedback_audit

**Title:** Accessibility Feedback Audit

## Required sections
- Access failure framing
- Barrier inventory
- Repair priorities
- Verification method

## Required evidence types
- standards rule
- interaction behavior
- verification method

## Required decisions
- blocked_user_action
- priority_order
- behavior_rule
- verification_step

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- accessibility later
- screen reader later
- just make focus blue

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- probably accessible
- seems fine

## Execution boundaries
- Lightweight supported: yes
- Default weight: `standard`
- Allowed modes: AUDIT, PEER
- Allowed phases: accessibility, ui

## Canonical source
- `src/schemas/task_contracts.json#accessibility_feedback_audit`
