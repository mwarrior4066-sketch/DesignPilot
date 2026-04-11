---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/document-presentation-architecture-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/DesignPilot Problem Catalogue.md
  - knowledge-base/source-docs/Design System Failure Diagnosis and Solutions.md
---
# Document Presentation Architecture Summary Runtime Summary

## Decision rules
- treat decks and reports as structured information architectures, not flat asset sequences
- use tonal temperature shifts, not brightness inversion, to create rhythm in dark systems
- avoid pure `#000000` backgrounds as the default dark surface when reading or prolonged viewing matters
- use a single content box or equivalent vertical-fill model so all cards, rows, and modules fill to the footer predictably
- make top and bottom content gaps symmetrical wherever the layout contract expects them
- prefer one idea per slide in live-presentation contexts; split overloaded slides instead of shrinking everything
- keep section ID in the persistent chrome and keep page headlines unique to the local content
- use cover, TOC, chapter divider, content, and close as distinct architectural page roles when the deck is long enough to need wayfinding
- treat ghost numbers, decorative watermarks, and repeated labels as navigational artifacts only if they stay quiet enough not to compete with content

## Failure traps
- pure black dark mode causing harshness or halation risk
- warm/light alternation creating a different deck rather than a related rhythm
- ghost numbers acting like competing headlines
- header chrome repeating the same label above the page title
- hard-coded card heights causing floating content or large bottom dead zones
- overshoot lines crossing into adjacent sections
- one slide carrying too many independent concepts or components
- deck built as a flat sequence with no cover, TOC, chapter dividers, or closing logic

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/document-presentation-architecture-summary.md`
- `knowledge-base/source-docs/DesignPilot Problem Catalogue.md`
- `knowledge-base/source-docs/Design System Failure Diagnosis and Solutions.md`