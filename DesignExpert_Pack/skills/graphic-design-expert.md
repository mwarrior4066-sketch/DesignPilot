---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/graphic-design-format-summary.md
  - knowledge-base/source-docs/Strict Graphic Design Expert for a Modular AI Design Operator Pack.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: graphic-design
---

# Graphic Design Expert

## Purpose
Use this skill for posters, campaigns, editorial composition, presentation slides, image/text balance, visual hierarchy, and distance-driven communication when the output is more graphic-communication-driven than product-UI-driven.

## Activate when
- the task is about posters, campaigns, decks, editorial composition, image/text balance, hierarchy, focal structure, or composition-heavy visual work
- the user needs a format-specific communication decision, not only a visual style direction
- the piece must work at distance, under time pressure, or within a strong communication contract

## Do not activate when
- the problem is mainly product flow, dashboard logic, keyboard accessibility, or document tagging
- the task is only implementation detail or low-level code translation
- the format is actually UI/product work wearing graphic-design language

## Read these first
- `knowledge-base/summaries/graphic-design-format-summary.md`
- `knowledge-base/summaries/grid-mediums-summary.md`
- `knowledge-base/summaries/typography-summary.md`
- `knowledge-base/summaries/brand-and-archetype-summary.md`
- `knowledge-base/summaries/pantone-production-summary.md` when print-aware
- `libraries/PANTONE_LIBRARY.json`, `libraries/PANTONE_LIBRARY.md` when print-aware
- `libraries/FONT_LIBRARY.json`, `libraries/FONT_LIBRARY.md` when type choice is active

## Decision rules
- format logic first
- hierarchy second
- viewing time and distance third
- type/image relationship fourth
- decorative effects last
- do not borrow UI logic unless the output is actually UI

## Default actions
- classify the format: expressive graphic, information-led, campaign/OOH, poster, editorial, presentation, or system-led brand graphic
- define the viewing-time class: momentary, short, medium, or long
- define the distance class: near, mid, or far
- define the primary, secondary, and tertiary information
- define the focal node and the permitted hierarchy depth
- choose the composition frame and whether the grid should stay strict or loosen intentionally
- define how type and image share power
- state whether the piece is brand-led, editorial, information-led, or distance-driven

## Useful thresholds
- campaign / OOH work should usually behave like a one-message system, not a brochure
- deck logic is time-based and distance-based; density should stay lower than editorial spreads
- distance-driven work needs larger type and stronger contrast than near-reading work
- if more than one element reads as the headline, hierarchy is unstable
- all-caps increase the legibility burden in distance contexts

## Exception rules
- posters and high-expression editorial work can break the grid intentionally, but the break must create measurable communication gain
- presentation slides may need much more restraint than posters, even when both are graphic communication tasks
- expressive work can tolerate some ambiguity only if mandatory information remains stable and legible
- asynchronous slide-doc hybrids may borrow from editorial rhythm, but only if they are genuinely read rather than presented live

## Fallback logic
- if the composition is unclear, simplify to one dominant focal node and a cleaner hierarchy before adding texture
- if viewing distance or time is unclear, default to the shorter viewing window and the stricter legibility assumption
- if print color is uncertain, use Pantone-aware language instead of pretending screen and print are identical
- if the piece feels neither graphic nor informationally stable, classify it by the harshest communication contract and simplify accordingly

## Failure traps
- category error: designing a deck like a magazine or a billboard like a brochure
- decorative noise replacing hierarchy
- multiple rival focal points with no dominant read
- expressive treatment used where distance legibility is the real requirement
- visual style chosen with no information ranking
- UI-style restraint forced onto expressive graphic work, or expressive chaos forced onto information-led work

## Evidence required
Use some combination of:
- format classification
- viewing-time and distance note
- composition logic
- hierarchy map
- type/image ratio
- distance/time legibility note
- grid or exception-zone note
- print-aware color note when relevant

## Handoff to other skills
- hand off to `brand-strategy-expert.md` when audience fit, trust, or tone is unclear
- hand off to `type-system-expert.md` when the type system needs deeper logic
- hand off to `color-system-expert.md` when contrast, APCA/WCAG, or print fidelity matter
- hand off to `grid-system-expert.md` or `layout-reconstruction-expert.md` when the grid is the main structural problem

## Output expectations
- clear format classification
- viewing contract explicit
- hierarchy and composition rationale
- no UI/system duplication unless the job is actually UI
- explicit note when expressiveness is allowed vs when clarity rules
