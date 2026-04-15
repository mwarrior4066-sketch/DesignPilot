# LAUNCH_FRONTEND_IMPLEMENTATION_REVIEW

Use this as the single-file launcher for **Front-End Implementation Review**.

## Startup path
- Default mode: profile-only or full
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_frontend_architecture`
- Use when: Use when the governing decision is front-end architecture rather than generic handoff or UI critique.
- Visual input supported: no
- Known tension: server-first performance vs client-side flexibility
- Known tension: semantic integrity vs custom-widget ambition
- Known tension: optimistic speed vs rollback safety
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_component_spec`

## Included skill logic
- Governing: `front-end-architecture-expert.md` - Use this skill for production-level front-end architecture decisions: rendering model, server and client boundaries, state ownership, mutation strategy, semantic structure, accessibility behavior at the system layer, and performance cost.
- Governing: `front-end-handoff-expert.md` - Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.
- Governing: `accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.
- Optional support: `component-systems-expert.md` - Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.
- Optional support: `back-end-aware-planner.md` - Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.

## Runtime summaries
- `dist/runtime/summaries/front-end-architecture-summary.md`
- `dist/runtime/summaries/front-end-handoff-summary.md`
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`
- `dist/runtime/summaries/component-systems-summary.md`
- `dist/runtime/summaries/backend-planning-summary.md`
- `dist/runtime/summaries/back-end-systems-architecture-summary.md`
- `dist/runtime/summaries/api-reliability-security-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Architectural framing  (Name the real front-end architectural problem and its user-facing consequence.)
  ## Boundary and state model  (Make server/client and state ownership explicit.)
  ## Rendering and mutation strategy  (Choose rendering, fetching, and mutation handling instead of generic implementation advice.)
  ## Risks and safer path  (Expose the cost surface and safer implementation order.)

- Required section: Architectural framing
- Required section: Boundary and state model
- Required section: Rendering and mutation strategy
- Required section: Risks and safer path
- Required evidence: rendering rule
- Required evidence: state model
- Required evidence: implementation constraint
- Required decision: rendering_model
- Required decision: state_ownership
- Required decision: boundary_placement
- Required decision: semantic_contract
- Required decision: cost_or_degraded_path
- Hard fail signal: just convert it to react
- Hard fail signal: componentize it later
- Hard fail signal: use more hooks
- Soft fail signal: should be simple
- Soft fail signal: probably fine

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Front-End Implementation Review. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
