# DesignPilot v2.8 — Live Regression Report
**Date:** April 13, 2026  
**Models tested:** claude-haiku-4-5-20251001 · claude-sonnet-4-6  
**Run IDs:** live-run-v2.8-haiku · live-run-v2.8-sonnet  
**Gate threshold:** 75% (≥ 15/19 tests must pass)

---

## Executive Summary

| Model | Pass Rate | Gate | Notes |
|-------|-----------|------|-------|
| Haiku 4.5 | 12/19 = 63% | ❌ FAIL | 3 pts below gate |
| Sonnet 4.6 | 14/19 = 74% | ❌ FAIL | 1 pt below gate |

Neither model cleared the gate. Sonnet 4.6 missed by a single test (14/19 vs the required 15/19). Haiku was further back at 12/19 but improved significantly over the documented pre-v2.8 baseline of 7/19. The dominant failure mode across both models is `missing_section` — the model produces substantive content but uses different section headings or collapses required sections into prose, which the validator cannot match against its contracts.

---

## Failure Mode Summary

| Issue ID | Haiku | Sonnet | Total | Meaning |
|----------|-------|--------|-------|---------|
| `missing_section` | 4× | 6× | 10× | Required section heading absent or renamed |
| `missing_evidence_class` | 3× | 1× | 4× | Output lacks a required evidence category (constraint, permission rule, receipt) |
| `missing_required_decision` | 2× | 0× | 2× | Specific named decision token absent from output |
| `missing_rationale` | 1× | 0× | 1× | No explicit rationale language found |

---

## Per-Test Detail

### pass-01 · `ui_structure_critique` · Pricing Page Audit

**Prompt:** Audit a B2B SaaS pricing page (hero, CTA, pricing table, feature comparison, testimonials).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 100 | PASS | ✅ |
| Sonnet | 64 | FAIL | ❌ |

**Haiku — what worked:** Generated all 15 required sections including explicit Problem Framing, Findings, and Recommendations headings. Covered every required finding area (hero CTA, color-coding, feature comparison position, testimonials). Word counts were strong (78w problem framing, 177w findings, 208w recommendations). Clean section structure aligned exactly with the validator contract.

**Sonnet — what failed:** Produced 12 sections of good quality but used its own heading vocabulary. The three required contract sections — "Problem framing", "Findings", and "Recommendations" — were all missing by name. Sonnet replaced them with "What this page is trying to do", numbered findings (1–7), and "Intervention order" respectively. The content was substantively present and well-written (83–277w per section), but the validator could not map these to the expected section tokens. This is a vocabulary mismatch failure, not a content quality failure.

---

### pass-02 · `component_spec` · Split Button Component

**Prompt:** Write a component spec for a split button with primary Save action and dropdown secondary actions.

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 94 | AUTO_REVISE | ✅ |
| Sonnet | 100 | PASS | ✅ |

**Both passed.** Sonnet achieved a perfect score with 8 well-structured sections (Purpose and scope, Anatomy, State matrix, Edge states, Keyboard support, ARIA contract, Accessibility notes). Haiku scored 94 across 15 sections — more granular coverage but one minor gap triggered AUTO_REVISE. Both models handled the ARIA semantics and keyboard behavior requirements correctly.

---

### pass-03 · `dashboard_audit` · SaaS Analytics Dashboard

**Prompt:** Audit a SaaS analytics dashboard (KPI row, line chart with 4 unnamed lines, 12-item sidebar nav).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 100 | PASS | ✅ |
| Sonnet | 90 | AUTO_REVISE | ✅ |

**Both passed.** Haiku produced a compact 5-section output (Dashboard role, Key failures, Evidence and rationale, Rebuild path, Tradeoffs) hitting every contract requirement cleanly. Sonnet's 7 sections covered the same ground with individual numbered findings per element (KPI row, line chart, sidebar) plus the required summary sections. Sonnet's AUTO_REVISE flag reflects a minor gap but still above the pass threshold.

---

### pass-04 · `backend_feasibility_review` · Real-Time Collaboration Feature

**Prompt:** Feasibility review for adding Google Docs-style real-time collaboration to a React + REST/PostgreSQL app.

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 77 | FAIL | ❌ |
| Sonnet | 78 | AUTO_REVISE | ✅ |

**Haiku — what failed:** Score 77, hard failure on `missing_evidence_class: permission_rule`. The output covered 16 sections with strong technical depth (WebSocket transport, OT vs CRDT, async job surface, conflict resolution) but never used a permission, auth, or ownership rule framing explicitly. The session and presence model section existed but didn't frame the WebSocket auth handshake as an ownership/permission rule.

**Sonnet — what worked:** Same general structure. Scored 78 with AUTO_REVISE, meaning it just cleared the pass threshold. Sonnet's section on "auth on the websocket handshake" (section 6) was explicit enough to satisfy the `permission_rule` evidence requirement. The feasibility verdict section and phased rebuild path were clean and well-grounded.

---

### pass-05 · `pdf_remediation_plan` · Screen Reader PDF Fix

**Prompt:** Fix a PDF exported from Figma so it works with screen readers (reading order, TOC links, artifact tagging).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 100 | PASS | ✅ |
| Sonnet | 80 | FAIL | ❌ |

**Haiku — what worked:** Perfect score with 8 phased sections clearly named (Current failure state, 4 numbered phases, Risk controls, Why this sequence works). The sequencing rationale and preservation constraints were both explicitly stated, satisfying the `implementation_constraint` evidence requirement.

**Sonnet — what failed:** 13 sections of detailed step-by-step remediation with strong technical content (Order panel repair, artifact tagging, tag audit, accessibility checker steps). Score 80 but hard fail on `missing_evidence_class: implementation_constraint`. Sonnet provided the procedural steps but never explicitly named the sequencing constraints — why steps must happen in a specific order, what breaks if you skip them. The content was more of an instruction list than a remediation plan with justified constraints.

---

### pass-06 · `brand_positioning_pass` · Fintech Startup for Freelancers

**Prompt:** Brand positioning pass for a fintech startup targeting freelancers (trustworthy but approachable, not corporate).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 82 | FAIL | ❌ |
| Sonnet | 90 | AUTO_REVISE | ✅ |

**Haiku — what failed:** Score 82, hard fail on `missing_evidence_class: implementation_constraint` — specifically, the validator requires use of a real constraint such as trust, usability, or category convention. Haiku's 7 sections (Audience, Positioning frame, Trust and proof burden, Tone territory, Next moves) were thematically correct but never grounded a constraint explicitly enough. The trust and proof burden section (158w) existed but framed it as recommendation rather than constraint.

**Sonnet — what worked:** Scored 90 with AUTO_REVISE. Added a "Wedge against the field" section and a "Positioning claim (internal compass, not tagline)" section that both made the category convention constraints explicit. The vocabulary satisfied the `implementation_constraint` check.

---

### pass-07 · `case_study_rewrite` · Design Portfolio Case Study

**Prompt:** Rewrite a bare-bones onboarding redesign case study for a design portfolio.

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 74 | FAIL | ❌ |
| Sonnet | 96 | AUTO_REVISE | ✅ |

**Haiku — what failed:** Score 74, two hard failures. First: `missing_section` — the validator requires an "Outcome and proof" section; Haiku had "What shifted" (21w) which is too short and too vague. Second: `missing_evidence_class: file_backed_receipt` — the output never referenced benchmark files, maps, or proof artifacts. The rewrite was stylistically fine across 8 sections but lacked proof infrastructure.

**Sonnet — what worked:** Score 96, AUTO_REVISE. Produced 5 clean sections including an explicit "Outcome and proof boundaries" section (128w) that directly addressed what was measured vs what was inferred. Named the specific constraints on proof ("we have session recordings but no A/B data"). This satisfied both the section contract and the evidence class.

---

### pass-08 · `accessibility_feedback_audit` · Mobile App Accessibility

**Prompt:** Audit a mobile app with icon-only nav, placeholder-only form labels, color-only errors, silent loading spinner.

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 100 | PASS | ✅ |
| Sonnet | 100 | PASS | ✅ |

**Both achieved perfect scores.** The most consistent result in the suite. Both models correctly identified all four barrier classes (icon-only nav, missing form labels, color-only error states, silent async feedback), assigned correct severity rankings, and provided WCAG-grounded repair priorities. Haiku used 15 granular sections; Sonnet used 8 more consolidated sections. Both passed the validator contract cleanly.

---

### pass-09 · `color_system_spec` · Healthcare SaaS Color System

**Prompt:** Define a color system for a healthcare SaaS dashboard (status colors, WCAG AA contrast, dark mode, migration from existing colors).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 70 | FAIL | ❌ |
| Sonnet | 84 | AUTO_REVISE | ✅ |

**Haiku — what failed:** Score 70, three hard failures. `missing_section`: no Migration notes section. `missing_rationale`: no explicit rationale language found anywhere in the output. `missing_required_decision: migration_strategy`: no description of how existing colors migrate into the new role model. Haiku produced only 4 sections (Role model, Core semantic roles, Token map light, Token map dark) — technically dense but missing the migration layer entirely. This is also flagged as a known open failure in the regression context for Sonnet on older runs, suggesting migration coverage has always been a weak point.

**Sonnet — what worked:** Score 84, AUTO_REVISE. Produced 11 sections including an explicit "Migration notes" section (60w) and a "Primitive palette (hue selection rationale)" section that satisfied the rationale requirement. The migration section was brief but present and named correctly, satisfying the contract.

---

### pass-10 · `graphic_critique` · Conference Poster Design

**Prompt:** Critique a conference poster with decorative typeface, photo background, small logo, invisible date.

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 82 | AUTO_REVISE | ✅ |
| Sonnet | 94 | AUTO_REVISE | ✅ |

**Both passed.** Sonnet scored higher (94) with a more consolidated 7-section structure (Communication goal, Composition failures, 4 numbered interventions, Distance and emphasis tradeoff). Haiku's 9 sections at 82 covered the same ground but with thinner per-section depth (12–33w on several sections). Both correctly identified the hierarchy problem, date invisibility, and photo dominance as primary issues.

---

### pass-11 · `layout_reconstruction_plan` · Brand Guidelines from 2018 PDF

**Prompt:** Reconstruct a layout system from a 2018 PDF brand guidelines document to apply to new templates.

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 72 | FAIL | ❌ |
| Sonnet | 88 | FAIL | ❌ |

**Both failed on the same issue:** `missing_section: Source constraints`. Neither model produced a section explicitly named or semantically equivalent to "Source constraints" — the section that documents what limitations the PDF source imposes on the reconstruction (e.g., what can't be inferred, what's ambiguous, what requires judgment calls).

**Haiku** produced 22 sections with strong technical coverage (grid extraction, confidence mapping, preservation rules, breakpoint specs) but didn't frame the PDF's limitations as a named constraints section. The closest was a "Beware of" section (64w) and "Risk controls and verification" (105w), but neither used source-constraint vocabulary.

**Sonnet** produced 15 cleaner sections including "What to flag as uncertain" (77w) and "Step 5: Write down the inference boundary" (54w). Again, semantically close but vocabulary didn't match. This is a consistent vocabulary gap for both models on this task type — they describe the constraints without naming the section "Source constraints."

---

### pass-12 · `type_system_recommendation` · Fintech Type System

**Prompt:** Recommend a type system for a fintech product spanning marketing site, dashboard, and mobile.

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 92 | AUTO_REVISE | ✅ |
| Sonnet | 84 | AUTO_REVISE | ✅ |

**Both passed.** Haiku scored higher (92) with 23 sections covering role map, display/heading/body/numeric roles, typeface pairing, readability rules, 4-phase adoption guidance, accessibility notes, and explicit Migration notes and Token naming subsections. Sonnet's 12 sections at 84 were more consolidated — stronger per-section depth but fewer subsections. Both AUTO_REVISE flags indicate minor gaps (likely thin sections or partial evidence class coverage) but well above the pass threshold.

---

### pass-13 · `ux_research_gap_map` · B2B Project Management Tool Research

**Prompt:** Map research gaps for a B2B project management redesign (3 stakeholder interviews, 2 usability sessions, no exit data, no competitive analysis).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 94 | AUTO_REVISE | ✅ |
| Sonnet | 88 | AUTO_REVISE | ✅ |

**Both passed comfortably.** Haiku scored 94 with 13 sections, correctly identifying 5 prioritized research gaps and providing a 3-phase research plan (run immediately / in parallel / defer). Sonnet scored 88 with 12 sections, 4 gaps with individual study designs (exit interviews, task walkthroughs, competitive review, drop-off analysis). Both demonstrated strong coverage of gap prioritization by decision impact, which is the core contract requirement.

---

### pass-14 · `frontend_implementation_review` · Permissions-Heavy Scheduling Dashboard

**Prompt:** Review a front-end implementation plan for a permissions-heavy scheduling dashboard (defaults to client-side rendering and ad-hoc boolean state).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 92 | FAIL | ❌ |
| Sonnet | 78 | AUTO_REVISE | ✅ |

**Haiku — what failed:** Score 92 — the highest-scoring failure in the suite. Hard fail on `missing_required_decision: cost_or_degraded_path`. The output (10 sections, 274w boundary/state model section, strong architectural framing) covered the server/client split, typed state machine, and mutation lifecycle in depth, but never explicitly named the cost surface or degraded path for the proposed architecture. The content implied it but didn't make it a named decision.

**Sonnet — what worked:** Score 78, AUTO_REVISE. Produced an "Identified cost surfaces" section (46w) that named the cost surface explicitly, satisfying the contract. The section was brief but present.

---

### pass-15 · `backend_architecture_spec` · Multi-Tenant Scheduling Platform

**Prompt:** Write a backend architecture spec for a multi-tenant scheduling platform (team workspaces, cursor-based activity feed, approval workflows).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 72 | AUTO_REVISE | ✅ |
| Sonnet | 96 | AUTO_REVISE | ✅ |

**Both passed.** Sonnet scored substantially higher (96 vs 72). Sonnet's 12 sections with clear tier-based framing (System framing → Authority boundaries → Data/consistency/delivery) provided richer coverage of tenant isolation model, RBAC authorization, and consistency stance. Haiku's 11 sections at 72 covered actors, authority tables, and permission model but with thinner depth on consistency model (122w) and activity feed design being absent. Both AUTO_REVISE flags reflect minor gaps but pass the gate.

---

### pass-16 · `api_reliability_security_review` · POST /exports PDF Generation

**Prompt:** Audit POST /exports endpoint that generates a PDF synchronously (no async, no idempotency, returns 200 even on failure).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 75 | AUTO_REVISE | ✅ |
| Sonnet | 75 | AUTO_REVISE | ✅ |

**Both passed with identical scores (75, AUTO_REVISE).** Haiku used 17 sections covering failure semantics, error contract, async lifecycle with full request/response examples (202 accepted, in-progress, success, failure states), idempotency contract, terminal states, and resilience. Sonnet used 11 more consolidated sections with a status code map and required async lifecycle flow. Both satisfied the core async job model contract at the minimum passing threshold. Both are borderline — one evidence gap away from failure.

---

### pass-17 · `frontend_implementation_review` · Redux vs Local State Architecture Decision

**Prompt:** Explain a front-end architecture decision (Redux vs local state + context) across Functional, Integrative, and Strategic tiers.

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 75 | FAIL | ❌ |
| Sonnet | 77 | FAIL | ❌ |

**Both failed.** The contract requires a "Rendering and mutation strategy" section (Haiku) and a "Risks and safer path" section (Sonnet). Neither model produced these named sections.

**Haiku** used 21 sections with strong tiered framing — Functional tier with decision matrix (how much state, how often it changes, team size, growth), 4 avoidance rules, Integrative tier with tradeoff resolution. Score 75 — the content is there but the required `Rendering and mutation strategy` section name is absent. This is a pure vocabulary mismatch.

**Sonnet** used 4 clean sections (Functional, Integrative, Three things that determine the right answer, Strategic). Score 77, missing "Risks and safer path." Sonnet's strategic tier addressed risk implicitly but never named a section for it. This is also vocabulary mismatch — the risk analysis exists inside "Strategic tier" prose but isn't surfaced as a standalone section.

---

### pass-18 · `api_reliability_security_review` · POST /api/v1/projects/{id}/members

**Prompt:** Review POST /api/v1/projects/{id}/members (adds a user to a project, returns 200 with full member list, no idempotency key, no object-level auth).

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 73 | AUTO_REVISE | ✅ |
| Sonnet | 73 | FAIL | ❌ |

**Haiku passed, Sonnet failed — same score (73).** The difference is in which contract checks each model satisfied.

**Haiku** produced 17 sections organized around governing decisions and idempotency/async lifecycle with a full request/response contract. The resilience and observability content was present within the governing decisions structure, satisfying that section check.

**Sonnet** produced 6 sections structured directly as governing decisions (object-level auth, 201 status code, idempotency key, RFC 9457 error format, return the created record, tradeoff summary). Score 73, hard fail on `missing_section: Resilience and observability`. The observability requirement (trace_id on errors, quota limits) was addressed in governing decision 4 but was not surfaced as a standalone section, which the validator requires.

This is the context document's known open failure for Sonnet — "model addresses async lifecycle but doesn't name the job lifecycle pattern explicitly."

---

### pass-19 · `text_humanization_revision` · AI Marketing Text Rewrite

**Prompt:** Rewrite a stiff, AI-flavored marketing paragraph about AI-powered solutions to read more naturally.

| Model | Score | Decision | Result |
|-------|-------|----------|--------|
| Haiku | 88 | AUTO_REVISE | ✅ |
| Sonnet | 90 | AUTO_REVISE | ✅ |

**Both passed.** This is the most straightforward task in the suite and both models handled it well. Haiku used 5 sections (Job of the piece, Pattern scan, Meaning-preservation guard, What changed, Why it works better). Sonnet used 3 sections (Patterns to fix, Revised, What changed and why). Both AUTO_REVISE flags likely reflect thin section depth on some subsections, but both well above the pass threshold.

---

## Cross-Model Comparison

### Tests where Haiku beat Sonnet
| Test | Haiku | Sonnet | Delta |
|------|-------|--------|-------|
| pass-01 | 100 ✅ | 64 ❌ | +36 |
| pass-05 | 100 ✅ | 80 ❌ | +20 |
| pass-09 | — (fail) | — (pass) | Haiku failed harder |
| pass-12 | 92 ✅ | 84 ✅ | +8 |

### Tests where Sonnet beat Haiku
| Test | Haiku | Sonnet | Delta |
|------|-------|--------|-------|
| pass-04 | 77 ❌ | 78 ✅ | +1 |
| pass-06 | 82 ❌ | 90 ✅ | +8 |
| pass-07 | 74 ❌ | 96 ✅ | +22 |
| pass-14 | 92 ❌ | 78 ✅ | Sonnet passed despite lower score |
| pass-15 | 72 ✅ | 96 ✅ | +24 |

### Both failed (structural problem, not model problem)
| Test | Haiku | Sonnet | Shared failure mode |
|------|-------|--------|---------------------|
| pass-11 | 72 ❌ | 88 ❌ | `missing_section: Source constraints` |
| pass-17 | 75 ❌ | 77 ❌ | `missing_section` (different names) |

---

## Root Cause Analysis

### 1. Vocabulary mismatch (largest category)
The validator matches section headings against a contract vocabulary list. Both models consistently produce the required *content* but under different heading names. Examples:
- pass-01: Sonnet uses "Intervention order" instead of "Recommendations"
- pass-11: Both models use "inference boundary" / "source uncertainty" instead of "Source constraints"
- pass-17: Both models embed risk analysis in a tier section instead of "Risks and safer path"

**Fix path:** Extend `any_of` aliases in `src/schemas/task_contracts.json` and log to `src/schemas/vocab_calibration_log.json`.

### 2. Missing named decision tokens (pass-04 Haiku, pass-14 Haiku)
The validator looks for explicit decision tokens (`permission_rule`, `cost_or_degraded_path`). Both models covered the underlying concept but never surfaced it as a standalone named decision. Haiku scored 92 on pass-14 — the content was almost entirely correct — but the decision token was buried in prose.

**Fix path:** Add explicit decision-framing instructions to the relevant task launchers in `dist/runtime/task_launchers/`.

### 3. Missing sections — structural omissions (pass-07 Haiku, pass-09 Haiku, pass-18 Sonnet)
Some failures are genuine content gaps, not vocabulary issues. Haiku on pass-09 produced no migration layer at all (only 4 sections, no Migration notes). Haiku on pass-07 had no outcome/proof section. These require launcher prompt improvements to enumerate required coverage areas explicitly.

### 4. Evidence class detection (pass-04, pass-05, pass-06)
The `missing_evidence_class` failures occur when the validator requires a specific type of reasoning to be present (permission rules, implementation constraints, proof receipts) and the model uses correct reasoning but not the expected vocabulary. Sonnet is better at this than Haiku overall (1 vs 3 evidence class failures).

---

## Recommendations

**To get Sonnet from 14/19 to 15/19 (gate PASS), fixing any one of these would be sufficient:**

1. **pass-01:** Add "Problem framing", "Findings", "Recommendations" as section aliases for Sonnet's vocabulary in the `ui_structure_critique` contract.
2. **pass-11:** Add "Source uncertainty" / "inference boundary" / "what to flag" as aliases for "Source constraints" in the `layout_reconstruction_plan` contract.
3. **pass-17:** Add "risks and tradeoffs" framing to the `frontend_implementation_review` tier-3 launcher so the model always produces a standalone risks section.
4. **pass-18:** Add "Resilience and observability" as a required standalone section to the `api_reliability_security_review` launcher (currently the launcher doesn't enforce this as a named section).

**To improve Haiku from 12/19 toward the gate, the highest-leverage changes are:**

1. pass-07: Strengthen the `case_study_rewrite` launcher to explicitly require an "Outcome and proof" section.
2. pass-09: Strengthen the `color_system_spec` launcher to explicitly require a "Migration notes" section with named strategy.
3. pass-11: Same alias fix as Sonnet above.
4. pass-17: Same tier-3 risks section fix as Sonnet above.
