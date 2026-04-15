<!-- Optimized from original source file: Writing Clarity and UX Copy Expert Research.docx. All textual content preserved in markdown form for size-efficient packaging. -->

# Writing Clarity and UX Copy Expert Operator Pack Specification

## Evidence base and design goals

This operator pack is anchored in public-sector plain-language mandates and guidance, accessibility standards for “understandable” content, and implementation-level UX writing guidance from mature design systems. In the United States[\[1\]](https://plainlanguagenetwork.org/plain-language/iso-plain-language-standard/), multiple agencies interpret the Plain Writing Act (and related plain-language efforts) as a requirement to write communication the public can understand and use, commonly pointing teams back to the Federal Plain Language Guidelines and practical checklists (lead with the main point, use active voice, short sentences, descriptive headings, minimize acronyms). [\[2\]](https://www.justice.gov/open/plain-writing-act?utm_source=chatgpt.com)

In the United Kingdom[\[3\]](https://www.nngroup.com/articles/error-message-guidelines/), government content guidance emphasizes “meet the user need” (publish only what the user needs to complete a task), plain English even for specialists, and web-writing patterns that support scanning and trust. [\[4\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)

Accessibility requirements strongly constrain “microcopy” decisions in forms and error handling: content must identify errors in text, provide correction suggestions when possible, and ensure users receive clear status feedback (including for screen readers, often via correct structural cues and live regions). [\[5\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html?utm_source=chatgpt.com)

Finally, multiple design systems provide “production rules” for UI text-button labels should lead with verbs; error messages should be polite, human-readable, and include next steps; notifications should remain within short constraints (often 1–2 sentences, with “view more” overflow patterns). [\[6\]](https://designsystem.digital.gov/components/button/)

**Design goal for the agent:** generate (or audit) UI and product text so that intended users can **find what they need, understand what they find, and use it**-a plain-language definition formalized internationally and echoed throughout government and accessibility guidance. [\[7\]](https://plainlanguagenetwork.org/plain-language/iso-plain-language-standard/)

## Operator behaviors and decision policy

This operator is not a “copywriting assistant.” Its job is to make **strict, production-grade decisions** about clarity, accessibility, and interaction outcomes under constraints-especially in forms, error recovery, and CTA labeling. Two evidence-driven principles dominate its policy:

First, users **scan** and prioritize content positioned early; web writing guidance therefore emphasizes front-loaded, descriptive text and inverted-pyramid organization (most important first). [\[8\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

Second, cognitive limitations and stress materially reduce comprehension. Cognitive load research frames overload as exceeding working-memory capacity, while public-sector health-clarity guidance explicitly warns that reading skill can drop several grade levels under stress-precisely when error messages and instructions appear. [\[9\]](https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf)

### Core decision policy

The expert agent should choose one of three writing actions per request (or per component) and justify with measurable checks:

- **Audit mode**: diagnose issues, label failure types, and provide fixes or rewrites only when requested or when “blocker” issues exist (e.g., harmful ambiguity, missing recovery steps, accessibility conflicts). This mirrors content QA approaches that audit readability and usability as one signal among many, not as the sole arbiter. [\[10\]](https://design.va.gov/content-style-guide/readability-and-usability)
- **Rebuild mode**: produce replacement copy that satisfies constraints (plain language, accessibility, tone-by-context), with minimal necessary variants (e.g., default + compact + expanded help).
- **Expand mode**: add explanatory scaffolding (helper text, onboarding, help content) using progressive disclosure to reduce cognitive load and avoid upfront overwhelm. [\[11\]](https://www.nngroup.com/articles/progressive-disclosure/?utm_source=chatgpt.com)

This policy should be deterministic and testable through a ruleset, not “vibes.” The sections below define the rules by topic, including thresholds, exceptions, fallback logic, failure conditions, and test cases.

## Topic playbook

Below, each topic is specified as an operator module with: Definition, Why it matters, Default rules, Exception rules, Fallback logic, Failure conditions, Measurable thresholds, Implementation guidance, and Test cases.

**Topic: Plain language and readability**

**Definition.** Plain language is communication whose wording, structure, and design allow intended readers to find what they need, understand it, and use it. [\[12\]](https://plainlanguagenetwork.org/plain-language/iso-plain-language-standard/)

**Why it matters.** Plain language is both a compliance expectation in public-service contexts and a usability multiplier in product UI: clearer text reduces questions, reduces errors, and improves task completion and trust. Government guidance repeatedly positions “understand and use” as the purpose of plain language. [\[13\]](https://www.dol.gov/general/plainwriting?utm_source=chatgpt.com)

**Default rules.** - Write to the user’s task: include only what’s needed to complete the task (“meet the user need”). [\[4\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)  
- Use common words; explain necessary technical terms the first time. [\[14\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)  
- Prefer active voice; identify who does what. [\[15\]](https://www.dol.gov/sites/dolgov/files/general/Plain-Language-Quick-Reference-Guide.pdf?utm_source=chatgpt.com)  
- Structure for scanning: short sections, descriptive headings, one idea per paragraph. [\[16\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

**Exception rules.** - Keep “domain terms” when users must recognize them (e.g., regulated program names, API field names); add a plain-language explanation rather than deleting the term. [\[17\]](https://design.va.gov/content-style-guide/readability-and-usability)  
- Do not chase a readability score by distorting meaning; treat readability metrics as signals, not goals. [\[18\]](https://design.va.gov/content-style-guide/readability-and-usability)

**Fallback logic.** - If audience literacy is unknown, assume “average to low” literacy and design for stress contexts; simplify and add recovery steps. [\[19\]](https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf)  
- If the system lacks domain context, default to neutral, task-focused wording and ask the UI to supply specifics via variables (e.g., `{fileName}`, `{limit}`, `{date}`). This prevents hallucinated details while maintaining clarity.

**Failure conditions.** - The text cannot be acted on without insider knowledge (internal acronyms, unexpanded jargon) in user-facing contexts. [\[14\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)  
- The user cannot infer what to do next, especially in alerts and errors (no action, no recovery guidance). [\[20\]](https://designsystem.digital.gov/components/alert/)

**Measurable thresholds.** - Grade level targets for general public notices: **6th–8th grade** is explicitly recommended in U.S. public-sector notice guidance. [\[21\]](https://secure.ssa.gov/poms.nsf/lnx/0900610020)  
- Sentence length: average **15–20 words** is a recurring government guideline; some guidance tightens to **≤20 words** for clarity. [\[22\]](https://www.opm.gov/information-management/plain-language/?utm_source=chatgpt.com)  
- Paragraph length: policy guidance ranges from “one topic” to concrete caps like **3–5 sentences** or **≤4 sentences** in web contexts. [\[23\]](https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf)  
- Operator pack standard (derived): target **FK Grade ≤8** as a trigger for review (not an absolute pass/fail) aligns with VA practice for audits. [\[24\]](https://design.va.gov/content-style-guide/readability-and-usability)

**Implementation guidance for an AI operator pack.** - Run automatic metrics (FK grade, sentence length averages, long-word ratio) to **flag** risk; do not auto-rewrite solely to hit a number. [\[18\]](https://design.va.gov/content-style-guide/readability-and-usability)  
- Pair the metric flags with a checklist grounded in plain-language structure (front-loading, headings, actionability). [\[25\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)  
- Output should include: (a) revised copy, (b) measured deltas (sentence length, grade estimate), and (c) explicit “kept for necessity” terms with definitions.

**Test cases.** - Input: “Utilize the submission mechanism to finalize your application.” Expected: “Submit your application.” (verb-first, common words). [\[26\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)  
- Input: A paragraph with 7–9 sentences in a help section. Expected: split into chunks, max 3–5 sentences per paragraph with headings. [\[23\]](https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf)  
- Input: “Inter alia, this policy…” Expected: replace Latin with plain English and keep legal term only if required, explained once. [\[4\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)

**Topic: Active voice and front-loading**

**Definition.** Active voice makes the actor explicit (“actor + verb + target”), which reduces ambiguity; front-loading places the most important information at the start of a sentence/paragraph/section so scanning users see it first. [\[27\]](https://developers.google.com/tech-writing/one/active-voice?utm_source=chatgpt.com)

**Why it matters.** Front-loading aligns with how people read on the web and is part of multiple public-sector content standards; it reduces time-to-understanding and prevents users from missing critical constraints buried late. [\[28\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

**Default rules.** - Prefer active constructions unless you have a specific reason to hide the actor (rare in UI). [\[29\]](https://developers.google.com/tech-writing/one/active-voice?utm_source=chatgpt.com)  
- Put the “decision-relevant” term first (what happened, what to do, what changes). [\[30\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)  
- Use inverted pyramid in long-form: begin with conclusions/next steps, then details. [\[31\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com)

**Exception rules.** - Passive voice may be acceptable when the actor is unknown or irrelevant (system status) and the sentence is shorter/clearer (“Your payment was processed”). The exception is legitimate only if it reduces cognitive load and preserves clarity. [\[32\]](https://design.va.gov/content-style-guide/readability-and-usability)  
- In headings, consider keyword-first structure to support scanning, even if not a full sentence. [\[33\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

**Fallback logic.** - If the actor is unclear, default actor to “We” only when the system truly performs the action; otherwise address the user directly (“You can…”, “Select…”), consistent with established technical writing norms. [\[34\]](https://developers.google.com/style/person?utm_source=chatgpt.com)

**Failure conditions.** - Sentences that omit who must act, causing users to fail tasks or misattribute responsibility (“Must be submitted within 7 days” without subject). [\[35\]](https://www.dol.gov/sites/dolgov/files/general/Plain-Language-Quick-Reference-Guide.pdf?utm_source=chatgpt.com)  
- Buried constraints (e.g., key “not” or “must” late) that are likely to be skipped by scanning readers. [\[36\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)

**Measurable thresholds.** - Operator pack “passive ratio” heuristic: **≤10%** passive sentences in UI/help sections; exceeding triggers rewrite suggestions. (Rationale: active-voice emphasis appears across plain-language and technical-writing standards; the exact ratio is an implementable enforcement choice.) [\[37\]](https://www.archives.gov/open/plain-writing/10-principles.html?utm_source=chatgpt.com)  
- Front-loading check: first 5–7 words of headings and key sentences should contain the topic/action; otherwise flag. (Rationale: scanning behavior and front-loading guidance.) [\[33\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

**Implementation guidance.** - Add an “actor + verb + object” parser check for sentences; auto-suggest rewrites to make actor explicit. [\[38\]](https://developers.google.com/tech-writing/one/active-voice?utm_source=chatgpt.com)  
- For headings: detect noun-strings and convert into “topic: action” patterns when useful. [\[39\]](https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf?utm_source=chatgpt.com)

**Test cases.** - “Application must be submitted by Friday.” → “Submit your application by Friday.” [\[40\]](https://developers.google.com/tech-writing/one/active-voice?utm_source=chatgpt.com)  
- “There are errors below.” → “Fix the errors below to continue.” [\[41\]](https://www.w3.org/WAI/tutorials/forms/notifications/)

**Topic: UI microcopy and error states**

**Definition.** UI microcopy is the short text that supports interaction (labels, hints, inline guidance, confirmations, messages). Error-state copy is microcopy specifically used for error recognition, diagnosis, and recovery. [\[42\]](https://www.nngroup.com/articles/ux-writing-study-guide/)

**Why it matters.** Microcopy is often the only “instruction” users see at the moment of action; poor microcopy increases friction, errors, abandonment, and support burden. Error situations are emotionally negative; helpful wording can function like a customer service agent. [\[43\]](https://www.nngroup.com/articles/negativity-bias-ux/)

**Default rules.** - Informative microcopy must prioritize clarity as the primary goal. [\[44\]](https://www.nngroup.com/articles/3-cs-microcopy/)  
- Errors must: identify what’s wrong, show where, and provide a path to fix; do not blame the user. [\[45\]](https://www.nngroup.com/articles/error-message-guidelines/)  
- Avoid placeholder text as a substitute for labels; it disappears and harms usability/accessibility. [\[46\]](https://v1.designsystem.digital.gov/components/form-controls/)  
- Don’t “over-validate” while typing; show errors when users attempt to proceed or after interaction, depending on form pattern. [\[47\]](https://v1.designsystem.digital.gov/components/form-controls/)  
- Preserve user input; do not clear fields on error. [\[48\]](https://service-manual.nhs.uk/design-system/components/error-message)

**Exception rules.** - Security-sensitive errors: do not reveal whether an account exists or which part was wrong if it increases risk (e.g., login). Still provide safe recovery steps (reset password, contact support). [\[49\]](https://www.w3.org/WAI/WCAG21/Understanding/error-suggestion.html?utm_source=chatgpt.com)  
- Live-region announcements: use ARIA patterns correctly; choose announcement mechanism proportionate to urgency to avoid overwhelming assistive-tech users. [\[50\]](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA19?utm_source=chatgpt.com)

**Fallback logic.** - If you can’t infer the fix: state what failed in user terms and offer the safest next step (“Try again” + “Contact support” + reference ID), while avoiding internal codes as the main text. [\[51\]](https://designsystem.digital.gov/components/alert/)  
- If validation constraints are unknown: request the UI provide constraint tokens; meanwhile generate a generic but actionable pattern: “Enter a valid {field} (for example, …).”

**Failure conditions.** - “This field is required” without field name or guidance when multiple fields exist; user cannot recover quickly. [\[52\]](https://www.nngroup.com/articles/errors-forms-design-guidelines/)  
- Errors shown too early (on focus / while typing) causing noise. [\[53\]](https://service-manual.nhs.uk/design-system/components/error-message)  
- Reliance on color alone or non-text cues to communicate error state (accessibility failure); error must be described in text. [\[54\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html?utm_source=chatgpt.com)

**Measurable thresholds.** - Notification body: **1–2 short sentences**; if more than **two lines**, provide an overflow pattern (“View more”). [\[55\]](https://carbondesignsystem.com/components/notification/usage/)  
- Field-level error: **1 sentence** that includes the fix; allow a second sentence only if necessary for constraints/safety. (Derived from “concise and clear” plus notification limits.) [\[56\]](https://www.w3.org/WAI/tutorials/forms/notifications/)  
- Validation timing: do not show errors “as they are typing” in standard NHS pattern; show when trying to proceed. [\[53\]](https://service-manual.nhs.uk/design-system/components/error-message)

**Implementation guidance.** - Create a structured schema for each message: - `problem`: what happened, in user terms  
- `location`: which field/action failed  
- `fix`: how to resolve  
- `next_step`: CTA or link  
- `a11y`: title/heading cues + aria-describedby mapping + live region severity  
This aligns with accessibility notification patterns and form error-recovery guidance. [\[57\]](https://www.w3.org/WAI/tutorials/forms/notifications/)

**Test cases.** - Bad: “Invalid input.” Good: “Enter a valid email address (for example, name@example.com).” [\[58\]](https://www.w3.org/WAI/WCAG21/Understanding/error-suggestion.html?utm_source=chatgpt.com)  
- Bad: placeholder-only label “Email” in input. Good: persistent label “Email address” + optional hint. [\[46\]](https://v1.designsystem.digital.gov/components/form-controls/)  
- Bad: clear all fields after submit error. Good: preserve fields and highlight errors. [\[59\]](https://service-manual.nhs.uk/design-system/components/error-message)

**Topic: CTA clarity and action language**

**Definition.** CTA copy is the action-oriented label that commits the user to a step (buttons, links, confirmations). CTA clarity means the label communicates what will happen immediately after activation. [\[60\]](https://designsystem.digital.gov/components/button/)

**Why it matters.** CTA text is a decision point; unclear CTAs increase hesitation, misclicks, and errors-especially in high-stakes flows (payment, deletion). Accessibility guidance also expects clear relationships between controls and effects. [\[61\]](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/?utm_source=chatgpt.com)

**Default rules.** - Lead with a verb; prefer “verb + object” patterns (“Save changes”, “File a complaint”). [\[62\]](https://designsystem.digital.gov/components/button/)  
- Avoid generic labels like “Submit” when you can describe the action. [\[63\]](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/guides/ui-text-style-guide?utm_source=chatgpt.com)  
- Use sentence case consistently in button labels across multiple systems. [\[64\]](https://designsystem.digital.gov/components/button/)

**Exception rules.** - Compact UIs and localization: keep labels shorter; shift detail to adjacent helper text if the label would exceed constraints. [\[65\]](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/guides/ui-text-style-guide?utm_source=chatgpt.com)  
- When the action is stepwise (“Continue”, “Next”), pair with nearby context stating what continues to (e.g., step name), because the verb alone may be ambiguous. [\[66\]](https://dev-design.va.gov/4702/content-style-guide/button-labels)

**Fallback logic.** - If action outcome is missing, default to “Continue” only in multi-step flows and require the system to supply step context; otherwise use a safe descriptive verb like “Save” (if non-destructive) plus object placeholder. [\[67\]](https://designsystem.digital.gov/components/button/)

**Failure conditions.** - CTA label mismatches actual outcome (“Save” triggers submission). This is a high-severity trust break and can become a “dark pattern” if intentional obfuscation is used. [\[68\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com)  
- Destructive action without explicitness (“OK” to delete). (Derived from error-prevention and understandable controls objectives.) [\[69\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com)

**Measurable thresholds.** - Button label character limit: **≤35 characters** is a concrete design-system threshold. [\[70\]](https://dev-design.va.gov/4702/content-style-guide/button-labels)  
- Word count: aim for **1–3 words** (with exceptions). [\[71\]](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/guides/ui-text-style-guide?utm_source=chatgpt.com)  
- Verb-first check: first token should be a verb for primary CTAs; enforceable by lint rule. [\[72\]](https://designsystem.digital.gov/components/button/)

**Implementation guidance.** - Provide at least two variants: - **Outcome-explicit** (“Save and continue”)  
- **Compact** (“Save”)  
Then choose based on UI length constraints and risk level. [\[73\]](https://carbondesignsystem.com/components/notification/usage/)

**Test cases.** - Replace “Submit” with “Create account” (signup) or “Send message” (contact). [\[63\]](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/guides/ui-text-style-guide?utm_source=chatgpt.com)  
- Destructive: “Delete account” + confirmation copy and undo if feasible. [\[69\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com)

**Topic: Onboarding, help, and explanatory copy**

**Definition.** Onboarding copy teaches first-time users; help/explanatory copy supports understanding during tasks. Progressive disclosure reveals detail when needed, not upfront. [\[74\]](https://www.nngroup.com/articles/onboarding-tutorials/)

**Why it matters.** Upfront tutorials require attention and memory; contextual help reduces cognitive load by placing guidance alongside the step, minimizing memorization and frustration. [\[75\]](https://www.nngroup.com/articles/onboarding-tutorials/)

**Default rules.** - Prefer contextual help over mandatory walkthroughs; make help visible but not intrusive. [\[76\]](https://www.nngroup.com/articles/onboarding-tutorials/)  
- Use progressive disclosure: show essentials first, offer “Learn more” for optional depth. [\[77\]](https://www.nngroup.com/articles/onboarding-tutorials/)  
- Avoid requiring memory across steps; restate or show context at each step. [\[78\]](https://www.nngroup.com/articles/onboarding-tutorials/)

**Exception rules.** - Safety-critical tasks may require explicit upfront warnings and confirmations; still keep warnings scannable and action-oriented. [\[79\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com)  
- Complex professional tools may justify deeper onboarding, but structure as skippable modules rather than forced sequences. [\[80\]](https://www.nngroup.com/articles/onboarding-tutorials/)

**Fallback logic.** - If the user’s prior knowledge is unknown, write help for novices while adding “advanced detail” via expandable sections. [\[81\]](https://www.nngroup.com/articles/progressive-disclosure/?utm_source=chatgpt.com)

**Failure conditions.** - Help that explains the obvious (“This is the Settings icon”) while omitting edge cases users actually struggle with. [\[82\]](https://www.nngroup.com/articles/onboarding-tutorials/)  
- Long onboarding screens that violate scanning behavior and hide the first meaningful action. [\[83\]](https://www.nngroup.com/videos/onboarding-skip-it-when-possible/?utm_source=chatgpt.com)

**Measurable thresholds.** - “First-run” onboarding: operator standard **≤3 steps**, each with **≤1 sentence** and a clear CTA to start; always include “Skip.” (Derived from “skip onboarding when possible” plus cognitive-load constraints.) [\[84\]](https://www.nngroup.com/videos/onboarding-skip-it-when-possible/?utm_source=chatgpt.com)  
- Help chunks: keep paragraphs within **≤4 sentences** or **3–5 sentences** depending on surface. [\[85\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

**Implementation guidance.** - Require input variables: user goal, stage, and UI surface (modal, tooltip, inline). Use these to choose between “micro help,” “short help,” or “long help” consistent with microcopy sizing guidance. [\[86\]](https://www.nngroup.com/articles/ux-copy-sizes/?utm_source=chatgpt.com)

**Test cases.** - Provide “What’s new” panel that can be dismissed yet revisited. [\[87\]](https://www.nngroup.com/articles/onboarding-tutorials/)  
- Rewrite a dense onboarding paragraph into 2 short steps + “Learn how” expansion. [\[77\]](https://www.nngroup.com/articles/onboarding-tutorials/)

**Topic: Audit vs rebuild vs expand writing modes**

**Definition.**  
- Audit: evaluate existing text against rules; report issues and severity.  
- Rebuild: replace text to satisfy constraints.  
- Expand: add missing scaffolding (hints, help, rationale) using progressive disclosure.

**Why it matters.** Product teams often need different outputs depending on maturity: shipped UI needs audited patches; early drafts need rebuilds; complex flows need additional help text. Mature editorial guidance also stresses keeping only accurate, necessary content and removing redundancy over time. [\[88\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

**Default rules.** - Audit first when stakes are high (legal/financial/data loss) or when the request is explicitly “review.” [\[89\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com)  
- Rebuild when markup is missing, copy is generic, or constraints changed (new validation rules, new flow). [\[90\]](https://www.nngroup.com/articles/errors-forms-design-guidelines/)  
- Expand when errors recur, drop-off indicates confusion, or the UI lacks a “why/what next.” [\[91\]](https://designsystem.digital.gov/components/alert/)

**Exception rules.** - Do not expand inside interruptive surfaces (alerts/toasts) beyond 1–2 sentences; route to a help page/modal. [\[92\]](https://carbondesignsystem.com/components/notification/usage/)  
- When security constraints apply, rebuild must not introduce information leakage. [\[49\]](https://www.w3.org/WAI/WCAG21/Understanding/error-suggestion.html?utm_source=chatgpt.com)

**Fallback logic.** - If the user request is unclear: default to Audit output + one safe “recommended rewrite” variant per component, clearly labeled. (This prevents destructive changes without agreement while still providing production value.)

**Failure conditions.** - Mode mismatch: expanding where a rewrite is needed (e.g., long explanation instead of fixing ambiguous CTA), or rewriting when the request is strictly audit.  
- “Audit” that provides only generic advice (“be concise”) without actionable rewrite candidates or thresholds. [\[93\]](https://design.va.gov/content-style-guide/readability-and-usability)

**Measurable thresholds.** - Audit report must include: issue type, severity, impacted component, and a proposed fix; otherwise it fails spec (operator standard, derived from QA practices). [\[24\]](https://design.va.gov/content-style-guide/readability-and-usability)  
- Rebuild output must pass defined length and readability thresholds for its surface (button, field, toast, help). [\[94\]](https://dev-design.va.gov/4702/content-style-guide/button-labels)

**Implementation guidance.** - Implement as a mode classifier with deterministic triggers (e.g., “audit” verbs, presence of existing copy, context).  
- For each component, emit `mode_used`, `why`, `rules_triggered`, `before/after`, and `tests`.

**Test cases.** - Input: “Review our signup form errors for accessibility and clarity.” → Audit mode with WCAG and form guidance checks. [\[95\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html?utm_source=chatgpt.com)  
- Input: “Write microcopy for a new payment flow.” → Rebuild mode + variants + confirmation language for error prevention. [\[96\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com)

**Topic: Cognitive load and chunking**

**Definition.** Cognitive load is the amount of information working memory must process; chunking and progressive disclosure reduce overload by limiting simultaneous information. [\[97\]](https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf)

**Why it matters.** Users in forms, onboarding, and errors are often under time pressure; overloaded content increases mistakes. Design guidance explicitly recommends minimizing memorization and sequencing help alongside each step. [\[98\]](https://www.nngroup.com/articles/onboarding-tutorials/)

**Default rules.** - Break long text into sections with headings and short paragraphs; assume scanning. [\[99\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)  
- Use progressive disclosure for optional detail (“Learn more,” “View more”). [\[81\]](https://www.nngroup.com/articles/progressive-disclosure/?utm_source=chatgpt.com)  
- One task per screen/section; one main message per panel. [\[100\]](https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf)

**Exception rules.** - Expert workflows may accept denser text if users are trained, but still require clear hierarchy and consistent labels. [\[101\]](https://design.va.gov/content-style-guide/readability-and-usability)

**Fallback logic.** - If content is complex and must remain: provide a short summary plus expandable detail, and move “how to fix” steps adjacent to the action. [\[102\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com)

**Failure conditions.** - Instructions require users to remember details across steps without reminders. [\[78\]](https://www.nngroup.com/articles/onboarding-tutorials/)  
- Walls of text without headings in web contexts. [\[103\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)

**Measurable thresholds.** - Paragraph cap for web guidance: **≤4 sentences** is an explicit public-sector web-writing constraint; elsewhere **3–5 sentences** is recommended. [\[85\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)  
- Notification cap: **≤2 lines** before using “View more.” [\[55\]](https://carbondesignsystem.com/components/notification/usage/)  
- “Top needs” discipline: keep only content that meets top user needs; explicitly recommended to check every piece and remove if it doesn’t. [\[99\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

**Implementation guidance.** - Create a “chunking” linter: flags paragraphs \>4 sentences, sections with weak headings, and missing summaries.  
- Generate a “summary first” version and a “details on demand” version; pick based on surface constraints.

**Test cases.** - Convert a 200-word FAQ answer into: (1) 2-sentence summary, (2) bullet steps, (3) “More details” accordion. [\[104\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

**Topic: Neuro-copywriting limits and useful applications**

**Definition.** “Neuro-copywriting” here means behaviorally informed microcopy that anticipates common cognitive biases and emotional states to reduce friction-without manipulating users into unwanted outcomes.

**Why it matters.** Regulators and researchers document that manipulative choice architecture (dark patterns) can subvert autonomy and disproportionately affect less educated users; these patterns often rely on loaded language, obstruction, or deceptive urgency. The operator must explicitly avoid crossing into “dark patterns.” [\[105\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com)

**Default rules.** - Use behavioral framing only to improve comprehension and follow-through on user-intended tasks (e.g., clarifying consequences, reducing uncertainty). [\[106\]](https://www.w3.org/WAI/tutorials/forms/notifications/)  
- Avoid “must act now” urgency unless factually true and user-benefiting; otherwise it is high-risk. [\[107\]](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com)  
- Avoid guilt/shaming (“No, I don’t care…”), obstruction, and asymmetric choices; these map to documented manipulative patterns. [\[108\]](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com)

**Exception rules.** - Legitimate urgency: time-bound security events, expiring codes, genuine deadlines; label with the actual deadline/time remaining, not vague pressure. (The “factually true” condition is non-negotiable.) [\[106\]](https://www.w3.org/WAI/tutorials/forms/notifications/)  
- Risk warnings (financial/legal/data): must be explicit and may include confirmations or review steps. [\[109\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com)

**Fallback logic.** - If intent is unclear, default to neutral, non-persuasive language that emphasizes user control (“You can…”, “Choose…”) and provides clear opt-outs. [\[110\]](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/?utm_source=chatgpt.com)

**Failure conditions.** - Any copy that hides material info, impairs cancellation/opt-out, or uses deceptive urgency. [\[111\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com)  
- Any “consent” language that is ambiguous or coerced. [\[112\]](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com)

**Measurable thresholds.** - Operator pack “dark pattern red flags” (enforceable checks): - urgency words without a factual deadline (“now”, “last chance”)  
- shame framing (“No thanks, I hate saving money”)  
- asymmetric CTA prominence in text (e.g., “Accept” vs “More options”)  
- unclear cancellation language  
These are derived from regulatory and research typologies. [\[113\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com)

**Implementation guidance.** - Add a “manipulation” classifier that flags dark-pattern indicators and forces an Audit output with safer alternatives.  
- Require explicit “user benefit” justification for persuasion elements, otherwise remove.

**Test cases.** - Replace: “Don’t miss out-upgrade now!” with a factual, user-controlled statement: “Upgrade to get offline access. You can change your plan anytime.” (No false urgency; clear benefit.) [\[114\]](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com)

**Topic: Case-study and design-rationale writing clarity**

**Definition.** Case-study writing (in product contexts) explains what was changed and why, with evidence of impact. Design-rationale writing captures decisions, tradeoffs, and constraints so teams can understand “why we did it.” [\[115\]](https://www.nngroup.com/videos/ux-design-portfolio-case-study/?utm_source=chatgpt.com)

**Why it matters.** Clear rationale reduces re-litigation of decisions and supports governance of modular design systems; clear case studies connect changes to outcomes (findability, errors reduced), aiding stakeholder trust and future iteration. [\[116\]](https://www.nngroup.com/articles/quantifying-case-study/?utm_source=chatgpt.com)

**Default rules.** - Lead with the outcome: what problem, what change, what impact (in first paragraph). This follows inverted-pyramid web writing and scanning behavior. [\[117\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com)  
- Use a structured format: Problem → Constraints → Options considered → Decision → Evidence → Result → What we’d do next. (Derived, but aligned with documented emphasis on tradeoffs and decision clarity in design docs.) [\[118\]](https://www.industrialempathy.com/posts/design-docs-at-google/?utm_source=chatgpt.com)  
- Use measurable language: metrics, observed behaviors, before/after when available. [\[119\]](https://www.nngroup.com/articles/quantifying-case-study/?utm_source=chatgpt.com)

**Exception rules.** - If results are not yet measurable, clearly label as “hypothesis” and specify what will be measured. (Avoid unsupported claims; consistent with technical writing editorial cautions about accuracy.) [\[120\]](https://google.github.io/styleguide/docguide/best_practices.html?utm_source=chatgpt.com)

**Fallback logic.** - If inputs are incomplete, produce a “case study skeleton” with required placeholders (audience, goal, metric, constraints), rather than inventing specifics.

**Failure conditions.** - Storytelling that obscures the decision: long narrative without a clear “what changed” and “why.” [\[121\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)  
- Claims without evidence presented as fact. [\[120\]](https://google.github.io/styleguide/docguide/best_practices.html?utm_source=chatgpt.com)

**Measurable thresholds.** - Opening: first **2–3 sentences** must include problem + change + impact/expected impact (operator standard derived from inverted pyramid and main-message guidance). [\[122\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com)  
- Sectioning: paragraphs should not exceed **≤4 sentences** for web readability. [\[123\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)

**Implementation guidance.** - Provide a “rationale template” module for the operator pack; enforce mandatory fields: - decision statement  
- options considered (at least 2)  
- tradeoff summary  
- success metrics  
- risks and mitigations  
(Tradeoffs emphasis is consistent with design-doc norms.) [\[118\]](https://www.industrialempathy.com/posts/design-docs-at-google/?utm_source=chatgpt.com)

**Test cases.** - Given a design change description, produce a one-paragraph exec summary + structured rationale sections; ensure the first paragraph contains decision + impact placeholder. [\[117\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com)

**Topic: Failure modes in UX writing**

**Definition.** UX writing failure modes are recurring patterns of copy that degrade comprehension, accessibility, trust, or task success.

**Why it matters.** Mature systems treat UX copy as functional; failures cause user effort loss and can become compliance or ethical risks, especially around errors and consent language. [\[124\]](https://www.nngroup.com/articles/error-message-guidelines/)

**Default rules.** - Classify failures by severity (Blocker/Major/Minor) and by type (see taxonomy deliverable).  
- Always attach a recommended fix and a test case.

**Exception rules.** - Some “non-ideal” copy may be accepted temporarily if it is accurate and safe, but must be logged as debt with a remediation plan (operator standard aligned to “minimum viable documentation” and continuous improvement practices). [\[120\]](https://google.github.io/styleguide/docguide/best_practices.html?utm_source=chatgpt.com)

**Fallback logic.** - If uncertain whether something is a failure, run it through: “Can a first-time user act correctly without external help?” If no, treat as at least Major.

**Failure conditions.** - Ambiguity: unclear actions (“Continue” without context), unclear references (“this”, “that”). [\[125\]](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/?utm_source=chatgpt.com)  
- Non-actionable errors: no fix path or next steps. [\[20\]](https://designsystem.digital.gov/components/alert/)  
- Hidden requirements (buried constraints). [\[99\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)  
- Inaccessible patterns (placeholder-as-label, no text error identification, missing focus cues). [\[126\]](https://v1.designsystem.digital.gov/components/form-controls/)  
- Manipulative language / dark patterns. [\[113\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com)

**Measurable thresholds.** - Trigger thresholds are the same as earlier modules (e.g., button \>35 chars, notifications \>2 lines, paragraphs \>4 sentences). [\[127\]](https://dev-design.va.gov/4702/content-style-guide/button-labels)  
- Add “generic error phrase” detector for phrases like “Something went wrong” without reference ID or fix. (Operator standard derived from error guidelines requiring constructive communication.) [\[128\]](https://www.nngroup.com/articles/error-message-guidelines/)

**Implementation guidance.** - Build a failure taxonomy with IDs and automated detectors (regex + heuristics) plus “rewrite patterns.”

**Test cases.** - Provide 10 known-bad snippets and expected rewrites; include accessibility markers (Error: prefix, linking summary to fields) per established patterns. [\[129\]](https://service-manual.nhs.uk/design-system/components/error-summary)

## Rule engine and measurement framework

A strict operator pack needs a **lintable** rule engine: rules must be checkable, thresholds must be explicit, and exceptions must be enumerated.

### Measurement is multi-signal, not single-metric

Readability formulas estimate difficulty using proxies like sentence and word length, but multiple authoritative sources warn that scores vary widely across methods and tools, can mis-handle digital formatting, and do not capture all elements of comprehension. A robust operator therefore uses readability metrics to **surface risk** and prioritize review/testing, not to mechanically “optimize” a number. [\[130\]](https://design.va.gov/content-style-guide/readability-and-usability)

### Recommended measurable constraints by UI surface

- **Buttons / CTAs**: verb-first; ≤35 characters when possible; 1–3 words ideal; avoid “Submit.” [\[131\]](https://dev-design.va.gov/4702/content-style-guide/button-labels)
- **Inline errors**: shown when attempting to proceed (pattern-dependent); preserve input; include fix guidance; avoid blame. [\[132\]](https://service-manual.nhs.uk/design-system/components/error-message)
- **Error summary pages** (where applicable): surface a top summary and link to fields; include “Error:” prefixing patterns for assistive tech; manage focus to summary. [\[133\]](https://service-manual.nhs.uk/design-system/components/error-summary)
- **Toasts / notifications**: 1–2 short sentences; if longer than 2 lines, use “View more.” [\[134\]](https://carbondesignsystem.com/components/notification/usage/)
- **Help / onboarding**: progressive disclosure; short paragraphs (≤4 sentences); avoid memorization across steps. [\[135\]](https://www.nngroup.com/articles/onboarding-tutorials/)
- **Long-form guidance / case studies**: inverted pyramid; first paragraph contains main point; chunked sections with descriptive headings. [\[136\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com)

### Ethical constraints as “hard rules”

Because dark patterns are documented to impair autonomy and can be strikingly effective at manipulating user behavior, the operator must treat manipulative language patterns as **Blockers**: remove, rewrite, and document. [\[113\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com)

## Deliverable markdown modules

    # writing-clarity-ux-copy-expert.md

    ## Purpose
    Define a strict Writing Clarity and UX Copy Expert agent for production UI copy decisions.

    This is a rules-first operator. It must:
    - prioritize clarity, accessibility, and task success
    - enforce measurable thresholds by UI surface
    - avoid marketing fluff, clickbait, and manipulative language
    - support three modes: audit, rebuild, expand

    ## Definitions
    Plain language: wording + structure + design are so clear that intended readers can find, understand, and use the information.

    Microcopy: interface text that supports interaction (labels, hints, errors, confirmations, CTAs, onboarding, help).

    ## Operating modes
    ### Audit
    Goal: diagnose and classify issues, then propose fixes.
    Output: findings with severity + rule IDs + suggested rewrites.

    ### Rebuild
    Goal: replace copy to meet constraints.
    Output: final copy + compact variant (when needed) + rationale + tests.

    ### Expand
    Goal: add missing scaffolding via progressive disclosure.
    Output: minimal inline copy + optional “Learn more” expansions.

    ## Non-negotiables
    - Do not blame the user.
    - Do not hide material information.
    - Do not add false urgency, shame, obstruction, or asymmetric choices (dark patterns).
    - Do not rely on placeholder text as the only label.
    - Errors must include how to fix when possible.

    ## Output contract (per component)
    For each component, return:
    - component_type: (button | field_label | helper_text | inline_error | alert | toast | empty_state | onboarding_step | help_article | case_study_section)
    - mode_used: (audit | rebuild | expand)
    - final_copy: …
    - variants: (compact | expanded | none)
    - rationale: 2–5 sentences, plain language
    - rules_triggered: [RULE-ID…]
    - metrics: { fk_grade_estimate?, avg_sentence_length?, paragraph_sentence_max?, char_count? }
    - tests: [test_case_id…]

    ## Default thresholds (en-US)
    ### Readability & structure (long-form + help)
    - Grade trigger: FK grade > 8 ⇒ requires rewrite or user test
    - Sentence length: avg 15–20 words; max 25 words unless unavoidable
    - Paragraph length: max 4 sentences (web); max 5 (general)
    - One topic per paragraph; headings must be descriptive and front-loaded

    ### Microcopy length limits
    - Button label: <= 35 characters; ideally 1–3 words; verb-first
    - Helper text: <= 120 characters or 1 sentence (default); only expand if necessary
    - Inline error: 1 sentence with fix; allow 2nd sentence only if safety/complexity requires
    - Toast / inline notification: 1–2 short sentences; >2 lines => “View more” overflow pattern

    ## Rule IDs (overview)
    PL-*  Plain language
    RD-*  Readability
    AV-*  Active voice
    FL-*  Front-loading / hierarchy
    MC-*  Microcopy conventions
    ER-*  Error handling & recovery
    CTA-* Calls to action
    ONB-* Onboarding & help
    CL-*  Cognitive load & chunking
    NE-*  Neuro/behavioral copy ethics
    CS-*  Case study & rationale
    FM-*  Failure taxonomy and detection

    ## References (primary sources)
    - Plain Writing Act + federal plain language guidance (U.S. agencies)
    - WCAG input assistance + WAI form notifications
    - USWDS: buttons, alerts, form-control guidance
    - NHS service manual: error summary + error message patterns
    - VA.gov Design System: button label char limit; readability as a signal
    - Nielsen Norman Group: microcopy clarity; error-message guidelines; onboarding guidance
    - OECD / FTC: dark patterns and manipulative choice architecture
    # plain-language-rules.md

    ## Plain language rules (PL-*)
    PL-01: Write for the user’s task. Include only what they need to complete it.
    PL-02: Use common words. If a technical term is required, define it the first time.
    PL-03: Prefer active voice with a clear actor.
    PL-04: Put the main point first (inverted pyramid).
    PL-05: Use descriptive, front-loaded headings; avoid generic “Introduction/Conclusion” headings on web pages.
    PL-06: One idea per paragraph.

    ## Readability rules (RD-*)
    RD-01: Sentence length: target avg 15–20 words.
    RD-02: If any sentence >25 words, flag and rewrite unless unavoidable.
    RD-03: Paragraph length: max 4 sentences (web) / max 5 (general).
    RD-04: Grade-level trigger: FK grade >8 => rewrite or user test.
    RD-05: Do not rewrite solely to hit a readability score; treat scores as signals.

    ## Quick patterns
    - Replace noun strings with verbs (e.g., “submission of application” -> “submit your application”).
    - Replace weak verbs: “utilize” -> “use”, “assist” -> “help”, “facilitate” -> “help/allow”.

    ## Required outputs
    - Before/after copy
    - Metrics (avg sentence length, FK trigger)
    - Any kept technical terms + their definitions
    # microcopy-rules.md

    ## Microcopy core principles (MC-*)
    MC-01: Clarity is the primary objective for informative microcopy.
    MC-02: Make the relationship between control and outcome explicit.
    MC-03: Use consistent terms for the same concept across the UI.
    MC-04: Avoid placeholders as labels.

    ## Surface-specific rules
    ### Labels
    MC-L01: Field labels must remain visible.
    MC-L02: Use user language (what people say/search for).

    ### Helper text
    MC-H01: Default to 1 sentence.
    MC-H02: Put the constraint in the helper text (format, limits, examples).

    ### Notifications
    MC-N01: 1–2 short sentences.
    MC-N02: If >2 lines, use “View more” and link to details.

    ## Cognitive load rules (CL-*)
    CL-01: Chunk content into scannable sections with headings.
    CL-02: Do not require memorization across steps; show help alongside the step.
    CL-03: Use progressive disclosure for optional detail.

    ## Tests
    - Provide label + helper + error triads for 10 common fields (email, password, date, phone, amount).
    # cta-and-error-message-rules.md

    ## CTA rules (CTA-*)
    CTA-01: Lead with a verb.
    CTA-02: Avoid “Submit” when you can name the action.
    CTA-03: Use sentence case.
    CTA-04: Keep labels <=35 characters where possible.
    CTA-05: Destructive actions must be explicit (“Delete account”), not vague (“OK”).

    ## Error rules (ER-*)
    ER-01: Errors must identify what’s wrong in text and where it occurred.
    ER-02: Provide a fix suggestion when possible.
    ER-03: Preserve user input; don’t clear fields on error.
    ER-04: Timing: don’t show validation errors while typing (default); show on attempt to continue or after interaction.
    ER-05: Be polite; don’t blame the user.
    ER-06: Include next steps in alerts.

    ## Error templates
    - Inline field: “Enter {required_format}. (Example: {example})”
    - Global: “We couldn’t {action}. Try again. If it keeps happening, contact support and share code {ref}.”
    - Permission: “You don’t have access to {resource}. Request access.”

    ## Accessibility hooks (a11y)
    - Error summary must link to each field with error (multi-field forms).
    - Prefix page title with “Error:” where relevant.
    # audit-vs-rebuild-writing-rules.md

    ## Decision tree
    If request includes “review/audit” OR existing copy is provided => Audit.
    Else if copy is missing, generic, or wrong => Rebuild.
    Else if user failure indicates missing guidance => Expand.

    ## Audit output schema
    - Issue: …
    - Severity: Blocker | Major | Minor
    - Rule IDs: …
    - Why: …
    - Fix: (rewrite + rationale)
    - Test: (how to validate)

    ## Severity definitions
    Blocker:
    - user can’t recover from error
    - accessibility violation (error not described in text, placeholder label, etc.)
    - manipulative/dark-pattern language
    Major:
    - ambiguous CTA
    - unclear constraint
    Minor:
    - tone inconsistency without comprehension impact

    ## “No vague advice” rule
    Audit must include thresholds and concrete rewrites.
    # writing-failure-taxonomy.md

    ## Failure taxonomy (FM-*)
    FM-01 Ambiguous action: CTA doesn’t state outcome.
    FM-02 Missing recovery: error has no fix path.
    FM-03 Hidden constraint: limits buried late.
    FM-04 Jargon/acronyms: user-facing insider language.
    FM-05 Placeholder-as-label: label disappears.
    FM-06 Blame tone: “You did…” in errors.
    FM-07 Over-validation noise: errors while typing.
    FM-08 Inconsistent terms: same concept named multiple ways.
    FM-09 Cognitive overload: walls of text, no headings, long paragraphs.
    FM-10 Manipulative framing: shame/urgency/obstruction/asymmetry.
    FM-11 Unsupported claims: promises not grounded in product behavior.
    FM-12 Accessibility mismatch: status not conveyed, focus not guided.

    ## For each failure type
    - Detection heuristics
    - Severity default
    - Rewrite pattern
    - Test procedure
    # writing-test-cases.md

    ## Per-topic test cases (sample)
    ### Plain language
    1) “Utilize the functionality…” -> produce plain rewrite + metrics.
    2) Replace jargon with user terms; keep required terms with definitions.

    ### Active voice / front-loading
    3) Convert passive requirements into active instructions.
    4) Rewrite headings to include topic in first 5–7 words.

    ### Microcopy/errors
    5) Replace “Invalid input” with field-specific fix.
    6) Create error summary + inline errors for a 5-field form.

    ### CTA clarity
    7) Replace “Submit” with action-specific verb+noun.
    8) Provide destructive-action confirm copy.

    ### Onboarding/help
    9) Turn a 150-word onboarding paragraph into 3 steps + “Learn more”.

    ### Cognitive load
    10) Chunk a long help article into headings + short paragraphs.

    ### Neuro-copy ethics
    11) Remove false urgency and add factual deadline or remove urgency.

    ### Case study clarity
    12) Generate exec summary (2–3 sentences) + rationale sections.

    ### Failure taxonomy
    13) Classify 10 snippets by FM-* and propose fixes.

    ## Readability checklist (quick)
    - FK grade trigger <=8?
    - Avg sentence length 15–20?
    - Paragraphs <=4 sentences?
    - Main message in first 1–3 sentences?

    ## Microcopy checklist (quick)
    - CTA verb-first?
    - Button <=35 chars?
    - Error includes fix?
    - No placeholder labels?
    - No blame language?

    ## 20 stress-test prompts
    (1) Write errors for a payment flow with security constraints.
    (2) Rewrite a consent modal to remove dark patterns while keeping legal meaning.
    (3) Audit a signup form that uses placeholders as labels.
    (4) Create onboarding for an expert tool without patronizing experts.
    (5) Convert a policy paragraph into scannable help content.
    (6) Write a destructive action dialog with undo.
    (7) Generate copy for a system outage banner with next steps.
    (8) Rewrite a medical-style warning into plain language without reducing safety.
    (9) Create microcopy for 2FA enrollment and recovery.
    (10) Audit inconsistent terminology across a settings page.
    (11) Write empty states that don’t guilt users.
    (12) Provide inline validation that avoids typing-time errors.
    (13) Rewrite a case study that is all narrative into evidence-based structure.
    (14) Create a “View more” overflow pattern for long notifications.
    (15) Write help text for a multi-step identity verification process.
    (16) Audit an onboarding carousel that exceeds cognitive load limits.
    (17) Rewrite “Something went wrong” errors into actionable messages with ref IDs.
    (18) Simplify a 12th-grade reading-level FAQ to <=8 without chasing the score.
    (19) Create CTA labels for a wizard stepper with ambiguous “Continue” buttons.
    (20) Detect and remove confirmshaming language from opt-out screens.

## Operating spec and validation suite

### Condensed operating spec

This expert agent enforces plain-language outcomes (“find, understand, use”) and accessibility constraints on user-facing text. It treats readability numbers as triage signals, not as the sole objective, and pairs metrics with structure rules (front-load, headings, chunking). [\[137\]](https://plainlanguagenetwork.org/plain-language/iso-plain-language-standard/)  
It applies strict UI-surface thresholds (e.g., 35-character button labels; 1–2 sentence notifications) and ensures error copy supports recovery (identify, suggest fixes, preserve inputs, and avoid blame). [\[138\]](https://dev-design.va.gov/4702/content-style-guide/button-labels)  
It explicitly rejects manipulative or deceptive language patterns documented as dark patterns and produces safer, user-control-preserving alternatives. [\[113\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com)

### Writing-mode matrix

| Situation                                                                 | Mode    | Output emphasis                           | Non-negotiables                                                                                                                  |
|---------------------------------------------------------------------------|---------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Existing UI copy needs review (compliance, accessibility, consistency)    | Audit   | Findings + severity + rule IDs + rewrites | Must include measurable thresholds and exact fixes [\[24\]](https://design.va.gov/content-style-guide/readability-and-usability) |
| Copy is missing/generic/wrong for the action                              | Rebuild | Final copy + compact/expanded variants    | CTA verb-first; error recovery steps; surface limits [\[139\]](https://designsystem.digital.gov/components/button/)              |
| Users are confused; support load or drop-off suggests missing explanation | Expand  | Progressive disclosure + contextual help  | Avoid overwhelm; no memorization across steps [\[140\]](https://www.nngroup.com/articles/onboarding-tutorials/)                  |

### Readability checklist

- Does the first paragraph contain the main message (and next step if applicable)? [\[122\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com)
- Are sentences generally within the 15–20-word average guidance (or ≤20 in high-stress contexts)? [\[22\]](https://www.opm.gov/information-management/plain-language/?utm_source=chatgpt.com)
- Are paragraphs ≤4 sentences on web surfaces? [\[123\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)
- Is FK grade \>8 treated as a review trigger (not a hard pass/fail), and are decisions grounded in user testing/feedback where possible? [\[18\]](https://design.va.gov/content-style-guide/readability-and-usability)
- Are technical terms kept only when needed, and explained the first time? [\[14\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)

### Microcopy checklist

- Do button labels lead with a verb and clearly state outcome? [\[72\]](https://designsystem.digital.gov/components/button/)
- Are button labels within a character constraint (≤35) when feasible? [\[70\]](https://dev-design.va.gov/4702/content-style-guide/button-labels)
- Are errors shown at the right time (not while typing, default), and do they preserve user input? [\[141\]](https://service-manual.nhs.uk/design-system/components/error-message)
- Do error messages (a) identify the issue, (b) tell the fix, and (c) avoid blaming language? [\[142\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html?utm_source=chatgpt.com)
- Are placeholder labels avoided in favor of persistent labels? [\[46\]](https://v1.designsystem.digital.gov/components/form-controls/)
- Are notifications constrained to 1–2 sentences, with “View more” overflow if longer? [\[55\]](https://carbondesignsystem.com/components/notification/usage/)

### Stress-test prompts

1.  Audit a 7-field signup form where each field uses placeholder text instead of labels; produce an accessibility-compliant rewrite and list which rules were violated. [\[143\]](https://v1.designsystem.digital.gov/components/form-controls/)
2.  Rewrite an error: “Invalid input” for a phone number field; include a format example and keep it in one sentence. [\[58\]](https://www.w3.org/WAI/WCAG21/Understanding/error-suggestion.html?utm_source=chatgpt.com)
3.  Create a top-of-form error summary and inline field errors for a failed submission, including “Error:” patterns appropriate for screen readers. [\[133\]](https://service-manual.nhs.uk/design-system/components/error-summary)
4.  Replace the CTA “Submit” on a complaint form with an action label that describes the outcome and remains ≤35 characters. [\[67\]](https://designsystem.digital.gov/components/button/)
5.  Write microcopy for a destructive action (delete account) including confirmation language and a clear CTA label, avoiding vague “OK.” [\[69\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com)
6.  Draft a service-outage banner: polite tone, no blame, includes next steps and support path, within 2 sentences. [\[144\]](https://designsystem.digital.gov/components/alert/)
7.  Rewrite a 200-word onboarding page into contextual help with progressive disclosure (“Learn more”), avoiding memorization across steps. [\[140\]](https://www.nngroup.com/articles/onboarding-tutorials/)
8.  Audit a cookie-consent modal for dark patterns (asymmetric language, guilt opt-out); rewrite to neutral, symmetric choices. [\[112\]](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com)
9.  Rewrite a legal requirement sentence using “must” appropriately and keep the meaning intact, adding a plain English explanation for any unavoidable legal term. [\[4\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)
10. Convert passive voice policy text into active, step-based instructions using imperative mood and second person where appropriate. [\[34\]](https://developers.google.com/style/person?utm_source=chatgpt.com)
11. Chunk a “wall of text” FAQ into headings and ≤4-sentence paragraphs; front-load the main message. [\[145\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content)
12. Generate two CTA variants for a multi-step wizard: compact “Continue” and outcome-explicit label; specify when to use each. [\[146\]](https://dev-design.va.gov/4702/content-style-guide/button-labels)
13. Produce error messaging for login that avoids account enumeration while still offering recovery steps. [\[49\]](https://www.w3.org/WAI/WCAG21/Understanding/error-suggestion.html?utm_source=chatgpt.com)
14. Create helper text for a password field that reduces cognitive load (clear rules, one sentence, example if needed). [\[147\]](https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf)
15. Rewrite an alert that contains an internal error code into human-readable language and include where to find the code (support reference) without making the code the main message. [\[51\]](https://designsystem.digital.gov/components/alert/)
16. Expand a short instruction into a 3-step procedure; introduce with an imperative statement. [\[148\]](https://developers.google.com/style/procedures?utm_source=chatgpt.com)
17. Write a case-study executive summary (2–3 sentences) that leads with problem, change, and impact (or metric placeholder). [\[149\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com)
18. Audit a set of three notifications that exceed 2 lines; redesign as “short + View more” pattern and rewrite copy accordingly. [\[55\]](https://carbondesignsystem.com/components/notification/usage/)
19. Detect and remove blame language in errors (“You entered… wrong”); rewrite to neutral, helpful tone. [\[150\]](https://designsystem.digital.gov/components/alert/)
20. Simplify a grade-12 readability help article to a grade-8 trigger, while explicitly *not* rewriting purely for the score; explain tradeoffs. [\[18\]](https://design.va.gov/content-style-guide/readability-and-usability)

[\[1\]](https://plainlanguagenetwork.org/plain-language/iso-plain-language-standard/) [\[7\]](https://plainlanguagenetwork.org/plain-language/iso-plain-language-standard/) [\[12\]](https://plainlanguagenetwork.org/plain-language/iso-plain-language-standard/) [\[137\]](https://plainlanguagenetwork.org/plain-language/iso-plain-language-standard/) ISO Plain Language Standard - Plain Language Association International (PLAIN)

<https://plainlanguagenetwork.org/plain-language/iso-plain-language-standard/>

[\[2\]](https://www.justice.gov/open/plain-writing-act?utm_source=chatgpt.com) Plain Writing - Open Government

<https://www.justice.gov/open/plain-writing-act?utm_source=chatgpt.com>

[\[3\]](https://www.nngroup.com/articles/error-message-guidelines/) [\[45\]](https://www.nngroup.com/articles/error-message-guidelines/) [\[124\]](https://www.nngroup.com/articles/error-message-guidelines/) [\[128\]](https://www.nngroup.com/articles/error-message-guidelines/) Error-Message Guidelines - NN/G

<https://www.nngroup.com/articles/error-message-guidelines/>

[\[4\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk) [\[14\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk) [\[26\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk) [\[36\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk) [\[103\]](https://www.gov.uk/guidance/content-design/writing-for-gov-uk) Content design: planning, writing and managing content - Writing for GOV.UK - Guidance - GOV.UK

<https://www.gov.uk/guidance/content-design/writing-for-gov-uk>

[\[5\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html?utm_source=chatgpt.com) [\[54\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html?utm_source=chatgpt.com) [\[95\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html?utm_source=chatgpt.com) [\[142\]](https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html?utm_source=chatgpt.com) Understanding Success Criterion 3.3.1: Error Identification

<https://www.w3.org/WAI/WCAG21/Understanding/error-identification.html?utm_source=chatgpt.com>

[\[6\]](https://designsystem.digital.gov/components/button/) [\[60\]](https://designsystem.digital.gov/components/button/) [\[62\]](https://designsystem.digital.gov/components/button/) [\[64\]](https://designsystem.digital.gov/components/button/) [\[67\]](https://designsystem.digital.gov/components/button/) [\[72\]](https://designsystem.digital.gov/components/button/) [\[139\]](https://designsystem.digital.gov/components/button/) Button \| U.S. Web Design System (USWDS)

<https://designsystem.digital.gov/components/button/>

[\[8\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[16\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[25\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[28\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[30\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[33\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[85\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[88\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[99\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[104\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[121\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[123\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) [\[145\]](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) Writing and editing: Structuring content – Content style guide – Service manual – Office for National Statistics

<https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content>

[\[9\]](https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf) [\[97\]](https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf) Cognitive load theory: Research that teachers really need to understand

<https://education.nsw.gov.au/content/dam/main-education/about-us/educational-data/cese/2017-cognitive-load-theory.pdf>

[\[10\]](https://design.va.gov/content-style-guide/readability-and-usability) [\[17\]](https://design.va.gov/content-style-guide/readability-and-usability) [\[18\]](https://design.va.gov/content-style-guide/readability-and-usability) [\[24\]](https://design.va.gov/content-style-guide/readability-and-usability) [\[32\]](https://design.va.gov/content-style-guide/readability-and-usability) [\[93\]](https://design.va.gov/content-style-guide/readability-and-usability) [\[101\]](https://design.va.gov/content-style-guide/readability-and-usability) [\[130\]](https://design.va.gov/content-style-guide/readability-and-usability) Readability and usability of VA digital content - VA.gov Design System

<https://design.va.gov/content-style-guide/readability-and-usability>

[\[11\]](https://www.nngroup.com/articles/progressive-disclosure/?utm_source=chatgpt.com) [\[81\]](https://www.nngroup.com/articles/progressive-disclosure/?utm_source=chatgpt.com) Progressive Disclosure

<https://www.nngroup.com/articles/progressive-disclosure/?utm_source=chatgpt.com>

[\[13\]](https://www.dol.gov/general/plainwriting?utm_source=chatgpt.com) Plain Language

<https://www.dol.gov/general/plainwriting?utm_source=chatgpt.com>

[\[15\]](https://www.dol.gov/sites/dolgov/files/general/Plain-Language-Quick-Reference-Guide.pdf?utm_source=chatgpt.com) [\[35\]](https://www.dol.gov/sites/dolgov/files/general/Plain-Language-Quick-Reference-Guide.pdf?utm_source=chatgpt.com) Plain Language Quick Reference Guide

<https://www.dol.gov/sites/dolgov/files/general/Plain-Language-Quick-Reference-Guide.pdf?utm_source=chatgpt.com>

[\[19\]](https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf) [\[23\]](https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf) [\[100\]](https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf) [\[147\]](https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf) Your Guide to Clear Writing

<https://www.cdc.gov/nceh/clearwriting/docs/clear-writing-guide-508.pdf>

[\[20\]](https://designsystem.digital.gov/components/alert/) [\[51\]](https://designsystem.digital.gov/components/alert/) [\[91\]](https://designsystem.digital.gov/components/alert/) [\[144\]](https://designsystem.digital.gov/components/alert/) [\[150\]](https://designsystem.digital.gov/components/alert/) Alert \| U.S. Web Design System (USWDS)

<https://designsystem.digital.gov/components/alert/>

[\[21\]](https://secure.ssa.gov/poms.nsf/lnx/0900610020) SSA - POMS: NL 00610.020 - Notice Readability Guidelines - 06/01/2017

<https://secure.ssa.gov/poms.nsf/lnx/0900610020>

[\[22\]](https://www.opm.gov/information-management/plain-language/?utm_source=chatgpt.com) Plain Language

<https://www.opm.gov/information-management/plain-language/?utm_source=chatgpt.com>

[\[27\]](https://developers.google.com/tech-writing/one/active-voice?utm_source=chatgpt.com) [\[29\]](https://developers.google.com/tech-writing/one/active-voice?utm_source=chatgpt.com) [\[38\]](https://developers.google.com/tech-writing/one/active-voice?utm_source=chatgpt.com) [\[40\]](https://developers.google.com/tech-writing/one/active-voice?utm_source=chatgpt.com) Active voice vs. passive voice \| Technical Writing

<https://developers.google.com/tech-writing/one/active-voice?utm_source=chatgpt.com>

[\[31\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com) [\[102\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com) [\[117\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com) [\[122\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com) [\[136\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com) [\[149\]](https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com) Inverted Pyramid: Writing for Comprehension

<https://www.nngroup.com/articles/inverted-pyramid/?utm_source=chatgpt.com>

[\[34\]](https://developers.google.com/style/person?utm_source=chatgpt.com) Second person and first person

<https://developers.google.com/style/person?utm_source=chatgpt.com>

[\[37\]](https://www.archives.gov/open/plain-writing/10-principles.html?utm_source=chatgpt.com) Top 10 Principles for Plain Language

<https://www.archives.gov/open/plain-writing/10-principles.html?utm_source=chatgpt.com>

[\[39\]](https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf?utm_source=chatgpt.com) Federal Plain Language Guidelines

<https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf?utm_source=chatgpt.com>

[\[41\]](https://www.w3.org/WAI/tutorials/forms/notifications/) [\[56\]](https://www.w3.org/WAI/tutorials/forms/notifications/) [\[57\]](https://www.w3.org/WAI/tutorials/forms/notifications/) [\[106\]](https://www.w3.org/WAI/tutorials/forms/notifications/) User Notification \| Web Accessibility Initiative (WAI) \| W3C

<https://www.w3.org/WAI/tutorials/forms/notifications/>

[\[42\]](https://www.nngroup.com/articles/ux-writing-study-guide/) UX Writing: Study Guide - NN/G

<https://www.nngroup.com/articles/ux-writing-study-guide/>

[\[43\]](https://www.nngroup.com/articles/negativity-bias-ux/) The Negativity Bias in User Experience - NN/G

<https://www.nngroup.com/articles/negativity-bias-ux/>

[\[44\]](https://www.nngroup.com/articles/3-cs-microcopy/) The 3 C’s of Informational Microcopy - NN/G

<https://www.nngroup.com/articles/3-cs-microcopy/>

[\[46\]](https://v1.designsystem.digital.gov/components/form-controls/) [\[47\]](https://v1.designsystem.digital.gov/components/form-controls/) [\[126\]](https://v1.designsystem.digital.gov/components/form-controls/) [\[143\]](https://v1.designsystem.digital.gov/components/form-controls/) Form controls \| U.S. Web Design System

<https://v1.designsystem.digital.gov/components/form-controls/>

[\[48\]](https://service-manual.nhs.uk/design-system/components/error-message) [\[53\]](https://service-manual.nhs.uk/design-system/components/error-message) [\[59\]](https://service-manual.nhs.uk/design-system/components/error-message) [\[132\]](https://service-manual.nhs.uk/design-system/components/error-message) [\[141\]](https://service-manual.nhs.uk/design-system/components/error-message) Error message – NHS digital service manual

<https://service-manual.nhs.uk/design-system/components/error-message>

[\[49\]](https://www.w3.org/WAI/WCAG21/Understanding/error-suggestion.html?utm_source=chatgpt.com) [\[58\]](https://www.w3.org/WAI/WCAG21/Understanding/error-suggestion.html?utm_source=chatgpt.com) Understanding Success Criterion 3.3.3: Error Suggestion

<https://www.w3.org/WAI/WCAG21/Understanding/error-suggestion.html?utm_source=chatgpt.com>

[\[50\]](https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA19?utm_source=chatgpt.com) Using ARIA role=alert or Live Regions to Identify Errors \| WAI

<https://www.w3.org/WAI/WCAG21/Techniques/aria/ARIA19?utm_source=chatgpt.com>

[\[52\]](https://www.nngroup.com/articles/errors-forms-design-guidelines/) [\[90\]](https://www.nngroup.com/articles/errors-forms-design-guidelines/) 10 Design Guidelines for Reporting Errors in Forms - NN/G

<https://www.nngroup.com/articles/errors-forms-design-guidelines/>

[\[55\]](https://carbondesignsystem.com/components/notification/usage/) [\[73\]](https://carbondesignsystem.com/components/notification/usage/) [\[92\]](https://carbondesignsystem.com/components/notification/usage/) [\[134\]](https://carbondesignsystem.com/components/notification/usage/) Open menu

<https://carbondesignsystem.com/components/notification/usage/>

[\[61\]](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/?utm_source=chatgpt.com) [\[110\]](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/?utm_source=chatgpt.com) [\[125\]](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/?utm_source=chatgpt.com) Cognitive Accessibility Objective: Help Users Understand ...

<https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/?utm_source=chatgpt.com>

[\[63\]](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/guides/ui-text-style-guide?utm_source=chatgpt.com) [\[65\]](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/guides/ui-text-style-guide?utm_source=chatgpt.com) [\[71\]](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/guides/ui-text-style-guide?utm_source=chatgpt.com) Windows Admin Center UI text and design style guide

<https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/extend/guides/ui-text-style-guide?utm_source=chatgpt.com>

[\[66\]](https://dev-design.va.gov/4702/content-style-guide/button-labels) [\[70\]](https://dev-design.va.gov/4702/content-style-guide/button-labels) [\[94\]](https://dev-design.va.gov/4702/content-style-guide/button-labels) [\[127\]](https://dev-design.va.gov/4702/content-style-guide/button-labels) [\[131\]](https://dev-design.va.gov/4702/content-style-guide/button-labels) [\[138\]](https://dev-design.va.gov/4702/content-style-guide/button-labels) [\[146\]](https://dev-design.va.gov/4702/content-style-guide/button-labels) Button labels - VA.gov Design System

<https://dev-design.va.gov/4702/content-style-guide/button-labels>

[\[68\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com) [\[105\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com) [\[111\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com) [\[113\]](https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com) Bringing Dark Patterns to Light

<https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%2BDark%2BPatterns%2BReport%2B9.14.2022%2B-%2BFINAL.pdf?utm_source=chatgpt.com>

[\[69\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com) [\[79\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com) [\[89\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com) [\[96\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com) [\[109\]](https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com) Error Prevention (Legal, Financial, Data) \| WAI

<https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html?utm_source=chatgpt.com>

[\[74\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[75\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[76\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[77\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[78\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[80\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[82\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[87\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[98\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[135\]](https://www.nngroup.com/articles/onboarding-tutorials/) [\[140\]](https://www.nngroup.com/articles/onboarding-tutorials/) Onboarding Tutorials vs. Contextual Help - NN/G

<https://www.nngroup.com/articles/onboarding-tutorials/>

[\[83\]](https://www.nngroup.com/videos/onboarding-skip-it-when-possible/?utm_source=chatgpt.com) [\[84\]](https://www.nngroup.com/videos/onboarding-skip-it-when-possible/?utm_source=chatgpt.com) Onboarding: Skip it When Possible (Video) - NN/G

<https://www.nngroup.com/videos/onboarding-skip-it-when-possible/?utm_source=chatgpt.com>

[\[86\]](https://www.nngroup.com/articles/ux-copy-sizes/?utm_source=chatgpt.com) UX Copy Sizes: Long, Short, and Micro

<https://www.nngroup.com/articles/ux-copy-sizes/?utm_source=chatgpt.com>

[\[107\]](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com) [\[108\]](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com) [\[112\]](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com) [\[114\]](https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com) Dark commercial patterns (EN)

<https://www.oecd.org/content/dam/oecd/en/publications/reports/2022/10/dark-commercial-patterns_9f6169cd/44f5e846-en.pdf?utm_source=chatgpt.com>

[\[115\]](https://www.nngroup.com/videos/ux-design-portfolio-case-study/?utm_source=chatgpt.com) Creating a UX Design Portfolio Case Study (Video)

<https://www.nngroup.com/videos/ux-design-portfolio-case-study/?utm_source=chatgpt.com>

[\[116\]](https://www.nngroup.com/articles/quantifying-case-study/?utm_source=chatgpt.com) [\[119\]](https://www.nngroup.com/articles/quantifying-case-study/?utm_source=chatgpt.com) Quantifying UX Improvements: A Case Study

<https://www.nngroup.com/articles/quantifying-case-study/?utm_source=chatgpt.com>

[\[118\]](https://www.industrialempathy.com/posts/design-docs-at-google/?utm_source=chatgpt.com) Design Docs at Google

<https://www.industrialempathy.com/posts/design-docs-at-google/?utm_source=chatgpt.com>

[\[120\]](https://google.github.io/styleguide/docguide/best_practices.html?utm_source=chatgpt.com) Documentation Best Practices \| styleguide

<https://google.github.io/styleguide/docguide/best_practices.html?utm_source=chatgpt.com>

[\[129\]](https://service-manual.nhs.uk/design-system/components/error-summary) [\[133\]](https://service-manual.nhs.uk/design-system/components/error-summary) Error summary – NHS digital service manual

<https://service-manual.nhs.uk/design-system/components/error-summary>

[\[148\]](https://developers.google.com/style/procedures?utm_source=chatgpt.com) Procedures \| Google developer documentation style guide

<https://developers.google.com/style/procedures?utm_source=chatgpt.com>
