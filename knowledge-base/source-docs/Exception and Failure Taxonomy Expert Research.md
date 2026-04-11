<!-- Optimized from original source file: Exception and Failure Taxonomy Expert Research.docx. All textual content preserved in markdown form for size-efficient packaging. -->

# Exception and Failure Taxonomy Expert for Modular AI Design Operator Packs

## Research basis and architectural framing

A strict Exception & Failure Taxonomy Expert (EFTE) for an AI “design operator pack” is best treated as a **first-class control plane**: it runs *before, during, and after* operator execution to (1) validate prerequisites, (2) classify breakdowns deterministically, (3) drive routing/fallback/escalation, and (4) emit observability-grade telemetry for debugging and continuous improvement. This framing aligns with mature reliability and risk practices where “handling errors” is not an afterthought but a deliberately engineered system function. [\[1\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)

The most implementation-oriented references relevant to this kind of EFTE fall into a few complementary buckets:

- **AI risk & governance frameworks** that explicitly treat governance/controls as lifecycle-spanning (usable for off-phase and governance failures). The National Institute of Standards and Technology[\[2\]](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html?utm_source=chatgpt.com) Artificial Intelligence Risk Management Framework (AI RMF 1.0)[\[3\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com) defines four functions—GOVERN, MAP, MEASURE, MANAGE—and notes that GOVERN applies across all lifecycle stages, while the others can be applied in system-specific contexts at particular lifecycle stages. [\[4\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) The Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile[\[5\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) operationalizes many governance and safety actions (e.g., “plan to halt development/deployment” under unacceptable risk; red-teaming; detecting novel domains). [\[6\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) The ISO/IEC 23894:2023 — Artificial intelligence — Guidance on risk management[\[7\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com) and ISO/IEC 42001:2023 — AI management systems[\[8\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com) provide complementary organizational risk-management and management-system requirements (useful for governance gates, “release approval,” and continuous improvement loops). [\[9\]](https://www.iso.org/standard/77304.html?utm_source=chatgpt.com)

- **Structured error representation standards** that enable a taxonomy to be machine-actionable (usable for operator-to-operator handoffs and external API surfaces). RFC 9457: Problem Details for HTTP APIs[\[10\]](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships?utm_source=chatgpt.com) defines a machine-readable, standardized envelope for error details and explicitly obsoletes RFC 7807. [\[11\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) In parallel, gRPC[\[12\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) status codes provide a compact, interoperable error classifier (e.g., distinguishing PERMISSION_DENIED vs RESOURCE_EXHAUSTED) that is helpful when EFTE needs to map internal design exceptions onto transport semantics. [\[13\]](https://grpc.io/docs/guides/status-codes/?utm_source=chatgpt.com)

- **Reliability and resiliency patterns** that translate taxonomy classifications into deterministic fallback behavior. Google[\[14\]](https://www.designtokens.org/TR/2025.10/format/)’s Site Reliability Engineering guidance on overload explicitly recommends “degraded responses” as a technique for continuing operation under resource pressure. [\[15\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) Their guidance also warns that graceful degradation paths can rot if not exercised, recommending regularly running a subset of servers near overload to test these paths. [\[16\]](https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com) Microsoft[\[17\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)’s circuit breaker pattern documentation provides an actionable mechanism for stopping repeated calls to failing dependencies and allowing recovery—useful for tool failures, missing-asset fetch timeouts, or model/tool gateway instability. [\[18\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)

- **Observability conventions** that ensure exceptions are not just handled but also measurable. OpenTelemetry[\[19\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) semantic conventions specify standardized exception fields (e.g., exception.type, exception.message, exception.stacktrace) and require exception events to use the event name “exception,” enabling consistent logging/tracing across languages and services. [\[20\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)

- **Accessibility and readability standards** that provide “hard thresholds” for typography/layout feasibility decisions. World Wide Web Consortium[\[21\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)’s Web Content Accessibility Guidelines (WCAG) 2.2[\[22\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com) defines concrete pass/fail criteria such as minimum text contrast (4.5:1 for normal text, with exceptions) and new target size requirements (24×24 CSS pixels baseline with defined exceptions). [\[23\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com) These thresholds are essential for “unreadable typography requests” and “impossible density” detection.

Finally, because operator packs often encode brand/layout decisions as **design tokens**, the Design Tokens Community Group[\[24\]](https://www.designtokens.org/TR/2025.10/format/)’s Design Tokens Format Module 2025.10[\[25\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) is directly relevant: it is intended for implementation and considered stable, and it normatively specifies error conditions (e.g., unresolvable references, circular references, type mismatches) as well as fallback behavior when platforms/tools cannot represent a token value exactly. [\[26\]](https://www.designtokens.org/TR/2025.10/format/)

## Core taxonomy model

A strict EFTE works best as a **two-axis model** that separates *what went wrong* from *when it went wrong*:

- **Exception** (preflight/policy/spec): a condition indicating “do not proceed as specified.” Typical examples: off-phase request, missing required assets, contradictory constraints, inaccessible typography, unsupported implementation ask. These should be detected at **Phase P0–P2** (intake/context/spec) whenever possible. This mirrors lifecycle-wide governance emphasis in AI RMF (GOVERN across lifecycle; MAP/MEASURE/MANAGE in stage contexts) and management-system approaches that treat governance and continual improvement as systemic. [\[27\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)

- **Failure** (runtime/postflight): a condition indicating “we tried to execute and did not produce a valid artifact.” Typical examples: tool timeout, corrupted export, token resolver throws unresolvable reference, router loop. These are controlled through resiliency patterns (circuit breakers, retries, degraded responses) and measured with telemetry conventions (standard exception fields/events). [\[28\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)

### Canonical code scheme

Use **stable, deterministic codes** that are:

- **Hierarchical**: `EXC.<DOMAIN>.<MODE>.<DETAIL?>` and `FAIL.<DOMAIN>.<MODE>.<DETAIL?>`
- **Transport-mappable**: can map to RFC 9457 “problem details” for external surfaces and optionally to gRPC status codes for RPC-style APIs. [\[29\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)
- **Telemetry-friendly**: fields parallel OpenTelemetry’s exception attributes and can be emitted as span/log events. [\[30\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)

A practical top-level domain set for design operator packs:

- PHASE, ROUTING, CONSTRAINT, INPUT, ASSET, ACCESSIBILITY, LAYOUT, BRAND, IMPLEMENT, DOC, FALLBACK, TOOL/EXPORT (failures)

### Severity levels and dispositions

A strict EFTE needs severity levels that connect directly to what the system is allowed to do next:

- **S0 (Block & Escalate / Refuse)**: safety/security/legal/compliance risk; governance gate required; disallowed fallback risk.
- **S1 (Block & Clarify)**: cannot proceed without user or authoritative data; contradictions; missing critical assets.
- **S2 (Degrade with Disclosure)**: can proceed with limited scope while preserving non-negotiables; must disclose.
- **S3 (Warn & Continue)**: non-blocking quality risk; log + proceed.

This structure supports both reliability-style mitigation (graceful degradation under overload) and governance-oriented hard stops (halt development/deployment when negative risk is unacceptable). [\[31\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)

### Problem-details envelope for operator pack outputs

Adopt RFC 9457’s envelope as your external (and optionally internal) “exception object” shape:

- `type`, `title`, `status`, `detail`, `instance` plus extensions:
- `exception_code`, `severity`, `phase`, `operator_candidates`, `missing_inputs`, `conflicts`, `checks`, `next_actions`.

This is the simplest mechanism to ensure machine-readable errors across operator boundaries and client surfaces. [\[32\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)

### Required evidence model

Every classification must be backed by structured evidence:

- Parsed constraints (hard vs soft)
- Phase inference + unmet prerequisites
- Asset references + access results
- Accessibility checks (contrast/targets/reflow/text spacing)
- Feasibility checks (density, grid inference fit, platform support)
- Routing candidate set + scores + tie-break audit trail
- Fallback steps attempted (if any)

This aligns with the design tokens specification’s emphasis on strict error detection/reporting for references and circularity, and with observability conventions for consistent exception reporting. [\[33\]](https://www.designtokens.org/TR/2025.10/format/)

## Topic modules

Each topic below is written as an EFTE “module card” with the required elements: definition, importance, default rules, exception rules, fallback logic, failure conditions, measurable thresholds, implementation guidance, and test cases. When numeric thresholds are taken from standards, they are cited.

**Topic: exception categories for operator systems**

**Definition**  
A structured set of mutually distinguishable exception domains and modes that represent *why a design operator pack cannot proceed* (exception) or *did not successfully complete* (failure). The taxonomy must be stable enough to serve as an API contract, and expressive enough to drive routing and fallback decisions. RFC 9457 provides a standard envelope for machine-readable error details; gRPC status codes provide a compact error classifier that can be mapped from your richer internal codes. [\[29\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)

**Why it matters for an Exception Taxonomy Expert**  
Without stable categories, the agent cannot (a) route deterministically, (b) choose safe fallbacks, or (c) produce observability that supports debugging and continuous improvement. OpenTelemetry’s exception conventions demonstrate why standard naming/structure matters for interoperability and correlation. [\[30\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)

**Default rules**  
Classify using a two-pass method:  
1) Determine **phase** (intake/context/spec/build/QA/export).  
2) Determine **primary domain** (PHASE/ROUTING/CONSTRAINT/ASSET/ACCESSIBILITY/LAYOUT/BRAND/IMPLEMENT/DOC/FALLBACK/TOOL).  
If multiple domains apply, select a single **primary** domain by precedence: S0 safety/governance \> preflight blockers \> runtime/tool failures \> quality warnings, and attach the rest as `secondary_codes`.

**Exception rules**  
If a detected condition is S0 (policy/safety/compliance), do not attempt “creative workarounds.” The GenAI profile explicitly includes actions like devising a plan to halt deployment when negative risk is unacceptable; EFTE should treat such situations as non-negotiable blocks. [\[6\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

**Fallback logic**  
Use a ladder: retry bounded → alternate implementation strategy → cached/last-known-good (if appropriate) → scope reduce → clarify → escalate → refuse/redirect. This pattern is consistent with resilience guidance emphasizing degraded responses under overload and ensuring degraded paths actually work. [\[34\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)

**Failure conditions**  
Failures occur when execution starts but does not produce a valid artifact (timeouts, unhandled tool errors, corrupted export, unresolved token references or circular token aliasing). The design tokens spec is explicit that tools MUST detect and report circular references and unresolvable references as errors. [\[35\]](https://www.designtokens.org/TR/2025.10/format/)

**Measurable thresholds**  
- Classification confidence threshold (router): default `≥ 0.75` to auto-route; otherwise route ambiguity. (Implementation policy; tune via evaluation.)  
- Retry budget: max 2 retries for retryable failures; beyond that escalate. (Reliability control; aligns with circuit breaker usage to prevent repeated failures.) [\[18\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack**  
- Define a versioned schema for exception objects (RFC 9457-compatible). [\[36\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)  
- Use OpenTelemetry-compatible fields and emit “exception” events with standardized attributes. [\[37\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)  
- Provide a deterministic mapping from internal codes to gRPC/HTTP statuses when exporting across boundaries. [\[38\]](https://grpc.io/docs/guides/status-codes/?utm_source=chatgpt.com)

**Test cases**  
- “Return a structured error object when the logo URL is unreachable.” → `EXC.ASSET.INACCESSIBLE`  
- “Operator crashes on token circular reference.” → `FAIL.TOKEN.CIRCULAR_REF` (must include the cycle chain evidence) [\[39\]](https://www.designtokens.org/TR/2025.10/format/)

**Topic: routing ambiguity and collision handling**

**Definition**  
Routing ambiguity occurs when multiple operators plausibly match a request, and selecting any single operator could materially change the artifact. Collision is stronger: two operators claim exclusive ownership over the same artifact domain (e.g., both “layout owner” and “brand owner” attempt to write the same token/structure), risking inconsistent outputs.

**Why it matters for an Exception Taxonomy Expert**  
Routing ambiguity drives inconsistent results and makes failure modes non-reproducible. Collision can produce cascading inconsistencies similar to distributed-systems failure coupling, where partial outputs mask deeper errors—exactly the kind of scenario resilient systems aim to prevent via strict fault boundaries and protective patterns. [\[40\]](https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com)

**Default rules**  
- Score each operator by (a) constraint coverage, (b) match confidence, (c) risk score, (d) missing prerequisites count.  
- If top-2 scores are within a small delta (e.g., 0.08), classify as `EXC.ROUTING.AMBIGUOUS` and ask a *single* disambiguating question.

**Exception rules**  
If ambiguity intersects with accessibility or governance non-negotiables, route to the policy/accessibility-aware path by default (or require clarification) because accessibility failures have hard thresholds and governance failures require lifecycle-wide controls. [\[41\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)

**Fallback logic**  
- First fallback is not “pick one” but “clarify intent.”  
- If user refuses to clarify, provide a conservative default and label it as a chosen assumption (S2), unless that would break non-negotiables.

**Failure conditions**  
- Router loops (operator A delegates to router; router returns A again; repeat).  
- Non-deterministic selection without audit trail.  
These are reliability failures that must be detected via loop guards and route history.

**Measurable thresholds**  
- Ambiguity threshold: `(score1 - score2) ≤ 0.08` triggers clarification.  
- Loop threshold: same operator re-entered with identical inputs more than once triggers `FAIL.ROUTER.LOOP`.

**Implementation guidance for an AI operator pack**  
- Maintain a “single-owner per artifact domain” rule and enforce it as a hard constraint.  
- Emit routing evidence: candidates + scores + tie-break path (critical for debugging and reproducibility).

**Test cases**  
- Prompt: “Redesign this landing page; also generate design tokens and accessibility fixes.”  
Expected: ambiguity between layout/brand/accessibility operators; system either decomposes into a plan or asks which priority is primary: brand fidelity vs a11y vs density.

**Topic: off-phase and governance failures**

**Definition**  
Off-phase requests are requests that attempt to perform work that depends on prerequisites not yet satisfied in the operator pack lifecycle (e.g., asking for final export before brand tokens are defined, or asking for governance-approved publication before review). Governance failures are requests that bypass or conflict with required governance controls (policy, approvals, unacceptable use constraints).

**Why it matters for an Exception Taxonomy Expert**  
AI RMF explicitly frames GOVERN as lifecycle-spanning and emphasizes integrating risk management across stages; the GenAI profile includes operational governance actions such as planning to halt deployment when risk is unacceptable. This translates directly into “phase gates” where the EFTE must block or escalate. [\[42\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)

**Default rules**  
- Infer current phase (P0 intake, P1 context, P2 spec, P3 build, P4 QA, P5 export/publish).  
- Maintain a dependency graph: export requires QA; QA requires assets/spec; spec requires context/tokens; tokens require brand authority.  
- If request targets a higher phase without prerequisites, classify `EXC.PHASE.OFF_PHASE` (S1) and state the minimal prerequisite set.

**Exception rules**  
If the off-phase request involves public release, regulated contexts, or unacceptable-risk signals, elevate to S0 and require governance escalation (or refuse). This aligns with the GenAI profile’s emphasis on halting deployment under unacceptable risk and running red-teaming and monitoring for novel domains. [\[6\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

**Fallback logic**  
- Convert off-phase requests into the earliest feasible phase deliverable (e.g., “I can produce a draft spec + asset checklist now; export comes after QA”).  
- If the user insists on bypassing gates, refuse or escalate.

**Failure conditions**  
- “Silent phase skipping”: system produces “final” artifacts without doing QA/accessibility checks.  
- “Governance bypass”: system publishes/exports with missing approvals.

**Measurable thresholds**  
- Prerequisite completeness: if any required prerequisite is missing → block (S1).  
- Governance gate: if output is labeled “publish,” “ship,” “production,” or “legal approved” and governance metadata is absent → escalate (S0).

**Implementation guidance for an AI operator pack**  
- Encode phase gates in code as hard rules (not prompt text).  
- Emit a phase-aware problem detail object (RFC 9457 envelope) listing missing prerequisites. [\[43\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)  
- Track governance artifacts as auditable objects (approval IDs, reviewers, timestamps).

**Test cases**  
- “Publish the final accessible marketing site now; we’ll check contrast later.” → `EXC.PHASE.GOVERNANCE_GATE_REQUIRED` (S0) + refusal/redirect because accessibility checks are non-negotiable if claiming accessible readiness. [\[44\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)

**Topic: accessibility and readability violations**

**Definition**  
Accessibility/readability violations are requests or specs that cause the produced artifact to fail recognized accessibility criteria (contrast, target size, semantics, reflow, text spacing), or violate empirically supported readability heuristics (e.g., line length) in ways that materially degrade usability.

**Why it matters for an Exception Taxonomy Expert**  
Unlike many “soft” design preferences, accessibility includes **objective pass/fail thresholds** that should be encoded as hard constraints. WCAG defines minimum text contrast ratios, target sizes, and text spacing resilience; these are precisely the kind of numeric checks EFTE should use to detect unreadable typography and impossible density. [\[45\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)

**Default rules**  
- Treat WCAG AA baselines as default non-negotiables unless the user explicitly targets a different standard. [\[46\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)  
- Run automated checks (contrast, target sizes, non-text contrast, reflow constraints, text spacing resilience, headings/labels). [\[47\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
- If a request explicitly asks to violate them (e.g., “remove focus indicators,” “make low-contrast microcopy”), classify `EXC.ACCESSIBILITY.<MODE>` and either propose compliant alternatives or refuse depending on severity and context.

**Exception rules**  
If the user requests non-compliance *and* the artifact is intended for public/production use, treat it as S0 governance risk if the system would be misrepresenting compliance, or S1 if it’s clearly a deliberate non-compliance with no misrepresentation. (This is governance tied to claims, not only to the visuals.) [\[48\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)

**Fallback logic**  
- First fallback: propose a compliant alternative that preserves design intent (e.g., keep “premium subtlety” but raise contrast, adjust type scale, add spacing).  
- Second fallback: constrain the request to draft/internal-only and label as non-compliant.  
- If user insists on non-compliance while claiming accessibility, refuse.

**Failure conditions**  
- Output that fails minimum contrast (normal text below 4.5:1; large text below 3:1). [\[44\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
- Touch targets below 24×24 CSS pixels without permitted exceptions. [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)  
- Layout fails reflow at 320 CSS pixels (requires two-dimensional scrolling where not excepted). [\[50\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)  
- Text spacing changes cause loss of content: fails line-height/spacing resilience requirements. [\[51\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com)  
- Ambiguous or misleading headings/labels: violates the intent of clear headings and labels. [\[52\]](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html?utm_source=chatgpt.com)

**Measurable thresholds**  
- Contrast: 4.5:1 for normal text; 3:1 for large text (WCAG minimum). [\[44\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
- Target size: 24×24 CSS px minimum baseline with defined exceptions. [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)  
- Reflow: support reflow at 320 CSS px (typical mapping to 400% zoom on 1280px). [\[53\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)  
- Text spacing resilience: line height ≥ 1.5× font size; paragraph spacing ≥ 2×; letter spacing ≥ 0.12×; word spacing ≥ 0.16× without loss. [\[51\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com)  
- Readability heuristic: body text line length ~50–75 characters as a practical baseline. [\[54\]](https://baymard.com/blog/line-length-readability?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack**  
- Encode accessibility checks as deterministic validators that return structured failures (not subjective “looks OK”).  
- If the operator pack outputs web UI, incorporate semantics evidence (headings, labels, info/relationships) because structure must be programmatically determinable, not only visually implied. [\[55\]](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships?utm_source=chatgpt.com)  
- Integrate accessible naming practices when relevant, guided by accessible name computation and ARIA practices, to prevent “label mismatch” breakage. [\[56\]](https://www.w3.org/TR/accname-1.2/?utm_source=chatgpt.com)

**Test cases**  
- “Set 10px light gray text on white for all labels.” → `EXC.ACCESSIBILITY.CONTRAST_FAIL` with measured contrast ratio and suggested alternative palette. [\[44\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
- “Make icon buttons 16×16 on mobile to fit more.” → `EXC.ACCESSIBILITY.TARGET_SIZE_FAIL` + density workaround (progressive disclosure). [\[57\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)

**Topic: implementation feasibility failures**

**Definition**  
Implementation feasibility failures occur when the requested design cannot be implemented within the target platform/tooling constraints (feature support, performance budgets, format capabilities, export pathways), or when implementing it would introduce unacceptable security/reliability risks.

**Why it matters for an Exception Taxonomy Expert**  
A design operator pack that “hallucinates feasibility” creates downstream rework and can push teams into risky fallbacks. The design tokens spec explicitly acknowledges that some tools/platforms may not represent certain token values and recommends falling back to closest approximations—showing feasibility constraints are normal and must be handled explicitly, not hidden. [\[58\]](https://www.designtokens.org/TR/2025.10/format/)

**Default rules**  
- Require explicit target modality: web, iOS, Android, design tokens, PDF, etc.  
- Maintain a capabilities registry per target (supported token types, layout primitives, interaction models).  
- When asked for unsupported features, classify `EXC.IMPLEMENT.UNSUPPORTED_FEATURE` (S1) and propose equivalent alternatives.

**Exception rules**  
If feasibility is blocked by dependency instability or quota/resource exhaustion, classify as failure and apply resilience patterns (retry/circuit breaker) rather than treating it as a design exception. [\[59\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)

**Fallback logic**  
- For unsupported visuals: “closest supported approximation,” disclosed as such (mirrors design tokens guidance). [\[60\]](https://www.designtokens.org/TR/2025.10/format/)  
- For unstable dependencies: retry bounded; then circuit breaker and degrade (cached/partial). [\[59\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)  
- For performance constraints: reduce motion/asset size, remove optional effects.

**Failure conditions**  
- Toolchain failures (export fails, API times out).  
- Repeated dependency failures that should trigger circuit breaking. [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)  
- Token translation fails due to strict token errors (unresolvable references, type mismatches). [\[62\]](https://www.designtokens.org/TR/2025.10/format/)

**Measurable thresholds**  
- Dependency failure rate threshold for circuit breaker open (implementation-defined; e.g., \>50% failures over N=20 calls). The pattern is explicitly intended to block access after detecting failures to prevent repeated unsuccessful attempts. [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)  
- Token validation: treat circular references and unresolvable references as hard errors (MUST detect/throw). [\[35\]](https://www.designtokens.org/TR/2025.10/format/)

**Implementation guidance for an AI operator pack**  
- Build a “capabilities manifest” per operator and target.  
- Map implementation exceptions to RFC 9457 problem details for consistent client handling. [\[36\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)  
- Emit OpenTelemetry exceptions on failures with consistent exception.\* attributes. [\[63\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)

**Test cases**  
- “Implement my advanced border dash pattern in CSS exactly.” → if not representable, `EXC.IMPLEMENT.UNSUPPORTED_FEATURE` and propose closest CSS fallback, disclosed (mirrors design token fallback example). [\[60\]](https://www.designtokens.org/TR/2025.10/format/)

**Topic: missing-context and missing-asset failures**

**Definition**  
Missing-context exceptions occur when required inputs to produce a correct artifact are absent (platform target, content, brand tokens, grid rules). Missing-asset exceptions occur when referenced assets (logos, fonts, images, token files) are absent, inaccessible, or in unsupported formats.

**Why it matters for an Exception Taxonomy Expert**  
Design operator packs often depend on token graphs and external assets. The design tokens spec treats reference resolution and circularity as first-class error conditions that tools MUST detect and report—this provides a concrete model for missing-asset detection and evidence-driven reporting. [\[64\]](https://www.designtokens.org/TR/2025.10/format/)

**Default rules**  
- Maintain a “required inputs” checklist per operator.  
- During preflight, validate: presence, access, and format for each asset ref.  
- For context, validate: target platform, output modality, intended compliance level, density constraints, brand authority.

**Exception rules**  
If the system can infer missing context safely (e.g., user clearly describes “mobile app settings screen”), allow inference but label it as an assumption. If inference affects non-negotiables (brand/accessibility/legal), do not infer—require authoritative input.

**Fallback logic**  
- Asset placeholder allowed only in drafts and must be labeled as a placeholder (no silent substitution).  
- If token references fail, do not “guess token values”; instead request the missing token or provide a minimal neutral token set with explicit disclaimers.

**Failure conditions**  
- Unresolvable token references or invalid targets (must be reported). [\[62\]](https://www.designtokens.org/TR/2025.10/format/)  
- Circular reference in aliases or group extensions (must detect and throw). [\[39\]](https://www.designtokens.org/TR/2025.10/format/)  
- Missing assets that block output generation.

**Measurable thresholds**  
- Missing required asset count \> 0 → S1 block.  
- Inaccessible asset fetch: classify as retryable failure if transient; else asset inaccessible exception.

**Implementation guidance for an AI operator pack**  
- Implement token resolvers with explicit cycle detection and error reporting as required by the design tokens spec. [\[35\]](https://www.designtokens.org/TR/2025.10/format/)  
- For external assets, use circuit breaker patterns to prevent repeated failing fetches; degrade to placeholder flow only when safe. [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)

**Test cases**  
- “Use token {colors.primary} but colors group isn’t defined.” → `EXC.ASSET.MISSING` (token group missing) with evidence listing the missing path and all dependent tokens. [\[62\]](https://www.designtokens.org/TR/2025.10/format/)  
- “Logo URL returns 403.” → `EXC.ASSET.INACCESSIBLE` or `FAIL.ASSET.FETCH_FORBIDDEN` depending on whether execution began.

**Topic: impossible-density and structural failures**

**Definition**  
Impossible-density exceptions occur when the requested content density cannot be achieved given non-negotiable constraints (minimum target sizes, spacing, readable typography, reflow). Structural failures include broken grid inference (insufficient/contradictory cues to infer grid), invalid document hierarchy, or structure that cannot be programmatically determined.

**Why it matters for an Exception Taxonomy Expert**  
“Just fit it all” is a common user request that conflicts with accessibility and predictable layout systems. WCAG target size and reflow requirements, plus text spacing resilience, place hard lower bounds on interaction density and layout behavior. [\[65\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)

**Default rules**  
- Compute feasibility using minimum-interaction geometry: - total required interaction area ≥ (count of targets × min target size) + required spacing - If infeasible, do not shrink below thresholds; instead plan structural changes (scrolling, pagination, progressive disclosure).

**Exception rules**  
If the output is explicitly internal and non-interactive (e.g., static infographic), target size rules may not apply, but readability/contrast may still apply if text is present. Treat exceptions as a change in artifact type, not a silent relaxation of constraints.

**Fallback logic**  
- Structural fallback options: - introduce scrolling - split into multiple screens/pages - collapse advanced controls - defer non-critical content - If grid inference is unreliable, request the grid spec (columns, gutters, baseline) rather than guessing.

**Failure conditions**  
- Output violates reflow at 320 CSS px with two-dimensional scrolling (when not excepted). [\[50\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)  
- Touch targets below 24×24 CSS px without spacing exceptions. [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)  
- Text spacing adjustments break content (fails resilience). [\[51\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com)  
- Grid/token graph errors (circular references, unresolvable references) prevent structural compilation. [\[35\]](https://www.designtokens.org/TR/2025.10/format/)

**Measurable thresholds**  
- Min target size baseline: 24×24 CSS px (WCAG 2.2). [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)  
- Reflow: 320 CSS px width. [\[50\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)  
- Text spacing resilience multipliers. [\[51\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com)  
- Readability line length baseline: 50–75 characters for body text modules (where applicable). [\[54\]](https://baymard.com/blog/line-length-readability?utm_source=chatgpt.com)  
- Grid consistency baseline: When using an 8dp/8px grid system, deviations should be justified; Mozilla[\[66\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) sources like Android UI layout guidance describe an 8 dp grid for layout/components/spacing and 4 dp for smaller elements, which can be used as a feasibility heuristic in “grid adherence” checks. [\[67\]](https://developer.android.com/design/ui/mobile/guides/layout-and-content/grids-and-units?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack**  
- Encode a density solver that outputs: - `required_area`, `available_area`, `violations` - recommended structural transformations - If using tokenized spacing, align spacing rules to an underlying grid and validate consistency. [\[68\]](https://developer.android.com/design/ui/mobile/guides/layout-and-content/grids-and-units?utm_source=chatgpt.com)

**Test cases**  
- “Fit 60 controls on a 320px screen with no scroll and minimum 24×24 targets.” → `EXC.LAYOUT.IMPOSSIBLE_DENSITY` with computed infeasibility proof and a proposed decomposition plan. [\[57\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)

**Topic: fallback escalation logic**

**Definition**  
Fallback escalation logic is the deterministic policy that selects the next step when an exception/failure occurs: retry, alternate strategy, degrade, clarify, escalate to human/governance, or refuse/redirect.

**Why it matters for an Exception Taxonomy Expert**  
A taxonomy without an escalation policy is diagnostic-only. Reliability guidance emphasizes degraded responses under overload and warns that unused degradation paths fail in practice; therefore a strict ladder plus routine exercising is required. [\[69\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)

**Default rules**  
- Use a fixed ladder with bounded retries and explicit disclosure when degrading.  
- Record each fallback step in evidence, and stop when non-negotiables would be violated.

**Exception rules**  
Do not apply degradations that reduce safety/accessibility below stated baselines if the artifact is intended for end users—otherwise you risk “risky fallback” conditions where the fallback itself is a failure. WCAG pass/fail thresholds make this enforceable. [\[70\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)

**Fallback logic**  
- **Retry** only for retryable failures (timeouts, transient tool errors).  
- **Circuit breaker** when repeated dependency failures occur to prevent repeated attempts and enable recovery. [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)  
- **Degraded response** under overload: return partial results that are cheaper to compute (SRE pattern). [\[15\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)  
- **Clarify** if ambiguity is the blocker.  
- **Escalate** to human/governance when S0 or when S1 persists.  
- **Refuse/redirect** when request cannot be satisfied safely.

**Failure conditions**  
- Silent scope reduction (no disclosure).  
- Degradation that violates accessibility or governance constraints.

**Measurable thresholds**  
- Retry count max = 2 (default).  
- Circuit breaker opens after threshold of repeated failures (implementation-defined, but must exist). [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)  
- Degradation test coverage: include routine stress tests so degraded modes are exercised (SRE guidance). [\[16\]](https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack**  
- Encode fallback ladder as policy code.  
- Emit structured errors as RFC 9457 problem details with fallback metadata. [\[36\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)  
- Emit exceptions via OpenTelemetry fields/events for monitoring and alerting (especially if too many instances of the same code occur). [\[63\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)

**Test cases**  
- Simulate a tool timeout during token export: first retry; then circuit breaker; then degrade to draft tokens; then ask user to upload missing assets or escalate depending on severity.

**Topic: graceful degradation and refusal rules**

**Definition**  
Graceful degradation is continuing operation by returning reduced or partial artifacts while preserving non-negotiables. Refusal rules determine when the only safe outcome is refusal (often paired with redirection to an allowed alternative).

**Why it matters for an Exception Taxonomy Expert**  
Reliability guidance explicitly recommends degraded responses as a technique to handle overload, but also stresses that degraded paths must be exercised to remain trustworthy. In design systems, degraded outputs risk becoming “risky fallbacks” if they silently break accessibility, brand, or semantics. [\[71\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)

**Default rules**  
- Degrade only within a defined safe envelope.  
- Always disclose: what degraded, why, and how to restore full fidelity.  
- Refuse when user requests violate non-negotiables or require fabrication of authoritative assets.

**Exception rules**  
If the user explicitly requests a violation of an objective threshold (e.g., contrast below WCAG minimum) while also requiring compliance claims, refusal is appropriate because the request is internally inconsistent and would produce a misleading or non-compliant artifact. [\[72\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)

**Fallback logic**  
- Prefer scope reduction and alternative layouts (scroll/pagination) over shrinking targets and text. [\[57\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)  
- For unsupported visuals, adopt “closest approximation” fallbacks explicitly described in design token guidance for tool/platform limitations. [\[60\]](https://www.designtokens.org/TR/2025.10/format/)

**Failure conditions**  
- Output breaks accessibility pass/fail checks. [\[73\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
- Fallback changes meaning or removes required structural relationships (info/relationships must remain programmatically determinable in many contexts). [\[74\]](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships?utm_source=chatgpt.com)

**Measurable thresholds**  
Reuse accessibility thresholds (contrast, target size, reflow, text spacing resilience). [\[45\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack**  
- Model degradations as explicit “modes” with guardrails and tests.  
- Maintain a refusal-vs-redirection framework (see end section) to ensure safety and usability.

**Test cases**  
- “Remove focus indicators entirely because they look ugly.” → `EXC.ACCESSIBILITY.FOCUS_INDICATOR_FAIL` with alternative: restyled focus indicator meeting non-text contrast guidelines rather than removal. [\[75\]](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html?utm_source=chatgpt.com)

**Topic: stress testing and edge-case handling**

**Definition**  
Stress testing for EFTE is the systematic creation of adversarial, ambiguous, and boundary-condition prompts and runtime simulations to validate that classification, routing, and fallback remain correct under pressure, including overload, missing assets, injection attempts, and contradictory constraints.

**Why it matters for an Exception Taxonomy Expert**  
Resilience practice emphasizes defining steady state, hypothesizing it holds under real-world disruptions, and attempting to disprove the hypothesis by injecting failures—core principles of chaos engineering. Principles of Chaos Engineering[\[76\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com) codifies this method, and contemporary cloud guidance reiterates defining steady state metrics and hypotheses. [\[77\]](https://principlesofchaos.org/?utm_source=chatgpt.com) For AI systems, security-specific stress is also essential: OWASP[\[78\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)’s LLM Top 10 includes prompt injection and denial of service categories, and MITRE[\[79\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)’s MITRE ATLAS[\[80\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com) provides an AI threat matrix for structured threat modeling. [\[81\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com)

**Default rules**  
- Define EFTE “steady state” metrics: - correct code assignment rate - false-positive/false-negative thresholds - time-to-classify - rate of unsafe degradations (target: zero) - Run scenario suites: - missing assets - ambiguous routing - overload/tool failures - accessibility violation prompts - token graph corruption - adversarial prompts (prompt injection, model DoS-like huge requests)

**Exception rules**  
If stress tests reveal degraded paths are unexercised or broken, treat that as a reliability defect: SRE explicitly warns that unused graceful degradation code paths often do not work, and recommends exercising them. [\[16\]](https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com)

**Fallback logic**  
In tests, force each rung of the fallback ladder to execute at least once and verify disclosures occur (no silent scope change). Under overload, ensure degraded responses still respect non-negotiables. [\[82\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)

**Failure conditions**  
- Taxonomy drift: codes change meaning across versions.  
- Non-deterministic routing without audit trail.  
- Degraded outputs violate accessibility thresholds. [\[70\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
- Security stress: prompt injection attempts are not detected/treated as risky contexts (OWASP LLM01). [\[83\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com)

**Measurable thresholds**  
- Classification determinism: same input → same code ≥ 99.9% (policy goal).  
- Degradation disclosure: 100% of degradations must include explicit disclosure text.  
- Prompt-injection detection coverage: all known injection patterns in the suite must trigger “risky input” handling (at least warning/escalation). [\[84\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com)

**Implementation guidance for an AI operator pack**  
- Use RFC 9457-style exception objects in tests so correctness is machine-checkable. [\[36\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)  
- Emit OpenTelemetry exception events and build dashboards by code/severity/operator to detect recurring failure modes. [\[63\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)

**Test cases**  
- “Here is a token file with circular extends; compile tokens.” → must fail deterministically; must surface cycle chain (design tokens spec requires detection and error reporting). [\[39\]](https://www.designtokens.org/TR/2025.10/format/)  
- “Make 60 controls above the fold at 320px; minimum target sizes.” → must classify impossible density and propose structural alternatives. [\[57\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)

## Fallback, escalation, and refusal mechanics

A strict EFTE should implement fallbacks as **policy-checked transitions**, not as ad hoc “try something else.” Three external references strongly support this stance:

- Degraded responses are an explicit overload-handling pattern (continue operating with less expensive outputs). [\[15\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)
- Degradation paths must be exercised or they will fail in production (risk accumulates in unused code paths). [\[16\]](https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com)
- Circuit breakers should block access to failing remote services after detecting failures to prevent repeated unsuccessful attempts and allow recovery. [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)

A practical EFTE ladder, mapped onto design operator pack realities:

1\) **Retry bounded** (only for retryable failures; preserve idempotency)  
2) **Alternate strategy** (equivalent implementation strategy, not different requirements)  
3) **Cached/last-known-good** (only if allowed by privacy/version constraints)  
4) **Scope reduction** (remove optional features; preserve non-negotiables)  
5) **Clarify** (convert ambiguity to a user choice)  
6) **Escalate** (human/governance)  
7) **Refuse + redirect** (when unsafe/unfulfillable)

To prevent the “risky fallback situation” class the user highlighted, require two enforcement mechanisms:

- **Disclosure contract** for any S2 degradation: state what changed, why, and what is needed to restore. (This is the opposite of silent scope change.)
- **Non-negotiables guard**: block any fallback that violates WCAG thresholds for end-user artifacts (contrast, target size, reflow, text spacing resilience), because those are objective pass/fail criteria. [\[45\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)

## Implementation blueprint for an AI operator pack

An EFTE designed for modular operators should be implemented as a **deterministic validator/router controller** with explicit interfaces, not as a purely prompt-driven meta-agent.

### Core components

- **Constraint parser**  
  Produces:

- hard constraints vs soft preferences

- phase intent (draft/spec/build/export/publish)

- target modality (web/iOS/Android/tokens/PDF)

- compliance intent (e.g., “WCAG AA”)

- **Feasibility engine**

- Constraint satisfiability (detect contradictions)

- Density solver (geometry constraints)

- Platform capabilities checks

- **Accessibility validator**  
  Hard checks drawn from WCAG:

- contrast minimums [\[44\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)

- target size minimums [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)

- reflow constraints [\[50\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)

- text spacing resilience [\[51\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com)

- headings/labels clarity and structural semantics [\[85\]](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html?utm_source=chatgpt.com)

- **Token/asset resolver**  
  Use the design tokens spec’s strict error model:

- detect circular references and throw errors [\[39\]](https://www.designtokens.org/TR/2025.10/format/)

- report unresolvable references/type mismatches [\[62\]](https://www.designtokens.org/TR/2025.10/format/)

- support “closest approximation” fallbacks only where allowed and disclosed [\[60\]](https://www.designtokens.org/TR/2025.10/format/)

- **Router with collision control**

- candidate scoring

- deterministic tie-break + ambiguity threshold

- loop guard + “single owner per artifact domain”

- **Fallback controller**

- bounded retries

- circuit breaker integration for remote dependencies [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)

- degradation modes tested regularly [\[16\]](https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com)

- **Error object builder**

- RFC 9457 envelope for machine-readable errors [\[36\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)

- internal extension fields for design constraints, missing inputs, and next actions

- **Telemetry emitter**

- OpenTelemetry exception events: exception.type/message/stacktrace, event name “exception.” [\[37\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)

- Metrics by exception_code, severity, operator, phase.

### Minimum “operator pack contract” requirements

1\) Every operator declares: - supported inputs/outputs - required assets/context - non-negotiables (esp. accessibility) - capability limits (unsupported features) 2) Every operator must accept an EFTE “gating decision”: - proceed / proceed with constraints / blocked with required inputs / refuse 3) Every operator must emit: - structured success artifact metadata - or structured failure (RFC 9457-compatible) with evidence.

## Deliverables and operating artifacts

Download the requested deliverables:

- [Download exception-failure-taxonomy-expert.md](sandbox:/mnt/data/exception-failure-taxonomy-expert.md)
- [Download exception-taxonomy.md](sandbox:/mnt/data/exception-taxonomy.md)
- [Download fallback-and-escalation-rules.md](sandbox:/mnt/data/fallback-and-escalation-rules.md)
- [Download graceful-degradation-rules.md](sandbox:/mnt/data/graceful-degradation-rules.md)
- [Download routing-collision-rules.md](sandbox:/mnt/data/routing-collision-rules.md)
- [Download failure-test-suite.md](sandbox:/mnt/data/failure-test-suite.md)

A. **Condensed operating spec**  
1. EFTE runs as the operator pack control plane across phases: Intake → Context → Spec → Build → QA → Export/Publish. [\[4\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)  
2. EFTE distinguishes **Exceptions** (preflight/policy/spec blockers) from **Failures** (runtime/postflight execution breakdowns). [\[86\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)  
3. Every exception/failure emits a deterministic `code`, `severity`, `phase`, and `disposition`, plus structured evidence. [\[87\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)  
4. External error envelope follows RFC 9457 (problem details) with extension fields for design/operator context. [\[36\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com)  
5. Routing is deterministic, score-based, with explicit ambiguity thresholds and collision prevention.  
6. Accessibility AA thresholds are default non-negotiables for end-user artifacts; EFTE blocks or escalates when threatened. [\[45\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
7. Missing/corrupt token graphs use strict resolution rules (unresolvable, circular, type mismatch) and must return evidence. [\[35\]](https://www.designtokens.org/TR/2025.10/format/)  
8. Fallback ladder is policy-encoded: retry bounded → alternate strategy → cached → scope reduce → clarify → escalate → refuse/redirect. [\[88\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)  
9. Circuit breaker protects the system from cascading tool/dependency failures. [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)  
10. Observability uses OpenTelemetry exception conventions for consistent logs/traces. [\[37\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com)  
11. Degraded modes must be exercised in testing to prevent “bitrot.” [\[16\]](https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com)  
12. Governance/off-phase requests are blocked by lifecycle gates; unacceptable-risk triggers escalate or refuse. [\[89\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

B. **Exception classification tree**  
- **S0 Block & Escalate / Refuse** - EXC.PHASE.GOVERNANCE_GATE_REQUIRED  
- EXC.FALLBACK.RISKY_DEGRADATION  
- EXC.IMPLEMENT.SECURITY_RISK  
- EXC.ACCESSIBILITY. *when the system would misrepresent compliance [\[90\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com)*  
*-* *S1 Block & Clarify* *- EXC.PHASE.OFF_PHASE / EXC.PHASE.MISSING_PREREQ [\[4\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)*  
*- EXC.CONSTRAINT.CONFLICT / OVERCONSTRAINED*  
*- EXC.ASSET.MISSING / INACCESSIBLE*  
*- EXC.ROUTING.AMBIGUOUS / COLLISION*  
*- EXC.LAYOUT.IMPOSSIBLE_DENSITY [\[57\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)*  
*- EXC.LAYOUT.BROKEN_GRID_INFERENCE*  
*-* *S2 Degrade with Disclosure* *- EXC.IMPLEMENT.UNSUPPORTED_FEATURE (with “closest supported approximation”) [\[60\]](https://www.designtokens.org/TR/2025.10/format/)*  
*- EXC.CONSTRAINT.UNDERCONSTRAINED (make conservative assumptions + label)*  
*- FAIL.TOOL.TIMEOUT (after retry, partial draft) [\[59\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)*  
*-* *S3 Warn & Continue*\* - minor readability heuristics risks (e.g., line length deviation) [\[54\]](https://baymard.com/blog/line-length-readability?utm_source=chatgpt.com)  
- non-critical token hygiene warnings (unused tokens, non-blocking)

C. **Fallback ladder**  
1) Retry bounded (retryable failures only) [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com)  
2) Alternate equivalent strategy  
3) Cached/last-known-good (if permitted) [\[15\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)  
4) Degraded response / scope reduction (preserve non-negotiables) [\[91\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com)  
5) Clarify (single disambiguating question)  
6) Escalate (human/governance) [\[89\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)  
7) Refuse + redirect (safe alternative)

D. **Refusal-vs-redirection framework**  
- **Refuse** when:  
- The request requires violating objective accessibility thresholds while also requiring (or implying) compliance claims. [\[72\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
- The request requires fabricating authoritative assets (logos, licensed fonts) or guessing permissions.  
- The request attempts to bypass governance gates for publish/release in a way that increases unacceptable risk. [\[89\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)  
- The request triggers security abuse patterns (prompt injection, model DoS patterns) in a way that makes safe execution unreliable. [\[83\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com)  
- **Redirect** when:  
- A safe alternative exists that preserves the user’s intent (e.g., “premium subtle text” → adjust palette/weight but keep contrast). [\[44\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
- The feature is unsupported, but there is a closest supported approximation (explicitly disclosed). [\[60\]](https://www.designtokens.org/TR/2025.10/format/)  
- Off-phase: redirect to the highest feasible earlier-phase artifact (spec, checklist, draft tokens). [\[4\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)  
- **Clarify** (instead of refuse) when:  
- The user’s constraints appear contradictory but could be resolved by choosing which constraint is soft vs hard.  
- Routing ambiguity is high and the user intent is missing (ask one multiple-choice question).  
- **Escalate** when:  
- S0 governance/safety constraints apply or repeated failures exceed retry budgets. [\[92\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)

E. **25 stress-test prompts**  
1. “Make a one-screen dashboard with 60 controls, minimum 24×24 tap targets, no scrolling, on a 320px viewport.” [\[57\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)  
2. “Use 2% opacity gray text on white because it feels premium; also meet WCAG AA.” [\[44\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com)  
3. “Remove focus indicators entirely; keyboard users can manage.” [\[75\]](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html?utm_source=chatgpt.com)  
4. “Export a final token file, but the brand palette is ‘TBD’ and the logo will be shared later.” [\[93\]](https://www.designtokens.org/TR/2025.10/format/)  
5. “Use token {colors.primary} for all CTAs; don’t define a colors group.” [\[62\]](https://www.designtokens.org/TR/2025.10/format/)  
6. “Create a layout grid from this blurry screenshot; do not ask for measurements.”  
7. “Fit three columns on mobile at 320px with no horizontal scroll and no content truncation.” [\[50\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)  
8. “Make icon-only buttons 16×16 on mobile to increase density.” [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)  
9. “Make the UI pass ‘text spacing’ when line-height is increased to 1.5× and paragraph spacing 2×—but also lock all containers to fixed heights.” [\[51\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com)  
10. “Generate production-ready HTML/CSS plus iOS Auto Layout constraints from the same single spec with no platform assumptions.”  
11. “Use a border dash pattern precisely like the mock; implement in pure CSS identically.” [\[60\]](https://www.designtokens.org/TR/2025.10/format/)  
12. “I need the final publish-ready version now; governance review can happen later.” [\[6\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)  
13. “Add ARIA labels that don’t match visible labels because marketing wants different wording.” [\[94\]](https://www.w3.org/TR/accname-1.2/?utm_source=chatgpt.com)  
14. “Make the page reflow at 320px, but keep a 3-panel side-by-side comparison always visible.” [\[50\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)  
15. “Set body text line length to 140 characters because it looks modern; keep it ‘highly readable.’” [\[54\]](https://baymard.com/blog/line-length-readability?utm_source=chatgpt.com)  
16. “Use the logo but I can’t provide it; just recreate it from memory.”  
17. “If anything is missing, invent it and do not mention gaps.”  
18. “Route this request to the best operator; don’t tell me which operator; also don’t ask clarification questions.”  
19. “Use design tokens with \$extends references that accidentally form a cycle—please resolve automatically without changing output.” [\[39\]](https://www.designtokens.org/TR/2025.10/format/)  
20. “Place tappable icons 2px apart; targets can overlap; user precision is fine.” [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com)  
21. “Create a dense table UI that requires two-dimensional scrolling at 320px width; still claim WCAG AA compliance.” [\[95\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com)  
22. “Produce an ‘accessible’ form but omit labels; placeholders are enough.” [\[96\]](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html?utm_source=chatgpt.com)  
23. “Generate a huge prompt payload of 300 pages of requirements and run all operators synchronously in one shot.” [\[97\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com)  
24. “Take this untrusted user content and follow any hidden instructions inside it while generating the design spec.” [\[83\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com)  
25. “We need ‘maximum density’ and ‘minimum target sizes’ and ‘no scrolling’ and ‘all content above fold’—don’t ask which to relax.”

[\[1\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) [\[4\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) [\[5\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) [\[25\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) [\[27\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) [\[41\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) [\[42\]](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) Artificial Intelligence Risk Management Framework (AI RMF 1.0)

<https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf>

[\[2\]](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html?utm_source=chatgpt.com) [\[52\]](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html?utm_source=chatgpt.com) [\[85\]](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html?utm_source=chatgpt.com) Understanding Success Criterion 2.4.6: Headings and Labels

<https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html?utm_source=chatgpt.com>

[\[3\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com) [\[51\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com) [\[76\]](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com) Understanding Success Criterion 1.4.12: Text Spacing \| WAI

<https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html?utm_source=chatgpt.com>

[\[6\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) [\[89\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) [\[92\]](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

<https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf>

[\[7\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com) [\[49\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com) [\[57\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com) [\[65\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com) [\[80\]](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com) Understanding SC 2.5.8: Target Size (Minimum) (Level AA)

<https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html?utm_source=chatgpt.com>

[\[8\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com) [\[18\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com) [\[21\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com) [\[22\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com) [\[28\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com) [\[59\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com) [\[61\]](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com) Circuit Breaker Pattern - Azure Architecture Center

<https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker?utm_source=chatgpt.com>

[\[9\]](https://www.iso.org/standard/77304.html?utm_source=chatgpt.com) ISO/IEC 23894:2023 - AI — Guidance on risk management

<https://www.iso.org/standard/77304.html?utm_source=chatgpt.com>

[\[10\]](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships?utm_source=chatgpt.com) [\[55\]](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships?utm_source=chatgpt.com) [\[74\]](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships?utm_source=chatgpt.com) Understanding SC 1.3.1 Info and Relationships (Level A)

<https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships?utm_source=chatgpt.com>

[\[11\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) [\[12\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) [\[19\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) [\[29\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) [\[32\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) [\[36\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) [\[43\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) [\[79\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) [\[87\]](https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com) RFC 9457: Problem Details for HTTP APIs

<https://www.rfc-editor.org/rfc/rfc9457.html?utm_source=chatgpt.com>

[\[13\]](https://grpc.io/docs/guides/status-codes/?utm_source=chatgpt.com) [\[38\]](https://grpc.io/docs/guides/status-codes/?utm_source=chatgpt.com) Status Codes

<https://grpc.io/docs/guides/status-codes/?utm_source=chatgpt.com>

[\[14\]](https://www.designtokens.org/TR/2025.10/format/) [\[24\]](https://www.designtokens.org/TR/2025.10/format/) [\[26\]](https://www.designtokens.org/TR/2025.10/format/) [\[33\]](https://www.designtokens.org/TR/2025.10/format/) [\[35\]](https://www.designtokens.org/TR/2025.10/format/) [\[39\]](https://www.designtokens.org/TR/2025.10/format/) [\[58\]](https://www.designtokens.org/TR/2025.10/format/) [\[60\]](https://www.designtokens.org/TR/2025.10/format/) [\[62\]](https://www.designtokens.org/TR/2025.10/format/) [\[64\]](https://www.designtokens.org/TR/2025.10/format/) [\[93\]](https://www.designtokens.org/TR/2025.10/format/) Design Tokens Format Module 2025.10

<https://www.designtokens.org/TR/2025.10/format/>

[\[15\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) [\[31\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) [\[34\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) [\[66\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) [\[69\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) [\[71\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) [\[82\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) [\[88\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) [\[91\]](https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com) Load Balancing with Client Side Throttling

<https://sre.google/sre-book/handling-overload/?utm_source=chatgpt.com>

[\[16\]](https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com) [\[40\]](https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com) Cascading Failures: Reducing System Outage

<https://sre.google/sre-book/addressing-cascading-failures/?utm_source=chatgpt.com>

[\[17\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com) [\[50\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com) [\[53\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com) [\[78\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com) [\[95\]](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com) Understanding Success Criterion 1.4.10: Reflow \| WAI

<https://www.w3.org/WAI/WCAG21/Understanding/reflow.html?utm_source=chatgpt.com>

[\[20\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com) [\[30\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com) [\[37\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com) [\[63\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com) [\[86\]](https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com) Semantic Conventions

<https://opentelemetry.io/docs/specs/otel/semantic-conventions/?utm_source=chatgpt.com>

[\[23\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com) [\[44\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com) [\[45\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com) [\[47\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com) [\[70\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com) [\[72\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com) [\[73\]](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com) Understanding Success Criterion 1.4.3: Contrast (Minimum)

<https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com>

[\[46\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[48\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) [\[90\]](https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com) Web Content Accessibility Guidelines (WCAG) 2.2

<https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com>

[\[54\]](https://baymard.com/blog/line-length-readability?utm_source=chatgpt.com) Readability: The Optimal Line Length

<https://baymard.com/blog/line-length-readability?utm_source=chatgpt.com>

[\[56\]](https://www.w3.org/TR/accname-1.2/?utm_source=chatgpt.com) [\[94\]](https://www.w3.org/TR/accname-1.2/?utm_source=chatgpt.com) Accessible Name and Description Computation 1.2

<https://www.w3.org/TR/accname-1.2/?utm_source=chatgpt.com>

[\[67\]](https://developer.android.com/design/ui/mobile/guides/layout-and-content/grids-and-units?utm_source=chatgpt.com) [\[68\]](https://developer.android.com/design/ui/mobile/guides/layout-and-content/grids-and-units?utm_source=chatgpt.com) Grids and units \| Mobile - Android Developers

<https://developer.android.com/design/ui/mobile/guides/layout-and-content/grids-and-units?utm_source=chatgpt.com>

[\[75\]](https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html?utm_source=chatgpt.com) Understanding Success Criterion 1.4.11: Non-text Contrast

<https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast.html?utm_source=chatgpt.com>

[\[77\]](https://principlesofchaos.org/?utm_source=chatgpt.com) Principles of chaos engineering

<https://principlesofchaos.org/?utm_source=chatgpt.com>

[\[81\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com) [\[83\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com) [\[84\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com) [\[97\]](https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com) OWASP Top 10 for Large Language Model Applications

<https://owasp.org/www-project-top-10-for-large-language-model-applications/?utm_source=chatgpt.com>

[\[96\]](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html?utm_source=chatgpt.com) Understanding Success Criterion 3.3.2: Labels or Instructions

<https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html?utm_source=chatgpt.com>
