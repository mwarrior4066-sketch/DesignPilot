# LAUNCH_BACKEND_ARCHITECTURE_SPEC

Use this as the single-file launcher for **Back-End Architecture Spec**.

## Startup path
- Default mode: profile-only or full
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_backend_systems_architecture`
- Use when: Use when the governing decision is the structure of the backend system itself.
- Visual input supported: no
- Known tension: consistency vs latency
- Known tension: real-time freshness vs replayable sanity
- Known tension: authority precision vs implementation complexity
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_backend_feasibility`

## Included skill logic
- Governing: `back-end-systems-architect.md` - Use this skill for deeper system-architecture work beyond feasibility: authority boundaries, authorization model, consistency stance, pagination, async events, webhooks, multi-tenancy, and observability.
- Governing: `back-end-aware-planner.md` - Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.
- Governing: `api-reliability-security-expert.md` - Use this skill when the answer depends on structured failures, authorization perimeters, retry safety, async job lifecycles, resilience patterns, quotas, or telemetry across API and tool boundaries.
- Optional support: `dashboard-data-expert.md` - Use this skill to make production-level decisions about dashboard type, KPI hierarchy, chart choice, density, filters, drill-down, and dense-data readability.
- Optional support: `front-end-handoff-expert.md` - Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.

## Runtime summaries
- `dist/runtime/summaries/back-end-systems-architecture-summary.md`
- `dist/runtime/summaries/backend-planning-summary.md`
- `dist/runtime/summaries/api-reliability-security-summary.md`
- `dist/runtime/summaries/dashboard-and-density-summary.md`
- `dist/runtime/summaries/front-end-handoff-summary.md`
- `dist/runtime/summaries/front-end-architecture-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## System framing  (Names the system, actors, resources, and why architecture is needed.)
  ## Core model and authority boundaries  (Defines ownership, authorization, and source-of-truth.)
  ## Data, consistency, and delivery design  (Chooses consistency, pagination, events, async, or webhook patterns.)
  ## Observability and failure posture  (Shows how the system will be monitored and where it can safely degrade.)

- Required section: System framing
- Required section: Core model and authority boundaries
- Required section: Data, consistency, and delivery design
- Required section: Observability and failure posture
- Required evidence: authority model
- Required evidence: consistency stance
- Required evidence: delivery pattern
- Required decision: actor_resource_action
- Required decision: source_of_truth
- Required decision: authorization_model
- Required decision: consistency_stance
- Required decision: delivery_pattern
- Required decision: observability_tax
- Hard fail signal: just add an endpoint
- Hard fail signal: make it realtime
- Hard fail signal: use uuid and it is secure
- Soft fail signal: should scale fine
- Soft fail signal: probably okay

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Back-End Architecture Spec. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
