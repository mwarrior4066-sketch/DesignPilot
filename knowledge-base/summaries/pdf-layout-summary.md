---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/AI PDF Creation_ Grid and Typography.md
last_updated: 2026-04-09
synchronized: true
domain: pdf-layout
---

# PDF Layout Summary

Primary sources: AI PDF Creation_ Grid and Typography, AI Design Operator Pack Improvement Brief, AI Design Operator Pack Research.

## Use this summary when
- the task involves PDF editing, tagged documents, reading order, extraction, or layout repair

## Core rules
- for report decks and presentation PDFs, maintain explicit page roles (cover, TOC, divider, content, close) when navigation matters
- preserve symmetric top/bottom spacing contracts and a known content box before tuning component heights
- lines, guides, and decorative indicators must stop exactly at their intended section bounds
- repeated chrome labels should not be duplicated above local page titles
- if spacing debt, density debt, and narrative debt keep recurring together, escalate from patching to structured rebuild
- treat PDFs as documents, not screenshots
- preserve text frames, reading order, and extraction when required
- decorative material should be marked as artifacts when structure matters
- fonts should be embedded and mapped to Unicode when possible
- tagged structure matters for accessible PDFs

## Failure conditions
- rasterizing as a shortcut
- white-box patching presented as real repair
- broken reading order
- ligature or Unicode extraction failures
- untagged or badly tagged “real content”

## Evidence to return
- frame logic
- tagging / artifact rule
- reading-order rule
- extraction rule
- rasterization rule
