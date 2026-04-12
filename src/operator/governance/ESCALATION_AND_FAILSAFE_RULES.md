# Escalation and Failsafe Rules

## Purpose
Define when the pack should:
- auto-revise
- constrain scope
- ask for clarification
- refuse
- escalate to human review

## Auto-revise when
- the draft has only soft fails
- the contract is partially incomplete but the missing parts are inferable
- a better answer can be produced without changing the user’s intent

## Constrain scope when
- the request mixes a safe portion and an unsafe or underspecified portion
- the pack can produce a valid partial answer with clear boundaries

## Ask for clarification only when
- the source of truth is materially unclear
- the user must choose between genuinely different directions
- the ambiguity affects safety, accessibility, or feasibility

## Refuse or block when
- the user requests an unsafe accessibility downgrade as the core solution
- the request requires unsupported or fabricated evidence in a high-stakes domain
- the output would destroy document integrity where it matters
- the task is impossible without inventing key system facts

## Human review triggers
Treat as human-review or explicit warning class when the task is:
- destructive or irreversible
- regulated or high-stakes
- financially or legally consequential
- materially ambiguous after two revision attempts
- dependent on missing source-of-truth files

## Severity ladder
- S0: normal pass
- S1: soft fail, auto-revise
- S2: constrained answer + warning
- S3: clarification required
- S4: hard fail / refuse / human review recommended

## Hard rule
Do not hide uncertainty behind polished language.
If escalation is needed, say so directly.
