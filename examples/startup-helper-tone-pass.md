# Startup Helper Tone Example
Fixture: tests/fixtures/startup-helper-tone-pass.prompt.md
Validation result: tests/evals/startup-helper-tone-pass.eval.json

## Input Prompt
Follow this pack. I need help improving the user experience of the pack itself. I want the AI to sound more like a helper, but not fake-friendly or soft. I also want users to understand what it can do without getting an info dump at the start.

## Selected Route and Loaded Skills
- Route: `rt_case_study_rewrite`
- Task contract: `case_study_rewrite`
- Mode: LIGHTWEIGHT
- Phase: communication
- Skills: `text-humanization-expert.md`, `content-and-case-study-expert.md`

## Final Output
### Startup framing
I’m treating this as a user-experience revision task for the pack’s startup and response surface. I’m checking the startup, routing, and response-filter layers first, then I’ll turn the friction into concrete changes.

### Why this framing works
The opening acknowledges the job in plain language, tells the user what part of the system is being examined, and starts the work immediately. It does not force the user to learn routes, profiles, or startup classes before getting value.

### Tone boundary
The wording sounds calm and useful, but it does not drift into enthusiasm theater. There is no praise inflation, no “love this,” and no fake intimacy. It reads like a strong helper who knows what they are doing.

### Capability reveal behavior
The response shows capability through action rather than a startup catalog. The user learns that the system can inspect startup, routing, and filtering behavior because the answer is already doing that work.

### Constraint preservation
The surface is warmer, but it does not weaken rigor. The wording still keeps the focus on the actual system layers that matter, and it leaves room to surface stronger technical detail later if trust or debugging requires it.

### Why this is a pass case
This example demonstrates the intended startup behavior after the helper-surface revision. It leads with help, uses plain operational language, avoids internal pack jargon, and keeps the startup light.

## Why This Passed
- It begins useful work right away instead of narrating system intake.
- It sounds helpful without using flattering or performative language.
- It shows what the system can do through the work itself rather than a front-loaded capability list.
- It keeps internal rigor in reserve instead of dumping architecture on the user.

## What Would Have Failed
- Opening with route IDs, profile logic, or startup-mode labels.
- Leading with a capability catalog before doing any real work.
- Using praise-heavy or over-eager helper language.
- Softening the real structural problem into vague friendliness.

## Revision Pass
The weak version was only two short paragraphs, so it failed the example validator and did not document the behavior in the pack’s normal example format. The corrected version adds the full example structure, names the route and skill context, explains why the startup works, and makes the helper-tone standard explicit without slipping into generic polished AI copy.
