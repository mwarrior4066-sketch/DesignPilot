# API Reliability and Security Review Example
Fixture: tests/fixtures/api-reliability-security-review.prompt.md
Validation result: tests/evals/api-reliability-security-review.eval.json

## Input Prompt
Audit this API design for reliability and security. It currently returns 200 with an error field, retries POST exports with no Idempotency-Key, and runs large PDF generations synchronously even when they exceed a minute.

## Selected Route and Loaded Skills
- Route: `rt_api_reliability_security`
- Task contract: `api_reliability_security_review`
- Mode: AUDIT
- Phase: implementation
- Skills: `api-reliability-security-expert.md`, `back-end-systems-architect.md`, `back-end-aware-planner.md`
- Known tensions: strict safety vs fast delivery, synchronous convenience vs retry-safe async workflows

## Final Output
### Failure semantics
The current API is failing at the contract layer. Returning `200 OK` with an embedded error field prevents clients and agents from reasoning about failure correctly. Replace that with an RFC 9457 Problem Details envelope using `application/problem+json`, with explicit `type`, `title`, `status`, `detail`, and `instance` members. That gives the client a machine-readable failure profile and keeps logs, retries, and support traces consistent.

For long export failures, add an instance or request identifier that links the failed call back to a trace and audit record. The tradeoff is a slightly stricter error surface for clients, but that strictness should win because it prevents silent contract drift.

### Authorization and resource protection
The design must assume BOLA and BFLA risk anywhere a client-supplied object identifier or method switch can cross a privilege boundary. A report export endpoint should verify object-level authorization on the export target, not just trust that the caller is authenticated. Administrative routes should also be deny by default and protected separately so a method change from GET to DELETE or POST cannot bypass function-level policy.

Because export and PDF generation are expensive, add quotas and timeout budgets per actor or tenant. Costly AI or document-generation endpoints are resource-protection problems as much as they are performance problems.

### Idempotency and async lifecycle
Retrying POST exports without an Idempotency-Key is unsafe. The client should generate the Idempotency-Key, and the server should pair it with a request fingerprint so the same key cannot be reused for a different payload. If the original export is still running, return `409 Conflict` and a retry hint. If the same key is reused for a different fingerprint, return `422 Unprocessable Content`. If the key is mandatory and missing, return `400 Bad Request`.

A PDF generation that exceeds a normal interactive budget should not remain synchronous. Move it to a `202 Accepted` workflow with a status URL. The job lifecycle should be explicit: queued, running, terminal success, or terminal failure. That lets the client poll or subscribe to a signed webhook rather than guess whether the long request failed or merely timed out.

### Resilience and observability
Add retry with backoff and jitter only for transient faults. Pair that with a circuit breaker so repeated downstream failures do not create tool thrash or retry storms. During saturation, apply load shedding and graceful degradation so critical workflows survive while low-priority jobs are delayed or rejected.

Finally, propagate a `trace_id` across the gateway, job worker, and export service. Reliability claims without trace propagation, quota visibility, and status telemetry are too soft to trust.

## Why This Passed
- It makes the structured problem-details contract explicit.
- It names BOLA and BFLA style perimeter risks instead of generic security advice.
- It defines idempotency-key, fingerprint, 409, 422, and 202 Accepted behavior.
- It names resilience and observability patterns that match the workload risk.

## What Would Have Failed
- Saying to just retry the export until it works.
- Keeping 200 responses with hidden failure objects.
- Calling the API reliable without quotas, trace_id propagation, or async lifecycle design.

## Revision Pass
The weak draft only recommended better retries and stronger auth. The corrected version turned the review into explicit contracts for failure, authorization, idempotency, async jobs, resilience, and observability.
