# LAUNCH_TEXT_HUMANIZATION_REVISION

Use this as the single-file launcher for **Text Humanization Revision**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_BRAND.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_text_humanization`
- Use when: Use when the governing need is prose-quality revision rather than structural rewriting or route-level diagnosis.
- Visual input supported: no
- Known tension: natural texture vs semantic drift
- Known tension: voice preservation vs generic polish
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_case_study_rewrite`

## Included skill logic
- Governing: `text-humanization-expert.md` - Use this skill to revise prose so it sounds authored, readable, and natural without changing meaning, adding claims, or flattening the writer’s voice.
- Governing: `content-and-case-study-expert.md` - Use this skill to audit, rewrite, expand, or structure UX copy, design rationale, documentation, and case-study writing without losing clarity, mode control, or evidence.
- Optional support: `brand-strategy-expert.md` - Use this skill to make strict positioning, audience-fit, trust-signal, convention, and brand-vs-interface decisions. Treat brand work as a system of falsifiable hypotheses, not a moodboard.

## Runtime summaries
- `dist/runtime/summaries/text-humanization-summary.md`
- `dist/runtime/summaries/writing-and-case-study-summary.md`
- `dist/runtime/summaries/audience-and-industry-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Job of the piece  (Identifies what the text must still do after revision.)
  ## Pattern scan  (Shows what felt machine-shaped or repetitive.)
  ## Meaning-preservation guard  (Protects against semantic drift or tone replacement.)
  ## Revised passage  (Shows the rewritten prose.)
  ## Why this reads more human  (Explains the revision logic instead of asserting it.)

- Required section: Job of the piece
- Required section: Pattern scan
- Required section: Meaning-preservation guard
- Required section: Revised passage
- Required section: Why this reads more human
- Required evidence: meaning guard
- Required evidence: pattern note
- Required evidence: before/after revision rationale
- Required decision: job_of_piece
- Required decision: pattern_scan
- Required decision: meaning_guard
- Required decision: revision_sequence
- Required decision: voice_guard
- Hard fail signal: rewrite for difference only
- Hard fail signal: casualize it more
- Hard fail signal: make it sound human somehow
- Soft fail signal: a bit more natural
- Soft fail signal: less robotic

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Text Humanization Revision. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
