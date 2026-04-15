# LAUNCH_API_RELIABILITY_SECURITY_REVIEW

Use this as the single-file launcher for **API Reliability and Security Review**.

## Startup path
- Default mode: profile-only or full
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_api_reliability_security`
- Use when: Use when the governing decision is failure, retry, authorization, or resilience semantics for APIs or tools.
- Visual input supported: no
- Known tension: strict safety vs fast delivery
- Known tension: synchronous convenience vs retry-safe async workflows
- Known tension: graceful degradation vs exact freshness
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_backend_systems_architecture`

## Included skill logic
- Governing: `api-reliability-security-expert.md` - Use this skill when the answer depends on structured failures, authorization perimeters, retry safety, async job lifecycles, resilience patterns, quotas, or telemetry across API and tool boundaries.
- Governing: `back-end-systems-architect.md` - Use this skill for deeper system-architecture work beyond feasibility: authority boundaries, authorization model, consistency stance, pagination, async events, webhooks, multi-tenancy, and observability.
- Governing: `back-end-aware-planner.md` - Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.
- Optional support: `front-end-handoff-expert.md` - Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.
- Optional support: `document-accessibility-expert.md` - Use this skill to preserve or restore document accessibility: tagging, reading order, artifacts, Unicode mapping, OCR remediation, and extraction fidelity.

## Runtime summaries
- `dist/runtime/summaries/api-reliability-security-summary.md`
- `dist/runtime/summaries/back-end-systems-architecture-summary.md`
- `dist/runtime/summaries/backend-planning-summary.md`
- `dist/runtime/summaries/front-end-handoff-summary.md`
- `dist/runtime/summaries/front-end-architecture-summary.md`
- `dist/runtime/summaries/pdf-document-accessibility-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Failure semantics  (Defines the error envelope and what the client can reason about.)
  ## Authorization and resource protection  (Names BOLA/BFLA style boundaries and resource controls.)
  ## Idempotency and async lifecycle  (Makes retry safety and long-running job behavior explicit.)
  ## Resilience and observability  (Names resilience, quotas, degradation, and telemetry posture.)

- Required section: Failure semantics
- Required section: Authorization and resource protection
- Required section: Idempotency and async lifecycle
- Required section: Resilience and observability
- Required evidence: problem details
- Required evidence: idempotency contract
- Required evidence: resilience policy
- Required decision: problem_details_contract
- Required decision: authorization_perimeter
- Required decision: idempotency_contract
- Required decision: async_job_model
- Required decision: resilience_strategy
- Hard fail signal: just retry it
- Hard fail signal: rate limit later
- Hard fail signal: return 200 with an error field
- Hard fail signal: uuid makes it secure
- Soft fail signal: should be reliable
- Soft fail signal: probably secure

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for API Reliability and Security Review. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
