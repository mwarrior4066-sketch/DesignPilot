---
runtime_card_version: 1.0.0
canonical_skill: src/skills/brand-strategy-expert.md
last_generated: 2026-04-11
overlay: true
---
# brand-strategy-expert.md

## Activation conditions
- the task is about positioning, category framing, audience fit, tone, trust, differentiation, brand architecture, or identity logic
- the user needs strategic reasons for brand decisions, not only visual direction
- expressive brand behavior may conflict with interface clarity, compliance, or audience trust
- the task is only a local UI state, implementation detail, or isolated visual tweak with no strategic meaning
- the request is only about one font or one color choice and strategy is not the deciding factor

## Non-activation conditions
- the task is only a local UI state, implementation detail, or isolated visual tweak with no strategic meaning
- the request is only about one font or one color choice and strategy is not the deciding factor

## Core decision rules
- audience fit beats personal taste
- positioning requires a frame of reference, points of parity, points of difference, and a reason-to-believe
- every serious claim needs proof, scope, or an explicit downgrade to hypothesis
- trust is domain- and risk-sensitive, not a vague vibe
- distinctiveness and differentiation are related but not identical; measure which one actually matters in the category
- conventions may be bent only when the communication gain is real and the usability/trust cost is named
- brand systems and interface systems can overlap, but they are not automatically identical

## Failure traps
- demographic stereotypes treated as strategy
- “luxury,” “trusted,” “AI-powered,” “secure,” or “best” asserted without proof or category logic
- brand expression forced into every UI role
- category rebellion with no business reason
- collapsing brand, interface, and campaign language into one undifferentiated system
- using distinctiveness language to avoid proving an actual value claim

## Summary dependencies
- audience-and-industry-summary.md
- Brand Strategy Expert for DesignPilot.md

## Escalation triggers
- niche brands may justify stronger visual divergence if the audience is real, the context supports it, and the cost is understood
- low-risk consumer products may tolerate more novelty than regulated, institutional, civic, health, or finance contexts
- distinctiveness can matter more than abstract “meaningful differentiation” in some categories, but only if recognizability is measurable
- if audience evidence is weak, use the most defensible industry-safe position and clearly state the uncertainty
- if proof for a claim is weak, downgrade to a narrower claim or a hypothesis instead of presenting it as fact
- if brand expression harms interface predictability, keep the behavior conventional and move the expression to non-critical surfaces
- if architecture is unclear, fall back to a simpler endorsed or master-brand pattern instead of proliferating unclear sub-brands
- category frame

## Adjacent handoff rules
- hand off to `color-system-expert.md` when palette roles must be translated into interface or print-safe color systems
- hand off to `type-system-expert.md` when the strategic decision becomes a type-system decision
- hand off to `graphic-design-expert.md` when the problem is composition, art direction, or campaign format
- hand off to `content-and-case-study-expert.md` when the problem is brand tone in words, claims, or case-study narration
- hand off to `ui-system-expert.md` when the user is pushing expressive brand signals into product behavior

## Canonical fallback
- `src/skills/brand-strategy-expert.md`
- `src/knowledge-base/summaries/audience-and-industry-summary.md`
- `src/knowledge-base/summaries/Brand Strategy Expert for DesignPilot.md`