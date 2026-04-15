---
summary_version: 2.0.0
source_reference:
  - src/knowledge-base/source-docs/UX Cognition Expert Research.md
  - src/knowledge-base/source-docs/Design Strategy and Communication Research.md
last_updated: 2026-04-13
synchronized: true
domain: ux-cognition
---

# UX Cognition Summary

## Cognitive load framework

Three load types with design responses:

| Task complexity | Interface density | Load class | Required design response |
|---|---|---|---|
| Low (linear) | Low | Baseline | Focus on clarity and aesthetic-usability |
| Low (linear) | High | Extraneous-heavy | Aggressive de-cluttering; use proximity grouping |
| High (relational) | Low | Intrinsic-heavy | Scaffolding; contextual help; worked examples |
| High (relational) | High | Critical overload | Mandatory progressive disclosure; split task |

Working memory threshold: ~4 chunks for novel unorganized data (Cowan); 7±2 for organized familiar content (Miller). Design for the lower bound.

Chunking rule: group related items so each group reads as one chunk. Never require users to hold more than 4 unrelated items in mind simultaneously.

## Mental model alignment

- Violation signal: users attempt interactions the system does not support, or avoid interactions the system requires
- New model cost: 3–5 repetitions before a new pattern begins to automate; design must signal the new pattern clearly on first encounter
- Gap detection test: if a user cannot predict what a control does before activating it, the mental model is broken
- Preservation rule: when a system is already established, preserve existing patterns before introducing new ones

## Heuristics with testable criteria

Nielsen severity scale: 0 (not a problem) → 4 (usability catastrophe). Severity 3–4 requires fix before release.

Critical testable violations:
- **Visibility of system status**: no loading indicator when latency >1s → severity 3
- **Match between system and world**: labels or icons that require domain knowledge the user does not have → severity 2–4
- **User control and freedom**: no undo, no cancel, no back → severity 3–4
- **Error prevention**: irreversible action with no confirmation → severity 3–4
- **Recognition over recall**: requiring users to remember information from a previous screen → severity 2–3

Hick's Law threshold: RT = b × log₂(n+1). For n > 7 choices, decision time increases significantly. Above 7 options, group or filter before presenting.

Fitts's Law implication: target acquisition time increases with distance and decreases with size. CTA minimum touch target: 48×48dp. Primary actions belong near the user's natural resting position.

## Scanning behavior

| Pattern | Trigger conditions | Layout rules |
|---|---|---|
| F-pattern | Text-heavy, list content, low visual hierarchy | Critical info top-left and first line; left rail carries navigation |
| Z-pattern | Marketing, simple pages, strong visual hierarchy | Corners are anchor points; CTA at Z-endpoint (bottom right) |
| Layer cake | Structured content with clear headings | Headings must carry meaning; users skip body if heading is weak |
| Spotted | High visual contrast, images, charts | Visual anchors determine reading entry; caption/label must accompany |

Reading gravity rules:
- Users exit a block of text at the bottom; place next action there
- Left edge carries more attention than right edge in Western left-to-right reading
- Above-the-fold: if the user's primary question is not answered in the first viewport, bounce rate increases

## Decision fatigue and choice architecture

- Choice overload threshold: >7 options in an undifferentiated list degrades decision quality
- Default selection rule: pre-select the most common or safest option; don't default to a blank or dangerous choice
- Option sequencing: place recommended option first or visually accent it; don't make users search for the best choice
- Destructive confirmation pattern: confirmation dialog must name the specific thing being destroyed; "Are you sure?" alone is insufficient - severity 3

## Attention cost and interruption

- Tolerable interruption duration: ≤2 seconds for non-critical notifications
- Interruption recovery time: 23 minutes average to fully return to a deep task after an interruption
- Modal rules: modals are justified only when the user must make a decision before proceeding; informational modals that can be dismissed are almost always wrong
- Toast/snackbar timing: 4–7 seconds for confirmations; must not obscure primary actions
- Interruption timing rule: never interrupt at the moment of task commitment (form submission, confirm click)

## Error recovery

Prevention vs. recovery decision:
- Prevent when: action is irreversible, data loss is likely, or the error is predictable from input pattern
- Recover when: error is only detectable after submission or when prevention would create excessive friction

Validation timing rules:
- Inline validation: trigger on blur (field exit), not on keystroke (too aggressive)
- Form-level validation: trigger on submit; show all errors simultaneously, not one at a time
- Error message must contain: what went wrong + why + how to fix it

Error message failure: generic messages ("Something went wrong") are severity 3 - they give users no recovery path.

## Cognitive failure pattern catalogue

1. **The Ghosting Placeholder**: placeholder text disappears on focus before user can read it - violates recognition over recall
2. **Mystery Meat Navigation**: icon-only nav with no label - violates match between system and world
3. **The Scolding on Blur**: aggressive inline error triggered while user is still typing - increases extraneous load
4. **The Blind Man's Error**: "An error occurred" with no actionable detail - prevents error recovery
5. **The Context Switch Penalty**: forcing user to navigate away to get information needed for the current task - violates working memory limit
6. **The Analysis Paralysis Feed**: undifferentiated list of >10 options with no default or recommendation - triggers choice overload
7. **The Vanishing Progress Bar**: progress indicator that resets or disappears mid-flow - breaks system status visibility
8. **The Memory Trap**: asking user to re-enter information from a previous step - violates recognition over recall
9. **The Action-Momentum Interruption**: confirmation modal triggered immediately after user commits - violates task flow momentum
10. **The Jargon Fortress**: interface labels only decipherable by domain experts in a product used by novices - violates match between system and world
