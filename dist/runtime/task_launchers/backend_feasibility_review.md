# LAUNCH_BACKEND_FEASIBILITY_REVIEW

Use this as the single-file launcher for **Back-End Feasibility Review**.

## Startup path
- Default mode: profile-only or full
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_backend_feasibility`
- Use when: Reveal back-end implications before treating the request as visual-only.
- Visual input supported: no
- Known tension: speed vs correctness
- Known tension: frontend promise vs backend feasibility
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_component_spec`

## Included skill logic
- Governing: `back-end-aware-planner.md` - Use this skill as a strict feasibility control plane between product or design intent and engineering reality. It translates visual or workflow requests into explicit requirements for actors, permissions, data models, APIs, storage, exports, background jobs, observability, and degraded modes. It is the gate, not the deep architecture owner.
- Governing: `front-end-handoff-expert.md` - Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.
- Optional support: `component-systems-expert.md` - Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.

## Runtime summaries
- `dist/runtime/summaries/backend-planning-summary.md`
- `dist/runtime/summaries/back-end-systems-architecture-summary.md`
- `dist/runtime/summaries/api-reliability-security-summary.md`
- `dist/runtime/summaries/front-end-handoff-summary.md`
- `dist/runtime/summaries/front-end-architecture-summary.md`
- `dist/runtime/summaries/component-systems-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Requested capability  (States the visible ask and hidden system implications.)
  ## Hidden system requirements  (Maps UI ask to auth, storage, exports, or APIs.)
  ## Feasibility assessment  (Calls out blockers, assumptions, and sequencing.)
  ## Safer implementation path  (Shows a realistic build order.)

- Required section: Requested capability
- Required section: Hidden system requirements
- Required section: Feasibility assessment
- Required section: Safer implementation path
- Required evidence: auth rule
- Required evidence: data model need
- Required evidence: integration risk
- Required decision: data_dependency
- Required decision: permissions_dependency
- Required decision: system_surface_dependency
- Required decision: blocking_constraint
- Hard fail signal: purely visual change
- Hard fail signal: no backend impact
- Soft fail signal: should be straightforward

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Back-End Feasibility Review. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
