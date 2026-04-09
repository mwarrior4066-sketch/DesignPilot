---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/Comprehensive Typeface Database and Systematic Engineering Report for Design Systems.md
last_updated: 2026-04-09
synchronized: true
domain: typeface-database
---

# Typeface Database Summary

Primary sources: Comprehensive Typeface Database and Systematic Engineering Report for Design Systems, The Global Typographic Landscape of 2026.

## Use this summary when
- the task needs a concrete typeface recommendation instead of generic typography advice
- the task needs substitutions between premium and open-source faces
- licensing, platform availability, or implementation constraints matter
- the task needs a shortlist by use case: UI, editorial, branding, dashboards, presentation, accessibility, multilingual

## Core schema the pack should think in
For any meaningful font recommendation, try to account for:
- identity: name, foundry, designer, category, lineage
- technical system: variable/static, axes, figures, OT features, script support
- readability: x-height, apertures, density, long-form performance, small-size behavior
- implementation: WOFF2 efficiency, preload needs, fallback compatibility, token mapping
- licensing: OFL/commercial/proprietary, web/app restrictions, platform availability
- decision support: best use, substitution logic, role in the system, why it beats close alternatives

## High-value role buckets
### UI / product sans
Inter, Roboto, Public Sans, IBM Plex Sans, Mona Sans, Open Sans, Work Sans, DM Sans, Figtree

### Humanist / approachable sans
Open Sans, Source Sans 3, Lato, Seravek, Gill Sans Nova, Ubuntu, Calibri, DejaVu Sans

### Neutral grotesk / premium branding sans
Helvetica Now, Söhne, Aktiv Grotesk, Neue Montreal, Basis Grotesk, Maison Neue, Univers, Akzidenz-Grotesk

### Geometric sans
Montserrat, Satoshi, Avenir Next, Futura Now, Gotham, Brown, Gilroy, Circular

### Editorial serif workhorses
Merriweather, Charter, Source Serif 4, Miller Text, Georgia, Tinos, Lora, Alegreya

### Display serifs
Tiempos Fine, Editorial New, Didot, Bodoni, Prata, Migra, Cinzel

### Monospaces
JetBrains Mono, IBM Plex Mono, Noto Sans Mono, Söhne Mono, Whyte Mono, Cascadia Code, Source Code Pro, Menlo

### Accessibility-first faces
Atkinson Hyperlegible, Lexend, Andika, Luciole, FS Me, Tiresias, Dyslexie, OpenDyslexic

### Multilingual / global-system faces
Noto Sans, Noto Serif, Noto Sans Mono, IBM Plex Sans, Source Han Sans, Brill, Gentium Plus, Akkurat, Frutiger Next

## Decision rules
- role clarity outranks novelty
- preserve readable structure before expressive tone
- for product UI, default to system-safe or open-source sans families unless brand needs clearly justify a premium choice
- for long-form editorial, prefer serif workhorses or warm humanist sans over tight geometric faces
- for dashboards and dense tools, prefer high x-height, open counters, tabular-figure support, and width economy
- for premium branding, compare neutral-premium grotesks, refined geometric sans, and high-contrast display serifs rather than defaulting to Inter or Helvetica every time
- avoid pairing two fonts from the same category unless their proportions, x-height, or tone differ enough to create real contrast
- if the requested face is missing, preserve role, structure, licensing fit, and implementation risk before preserving brand romance

## Substitution logic
### Premium → high-quality open-source
- Helvetica / SF Pro → Inter, Archivo, Roboto
- Proxima Nova / Gotham → Montserrat, Figtree, Work Sans
- Avenir / Frutiger → Lato, Nunito Sans, Open Sans
- Arnhem / Freight Text → Source Serif 4, Merriweather
- Times New Roman → Tinos, Gelasio, Source Serif 4

### Common fallback patterns
- Apple product UI → SF Pro if native, Inter if cross-platform
- Enterprise dashboard → Inter / Roboto / Public Sans / IBM Plex Sans
- Editorial PDF → Charter / Source Serif 4 / Merriweather / Georgia
- Luxury / fashion → Didot / Tiempos Fine / GT Sectra / Söhne / Editorial New
- Developer tooling → JetBrains Mono / IBM Plex Mono / Cascadia Code

## Implementation notes
- prefer WOFF2 first
- use `font-display: swap` by default unless the design explicitly requires blocking behavior
- variable fonts can replace many static files and reduce request count when used carefully
- use optical sizing when supported
- if a face has GRAD or opsz axes, use them before forcing unrelated weight changes
- always name fallback stacks and substitution logic rather than pretending the requested face is universally available

## Evidence to return
- role map
- primary family + fallback stack
- why the face fits the medium
- any licensing or availability caveat
- any substitution logic
- implementation note when relevant
