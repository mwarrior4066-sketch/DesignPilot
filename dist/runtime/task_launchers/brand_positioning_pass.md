# LAUNCH_BRAND_POSITIONING_PASS

Use this as the single-file launcher for **Brand Positioning Pass**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_BRAND.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_brand_positioning`
- Use when: Use when the system must decide who the brand is for and how it earns trust.
- Visual input supported: no
- Known tension: distinctiveness vs usability
- Known tension: expressive tone vs credibility
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_case_study_rewrite`

## Included skill logic
- Governing: `brand-strategy-expert.md` - Use this skill to make strict positioning, audience-fit, trust-signal, convention, and brand-vs-interface decisions. Treat brand work as a system of falsifiable hypotheses, not a moodboard.
- Governing: `content-and-case-study-expert.md` - Use this skill to audit, rewrite, expand, or structure UX copy, design rationale, documentation, and case-study writing without losing clarity, mode control, or evidence.
- Optional support: `ux-research-expert.md` - Use this skill to frame the problem, identify the user, surface cognitive/ergonomic constraints, and keep work tied to real needs instead of surface styling.

## Runtime summaries
- `dist/runtime/summaries/audience-and-industry-summary.md`
- `dist/runtime/summaries/writing-and-case-study-summary.md`
- `dist/runtime/summaries/ux-roadmap-summary.md`
- `dist/runtime/summaries/ux-cognition-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Audience and problem  (Anchors brand to a real segment and pain.)
  ## Positioning frame  (Shows category, alternative, and wedge.)
  ## Trust and proof burden  (Prevents adjective-only branding.)
  ## Messaging consequences  (Translates strategy into language behavior.)

- Required section: Audience and problem
- Required section: Positioning frame
- Required section: Trust and proof burden
- Required section: Messaging consequences
- Required evidence: segment proof
- Required evidence: differentiation logic
- Required evidence: trust signal
- Required decision: audience_frame
- Required decision: differentiation_frame
- Required decision: trust_logic
- Required decision: messaging_consequence
- Hard fail signal: best-in-class brand
- Hard fail signal: premium modern innovative
- Soft fail signal: strong brand presence

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Brand Positioning Pass. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
