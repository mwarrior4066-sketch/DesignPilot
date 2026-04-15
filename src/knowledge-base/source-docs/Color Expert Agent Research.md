<!-- Optimized from original source file: Color Expert Agent Research.docx. All textual content preserved in markdown form for size-efficient packaging. -->

# Operational Architecture and Perceptual Logic for an AI Color Expert Agent

The systematic governance of color within multi-platform design ecosystems has evolved from a subjective aesthetic pursuit into a rigorous engineering discipline rooted in vision science and cognitive psychology.<sup>1</sup> This transition is driven by the necessity of ensuring universal accessibility, maintaining brand integrity across divergent media, and managing the complexity of tokenized implementation.<sup>3</sup> To function as a production-level operator, an AI Color Expert Agent must move beyond generic color theory to employ a deterministic architecture that prioritizes measurable evidence-specifically perceptual contrast models, tonal scaling algorithms, and semantic token hierarchies.<sup>5</sup> This report establishes the comprehensive operational knowledge needed to build such an agent, providing the technical rules, fallback logic, and validation protocols required for an integrated AI design operator pack.

## 1. Color decision architecture

### 1.1. Definition

Color decision architecture is the high-level logic framework and routing system that an expert agent uses to classify design tasks and apply the appropriate mathematical constraints based on medium, intent, and platform.<sup>8</sup> It defines the sequence of operations from initial intent detection to the generation of implementation-ready variables.<sup>10</sup>

### 1.2. Why it matters for an AI Color Expert Agent

An agent without a formal decision architecture risks applying "marketing colors" to "functional interfaces," leading to catastrophic accessibility failures.<sup>12</sup> By employing a routing model, the agent can distinguish between expressive tasks (branding) and utility tasks (UX/UI), loading specific rules for each without manual intervention.<sup>13</sup> This ensures that color decisions are context-aware and verifiable.<sup>6</sup>

### 1.3. Default rules

The system defaults to a hierarchical orchestrator-worker pattern.<sup>11</sup> The orchestrator agent identifies the task type (e.g., "Web Dashboard") and delegates to the "Accessibility Rule File" and "Token Architecture File".<sup>9</sup> The primary color space is sRGB for screen and CMYK for print, with HCT (Hue, Chroma, Tone) acting as the underlying model for all tonal transformations.<sup>7</sup>

### 1.4. Exception rules

In high-density environments like EHR (Electronic Health Records) or financial dashboards, the system overrides standard "spacious" contrast rules, prioritizing legibility at small font sizes (10-12px) and increasing the required APCA Lc values by a minimum of 15 points.<sup>18</sup>

### 1.5. Fallback logic

If the input intent is ambiguous, the agent defaults to the U.S. Web Design System (USWDS) base palette, which is pre-validated for Section 508 compliance.<sup>21</sup> If a requested color fails the contrast check, the agent must not reject it entirely but instead shift its "Tone" in the HCT space to the nearest compliant value while maintaining Hue and Chroma fidelity.<sup>22</sup>

### 1.6. Failure conditions

Failure occurs when the agent follows a "deterministic chain" for a task requiring "dynamic reasoning," such as failing to adjust a palette when switching from a high-quality monitor to a low-contrast projector.<sup>10</sup>

### 1.7. Measurable thresholds

Thresholds are determined by the routing classifier, as detailed in the following table:

| **Task Category**      | **Primary Goal** | **Minimum Contrast Metric** | **Logic Source** |
|------------------------|------------------|-----------------------------|------------------|
| **UX/UI System**       | Readability      | WCAG 2.1 AA / Lc 75         | <sup>26</sup>    |
| **Branding/Identity**  | Expression       | Delta E \< 2 (Consistency)  | <sup>13</sup>    |
| **Data Visualization** | Discriminability | CVD-safe (Okabe-Ito)        | <sup>29</sup>    |
| **Print Production**   | Color Match      | Pantone Match               | <sup>31</sup>    |

### 1.8. Implementation guidance for an AI operator pack

The agent should be stored in color-expert-agent.md. It must contain "discovery" triggers that activate when terms like "palette," "contrast," or "theme" are detected.<sup>11</sup> It should hand off to the typography-agent for font-weight-dependent contrast checks and to the layout-agent for density assessments.<sup>16</sup>

### 1.9. Test cases

Scenario: "Create a color system for a medical dashboard using the hospital's primary red brand color." Agent Logic: Classify as "High-Density Utility." Delegate brand color to the "Branding Agent" for accents. Generate high-contrast neutrals for the interface. Ensure "Error Red" is chromatically distinct from "Brand Red" to avoid semantic overlap.<sup>35</sup>

## 2. Accessibility and contrast science

### 2.1. Definition

Accessibility in color is the application of psychophysical models to ensure that text and graphics remain perceivable across a diverse range of visual abilities, including color vision deficiencies (CVD) and sensitivity to glare or halation.<sup>26</sup>

### 2.2. Why it matters for an AI Color Expert Agent

Standard WCAG 2.x ratios are based on a simple linear luminance formula that does not account for the "spatial frequency" of text or the way humans perceive contrast in dark mode.<sup>5</sup> An expert agent must utilize APCA (Accessible Perceptual Contrast Algorithm) to provide "reading-centric" advice that adjusts for font size and weight.<sup>27</sup>

### 2.3. Default rules

The agent enforces WCAG 2.1/2.2 AA as the legal minimum (4.5:1 for body text) while using APCA Lc 75 as the quality target for standard reading.<sup>27</sup> For non-text elements like borders or focus rings, a 3:1 ratio (WCAG) or Lc 45 (APCA) is required.<sup>27</sup>

### 2.4. Exception rules

"Vibrating Colors": The agent must detect and block saturated red/green or blue/orange combinations even if they pass contrast math, as they cause physiological discomfort and headaches.<sup>38</sup>

### 2.5. Fallback logic

When a color fails Lc 75 for body text, the agent evaluates if increasing the font weight (e.g., from 400 to 700) or size (e.g., to 24px) allows it to pass at a lower threshold (Lc 60).<sup>5</sup>

### 2.6. Failure conditions

"The Orange Problem": WCAG often passes bright orange text on white despite its poor legibility; the agent must flag this as a failure based on the APCA "borderline" score.<sup>26</sup>

### 2.7. Measurable thresholds

Based on the APCA Readability Criterion (ARC):

| **Text Use Case**      | **Standard Weight** | **Bold Weight (700+)** | **Non-Text Target** |
|------------------------|---------------------|------------------------|---------------------|
| **Main Body Text**     | Lc 75               | Lc 60                  | N/A                 |
| **Large Text (18pt+)** | Lc 60               | Lc 45                  | N/A                 |
| **Captions/Labels**    | Lc 90               | Lc 75                  | N/A                 |
| **UI Components**      | N/A                 | N/A                    | Lc 45 (3:1)         |
| **Ref**                | <sup>5</sup>        | <sup>5</sup>           | <sup>27</sup>       |

### 2.8. Implementation guidance for an AI operator pack

The pack should include color-accessibility-rules.md, which defines a "Contrast Matrix Framework".<sup>12</sup> This framework should calculate contrast for every foreground/background pair in a theme. The agent must use Delta E 2000 calculations to ensure that functional colors (e.g., "Success" and "Warning") are distinguishable for users with color-blindness.<sup>28</sup>

### 2.9. Test cases

Input: "Verify if \#767676 is acceptable for body text on a \#FFFFFF background." Agent Logic: WCAG 2.1 ratio is 4.54:1 (Pass). APCA Lc is ~63 (Fail for body text, target is Lc 75). Recommendation: Darken color to \#595959 to reach Lc 75.<sup>27</sup>

## 3. Light mode and dark mode system behavior

### 3.1. Definition

Light and dark mode system behavior is the set of rules for transforming a palette's luminance and saturation when the display polarity shifts, ensuring hierarchical consistency and eye comfort.<sup>3</sup>

### 3.2. Why it matters for an AI Color Expert Agent

Dark mode is not a literal inversion of light mode. In low-light environments, the human eye becomes more sensitive to brightness (Hunt Effect) and contrast (Stevens Effect), meaning that pure white on pure black causes "halation"-the visual bleeding of text.<sup>23</sup> The agent must proactively manage "Elevation" where surfaces closer to the light source are lighter in both modes.<sup>50</sup>

### 3.3. Default rules

Use "Parallel Color Scales".<sup>3</sup> In dark mode, the system defaults to a dark gray background (Tone 10, e.g., \#121212) rather than pure black to reduce glare.<sup>38</sup> Brand and semantic colors must be desaturated by 15-30% to prevent visual vibration against dark surfaces.<sup>38</sup>

### 3.4. Exception rules

Highly saturated "Neon" colors should be used exclusively for CTAs and never for large surfaces in dark mode, as they violate visual comfort principles.<sup>49</sup>

### 3.5. Fallback logic

If the user provides only a light-mode brand color, the agent uses HCT "Tonal Mirroring": a color at Tone 30 in light mode (dark version) is remapped to Tone 80 in dark mode (light version) to maintain the same contrast distance from the background.<sup>1</sup>

### 3.6. Failure conditions

"Burnt" colors: When a light-mode color is applied to a dark background without adjustment, appearing too intense or losing its hue character.<sup>23</sup> "Lost Elevation": When nested elements in dark mode are the same tone as the base background, destroying spatial hierarchy.<sup>3</sup>

### 3.7. Measurable thresholds

- **Elevation Delta:** Each level of elevation (e.g., surface to card) should increase luminance by a minimum of 4-8%.<sup>49</sup>

- **Glare Limit:** Body text in dark mode should not exceed Tone 90 (Off-white).<sup>49</sup>

- **Desaturation Limit:** Primary colors in dark mode should have a Chroma value ~30% lower than their light-mode counterparts.<sup>49</sup>

### 3.8. Implementation guidance for an AI operator pack

Define the dark-mode-color-logic.md file. It should include a "token swapping table" that maps light-mode tokens to dark-mode counterparts based on their semantic intent.<sup>3</sup> It should use the prefers-color-scheme media query as the primary activation condition.<sup>52</sup>

### 3.9. Test cases

Scenario: "Apply the 'Corporate Blue' brand color to a header in dark mode." Agent Logic: Identify the base light-mode blue. Reduce saturation by 20%. Increase lightness (Tone) from 40 to 80. Ensure it maintains Lc 60 contrast against the \#121212 background.<sup>23</sup>

## 4. Semantic color token architecture

### 4.1. Definition

Semantic color token architecture is a hierarchical data structure that maps raw color values (Primitives) to their functional roles (Semantics) and specific UI uses (Components), enabling scalable theme management and cross-platform portability.<sup>53</sup>

### 4.2. Why it matters for an AI Color Expert Agent

An agent without semantic tokens is forced to manage "hard-coded chaos" where every color change requires manual updates to hundreds of variables.<sup>12</sup> Tokens act as a "contract" between design and code; the agent manages the *logic* of the token (e.g., "all warning borders must be orange-500"), and the implementation follows automatically.<sup>4</sup>

### 4.3. Default rules

Follow the W3C Design Tokens Community Group (DTCG) specification.<sup>57</sup> Use a three-tier naming system:

1.  **Primitive:** blue-500 (Value).<sup>53</sup>

2.  **Semantic:** action-primary (Intent).<sup>12</sup>

3.  **Component:** button-primary-bg (Scope).<sup>53</sup> All names should be human-readable, flat, and predictable (e.g., text-muted vs gray-300).<sup>53</sup>

### 4.4. Exception rules

Static colors (fixed colors) should be used for elements that must never change across themes, such as a logo or a status indicator that depends on external real-world metaphors (e.g., "Live" recording red).<sup>1</sup>

### 4.5. Fallback logic

If a component token is requested but not defined, the agent "aliases" it to the nearest semantic token (e.g., alert-icon fallback to icon-negative).<sup>53</sup>

### 4.6. Failure conditions

"Atomic Token Hell": Creating a unique token for every single element, leading to system bloat.<sup>6</sup> Value-based naming in the semantic layer (e.g., naming a token primary-blue which breaks when the brand changes to purple).<sup>12</sup>

### 4.7. Measurable thresholds

- **Token Depth:** Limit to 3 levels of aliasing to maintain performance and debuggability.<sup>59</sup>

- **Schema Validity:** Must comply with JSON Schema Draft 2020-12.<sup>63</sup>

- **Naming Convention:** Must follow the Context-Unit-Clarification structure.<sup>53</sup>

### 4.8. Implementation guidance for an AI operator pack

Create semantic-color-token-architecture.md. It must include a JSON-friendly schema example.<sup>57</sup> The agent should provide a "Token Registry" that defines the mandatory metadata for each entry: name, value, type, description, and contrast requirement.<sup>61</sup>

### 4.9. Test cases

Prompt: "Create a set of tokens for a primary success notification."

Agent Logic:

1.  Primitive: green-500 (#228B22).

2.  Semantic: feedback-success-bg -\> green-100; feedback-success-text -\> green-900.

3.  Component: notification-success-border -\> feedback-success-bg-dark.<sup>12</sup>

## 5. Palette construction logic

### 5.1. Definition

Palette construction logic is the mathematical process of generating a foundational set of color scales (ramps) based on brand anchors and functional requirements, ensuring consistency in luminosity and saturation across all hues.<sup>1</sup>

### 5.2. Why it matters for an AI Color Expert Agent

Designers often create palettes based on "taste," leading to "muddy" or "grayed-out" shades that fail contrast checks.<sup>68</sup> An expert agent uses calculated decisions-manipulating HSL or HCT properties-to generate "perceptually uniform" scales where a weight of 500 in blue is equivalent in perceived brightness to a weight of 500 in red.<sup>7</sup>

### 5.3. Default rules

The system uses the "Magic Number" system from USWDS.<sup>21</sup> Each color family is generated with 10 grades (5-90), where white is 0 and black is 100.<sup>21</sup> A grade difference of 50+ points between two colors guarantees Section 508 AA compliance.<sup>21</sup> Apply the 60/30/10 rule for proportional distribution: 60% neutrals, 30% supporting secondaries, 10% accent.<sup>75</sup>

### 5.4. Exception rules

"Hue Shifting": As colors darken, the agent must shift the hue toward "darkness wells" (Red/Blue); as they lighten, shift toward "brightness peaks" (Yellow/Cyan) to prevent graying.<sup>70</sup> For example, light red should shift toward orange/yellow; dark red should shift toward purple.<sup>70</sup>

### 5.5. Fallback logic

If brand guidance is missing, the agent generates a "Neutral-Heavy" palette: a base gray scale (Tone 98-10) with one brand-agnostic interactive blue (Tone 60v) and three semantic colors (Success, Warning, Error).<sup>12</sup>

### 5.6. Failure conditions

"Color Bloat": Defining more than 15 steps per family, which creates redundant options that make selection difficult.<sup>12</sup> "Pure Inversion": Swapping Tone 0 for Tone 100 in dark mode without adjusting saturation, leading to vibrating text.<sup>23</sup>

### 5.7. Measurable thresholds

- **Tonal Ramps:** 10-12 discrete steps per color family.<sup>1</sup>

- **Luminance Targets:** Grade 50 must fall between relative luminance 0.175 and 0.183.<sup>21</sup>

- **Magic Number Implication:** 40+ points = AA Large Text; 50+ points = AA Normal Text; 70+ points = AAA.<sup>21</sup>

### 5.8. Implementation guidance for an AI operator pack

Create palette-decision-framework.md. It should contain the "Hue Shift Step" table (e.g., 30° shift for orange to yellow).<sup>70</sup> Use tools like Leonardo or HCT pickers to automate the generation of tonal scales from a single seed color.<sup>22</sup>

### 5.9. Test cases

Scenario: "Generate a palette from a bright blue anchor (#0000FF)."

Agent Logic:

1.  Map anchor to Tone 40 (Primary CTA).

2.  Generate Tones 98, 90, 80 (Light surfaces).

3.  Generate Tones 30, 20, 10 (Dark text/borders).

4.  Shift Tones 90-80 toward Cyan (+Hue angle) and Tones 30-10 toward Purple (-Hue angle).<sup>67</sup>

## 6. Dashboard and data visualization color rules

### 6.1. Definition

Data visualization color rules are the constraints applied to qualitative (categorical), sequential, and diverging palettes to maximize data discriminability, prevent cognitive overload, and support CVD-safe viewing.<sup>78</sup>

### 6.2. Why it matters for an AI Color Expert Agent

Dashboards are "high-density" environments where color carries meaning, not just style.<sup>80</sup> Improper use of color can lead to "False Interpretation" (e.g., using red for a neutral category that users perceive as an error) or "Visual Noise" (using too many hues).<sup>35</sup>

### 6.3. Default rules

Limit categorical palettes to a maximum of 6-8 distinct hues.<sup>83</sup> Prioritize the Okabe-Ito (Wong) palette for universal color-blind accessibility.<sup>29</sup> For sequential data (magnitude), use a single hue with perceptually uniform tonal steps (e.g., light-to-dark).<sup>78</sup>

### 6.4. Exception rules

Diverging palettes (e.g., Red-to-Blue) should only be used when a meaningful midpoint (e.g., Zero, Average) exists.<sup>78</sup>

### 6.5. Fallback logic

If more than 8 categories are required, the agent must require "Multiple Encoding" (e.g., color + pattern, color + shape, or color + direct label) to ensure the data is readable regardless of color perception.<sup>35</sup>

### 6.6. Failure conditions

"Rainbow Palettes": Using the full spectrum for a single data series, which lacks a logical order and is inaccessible for color-blind users.<sup>30</sup> "Border-less charts": Chart segments that blend together without a 1px neutral border.<sup>37</sup>

### 6.7. Measurable thresholds

- **Max Hues:** 6 (Ideal) to 8 (Limit).<sup>83</sup>

- **Segment Contrast:** Minimum 3:1 contrast ratio between adjacent segments in a pie or bar chart.<sup>41</sup>

- **CVD discriminability:** All categories must maintain Delta E \> 5 when viewed in Protanopia/Deuteranopia simulation.<sup>28</sup>

### 6.8. Implementation guidance for an AI operator pack

Establish dashboard-color-rules.md. Include pre-defined color arrays for categorical data (e.g., Okabe-Ito hex codes: \#E69F00, \#56B4E9, \#009E73).<sup>30</sup> The agent should audit charts for "Red/Green Dependency" and recommend Blue/Orange as a safer alternative.<sup>30</sup>

### 6.9. Test cases

Scenario: "Color a map of the US showing population growth per state." Agent Logic: Use a Sequential Palette (e.g., Teal 100 to 900). Assign Tone 90 to the lowest growth and Tone 10 to the highest. Do not use random hues.<sup>78</sup>

## 7. Brand and identity color logic

### 7.1. Definition

Brand color logic governs the translation of high-level visual identity assets into product-safe interface tokens, ensuring that expressive colors do not compromise functional usability.<sup>12</sup>

### 7.2. Why it matters for an AI Color Expert Agent

The brand is "who we are," while the interface is "what we do".<sup>13</sup> A "Luxury Black" brand palette may work for an editorial site but can be physically painful if applied to an enterprise spreadsheet.<sup>19</sup> The agent must proactively "de-brand" certain functional elements (e.g., form fields, table borders) to maintain cognitive efficiency.<sup>12</sup>

### 7.3. Default rules

Strictly separate brand colors from utility colors.<sup>12</sup> Use brand colors only for "Emphasis" (Logos, primary buttons, high-level navigation).<sup>2</sup> All functional signals (Success, Error) must follow universal semantic patterns (Green, Red) regardless of the brand palette.<sup>12</sup>

### 7.4. Exception rules

Institutional and Civic brands (e.g., government) must prioritize "Federal Neutrals" and strictly follow AAA standards, limiting brand expression to the logo and header bar.<sup>21</sup>

### 7.5. Fallback logic

When a brand color is too light for accessibility (e.g., \#FFFF00 Yellow), the agent creates an "Ink" variant (Tone 10) for text on that background and a "Deep" variant (Tone 20) for that hue to be used as text on light surfaces.<sup>60</sup>

### 7.6. Failure conditions

"Identity Overload": Using brand colors for 30%+ of the UI surface, which creates visual fatigue and hides secondary actions.<sup>75</sup> Using "Success Green" as the primary brand color, which causes semantic collisions during error/success messaging.<sup>36</sup>

### 7.7. Measurable thresholds

- **Expression Limit:** Brand-specific tokens should comprise \<10% of total UI pixels.<sup>75</sup>

- **Semantic Integrity:** Error red must be at least Delta E \> 15 away from any brand-primary color.<sup>28</sup>

### 7.8. Implementation guidance for an AI operator pack

Create brand-vs-interface-color-rules.md. Define a "Psychographic Context" matrix:

- **Technical:** Prioritize density and neutral grays.<sup>18</sup>

- **Creative:** Allow higher chroma and experimental pairings.<sup>13</sup>

- **Civic:** Prioritize trust-heavy blues and safe grays.<sup>21</sup>

### 7.9. Test cases

Scenario: "The brand is 'Solar Energy' with a Primary Yellow anchor. Design the login page."

Agent Logic:

1.  Surface: White (#FFFFFF).

2.  CTA: Yellow background with Black text (Pass Lc 90).

3.  Error: Red text with warning icon (Do not use Yellow for errors).

4.  Borders: Neutral Gray-200.<sup>12</sup>

## 8. Print, PDF, and presentation color behavior

### 8.1. Definition

This logic governs the conversion of screen-based RGB colors into the specific technical gamuts of physical print (CMYK), universally accessible documents (PDF/UA), and large-scale projection (High Contrast).<sup>17</sup>

### 8.2. Why it matters for an AI Color Expert Agent

A color that looks "Perfectly Accessible" on an OLED screen may become "Invisible" when printed on uncoated paper or projected in a brightly lit conference room.<sup>17</sup> The agent must handle gamut-mapping failures by proactively shifting values to "Print-Safe" and "Projector-Safe" ranges.<sup>32</sup>

### 8.3. Default rules

For print, the system converts all tokens using the Pantone Color Bridge standard.<sup>99</sup> For PDF/UA compliance, the agent must generate a "Text Layer" for all graphics and ensure 4.5:1 contrast for all document text.<sup>41</sup> For presentations, default to high-contrast mode (Ivory text on dark background) to account for light washout.<sup>24</sup>

### 8.4. Exception rules

Specialty brand colors (e.g., Neon or Metallic) must be flagged for "Spot Color" (Pantone PMS) usage, as they cannot be replicated in 4-color process (CMYK).<sup>17</sup>

### 8.5. Fallback logic

If a projector is low-quality, the agent recommends increasing the "Delta" between colors by 20% and avoiding thin font weights.<sup>44</sup>

### 8.6. Failure conditions

"CMYK Saturation Loss": Using bright electric blue (#0000FF) in a print file, which results in a muddy purple-gray.<sup>17</sup> "Un-tagged PDF": A document that has accessible colors but lacks the structural "tags" required by screen readers.<sup>101</sup>

### 8.7. Measurable thresholds

- **Print Contrast:** 4.5:1 ratio is required for all text in brochures/reports.<sup>41</sup>

- **Presentation Contrast:** Minimum Lc 80 for body text to survive projector washout.<sup>24</sup>

- **Gamut Check:** 100% of tokens must be within the CMYK gamut for print tasks.<sup>31</sup>

### 8.8. Implementation guidance for an AI operator pack

Include print-pdf-presentation-color-rules.md. It must provide a "Gamut Conversion Checklist":

1.  Convert sRGB -\> CMYK.

2.  Identify out-of-gamut colors.

3.  Shift to nearest in-gamut Pantone Bridge value.<sup>31</sup>

### 8.9. Test cases

Scenario: "Export the dashboard for a client boardroom presentation." Agent Logic: Detect "Presentation" intent. Swap to a dark theme with Ivory text. Increase line-weight for charts. Audit for "Vibrating Red/Green" and recommend Magenta/Cyan as safer high-contrast alternatives.<sup>44</sup>

## 9. Interaction states and feedback color systems

### 9.1. Definition

Interaction states are the visual cues used to communicate the dynamic status of a UI element as the user navigates (Rest, Hover, Focus, Pressed, Disabled, Error, Success).<sup>105</sup>

### 9.2. Why it matters for an AI Color Expert Agent

Interaction is a dialogue.<sup>107</sup> If the color change is too subtle, the user doesn't know their action was registered; if it's too jarring, it causes cognitive distraction.<sup>51</sup> The agent must apply a consistent "State Delta" to ensure that the user can distinguish between an "Available" action and a "Selected" one.<sup>42</sup>

### 9.3. Default rules

Use "State Layers" (Overlays).<sup>51</sup>

- **Hover:** +8% Black (Light Mode) or +12% White (Dark Mode) overlay.<sup>51</sup>

- **Focus:** A 3px high-contrast ring (3:1 vs background) that is distinct from the component border.<sup>42</sup>

- **Pressed:** +12-16% Black/White overlay to simulate depth.<sup>51</sup>

- **Disabled:** De-emphasize by 38% opacity and remove all hover/focus logic.<sup>109</sup>

### 9.4. Exception rules

"Color-Alone Violation": The agent must never allow an error state to be indicated *only* by color; it must require an accompanying icon or label.<sup>37</sup>

### 9.5. Fallback logic

For components without background fills (e.g., ghost buttons, links), the agent applies an underline or shifts text chroma/tone by a minimum of 20% for the hover state.<sup>51</sup>

### 9.6. Failure conditions

"The Invisible Focus": When the focus ring color matches the card background.<sup>38</sup> "Active-Inactive Paradox": When a disabled button has enough contrast to look clickable, leading to user frustration.<sup>109</sup>

### 9.7. Measurable thresholds

- **State Delta:** Minimum 10% shift in luminance between Rest and Hover.<sup>51</sup>

- **Focus Visibility:** Minimum 3:1 non-text contrast for the focus indicator.<sup>42</sup>

- **Disabled Opacity:** Fixed at 38% as per Material Design industry standard.<sup>109</sup>

### 9.8. Implementation guidance for an AI operator pack

The agent should output a "State Matrix Table" for every primary component.<sup>42</sup> It must ensure that "Focus" and "Hover" are additive states (can occur simultaneously).<sup>51</sup>

### 9.9. Test cases

Prompt: "Define interaction states for a primary action button."

Agent Logic:

1.  Rest: primary-600.

2.  Hover: primary-700 (Delta L: -10).

3.  Focus: primary-600 with \#FFFFFF / primary-900 dual-ring.

4.  Pressed: primary-800 (Delta L: -20).

5.  Disabled: primary-600 at 38% opacity.<sup>51</sup>

## 10. Failure modes and risk detection

### 10.1. Definition

Failure modes are the systematic taxonomies of color-related design errors that negatively impact usability, accessibility, or technical implementation.<sup>112</sup>

### 10.2. Why it matters for an AI Color Expert Agent

An agent is only as good as its "Self-Correction" capability.<sup>33</sup> It must identify when a design passes mathematical contrast math but fails perceptual "Quality" (e.g., thin fonts, muddy grays, vibrating hues).<sup>39</sup> It must also detect "Process Errors" where token names do not match their intent.<sup>113</sup>

### 10.3. Default rules

The agent runs an "Adversarial Stress Test" on every output.<sup>114</sup> It must flag any color combination with a Delta E \< 2 as "Indistinguishable" and any combination \< Lc 60 as a "Hard Failure" for body text.<sup>27</sup>

### 10.4. Exception rules

Incidental text (pure decoration, invisible UI) has no contrast requirement, but the agent should still flag it for "Visual Clarity".<sup>26</sup>

### 10.5. Fallback logic

If the system detects a "Total Failure" (e.g., the palette is completely unusable), it triggers a "Safety Reset" to the USWDS grayscale palette until the user provides a valid anchor.<sup>21</sup>

### 10.6. Failure conditions

- **The Halation Trap:** Bright white text on pure black (#000000) that strains eyes.<sup>38</sup>

- **The Muddy Neutral:** Grays that carry a faint green or purple tint, making the UI look dirty.<sup>68</sup>

- **Token Drift:** When a designer overrides a token with a raw hex code, breaking the system.<sup>56</sup>

### 10.7. Measurable thresholds

- **Delta E (JND):** \$\Delta E \le 1.0\$ is not perceptible; \$2-10\$ is perceptible at a glance; \$100\$ is opposite.<sup>28</sup>

- **Hue Rollover Discontinuity:** \< 4% error allowed in color space conversion.<sup>116</sup>

- **Axe-Core compliance:** Catch 57%+ of WCAG violations automatically before handoff.<sup>108</sup>

### 10.8. Implementation guidance for an AI operator pack

Develop color-failure-taxonomy.md. It should contain the "11 Red-Team Prompts" to stress-test UI agents.<sup>117</sup> The agent should act as a "Kernel Mode" orchestrator that prevents "User Mode" sub-agents from bypassing accessibility rules.<sup>11</sup>

### 10.9. Test cases

Stress Test: "Use \#FF00FF and \#00FF00 for the login form." Agent Logic: "Reject: Vibrating color pair. Fail: CVD discriminability. Fail: APCA Lc \< 15. Recommendation: Use Functional Neutrals for inputs and High-Chroma Blue for Submit".<sup>30</sup>

## Final Deliverables

### A. Operational spec for the Color Expert Agent

| **Parameter**  | **Specification**                                     | **Ref**       |
|----------------|-------------------------------------------------------|---------------|
| **Purpose**    | Govern all color decisions through perceptual science | <sup>2</sup>  |
| **Triggers**   | Token creation, palette audits, theme transforms      | <sup>8</sup>  |
| **Routing**    | Task -\> Context -\> Ruleset -\> Logic -\> Validation | <sup>11</sup> |
| **Logic**      | Prioritize APCA Lc over WCAG 2.1 ratios for screens   | <sup>5</sup>  |
| **Constraint** | Never use color alone to convey status                | <sup>88</sup> |
| **Handoff**    | Send structured.tokens.json to Dev Skill              | <sup>57</sup> |
| **Evidence**   | Output Lc scores, WCAG ratios, and Delta E            | <sup>5</sup>  |

### B. Color decision tree

1.  **Intent Discovery:** Is this for Utility (UX), Expression (Brand), or Information (Data)?.<sup>12</sup>

2.  **Environment Check:** Is the medium Screen (sRGB), Print (CMYK), or Low-Fi (Projector)?.<sup>24</sup>

3.  **Tonal Generation:** Apply HCT scaling. Is the base surface Light or Dark?.<sup>7</sup>

4.  **Accessibility Audit:** Run APCA check. If Lc \< 75 for body text, shift Tone..<sup>27</sup>

5.  **CVD Simulation:** Run Okabe-Ito audit. Is Delta E \> 5 for all categories?.<sup>30</sup>

6.  **Tokenization:** Map to Context-Unit-Clarification names. Output JSON.<sup>53</sup>

### C. Contrast matrix framework

A production-ready agent must generate this matrix for every theme.

| **Foreground Token** | **Background: surface-base** | **Background: surface-elevated** | **Background: primary-bg** |
|----------------------|------------------------------|----------------------------------|----------------------------|
| **text-primary**     | Lc 85 (Target: 75+)          | Lc 80                            | Lc 70 (Borderline)         |
| **text-muted**       | Lc 65 (Target: 60+)          | Lc 60                            | Lc 50 (Fail)               |
| **icon-accent**      | Lc 55 (Target: 45+)          | Lc 50                            | Lc 30 (Fail)               |
| **link-default**     | Lc 75 (Target: 75+)          | Lc 70                            | Lc 60 (Fail)               |
| **Ref**              | <sup>27</sup>                | <sup>27</sup>                    | <sup>12</sup>              |

### D. Failure test suite (Stress Prompts)

1.  "Create a dark mode where the background is pure \#000000." -\> *Must flag glare/halation risk*.<sup>49</sup>

2.  "Use thin weight Inter font at 12px for body copy in light gray." -\> *Must flag Lc \< 75 failure*.<sup>5</sup>

3.  "Use the brand's 'Gold' color for both warnings and premium buttons." -\> *Must flag semantic collision*.<sup>12</sup>

4.  "Export a bar chart with 15 different hues." -\> *Must reject category count \> 8*.<sup>83</sup>

5.  "Design a form where errors are shown only by a red border." -\> *Must flag color-only violation*.<sup>37</sup>

6.  "Use a bright orange text on a white background." -\> *Must flag WCAG pass/APCA fail trap*.<sup>26</sup>

7.  "Design a disabled button with 4.5:1 contrast." -\> *Must flag failure to de-emphasize*.<sup>109</sup>

8.  "Apply a drop shadow for depth in dark mode." -\> *Must recommend elevation through luminance instead*.<sup>38</sup>

9.  "Use a blue link on a black background." -\> *Must flag visibility failure for dark blues*.<sup>49</sup>

10. "Create a sequential map palette using 5 different hues." -\> *Must recommend single-hue tonal ramp*.<sup>78</sup>

11. "Use \#FFFFFF on \#EEEEEE for a divider." -\> *Must flag Delta E \< 2 failure*.<sup>28</sup>

12. "Name a token 'color-dark-blue'." -\> *Must recommend semantic intent naming*.<sup>12</sup>

13. "Create a three-tier token alias: blue-500 -\> primary -\> button-bg." -\> *Must validate path resolution*.<sup>53</sup>

14. "Use a red text label for 'Delete' and 'Critical Error'." -\> *Must verify semantic distinction*.<sup>36</sup>

15. "Design a chart for Protanopia users using Red and Green." -\> *Must recommend Blue and Orange*.<sup>30</sup>

16. "Apply 100% saturation to all interaction states in dark mode." -\> *Must flag vibrating color risk*.<sup>23</sup>

17. "Design a high-density table using 8pt font." -\> *Must increase Lc targets by +15*.<sup>19</sup>

18. "Export a web-safe palette to CMYK for high-end glossy print." -\> *Must verify gamut constraints*.<sup>17</sup>

19. "Use a white focus ring on a light gray card." -\> *Must flag contrast failure \< 3:1*.<sup>42</sup>

20. "Remap a light-mode primary-50 to dark-mode primary-50." -\> *Must flag failure to transform luminance*.<sup>3</sup>

### E. Shortlist of strongest source references

- **APCA/ARC Readability Criterion (Somers):** The primary science for perceptual contrast.<sup>5</sup>

- **W3C/WCAG 2.2:** The regulatory baseline for global accessibility.<sup>26</sup>

- **Google Material Design 3 (HCT Model):** The industry standard for tonal scaling and color roles.<sup>7</sup>

- **Adobe Spectrum:** Excellence in semantic token naming and theme mode behavior.<sup>53</sup>

- **U.S. Web Design System (USWDS):** Validated accessibility grading and magic numbers.<sup>21</sup>

- **Okabe-Ito (Nature Methods):** Science-backed color-blind safe data palettes.<sup>29</sup>

- **W3C Design Tokens Community Group (DTCG):** Standard JSON schema for variables.<sup>57</sup>

- **ISO 14289 (PDF/UA):** The definitive standard for document accessibility.<sup>97</sup>

#### Works cited

1.  Building a colour system? A guide for product designers. \| by Aileen Xin, accessed April 8, 2026, [<u>https://www.designsystemscollective.com/building-a-colour-system-a-guide-for-product-designers-b0485d94f5a7</u>](https://www.designsystemscollective.com/building-a-colour-system-a-guide-for-product-designers-b0485d94f5a7)

2.  Designing a scalable and accessible color system for your design system - UX Collective, accessed April 8, 2026, [<u>https://uxdesign.cc/designing-a-scalable-and-accessible-color-system-for-your-design-system-f98207eda166</u>](https://uxdesign.cc/designing-a-scalable-and-accessible-color-system-for-your-design-system-f98207eda166)

3.  Dark Mode Design Systems: A Practical Guide \| by Ravindi \| Bootcamp - Medium, accessed April 8, 2026, [<u>https://medium.com/design-bootcamp/dark-mode-design-systems-a-practical-guide-13bc67e43774</u>](https://medium.com/design-bootcamp/dark-mode-design-systems-a-practical-guide-13bc67e43774)

4.  Systematic Taxonomy in Design Tokens: A Framework for Scalable UI Architecture, accessed April 8, 2026, [<u>https://www.designsystemscollective.com/systematic-taxonomy-in-design-tokens-a-framework-for-scalable-ui-architecture-45cc6f2c7686</u>](https://www.designsystemscollective.com/systematic-taxonomy-in-design-tokens-a-framework-for-scalable-ui-architecture-45cc6f2c7686)

5.  WCAG 2 vs APCA Comparisons · Myndex SAPC-APCA · Discussion \#30 - GitHub, accessed April 8, 2026, [<u>https://github.com/Myndex/SAPC-APCA/discussions/30</u>](https://github.com/Myndex/SAPC-APCA/discussions/30)

6.  Finally understanding the Material 3 color system, it took me 1 year : r/UXDesign - Reddit, accessed April 8, 2026, [<u>https://www.reddit.com/r/UXDesign/comments/1oc7e95/finally_understanding_the_material_3_color_system/</u>](https://www.reddit.com/r/UXDesign/comments/1oc7e95/finally_understanding_the_material_3_color_system/)

7.  Color - Material Design 3 - Create personal color schemes, accessed April 8, 2026, [<u>https://m3.material.io/styles/color/system/how-the-system-works</u>](https://m3.material.io/styles/color/system/how-the-system-works)

8.  Decision Trees For UI Components - Smart Interface Design Patterns, accessed April 8, 2026, [<u>https://smart-interface-design-patterns.com/articles/decision-trees/</u>](https://smart-interface-design-patterns.com/articles/decision-trees/)

9.  What is AI Agent Orchestration? - IBM, accessed April 8, 2026, [<u>https://www.ibm.com/think/topics/ai-agent-orchestration</u>](https://www.ibm.com/think/topics/ai-agent-orchestration)

10. Agent system design patterns \| Databricks on AWS, accessed April 8, 2026, [<u>https://docs.databricks.com/aws/en/generative-ai/guide/agent-system-design-patterns</u>](https://docs.databricks.com/aws/en/generative-ai/guide/agent-system-design-patterns)

11. Deterministic AI Orchestration: A Platform Architecture for Autonomous Development, accessed April 8, 2026, [<u>https://www.praetorian.com/blog/deterministic-ai-orchestration-a-platform-architecture-for-autonomous-development/</u>](https://www.praetorian.com/blog/deterministic-ai-orchestration-a-platform-architecture-for-autonomous-development/)

12. Color Consistency in Design Systems - UXPin, accessed April 8, 2026, [<u>https://www.uxpin.com/studio/blog/color-consistency-design-systems/</u>](https://www.uxpin.com/studio/blog/color-consistency-design-systems/)

13. What's a Color Scheme? Creating a Palette for Design Systems - Neue World, accessed April 8, 2026, [<u>https://www.neue.world/learn/design-system/establishing-a-visual-language-colors-a-deep-dive-into-creating-a-color-palette-for-a-design-system</u>](https://www.neue.world/learn/design-system/establishing-a-visual-language-colors-a-deep-dive-into-creating-a-color-palette-for-a-design-system)

14. Orchestration vs Routing in AI: Choosing the Right Pattern for Enterprise Systems - Medium, accessed April 8, 2026, [<u>https://medium.com/@qutbuddinkamaal/orchestration-vs-routing-in-ai-choosing-the-right-pattern-for-enterprise-systems-44a9edcd3268</u>](https://medium.com/@qutbuddinkamaal/orchestration-vs-routing-in-ai-choosing-the-right-pattern-for-enterprise-systems-44a9edcd3268)

15. Four Design Patterns for Event-Driven, Multi-Agent Systems - Confluent, accessed April 8, 2026, [<u>https://www.confluent.io/blog/event-driven-multi-agent-systems/</u>](https://www.confluent.io/blog/event-driven-multi-agent-systems/)

16. Agent orchestration for design systems \| by Cristian Morales Achiardi, accessed April 8, 2026, [<u>https://www.designsystemscollective.com/agent-orchestration-for-design-systems-da0f6a5f24fb</u>](https://www.designsystemscollective.com/agent-orchestration-for-design-systems-da0f6a5f24fb)

17. Understanding the Difference Between Print and Screen Colors - Nebraska.gov, accessed April 8, 2026, [<u>https://corrections.nebraska.gov/sites/default/files/2025-09/Print%20Services.pdf</u>](https://corrections.nebraska.gov/sites/default/files/2025-09/Print%20Services.pdf)

18. 8 Enterprise UX Design Best Practices and Principles \[with examples\], accessed April 8, 2026, [<u>https://uxpilot.ai/blogs/enterprise-ux-design</u>](https://uxpilot.ai/blogs/enterprise-ux-design)

19. Shifting from Consumer UX Design to Enterprise Product Design - Slack Design, accessed April 8, 2026, [<u>https://slack.design/articles/shifting-from-consumer-ux-design-to-enterprise-product-design/</u>](https://slack.design/articles/shifting-from-consumer-ux-design-to-enterprise-product-design/)

20. A framework to create an accessible & harmonious typography system for faster design-dev handoff \| by Priyanka Godbole \| Prototypr, accessed April 8, 2026, [<u>https://blog.prototypr.io/10-practical-steps-to-create-a-predictable-accessible-and-harmonious-typography-system-a-case-6c85d901bedd</u>](https://blog.prototypr.io/10-practical-steps-to-create-a-predictable-accessible-and-harmonious-typography-system-a-case-6c85d901bedd)

21. Using color \| U.S. Web Design System (USWDS), accessed April 8, 2026, [<u>https://designsystem.digital.gov/design-tokens/color/overview/</u>](https://designsystem.digital.gov/design-tokens/color/overview/)

22. Turn your custom color into Material 3 (Material You) colour schema - Medium, accessed April 8, 2026, [<u>https://medium.com/@iam_riyas/turn-your-custom-color-into-material-3-material-you-colour-schema-f490ef2fdee5</u>](https://medium.com/@iam_riyas/turn-your-custom-color-into-material-3-material-you-colour-schema-f490ef2fdee5)

23. Dark Mode Design: Colors That Work in Both Modes \| Görkem YILDIZ, accessed April 8, 2026, [<u>https://gorkemyildiz.com/articles/dark-mode-design-colors-that-work-in-both-modes</u>](https://gorkemyildiz.com/articles/dark-mode-design-colors-that-work-in-both-modes)

24. Projector Color Deviation: Causes and Calibration Methods - Wifi Digital Photo Frame, accessed April 8, 2026, [<u>https://www.ssa-digital.com/faq/projector-color-deviation-causes-and-calibration-methods.html</u>](https://www.ssa-digital.com/faq/projector-color-deviation-causes-and-calibration-methods.html)

25. AI Agent Orchestration Patterns - Azure Architecture Center \| Microsoft Learn, accessed April 8, 2026, [<u>https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns</u>](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)

26. Accessible Colors: From WCAG to APCA - Capellic, accessed April 8, 2026, [<u>https://capellic.com/insights/accessible-colors</u>](https://capellic.com/insights/accessible-colors)

27. Color contrast and APCA - Horizon Design System - ServiceNow, accessed April 8, 2026, [<u>https://horizon.servicenow.com/guidelines/accessibility/color-contrast</u>](https://horizon.servicenow.com/guidelines/accessibility/color-contrast)

28. What Is Delta E? And Why Is It Important for Color Accuracy? - ViewSonic Library, accessed April 8, 2026, [<u>https://www.viewsonic.com/library/creative-work/what-is-delta-e-and-why-is-it-important-for-color-accuracy/</u>](https://www.viewsonic.com/library/creative-work/what-is-delta-e-and-why-is-it-important-for-color-accuracy/)

29. color palette - siegal lab, accessed April 8, 2026, [<u>https://siegal.bio.nyu.edu/color-palette/</u>](https://siegal.bio.nyu.edu/color-palette/)

30. Okabe-Ito Palette Hex Codes & 5 Colorblind-Safe Palettes for Science (2026) \| ConceptViz, accessed April 8, 2026, [<u>https://conceptviz.app/blog/scientific-color-palette-for-research-papers-and-posters</u>](https://conceptviz.app/blog/scientific-color-palette-for-research-papers-and-posters)

31. Pantone to RGB Converter: Your No-Stress Guide for Digital Design - Medium, accessed April 8, 2026, [<u>https://medium.com/@paarthgupta6393/pantone-to-rgb-converter-your-no-stress-guide-for-digital-design-54ea883e4b23</u>](https://medium.com/@paarthgupta6393/pantone-to-rgb-converter-your-no-stress-guide-for-digital-design-54ea883e4b23)

32. Understanding RGB, CMYK, HEX, and Pantone Colors in Commercial Printing, accessed April 8, 2026, [<u>https://davetheprinter.com/printing-tips/understanding-rgb-cmyk-hex-and-pantone-colors-in-commercial-printing/</u>](https://davetheprinter.com/printing-tips/understanding-rgb-cmyk-hex-and-pantone-colors-in-commercial-printing/)

33. Harness design for long-running application development - Anthropic, accessed April 8, 2026, [<u>https://www.anthropic.com/engineering/harness-design-long-running-apps</u>](https://www.anthropic.com/engineering/harness-design-long-running-apps)

34. Typography in Design Systems. Choose Fonts, Set a Hierarchy, and… \| by Nathan Curtis \| EightShapes \| Medium, accessed April 8, 2026, [<u>https://medium.com/eightshapes-llc/typography-in-design-systems-6ed771432f1e</u>](https://medium.com/eightshapes-llc/typography-in-design-systems-6ed771432f1e)

35. How do you handle colors for data visualization in a design system? : r/UXDesign - Reddit, accessed April 8, 2026, [<u>https://www.reddit.com/r/UXDesign/comments/1n6dzb7/how_do_you_handle_colors_for_data_visualization/</u>](https://www.reddit.com/r/UXDesign/comments/1n6dzb7/how_do_you_handle_colors_for_data_visualization/)

36. The Crucial Role of Color Theory in Data Analysis and Visualization, accessed April 8, 2026, [<u>https://towardsdatascience.com/the-crucial-role-of-color-theory-in-data-analysis-and-visualization/</u>](https://towardsdatascience.com/the-crucial-role-of-color-theory-in-data-analysis-and-visualization/)

37. Understanding Color Blindness: A Guide to Accessible Design - Crux Collaborative, accessed April 8, 2026, [<u>https://cruxcollaborative.com/insights/understanding-color-blindness-guide-to-accessible-design</u>](https://cruxcollaborative.com/insights/understanding-color-blindness-guide-to-accessible-design)

38. The Designer's Guide to Dark Mode Accessibility, accessed April 8, 2026, [<u>https://www.accessibilitychecker.org/blog/dark-mode-accessibility/</u>](https://www.accessibilitychecker.org/blog/dark-mode-accessibility/)

39. Understanding the APCA Advanced Perceptual Contrast Algorithm - Accessibility Checker, accessed April 8, 2026, [<u>https://www.accessibilitychecker.org/blog/apca-advanced-perceptual-contrast-algorithm/</u>](https://www.accessibilitychecker.org/blog/apca-advanced-perceptual-contrast-algorithm/)

40. Contrasts an digital Accessibility - a deep Dive - Netz-barrierefrei.de, accessed April 8, 2026, [<u>https://netz-barrierefrei.de/en/deep-dive-contrasts.html</u>](https://netz-barrierefrei.de/en/deep-dive-contrasts.html)

41. Making Color Usage Accessible \| Section508.gov, accessed April 8, 2026, [<u>https://www.section508.gov/create/making-color-usage-accessible/</u>](https://www.section508.gov/create/making-color-usage-accessible/)

42. To hover or not to hover? Understanding WCAG requirements for UI component states - MN.gov, accessed April 8, 2026, [<u>https://mn.gov/mnit/media/blog/?id=38-680276</u>](https://mn.gov/mnit/media/blog/?id=38-680276)

43. How to annotate design system components for accessibility - Zeroheight, accessed April 8, 2026, [<u>https://zeroheight.com/blog/how-to-annotate-design-system-components-for-accessibility/</u>](https://zeroheight.com/blog/how-to-annotate-design-system-components-for-accessibility/)

44. Optimizing Colors for Projected Presentations - Edge for Scholars at Vanderbilt, accessed April 8, 2026, [<u>https://edgeforscholars.vumc.org/optimizing-colors-for-projected-presentations/</u>](https://edgeforscholars.vumc.org/optimizing-colors-for-projected-presentations/)

45. The Ultimate Guide to Accessible Presentation Design, accessed April 8, 2026, [<u>https://www.stinsondesign.com/blog/ultimate-guide-accessible-presentation-design</u>](https://www.stinsondesign.com/blog/ultimate-guide-accessible-presentation-design)

46. Dissecting Delta E and the Mathematical Difference Between Colors - PRINTING United Alliance, accessed April 8, 2026, [<u>https://www.printing.org/content/2025/02/18/dissecting-delta-e-and-the-mathematical-difference-between-colors</u>](https://www.printing.org/content/2025/02/18/dissecting-delta-e-and-the-mathematical-difference-between-colors)

47. It's time for a more sophisticated color contrast check for data visualizations - Datawrapper, accessed April 8, 2026, [<u>https://www.datawrapper.de/blog/color-contrast-check-data-vis-wcag-apca</u>](https://www.datawrapper.de/blog/color-contrast-check-data-vis-wcag-apca)

48. Color adjustment of brand logos for dark mode display - PMC, accessed April 8, 2026, [<u>https://pmc.ncbi.nlm.nih.gov/articles/PMC12822999/</u>](https://pmc.ncbi.nlm.nih.gov/articles/PMC12822999/)

49. Designing Dark Mode - Complete Web and Mobile Designer UI/UX, Figma, + more - EduRev, accessed April 8, 2026, [<u>https://edurev.in/t/504193/Designing-Dark-Mode</u>](https://edurev.in/t/504193/Designing-Dark-Mode)

50. The Dark Art of Designing for Dark Mode - Flagrant, accessed April 8, 2026, [<u>https://www.beflagrant.com/blog/dark-art-of-dark-mode</u>](https://www.beflagrant.com/blog/dark-art-of-dark-mode)

51. Interaction States \| Foundations - eBay Playbook, accessed April 8, 2026, [<u>https://playbook.ebay.com/foundations/interaction-states</u>](https://playbook.ebay.com/foundations/interaction-states)

52. prefers-color-scheme - CSS - MDN Web Docs - Mozilla, accessed April 8, 2026, [<u>https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme</u>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)

53. Design tokens - Spectrum, Adobe's design system, accessed April 8, 2026, [<u>https://spectrum.adobe.com/page/design-tokens/</u>](https://spectrum.adobe.com/page/design-tokens/)

54. Color token naming: what works, what fails & the best approach for your design system, accessed April 8, 2026, [<u>https://www.designsystemscollective.com/color-token-naming-what-works-what-fails-the-best-approach-for-your-design-system-50f844d25f01</u>](https://www.designsystemscollective.com/color-token-naming-what-works-what-fails-the-best-approach-for-your-design-system-50f844d25f01)

55. Design tokens explained (and how to build a design token system) - Contentful, accessed April 8, 2026, [<u>https://www.contentful.com/blog/design-token-system/</u>](https://www.contentful.com/blog/design-token-system/)

56. Color Palette in Design Systems for UI, accessed April 8, 2026, [<u>https://designsystems.surf/articles/color-in-design-systems</u>](https://designsystems.surf/articles/color-in-design-systems)

57. Design Tokens Community Group - Style Dictionary, accessed April 8, 2026, [<u>https://styledictionary.com/info/dtcg/</u>](https://styledictionary.com/info/dtcg/)

58. Design Tokens Format Module 2025.10, accessed April 8, 2026, [<u>https://www.designtokens.org/tr/drafts/format/</u>](https://www.designtokens.org/tr/drafts/format/)

59. Design tokens - The Design System Guide, accessed April 8, 2026, [<u>https://thedesignsystem.guide/design-tokens</u>](https://thedesignsystem.guide/design-tokens)

60. Using color - Spectrum, Adobe's design system, accessed April 8, 2026, [<u>https://spectrum.adobe.com/page/using-color/</u>](https://spectrum.adobe.com/page/using-color/)

61. design-tokens \| Skills Marketplace - LobeHub, accessed April 8, 2026, [<u>https://lobehub.com/bg/src/skills/tyler-r-kendrick-agent-skills-design-tokens</u>](https://lobehub.com/bg/src/skills/tyler-r-kendrick-agent-skills-design-tokens)

62. 3-tier design token system : r/DesignSystems - Reddit, accessed April 8, 2026, [<u>https://www.reddit.com/r/DesignSystems/comments/1it1erb/3tier_design_token_system/</u>](https://www.reddit.com/r/DesignSystems/comments/1it1erb/3tier_design_token_system/)

63. Create initial JSON Schemas (token, dimension, manifest) · Issue \#720 · adobe/spectrum-design-data - GitHub, accessed April 8, 2026, [<u>https://github.com/adobe/spectrum-design-data/issues/720</u>](https://github.com/adobe/spectrum-design-data/issues/720)

64. Design Tokens Community Group Format · Issue \#5290 - GitHub, accessed April 8, 2026, [<u>https://github.com/SchemaStore/schemastore/issues/5290</u>](https://github.com/SchemaStore/schemastore/issues/5290)

65. Spectrum Design Data - Adobe Open Source, accessed April 8, 2026, [<u>https://opensource.adobe.com/spectrum-design-data/</u>](https://opensource.adobe.com/spectrum-design-data/)

66. Design Systems Are Products Too; Build Accessibility In From the Start \| by Ashita Taneja, accessed April 8, 2026, [<u>https://medium.com/@taneja.ashita/design-systems-are-products-too-build-accessibility-in-from-the-start-b92eaaa31f8e</u>](https://medium.com/@taneja.ashita/design-systems-are-products-too-build-accessibility-in-from-the-start-b92eaaa31f8e)

67. Improving a Design System Color Palette \| by Miguel Silva, accessed April 8, 2026, [<u>https://www.designsystemscollective.com/improving-a-design-system-color-palette-3275eef10ac0</u>](https://www.designsystemscollective.com/improving-a-design-system-color-palette-3275eef10ac0)

68. How to Use “Muddy Colors” to Create a Sophisticated and Earthy Aesthetic, accessed April 8, 2026, [<u>https://www.anthonymichaelinteriordesign.com/how-to-use-muddy-colors-to-create-a-sophisticated-and-earthy-aesthetic</u>](https://www.anthonymichaelinteriordesign.com/how-to-use-muddy-colors-to-create-a-sophisticated-and-earthy-aesthetic)

69. Why can some designers pull flat colors off and it looks modern and cool but when I try to do flat colors it looks "muddy"? How do you avoid colors looking muddy when aiming for a trendy flat color : r/graphic_design - Reddit, accessed April 8, 2026, [<u>https://www.reddit.com/r/graphic_design/comments/okoz4c/why_can_some_designers_pull_flat_colors_off_and/</u>](https://www.reddit.com/r/graphic_design/comments/okoz4c/why_can_some_designers_pull_flat_colors_off_and/)

70. Principles of Creating a Color Palette in Interface Design \| by Nikita Zinchenko, accessed April 8, 2026, [<u>https://www.designsystemscollective.com/principles-of-creating-a-color-palette-in-interface-design-d86b942775cd</u>](https://www.designsystemscollective.com/principles-of-creating-a-color-palette-in-interface-design-d86b942775cd)

71. Design System Sprint 2: One Color Palette to Rule them All \| by Marcin Treder \| Medium, accessed April 8, 2026, [<u>https://medium.com/@marcintreder/design-system-sprint-2-one-color-palette-to-rule-them-all-d0114ed1f659</u>](https://medium.com/@marcintreder/design-system-sprint-2-one-color-palette-to-rule-them-all-d0114ed1f659)

72. Unlocking Accessible Design. Demystifying Contrast Ratios \| by Axis Design Lab \| Medium, accessed April 8, 2026, [<u>https://medium.com/@AxisDesignLab/unlocking-accessible-design-ecb5990a6ca8</u>](https://medium.com/@AxisDesignLab/unlocking-accessible-design-ecb5990a6ca8)

73. Designing an accessible color scheme, again \| by Katie Riley \| Envoy Design \| Medium, accessed April 8, 2026, [<u>https://medium.com/envoy-design/designing-an-accessible-color-scheme-again-fd35cfa9d796</u>](https://medium.com/envoy-design/designing-an-accessible-color-scheme-again-fd35cfa9d796)

74. Use the U.S. Web Design System and focus on bigger challenges - Nava, accessed April 8, 2026, [<u>https://www.navapbc.com/insights/us-web-design-system</u>](https://www.navapbc.com/insights/us-web-design-system)

75. What is the 60-30-10 Rule? Complete Guide to Color Balance - sixtythirtyten Blog, accessed April 8, 2026, [<u>https://www.sixtythirtyten.co/blog/60-30-10-rule-complete-guide</u>](https://www.sixtythirtyten.co/blog/60-30-10-rule-complete-guide)

76. Best Practice Color Balance with 60–30–10 Rule for Harmonious Design, accessed April 8, 2026, [<u>https://alwanth.webflow.io/blog/best-practice-color-balance-with-60-30-10-rule-for-harmonious-design</u>](https://alwanth.webflow.io/blog/best-practice-color-balance-with-60-30-10-rule-for-harmonious-design)

77. Theme color tokens \| U.S. Web Design System (USWDS), accessed April 8, 2026, [<u>https://designsystem.digital.gov/design-tokens/color/theme-tokens/</u>](https://designsystem.digital.gov/design-tokens/color/theme-tokens/)

78. Data Visualization - Tegel \| Scania, accessed April 8, 2026, [<u>https://tegel.scania.com/patterns/data-visualization/color-palettes</u>](https://tegel.scania.com/patterns/data-visualization/color-palettes)

79. Data visualization colors - Texas Department of Transportation, accessed April 8, 2026, [<u>https://www.txdot.gov/about/brand-guidelines/data-visualization/data-visualization-colors.html</u>](https://www.txdot.gov/about/brand-guidelines/data-visualization/data-visualization-colors.html)

80. Visual Perception and Pre-Attentive Attributes in Oncological Data Visualisation - PMC - NIH, accessed April 8, 2026, [<u>https://pmc.ncbi.nlm.nih.gov/articles/PMC12292122/</u>](https://pmc.ncbi.nlm.nih.gov/articles/PMC12292122/)

81. Minimalism in Data Visualization: A Guide to Smarter Dashboards - ClicData, accessed April 8, 2026, [<u>https://www.clicdata.com/blog/the-power-of-minimalism-in-data-visualization/</u>](https://www.clicdata.com/blog/the-power-of-minimalism-in-data-visualization/)

82. Colors don't solve problems - D'Amato, accessed April 8, 2026, [<u>https://blog.damato.design/posts/colors-dont-solve-problems/</u>](https://blog.damato.design/posts/colors-dont-solve-problems/)

83. 8 Rules for optimal use of color in data visualization, accessed April 8, 2026, [<u>https://towardsdatascience.com/8-rules-for-optimal-use-of-color-in-data-visualization-b283ae1fc1e2/</u>](https://towardsdatascience.com/8-rules-for-optimal-use-of-color-in-data-visualization-b283ae1fc1e2/)

84. Color for data visualization - Spectrum, Adobe's design system, accessed April 8, 2026, [<u>https://spectrum.adobe.com/page/color-for-data-visualization/</u>](https://spectrum.adobe.com/page/color-for-data-visualization/)

85. Mastering The Art of Data Visualization Color Palettes - Datylon, accessed April 8, 2026, [<u>https://www.datylon.com/blog/a-guide-to-data-visualization-color-palette</u>](https://www.datylon.com/blog/a-guide-to-data-visualization-color-palette)

86. Data visualization colour palette - Summit Design System - The City of Calgary, accessed April 8, 2026, [<u>https://summit.calgary.ca/visual-identity/colour/data-visualization-colour-palette.html</u>](https://summit.calgary.ca/visual-identity/colour/data-visualization-colour-palette.html)

87. When to use sequential and when to use diverging color scales \| Datawrapper Blog, accessed April 8, 2026, [<u>https://www.datawrapper.de/blog/diverging-vs-sequential-color-scales</u>](https://www.datawrapper.de/blog/diverging-vs-sequential-color-scales)

88. How to Design for Color Blindness: Best Practices for Accessible Websites - AudioEye, accessed April 8, 2026, [<u>https://www.audioeye.com/post/8-ways-to-design-a-color-blind-friendly-website/</u>](https://www.audioeye.com/post/8-ways-to-design-a-color-blind-friendly-website/)

89. Colour design system for an accessible colour palette - Manitoba Flexible Learning Hub, accessed April 8, 2026, [<u>https://mbhub.ca/resources/colour-design-system-for-an-accessible-colour-palette/</u>](https://mbhub.ca/resources/colour-design-system-for-an-accessible-colour-palette/)

90. Colors \| Data Visualization Standards, accessed April 8, 2026, [<u>https://xdgov.github.io/data-design-standards/components/colors</u>](https://xdgov.github.io/data-design-standards/components/colors)

91. Please help explain to me like I'm five the difference between design system and a brand guide or brand system? And how do you use them IRL? : r/UXDesign - Reddit, accessed April 8, 2026, [<u>https://www.reddit.com/r/UXDesign/comments/1m5zxnr/please_help_explain_to_me_like_im_five_the/</u>](https://www.reddit.com/r/UXDesign/comments/1m5zxnr/please_help_explain_to_me_like_im_five_the/)

92. What is brand identity? 5 key elements (with real examples) \| Canva, accessed April 8, 2026, [<u>https://www.canva.com/resources/brand-identity/</u>](https://www.canva.com/resources/brand-identity/)

93. A Guide to Colors in Design Systems: How to Build, Name, and Validate Them, accessed April 8, 2026, [<u>https://supercharge.design/blog/a-guide-to-colors-in-design-systems</u>](https://supercharge.design/blog/a-guide-to-colors-in-design-systems)

94. Inclusive Color Palettes for Government Websites - Avero Advisors, accessed April 8, 2026, [<u>https://averoadvisors.com/insights/inclusive-color-palettes-for-government-websites/</u>](https://averoadvisors.com/insights/inclusive-color-palettes-for-government-websites/)

95. Color system - Spectrum, Adobe's design system, accessed April 8, 2026, [<u>https://spectrum.adobe.com/page/color-system/</u>](https://spectrum.adobe.com/page/color-system/)

96. Delta E 101, accessed April 8, 2026, [<u>http://zschuessler.github.io/DeltaE/learn/</u>](http://zschuessler.github.io/DeltaE/learn/)

97. Accessible PDF: requirements, standards, and compliance - aiopsgroup, accessed April 8, 2026, [<u>https://aiopsgroup.com/accessible-pdfs/</u>](https://aiopsgroup.com/accessible-pdfs/)

98. Color Contrast in PDFs: Ensuring Readability for All Users - Elon University, accessed April 8, 2026, [<u>https://www.elon.edu/u/university-communications/online-communications/accessibility-toolkit/pdfs/color-contrast/</u>](https://www.elon.edu/u/university-communications/online-communications/accessibility-toolkit/pdfs/color-contrast/)

99. Color Bridge Guide Coated - PANTONE® USA, accessed April 8, 2026, [<u>https://www.pantone.com/products/graphics/color-bridge-guide-coated</u>](https://www.pantone.com/products/graphics/color-bridge-guide-coated)

100. Color for Print and Packaging: Which guide is right for you? - Pantone, accessed April 8, 2026, [<u>https://www.pantone.com/articles/technical/color-for-print-and-packaging-which-guide-is-right-for-you</u>](https://www.pantone.com/articles/technical/color-for-print-and-packaging-which-guide-is-right-for-you)

101. WCAG 2.1 AA vs. PDF/UA - Accessibility at UB, accessed April 8, 2026, [<u>https://www.buffalo.edu/access/digital/content/documents/pdf/wcagvspdfua.html</u>](https://www.buffalo.edu/access/digital/content/documents/pdf/wcagvspdfua.html)

102. What Are the PDF/UA Standards and Guidelines? - Recite Me, accessed April 8, 2026, [<u>https://reciteme.com/us/news/pdf-ua-standards-and-guidelines/</u>](https://reciteme.com/us/news/pdf-ua-standards-and-guidelines/)

103. Recommended Background for Projected Presentations \| Edward Tufte, accessed April 8, 2026, [<u>https://www.edwardtufte.com/notebook/recommended-background-for-projected-presentations/</u>](https://www.edwardtufte.com/notebook/recommended-background-for-projected-presentations/)

104. PDF/UA compliance guide: Requirements, standards, and best practices - Nutrient, accessed April 8, 2026, [<u>https://www.nutrient.io/blog/pdf-ua-compliance-guide/</u>](https://www.nutrient.io/blog/pdf-ua-compliance-guide/)

105. Interaction states \| Dynatrace Developer, accessed April 8, 2026, [<u>https://developer.dynatrace.com/design/foundations/interaction-states/</u>](https://developer.dynatrace.com/design/foundations/interaction-states/)

106. States – Material Design 3, accessed April 8, 2026, [<u>https://m3.material.io/foundations/interaction/states</u>](https://m3.material.io/foundations/interaction/states)

107. Design systems - The Book on Accessibility, accessed April 8, 2026, [<u>https://www.thebookonaccessibility.com/roles/design-systems/</u>](https://www.thebookonaccessibility.com/roles/design-systems/)

108. Accessibility in Design Systems: Building the Foundation for Compliant Products - A11y Pros, accessed April 8, 2026, [<u>https://a11ypros.com/blog/accessibility-in-design-systems</u>](https://a11ypros.com/blog/accessibility-in-design-systems)

109. States - Material Design, accessed April 8, 2026, [<u>https://m2.material.io/design/interaction/states.html</u>](https://m2.material.io/design/interaction/states.html)

110. States – Material Design 3, accessed April 8, 2026, [<u>https://m3.material.io/foundations/interaction/states/applying-states</u>](https://m3.material.io/foundations/interaction/states/applying-states)

111. Color Blindness Accessibility: A Designer Guide, accessed April 8, 2026, [<u>https://www.levelaccess.com/blog/color-blindness-accessibility-what-designers-need-to-know/</u>](https://www.levelaccess.com/blog/color-blindness-accessibility-what-designers-need-to-know/)

112. The 6 most common WCAG failures and how to fix them - Recite Me, accessed April 8, 2026, [<u>https://reciteme.com/us/news/6-most-common-wcag-failures/</u>](https://reciteme.com/us/news/6-most-common-wcag-failures/)

113. Development of a Software Design Error Taxonomy: A Systematic Literature Review, accessed April 8, 2026, [<u>https://digitalcommons.montclair.edu/cgi/viewcontent.cgi?article=1004&context=computing-facpubs</u>](https://digitalcommons.montclair.edu/cgi/viewcontent.cgi?article=1004&context=computing-facpubs)

114. Designing for AI Failures: Error States and Recovery Patterns \| Clearly Design, accessed April 8, 2026, [<u>https://clearly.design/articles/ai-design-4-designing-for-ai-failures</u>](https://clearly.design/articles/ai-design-4-designing-for-ai-failures)

115. What Is Factorial Stress Testing for AI Agents? The Mount Sinai Method \| MindStudio, accessed April 8, 2026, [<u>https://www.mindstudio.ai/blog/what-is-factorial-stress-testing-ai-agents</u>](https://www.mindstudio.ai/blog/what-is-factorial-stress-testing-ai-agents)

116. Color difference - Wikipedia, accessed April 8, 2026, [<u>https://en.wikipedia.org/wiki/Color_difference</u>](https://en.wikipedia.org/wiki/Color_difference)

117. Multimodal Safety: 11 Prompts That Break UI Agents \| by Modexa \| Mar, 2026 \| Medium, accessed April 8, 2026, [<u>https://medium.com/@Modexa/multimodal-safety-11-prompts-that-break-ui-agents-af0f599f27bb</u>](https://medium.com/@Modexa/multimodal-safety-11-prompts-that-break-ui-agents-af0f599f27bb)

118. Understanding Success Criterion 1.4.1: Use of Color \| WAI - W3C, accessed April 8, 2026, [<u>https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html</u>](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html)

119. Design Tokens Format Module 2025.10, accessed April 8, 2026, [<u>https://www.designtokens.org/tr/2025.10/format/</u>](https://www.designtokens.org/tr/2025.10/format/)

120. Dark Mode Best Practices: Improving the Experience - Gapsy Studio, accessed April 8, 2026, [<u>https://gapsystudio.com/blog/designing-for-dark-mode/</u>](https://gapsystudio.com/blog/designing-for-dark-mode/)
