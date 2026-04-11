# Case Study Proof Gap Prompt Pack

## Pack metadata
- Prompt pack name: case-study-proof-gap-prompt-pack-v1
- Related project: DesignPilot
- Related decision: strengthen the public proof narrative without overstating results
- Version: v1
- Last updated: 2026-04-10

## Research goal
- gather evidence and communication frameworks for writing a proof-honest case study around an operator pack

## What is already known
- the project now has a proof stack summary, a claim map, and benchmark artifacts
- the current risk is sounding more proven than the evidence allows

## What is missing
- stronger external frameworks for proof calibration and narrative order

## Scope boundary
- do not drift into general portfolio storytelling advice

## Evidence target
- case-study proof and communication rules

## Exclusions
- generic “tell a story” articles
- marketing advice with no evidence hierarchy

## Output format
- return a structured case-study proof brief with narrative order, evidence hierarchy, and banned wording patterns

## Prompts
### Prompt 1
- Why this prompt exists: finds evidence-backed case-study sequencing
- Intended evidence burden: communication framework
- When not to use: when you already have the exact narrative order locked
```text
Research strong frameworks for writing case studies that distinguish what was built, what was tested, what was measured, and what remains unproven. Prioritize design-rationale, evidence framing, and plain-language documentation sources. Return a recommended narrative order, proof hierarchy, wording cautions, and examples of how to present open gaps without sounding evasive.
```

### Prompt 2
- Why this prompt exists: finds rules for before/after and comparison honesty
- Intended evidence burden: comparative-proof communication guidance
- When not to use: when no comparison artifact exists
```text
Research best practices for presenting before-and-after or baseline-versus-operator comparisons without making the baseline artificially weak. Focus on fair-test setup, prompt transparency, rubric consistency, and interpretation limits. Return a comparison-integrity checklist and explicit overclaim warnings.
```

## Target artifacts or decisions
- case-study rewrite decisions
- proof-language calibration
- comparison-integrity section
