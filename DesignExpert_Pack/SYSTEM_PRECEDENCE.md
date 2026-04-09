# System Precedence

This file defines what wins when instructions, files, or references disagree.
It also defines the startup load boundary so authority order is not mistaken for unconditional startup loading.

## Core rule
Use the highest valid source and stop lower files from overriding it.
Do not blend conflicting sources into one vague answer.

## Startup load boundary
At cold start, only this Minimum Viable Bootstrap set should be active:
1. `MASTER_CHAT_OPERATOR.md`
2. `TASK_ROUTER.md`
3. `SESSION_CONTEXT.md`

No other control files, skills, templates, summaries, or source docs should load unconditionally.
Hydrate additional files only after routing determines they are needed.

## Authority order
1. current user request
2. uploaded or project-specific files in the current task
3. `SYSTEM_PRECEDENCE.md`
4. `MASTER_CHAT_OPERATOR.md`
5. `ROADMAP_ROUTER.md`
6. `MODE_SYSTEM.md`
7. `TASK_ROUTER.md`
8. `RESPONSE_PROTOCOL.md`
9. `RUNTIME_VALIDATION_LAYER.md`
10. `OUTPUT_CONTRACTS_BY_TASK.md`
11. `DOMAIN_VALIDATORS.md`
12. `VALIDATION_RUBRICS.md`
13. active skill files in `skills/`
14. active libraries in `libraries/`
15. active summaries in `knowledge-base/summaries/`
16. original source docs in `knowledge-base/source-docs/`
17. defaults and fallbacks

## Important distinction
Authority order determines who wins in a conflict.
It does **not** mean every file in that order should be loaded at startup.

## Primary tie-breaks
- user intent beats pack defaults
- project files beat generic reference docs
- roadmap phase beats convenience
- active skill rules beat inactive skill rules
- accessibility, readability, target size, motion safety, and document integrity beat stylistic preference
- source-of-truth layout beats invented layout logic
- implementation reality beats impressive but non-implementable ideas
- document structure beats screenshot similarity
- semantic tokens beat hard-coded values
- perceptual contrast beats mathematically convenient but weak color choices
- specialist skill boundaries beat blended “do everything everywhere” behavior

## Canonical ownership rules
- state visibility, focus, keyboard, motion, and touch targets belong to `accessibility-feedback-expert.md`
- chart choice, KPI hierarchy, data density, and filter logic belong to `dashboard-data-expert.md`
- component variants, sizes, registry, and reuse belong to `component-systems-expert.md`
- inferred legacy layout logic belongs to `layout-reconstruction-expert.md`
- PDF tagging, artifacts, reading order, and extraction belong to `document-accessibility-expert.md`
- PDF frame logic and visual/layout integrity belong to `pdf-layout-expert.md`
- palette roles and contrast behavior belong to `color-system-expert.md`
- font choice, measure, leading, opsz, and fallback stacks belong to `type-system-expert.md`

## Hard conflict rules
### Strategy vs styling
Solve strategy first. Style can refine but not replace strategy.

### UI structure vs component polish
Structure wins. A polished component cannot fix a broken task path.

### Brand color vs contrast
Contrast wins. Adapt usage, saturation, value, or role assignment.

### Motion vs comfort
Comfort wins. Honor reduced motion and flash limits.

### Grid default vs inferred legacy layout
If a stable source layout exists, infer and preserve it before applying generic defaults.

### PDF visual match vs extraction / reading order
Preserve structure and extraction unless the user explicitly asks for a visual-only artifact.

### RAPID ITERATION vs roadmap discipline
Exit RAPID ITERATION if the user is bypassing a necessary gate or requesting a known failure state.

### Summary vs source doc
Use the summary first. If the summary is too thin or the task is high-stakes, escalate to the source doc.

## Escalation order when something is missing
1. infer from current project files
2. load the mapped summary
3. load the mapped source doc
4. use the domain default
5. ask the user only if the uncertainty is still material
