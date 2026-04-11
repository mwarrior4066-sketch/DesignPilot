# Type System Recommendation Example
Fixture: tests/fixtures/type-system-pass.prompt.md
Validation result: tests/evals/type-system-pass.eval.json

## Input Prompt
Recommend a type system for a dense operations dashboard and supporting case-study page. The current file mixes arbitrary sizes, labels are hard to scan, and long-form explanation text feels cramped.

## Selected Route and Loaded Skills
- Route: `rt_type_system_recommendation`
- Task contract: `type_system_recommendation`
- Mode: REBUILD
- Phase: tokens
- Skills: `type-system-expert.md`, `accessibility-feedback-expert.md`
- Known tensions: brand personality vs reading efficiency, density vs legibility

## Final Output
### Reading context
The dashboard is scan-heavy and dense, while the case-study page is long-form and narrative. One font decision will not solve both unless the system separates role logic from surface style. The recommendation needs to support fast label reading in the dashboard and sustained body reading in the case study.

### Scale and role map
- Use a clear role map: display, section heading, body, label, meta, and data emphasis.
- Keep dashboard labels and table text on a tighter but still readable scale, while narrative body copy uses a more generous line-height and line length.
- Tie type tokens to roles instead of page-by-page overrides.
- Reserve strong weight contrast for headings and key metrics, not for every secondary label.

### Readability rules
Body copy should stay within a readable line length threshold such as 45-75 characters when possible. Dashboard labels need enough contrast, line-height, and spacing to survive quick scan conditions. The obvious alternative is to tighten everything and use a single compact scale, but that preserves the current cramped long-form reading. Instead, let role and context drive the scale. The tradeoff is a slightly wider long-form setting versus maximum density. Readability should win for the narrative surface, while compactness can win in the data surface.

### Adoption guidance
Phase the system by mapping current text styles to roles first, then replace one-off sizes. Keep existing brand voice through typeface choice if needed, but migrate hierarchy with tokens and role names so future additions stay consistent.


- Additional note: labels in dense tables should not borrow the same emphasis pattern as headings.
- Verification note: review one dashboard table and one long-form section after migration to confirm the role map holds.

## Why This Passed
- It separates reading contexts instead of giving a single-font answer.
- It creates a reusable role map.
- It uses measurable readability language like line length and density.
- It explains what changes first during adoption.

## What Would Have Failed
- Suggesting a nicer font and tighter tracking with no system logic.
- Using precise px numbers without context or thresholds.
- Treating dashboard labels and long-form copy as the same reading environment.

## Revision Pass
The weak draft recommended a modern grotesk at one compact size for everything. The corrected version split the problem by reading context and rebuilt the type system around roles and readability.
