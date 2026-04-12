---
summary_version: 1.1.0
source_reference:
  - src/knowledge-base/source-docs/Global Typography Intelligence Index.md
  - src/knowledge-base/source-docs/Comprehensive Typeface Database and Systematic Engineering Report for Design Systems.md
last_updated: 2026-04-11
synchronized: true
domain: typeface-database
---

# Typeface Database Summary

## Use this summary when
- the task needs a concrete typeface recommendation instead of generic typography advice
- the task needs substitutions between premium and open-source faces
- licensing, platform availability, script coverage, or implementation constraints matter
- the task needs a shortlist by use case: UI, editorial, branding, dashboards, presentation, accessibility, multilingual, Arabic, or CJK

## Core schema the pack should think in
For any meaningful font recommendation, try to account for:
- identity: name, foundry, category, lineage
- technical system: variable/static, axes, figures, OT features, script support
- readability: x-height, apertures, density, long-form performance, small-size behavior
- implementation: WOFF2 efficiency, preload needs, fallback compatibility, token mapping, install path caveats
- licensing: OFL/commercial/proprietary, web/app restrictions, platform availability
- decision support: best use, substitution logic, role in the system, and why it beats close alternatives

## High-value role buckets
### UI / product sans
Inter, Geist Sans, Public Sans, IBM Plex Sans, Roboto Flex, Mona Sans, Open Sans, Work Sans, DM Sans, Figtree

### Humanist / approachable sans
Open Sans, Source Sans 3, Lato, IBM Plex Sans, Seravek, Gill Sans Nova, Ubuntu

### Neutral grotesk / premium branding sans
Söhne, Akkurat, Graphik, Atlas Grotesk, Aktiv Grotesk, Neue Montreal, Basis Grotesk, Maison Neue, Univers, Akzidenz-Grotesk

### Geometric sans
Montserrat, Satoshi, Avenir Next, Futura PT / Futura Now, Gotham, Brown, Gilroy, Circular, Poppins

### Editorial serif workhorses
Charter, Source Serif 4, Tiempos Text, Literata, Merriweather, Georgia, Lora, Alegreya, Garamond, Baskerville

### Display serifs
Editorial New, GT Sectra, Canela, Ogg, Didot, Bodoni Moda, Tiempos Fine, Signifier

### Monospaces
JetBrains Mono, IBM Plex Mono, Geist Mono, Noto Sans Mono, Cascadia Code, Source Code Pro, Fira Code, Menlo

### Accessibility-first faces
Atkinson Hyperlegible Next, Atkinson Hyperlegible Mono, Lexend, Andika, Luciole, FS Me, Tiresias

### Multilingual / global-system faces
Noto Sans, Noto Serif, Noto Sans CJK, Noto Serif CJK, Source Han Sans, Source Han Serif, IBM Plex Sans, Brill, Gentium Plus

### Arabic-supportive starting points
Noto Sans Arabic, Noto Naskh Arabic, Cairo, IBM Plex Sans Arabic, 29LT Bukra when licensed

## Decision rules
- role clarity outranks novelty
- preserve script coverage, readable structure, and implementation fit before expressive tone
- for product UI, default to system-safe or open-source sans families unless brand needs clearly justify a premium choice
- for long-form editorial, prefer serif workhorses or warm humanist sans over tight geometric faces
- for dashboards and dense tools, prefer high x-height, open counters, tabular-figure support, clear zero/one differentiation, and width economy
- for premium branding, compare neutral-premium grotesks, refined geometric sans, and high-contrast display serifs rather than defaulting to Inter or Helvetica every time
- avoid pairing two fonts from the same category unless their proportions, x-height, or tone differ enough to create real contrast
- if the requested face is missing, preserve role, script support, licensing fit, and implementation risk before preserving romance

## Substitution logic
### Premium → high-quality open-source
- Helvetica / SF Pro → Inter, Public Sans, Roboto Flex
- Graphik / Suisse / Neue Montreal → Inter, Figtree, Archivo
- Proxima Nova / Gotham → Montserrat, Work Sans, Figtree
- Avenir / Frutiger → Lato, Open Sans, Nunito Sans
- Freight Text / Miller Text → Source Serif 4, Literata, Merriweather
- Didot / Bodoni → Bodoni Moda, Playfair Display
- Whyte / Söhne Mono → IBM Plex Mono, JetBrains Mono, Geist Mono

## Implementation notes
- prefer WOFF2 first
- use `font-display: swap` by default unless the design explicitly requires blocking behavior
- variable fonts can replace many static files and reduce request count when used carefully
- use optical sizing when supported
- use high-level CSS properties before low-level `font-variation-settings`
- if a face has GRAD or opsz axes, use them before forcing unrelated weight changes
- always name fallback stacks and substitution logic rather than pretending the requested face is universally available
- for multilingual systems, name the script-aware stack explicitly

## Evidence to return
- role map
- primary family + fallback stack
- why the face fits the medium
- any script coverage or localization caveat
- any licensing or availability caveat
- any substitution logic
- implementation note when relevant
