# Minimum Viable External Credibility (MVEC) Protocol

## Round 1 design
- 3 independent expert reviewers
- 20 high-stakes outputs
- one primary rubric dimension: implementation realism
- 1–5 confidence score per review
- unedited trust note per reviewer
- explicit win/loss disclosure against a baseline

## Storage
- structured reviews in `evals/external_reviews/`
- public summary in `proof/trust_notes/`
- release-level conclusion in `proof/release_cards/`


---

## Blind Comparison Protocol

# Blind Comparison Protocol

For DesignPilot versus baseline comparisons:
- strip assistant-specific greetings and sign-offs
- normalize headings and code-block style
- preserve the same task constraints across systems
- remove model or vendor identifiers before expert review
- collect score, confidence, and trust note separately
