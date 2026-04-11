# UI Structure Critique Example
Fixture: tests/fixtures/ui-structure-critique.prompt.md
Validation result: tests/evals/ui-structure-critique.eval.json

## Input Prompt
Audit this pricing page hero and first three sections. The page has a strong visual style but users are not finding the primary action fast enough, the feature grid feels crowded, and the enterprise proof is buried.

## Selected Route and Loaded Skills
- Route: `rt_ui_structure_critique`
- Task contract: `ui_structure_critique`
- Mode: AUDIT
- Phase: structure
- Skills: `ui-system-expert.md`, `grid-system-expert.md`
- Known tensions: density vs readability, brand expression vs task clarity

## Final Output
### Problem framing
The page is not failing because it lacks polish. It is failing because the hierarchy spends its first attention burst on mood instead of decision support. The user needs to know what the product is, whether it is for them, and where to act within the first scan.

### Findings
1. The hero headline is broad while the subhead tries to do product, proof, and differentiation at once. That creates a slow first parse.
2. The primary CTA competes with a decorative secondary treatment, so the “act now” path is visually diluted.
3. The feature grid introduces too many parallel cards before the enterprise trust layer appears. That is a density problem, not a copy-only problem.
4. The strongest proof element is below the feature grid. That forces the user to commit attention before credibility is earned.

### Recommendations
- Collapse the hero into one clear value proposition, one support line, and one dominant CTA because the first decision moment should resolve in under one scan.
- Move one enterprise proof block directly under the hero. This preserves the brand tone while letting credibility arrive before the dense grid.
- Reduce the feature grid from six equal-priority cards to three grouped capability clusters. The tradeoff is breadth versus clarity. Clarity should win first because scan time is the active constraint.
- Demote decorative secondary actions until the primary path becomes unambiguous. The obvious alternative is to keep both CTAs visually loud, but that preserves the current indecision.

### Tradeoffs
This recommendation sacrifices some immediate “full product breadth” in order to improve decision speed and first-scan comprehension. Preserve the visual identity, but flex information density first because the user cannot evaluate the broader offer until the primary path is legible.

## Why This Passed
- It names the real structural failure instead of calling the page “busy” in a vague way.
- It links each recommendation to a user-task consequence.
- It includes an explicit tradeoff and why the obvious alternative loses.
- It gives a rebuild order that a designer can act on immediately.

## What Would Have Failed
- Saying the page “looks strong overall” and then offering only cosmetic spacing changes.
- Recommending more visual emphasis everywhere instead of choosing a hierarchy winner.
- Claiming the hero is “validated” without any scan or click evidence.

## Revision Pass
The weak draft focused on “make the CTA blue and add more whitespace.” The corrected version moved the diagnosis up a level: the problem is first-scan hierarchy, so the safer fix is to reduce equal-priority signals before touching style tokens.
