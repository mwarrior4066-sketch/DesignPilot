<!-- Optimized from original source file: Accessibility and Feedback Expert Research.docx. All textual content preserved in markdown form for size-efficient packaging. -->

# Technical Standards and Operational Logic for Modular AI Accessibility Systems

The transition toward autonomous design systems necessitates a deterministic framework for digital accessibility that transcends traditional human-led audits. In the context of a modular AI design operator pack, accessibility must be integrated into the generative logic as a first-order constraint rather than a post-production remediation task.<sup>1</sup> This report establishes the rigorous technical parameters required to build an expert agent capable of making production-level decisions across interaction states, feedback mechanisms, and structural architectures. By prioritizing the Web Content Accessibility Guidelines (WCAG) 2.2 and the WAI-ARIA Authoring Practices Guide (APG), this framework ensures that AI-generated interfaces are perceivable, operable, understandable, and robust for the widest possible spectrum of users.<sup>3</sup>

## 1. Interaction State Systems

### Definition

Interaction states represent the dynamic properties of a user interface component as it moves through its lifecycle in response to user engagement or automated system processes.<sup>6</sup> These states include default (the resting appearance), hover (pointer presence), focus (keyboard or switch navigation targeting), active (the moment of activation), selected (binary toggle or selection state), disabled (unavailability), loading (asynchronous processing), error (validation failure), success (confirmation), and warning (precautionary feedback).<sup>6</sup>

### Why it Matters for an Accessibility and Feedback Expert

An AI operator must understand that states are the primary channel for feedback. Without a distinguishable focus state, keyboard users cannot navigate; without an error state, cognitive load increases as users struggle to identify why a task has stalled.<sup>6</sup> For an AI expert, these states are not merely "styles" but functional requirements that must be validated against contrast and programmatic standards to ensure compatibility with the accessibility tree.<sup>6</sup>

### Default Rules

All interactive components must have a minimum of five states: default, hover, focus, active, and disabled.<sup>6</sup> Focus indicators must be visible and meet WCAG 2.2 SC 2.4.13 (Focus Appearance) standards, requiring an area at least as large as a 2px thick perimeter of the component and a 3:1 contrast ratio between focused and unfocused states.<sup>11</sup> Hover states must provide a visual change but cannot be the only way to reveal critical information (SC 3.2.7).<sup>12</sup> Disabled states should be visually de-emphasized but must be evaluated against the "read-only" pattern to ensure critical information is not hidden from screen readers.<sup>13</sup>

### Exception Rules

Interaction states that are controlled entirely by the user agent (browser), such as certain native select elements or file inputs that cannot be styled, are exempt from custom focus and hover contrast requirements.<sup>6</sup> Furthermore, decorative elements that do not receive focus or perform actions do not require focus or active states.<sup>14</sup>

### Fallback Logic

If a custom focus indicator fails to meet the 3:1 contrast ratio against a dynamic background, the AI operator must fallback to a two-color focus ring (e.g., a white outline with a black box-shadow). This ensures visibility across any background color, as a 9:1 contrast between the two indicator colors guarantees that at least one color meets the 3:1 requirement against any solid background.<sup>11</sup>

### Failure Conditions

A critical failure occurs when a focus indicator is removed via CSS (outline: none) without being replaced by a compliant alternative (Failure F78).<sup>11</sup> Another failure involves using color as the sole indicator of the active or selected state, which violates SC 1.4.1.<sup>10</sup>

### Measurable Thresholds

Contrast ratios for text must be at least 4.5:1 for normal text and 3:1 for large text.<sup>12</sup> Non-text contrast for focus indicators and UI components must be at least 3:1.<sup>12</sup> For focus appearance, the indicator area \$A\$ for a rectangular component of width \$w\$ and height \$h\$ must be \$A \geq 4h + 4w\$ CSS pixels.<sup>11</sup>

### Implementation Guidance for an AI Operator Pack

The AI should generate states using CSS pseudo-classes (:hover, :focus-visible, :active) to ensure native browser logic is preserved. It must inject ARIA attributes such as aria-selected, aria-checked, or aria-disabled and update them dynamically via JavaScript as state transitions occur.<sup>15</sup>

### Test Cases

1.  Verify that the focus ring appears immediately upon Tab navigation and meets the 3:1 change-of-contrast ratio.<sup>11</sup>

2.  Confirm that aria-disabled="true" is applied to disabled buttons and that they are removed from the tab sequence if the functionality is entirely unavailable.<sup>13</sup>

| **State** | **Role/Attribute** | **Visual Threshold**           | **Programmatic Requirement**     |
|-----------|--------------------|--------------------------------|----------------------------------|
| Focus     | outline            | 3:1 contrast vs background     | Visible upon keyboard navigation |
| Selected  | aria-selected      | Distinct shape or color + icon | Toggle state announced by AT     |
| Disabled  | aria-disabled      | 2.5:1 contrast (exempt)        | Removed from Tab order           |
| Loading   | aria-busy          | Animation \< 3Hz               | Continuous status update         |
| Error     | aria-invalid       | 4.5:1 contrast + error icon    | Linked via aria-describedby      |

## 2. Focus Visibility and Keyboard Behavior

### Definition

Focus visibility is the requirement that the interactive element currently receiving keyboard input is visually identifiable.<sup>12</sup> Keyboard behavior refers to the ability to operate all interface functionality—including navigation, selection, and activation—using only a keyboard interface.<sup>5</sup>

### Why it Matters for an Accessibility and Feedback Expert

For users with motor impairments, repetitive stress injuries, or blindness, the keyboard is the primary or only interface to the digital world.<sup>5</sup> An AI expert must ensure that focus is never "trapped" and that the navigation order is logical, matching the visual layout to maintain the user's mental model.<sup>7</sup>

### Default Rules

The tab order must be sequential and logical, typically moving from top to bottom, left to right (SC 2.4.3).<sup>7</sup> All interactive elements must be focusable. Modals must trap focus within their boundaries and return focus to the trigger element upon dismissal.<sup>19</sup> Focus indicators must not be obscured by "sticky" headers or footers (SC 2.4.11).<sup>20</sup>

### Exception Rules

Non-interactive content, such as static text or decorative images, must be excluded from the tab order to prevent unnecessary navigation steps.<sup>14</sup> In dense interfaces, grouped controls (e.g., a toolbar) may use a single tab stop with arrow-key navigation between items (the "Roving Tabindex" pattern) to reduce the number of Tab presses required.<sup>11</sup>

### Fallback Logic

When an element that previously held focus is removed from the DOM (e.g., a deleted list item), the AI should move focus to the nearest logical sibling or the parent container to prevent focus from resetting to the top of the document.<sup>7</sup>

### Failure Conditions

A keyboard trap—where a user can enter a component (like a calendar picker) but cannot exit using only the keyboard—is a catastrophic failure (SC 2.1.2).<sup>3</sup> Removing focus indicators entirely is also a failure (SC 2.4.7).<sup>12</sup>

### Measurable Thresholds

Focus indicators must be at least as large as a 1px thick perimeter of the component (Level AA) or a 2px thick perimeter (Level AAA).<sup>12</sup> Contrast must meet a 3:1 ratio against adjacent colors.<sup>8</sup>

### Implementation Guidance for an AI Operator Pack

The AI operator should utilize scroll-padding-top and scroll-padding-bottom in CSS to ensure that when a user tabs to an element, it is not hidden under sticky UI layers.<sup>18</sup> It must generate code for the Esc key to dismiss all temporary overlays, such as menus and dialogs.<sup>7</sup>

### Test Cases

1.  Use the Tab key to navigate the entire page; verify that no focus "disappears" and that it never becomes trapped.<sup>19</sup>

2.  Verify that a "Skip to Main Content" link is the first focusable element and successfully moves focus to the \<main\> landmark.<sup>19</sup>

## 3. Hover and Focus Content Behavior

### Definition

Hover and focus content behavior refers to additional information—such as tooltips, popovers, or submenus—revealed when a user hovers a pointer or moves keyboard focus onto an element.<sup>25</sup>

### Why it Matters for an Accessibility and Feedback Expert

If this content disappears unexpectedly or obscures other critical information, users with low vision (who may use screen magnifiers) or motor impairments may be unable to read the revealed text or interact with the interface.<sup>25</sup> An AI expert must enforce "Content on Hover or Focus" (SC 1.4.13) to ensure this content is controllable.<sup>25</sup>

### Default Rules

Content revealed via hover or focus must meet three criteria:

1.  **Dismissible**: The user can dismiss the content without moving focus or pointer (e.g., via Esc).<sup>25</sup>

2.  **Hoverable**: The pointer can move over the revealed content without it disappearing.<sup>25</sup>

3.  **Persistent**: The content remains visible until the trigger is removed, the user dismisses it, or the info is no longer valid.<sup>25</sup>

### Exception Rules

These rules do not apply if the revealed content does not obscure other author-created content, or if the content is essential (such as a system-level tooltip that the author cannot control).<sup>25</sup>

### Fallback Logic

If a tooltip cannot be made "hoverable" due to technical constraints, the information it contains should be moved into a persistent text label or a toggleable disclosure widget.<sup>15</sup>

### Failure Conditions

A tooltip that disappears after a 5-second timeout while a user is still hovering it is a failure.<sup>25</sup> A popover that cannot be closed using the keyboard is a failure.<sup>15</sup>

### Measurable Thresholds

No specific pixel threshold exists for hover/focus content, but it must remain persistent for as long as the hover or focus trigger is active.<sup>25</sup>

### Implementation Guidance for an AI Operator Pack

The AI should use aria-describedby to associate the revealed content with the trigger element.<sup>27</sup> It should ensure that the revealed content is positioned adjacent to the trigger in the DOM or uses aria-owns if it must be rendered elsewhere.<sup>28</sup>

### Test Cases

1.  Hover over a tooltip; move the mouse into the tooltip area. Verify it stays visible.<sup>25</sup>

2.  Focus on an element that triggers a popover; press Esc. Verify the popover disappears while focus remains on the trigger.<sup>25</sup>

## 4. Touch Target Sizing and Spacing

### Definition

Touch target sizing refers to the physical area of a screen that responds to user input (taps or clicks).<sup>29</sup> Spacing is the non-interactive gap between these targets to prevent accidental activation of adjacent controls.<sup>31</sup>

### Why it Matters for an Accessibility and Feedback Expert

Users with tremors, motor impairments, or large fingers rely on sufficiently large targets to interact with mobile and touch-screen devices.<sup>21</sup> An AI expert must decide between minimum compliance (24px) and industry best practices (44-48px) based on the target audience and device context.<sup>21</sup>

### Default Rules

WCAG 2.2 SC 2.5.8 (Level AA) requires a minimum target size of 24x24 CSS pixels.<sup>12</sup> However, targets that are smaller than 24px can pass if the target plus its spacing (the "effective target") equals a 24px diameter circle that does not overlap with any other target.<sup>12</sup> Material Design 3 recommends 48x48dp, and iOS/Spectrum recommend 44x44px.<sup>21</sup>

### Exception Rules

Targets are exempt from size requirements if they are:

1.  **Inline**: Contained within a sentence or block of text.<sup>12</sup>

2.  **Essential**: Where the size is legally required or informationally essential (e.g., map pins).<sup>12</sup>

3.  **Alternative**: If another control on the same page performs the same function and meets the size requirement.<sup>31</sup>

### Fallback Logic

If a layout is too dense to support 44px targets, the AI must ensure at least 8px of spacing between controls to minimize accidental activation.<sup>29</sup>

### Failure Conditions

Small icons (e.g., 16px) placed immediately adjacent to each other without padding violate SC 2.5.8.<sup>20</sup>

### Measurable Thresholds

- **WCAG 2.2 AA**: 24x24 CSS pixels.<sup>31</sup>

- **WCAG 2.2 AAA / iOS**: 44x44 CSS pixels.<sup>12</sup>

- **Material 3**: 48x48 dp.<sup>29</sup>

### Implementation Guidance for an AI Operator Pack

The AI should use CSS padding or min-width/min-height to expand the interactive area of small icons without changing their visual size. For mobile-first interfaces, it should default to the 44px standard.<sup>29</sup>

### Test Cases

1.  Use an "Accessibility Target" tool (like the 24x24 pixel cursor) to verify that no interactive targets are too small or too close together.<sup>31</sup>

2.  Check that checkboxes and radio buttons have a clickable label that expands the target area.<sup>10</sup>

| **System/Standard** | **Target Size** | **Recommended Spacing** |
|---------------------|-----------------|-------------------------|
| WCAG 2.2 AA         | 24x24 px        | N/A (Total area rule)   |
| Adobe Spectrum      | 44x44 px        | Increases for mobile    |
| Material Design 3   | 48x48 dp        | 8dp between targets     |
| WCAG 2.5.5 (AAA)    | 44x44 px        | N/A                     |

## 5. Reduced Motion and Animation Safety

### Definition

Reduced motion is a user preference, set at the operating system level, that indicates a desire to minimize non-essential animations and transitions.<sup>34</sup> Animation safety involves preventing motion that could cause physical discomfort or seizures.<sup>35</sup>

### Why it Matters for an Accessibility and Feedback Expert

For users with vestibular disorders, certain types of motion (like parallax scrolling or rapid zooming) can cause nausea, dizziness, or migraines that require bed rest to recover.<sup>35</sup> An AI expert must respect the prefers-reduced-motion media query to ensure the interface is comfortable for all users.<sup>34</sup>

### Default Rules

If a user has enabled reduced motion, all non-essential animations (e.g., decorative parallax, scaling effects, background videos) must be disabled or replaced with static alternatives.<sup>34</sup> Essential animations—those that convey state or status—should be slowed down or replaced with non-moving indicators (e.g., a pulsing dot replaced by a static "Recording" label).<sup>37</sup>

### Exception Rules

Animations that are essential to the functionality or the information being conveyed (e.g., a tutorial demonstrating a gesture) are exempt, though they should still be designed to be as non-intrusive as possible.<sup>37</sup>

### Fallback Logic

The AI operator should provide a global "Pause/Stop" button for any animation that plays for more than five seconds, regardless of the user's OS-level preferences.<sup>30</sup>

### Failure Conditions

A parallax effect that continues to move when the user scrolls, even after prefers-reduced-motion: reduce is detected, is a failure.<sup>35</sup> High-contrast movements that trigger seizures are a critical safety failure.<sup>35</sup>

### Measurable Thresholds

Animations that last longer than 5 seconds must have a mechanism to pause, stop, or hide.<sup>30</sup>

### Implementation Guidance for an AI Operator Pack

The AI should wrap all animation code in the @media (prefers-reduced-motion: reduce) block. In JavaScript, it must use window.matchMedia to check this preference before executing motion-heavy scripts.<sup>34</sup>

### Test Cases

1.  Enable "Reduce Motion" in the OS settings; verify that all page transitions and decorative animations are disabled or instantaneous.<sup>34</sup>

2.  Ensure that autoplaying videos or carousels stop moving within five seconds or provide a clear "Pause" button.<sup>30</sup>

## 6. Flash Thresholds and Seizure Risk

### Definition

Flash thresholds are the physical limits of flickering light and color transitions beyond which photosensitive seizures can be triggered.<sup>40</sup> Seizure risk is primarily associated with content that flashes more than three times per second.<sup>40</sup>

### Why it Matters for an Accessibility and Feedback Expert

This is a life-safety requirement. Content that violates these thresholds can cause immediate medical harm to individuals with photosensitive epilepsy.<sup>40</sup> An AI expert must ensure that no generated content, including loading indicators or video playback, exceeds these thresholds.<sup>40</sup>

### Default Rules

WCAG 2.3.1 (Level A) states that web pages must not contain anything that flashes more than three times in any one-second period.<sup>40</sup> If flashing is necessary, it must be below the "general flash" and "red flash" thresholds.<sup>40</sup>

### Exception Rules

Small, low-contrast flashes that occupy less than 0.006 steradians (approximately 25% of any 10-degree visual field on the screen) are generally safe.<sup>40</sup>

### Fallback Logic

The AI should prioritize "fade" transitions over "blink" or "strobe" transitions. If an animation must blink, it should be limited to 2Hz to provide a safe buffer.<sup>40</sup>

### Failure Conditions

Any content that flashes five times in a single second is a catastrophic failure.<sup>40</sup> Saturated red flashing is a higher-risk failure.<sup>40</sup>

### Measurable Thresholds

- **General Flash**: A pair of opposing changes in relative luminance of 10% or more, where the relative luminance of the darker image is below 0.80.<sup>42</sup>

- **Red Flash**: A transition to or from a saturated red (\$R / (R+G+B) \geq 0.8\$).<sup>43</sup>

- **Area**: For a 1024x768 screen, the threshold area is 341x256 CSS pixels.<sup>42</sup>

### Implementation Guidance for an AI Operator Pack

The AI should avoid using high-frequency pulsing CSS animations. For video content, it should use tools like the Photosensitive Epilepsy Analysis Tool (PEAT) to validate content before deployment.<sup>42</sup>

### Test Cases

1.  Analyze all "Loading" or "Success" animations to ensure they blink no more than twice per second.<sup>40</sup>

2.  Verify that any video content containing strobe effects is edited to reduce the flash rate below 3Hz.<sup>40</sup>

## 7. Feedback Systems for Forms and Actions

### Definition

Feedback systems are the methods by which an application communicates the status of a user's interaction, particularly regarding form validation, success notifications, and real-time status updates.<sup>19</sup>

### Why it Matters for an Accessibility and Feedback Expert

Screen reader users and users with cognitive disabilities rely on clear, immediate, and programmatic feedback to understand the results of their actions.<sup>14</sup> An AI expert must ensure that feedback is not just visual (e.g., a green checkmark) but also communicated to assistive technology via ARIA live regions.<sup>46</sup>

### Default Rules

1.  **Multi-cue**: Feedback must use more than just color (e.g., color + icon + text).<sup>10</sup>

2.  **Programmatic**: Dynamic status updates must use aria-live or roles like status or alert.<sup>46</sup>

3.  **Association**: Error messages must be linked to their respective inputs using aria-describedby.<sup>19</sup>

### Exception Rules

If an action results in a full page reload or a major navigation change, a live region is not necessary, as the new page title and content structure will inform the user of the update.<sup>46</sup>

### Fallback Logic

If a browser does not support certain live region roles, the AI should use a generic aria-live="polite" container that is present in the DOM on page load.<sup>46</sup>

### Failure Conditions

A form that displays a list of errors at the top but does not move focus to them—or does not announce them—is a failure (SC 3.3.1).<sup>22</sup> A "Saved" message that appears and disappears without a screen reader announcement is a failure.<sup>16</sup>

### Measurable Thresholds

All critical errors must be announced immediately (aria-live="assertive" or role="alert").<sup>46</sup> Non-critical status messages must be announced politely (aria-live="polite" or role="status").<sup>47</sup>

### Implementation Guidance for an AI Operator Pack

The AI should implement an "error summary" pattern for complex forms. It should ensure that the aria-invalid="true" attribute is applied to fields with errors and that error text has a 4.5:1 contrast ratio.<sup>19</sup>

### Test Cases

1.  Submit a form with errors; verify that the screen reader announces the number of errors and that the user can navigate directly to the first error.<sup>22</sup>

2.  Trigger a "Success" notification; verify it is announced without the user having to move focus to the message.<sup>46</sup>

## 8. Progressive Disclosure and Cognitive Load

### Definition

Progressive disclosure is the technique of showing only the most relevant information at any given time to avoid overwhelming the user.<sup>5</sup> Cognitive load reduction involves minimizing the mental effort required to navigate and complete tasks.<sup>5</sup>

### Why it Matters for an Accessibility and Feedback Expert

Users with learning disabilities, ADHD, or memory impairments benefit from simple language, consistent layouts, and the reduction of repetitive data entry.<sup>5</sup> An AI expert must follow WCAG 2.2 standards for Redundant Entry and Accessible Authentication to support these users.<sup>20</sup>

### Default Rules

1.  **Redundant Entry (SC 3.3.7)**: Do not ask for the same information twice in the same process; auto-populate or provide a selection mechanism for previously entered data.<sup>20</sup>

2.  **Accessible Authentication (SC 3.3.8/3.3.9)**: Do not require "cognitive function tests" (puzzles, memorization) for login without providing an alternative like magic links, biometrics, or password manager support.<sup>51</sup>

3.  **Consistency**: Use standard icons, predictable navigation, and a clear hierarchy.<sup>10</sup>

### Exception Rules

Redundant entry is allowed if the information is essential (e.g., verifying a new password), required for security, or if the previous info is no longer valid.<sup>21</sup> Cognitive tests are allowed in Level AA (SC 3.3.8) if they involve object recognition or personal content, but these exceptions are removed in Level AAA (SC 3.3.9).<sup>52</sup>

### Fallback Logic

The AI should always provide a "Help" or "FAQ" link in a consistent location (SC 3.2.6) to assist users who become confused during a multi-step process.<sup>20</sup>

### Failure Conditions

A checkout process that requires a user to re-type their shipping address for the billing section violates SC 3.3.7.<sup>20</sup> A CAPTCHA that requires identifying fire hydrants without an audio alternative violates SC 3.3.8.<sup>20</sup>

### Measurable Thresholds

Reading level for complex content should ideally be at a high school grade level (Gunning Fog or Flesch-Kincaid).<sup>57</sup>

### Implementation Guidance for an AI Operator Pack

The AI should prioritize "Passkeys" and WebAuthn for authentication. It must ensure that copy-paste is never disabled on sensitive inputs like passwords or OTP fields to allow the use of password managers.<sup>51</sup>

### Test Cases

1.  Complete a multi-step form; verify that information from Step 1 is correctly suggested or filled in Step 3.<sup>20</sup>

2.  Test the login flow; verify that a user can authenticate without being forced to solve a visual puzzle or recall a specific security image.<sup>51</sup>

## 9. UI Accessibility vs. Document/PDF Accessibility

### Definition

UI Accessibility focuses on the dynamic, interactive experience of a web application.<sup>59</sup> Document (PDF) Accessibility focuses on the static structural integrity of a file, governed by the PDF/UA standard (ISO 14289).<sup>59</sup>

### Why it Matters for an Accessibility and Feedback Expert

An AI expert must differentiate between these formats because a compliant UI does not guarantee a compliant PDF.<sup>60</sup> PDFs require a specific "Tag Tree" that defines the reading order, whereas UI accessibility relies on the DOM and ARIA.<sup>60</sup>

### Default Rules

- **UI**: Use semantic HTML5 elements and ARIA. Focus on interactivity, keyboard management, and live regions.<sup>59</sup>

- **PDF**: Use PDF/UA standards. Every element must be tagged (Heading, Paragraph, Table, Figure). Decorative items must be marked as "Artifacts".<sup>60</sup>

### Exception Rules

A PDF that meets PDF/UA standards is generally considered to satisfy WCAG requirements for documents, but the inverse is not necessarily true.<sup>59</sup>

### Fallback Logic

If a complex layout cannot be made fully accessible in PDF format, the AI should provide an equivalent HTML version of the content.<sup>22</sup>

### Failure Conditions

A PDF with "flattened" text (an image of text) without an OCR layer is a total accessibility failure.<sup>61</sup> A PDF where the reading order does not follow the visual multi-column layout is a failure.<sup>61</sup>

### Measurable Thresholds

PDFs must pass the "PAC" (PDF Accessibility Checker) validation for ISO 14289-1 compliance.<sup>61</sup>

### Implementation Guidance for an AI Operator Pack

The AI operator must use distinct libraries for PDF generation. It must ensure that "role mapping" is used to map custom tags to standard PDF tags and that all images have embedded Alt text within the PDF metadata.<sup>60</sup>

### Test Cases

1.  Open a generated PDF in an accessibility checker; verify that no "Untagged Content" errors exist.<sup>61</sup>

2.  Use a screen reader to read a multi-column PDF; verify that the reading order is logical and does not skip between columns prematurely.<sup>60</sup>

| **Component** | **UI Strategy (HTML)**     | **Document Strategy (PDF/UA)**        |
|---------------|----------------------------|---------------------------------------|
| Hierarchy     | \<h1\> through \<h6\> tags | Nested Heading tags in Structure Tree |
| Images        | alt attribute              | Alt entry in Figure tag dictionary    |
| Tables        | \<thead\>, \<th\>, scope   | TH with Scope or ID/Headers           |
| Decorations   | aria-hidden="true" or CSS  | Tagged as "Artifact"                  |
| Language      | lang on \<html\>           | Document-level language metadata      |

## 10. Failure Patterns and Remediation

### Definition

Failure patterns are recurring mistakes in implementation that break accessibility.<sup>11</sup> Remediation is the process of identifying these gaps and applying technical fixes to reach compliance.<sup>1</sup>

### Why it Matters for an Accessibility and Feedback Expert

An AI expert must act as a real-time auditor. Understanding common failures (e.g., the "ARIA patch" problem) allows the AI to proactively prevent them during the design phase.<sup>9</sup>

### Default Rules

1.  **Source over Overlay**: Always remediate the source code. Avoid "accessibility overlays" or "widgets" that mask errors rather than fixing them.<sup>1</sup>

2.  **First Rule of ARIA**: If you can use a native HTML element instead of ARIA, do it.<sup>63</sup>

3.  **No Focus Removal**: Never use scripts to remove focus immediately after it is received (Failure F55).<sup>11</sup>

### Exception Rules

Custom ARIA widgets are permitted when no native HTML equivalent exists (e.g., a complex autocomplete combobox), provided they follow the ARIA APG keyboard and role patterns.<sup>15</sup>

### Fallback Logic

If a complex third-party widget (e.g., a chart) is inaccessible, the AI must provide a "View Data as Table" fallback that is fully semantic and keyboard-accessible.<sup>5</sup>

### Failure Conditions

Using div or span for buttons without a role="button" and a tabindex="0" is a common failure.<sup>9</sup> Redundant alt text (e.g., "Image of a puppy") is a minor but common failure.<sup>14</sup>

### Measurable Thresholds

Automated tools (like axe-core) should report zero "Critical" or "Serious" violations in the remediated code.<sup>1</sup>

### Implementation Guidance for an AI Operator Pack

The AI should implement an "Accessibility Linter" that runs on every code generation. It should automatically flag and fix missing alt tags, orphaned label elements, and invalid ARIA roles.<sup>1</sup>

### Test Cases

1.  Run an automated audit (e.g., WAVE or Lighthouse) on a generated page; verify 100% compliance on detectable rules.<sup>1</sup>

2.  Perform a "Manual Keyboard Walkthrough"; verify that every interactive element can be reached and activated.<sup>19</sup>

# Final Deliverables: AI Operator Pack Configuration

## 1. accessibility-and-feedback-expert.md

- **Purpose**: The central logic and behavioral definition for the AI agent.

- **Contains**: Strategic decision-making rules (POUR principles), standard prioritization (WCAG 2.2 over 2.1), and tone/style guidelines for providing feedback to designers.

- **Does Not Contain**: Specific code snippets for components or detailed checklists.

- **Depends On**: All other .md files in this pack for technical reference.

- **Handoff Skills**: Leadership, Strategic Planning, Technical Writing.

## 2. interaction-state-matrix.md

- **Purpose**: To provide a deterministic lookup for the visual and programmatic requirements of every component state.

- **Contains**: Tables mapping states (Focus, Hover, Active, etc.) to CSS properties (contrast, area) and ARIA attributes (aria-expanded, aria-busy).

- **Does Not Contain**: Navigation or structural rules.

- **Depends On**: keyboard-and-focus-rules.md.

- **Handoff Skills**: Front-end Engineering, CSS Architecture.

## 3. motion-safety-rules.md

- **Purpose**: To enforce life-safety and comfort standards regarding movement and flashing.

- **Contains**: prefers-reduced-motion implementation patterns, 3Hz flash frequency limits, and luminance change thresholds.

- **Does Not Contain**: Layout or color contrast rules.

- **Depends On**: None.

- **Handoff Skills**: Motion Design, Animation Programming.

## 4. keyboard-and-focus-rules.md

- **Purpose**: To ensure the interface is fully operable by keyboard, switch, and voice input.

- **Contains**: Focus area calculations (\$4h + 4w\$), Tab sequence logic, modal trapping patterns, and skip-link requirements.

- **Does Not Contain**: Touch or pointer-specific logic.

- **Depends On**: interaction-state-matrix.md.

- **Handoff Skills**: Interaction Design, DOM Engineering.

## 5. touch-target-rules.md

- **Purpose**: To provide ergonomics and size requirements for touch and pointer-based interactions.

- **Contains**: Minimum pixel sizes (24px, 44px, 48px), spacing requirements, and padding-expansion techniques.

- **Does Not Contain**: Keyboard or motion rules.

- **Depends On**: None.

- **Handoff Skills**: Mobile UX Design, Human Factors Engineering.

## 6. feedback-failure-taxonomy.md

- **Purpose**: A library of "what NOT to do" and how to fix it when errors occur.

- **Contains**: Categorized failure patterns (e.g., F55, F78) and corresponding remediation code snippets.

- **Does Not Contain**: New component design logic.

- **Depends On**: accessibility-test-cases.md.

- **Handoff Skills**: QA Automation, Accessibility Auditing.

## 7. accessibility-test-cases.md

- **Purpose**: A suite of manual and automated tests to verify compliance.

- **Contains**: Screen reader scripts, keyboard walkthrough paths, and automated tool configuration (e.g., axe-core).

- **Does Not Contain**: General UX usability test scripts.

- **Depends On**: All other .md files.

- **Handoff Skills**: Software Testing, Assistive Technology Proficiency.

# A. Condensed Operating Spec for the Expert

1.  **Strict Adherence**: Prioritize WCAG 2.2 Level AA at all times. Never propose a design that violates a Level A or AA success criterion.<sup>3</sup>

2.  **State Mandatory**: Every interactive component must have Focus, Hover, Active, and Disabled states defined before visual polish.<sup>6</sup>

3.  **Contrast First**: No color palette is acceptable without a documented contrast check (4.5:1 for text, 3:1 for graphics).<sup>12</sup>

4.  **No Keyboard Traps**: Any generated modal, menu, or complex widget must have a documented "Escape" and "Tab" logic.<sup>15</sup>

5.  **Touch Target Enforcement**: Default all touch-interface controls to a minimum 44x44 CSS pixel target area.<sup>21</sup>

6.  **Motion Respect**: Wrap all animations in prefers-reduced-motion blocks. Limit any auto-playing motion to \< 5 seconds.<sup>37</sup>

7.  **Semantic Purity**: Prefer \<button\> and \<a\> over \<div\> or \<span\>. Use ARIA only to augment, never to replace, native semantics.<sup>9</sup>

# B. State Matrix Framework

- **Default**: Base state. Text contrast \$\geq 4.5:1\$.<sup>14</sup>

- **Hover**: Pointer enters. Change cursor to pointer. Maintain \$\geq 3:1\$ non-text contrast.<sup>7</sup>

- **Focus**: Tab focus enters. Apply outline (\$2px\$ thickness, \$3:1\$ contrast change).<sup>11</sup>

- **Active**: Activation moment. Visual feedback (e.g., ripple). No specific contrast minimum but must be distinguishable.<sup>7</sup>

- **Selected**: Binary state. Apply aria-selected="true". Use an icon + color change.<sup>15</sup>

- **Disabled**: Inactive. Apply aria-disabled="true". Remove from Tab sequence unless "Read-Only" is needed.<sup>13</sup>

- **Loading**: Asynchronous update. Apply aria-busy="true". Animation must be \$\< 3Hz\$.<sup>40</sup>

- **Error**: Validation failure. Apply aria-invalid="true". Link message via aria-describedby.<sup>19</sup>

# C. Keyboard and Focus Checklist

- \[ \] Is a visible skip-link provided as the first focusable element? <sup>19</sup>

- \[ \] Does every interactive element have a 3:1 contrast focus indicator? <sup>11</sup>

- \[ \] Is the focus indicator at least as large as a 1px perimeter of the component? <sup>12</sup>

- \[ \] Does focus follow a logical top-to-bottom, left-to-right order? <sup>7</sup>

- \[ \] Can all modals and menus be dismissed with the Esc key? <sup>7</sup>

- \[ \] Are there zero keyboard traps in the interface? <sup>3</sup>

- \[ \] Are sticky elements prevented from obscuring focused content? <sup>18</sup>

# D. Motion-Safety Checklist

- \[ \] Does the interface respect the prefers-reduced-motion media query? <sup>34</sup>

- \[ \] Are all non-essential animations disabled for reduced-motion users? <sup>34</sup>

- \[ \] Do all flashing elements flicker at a rate of 3Hz or less? <sup>40</sup>

- \[ \] Is saturated red avoided for any flashing content? <sup>40</sup>

- \[ \] Do animations exceeding 5 seconds provide a Pause/Stop control? <sup>30</sup>

- \[ \] Are rapid zooming or parallax effects limited to essential context? <sup>35</sup>

# E. 20 Stress-Test Prompts for the Expert

1.  "Design a multi-step form that prevents redundant entry of user data from Step 1 to Step 4." <sup>20</sup>

2.  "Create a focus indicator for a star-shaped rating widget that meets WCAG 2.2 Level AAA contrast and size requirements." <sup>11</sup>

3.  "Validate a mobile navigation drawer for focus trapping and 'Esc' key dismissal." <sup>7</sup>

4.  "Implement a tooltip that remains persistent when the user moves their pointer into the tooltip itself." <sup>25</sup>

5.  "Remediate a 'drag and drop' Kanban board to be fully operable via keyboard only." <sup>20</sup>

6.  "Convert a 16x16 icon button into a 44x44 touch target without changing the icon's visual scale." <sup>29</sup>

7.  "Audit a login flow for compliance with Accessible Authentication (Enhanced) Level AAA." <sup>52</sup>

8.  "Establish the aria-live strategy for a real-time stock ticker to avoid interrupting the user." <sup>46</sup>

9.  "Determine the correct 'Read-Only' state implementation for a date picker in a financial dashboard." <sup>13</sup>

10. "Design a high-contrast success state for a color-blind user that does not rely on the color green." <sup>10</sup>

11. "Draft the 'Structure Tree' requirements for a 20-page accessible PDF generated from this UI." <sup>60</sup>

12. "Remediate a div button that currently lacks keyboard accessibility and screen reader roles." <sup>9</sup>

13. "Implement a 'Consistent Help' module that maintains visibility at 400% zoom levels." <sup>3</sup>

14. "Evaluate a pulse animation for potential seizure risks based on general and red flash thresholds." <sup>40</sup>

15. "Create a skip link that becomes visible on focus and bypasses three separate navigation sidebars." <sup>19</sup>

16. "Refactor an 'infinite scroll' feed to include a mechanism for keyboard users to skip to the footer." <sup>19</sup>

17. "Validate the contrast of a progress bar that uses a red-to-green gradient as its fill color." <sup>12</sup>

18. "Design a 'Loading' skeleton screen that is hidden from screen readers until the content actually arrives." <sup>14</sup>

19. "Write the ARIA role and state mapping for a three-state toggle (On, Off, Partial)." <sup>15</sup>

20. "Remediate an accessibility overlay widget by replacing its features with native source code fixes." <sup>1</sup>

#### Works cited

1.  UserWay Alternative: Why Overlays Fail and What Actually Works - TestParty, accessed April 8, 2026, [<u>https://testparty.ai/blog/userway-alternative-real-accessibility-compliance</u>](https://testparty.ai/blog/userway-alternative-real-accessibility-compliance)

2.  Accessibility Overlay Widgets Attract Lawsuits, accessed April 8, 2026, [<u>https://www.accessibility.works/blog/accessibility-overlay-widgets-attract-lawsuits/</u>](https://www.accessibility.works/blog/accessibility-overlay-widgets-attract-lawsuits/)

3.  Web Content Accessibility Guidelines (WCAG) 2.2 - W3C, accessed April 8, 2026, [<u>https://www.w3.org/TR/WCAG22/</u>](https://www.w3.org/TR/WCAG22/)

4.  Salesforce Accessibility Overview: Features and Tips - Twistellar, accessed April 8, 2026, [<u>https://twistellar.com/blog/salesforce-accessibility-overview</u>](https://twistellar.com/blog/salesforce-accessibility-overview)

5.  Accessibility - Carbon Design System, accessed April 8, 2026, [<u>https://carbondesignsystem.com/guidelines/accessibility/overview/</u>](https://carbondesignsystem.com/guidelines/accessibility/overview/)

6.  To hover or not to hover? Understanding WCAG requirements for UI component states - MN.gov, accessed April 8, 2026, [<u>https://mn.gov/mnit/media/blog/?id=38-680276</u>](https://mn.gov/mnit/media/blog/?id=38-680276)

7.  Inputs – Material Design 3, accessed April 8, 2026, [<u>https://m3.material.io/foundations/interaction/inputs</u>](https://m3.material.io/foundations/interaction/inputs)

8.  2.4.13 Focus Appearance (Level AAA) - WCAG, accessed April 8, 2026, [<u>https://www.wcag.com/designers/2-4-13-focus-appearance/</u>](https://www.wcag.com/designers/2-4-13-focus-appearance/)

9.  ARIA & Advanced Semantics - by Tito Adeoye - Medium, accessed April 8, 2026, [<u>https://medium.com/@titoadeoye/aria-advanced-semantics-8740f449321e</u>](https://medium.com/@titoadeoye/aria-advanced-semantics-8740f449321e)

10. Accessibility - Lightning Design System 2, accessed April 8, 2026, [<u>https://www.lightningdesignsystem.com/2e1ef8501/p/112ac5</u>](https://www.lightningdesignsystem.com/2e1ef8501/p/112ac5)

11. Understanding Success Criterion 2.4.13: Focus Appearance \| WAI ..., accessed April 8, 2026, [<u>https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html</u>](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)

12. The New Requirements for WCAG 2.2 \| Vision Australia. Blindness ..., accessed April 8, 2026, [<u>https://www.visionaustralia.org/business-consulting/digital-access/blog/the-new-requirements-for-wcag-2-2</u>](https://www.visionaustralia.org/business-consulting/digital-access/blog/the-new-requirements-for-wcag-2-2)

13. Read-only states - Carbon Design System, accessed April 8, 2026, [<u>https://carbondesignsystem.com/patterns/read-only-states-pattern/</u>](https://carbondesignsystem.com/patterns/read-only-states-pattern/)

14. Accessibility - Material Design, accessed April 8, 2026, [<u>https://m2.material.io/design/usability/accessibility.html</u>](https://m2.material.io/design/usability/accessibility.html)

15. Authoring Practices Guide (APG) Examples & Rules in 2025 - Elementor, accessed April 8, 2026, [<u>https://elementor.com/blog/apg-explained/</u>](https://elementor.com/blog/apg-explained/)

16. Top 5 ARIA Implementation Errors - BarrierBreak, accessed April 8, 2026, [<u>https://www.barrierbreak.com/top-5-aria-implementation-errors/</u>](https://www.barrierbreak.com/top-5-aria-implementation-errors/)

17. WAI-ARIA basics - Learn web development \| MDN, accessed April 8, 2026, [<u>https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/WAI-ARIA_basics</u>](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/WAI-ARIA_basics)

18. What's New in WCAG 2.2 \| Web Accessibility Initiative (WAI) - W3C, accessed April 8, 2026, [<u>https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/</u>](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)

19. Mastering Website Accessibility Remediation \| Bug Tracking Blog @ Bird Eats Bug, accessed April 8, 2026, [<u>https://birdeatsbug.com/blog/web-accessibility-remediation</u>](https://birdeatsbug.com/blog/web-accessibility-remediation)

20. WCAG 2.2 New Success Criteria: Complete Implementation Guide - TestParty, accessed April 8, 2026, [<u>https://testparty.ai/blog/wcag-22-new-success-criteria</u>](https://testparty.ai/blog/wcag-22-new-success-criteria)

21. WCAG 2.2 Updates \| Accessibility Resources and Code Examples - Deque University, accessed April 8, 2026, [<u>https://dequeuniversity.com/resources/wcag-2.2/</u>](https://dequeuniversity.com/resources/wcag-2.2/)

22. Common Website Accessibility Issues: How to Fix Them Fast - Elfsight, accessed April 8, 2026, [<u>https://elfsight.com/blog/website-accessibility-issues/</u>](https://elfsight.com/blog/website-accessibility-issues/)

23. A.21 WCAG 2.2 Success Criterion 2.4.13 - Focus Appearance - Digital Policy Office, accessed April 8, 2026, [<u>https://www.digitalpolicy.gov.hk/en/our_work/digital_government/digital_inclusion/accessibility/promulgating_resources/handbook/appendix_a/a21_2413_focus_appearance.html</u>](https://www.digitalpolicy.gov.hk/en/our_work/digital_government/digital_inclusion/accessibility/promulgating_resources/handbook/appendix_a/a21_2413_focus_appearance.html)

24. Guide to Accessible Web Design & Development - Section508.gov, accessed April 8, 2026, [<u>https://www.section508.gov/develop/guide-accessible-web-design-development/</u>](https://www.section508.gov/develop/guide-accessible-web-design-development/)

25. 1.4.13 Content on Hover or Focus (Level AA) - WCAG, accessed April 8, 2026, [<u>https://www.wcag.com/authors/1-4-13-content-on-hover-or-focus/</u>](https://www.wcag.com/authors/1-4-13-content-on-hover-or-focus/)

26. W3C Accessibility Guidelines (WCAG) 3.0, accessed April 8, 2026, [<u>https://www.w3.org/TR/wcag-3.0/</u>](https://www.w3.org/TR/wcag-3.0/)

27. To ARIA! The Cause of, and Solution to, All Our Accessibility Problems - WebAIM, accessed April 8, 2026, [<u>https://webaim.org/blog/aria-cause-solution/</u>](https://webaim.org/blog/aria-cause-solution/)

28. ARIA Authoring Practices Guide \| APG \| WAI - W3C, accessed April 8, 2026, [<u>https://www.w3.org/WAI/ARIA/apg/</u>](https://www.w3.org/WAI/ARIA/apg/)

29. Accessibility designing – Material Design 3, accessed April 8, 2026, [<u>https://m3.material.io/foundations/designing/structure</u>](https://m3.material.io/foundations/designing/structure)

30. Usability - Accessibility - Material Design v3 - Under Development, accessed April 8, 2026, [<u>https://mdc.almoamen.net/usability/accessibility</u>](https://mdc.almoamen.net/usability/accessibility)

31. Staying on Target: Meeting the Minimum Target Size \| DubBot, accessed April 8, 2026, [<u>https://dubbot.com/dubblog/2024/staying-on-target.html</u>](https://dubbot.com/dubblog/2024/staying-on-target.html)

32. Match Media: Spectrum Web Components, accessed April 8, 2026, [<u>https://opensource.adobe.com/spectrum-web-components/tools/match-media/</u>](https://opensource.adobe.com/spectrum-web-components/tools/match-media/)

33. Text field - Spectrum, Adobe's design system, accessed April 8, 2026, [<u>https://spectrum.adobe.com/page/text-field/</u>](https://spectrum.adobe.com/page/text-field/)

34. prefers-reduced-motion - CSS - MDN Web Docs, accessed April 8, 2026, [<u>https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion</u>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)

35. prefers-reduced-motion: Sometimes less movement is more \| Articles - web.dev, accessed April 8, 2026, [<u>https://web.dev/articles/prefers-reduced-motion</u>](https://web.dev/articles/prefers-reduced-motion)

36. Supporting Reduced Motion: Enhancing Accessibility in Web Apps - Esri, accessed April 8, 2026, [<u>https://www.esri.com/arcgis-blog/products/js-api-arcgis/mapping/supporting-reduced-motion-enhancing-accessibility-in-web-apps</u>](https://www.esri.com/arcgis-blog/products/js-api-arcgis/mapping/supporting-reduced-motion-enhancing-accessibility-in-web-apps)

37. Design accessible animation and movement with code examples - Pope Tech Resources, accessed April 8, 2026, [<u>https://blog.pope.tech/2025/12/08/design-accessible-animation-and-movement/</u>](https://blog.pope.tech/2025/12/08/design-accessible-animation-and-movement/)

38. Using media queries for accessibility - CSS - MDN Web Docs, accessed April 8, 2026, [<u>https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility</u>](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility)

39. Understanding Success Criterion 2.2.2: Pause, Stop, Hide \| WAI - W3C, accessed April 8, 2026, [<u>https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html</u>](https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html)

40. Understanding Success Criterion 2.3.1 \| Understanding WCAG 2.0 - W3C, accessed April 8, 2026, [<u>https://www.w3.org/TR/UNDERSTANDING-WCAG20/seizure-does-not-violate.html</u>](https://www.w3.org/TR/UNDERSTANDING-WCAG20/seizure-does-not-violate.html)

41. Understanding Success Criterion 2.3.1: Three Flashes or Below Threshold - W3C, accessed April 8, 2026, [<u>https://www.w3.org/WAI/WCAG20/Understanding/three-flashes-or-below-threshold</u>](https://www.w3.org/WAI/WCAG20/Understanding/three-flashes-or-below-threshold)

42. Understanding Success Criterion 2.3.1: Three Flashes or Below Threshold - W3C on GitHub, accessed April 8, 2026, [<u>https://w3c.github.io/wcag21/understanding/three-flashes-or-below-threshold.html</u>](https://w3c.github.io/wcag21/understanding/three-flashes-or-below-threshold.html)

43. Understanding Success Criterion 2.3.1: Three Flashes or Below ..., accessed April 8, 2026, [<u>https://www.w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold.html</u>](https://www.w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold.html)

44. WCAG 2.1 - SC 2.3.1 Three Flashes or Below Threshold - Bureau of Internet Accessibility, accessed April 8, 2026, [<u>https://www.boia.org/wcag2/cp/2.3.1</u>](https://www.boia.org/wcag2/cp/2.3.1)

45. Testing Methods: Three Flashes or Below Threshold - Dennis Deacon, accessed April 8, 2026, [<u>https://www.dennisdeacon.com/web/accessibility/testing-methods-three-flashes-or-below-threshold/</u>](https://www.dennisdeacon.com/web/accessibility/testing-methods-three-flashes-or-below-threshold/)

46. ARIA live regions - MDN Web Docs - Mozilla, accessed April 8, 2026, [<u>https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions</u>](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Guides/Live_regions)

47. Technique ARIA22:Using role=status to present status messages - W3C, accessed April 8, 2026, [<u>https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22</u>](https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22)

48. Accessible notifications with ARIA Live Regions (Part 2) - Sara Soueidan, accessed April 8, 2026, [<u>https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-2/</u>](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-2/)

49. ARIA: aria-live attribute - MDN Web Docs - Mozilla, accessed April 8, 2026, [<u>https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-live</u>](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-live)

50. Understanding WCAG 3.0: Key Changes From WCAG 2 - TestDevLab, accessed April 8, 2026, [<u>https://www.testdevlab.com/blog/wcag-3-key-changes</u>](https://www.testdevlab.com/blog/wcag-3-key-changes)

51. Understanding Success Criterion 3.3.8: Accessible Authentication (Minimum) \| WAI - W3C, accessed April 8, 2026, [<u>https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html</u>](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)

52. An Accessible Guide to WCAG 3.3.9: Going for Gold - Auth0, accessed April 8, 2026, [<u>https://auth0.com/blog/an-accessible-guide-to-wcag-3-3-9/</u>](https://auth0.com/blog/an-accessible-guide-to-wcag-3-3-9/)

53. What is Carbon? - Carbon Design System, accessed April 8, 2026, [<u>https://carbondesignsystem.com/all-about-carbon/what-is-carbon/</u>](https://carbondesignsystem.com/all-about-carbon/what-is-carbon/)

54. WCAG 3.0: what's changing and what you need to know - We Create Digital, accessed April 8, 2026, [<u>https://wecreate.digital/blog/wcag-3-whats-changing-why-it-matters/</u>](https://wecreate.digital/blog/wcag-3-whats-changing-why-it-matters/)

55. Understanding Success Criterion 3.3.9: Accessible Authentication (Enhanced) \| WAI - W3C, accessed April 8, 2026, [<u>https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-enhanced.html</u>](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-enhanced.html)

56. WCAG 2.2: New Success Criteria, More Inclusive Content, accessed April 8, 2026, [<u>https://www.wcag.com/blog/wcag-2-2-aa-summary-and-checklist-for-website-owners/</u>](https://www.wcag.com/blog/wcag-2-2-aa-summary-and-checklist-for-website-owners/)

57. Readability and Accessibility Training \| WU Marketing - MyWillamette, accessed April 8, 2026, [<u>https://my.willamette.edu/site/digital-accessibility/guidelines/readability</u>](https://my.willamette.edu/site/digital-accessibility/guidelines/readability)

58. Accessibility Checklist for Web Developers & UX Designers - Recite Me, accessed April 8, 2026, [<u>https://reciteme.com/news/accessibility-checklist-for-web-developers-and-ux-designers/</u>](https://reciteme.com/news/accessibility-checklist-for-web-developers-and-ux-designers/)

59. PDF/UA vs WCAG: Key Differences & Why Both Matter - Continual Engine, accessed April 8, 2026, [<u>https://www.continualengine.com/blog/pdf-ua-vs-wcag/</u>](https://www.continualengine.com/blog/pdf-ua-vs-wcag/)

60. WCAG 2.1 AA vs. PDF/UA - Accessibility at UB, accessed April 8, 2026, [<u>https://www.buffalo.edu/access/digital/content/documents/pdf/wcagvspdfua.html</u>](https://www.buffalo.edu/access/digital/content/documents/pdf/wcagvspdfua.html)

61. PDF/UA compliance guide: Requirements, standards, and best practices - Nutrient, accessed April 8, 2026, [<u>https://www.nutrient.io/blog/pdf-ua-compliance-guide/</u>](https://www.nutrient.io/blog/pdf-ua-compliance-guide/)

62. Understanding PDF accessibility standards - Equidox, accessed April 8, 2026, [<u>https://equidox.co/blog/understanding-pdf-accessibility-standards/</u>](https://equidox.co/blog/understanding-pdf-accessibility-standards/)

63. Accessibility - Carbon Design System, accessed April 8, 2026, [<u>https://carbondesignsystem.com/guidelines/accessibility/developers/</u>](https://carbondesignsystem.com/guidelines/accessibility/developers/)

64. WCAG vs PDF/UA vs EN 301 549: What Each Accessibility Standard Means for Your Business Communication - Quertum, accessed April 8, 2026, [<u>https://quertum.net/accessibility-standards/</u>](https://quertum.net/accessibility-standards/)

65. Notes on relying on the ARIA Authoring Practices Guide - Stefan Judis, accessed April 8, 2026, [<u>https://www.stefanjudis.com/notes/notes-on-relying-on-the-aria-authoring-practices-guide/</u>](https://www.stefanjudis.com/notes/notes-on-relying-on-the-aria-authoring-practices-guide/)

66. Accessibility - Cards – Material Design 3, accessed April 8, 2026, [<u>https://m3.material.io/components/cards/accessibility</u>](https://m3.material.io/components/cards/accessibility)

67. ARIA live regions - Module 11 - ESDC / IT Accessibility office, accessed April 8, 2026, [<u>https://bati-itao.github.io/learning/esdc-self-paced-web-accessibility-course/module11/aria-live.html</u>](https://bati-itao.github.io/learning/esdc-self-paced-web-accessibility-course/module11/aria-live.html)
