# UX Research Gap Map Example
Fixture: tests/fixtures/ux-research-pass.prompt.md
Validation result: tests/evals/ux-research-pass.eval.json

## Input Prompt
Map the most important UX research gaps for a small scheduling platform that is redesigning onboarding, team setup, and shift publishing. The team has some support tickets and a few sales notes, but no recent user research.

## Selected Route and Loaded Skills
- Route: `rt_ux_research_gap_map`
- Task contract: `ux_research_gap_map`
- Mode: PEER
- Phase: research
- Skills: `ux-research-expert.md`, `content-and-case-study-expert.md`
- Known tensions: research depth vs team speed, breadth of curiosity vs decision-critical unknowns

## Final Output
### Known evidence
Right now the team has support tickets and sales notes, which count as weak directional evidence but not measured user proof. They may reveal friction themes, yet they do not tell you whether the onboarding, team setup, and shift publishing flow fails because of discoverability, permissions confusion, or mental-model mismatch.

### Critical gaps
1. Highest-risk gap: why first-time admins fail during team setup. This is a blocker because it changes whether the redesign should focus on guidance, permissions framing, or setup sequencing.
2. Second gap: how shift publishing is understood by managers versus staff. That affects terminology, permission rules, and notification expectations.
3. Third gap: what new users expect from onboarding progress and completion feedback. Without this, the redesign can easily optimize for aesthetics instead of task confidence.

### Research plan
- Run 5-7 moderated interviews with recent admins to map mental models around team setup and approval responsibility.
- Run 5 usability test sessions on the current onboarding and shift publishing flow to observe where users fail, hesitate, or misread the sequence.
- Use a short survey only after the interviews to size a few hypotheses, not as the first method. The tradeoff is breadth versus signal quality. Signal quality should win first because the team does not yet know which failure mechanism is real.
- Capture artifacts: interview notes, clipped transcripts, prioritized themes, and a decision summary after each round.

### Decision impact
Each method should unlock a specific decision. If interviews show permissions confusion, the product needs clearer role framing. If usability tests show sequence failure, the redesign should restructure the flow. If both are weak, the case-study narrative should stay honest and describe these as open gaps rather than measured outcomes.

## Why This Passed
- It separates known evidence from assumption.
- It ranks the gaps instead of giving a wish list.
- It maps gaps to methods, sample sizes, and decision outcomes.
- It keeps proof language honest by distinguishing directional signals from measured research.

## What Would Have Failed
- Saying to just do interviews.
- Treating support tickets as full user validation.
- Listing methods without explaining what decision each method changes.

## Revision Pass
The weak draft proposed surveys, interviews, and analytics without ranking them. The corrected version prioritized the unknowns that block the redesign and tied each method to a product decision.
