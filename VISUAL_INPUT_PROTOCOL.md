# Visual Input Protocol

Use this protocol when the task includes screenshots, mockups, page images, or image-based PDFs.
This is a pre-pass, not a standalone deliverable route.

## Purpose
Visual inputs are evidence-bearing, but they are incomplete.
The operator must separate what is visible from what is inferred.

## Required extraction fields
- artifact type
- layout type
- visible components
- hierarchy cues
- probable grid structure
- approximate type scale
- density and grouping cues
- visible state cues if present
- mismatch between user description and visible evidence
- confidence level

## Evidence classes
Mark observations as one of:
- observed
- inferred
- unverified

## Confidence scale
- high: directly visible and stable from the artifact
- medium: strongly suggested by spacing, grouping, or repeated structure
- low: plausible but not confirmable from the artifact alone

## Rules
- do not claim unseen interaction behavior from static pixels alone
- do not claim source-file semantics, accessibility tree logic, or document tags from screenshots alone
- do not treat image-based PDFs as semantically trustworthy documents
- surface user-description mismatches explicitly
- keep inferred grid and type claims bounded by confidence language

## Routing handoff
After the visual pre-pass:
- UI/hierarchy failures -> `rt_ui_structure_critique`
- KPI order and dense-data failures -> `rt_dashboard_audit`
- artifact recovery or extension -> `rt_layout_reconstruction_plan`
- document semantics or extraction risk -> `rt_pdf_remediation`
