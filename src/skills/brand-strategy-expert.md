---
skill_version: 1.0.0
source_reference:
  - src/knowledge-base/summaries/audience-and-industry-summary.md
  - src/knowledge-base/source-docs/Brand Strategy Expert for DesignPilot.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: brand-strategy
---

# Brand Strategy Expert

## Purpose
Use this skill to make strict positioning, audience-fit, trust-signal, convention, and brand-vs-interface decisions. Treat brand work as a system of falsifiable hypotheses, not a moodboard.

## Activate when
- the task is about positioning, category framing, audience fit, tone, trust, differentiation, brand architecture, or identity logic
- the user needs strategic reasons for brand decisions, not only visual direction
- expressive brand behavior may conflict with interface clarity, compliance, or audience trust

## Do not activate when
- the task is only a local UI state, implementation detail, or isolated visual tweak with no strategic meaning
- the request is only about one font or one color choice and strategy is not the deciding factor

## Read these first
- `src/knowledge-base/summaries/audience-and-industry-summary.md`
- `src/knowledge-base/summaries/brand-and-archetype-summary.md`
- `src/knowledge-base/summaries/ui-system-summary.md` when product behavior is at risk

## Decision rules
- audience fit beats personal taste
- positioning requires a frame of reference, points of parity, points of difference, and a reason-to-believe
- every serious claim needs proof, scope, or an explicit downgrade to hypothesis
- trust is domain- and risk-sensitive, not a vague vibe
- distinctiveness and differentiation are related but not identical; measure which one actually matters in the category
- conventions may be bent only when the communication gain is real and the usability/trust cost is named
- brand systems and interface systems can overlap, but they are not automatically identical

## Default actions
- define the category frame in one sentence
- identify table-stakes expectations that the brand must satisfy to feel credible
- identify audience logic: demographic, psychographic, behavioral, and contextual where possible
- state the trust burden for the category and the required trust signals
- decide whether the recommendation is driving toward differentiation, distinctiveness, or safe parity plus clarity
- separate expressive brand assets from interface-safe system decisions when needed
- classify unsupported assertions as assumptions plus validation plans

## Useful thresholds
- a positioning recommendation is weak if it cannot answer category, benefit, and why-trust-it in plain language
- segment definitions should include at least two measurable qualifiers beyond taste-language or stereotypes
- high-risk categories need hard trust cues early, not just tone or aesthetics
- if the audience evidence is single-source or speculative, confidence should be treated as provisional rather than final

## Exception rules
- niche brands may justify stronger visual divergence if the audience is real, the context supports it, and the cost is understood
- low-risk consumer products may tolerate more novelty than regulated, institutional, civic, health, or finance contexts
- distinctiveness can matter more than abstract “meaningful differentiation” in some categories, but only if recognizability is measurable

## Fallback logic
- if audience evidence is weak, use the most defensible industry-safe position and clearly state the uncertainty
- if proof for a claim is weak, downgrade to a narrower claim or a hypothesis instead of presenting it as fact
- if brand expression harms interface predictability, keep the behavior conventional and move the expression to non-critical surfaces
- if architecture is unclear, fall back to a simpler endorsed or master-brand pattern instead of proliferating unclear sub-brands

## Failure traps
- demographic stereotypes treated as strategy
- “luxury,” “trusted,” “AI-powered,” “secure,” or “best” asserted without proof or category logic
- brand expression forced into every UI role
- category rebellion with no business reason
- collapsing brand, interface, and campaign language into one undifferentiated system
- using distinctiveness language to avoid proving an actual value claim

## Evidence required
Use some combination of:
- category frame
- audience-fit note
- points-of-parity / points-of-difference note
- reason-to-believe or claim substantiation note
- trust-signal note
- brand-vs-interface separation rule
- validation gap note when evidence is weak

## Handoff to other skills
- hand off to `color-system-expert.md` when palette roles must be translated into interface or print-safe color systems
- hand off to `type-system-expert.md` when the strategic decision becomes a type-system decision
- hand off to `graphic-design-expert.md` when the problem is composition, art direction, or campaign format
- hand off to `content-and-case-study-expert.md` when the problem is brand tone in words, claims, or case-study narration
- hand off to `ui-system-expert.md` when the user is pushing expressive brand signals into product behavior

## Output expectations
- strategy before style
- audience fit explicit
- trust burden explicit
- unsupported claims labeled as hypotheses, not promises
- distinctiveness vs differentiation made explicit when relevant
- brand vs interface distinction named whenever relevant
