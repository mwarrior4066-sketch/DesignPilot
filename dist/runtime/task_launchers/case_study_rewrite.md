# LAUNCH_CASE_STUDY_REWRITE

Use this as the single-file launcher for **Case Study Rewrite**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_BRAND.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_case_study_rewrite`
- Use when: Use when communication quality depends on narrative order and proof clarity, not just editing.
- Visual input supported: no
- Known tension: story flow vs proof density
- Known tension: confidence vs honesty about open gaps
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_brand_positioning`

## Included skill logic
- Governing: `content-and-case-study-expert.md` - Use this skill to audit, rewrite, expand, or structure UX copy, design rationale, documentation, and case-study writing without losing clarity, mode control, or evidence.
- Optional support: `brand-strategy-expert.md` - Use this skill to make strict positioning, audience-fit, trust-signal, convention, and brand-vs-interface decisions. Treat brand work as a system of falsifiable hypotheses, not a moodboard.
- Optional support: `ux-research-expert.md` - Use this skill to frame the problem, identify the user, surface cognitive/ergonomic constraints, and keep work tied to real needs instead of surface styling.

## Runtime summaries
- `dist/runtime/summaries/writing-and-case-study-summary.md`
- `dist/runtime/summaries/audience-and-industry-summary.md`
- `dist/runtime/summaries/ux-roadmap-summary.md`
- `dist/runtime/summaries/ux-cognition-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Problem  (Names the original problem and stakes.)
  ## Process  (Shows what was actually done, not generic steps.)
  ## Solution  (Explains the rebuilt logic or artifact.)
  ## Outcome and proof  (Links claims to evidence and open gaps.)

- Required section: Problem
- Required section: Process
- Required section: Solution
- Required section: Outcome and proof
- Required evidence: comparison artifact
- Required evidence: measured outcome or proxy
- Required evidence: claim-to-proof link
- Required decision: claim_vs_proof_boundary
- Required decision: proxy_vs_measured
- Required decision: narrative_order
- Required decision: honesty_tradeoff
- Hard fail signal: findings only
- Hard fail signal: this case study shows my passion
- Soft fail signal: storytelling only

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Case Study Rewrite. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
