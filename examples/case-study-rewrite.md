# Case Study Rewrite Example
Fixture: tests/fixtures/case-study-rewrite.prompt.md
Validation result: tests/evals/case-study-rewrite.eval.json

## Input Prompt
Rewrite this project summary so it reads like a credible case study for a reasoning-driven design tool, not a polished artifact recap.

## Selected Route and Loaded Skills
- Route: `rt_case_study_rewrite`
- Task contract: `case_study_rewrite`
- Mode: REBUILD
- Phase: communication
- Skills: `content-and-case-study-expert.md`

## Final Output
### Problem
The project originally explained the system well but did not prove why it mattered. That made the work feel like a disciplined internal exercise instead of a tool that clearly improves decision quality. The result was a narrative with structure but without enough proof weight for a skeptical reviewer.

### Process
The rebuild separated pack logic from value proof, added a locked project workspace, introduced benchmark and comparison files, and tightened the validator so shallow-but-compliant answers could not pass on structure alone. That process matters because the pack’s claim is not just “organized outputs.” It is better routed, more reliable reasoning. The work also added worked examples, route mirrors, and release gates so the system could be inspected by both humans and tooling.

### Solution
The new case-study structure leads with the problem, then shows the operator architecture, then the proof stack, then the open gaps. It also makes the claim-to-proof chain visible so each major statement can be interrogated instead of trusted on tone. The tradeoff is narrative smoothness versus evidentiary honesty. Honesty wins, because overstating validation would directly undercut the product claim.

### Outcome and proof
The project now has executable validation, real worked examples, a benchmark structure, and a clearer claim-to-proof chain.
It also has a cleaner separation between pack logic proof and product-value proof, which keeps internal rigor from being mistaken for market validation.
What remains open is live external value proof.
That gap is stated directly instead of hidden behind polished language.

## Why This Passed
- The rebuilt structure appears before meta commentary.
- It distinguishes what was fixed from what remains open.
- It uses evidence language carefully and does not let proxy proof read like user-tested proof.
- It includes an explicit honesty-versus-smoothness tradeoff.
- It tells a reviewer where to interrogate the proof instead of smoothing over the weak spots.

## What Would Have Failed
- A findings-only rewrite.
- Portfolio storytelling with no proof chain.
- Calling the project validated without live evidence.
- Hiding open gaps inside soft, promotional summary language.

## Revision Pass
The weaker version spent too long on how the pack felt.
The revision moved the problem, process, solution, and outcome into a tighter order so the value claim can be interrogated.
It also added the proof-boundary language that keeps internal discipline from being misread as external validation.
