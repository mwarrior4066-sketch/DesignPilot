# Case-Study Structure and Narrative Order

Definition: A case study’s structure is the underlying logic that organizes its story[1]. It determines what comes first, what gets emphasis, and how key signals (problem, process, outcome) connect[2][3]. In practice, a well-structured case study goes beyond chronology: it highlights your problem framing, decision points, and impact rather than just listing artifacts[2][4].

Why it matters: Structure lets readers (e.g. recruiters or stakeholders) quickly scan and understand your thinking. According to UX research, a strong case study structure prioritizes signals reviewers care about (role clarity, problem framing, impact) and creates a clear progression from problem to outcome, reducing cognitive load[2][3]. Without a logical structure, even great work can seem confusing and superficial[5][6]. Case studies are evaluated as evidence of your problem-solving and communication skills[7][8], so structure is critical to make your reasoning visible and persuasive.

Default rules: Follow a coherent template that covers all key sections. For example, a standard UX case study includes a Hero/Title (project name and short summary), Overview (context: product description, your role, timeframe, tools, team)[9][10], Discovery/Research (methods used, findings, and how they shaped the problem)[11][12], Design Process (step-by-step problem–solution pairs: e.g. ideation, wireframes, prototypes, testing)[13][14], Solution/Final Design (the chosen design and rationale)[15], Impact/Results (metrics or qualitative validation of success)[16][17], and Learnings/Next Steps[18][19]. Each section should be clearly labeled and briefly explained. Titles and captions for images should appear in context (e.g. Figure 1: Description)[20][21]. Visuals should be annotated or captioned so they support (not distract from) the narrative
. For example, use a screenshot of a survey with a caption explaining key findings; don’t just drop an image without context[22][21].

Exception rules: There is no single ideal structure for every project[23]. Tailor the narrative to the project’s strengths. For a research-heavy project, emphasize discovery early; for a UI-heavy project, you might foreground final designs sooner[23][12]. If a section isn’t applicable (e.g. no team or tool details), it can be omitted, but the remaining flow should still make sense. For example, a solo project need not list “Team,” and a small redesign might combine “Discovery” and “Process.” Similarly, if no quantitative outcome is available, include qualitative impact or user testimonials instead[16]. The structure should always focus on why decisions were made and what changed as a result, even if those changes are small or anecdotal.

Fallback logic: If the ideal structure is unclear, default to the common flow: Problem → Process → Solution → Outcome. Start with a concise statement of the problem/goal, then describe your approach, then present the solution, and finally state the outcomes or what you learned. If content is missing (e.g. no metrics), explicitly note that (“metric data unavailable”) or use proxies (e.g. “after redesign, usability tests improved task success by anecdotal report”). When uncertain about ordering, ensure the problem statement always precedes the solution[2], and that results come at the end. This linear fallback ensures at least a coherent narrative.

Failure conditions: A case study fails if its structure is unclear or if key sections are missing. Signs include a lack of problem framing, no clear transitions between steps, or hiding outcomes at the very end (requiring readers to hunt for them). For example, “artifacts out of context” (random images/screenshots without explanation) is a failure mode[24]【50†】. Equally problematic is “chronological dumping” – simply retelling the timeline (“I did A, then B, then C”) without emphasizing reasoning or outcomes[25][2]. Overlong, unscannable text is another failure: case studies should be brief and skimmable[6]. If reviewers can’t quickly identify the core problem-solution-impact chain, the case study’s structure needs compression[6]. A weak structure “forces the reviewer to search” for relevance or decision points[26].

Measurable thresholds: Ensure each required section has at least minimal content. For example, a project overview should include at least 3–4 concise sentences plus 3–5 bullet points of context[9][27]. A discovery or design section should include at least two problem–solution examples, each explained in a few sentences[13][14]. Aim for sections that are no more than ~20 words per sentence and one main idea per paragraph to stay clear[28]. For structure, a quick check is: Headings present for all main sections? (e.g. “Project Overview,” “Process,” “Results”). A useful threshold is: case studies should not exceed ~800–1000 words, or beyond 10 minutes of reading[6]. (If longer, it should be clearly justified by complexity and broken into sub-sections.) Finally, verify that images have captions or figlinks – zero images should be unlabeled.

Implementation guidance (AI operator pack): The agent should apply a case-study template internally. For “case study” tasks, prompt the model to include all core sections in order. If the user input lacks structure, the model should ask clarifying questions or assume defaults (e.g. “What was the main problem? What were the outcomes?”). It should format output with headings/subheadings and bullet lists to aid scanning[29]. When critiquing a draft, the agent can say things like “The problem statement is missing – add an explicit framing of the issue you solved” or “I see outcomes, but I can’t find the baseline. What was the original metric?” to ensure structure is complete. In summary, the AI should treat case-study writing as narrative engineering: always look for Problem, Process, Solution, Outcome, and verify each is present and clearly delineated.

Test cases:

- Proper structure: Input: “Write a case study about redesigning an e-commerce checkout.” Check: It should have headings like Overview, Problem, Design Process, Results. If any part is missing (e.g. no Results), that’s a failure.
- Missing context: Input: A case study draft describing features without context. Expected: Agent flags “Needs problem framing; I only see features without why.”
- Artifacts only: Input: “Here are screenshots of a whiteboard.” Expected: “This shows artifacts out of context – add explanations of what they mean”[24]【50†】.
- Overlong text: Input: 1000+ word essay. Expected: “This reads too long; try bullet points and headings[6].”
- Restructuring prompt: Input: “Summarize project X.” Expected: Output structured with title, overview, process, outcome, not just one paragraph.
# Design Rationale and Evidence Framing

Definition: Design rationale is the explanation of why each design decision was made. It is the documented reasoning behind choices (colors, layouts, workflows)[30][31]. Evidence framing is presenting data or research that justifies those decisions (user research findings, usability metrics, expert guidelines). Together, they form the “why and how” behind design changes. In case studies or documentation, this means linking every claim or decision to concrete support rather than generic justification.

Why it matters: Stakeholders and reviewers need to trust that designs aren’t arbitrary. A clear rationale with evidence shows professionalism and rigor[32][33]. As one UX guide notes, including research (e.g. “Baymard’s study shows 68% cart abandonment; we addressed this”) strengthens your argument[33]. Design rationale also demonstrates critical thinking: it shows you weighed options and chose for good reasons, which is key to UX credibility[34]. Without rationale/evidence, writing falls into fluff or vague declarations (e.g. “we did testing to improve UX”) which experts find frustrating[25][34].

Default rules: By default, always link design decisions to reasons and evidence. For each feature or change, answer: “Why did I do this?” (motivations, constraints) and “How did I know it was right?” (user feedback, metrics, guidelines). Use statements like “We chose X because Y, based on evidence that Z”[31][33]. Include at least one source of evidence for major decisions: this can be data (analytics, survey results, A/B test) or credible heuristics (usability guidelines, research). For example: “We increased button size because usability tests showed users missed it (test success rate from 50% to 80%)[33].” Or cite known principles (e.g. “Aligned with Nielsen’s guideline that...”[31]). Structurally, present rationale immediately after describing a decision or in captions/annotations accompanying visuals[34]【50†】. Always frame outcomes as results (see Outcome rules below).

Exception rules: If no direct evidence exists (e.g. a pet project without user data), do not invent metrics. Instead, use reasoned assumptions: “Based on our domain expertise” or cite related standards. If the user base is unknown, say so (“In absence of user data, we assumed tech-savvy millennials and designed accordingly”). In purely hypothetical or exploratory projects, emphasize logic (“Our choice prioritized speed over aesthetics because the primary need was performance under tight constraints[31]”). Only cite guidelines if relevant to the context (avoid irrelevant quotes). Also, avoid citing internal opinions as “data”.

Fallback logic: If evidence is missing, fallback is to suggest ways to obtain it: “Consider running a short usability test or gathering analytics next.” If asked to critique text lacking evidence, default to prompting the user to provide sources or to mark uncertain statements (e.g. “[Need data here]”). For design rationales, if unspecific, replace generic phrasing with specifics. For example, convert “We optimized the UI” into “We optimized the UI by X%, to shorten task completion time” (even if estimated). If truly no data, clearly qualify statements as assumptions.

Failure conditions: Failures occur when decisions lack justification or rely on vacuous phrases. Watch for statements like “We did X to improve the experience” without explaining why or how we know it improved. Equally, avoid “everyone knows X so we did it” (common knowledge not tied to project). A key failure is over-reliance on adjectives without evidence: e.g. “This makes the UI more intuitive” without proof. Another failure is mismatched claims: presenting outcomes (“users loved it”) with no supporting evidence or metrics. Also, avoid stuffing case studies with theory (e.g. defining “usability testing”) instead of project-specific rationale[25].

Measurable thresholds: At least 80% of major claims should be backed by data or clear reasoning. For example, if a paragraph states three decisions, aim for at least two to have explicit rationale/evidence. Design rationale text should maintain a “why” clause in most sentences (e.g. 15–20% of lines begin with “because” or explain motivations). In critique mode, flag any section of text over 50 words that contains no data or “because” clause. For outcomes, define success metrics quantitatively whenever possible (e.g. conversion rate increase, error reduction). If we claim “better usability,” we should have a numeric improvement (or at least a before/after example) in >0 words. Readability: keep explanations concise (per [18†L239-L247]) and avoid jargon unless explained.

Implementation guidance (AI operator pack): When generating a case study or explanation, the agent should explicitly call out and incorporate rationale and evidence. It can have a checklist: for each design move, ask “What's our reason and do we have support?” If writing narratively, the agent should place evidence in parentheses or quotes. For example: “We added autocomplete to the search bar (based on user testing feedback and to align with [source] heuristic)[33].” If evidence is lacking, the agent should either ask for it or flag it: e.g., output may say “[No data provided]” or suggest conducting a survey. In evaluation mode, the agent should say things like “You claim increased engagement; do you have the metrics?” or “The rationale is unclear – what research informed this choice?” For training, include example prompts like “Provide justification for the color choice with data or user insight.” The agent should default to formal, factual tone with citations (if appropriate) to model evidence-based writing.

Test cases:

- Missing rationale: Input: “I changed the button color to blue.” Expected: Agent asks “Why blue specifically? Cite research or test results.” (It should not accept “because it looks better.”)
- Weak justification: Input: “Made font larger because users should see it.” Expected: “What evidence showed users had difficulty reading? Provide metric or quote.”
- Evidence incorporation: Input: “Design a case study section explaining the signup flow.” Expected: Section includes statements like “We reduced fields from 6 to 3, which improved completion rate (it rose from 60% to 85% in testing)[33].”
- Critique mode: Input: “Review: 'We streamlined checkout to improve UX.'” Expected: “Not enough detail – how did you measure UX? Add a metric or user feedback.”
# Audit vs Rebuild vs Expand Writing Modes

Definition: These are distinct writing “modes” describing intent and scope.

- Audit writing: Analyzes and critiques an existing design or content, often uncovering usability issues and recommending fixes. It reads like a review (e.g. “issue – impact – recommendation”) and typically uses an objective, findings-oriented tone.
- Rebuild (structure-mode) writing: Describes how to reconstruct or reimplement something from scratch. It is prescriptive and instructional (“Do X, then Y, using tools A, B”). Often step-by-step, focusing on what should be done to achieve a fresh outcome.
- Expand writing: Takes an existing baseline or feature and elaborates on it. It might involve adding detail, new features, or extending scope. The tone is additive and constructive. It assumes a foundation is in place and builds on it.
Why it matters: The agent must match the user’s intention. An audit report vs a rebuild plan vs an expansion proposal have very different formats and tones. Mixing them up causes confusion: for example, writing a “rebuild answer” with an audit’s style is a mode error (“this is a rebuild answer, but formatted like an audit”). Each mode serves different user needs (diagnosis vs instruction vs enhancement). Clear differentiation ensures relevance and tone consistency.

Default rules:

- Audit: Default to finding problems with the current design. Use headings like “Findings,” “Issues,” “Recommendations.” Be critical yet constructive. For each identified issue, explain its effect on users, and suggest an improvement. Avoid giving new designs or code; focus on evaluation. e.g. “The button label is unclear (issue) which may cause confusion (impact); we recommend rewriting it to be more specific (recommendation).”
- Rebuild: Default to describing a systematic re-design. Write as if instructing how to rebuild: use imperatives (“Use modular CSS,” “Set up a database…”). Outline steps or high-level architecture. Emphasize tools, processes, and structure. Do not delve into evaluating the existing (that’s audit). Instead, say how you would construct the ideal system.
- Expand: Default to building upon existing content. Use language like “Additionally,” “To enhance,” “Next steps could include.” The format often presents an “Existing state” and “Proposed expansion.” Focus on adding new features or content depth.
Exception rules: If instructions conflict (e.g. user says “do an audit but also implement changes”), default to one mode based on phrasing. For borderline cases, clarify with the user or fallback to audit (safe default: identify issues first, then indicate how one might rebuild). If asked to “expand on an audit,” treat it as audit because that was the user’s core request. If a rebuild is requested for something already perfect, note “rebuild unnecessary – provide detail on updating processes instead.”

Fallback logic: If mode is unclear, the agent can use meta cues: e.g., the presence of words “review,” “audit,” “evaluate” implies audit mode; words like “build,” “develop,” “recreate” imply rebuild; words like “add,” “extend,” “improve” imply expand. Lacking cues, the safe default is audit mode (since it’s basic to point out issues before suggesting changes). The agent should ask: “Are you looking for a critique or instructions to build?” if uncertain.

Failure conditions: Mixing modes is a failure. Examples: writing audit-style critique in a rebuild plan, or adding marketing fluff in audit. A specific failure is what the user highlighted: “rebuild answer formatted like an audit” – e.g., giving bullet lists of issues instead of construction steps. Another failure: in audit mode, writing in second person imperative (“You should…” in an audit is okay, but rebuilding requires detail beyond “you”). Lack of actionable recommendations in audit or lack of high-level structure in rebuild are failures.

Measurable thresholds: Check for keywords/format: An audit should contain at least 3 identified issues with reasons and solutions. A rebuild response should contain at least 3 steps or sub-sections describing a build process. Expand writing should mention an existing state and at least two extensions or features. Tone detection: audit mode tends to use modal verbs (“should,” “might”) and issue-based phrasing; rebuild uses definitive tone (“must,” present tense instructions); expand uses additive words (“additionally,” “improve upon”). As a heuristic, if the text has over 50% imperative sentences, it’s likely rebuild; if 50% questions/issues + recommendations, it’s audit; if many “also”/“moreover,” it’s expand.

Implementation guidance: The agent should first classify the requested mode by keywords. Then apply the corresponding template. In audit mode, use an evaluative checklist and output like a report (with headings “Issue/Impact/Recommendation”). In rebuild mode, use action-oriented language and logically ordered steps. In expand mode, start by summarizing current scope and then list additions. If the user’s prompt explicitly states “Audit” or “review,” ensure output addresses problems, not implementation. Use the stress-test remark: if the agent detects e.g. “The following is a rebuild answer but formatted as an audit,” it should correct by reformatting. For instance: “Your answer seems to list issues; instead, structure it as step-by-step instructions (rebuild mode).”

Test cases:

- Audit vs rebuild confusion: Input: “Redesign the login page, show me what’s wrong first.” Expected: Agent starts with an audit (“Finding 1: The login button is hidden…”), then maybe rebuild. It should not solely write rebuild steps.
- Rebuild misformatted: Input: “Rebuild the dashboard.” If agent writes like an audit (issue-solution list), it should be flagged “This is rebuild mode; use instructions not critique.”
- Expand prompt: Input: “We have a single-page form. How to add user profiles?” Expected: It should explain current form state then describe adding profiles (expand mode), not auditing or fully rebuilding.
- Implicit mode test: Input: “Tell me how to improve the site.” Expected: Likely treated as audit mode (issues+fixes). If agent answers with “build from scratch” steps, it’s a failure.
- Mode misalignment: Input: “Audit report for homepage.” Expected: A report format, not a step-by-step rewrite.
- User correction scenario: Input: If the agent’s first pass is in the wrong mode, user says “This is an audit but I want a rebuild.” Expected: Agent should switch style and apologize.
# Portfolio vs UX Copy vs Documentation

Definition: These writing categories differ by audience and purpose.
- Portfolio (Case Study) writing: Aimed at hiring managers or peers; it tells the story of your work and thought process. Tone is professional, reflective, and often first-person (“I did X”), emphasizing your role and impact. Structure is narrative-focused (as above).
- UX/Interface copy (UI microcopy): Aimed at end users of a product. Text is extremely concise and task-oriented. Examples: button labels, form hints, error messages. It should be in second person or imperative (e.g. “Click here,” “Your password”), and follow UX writing guidelines[35][36]. It often avoids first person and never talks about the designer.
- Documentation (product/help copy, explanatory docs): Aimed at users or stakeholders seeking information. It is more descriptive and can be longer. It should be clear, step-by-step (like instructions or explanations), and may include technical details. Tone is objective and informative. Example: user manuals, help center articles, or feature explanation guides[37].

Why it matters: Mixing these up causes confusion. A portfolio piece should not read like product marketing (“hero” language, second-person pitches)[38], and UX microcopy rules (short, imperative) differ from portfolio narratives. For instance, “interface design took 3 weeks and we used Figma” belongs in a case study, not in product copy. An AI expert must pick the mode that fits the task: writing documentation needs thorough descriptions and instructions, whereas portfolio writing needs storytelling and outcomes.

Default rules: - Portfolio writing: Write in past tense, first or third person, focusing on your actions and decisions. Use narrative structure as defined above. Provide data or evidence of impact[37][16]. Use plain language for any complex concept (keep reader=designer/recruiter, so moderately technical but not jargon-heavy).
- UX copy: Follow Nielsen’s copy-size guidelines[39][40]. Microcopy: <3 sentences, direct action verbs, friendly yet clear. Short-form copy: 1–2 paragraphs max, one idea, avoid fluff. Use guidelines from [23] and [24]. For example, a CTA button might be “Submit” (imperative) not “We propose to submit your application”.
- Documentation: Use formal tone, present tense or imperative depending on style, structured with headings. Avoid self-reference (“we”), be factual. Use bullet lists for steps. Use terms familiar to audience or define them[28].

Exception rules: If writing a case study for a product that includes UI elements, don’t inadvertently slip into UX copy style. For example, a portfolio might mention UI, but it should not write actual button text. Conversely, if the user asks “Generate UI text for login flow,” do not include personal anecdotes or metrics – keep it short, instructional. If documentation is user-facing, it may use second person (“you should do X”), while portfolio writing should not speak directly to “you” (the reader).

Fallback logic: If the task is ambiguous, guess based on length and phrasing. A very short prompt is likely for UX microcopy; long prompts with detail likely portfolio or documentation. The AI should confirm: “Are you asking for interface copy, or a project write-up?” If no clarity, default to portfolio (since many complex queries will be case-study related). The writing mode matrix below (B) can guide selection: e.g. if prompt contains “tutorial,” default documentation; if “UI,” default microcopy.

Failure conditions: Treat the sample failure lines literally. For instance, if a portfolio case reads like marketing (“Join thousands of users…”), say “This reads like marketing, not a case study.” If documentation is too casual or narrative (“We started by…”), it fails. Check voice: portfolio often uses “I/We did,” UX copy uses imperative/you, docs use neutral/you depending. If an output includes UI instructions in a case study, that’s a failure (“this is UX copy style, not portfolio”). Similarly, if a help article is in first person narrative, it’s wrong. Vague “be concise” violations should be concrete: e.g. a microcopy with multiple clauses is too long.

Measurable thresholds: For microcopy, ensure sentences <15 words[41] and <3 sentences per block[39]. For documentation/portfolio, a paragraph should average <20 words per sentence[28]. If a field label or button text exceeds 3 words, flag it (ex: “Submit Application Form” is long for a button). For tone: if “I/me/we” appears, likely not UX copy; if “you/your” appears, likely not portfolio (unless quoting user feedback). Check percentage of first-person pronouns: >5% suggests portfolio style. For clarity: portfolio and docs should score at grade 10–12 reading level[42]; UX microcopy ideally at 6-8 grade[42].

Implementation guidance: The agent should use a mode switch based on prompt intent. If in UX copy mode, it should produce short labels or messages, obeying the goals (inform, influence, interact)[36]. For documentation or audit summaries, it should be expository, use bullet lists, etc. For portfolio writing, it should incorporate narrative elements and outcomes. The “writing-mode matrix” (see B) can be coded as a decision table: if intent=“UX copy,” then apply UX-copy rules; if “portfolio,” apply case-study rules; if “documentation,” apply doc style. The agent should flag mismatches: e.g. “This output has long paragraphs – that’s not microcopy.” It can even warn the user if the content style seems off: “This reads more like a product page, not a case study; consider adding your process and results.” Use examples to train: e.g. “You wrote a promotional tagline; if a case study was intended, replace it with factual statement of outcome.”

Test cases:

- Mix-up detection: Input: “Write error messages for a signup form.” Expected: Short microcopy (imperative), not a case study. If agent starts story or metrics, it’s wrong.
- Wrong mode warning: Scenario: Agent produces a paragraph with “we” and outcomes but the user intended UI copy. Agent Response: “This looks like portfolio writing; I need microcopy style. Let me rewrite in first person tone.”
- Style check: Input: “Document how to use the API.” Expected: Instructional tone with “you” or imperative, not “I we.” If output says “In my case,” it's wrong.
- Case-study vs doc: Input: “Explain our new feature launch.” (ambiguous) Expected: Agent to ask clarifying question or guess portfolio mode (if context suggests internal project).
- Flip test: Input: “Write a case study on project X.” If agent outputs UI help text: Fail. Input: “Create labels for the settings page.” If agent outputs narrative: Fail.
# Clarity, Readability, and Plain Language

Definition: Plain language writing is clear, straightforward, and easily understood[43]. It avoids unnecessary jargon or complex structures. In our context, clarity means the writing can be scanned and digested quickly by the target audience, with short sentences, familiar vocabulary, and well-organized formatting[28][44].

Why it matters: Clear writing reduces misunderstanding and cognitive load. A well-known usability study confirms even experts prefer concise, simple language online[45]. Plain language benefits everyone: it ensures international or non-expert readers (including recruiters or diverse stakeholders) can follow your content[43]. It also improves SEO and credibility[43]. Specifically for UX and documentation, users scan content: if key points aren’t immediately clear, they may skip them[44]. In case studies or technical writing, clarity shows professionalism and focus.

Default rules:
1. Short sentences: Aim for ~15–20 words per sentence[46]. One idea per sentence.
2. Simple words: Prefer common terms over jargon[47]. If a technical term is needed, define it the first time. Replace idioms or branded terms with plain equivalents[47].
3. Active voice: Use active verbs (“We tested the button,” not “The button was tested”).
4. Audience awareness: Write to the intended reader. For case studies, assume the reader is a design professional – you can use design terms (e.g. “wireframes”) without explaining, but for documentation aimed at end-users, avoid unexplained acronyms. In general, aim for 10–12th grade reading level for technical audiences[48], and 6–8th for general audiences (like UX microcopy)[42].
5. Formatting for scan: Break up text with headings, bullet lists, short paragraphs (one sentence to two at most)[28][29]. Use bold or italics sparingly for emphasis (but see style guide).
6. Vocabulary: Use words familiar to the audience[47]. Avoid redundant pairs (“each and every”), qualifiers (“very”, “basically”), and cliches. Each word should add meaning.

Exception rules: Minor exceptions for clarity include:
- Technical terms: If writing for a specialized audience (e.g. a tech doc for developers), a few domain-specific words are acceptable without definition[48].
- Quotations/lyrics: if quoting an official name or term that’s inherently complex, keep it (with explanation).
- Cultural idioms: Generally avoid them, but if the audience is known to appreciate a bit of flair, a small idiom might be okay. However, default is strictly plain.

Fallback logic: If a sentence is longer than ~25 words, flag it for splitting. If passive voice is detected (many passive constructions), flag for active rewrite. If reading level >12th grade, simplify. If formatting is a wall of text, restructure into lists. If any jargon or acronym appears, require definition. The agent should rephrase unclear sentences automatically when possible.

Failure conditions: Non-plain-language phrases and structures. Examples: unnecessary nominalizations (“In order to accomplish this, the user engagement was raised” instead of “This raised user engagement”), or filler words (“in this day and age,” “utilize” when “use” suffices). A sign of failure is too many syllables per word or clauses per sentence. If Flesch-Kincaid or similar readability score (which the agent can approximate by counting words/sentences) is above 12th grade for a general document, it fails plain language guidelines[48]. Concretely, avoid stuffy tone: e.g. “commensurate with” → “as good as,” “ascertain”→“find out.”

Measurable thresholds:
- Sentence length: >20 words triggers a warning.
- Reading level: Aim for Flesch-Kincaid ~60–70 for documentation. The agent can approximate by checking average words per sentence and percent of long words.
- Passive voice: More than 20% of sentences passive is too high.
- Paragraph length: >5 sentences per paragraph is too long.
- Jargon count: Each paragraph should have <2 unexplained technical terms.
- Long phrases: If phrases like “in order to” or “at this point in time” appear, flag for shorter alternatives (e.g. “to” or “now”)[28].

Implementation guidance: The AI should run a clarity check on its output (or user-supplied text) before finalizing. It can apply known transformations: shorten, split, replace words using a plain-language lexicon. For example, list of red-flag words (“utilize,” “commence,” etc.) to replace. In critique mode, it can highlight or rewrite: “This sentence is too long; break it.” or “The word ‘utilize’ is too formal, use ‘use’ instead.” Tools or plugins could analyze readability scores. The agent should emphasize formatting: adding headings/bullets if not present. Whenever doubt, ask “Is this clear to someone unfamiliar with X?” and simplify accordingly.

Test cases:

- High reading level: Input: “The implementation of adaptive lighting schemes in user interfaces engenders enhanced engagement.” Expected: “This reads as very complex. Use simpler terms: e.g. ‘Using adaptive lighting makes interfaces more engaging.’”
- Passive voice: Input: “The button should be pressed by the user to proceed.” Expected: “Rewrite active: ‘Press the button to proceed.’”
- Jargon detection: Input: “Our solution uses a polyfill to ensure cross-browser compatibility.” Expected: either define “polyfill” or say “small script” if audience is broad.
- Long sentence split: Input: a 40-word sentence. Expected: Agent splits it into two sentences or a list.
- Formatting: Input: A 300-word wall of text. Expected: Agent outputs version with headings and bullet points.
# Outcome, Validation, and Metrics Writing

Definition: Outcome writing is describing the results or impact of your work (quantitative or qualitative). Validation writing frames evidence that the solution worked (metrics, user feedback, A/B tests, performance improvements). Together, they show how success is measured.

Why it matters: Case studies and reports must demonstrate that designs achieved something real. Stakeholders want to see “Return on Design” – did conversions go up? Did errors drop? Did users adopt the feature? Including clear outcomes (e.g. “conversion rate increased from 2% to 4%”) turns claims into proof[17][16]. Without validation, readers can’t judge effectiveness; they might think “so what changed?”. Impact metrics make a case study persuasive and evidence-based. As one UX template says, before-and-after analytics (e.g. checkouts up, CTR up, user feedback) are “the single most powerful tool” in a case study[49].

Default rules: Always include at least one measurable outcome. This could be a key metric (numbers, percentages) or a qualitative measure (user satisfaction, testimonials). For example: “After redesign, task success was 90% (up from 60%)” or “post-launch user surveys showed 95% positive feedback”. When writing outcomes: use before/after comparisons if possible. Always specify the metric and time frame (“in 3 months, X increased by Y%”). If using qualitative evidence, attribute it (e.g. “According to user testing, 80% of users completed checkout faster[17]”). Present outcomes as bullet points or a concise paragraph. For audit or evaluation modes, list findings with supporting data.

Exception rules: If genuine metrics are unavailable, use proxy outcomes: mention prototypes or MVP results. In early-stage projects, you might say “expected outcome” but label it as such (“We anticipate...”). Anecdotal evidence is allowed but should be framed as such (“several users reported… in usability testing”). If a feature hasn’t launched yet, indicate that outcomes are future or simulation. Never make up data. If outcomes are mixed, report neutrally (e.g. “conversion rate remained the same, but error rate decreased”).

Fallback logic: If no data, fall back to user quotes or usability findings (qualitative). If no quotes, fall back to design heuristics (e.g. cite industry benchmarks[33]). If the user asks for outcome writing but no outcome is present, the agent should reply that the data is missing and suggest either gathering it or using qualitative insights. If reviewing text with no outcomes, respond: “Add validation evidence such as metrics or quotes.”

Failure conditions: Writing that claims “success” without evidence is a failure. For example: “Users loved the redesign” without data. Also, burying results in narrative or adjectives (“greatly improved”) instead of numbers. Overly passive outcomes (“gains were observed”) or vague (“better performance”) should be flagged. A common failure is forgetting baseline: saying “time to complete reduced by 50%” with no mention of original time. Another is mixing up outcomes with process (“We iterated three times” is process, not outcome).

Measurable thresholds: At least one metric (with before/after) per project. For each stated “improvement,” check that it has a number or specific user feedback. The AI should produce outcomes with numbers if available, or mark if not. If an outcome claim is made, check it has >=1% or 1-point change (so it’s concrete). Ensure at least 2 outcome statements if project involved multiple metrics. If none exist, output should have zero outcome sentences.

Implementation guidance: Train the agent to output a bullet list of results for case studies. The outcome section can be flagged as separate. For example:

Impact:  
- Checkout completion up from 40% to 65% after redesign.  
- Average session duration decreased by 20%, indicating faster task flow.  
- Customer satisfaction (from survey) was 4.5/5 (post-launch), up from 3.8 pre-launch.

If it’s an audit, it should still include “improvement potential” and “estimated ROI”. The agent should prompt for or simulate data if needed (“Assume a 30% increase in X unless real data provided.”). Always label assumptions. In critique mode, say “No outcomes given—please quantify the impact (for instance, user error rate dropped).”

Test cases:

- Missing metrics: Input: “The redesign improved user engagement.” Expected: “By how much? Please provide a metric (e.g. time on site, clicks).”
- No baseline: Input: “Conversion doubled.” If no baseline was given: “What was the original conversion rate? Double compared to what?”
- Qualitative fallback: Input: “There was some positive feedback.” Expected: Suggest adding “80% of surveyed users said X” or “1 testimonial from a key user.”
- Before/after: Input: “Redesigned homepage.” Expected: Output includes “Before: metric A; After: metric B.”
- User quotes: Input: “User interviews showed satisfaction.” Expected: Include a sample quote if allowed, or number of participants.
# Before/After Comparison Writing

Definition: This writing explicitly compares the “before” state (original problem or baseline) to the “after” state (post-solution). It highlights the change achieved by the work. Essentially, it frames the impact by showing where you started and where you ended up.

Why it matters: Before/after framing makes outcomes concrete and relatable. It prevents vague claims by providing context: e.g. “We had X problems and now we have Y improvements.” It ensures readers see the transformation. Without it, an “after” statement lacks meaning (is X “good”?), and a “before” without “after” leaves unresolved issues. Before/after writing also emphasizes the narrative arc: problem → solution.

Default rules: Whenever you state a result or change, also state the baseline. For example: “Before the redesign, average page load time was 6.5s; after optimization, it’s 2.1s.” Format can be a sentence or bullet: “Before: A, After: B.” For narrative context: “Prior to this work, users struggled with A; now they can easily do B.” Use consistent units (percentages, time, dollars) for clear comparison. If not quantifiable, do qualitatively: “Before: users needed to navigate 5 menus; After: now 2 steps.”

Exception rules: If no actual “before” exists (e.g. brand new feature), compare to best estimates or competitors (but note it’s hypothetical). If improvement is qualitative, phrase carefully: e.g. “Before, customers often complained X; now, feedback is positive on that aspect.” If a project is ongoing, you might say “Baseline is current state; plan is future state.” Don’t create false baselines.

Fallback logic: If a baseline isn’t given in the input, prompt for one. If in critique mode, agent should ask “What was the original metric? Without it, readers can’t judge the improvement.” If none, say “Before/After: [no data].” Optionally use “source: hypothetical” vs “observed.”

Failure conditions: Stating improvements without reference. For example, “This change sped up performance” with no numbers. Or listing changes out of context. A common failure is using before/after images or captions without text explanation – e.g. showing old vs new UI but not describing the difference in writing. Or describing before state only (“Users complained about X”) with no follow-up on solution.

Measurable thresholds: For any outcome statement, check if it contains “before” or a baseline phrase. If not, encourage adding one. E.g. require at least one of the keywords “before,” “after,” “previously,” “baseline,” “compared to.” If the ratio of outcome lines that mention before/after is <50%, it needs improvement. If writing for less technical audience, present in table format.

Implementation guidance: Teach the AI to always elicit or include baseline. In output, use sentences like “Originally, [state problem/metric]. We then [action]. Now, [metric after][49].” For example: “Before: only 50% of users completed checkout. After: 85% completion (see metrics).” The agent could have a templated prompt fill-in: “Before: {baseline}. After: {result}.” If in analysis mode, use this check as a test: if an outcome is given without “before,” respond “Please provide the baseline for that metric.”

Test cases:

- Incomplete claim: Input: “Users navigate 30% faster.” Expected: “What is the baseline? ‘Navigate 30% faster’ – 30% of what original time?”
- Image compare without caption: Input: an interface before/after image with no text. Expected: Agent asks for description, or writes “Before, users saw A; after, we changed it to B.”
- Story form: Input: “The old site had cluttered menus, we cleaned it up and now it’s better.” Expected: “Before/After framing: e.g. ‘Before, X% drop-off; after, Y%.’”
# Visual Annotation and Caption Support

Definition: Visual annotation writing refers to the text (captions, labels, callouts) that accompanies images, diagrams, or screenshots. Captions are brief descriptions placed near images to explain their content or relevance.

Why it matters: In case studies and documentation, visuals (screenshots, graphs, diagrams) illustrate concepts. Captions ensure non-decorative images convey information to all readers[20]. Good captions connect the image to the main text: they summarize what the image shows and why it matters. Without captions, readers may misinterpret or skip images. Accessibility guidelines also mandate alt text for vision-impaired readers[20]. For an expert AI, including clear captions ensures completeness and clarity of communication.

Default rules: Every non-decorative image must have a concise caption (and alt text)[20][21]. Captions should be sentence fragments or 1–2 sentences that “explain everything in the image”[21]. For example: Figure 2: A/B test results comparing old (red) vs new (green) checkout flow, showing 20% more users completing checkout with the new design. Titles or figure numbers can be used if context requires reference. The caption should explicitly tie into the text (e.g. “See Figure 2”). If the image shows a process or data, call out the key point in the caption. Also, add alt text: a one-line description for accessibility[20][50].

Exception rules: Decorative or purely aesthetic images do not need informative captions or alt text (alt="" to mark decorative)[50]. If the image is fully described in nearby text, a caption can simply identify it (e.g. “Screenshot of the final design”). Do not use a caption space for credits or irrelevant info. If space is extremely limited (e.g. UI microcopy annotations), you can use shorter labels instead of full sentences (e.g. arrow with tooltip “Submit button” if context is obvious).

Fallback logic: If the agent sees an image tag or placeholder without text, it should prompt “Add a caption that describes this image’s content.” For UI mocks, add captions like “(UI screenshots)”. If the agent itself generates an image (in explanation or answer), it should also generate an appropriate caption. Always produce both caption and alt text when an image is present.

Failure conditions: A visual failure is an unlabeled or mis-labeled image. If an image is included and has no caption, that’s a failure. If a caption doesn’t explain the image (e.g. “Figure of app” only), fail. Using the same text in alt and caption is discouraged; one should provide unique information. Also, avoid duplicating in caption what is in main text; the caption adds value. If the caption is overly long (more than 2-3 sentences), it fails the “brief” rule.

Measurable thresholds: Each figure in the answer must have a caption ≥ 5 words and ≤ 25 words (enough to explain but still brief). If images >50% of page area have no caption, fail. For documentation (e.g. research paper style), tables/graphs must be referenced by number and captioned. The AI should check that every embed [...†embed_image] is preceded by a caption.

Implementation guidance: When generating answers with images (e.g., in documentation mode), enforce a caption placeholder after each Figure. The agent can use a template: “Figure X: [Short description].” For UI prototypes or wireframes, use annotations like labels or callouts linked to captions (e.g. <figcaption>). For graphs or charts, include key stats in text form in the caption, as in [39†L105-L108]. If critiquing writing with images, say “This image lacks caption explaining its contents.” Provide examples of good vs bad captions in training prompts.

Test cases:

- Missing caption: Input: A paragraph says “See image below.” but no caption is given. Expected: Agent flags “Image needs caption describing it (alt-text if applicable).”
- Incorrect caption: Input: Caption “Figure: Dashboard”. Expected: “This is too vague. Explain what we’re seeing (e.g. user metrics on dashboard).”
- Alt text check: Input: HTML snippet with <img alt=""> but image is not decorative. Expected: “Missing alt text – describe the image.”
- Figure referencing: Input: “As shown in the screenshot: [image].” Expected: Output with figure number and caption, not just image insertion.
- Long caption: Input: A caption with 4 sentences. Expected: Suggest condensing to 1-2 sentences.
# Failure Modes in Case-Study and Project Writing

Definition: Failure modes are common pitfalls or anti-patterns in writing case studies or project documentation that compromise clarity, relevance, or credibility. They are the specific ways the content can go wrong.

Why it matters: Recognizing failure modes helps the expert agent detect when an output needs revision. For example, marketing fluff or irrelevant context can mislead readers. By cataloging these, the AI can provide targeted feedback (e.g. “this is marketing fluff, not case study content”). We want the agent to answer like: “This explains process but not the problem,” etc.

Default rules (anti-patterns to avoid): Based on UXfolio and best practices, common failure modes include:
- Artifacts out of context: Including screenshots or photos (e.g. of whiteboards) without explanation[24]. If used, they must be captioned and tied to the text.
- Vague declarations / fluff: Generic statements that add no value (e.g. “We did user testing to improve UX”)[25]. These should be replaced by specific findings or actions.
- Method definitions: Explaining what a known UX method is (e.g. “A user persona is a fictional character...”) instead of how you used it in your project[25].
- Too long / wordy: Case studies that aren’t concise. Long sentences, paragraphs, or irrelevant details cause drop-off[51]. Words and content that don’t contribute to showing your decision process should be trimmed.
- Marketing tone/fluff: Using promotional or emotional language (“revolutionary,” “game-changer”) rather than factual storytelling. This fits neither case studies nor documentation.
- Jargon overload: Especially for portfolio writing – too much unexplained technical or business jargon alienates readers.
- Irrelevant storyline: Talking about unrelated experiences or storytelling for drama (inspirational fluff) that doesn’t reflect project reality.
- Misplaced focus: Focusing on visuals over decisions. E.g. “look at how good the UI is” vs explaining why and how it was designed.
- Mixed modes: Writing a case study answer in an audit style (see earlier), or vice versa, as already discussed.
- No measurement: Failing to provide any outcome metrics or evidence as discussed above.

Exception rules: Some supposed failures may not apply if justified. For instance, a longer explanation is acceptable in a highly technical documentation if complexity demands it. A marketing-ish statement might be appropriate in a product’s marketing copy (though not in case study). The agent should note context: if writing for a marketing brochure, “passionate tone” is fine; if for an interview, it’s not. If the user specifically asks for creative or inspiring tone, some narrative embellishment is allowed – but the agent should confirm this intent because we generally prioritize clarity.

Fallback logic: If a text exhibits a failure mode, the agent should suggest a fix. For example, if it reads like marketing, respond: “This sounds promotional. A case study needs problem-centric clarity, not marketing claims.” If method definitions appear, say “Everyone knows X; instead, focus on how you applied it.” If too long, say “Could this be bulletized?” If jargon, suggest a plain-language alternative. As a fallback, the agent can reframe content as needed.

Failure conditions: Any output that falls into the above anti-patterns should be treated as a failure of the writing mode. Specifically, if >50% of sentences in a paragraph are fluff or irrelevant to project specifics, fail. If there’s an image with no caption or context, fail. If results lack numbers, or sections are chronologically confused, fail. Also, any output with personal speculation (“I just felt”), unsupported claims, or disorganization should be flagged.

Measurable thresholds: For text review, define metrics:
- Genericness: If >30% of verbs are generic (“improve,” “optimize”) with no object, flag.
- Buzzwords: If words like “game-changing,” “cutting-edge” appear, flag.
- Contextual ties: Each visual or method mention should co-occur with explanation at least 80% of the time. If we see an asterisk point without detail, it’s a fail.
- Length: If a case study answer exceeds a certain ratio of filler (sentences without project-specific info), it fails clarity check.

Implementation guidance: Encode these failure modes into the agent’s critique checklist. For each potential output, the agent should scan for known red flags. For example:

- If “*” or list items have no elaboration, prompt to elaborate.
- If “@image” markers present without adjacent descriptions, flag for captions.
- If an answer uses “We” at the start of every sentence and no specifics, it might be a fluff list – ask for details.
Train with examples: “This sentence is an obvious generality – rephrase with specifics from the project[25].” The agent can give direct feedback: “This paragraph reads like storytelling. Try stating facts with evidence.”

Test cases:

- Artifact context: Input: “sketch
Some sketch image. It looks cool.” Expected:* “Caption is missing. Explain what this sketch represents and why it’s included[24].”
- Method definition: Input: “I used A/B testing, which means splitting users to compare.” Expected: “Remove general definition (‘which means splitting...’) and focus on your project’s A/B test results.”
- Fluff detection: Input: “This groundbreaking solution increases engagement.” Expected: “Generic or marketing tone – replace with specific details or remove adjectives.”
- Length issue: Input: A 500-word narrative with few paragraphs. Expected: Suggest splitting or summarizing; “Try bullet points for clarity.”
- Combined mode error: Input: “I wrote an audit, but it reads like a step list.” Expected: “Mode mismatch – restructure to audit-style or clarify ask.”
# Templates and Output Structures

Definition: Templates are predefined content outlines or skeletons that organize sections and formatting for a given document type (case study, audit, UX copy, etc.). They prescribe the structure of the output (headings, order of sections, list vs paragraphs) to ensure consistency and completeness.

Why it matters: Having standardized templates helps the agent reliably produce the right structure. It ensures that all required components appear and are in the right order. This helps avoid ad hoc writing that might miss important parts. For an AI operator, templates are like a plan or scaffold to fill in.

Default rules: Use distinct templates for each writing mode. For example, a Case Study Template (as noted above) includes the seven sections (Hero, Overview, Exploration, Process, Final Design, Impact, Learnings)[52]. An Audit Template might be: Summary, Scope, Findings (Issue–Impact–Recommendation for each), and Conclusion. An UX Copy Template: (none needed for microcopy, just keep each line separate). A Documentation Template: Title, Overview, Steps/Subsections, Troubleshooting, Conclusion. Always start with a concise title or hero, and end with a clear wrap-up or call to action if needed.

Exception rules: Don’t rigidly force templates when context demands flexibility. Small projects might combine sections (skip “Team and roles”). Templates may have optional parts (“UI design” only if relevant)[53]. The agent should adapt template density: e.g., a one-page mockup project may skip lengthy “exploration.” However, note that even a short project should mention problem, solution, and outcome (these are core).

Fallback logic: If specific template is unclear, use a general format: introduction, body, conclusion. If given partial user input (e.g. raw notes), the agent can map them onto the template sections. If asked for help writing documentation without a template provided, default to the case-study template if it sounds like a project story, or generic doc structure if it’s help writing.

Failure conditions: A template failure is when sections are omitted or in wrong order. E.g., jumping to Outcomes before explaining the process (out of narrative order) is a failure. Or writing an essay when bullets were expected. Also, not labeling sections (no headings when many topics are covered) is a failure of structure.

Measurable thresholds: Check that required sections are present. For case studies, that means all 6+ sections[52] or at least core (problem, solution, outcome). For audits, check that every identified issue is followed by a recommendation bullet (flag if any issue lacks one). For output length, ensure each bullet or paragraph meets the minimum and maximum guideline for its template. If a final design gallery is expected, ensure images are included.

Implementation guidance: The agent’s prompt should include the template as a guide. For instance, begin answering with “### Project Overview”, “### Discovery”, etc. The writing-mode matrix (B) can include pointers to templates. The agent should fill in templated sections systematically. In developer notes, define the sections for each mode explicitly. In an AI operator pack, templates might be stored as JSON or guidelines the agent retrieves. The agent should also be able to “hand off” tasks: for example, a content outline for a portfolio case study might hand off to a writing assistant who fills it in with details. Thus, the template can say “Placeholder: describe UX research” – and the agent then elaborates based on data.

Test cases:

- Missing section: Input: “Write a UX case study about X.” If output has no “Learnings” section: Fail. Agent should add it.
- Audit format: Input: “UX audit for homepage.” Expected structure: issues with bullet “Recommendation.” If agent wrote narrative paragraphs instead, it’s a fail.
- Rebuild format: Input: “Plan rebuild of dashboard.” Expected: step list or ordered sections “Step 1: …”. If formatted as an essay, fail.
- Template switching: Input: “Write a summary as a case study.” Expected: use case study template, not just a generic summary paragraph.
- Conciseness: Input: Template says “Scope: 1-2 sentences.” If output paragraph is 10 sentences, fail.
## Final Deliverables

### content-and-case-study-expert.md

- Purpose: Top-level specification of the Content and Case Study Expert agent. It defines the overall role, goals, and boundaries of the agent.
- Contains: An overview of the agent’s mission (e.g. “to ensure all UX case studies and content are clear, evidence-based, and properly structured”), plus high-level guidelines that are not specific to one mode (e.g. voice/tone principles, overall quality standards). References to the different writing modes and when to apply them. Possibly a summary of failure modes.
- Not contain: Detailed rules for each topic (those go in separate files). It should not contain actual case study content or examples (those belong in portfolio rules). Avoid low-level UI copy tips or microcopy – focus on “when in doubt, escalate to the relevant rule doc.”
- Depends on: All other rule documents (structure, rationale, audit/rebuild, writing modes, etc.). It references them conceptually.
- Hand-off to: Specific rule modules. It signals which specialized module handles which part (e.g. “For audit vs rebuild decisions, see audit-vs-rebuild rules”). It may also hand off to editorial/production (ensuring that final content passes through these checks).
### case-study-structure-rules.md

- Purpose: Detailed rules for case study organization and narrative (Topic 1).
- Contains: Definitions of a case study structure, default section order, examples of each part, guidelines on narrative flow. It should list mandatory components (title, overview, etc.), optional sections, formatting (headings, bullet guidelines). Include common mistakes (from UXfolio).
- Not contain: UX copy or microcopy rules, or audit-specific rules. Avoid general writing advice not specific to case studies (those go in plain-language or expert doc).
- Depends on: content-and-case-study-expert.md for context, plain-language rules (for readability), and possibly design rationale.
- Hand-off to: The writing phase for case studies (ensuring the output conforms). Also to failure detection (case-study-failure-taxonomy.md) – these structure rules inform what to check.
### audit-vs-rebuild-vs-expand-writing-rules.md

- Purpose: Specify how to handle queries in audit, rebuild, or expand modes (Topic 3).
- Contains: Definitions of each mode, distinguishing features, templates for each. Rules for detecting mode, formatting for each mode (headings, tone). Lists of phrases/keywords indicative of each mode.
- Not contain: Case study-specific content (no problem-solution narrative unless in context). No microcopy rules. Should not detail design rationale or plain language (beyond how style changes).
- Depends on: content-and-case-study-expert.md (for overall context), UX writing vs documentation rules.
- Hand-off to: Further writing modules (e.g. if in rebuild mode, actually generate instructions, which might hand off to an implementation writing tool). Also to case-study-failure-taxonomy (to mark mode mismatches).
### design-rationale-and-evidence-rules.md

- Purpose: Guidelines for including design rationale and evidence in content (Topic 2).
- Contains: Definition of rationale/evidence in writing, why essential, default expectations (always tie decisions to data or reasoning), suggestions for types of evidence (metrics, citations), and language to use (e.g. “because,” “data shows”).
- Not contain: Broader structure advice or templates. No unrelated writing or style guides.
- Depends on: plain-language rules (for clarity), evidence-and-outcomes checklist (for specifics).
- Hand-off to: Outcome writing module (to include metrics), and to failure mode checking (lack of evidence).
### portfolio-vs-ux-copy-vs-documentation-rules.md

- Purpose: Clarify the differences between portfolio/case-study writing, UX microcopy, and general documentation (Topic 4).
- Contains: Definitions, tone and style differences, examples of each, default formatting for each. Guidelines for switching between modes and avoiding confusion.
- Not contain: Specific design rationale or audit rules. No deep structural advice beyond style.
- Depends on: content-and-case-study-expert.md, plain-language rules, UX copy size rules.
- Hand-off to: mode selection logic (writing-mode matrix), and to templates for each mode.
### case-study-failure-taxonomy.md

- Purpose: Enumerate and describe common failure modes in case study and project writing (Topic 9).
- Contains: A taxonomy/list of specific errors (e.g. “Artifacts out of context,” “Vague claims,” “Overlong narratives”), with definitions and examples. How to detect them and correct them.
- Not contain: Positive guidelines (those are elsewhere). It should not repeat general writing rules (unless framed as the failure of not following them). No microcopy or mode classification.
- Depends on: case-study-structure-rules, design-rationale rules, plain-language, etc. (It references those by describing their negation).
- Hand-off to: Test-case generation (any detected failure can become a test prompt), and to editorial review (so editors can look for these patterns).
### case-study-test-cases.md

- Purpose: Collection of concrete scenario prompts and expected outcomes for verifying the agent’s behavior (Topic 10 test cases for all topics).
- Contains: At least 20 stress-test prompts (covering different modes and failure cases), structured as input + expected check or output guidelines. Possibly categorized by topic (structure, rationale, style).
- Not contain: Explanatory theory or rules. No actual content answers (just prompts).
- Depends on: All the above rules (it draws from them to create prompts and tests).
- Hand-off to: Testing framework (for automated or manual testing of the AI). Also useful as examples in documentation/training.
## A. Condensed Operating Spec

The Content & Case Study Expert agent ensures that all design-related content (case studies, documentation, audits, UX copy) is clear, well-structured, evidence-based, and tailored to its writing mode. Key points: It first identifies the writing mode (case study vs audit vs UX copy vs doc). Then it applies the specific template and style rules for that mode. It enforces narrative structure for case studies (problem → process → outcome), short concise writing (plain language), and includes design rationale and metrics. It distinguishes audience: recruiters (for portfolios) vs end-users (for UI copy). The agent flags failures like marketing fluff, missing context, or unclear language, offering precise feedback (“this is marketing language, not a case study”). It always checks for evidence/metrics in outcomes, appropriate before/after framing, and annotates visuals. For internal use, the spec says: follow the templates in Section C, use the writing-mode matrix (B) to decide style, and use the evidence checklist (D) to ensure impact is documented.

## B. Writing-Mode Matrix

| Mode | Audience | Tone/Person | Structure | Length | Goal | Example Content |
| --- | --- | --- | --- | --- | --- | --- |
| Case Study | Recruiters/Peers | Professional, first-person narrative (I/we) | Sections (Overview, Challenge, Process, Results, Learnings)[52] | Medium (600–1000 words)[54] | Showcase process, decisions, impact | “I identified the problem of X… We solved it by Y… Outcome: +35%” |
| Audit Report | Stakeholders | Objective, formal (third-person or “we”) | Issue-Impact-Recommendation list; Executive summary | Short to medium (bullets ok) | Diagnose existing design, recommend fixes | “Finding: The sign-up form has poor labeling (impact: users drop off). Recommendation: Use clear, action-oriented labels.” |
| Rebuild Plan | Developers/Team | Direct, imperative (“do X”) | Ordered steps or outline by component | Short (steps) or medium (explanations) | Instruct on creating a new design from scratch | “Step 1: Gather requirements… Step 2: Set up project scaffold in React…” |
| Expand Proposal | Product Managers | Collaborative, second-person or passive | Current-state ➔ Proposed additions | Medium | Describe extensions, new features to enhance existing design | “Currently, the app lacks personalization. We can add a profile feature… This will…” |
| UX Copy (micro) | End Users | Informal to friendly, second person (“you”) or imperative | Very brief; labels or 1-2 sentence messages | Very short (≤1 sentence per field; <3 total) | Guide user interaction efficiently[39] | “Submit”, “Enter your email”, “Error: Password too short.”[55] |
| Documentation | End Users or Team | Neutral, explanatory (you/third person) | Sections with headings; steps, bullet lists | Medium to long (structured as needed) | Explain usage or concepts in detail | “To reset your password: 1. Go to Settings. 2. Click ‘Reset Password’. The system will email you…” |

*Use this matrix to choose style and structure. Check the “goal” column for output purpose and use the correct voice and template. *

## C. Case-Study Structure Template

- Hero/Title Section: (1–2 sentences) Clear title/subtitle summarizing project and impact[10]. Optionally a cover image or screenshot of final design.
- Project Overview: (3–4 sentences + bullets) Context: Product name, timeframe, your role, team, tools, methods, and the core challenge[9][27].
- Bullets: Company, Duration, Team, Role, Tools, Methods, Problem statement.
- Discovery/Exploration: (3–5 sentences per method) Describe research: user interviews, surveys, competitive analysis, UX audits[11][12]. For each, answer why it was done, what was learned, how it influenced the project.
- Design Process (Problem–Solution Pairs): (3–5 sentences each) Detail key design iterations. For each major problem uncovered, explain your solution (use images or wireframes if possible)[13]. Include methods like sketching, prototyping, testing, and show how each solved a problem.
- Final Solution: (2–3 short paragraphs) Present the finished design. Explain why you chose this solution and what alternatives were considered[15]. Show final screenshots/galleries. If applicable, include before-and-after visuals.
- Impact/Results: (Bulleted) List quantified outcomes[16]. Use before/after framing. E.g. “Before: X metric. After: Y metric.” Include user feedback or business results.
- Learnings/Takeaways: (1–2 paragraphs) Reflect on what you learned (new skills, insights) and what you’d do differently next[19]. Show honesty and growth mindset.
Formatting: Use headings (H2/H3) for each section. Keep paragraphs short and use lists/graphics for clarity[29][28]. Always provide captions for images[20].

## D. Evidence-and-Outcomes Checklist

- [ ] Problem Metrics: Baseline data or user-state before project (e.g. conversion %, error rate, user satisfaction).
- [ ] Solution Changes: Clear description of what changed (features, designs, processes).
- [ ] Quantitative Outcomes: Specific metrics after changes (with before values). For each claim: “X went from __ to __.”[17]
- [ ] Qualitative Outcomes: User quotes, testimonials, or satisfaction survey results if metrics unavailable[16].
- [ ] Business Impact: How did it affect goals? (revenue, engagement, retention).
- [ ] Evidence Citations: References to research or standards used to justify design (e.g. “Baymard found 86% of users pain points…”[33]).
- [ ] Validation Methods: Note how outcomes were measured (A/B test, analytics, user study).
- [ ] Before/After: Ensure every outcome has a “before” and “after” statement for comparison.
- [ ] Accuracy Checks: Verify numbers make sense (no over 100% improvement unless explained).
- [ ] Sources or Tools: If data comes from tools (Google Analytics, surveys), mention it.
- [ ] Buffer for Uncertainty: If uncertain, state confidence or context (e.g. “sample size N=30”).
Use this checklist when writing or reviewing a case study’s results to ensure solid evidence supports your claims.

## E. Stress-Test Prompts (20+)

- Mode Confusion: “Write a UX case study for an e-commerce redesign.” (The agent should use case-study structure, not marketing slogans.)
- Audit Prompt: “Audit the login flow and suggest improvements.” (Should identify issues + recommendations, not present a new design from scratch.)
- Rebuild Prompt: “Rebuild the user profile page.” (Should give step-by-step instructions for rebuilding, not critique the old one.)
- Expand Prompt: “Expand the dashboard by adding analytics features.” (Should describe new feature ideas building on current dashboard.)
- Tone Trap: “Our platform soared to success with this feature.” (The agent should flag as marketing tone, expect critique.)
- Missing Outcome: “We implemented a chatbot.” (No outcomes given; agent should ask for or add outcomes/metrics.)
- Vague Rationale: “We chose grid layout because it’s better.” (Agent: ask “Why is it better? Cite study or user need.”)
- Artifact Only: “Check out this sketch: [image].” (Agent: “Add context/caption for the sketch and explain its purpose”)
- Lengthy Paragraph: Provide a 200-word single paragraph excerpt. (Agent: break into sub-points, add headings.)
- Passive Voice: “The interface was redesigned by us.” (Agent: “Use active voice: ‘We redesigned the interface.’”)
- Jargon Overload: “The UX heuristic evaluation yielded suboptimal affordances.” (Agent: simplify or explain terms.)
- Plain Language Flaw: “At this point in time, the users are not able to….” (Agent: “Replace with ‘Currently, users cannot…’ Remove fluff.”)
- No Baseline: “Customer satisfaction improved by 20%.” (Agent: “What was the baseline satisfaction rate?”)
- No Explanation: “We did user testing to get insights.” (Agent: “Everyone knows that. What did you find and how did it change your design?”)
- Mixed Mode: “Provide a portfolio case study audit.” (Agent: identify this as conflicting, ask if audit or case study is needed.)
- Caption Missing: “(Figure: data graph shown above)” without detail. (Agent: “Describe what the graph shows and why it’s important.”)
- Marketing Style: “Our revolutionary app will transform how people live!” (Agent: “Rewrite in factual case-study tone; remove superlatives.”)
- Out-of-Context Image: “Photo of whiteboard meeting.” (Agent: “Explain what decisions or ideas are on this whiteboard.”)
- Long-Term Data: “Chart shows weekly engagement.” (Agent: “Add caption summarizing key trend/outcome from the chart.”)
- Ambiguous Request: “Help me write about my project.” (Agent: ask clarifying questions to determine if case study, documentation, etc.)
- Narrow Focus: “Write the button labels for sign-up.” (Agent: Use microcopy style, short and clear.)
- Unsupported Claim: “Our UI is now the best in the industry.” (Agent: “Cite evidence or remove claim.”)
Each prompt is designed to trigger checks: correct mode application, structure, clarity, evidence, and style. The agent should respond with guidance or restructured output based on the rules above.

[1] [2] [3] [4] [5] [6] [7] [8] [9] [11] [13] [18] [22] [23] [24] [25] [26] [29] [51] [53] UX Case Study Structure: Best Practices, Examples & Template

https://blog.uxfol.io/ux-case-study-structure/

[10] [12] [14] [15] [16] [19] [27] [32] [34] [49] [52] [54] The Ultimate UX Case Study Template & Structure (2026 Guide)

https://blog.uxfol.io/ux-case-study-template/

[17] [33] 7 Incredible UX Case Study Examples to Inspire Your Portfolio in 2026

https://uiuxdesigning.com/ux-case-study-examples/

[20] [50] Alt text, captions and titles for images | Style Manual

https://www.stylemanual.gov.au/content-types/images/alt-text-captions-and-titles-images

[21] Documentation and Images | Inquiry Journal

https://www.unh.edu/inquiryjournal/get-involved/documentation-images

[28] [41] [42] [43] [44] [45] [46] [47] [48] Plain Language Is for Everyone, Even Experts - NN/G

https://www.nngroup.com/articles/plain-language-experts/

[30] [31] Design Rationale Documentation - Pencil & Paper

https://www.pencilandpaper.io/articles/design-rationale-documentation

[35] [39] [40] [55] UX Copy Sizes: Long, Short, and Micro - NN/G

https://www.nngroup.com/articles/ux-copy-sizes/

[36] The 3 I’s of Microcopy: Inform, Influence, and Interact - NN/G

https://www.nngroup.com/articles/3-is-of-microcopy/

[37] How to Write Instructional Design Case Studies for Your Portfolio

https://theelearningcoach.com/career/how-to-write-instructional-design-case-studies-for-your-portfolio/

[38] Content Strategy vs. UX Writing - NN/G

https://www.nngroup.com/articles/content-strategy-vs-ux-writing/
