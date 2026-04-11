---
summary_version: 1.1.0
source_reference:
  - knowledge-base/source-docs/Global Typography Intelligence Index.md
  - knowledge-base/source-docs/The Global Typographic Landscape of 2026.md
  - knowledge-base/source-docs/Comprehensive Typeface Database and Systematic Engineering Report for Design Systems.md
last_updated: 2026-04-11
synchronized: true
domain: typography
---

# Typography Summary

## Use this summary when
- the task is about fonts, hierarchy, readability, pairing, measure, variable fonts, localization, fallback stacks, or implementation-safe type choices

## Core rules
- body text for digital UI starts at 16px by default
- body leading defaults around 1.5x font size
- display leading tightens to about 1.1–1.25
- target 45–75 characters per line for continuous reading, with about 66 CPL as a strong default
- choose by role before taste, and by script coverage before tone when the system is multilingual
- for small text, prioritize open counters, higher x-height, and enough weight before chasing stylistic purity
- variable fonts are preferred when they reduce file overhead and increase control
- use high-level CSS controls before reaching for low-level `font-variation-settings`
- avoid pairing two fonts from the same broad category unless there is strong contrast in proportion, x-height, rhythm, width, or tone

## High-value decisions
- UI/product: favor neutral or humanist sans families with strong small-size behavior such as Inter, Geist Sans, Public Sans, IBM Plex Sans, or Roboto Flex
- editorial/long-form: favor serif workhorses or warm humanist sans with stable text color such as Charter, Source Serif 4, Tiempos Text, Literata, or Merriweather
- dashboards/dense tools: favor tabular figures, strong character distinction, width economy, and a usable mono companion
- multilingual systems: define script-aware families and fallback stacks explicitly instead of assuming a single Latin face can carry the system
- accessibility-sensitive work: prefer families with stronger character distinction, including the current Atkinson Hyperlegible Next and Mono family, when accessibility value is real

## Current implementation notes
- Geist’s npm and zip installs include the full glyph set and `font-feature-settings` support; the easier Google Fonts route is partial
- IBM Plex remains one of the strongest multi-subfamily enterprise systems because it pairs Sans, Serif, Mono, and broader language support coherently
- Noto remains the strongest default global fallback family set for broad script support

## Failure conditions
- line length above about 80 CPL for Latin reading without a very good reason
- tiny text used to solve layout problems
- weak hierarchy because pairings are too similar
- small text without enough weight, opsz support, or spacing
- premium recommendations with no licensing or fallback plan
- multilingual recommendations that ignore script coverage or RTL behavior

## Evidence to return
- role map
- body/display defaults
- measure target
- leading ratio
- variable-font / opsz logic
- script coverage or fallback logic when relevant
- licensing or implementation note when relevant
