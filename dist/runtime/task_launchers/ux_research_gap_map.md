# LAUNCH_UX_RESEARCH_GAP_MAP

Use this as the single-file launcher for **UX Research Gap Map**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_BRAND.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_ux_research_gap_map`
- Use when: Use when the answer must separate known evidence from assumptions and map the next studies.
- Visual input supported: no
- Known tension: research depth vs team speed
- Known tension: breadth of curiosity vs decision-critical unknowns
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_brand_positioning`

## Included skill logic
- Governing: `ux-research-expert.md` - Use this skill to frame the problem, identify the user, surface cognitive/ergonomic constraints, and keep work tied to real needs instead of surface styling.
- Governing: `content-and-case-study-expert.md` - Use this skill to audit, rewrite, expand, or structure UX copy, design rationale, documentation, and case-study writing without losing clarity, mode control, or evidence.
- Optional support: `brand-strategy-expert.md` - Use this skill to make strict positioning, audience-fit, trust-signal, convention, and brand-vs-interface decisions. Treat brand work as a system of falsifiable hypotheses, not a moodboard.

## Runtime summaries
- `dist/runtime/summaries/ux-roadmap-summary.md`
- `dist/runtime/summaries/ux-cognition-summary.md`
- `dist/runtime/summaries/writing-and-case-study-summary.md`
- `dist/runtime/summaries/audience-and-industry-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Known evidence  (Separates what is already known from assumption.)
  ## Critical gaps  (Names the highest-risk unknowns that block good decisions.)
  ## Research plan  (Maps each gap to a method, sample, and output.)
  ## Decision impact  (Shows what product or narrative decision each study unlocks.)

- Required section: Known evidence
- Required section: Critical gaps
- Required section: Research plan
- Required section: Decision impact
- Required evidence: research artifact
- Required evidence: gap priority
- Required evidence: decision linkage
- Required decision: known_vs_unknown
- Required decision: gap_priority
- Required decision: method_mapping
- Required decision: decision_linkage
- Hard fail signal: just do some interviews
- Hard fail signal: research later
- Hard fail signal: talk to users
- Soft fail signal: probably enough
- Soft fail signal: might learn something

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for UX Research Gap Map. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
