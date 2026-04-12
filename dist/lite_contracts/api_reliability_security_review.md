# api_reliability_security_review

**Title:** API Reliability and Security Review

## Required sections
- Failure semantics
- Authorization and resource protection
- Idempotency and async lifecycle
- Resilience and observability

## Required evidence types
- problem details
- idempotency contract
- resilience policy

## Required decisions
- problem_details_contract
- authorization_perimeter
- idempotency_contract
- async_job_model
- resilience_strategy

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- just retry it
- rate limit later
- return 200 with an error field
- uuid makes it secure

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- should be reliable
- probably secure

## Execution boundaries
- Lightweight supported: no
- Default weight: `compound`
- Allowed modes: AUDIT, PEER, STRUCTURE
- Allowed phases: implementation, specs, strategy

## Canonical source
- `src/schemas/task_contracts.json#api_reliability_security_review`
