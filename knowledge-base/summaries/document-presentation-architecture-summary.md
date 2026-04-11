---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/DesignPilot Problem Catalogue.md
  - knowledge-base/source-docs/Design System Failure Diagnosis and Solutions.md
last_updated: 2026-04-10
synchronized: true
domain: document-presentation-architecture
---

# Document & Presentation Architecture Summary

## Purpose
Canonical summary for production-level slide decks, reports, and PDF/page systems where theme discipline, wayfinding, density control, vertical fill, and rebuild-vs-refactor logic determine output quality.

## Use when
- the task is a slide deck, presentation system, report deck, or structured PDF where page rhythm and navigation matter
- the user is fixing dead zones, floating content, overshoot lines, duplicated chrome labels, or ghost markers
- the output must behave like an information environment rather than a flat sequence of pages

## Default rules
- treat decks and reports as structured information architectures, not flat asset sequences
- use tonal temperature shifts, not brightness inversion, to create rhythm in dark systems
- avoid pure `#000000` backgrounds as the default dark surface when reading or prolonged viewing matters
- use a single content box or equivalent vertical-fill model so all cards, rows, and modules fill to the footer predictably
- make top and bottom content gaps symmetrical wherever the layout contract expects them
- prefer one idea per slide in live-presentation contexts; split overloaded slides instead of shrinking everything
- keep section ID in the persistent chrome and keep page headlines unique to the local content
- use cover, TOC, chapter divider, content, and close as distinct architectural page roles when the deck is long enough to need wayfinding
- treat ghost numbers, decorative watermarks, and repeated labels as navigational artifacts only if they stay quiet enough not to compete with content

## Useful thresholds
- all major spacing should resolve to an 8pt rhythm, with 4pt used only for fine tuning
- dead zone under the last content block should stay at or below one base unit unless the format intentionally uses empty space as a focal device
- deck density should stay much lower than editorial density; if a slide exceeds the viewing-time contract, split it
- body text in deck/report contexts should stay in the readability-safe range and not rely on shrink-to-fit as the main fix
- decorative background markers should remain subordinate; anything above a subtle watermark level is a noise risk
- duplicate section labels across chrome and headline zones are a failure, not reinforcement

## Failure patterns
- pure black dark mode causing harshness or halation risk
- warm/light alternation creating a different deck rather than a related rhythm
- ghost numbers acting like competing headlines
- header chrome repeating the same label above the page title
- hard-coded card heights causing floating content or large bottom dead zones
- overshoot lines crossing into adjacent sections
- one slide carrying too many independent concepts or components
- deck built as a flat sequence with no cover, TOC, chapter dividers, or closing logic
- recurrent rebuilds caused by structural debt rather than isolated visual bugs

## Rebuild triggers
Choose rebuild over patching when three or more of these are true:
- architecture-content mismatch keeps reappearing after local fixes
- narrative or section changes require touching every page manually
- spacing rules are hard-coded and not tokenized or formula-driven
- density failures recur because the page archetypes are wrong
- theme changes require manual recoloring rather than token or semantic updates

## Hand off to
- `graphic-design-expert.md` for hierarchy, focal structure, and deck communication logic
- `layout-reconstruction-expert.md` when the existing page system must be inferred or normalized
- `pdf-layout-expert.md` when page fidelity, frame logic, or export-safe layout repair is the main issue
- `color-system-expert.md` when dark-surface contrast or tonal consistency is unstable
