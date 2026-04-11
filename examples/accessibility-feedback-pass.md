# Accessibility Feedback Audit Example
Fixture: tests/fixtures/accessibility-feedback-pass.prompt.md
Validation result: tests/evals/accessibility-feedback-pass.eval.json

## Input Prompt
Audit this checkout flow for accessibility. Keyboard users are getting lost after promo code entry, the address error message is not announced, and the fixed footer CTA may be trapping focus on mobile.

## Selected Route and Loaded Skills
- Route: `rt_accessibility_feedback_audit`
- Task contract: `accessibility_feedback_audit`
- Mode: AUDIT
- Phase: accessibility
- Skills: `accessibility-feedback-expert.md`, `ui-system-expert.md`
- Known tensions: strict repair vs release speed, visual cleanliness vs semantic clarity

## Final Output
### Access failure framing
The flow is failing at the point where a user has to recover from an error and continue the transaction. This is not only a visual polish issue. It is a blocked behavior issue because keyboard users can lose their place, and screen reader users do not get a reliable announcement when the address field fails.

### Barrier inventory
1. Focus returns to the promo field after submission instead of moving to the first invalid address field. That breaks expected tab order and increases recovery time.
2. The address error is rendered visually, but the error state is not exposed through an aria relationship or announcement pattern. A screen reader can miss the failure entirely.
3. The fixed footer CTA appears to stay in the reading sequence even when a modal-like sheet opens on mobile. That risks a focus trap and weakens escape behavior.
4. Success and error states rely too heavily on color. The user needs an icon and label pair, not just a red field treatment, because non-color semantics should carry the meaning.

### Repair priorities
- First, move focus to the first invalid field after submit and announce the error summary because recovery behavior is the highest-risk blocker.
- Then connect each field error with an explicit label, description, and screen reader announcement so the user hears both what failed and what to do next.
- Third, make the fixed footer CTA inert to keyboard focus while the sheet is active. The tradeoff is a slightly stricter focus model versus faster implementation. The stricter model should win because the current trap risk blocks checkout completion.
- Finally, add non-color support to status messaging with an icon and text pair instead of a color-only cue.

### Verification method
Verify the repair with a keyboard-only pass, a screen reader pass, and an automated axe check. Test that tab order lands on the first invalid field, that the announcement reads the address error, and that focus cannot escape to the footer CTA while the sheet is open.

## Why This Passed
- It names blocked user actions instead of calling the flow merely confusing.
- It uses standards and behavior language like focus, screen reader, aria, and non-color meaning.
- It gives an ordered repair path and a verification method.
- It resolves the tradeoff instead of keeping release speed and behavior safety equal.

## What Would Have Failed
- Suggesting a brighter error color and calling the issue solved.
- Deferring keyboard and screen reader work to a later pass.
- Claiming the flow is accessible without a verification method.

## Revision Pass
The weak draft said to improve accessibility by increasing contrast and making the error redder. The corrected version moved to the real failure: recovery behavior, announcement logic, and focus control.
