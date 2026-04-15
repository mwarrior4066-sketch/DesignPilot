# rt_text_humanization

**Task:** Text Humanization Revision

## Route fit
- Role: governing
- Lightweight eligible: yes
- Governing route or helper: governing route

## Use when
- Use when the governing need is prose-quality revision rather than structural rewriting or route-level diagnosis.

## Startup recommendation
- Recommended mode: lightweight
- Default contract: `dist/runtime/contracts_lite/text_humanization_revision.md`
- Recommended profile if you escalate: `dist/DEPLOY_BRAND.md`
- Visual input supported: no

## Governing skills
- `dist/runtime/skills/text-humanization-expert.md` - Use this skill to revise prose so it sounds authored, readable, and natural without changing meaning, adding claims, or flattening the writer’s voice.
- `dist/runtime/skills/content-and-case-study-expert.md` - Use this skill to audit, rewrite, expand, or structure UX copy, design rationale, documentation, and case-study writing without losing clarity, mode control, or evidence.

## Optional supporting skills
- `dist/runtime/skills/brand-strategy-expert.md` - Use this skill to make strict positioning, audience-fit, trust-signal, convention, and brand-vs-interface decisions. Treat brand work as a system of falsifiable hypotheses, not a moodboard.

## Runtime summaries
- `dist/runtime/summaries/text-humanization-summary.md`
- `dist/runtime/summaries/writing-and-case-study-summary.md`
- `dist/runtime/summaries/audience-and-industry-summary.md`

## Contract shape
- Job of the piece
- Pattern scan
- Meaning-preservation guard
- Revised passage
- Why this reads more human

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_case_study_rewrite`
- Canonical routing fallback: `src/schemas/routing_registry.json`
