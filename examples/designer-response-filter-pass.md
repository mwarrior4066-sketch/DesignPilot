# Designer Response Filter Pass
Fixture: tests/fixtures/designer-response-filter-pass.prompt.md
Validation result: tests/evals/designer-response-filter-pass.eval.json

## Input Prompt
Transform a backend architecture explanation into a designer-readable answer for an Integrative-tier user without weakening the system constraints.

## Selected Route and Loaded Skills
- Route: `rt_api_reliability_security`
- Task contract: `api_reliability_security_review`
- Mode: FILTER
- Phase: revision
- Skills: `api-reliability-security-expert.md`, `front-end-handoff-expert.md`

## Final Output
# API Reliability and Security Review
## POST /api/v1/projects/{id}/members

## Failure semantics

The endpoint currently returns 200 with the updated member list on success, and a plain string on failure. This conflates success and failure into a single status code, which forces clients to parse text and guess at retryability.

**Decision: adopt RFC 9457 Problem Details** (`application/problem+json`) for all error responses. Return `400 Bad Request` for invalid user IDs, `403 Forbidden` for authorization failures, `409 Conflict` for duplicate membership, and `500 Internal Server Error` for transient failures. Each error must include `type`, `title`, `status`, `detail`, and `instance` fields. The client can then determine whether to retry (5xx), fail silently (4xx), or surface a user-visible message -- without string parsing.

## Authorization and resource protection

The current authorization check confirms the caller is logged in but does not verify they are a project admin. This is a **BOLA** (Broken Object-Level Authorization) vulnerability: any authenticated user can add themselves or others to any project they know the ID of, regardless of whether they own or administer it.

**Decision: enforce object-level authorization before mutation.** Before executing the add-member operation, verify that `caller.id` holds an `admin` or `owner` relationship on `project.id`. Deny by default -- if no explicit relationship exists, return `403 Forbidden`. Do not rely on opaque or unguessable project IDs as a security boundary; these are not authorization. A **BFLA** (Broken Function-Level Authorization) check is also required: the ability to read a project's member list must not imply the ability to modify it. Read and write permissions must be independently checked.

## Idempotency and async lifecycle

The endpoint accepts POST requests with no `Idempotency-Key` header. If a client retries after a network timeout, the member may be added twice -- or the second request may return a 4xx error if the first succeeded, leaving the client unable to distinguish success from failure.

**Decision: require a client-generated `Idempotency-Key` header (UUID).** On the first request, execute the mutation and store `(key, response)` in a short-lived cache (24-hour TTL). On a retry with the same key, return the cached response without re-executing. On a duplicate key with a different request body, return `409 Conflict` -- not retryable. Return `201 Created` on initial success with a `Location` header. If member provisioning involves external systems, return `202 Accepted` with a status URL for polling; clients poll until terminal state (`queued` -> `running` -> `completed` | `failed`).

## Resilience and observability

The endpoint currently returns no `trace_id`, no rate-limit headers, and no partial-success signaling. An operator cannot correlate a client error report to a server log without a shared identifier.

**Decision: add `trace_id` to all responses** via the RFC 9457 `instance` field or a `Trace-ID` header. Add `RateLimit-Limit`, `RateLimit-Remaining`, and `RateLimit-Reset` headers. For quota violations return `429 Too Many Requests` with a `Retry-After` header. The tradeoff: adding headers increases response size marginally; the benefit is full observability and safe client backoff behavior -- without trace_id, debugging any production failure requires a full timestamp-based log search. For quota violations, graceful degradation means returning a structured 429 rather than silently dropping requests or returning a 500.

---

<!-- route: api_reliability_security_review | mode: AUDIT | phase: review -->

**Alternative approach considered:** accepting the current 200-for-all pattern and wrapping it in a client-side adapter layer. This is rather than fixing the server contract because the client adapter is cheaper short-term. The tradeoff is that every client must independently implement the adapter, error handling diverges across clients, and monitoring tools remain blind to server-side error rates. Fixing the server contract once is safer than distributing the workaround to every consumer.
