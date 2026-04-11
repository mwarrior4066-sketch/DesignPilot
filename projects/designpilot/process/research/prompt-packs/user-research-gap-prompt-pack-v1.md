# User Research Gap Prompt Pack

## Pack metadata
- Prompt pack name: user-research-gap-prompt-pack-v1
- Related project: DesignPilot
- Related decision: identify the minimum user-validation artifacts needed next
- Version: v1
- Last updated: 2026-04-10

## Research goal
- define the smallest credible user-validation plan that would move DesignPilot from comparative proof toward external confidence or production-adjacent proof

## What is already known
- reviewer confidence artifacts exist
- production outcome proof does not
- the project needs a live artifact review or implementation receipt

## What is missing
- a sharp map of which user evidence is highest-yield and lowest-cost next

## Scope boundary
- do not expand into a full startup research program

## Evidence target
- case-study proof and workflow evidence

## Exclusions
- abstract UX research frameworks with no artifact output
- broad discovery plans disconnected from the current proof gap

## Output format
- return a prioritized research gap map with artifact type, expected learning, effort level, and confidence gain

## Prompts
### Prompt 1
- Why this prompt exists: finds the next best external-confidence move
- Intended evidence burden: research prioritization with artifact outcomes
- When not to use: when asking for live participant recruiting scripts
```text
Map the highest-yield external-validation artifacts for a design-operator product that already has internal proof and benchmark comparisons but lacks production outcome evidence. Prioritize options like live artifact review, implementation review, timed task comparison, confidence interviews, and production-adjacent receipts. Return: priority ranking, why each artifact matters, confidence gain, effort cost, and what wording each artifact would or would not justify.
```

### Prompt 2
- Why this prompt exists: protects the case study from overclaiming
- Intended evidence burden: proof-calibration rules
- When not to use: when the request is only about research recruitment
```text
Research how case studies for AI-assisted or workflow-automation tools should distinguish internal benchmark proof, reviewer confidence proof, and true production outcome proof. Return a wording guide with allowed claim strength, banned overclaims, and the minimum acceptable evidence for each proof class.
```

## Target artifacts or decisions
- roadmap next steps
- claim-to-proof wording limits
- external validation planning
