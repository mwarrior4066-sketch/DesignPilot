---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/The Global Typographic Landscape of 2026.md
  - knowledge-base/source-docs/Comprehensive Typeface Database and Systematic Engineering Report for Design Systems.md
last_updated: 2026-04-09
synchronized: true
domain: typography
---

# Typography Summary

Primary sources: The Global Typographic Landscape of 2026, Comprehensive Typeface Database and Systematic Engineering Report for Design Systems, AI Design Operator Pack Research.

## Use this summary when
- the task is about fonts, hierarchy, readability, pairing, measure, variable fonts, optical sizing, or implementation-safe type choices

## Core rules
- body text for digital UI starts at 16px by default
- body leading defaults around 1.5x font size
- display leading tightens to about 1.1–1.25
- target 45–75 characters per line for continuous reading, with about 66 CPL as a strong default
- use optical sizing when the font supports it
- variable fonts are preferred when they reduce file overhead and increase control
- for small text, prioritize open counters, higher x-height, and enough weight before chasing stylistic purity
- avoid pairing two fonts from the same broad category unless there is strong contrast in proportion, x-height, or tone

## High-value decisions
- UI/product: favor neutral or humanist sans families with strong small-size behavior
- editorial/long-form: favor serif workhorses or warm humanist sans with stable text color
- dashboards/dense tools: favor width economy, tabular figures, strong character distinction, and clear mono support where needed
- branding: contrast can be higher, but state the licensing and deployment implications
- accessibility-sensitive work: prefer faces with strong character distinctness such as Atkinson Hyperlegible, Lexend, Luciole, or Andika when appropriate

## Failure conditions
- line length above about 80 CPL for Latin reading
- tiny text used to solve layout problems
- weak hierarchy because pairings are too similar
- small text without enough weight, opsz support, or spacing
- premium recommendations with no licensing or fallback plan

## Evidence to return
- role map
- body/display defaults
- measure target
- leading ratio
- opsz / fallback logic
- licensing or implementation note when relevant
