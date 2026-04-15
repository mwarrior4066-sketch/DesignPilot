---
summary_version: 1.0.0
source_reference:
  - src/knowledge-base/source-docs/Technical Reference Framework for Pantone Systems and Production-Aware Design Operations.md
  - src/libraries/PANTONE_NUMBERS.json
last_updated: 2026-04-09
synchronized: true
domain: print-color-pantone
---

# Pantone Production Summary

## Purpose
Canonical summary for Pantone system choice, coated vs uncoated behavior, process fallback risk, substrate-aware print decisions, and when spot color should remain the print anchor.

## Use when
- the task is print-aware and Pantone is relevant
- the system must translate between Pantone, CMYK, RGB, Hex, and PDF/print workflows
- packaging, editorial print, signage, posters, brand collateral, or premium print production are in scope

## Default rules
- treat Pantone spot color, CMYK, RGB, and Hex as related but not interchangeable systems
- keep Pantone as the print anchor when brand-critical fidelity matters
- treat coated and uncoated targets as separate visual outcomes, not just paper finishes
- prefer Lab*-based conversion logic over static bridge numbers when print fidelity matters
- use CMYK bridge values as approximations, not guarantees
- require substrate context before making high-confidence Pantone recommendations

## Key thresholds
- standard body text contrast target: 4.5:1 minimum
- large text contrast target: 3:1 minimum
- print body type baseline: at least 12pt for standard documents
- poster type baseline: at least 18pt for low-vision-safe poster reading
- Delta E < 1.0: imperceptible
- Delta E < 2.3: professional match
- Delta E 2.0–3.5: visible mismatch risk
- Delta E > 5.0: failure, keep spot color or choose a safer substitute

## Process hierarchy
1. use Pantone spot when identity-critical and the budget/process allows it
2. use Extended Gamut / ECG when available for high-fidelity process approximation
3. use Lab* to process conversion using the house ICC profile when professional matching matters
4. use Bridge / process-safe approximation only with explicit caveats
5. if mismatch risk remains high, choose a nearby Pantone with safer process behavior

## Specialty rules
- metallics: keep as spot-only unless a specific packaging metallic system is supported
- neons: treat as spot-only; do not pretend CMYK or RGB can reproduce them accurately
- pastels: safer in print than neons, but still check contrast and small-type performance
- uncoated stocks mute and soften color; compensate by selecting an appropriate uncoated target, not by assuming coated behavior

## Use-case guidance
- finance / institutional: prefer stable blues, navies, and restrained neutrals
- healthcare / wellness: use calm blues, teals, and soft greens with contrast discipline
- luxury / beauty: deep neutrals, burgundies, emeralds, and metallic accents; separate expression from legible running text
- food / beverage: appetite-driving reds, oranges, and warm yellows; avoid purple/gray dominance in appetite-critical packaging
- editorial / document systems: emphasize legibility, neutrals, and process-safe anchors

## Failure patterns
- picking Pantone without substrate context
- treating RGB or Hex as exact Pantone truth
- using bright yellow or lime for small text on white
- specifying metallic or neon as if process-only output can match it
- using static Bridge values without acknowledging the press/profile condition
- forcing one Pantone to act identically across coated, uncoated, digital, and PDF contexts

## Hand off to
- `color-system-expert.md` for role mapping and contrast logic
- `graphic-design-expert.md` for print-led composition and poster/editorial use
- `pdf-layout-expert.md` when Pantone decisions affect PDF/export specifications
- `document-accessibility-expert.md` when print/PDF contrast or legibility rules affect document usability
