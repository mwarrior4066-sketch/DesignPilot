# API Reliability and Security Review Template

## Failure semantics
- problem-details contract
- success vs failure envelope rule
- correlation or instance identifier

## Authorization and resource protection
- actor and object boundary
- object-level authorization
- function-level authorization
- quotas, limits, or rate controls

## Retry safety and async lifecycle
- idempotency-key ownership
- fingerprint and expiry logic
- in-flight collision behavior
- 202/status resource or webhook lifecycle

## Resilience and observability
- retry and timeout policy
- circuit breaker or graceful degradation
- trace propagation
- verification or incident-readiness note
