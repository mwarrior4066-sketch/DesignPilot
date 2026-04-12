---
runtime_card_version: 1.0.0
canonical_skill: src/skills/graphic-design-expert.md
last_generated: 2026-04-11
overlay: true
---
# graphic-design-expert.md

## Activation conditions
- the task is about posters, campaigns, decks, editorial composition, image/text balance, hierarchy, focal structure, or composition-heavy visual work
- the user needs a format-specific communication decision, not only a visual style direction
- the piece must work at distance, under time pressure, or within a strong communication contract
- the problem is mainly product flow, dashboard logic, keyboard accessibility, or document tagging
- the task is only implementation detail or low-level code translation
- the format is actually UI/product work wearing graphic-design language

## Non-activation conditions
- the problem is mainly product flow, dashboard logic, keyboard accessibility, or document tagging
- the task is only implementation detail or low-level code translation
- the format is actually UI/product work wearing graphic-design language

## Core decision rules
- format logic first
- hierarchy second
- viewing time and distance third
- type/image relationship fourth
- decorative effects last
- do not borrow UI logic unless the output is actually UI

## Failure traps
- category error: designing a deck like a magazine or a billboard like a brochure
- decorative noise replacing hierarchy
- multiple rival focal points with no dominant read
- expressive treatment used where distance legibility is the real requirement
- visual style chosen with no information ranking
- UI-style restraint forced onto expressive graphic work, or expressive chaos forced onto information-led work

## Summary dependencies
- graphic-design-format-summary.md
- Strict Graphic Design Expert for DesignPilot.md

## Escalation triggers
- posters and high-expression editorial work can break the grid intentionally, but the break must create measurable communication gain
- presentation slides may need much more restraint than posters, even when both are graphic communication tasks
- expressive work can tolerate some ambiguity only if mandatory information remains stable and legible
- asynchronous slide-doc hybrids may borrow from editorial rhythm, but only if they are genuinely read rather than presented live
- if the composition is unclear, simplify to one dominant focal node and a cleaner hierarchy before adding texture
- if viewing distance or time is unclear, default to the shorter viewing window and the stricter legibility assumption
- if print color is uncertain, use Pantone-aware language instead of pretending screen and print are identical
- if the piece feels neither graphic nor informationally stable, classify it by the harshest communication contract and simplify accordingly

## Adjacent handoff rules
- hand off to `brand-strategy-expert.md` when audience fit, trust, or tone is unclear
- hand off to `type-system-expert.md` when the type system needs deeper logic
- hand off to `color-system-expert.md` when contrast, APCA/WCAG, or print fidelity matter
- hand off to `grid-system-expert.md` or `layout-reconstruction-expert.md` when the grid is the main structural problem

## Canonical fallback
- `src/skills/graphic-design-expert.md`
- `src/knowledge-base/summaries/graphic-design-format-summary.md`
- `src/knowledge-base/summaries/Strict Graphic Design Expert for DesignPilot.md`