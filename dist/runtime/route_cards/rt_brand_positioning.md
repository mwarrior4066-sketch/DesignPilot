# rt_brand_positioning

**Task:** Brand Positioning Pass

## Route fit
- Role: governing
- Lightweight eligible: yes
- Governing route or helper: governing route

## Use when
- Use when the system must decide who the brand is for and how it earns trust.

## Startup recommendation
- Recommended mode: lightweight
- Default contract: `dist/runtime/contracts_lite/brand_positioning_pass.md`
- Recommended profile if you escalate: `dist/DEPLOY_BRAND.md`
- Visual input supported: no

## Governing skills
- `dist/runtime/skills/brand-strategy-expert.md` - Use this skill to make strict positioning, audience-fit, trust-signal, convention, and brand-vs-interface decisions. Treat brand work as a system of falsifiable hypotheses, not a moodboard.
- `dist/runtime/skills/content-and-case-study-expert.md` - Use this skill to audit, rewrite, expand, or structure UX copy, design rationale, documentation, and case-study writing without losing clarity, mode control, or evidence.

## Optional supporting skills
- `dist/runtime/skills/ux-research-expert.md` - Use this skill to frame the problem, identify the user, surface cognitive/ergonomic constraints, and keep work tied to real needs instead of surface styling.

## Runtime summaries
- `dist/runtime/summaries/audience-and-industry-summary.md`
- `dist/runtime/summaries/writing-and-case-study-summary.md`
- `dist/runtime/summaries/ux-roadmap-summary.md`
- `dist/runtime/summaries/ux-cognition-summary.md`

## Contract shape
- Audience and problem
- Positioning frame
- Trust and proof burden
- Messaging consequences

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_case_study_rewrite`
- Canonical routing fallback: `src/schemas/routing_registry.json`
