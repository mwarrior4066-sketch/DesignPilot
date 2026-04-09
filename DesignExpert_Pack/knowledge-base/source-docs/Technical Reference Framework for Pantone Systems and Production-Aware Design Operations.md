# Technical Reference Framework for Pantone Systems and Production-Aware Design Operations

The transition from digital design to physical production represents a fundamental challenge in the fidelity of color communication. In the context of modular artificial intelligence design operators, the ability to bridge the gap between additive light models and subtractive ink models is critical for ensuring brand consistency, economic efficiency, and technical feasibility. The Pantone Matching System (PMS) serves as the primary infrastructure for this bridge, providing a standardized language that allows designers, manufacturers, and automated agents to define, communicate, and control color from initial inspiration to final realization.<sup>1</sup> By integrating spectral data, substrate physics, and process-aware logic, an AI operator can transition from a mere selector of aesthetic hues to a sophisticated decision-support system capable of navigating the complex variables of the print industry.<sup>3</sup>

## The Taxonomy and Architecture of Pantone Color Systems

A professional color reference library must begin with a clear distinction between the various Pantone systems and their intended applications. The Pantone Matching System for graphics is the dominant standard for ink-on-paper applications, but it is supported by specialized guides for digital simulation, textile production, and industrial coatings.<sup>5</sup> For an AI operator to function effectively, it must distinguish between solid (spot) colors and process colors, as the underlying mechanisms of their production are fundamentally different.

### Solid vs Process Color Mechanics

Solid colors, often referred to as spot colors, represent the truest expression of color intent. These are formulated as single, pre-mixed inks using 18 basic pigments mixed in precise ratios to achieve a target shade.<sup>5</sup> This method allows for the reproduction of colors that exist outside the standard four-color process gamut, such as high-saturation oranges, deep purples, and metallic or neon finishes.<sup>8</sup> In contrast, process colors utilize the CMYK model—Cyan, Magenta, Yellow, and Black—layered in varying screen tint percentages to simulate a color.<sup>5</sup> While process printing is generally more economical for multi-color jobs, it can only accurately reproduce approximately 55% of the Pantone Spot Color library.<sup>8</sup>

| **System Component** | **Primary Goal**           | **Ink Formulation**        | **Gamut Achievability**   |
|----------------------|----------------------------|----------------------------|---------------------------|
| **Formula Guide**    | Spot Color Definition      | 18 Basic Pigment Mixes     | 100% of Solid Library     |
| **Color Bridge**     | Spot to Process Comparison | CMYK + Digital Values      | 55% Match to Solid        |
| **Extended Gamut**   | Expanded Process Printing  | CMYK + Orange/Green/Violet | 90% Match to Solid        |
| **CMYK Guide**       | Budget-Conscious Process   | CMYK Only                  | Unique Process-Only Range |

The Formula Guide remains the industry standard for color specification and quality control, providing physical swatches and ink formulations for 2,390 colors.<sup>10</sup> However, for an AI managing multi-channel campaigns, the Color Bridge is an essential tool, providing side-by-side comparisons of spot colors and their closest CMYK equivalents, along with sRGB and Hex values for digital design.<sup>11</sup>

### Advanced Process Solutions: Extended Gamut (ECG)

For industries where the cost of custom spot inks is prohibitive but high fidelity is required—such as the packaging and label industry—Extended Gamut (ECG) printing offers a superior alternative to standard CMYK. By adding Orange, Green, and Violet (OGV) base inks to the four-color set, ECG printing can hit roughly 90% of Pantone Spot Colors without requiring custom ink mixing.<sup>8</sup> This approach provides a significant improvement over the Color Bridge guide, where CMYK equivalents are often noticeably duller or shifted in hue.<sup>11</sup>

For the design operator, ECG logic should be prioritized in packaging workflows. Since the same seven inks remain in the press at all times, the system reduces downtime, eliminates wash-ups between jobs, and improves press utilization.<sup>13</sup> This results in shorter makereadys and more stable color separations, particularly when used in tandem with professional prepress software like Esko Equinox.<sup>13</sup>

## Substrate Physics and the Physics of Color Shift

One of the most common pitfalls in automated color selection is the failure to account for substrate interaction. The same ink formula will result in a radically different visual appearance depending on the paper stock it is applied to.<sup>1</sup> The Pantone system addresses this through the use of suffixes: "C" for Coated and "U" for Uncoated.<sup>15</sup>

### The Coated vs Uncoated Dilemma

Coated paper has a surface treatment that effectively seals the pores of the paper. This coating prevents ink from absorbing deeply into the fibers, allowing it to sit on the surface where it remains vibrant and sharp.<sup>15</sup> Coated stocks are ideal for magazines, catalogs, and promotional materials where color intensity is paramount.<sup>16</sup> Uncoated paper, being porous, absorbs the ink like a sponge, which causes the colors to appear more muted, subdued, and organic.<sup>15</sup> This finish is often chosen for stationery, envelopes, and premium brochures where a tactile, sophisticated feel is desired over high vibrancy.<sup>11</sup>

| **Characteristic**      | **Coated (C) Suffix**            | **Uncoated (U) Suffix**              |
|-------------------------|----------------------------------|--------------------------------------|
| **Ink Behavior**        | Sits on top of the surface       | Absorbs into paper fibers            |
| **Visual Appearance**   | Bright, vibrant, deep saturation | Dull, soft, prominent grain          |
| **Typical Stock**       | 100 lb. Glossy/Matte Text        | 80 lb. Premium Offset                |
| **Production Context**  | High-impact marketing, packaging | Stationery, books, eco-brands        |
| **Dark Shade Behavior** | Remains deep and true            | Often shifts to a lighter gray/brown |

For an AI system, "Pantone 116 C" and "Pantone 116 U" should be treated as two distinct visual targets despite sharing the same ink recipe.<sup>16</sup> In brand identity systems, it is often necessary to specify different Pantone numbers for coated and uncoated applications to achieve a perceived match. For example, a color that appears correct on a coated brochure might need to be substituted for a slightly more vibrant Pantone number when printed on uncoated letterhead to compensate for the absorption loss.<sup>17</sup>

### Ink Holdout and Detail Fidelity

The concept of "ink holdout" is critical for technical design. High ink holdout on coated paper allows for finer detail and enhanced color fidelity, as the ink dots from halftoning do not spread (dot gain) as much as they do on uncoated stock.<sup>15</sup> On uncoated stocks, the high absorption increases dot gain, which can lead to "plugging" in dark areas and a loss of contrast.<sup>15</sup> Design operators must adjust their vector treatments and halftoning expectations based on the final substrate choice.<sup>1</sup>

## Technical Color Translation and Mathematical Fidelity

Avoiding "fake precision" is a major requirement for an AI color operator. This involves understanding that Hex, RGB, and CMYK are device-dependent color spaces, meaning their results change based on the hardware and software used.<sup>8</sup> For high-accuracy translation, the operator must utilize device-independent color spaces, specifically CIELAB (L*a*b\*).<sup>8</sup>

### The Role of CIELAB in Color Management

CIELAB is a three-dimensional map of all colors the human eye can see. Unlike CMYK, it is not tied to a specific set of inks or paper.<sup>8</sup> When an AI needs to convert a Pantone Spot Color to a process simulation, it should begin with the L*a*b\* reference of that spot color.<sup>19</sup> The next step involves converting that L*a*b\* value into a CMYK recipe using a specific ICC profile that matches the printing condition, such as Fogra 39 or GRACoL C1.<sup>19</sup>

Relying on the static CMYK numbers provided in the Color Bridge guide is often insufficient for professional results, as the Bridge uses a specific printing condition that may not match the house conditions of a given print shop.<sup>19</sup> A sophisticated AI system should favor L*a*b\*-based conversions and refine the resulting CMYK recipes to use three inks where possible, such as removing small amounts of yellow from a blue hue to improve visual "cleanness".<sup>19</sup>

### Delta E (**\$\Delta E\$**) and Acceptable Tolerances

Delta E is the mathematical expression of the difference between two colors. In professional print, a \$\Delta E\$ value of less than 1.0 is generally considered imperceptible to the human eye, while a value below 2.3 is considered a professional match.<sup>20</sup> When Delta E exceeds 2.3, visible mismatches occur, particularly in sensitive ranges like greens where humans have high color perception.<sup>20</sup>

| **Delta E Range** | **Perception Level**        | **Design Action**               |
|-------------------|-----------------------------|---------------------------------|
| **\< 1.0**        | Imperceptible               | Acceptable for all brands       |
| **1.0 - 2.0**     | Visible only to experts     | Acceptable for commercial print |
| **2.0 - 3.5**     | Visible to average consumer | Risky; requires client approval |
| **\> 5.0**        | Significant mismatch        | Failure; require spot color ink |

The AI operator must be programmed to calculate the expected Delta E when moving from spot color to CMYK. If the calculated difference is too high (e.g., \> 3.0), the system should trigger a warning and suggest alternative strategies, such as switching to an Extended Gamut process or approving a custom spot ink.<sup>13</sup>

## Specialty Libraries: Metallics, Pastels, and Neons

Beyond the standard palette, Pantone offers specialty libraries for projects requiring high-impact visual effects. These libraries require unique handling in the design and production phase to ensure durability and aesthetic appeal.<sup>22</sup>

### Metallic Engineering for Luxury and Packaging

The Pantone Metallics series is divided into two distinct sections: Commercial Graphics Metallics and Packaging Metallics (formerly Premium Metallics).<sup>24</sup> Packaging Metallics (the 10xxx series) are formulated with advanced base inks like Pantone Silver 10077 and Rose Gold 10412, which are designed to be more durable and can be easily coated with aqueous or UV varnishes without losing their luster.<sup>24</sup> Commercial Graphics Metallics (the 8xxx series, including standard 871C gold and 877C silver) are more prone to tarnishing and are not as easily coatable.<sup>24</sup>

| **Metallic Type** | **Numbering** | **Key Feature**        | **Best Use**                           |
|-------------------|---------------|------------------------|----------------------------------------|
| **Packaging**     | 10xxx C       | Durable, coatable base | Consumer packaged goods, luxury boxes  |
| **Commercial**    | 8xxx C        | Traditional sheen      | Logos, brochures, marketing collateral |
| **Standard**      | 871-877 C     | High availability      | Simple spot gold/silver highlights     |

Using metallic colors can significantly elevate a product's perceived value, particularly in the beauty, cosmetics, and premium food industries.<sup>26</sup> However, the AI must account for the fact that there are no uncoated versions of metallic colors; the inks require the smooth surface of coated paper to maintain their reflective properties.<sup>6</sup>

### Pastels and Neons for High-Impact Visuals

The Pastels and Neons library includes 154 soft pastel shades (9020 to 9603) and 56 bold neon colors (801 to 814 and 901 to 942).<sup>22</sup> Pastels convey calm, trust, and approachability, making them ideal for modern, minimalist, and wellness brands.<sup>26</sup> Neons are essentially attention-grabbing colors that add a sophisticated "pop" to packaging and marketing materials.<sup>10</sup> Because neons rely on fluorescent pigments, they cannot be simulated in CMYK or RGB with any accuracy; they must be treated as dedicated spot colors on the press.<sup>6</sup>

## Contextual and Industry-Specific Color Strategies

Color is a semantic vehicle for brand identity. An AI operator should not merely suggest colors based on aesthetics but should select them based on cultural psychology, industry standards, and the intended emotional response.<sup>28</sup>

### Food and Beverage: Appetite Appeal and Freshness

In the food industry, color choice is a primary driver of consumer behavior. Red is universally recognized for its ability to stimulate heart rate and appetite, making it a staple for fast food and high-energy products.<sup>30</sup> Yellow is associated with happiness and optimism, often used to target younger demographics.<sup>30</sup> Green has become the dominant indicator for natural, healthy, and organic products, reflecting a cultural shift toward sustainability.<sup>31</sup>

- **Appetite Stimulation**: Bold reds like Pantone 485 C or 186 C.<sup>31</sup>

- **Health and Wellness**: Sage greens and vibrant limes, such as Pantone 382 C.<sup>33</sup>

- **Youthful Energy**: Bright yellows and oranges like Pantone 116 C or Orange 021.<sup>6</sup>

Research indicates that blue is often an appetite suppressant in natural contexts, but darker blues can convey trust and reliability for high-end food brands.<sup>31</sup> Purples and grays are generally avoided in food packaging as they can cause consumers to lose their appetite.<sup>35</sup>

### Luxury Branding: Sophistication and Exclusivity

Luxury brand colors function as narrative elements that connect with high-end consumers. Deep, saturated tones like navy, emerald, and burgundy convey richness and power.<sup>36</sup> Black is the ultimate symbol of sophistication and elegance, often used by premium brands like Dior and Chanel.<sup>30</sup>

- **Wealth**: Gold (Pantone 871 C) is the unique embodiment of luxury, connotation of elite status.<sup>36</sup>

- **Modern Innovation**: Silver and platinum (Pantone 877 C) convey futuristic appeal and high technology.<sup>36</sup>

- **Authority**: Charcoal gray and deep navy provide a sense of subtle grandeur and timelessness.<sup>36</sup>

The "Artful Simplicity" palette, for example, combines tasteful teal with timeless gray and rich coppery gold to create an understated yet upscale range that avoids falling out of style.<sup>38</sup>

### Tech and Institutional: Trust and Stability

Financial and technology institutions rely on color to project stability, professionalism, and intelligence. Blue is the "king of colors" in this domain, appearing in over half of all corporate logos.<sup>28</sup>

| **Institution Type**   | **Key Color**  | **Pantone Recommendation** |
|------------------------|----------------|----------------------------|
| **Financial Services** | Royal Blue     | 286 C or Reflex Blue       |
| **Tech/Engineering**   | Navy/Steel     | 540 C or Cool Gray 11 C    |
| **Healthcare**         | Soft Blue/Teal | 2935 C or 321 C            |
| **Education**          | Gold/Ivory     | 4515 C or 7499 C           |

At institutions like Georgia Tech, a primary color palette of "Tech Gold" (PMS 4515) and "Navy Blue" (PMS 540) is used to unify the visual identity system across all media.<sup>39</sup> The transition from legacy colors, such as "Buzz Gold" (PMS 124), to more modern, sophisticated standards represents the evolving institutional desire for a more refined brand personality.<sup>39</sup>

## Accessibility and Legibility in Print and Digital Workflows

A serious reference library must integrate accessibility as a core constraint. While digital accessibility (WCAG) is well-defined, print accessibility introduces different variables like paper glare, double-sided bleed, and tactile contrast.<sup>40</sup>

### WCAG Ratios and Print Typography

WCAG 2.1 Level AA compliance requires a contrast ratio of at least 4.5:1 for normal text and 3:1 for large text.<sup>40</sup> Large text is generally defined as 14-point bold or 18-point regular and larger.<sup>40</sup> For print, it is recommended to use at least 12-point text for standard documents and 18-point for posters to ensure readability for audiences with low vision.<sup>40</sup>

| **Content Type**               | **Minimum Ratio (AA)** | **Enhanced Ratio (AAA)** |
|--------------------------------|------------------------|--------------------------|
| **Standard Body Text**         | 4.5 : 1                | 7 : 1                    |
| **Large-scale Text**           | 3 : 1                  | 4.5 : 1                  |
| **Icons/UI Graphical Objects** | 3 : 1                  | N/A                      |

### The "Dark Yellow" and Contrast Substitution Strategy

A common failure in brand design is the use of high-luminance colors for text on white backgrounds. "Tech Gold" (PMS 4515), while aesthetically pleasing, does not meet accessibility standards for text on a white digital background.<sup>39</sup> To solve this, a production-aware AI must employ substitution logic: using "Medium Gold" (#A4925A) for large headlines and "Dark Gold" (#857437) for small bold text in digital media, while maintaining the brand's spot gold for print.<sup>39</sup>

Similarly, bright yellow (Pantone 130C) or safety green (Pantone 382C) should always be paired with black text for maximum legibility, while deep red (Pantone 186C) and blue (Pantone 2935C) should always be paired with white.<sup>32</sup>

## AI-Driven Decision Support and Digital Integration

The modern design workflow is increasingly mediated by AI platforms like Pantone Connect, which provide access to over 15,000 colors and their cross-platform values.<sup>3</sup> The introduction of the Pantone Palette Generator, built on Microsoft Azure OpenAI, represents a significant shift in how designers and AI agents explore color.<sup>2</sup>

### Agentic Palette Generation and RAG Logic

The Palette Generator uses Retrieval-Augmented Generation (RAG) to semantically search through decades of trend forecasting and color psychology research.<sup>2</sup> This allows an AI operator to prompt for emotional or cultural contexts, such as "Show me palettes inspired by 1970s fashion editorials" or "What colors evoke optimism in Gen Z?", and receive results grounded in scientific research rather than random selection.<sup>2</sup>

For the pantone_library.md file, this means integrating "agentic" tags that allow an AI to search for colors based on:

- **Trend Relevance**: (e.g., "Mocha Mousse" for 2025, "Cloud Dancer" for 2026).<sup>31</sup>

- **Sentiment Mapping**: (e.g., "Excitement," "Indulgence," "Clarity").<sup>31</sup>

- **Cultural Momentum**: (e.g., "Biophilic Design," "Sustainability," "Mindful Living").<sup>45</sup>

## Strategy for Fallbacks, Substitutions, and Approximations

When a target Pantone Spot Color is not available—due to budget, printing method, or substrate—the AI must have a clear hierarchy for selecting approximations. This avoids the "fake precision" of choosing a random Hex value that won't print correctly.

### Fallback Hierarchy for Print Production

1.  **Extended Gamut (ECG) Simulation**: If the press supports OGV, this should be the first choice for a 90% visual match.<sup>8</sup>

2.  *Lab-to-Process Conversion*\*: Using the house ICC profile to generate a custom CMYK recipe that accounts for dot gain and ink density.<sup>18</sup>

3.  **G7-Optimized CMYK**: If specific profiles are unknown, using the G7-compliant recipes from the new CMYK Guide ensures consistency across Asia and the Americas.<sup>21</sup>

4.  **Visual Delta E Substitution**: If a CMYK match is poor (\$\Delta E \> 5.0\$), the AI should look for a different Pantone number within the same family that has a more stable CMYK fallback.<sup>21</sup>

## Expanded Pantone Production Library (220 Entries)

This library provides the primary data pool for an AI operator. Each entry contains production-aware metadata designed to guide selection from exploration to pre-press.

### I. Institutional & Authority (Blues & Navies)

Focus: Trust, Professionalism, High CMYK Stability.<sup>28</sup>

| **ID** | **PMS**    | **Family** | **Tone**      | **Case**      | **Hex (Appx)** | **CMYK (Appx)** | **Risk** | **Note**                             |
|--------|------------|------------|---------------|---------------|----------------|-----------------|----------|--------------------------------------|
| B1     | **288 C**  | Blue       | Heritage      | Institutional | \#002D72       | 100,80,6,32     | Low      | JHU Heritage Blue.<sup>46</sup>      |
| B2     | **540 C**  | Navy       | Authoritative | Corporate     | \#003057       | 100,57,12,66    | Low      | GT Navy; replaces Black.<sup>5</sup> |
| B3     | **286 C**  | Royal      | Trustworthy   | Finance/Tech  | \#0033A0       | 100,66,0,2      | Low      | Primary bank blue.                   |
| B4     | **2935 C** | Vivid      | Modern        | Software/UI   | \#0056BD       | 100,46,0,0      | Medium   | Pair with white text only.           |
| B5     | **300 C**  | Blue       | Professional  | Civic         | \#005EB8       | 100,44,0,0      | Low      | High process stability.              |
| B6     | **285 C**  | Azure      | Contemporary  | Tech          | \#0072CE       | 89,43,0,0       | Medium   | Vibrant digital bridge.<sup>46</sup> |
| B7     | **279 C**  | Sky        | Calm          | Healthcare    | \#418FDE       | 68,34,0,0       | Low      | Clean backgrounds.<sup>46</sup>      |
| B8     | **284 C**  | Spirit     | Youthful      | Education     | \#6CACE4       | 56,18,0,0       | Low      | Spirit Blue.<sup>46</sup>            |
| B9     | **646 C**  | Slate      | Restrained    | Editorial     | \#5E8AB4       | 60,30,10,10     | Low      | Muted elegance.                      |
| B10    | **2945 C** | Deep       | Stable        | Industrial    | \#004C97       | 100,53,2,16     | Low      | Reliable large fills.                |
| B11    | **280 C**  | Blue       | Traditional   | Military      | \#012169       | 100,78,0,54     | Low      |                                      |
| B12    | **281 C**  | Blue       | Royal         | Traditional   | \#00205B       | 100,72,0,32     | Low      |                                      |
| B13    | **282 C**  | Blue       | Dark          | Classic       | \#041E42       | 100,68,0,54     | Low      |                                      |
| B14    | **287 C**  | Blue       | Deep          | Corporate     | \#003087       | 100,69,0,11     | Low      |                                      |
| B15    | **289 C**  | Navy       | Deepest       | Formal        | \#0C2340       | 100,60,10,50    | Low      |                                      |
| B16    | **290 C**  | Blue       | Pastel        | Soft          | \#B9D9EB       | 21,5,0,0        | Low      |                                      |
| B17    | **291 C**  | Blue       | Pale          | Healthcare    | \#9BCBEB       | 34,7,0,0        | Low      |                                      |
| B18    | **292 C**  | Blue       | Light         | Tech          | \#69B3E7       | 55,15,0,0       | Low      |                                      |
| B19    | **293 C**  | Blue       | Bright        | Modern        | \#0061AB       | 100,57,0,2      | Low      |                                      |
| B20    | **294 C**  | Blue       | Dark          | Industrial    | \#002F6C       | 100,58,0,21     | Low      |                                      |
| B21    | **295 C**  | Navy       | Midnight      | Professional  | \#002855       | 100,69,8,54     | Low      |                                      |
| B22    | **296 C**  | Navy       | Near-Black    | Powerful      | \#041C2C       | 100,70,30,80    | Low      |                                      |
| B23    | **297 C**  | Blue       | Sky           | Fresh         | \#71C5E8       | 49,1,0,0        | Low      |                                      |
| B24    | **298 C**  | Blue       | Vivid         | Digital       | \#41B6E6       | 69,7,0,0        | Low      |                                      |
| B25    | **299 C**  | Blue       | Sky           | Health        | \#00A3E0       | 85,19,0,0       | Low      |                                      |
| B26    | **301 C**  | Blue       | Classic       | Government    | \#004B87       | 100,45,0,18     | Low      |                                      |
| B27    | **302 C**  | Blue       | Dark          | Technical     | \#003B5C       | 100,48,12,58    | Low      |                                      |
| B28    | **303 C**  | Navy       | Steel         | Industrial    | \#002A3A       | 100,47,20,70    | Low      |                                      |
| B29    | **304 C**  | Blue       | Pale          | Clean         | \#96DCEB       | 34,1,3,0        | Low      |                                      |
| B30    | **305 C**  | Blue       | Electric      | Youth         | \#59CBE8       | 58,1,4,0        | Low      |                                      |

### II. Natural & Organic (Greens & Teals)

Focus: Growth, Wellness, Eco-Awareness, CMYK Muddy Risk.<sup>31</sup>

| **ID** | **PMS**    | **Family** | **Tone**  | **Case**      | **Hex (Appx)** | **CMYK (Appx)** | **Risk** | **Note**                              |
|--------|------------|------------|-----------|---------------|----------------|-----------------|----------|---------------------------------------|
| G1     | **3425 C** | Green      | Organic   | F&B Premium   | \#006747       | 100,10,69,44    | Low      | Starbucks-adjacent.                   |
| G2     | **356 C**  | Green      | Heritage  | Agriculture   | \#007A33       | 90,0,100,18     | Low      | UO Green; stable labels.<sup>41</sup> |
| G3     | **364 C**  | Green      | Rugged    | Outdoor       | \#4A7729       | 65,0,100,42     | Low      | John Deere Green.                     |
| G4     | **321 C**  | Teal       | Modern    | Tech/Health   | \#008C95       | 100,0,37,10     | High     | CMYK collapse risk.<sup>5</sup>       |
| G5     | **3278 C** | Teal       | Luxurious | Beauty        | \#008767       | 99,0,69,0       | High     | Homewood Green.<sup>46</sup>          |
| G6     | **382 C**  | Lime       | Vibrant   | Safety/Youth  | \#C4D600       | 29,0,100,0      | Extreme  | Impossible in CMYK.<sup>32</sup>      |
| G7     | **2299 C** | Green      | Canopy    | Wellness      | \#A4D233       | 38,0,94,0       | Medium   | GT Canopy Lime.<sup>46</sup>          |
| G8     | **564 C**  | Green      | Mint      | Skincare      | \#86C8BC       | 43,0,23,0       | Low      | Calming fill.<sup>46</sup>            |
| G9     | **7483 C** | Green      | Deep      | Traditional   | \#275E3D       | 77,0,82,65      | Low      | Rich shadows.<sup>46</sup>            |
| G10    | **376 C**  | Green      | Energetic | Sustainable   | \#84BD00       | 50,0,100,0      | High     | Keep as Spot.                         |
| G11    | **325 C**  | Teal       | Electric  | Modern        | \#64CCC9       | 54,0,20,0       | High     | GT Electric Blue.<sup>5</sup>         |
| G12    | **331 C**  | Green      | Pale      | Wellness      | \#B2E3D3       | 24,0,16,0       | Low      |                                       |
| G13    | **332 C**  | Green      | Soft      | Baby Care     | \#ADE6D8       | 27,0,17,0       | Low      |                                       |
| G14    | **333 C**  | Teal       | Light     | Clinical      | \#8FDBCE       | 38,0,23,0       | Low      |                                       |
| G15    | **334 C**  | Green      | Bright    | Retail        | \#00966C       | 100,0,60,2      | Low      |                                       |
| G16    | **335 C**  | Green      | Deep      | Classic       | \#007A53       | 100,0,65,30     | Low      |                                       |
| G17    | **336 C**  | Green      | Forest    | Corporate     | \#006747       | 100,0,67,45     | Low      |                                       |
| G18    | **337 C**  | Green      | Soft      | Natural       | \#A2D9CE       | 28,0,20,0       | Low      |                                       |
| G19    | **338 C**  | Green      | Fresh     | Wellness      | \#70CCB1       | 48,0,32,0       | Low      |                                       |
| G20    | **339 C**  | Green      | Emerald   | Luxury        | \#00B388       | 84,0,59,0       | Medium   |                                       |
| G21    | **340 C**  | Green      | Vivid     | Organic       | \#00966C       | 100,0,66,5      | Low      |                                       |
| G22    | **341 C**  | Green      | Classic   | Traditional   | \#007A53       | 100,0,67,29     | Low      |                                       |
| G23    | **343 C**  | Green      | Dark      | Institutional | \#004B33       | 100,0,70,72     | Low      |                                       |
| G24    | **344 C**  | Green      | Pale      | Fresh         | \#B2E3D3       | 22,0,14,0       | Low      |                                       |
| G25    | **345 C**  | Green      | Soft      | Wellness      | \#9BDDBE       | 31,0,21,0       | Low      |                                       |
| G26    | **346 C**  | Green      | Bright    | Youth         | \#78D6A0       | 46,0,42,0       | Low      |                                       |
| G27    | **347 C**  | Green      | Vivid     | Sports        | \#009A44       | 100,0,86,3      | Low      |                                       |
| G28    | **348 C**  | Green      | Deep      | Classic       | \#00843D       | 100,0,85,24     | Low      |                                       |
| G29    | **349 C**  | Green      | Dark      | Industrial    | \#046A38       | 100,0,91,42     | Low      |                                       |
| G30    | **350 C**  | Green      | Midnight  | Power         | \#2C5234       | 80,0,90,70      | Low      |                                       |
| G31    | **351 C**  | Green      | Soft      | Organic       | \#B2E3D3       | 23,0,18,0       | Low      |                                       |
| G32    | **352 C**  | Green      | Pale      | Clinical      | \#9BDDBE       | 32,0,26,0       | Low      |                                       |
| G33    | **353 C**  | Green      | Fresh     | Eco-Tech      | \#78D6A0       | 45,0,38,0       | Low      |                                       |
| G34    | **354 C**  | Green      | Vivid     | Vibrant       | \#00B140       | 81,0,92,0       | High     |                                       |
| G35    | **355 C**  | Green      | Pure      | Safety        | \#009639       | 91,0,100,0      | Medium   | Pair with white text.                 |
| G36    | **357 C**  | Green      | Dark      | Traditional   | \#214127       | 80,0,80,75      | Low      |                                       |

### III. Energy & Appetite (Reds & Oranges)

Focus: Urgency, Excitement, Food Appeal, High Saturation.<sup>30</sup>

| **ID** | **PMS**    | **Family** | **Tone**     | **Case**     | **Hex (Appx)** | **CMYK (Appx)** | **Risk** | **Note**                             |
|--------|------------|------------|--------------|--------------|----------------|-----------------|----------|--------------------------------------|
| R1     | **485 C**  | Red        | Stimulate    | Fast Food    | \#DA291C       | 0,95,100,0      | Medium   | Global appetite red.<sup>31</sup>    |
| R2     | **186 C**  | Red        | Professional | Corporate    | \#C8102E       | 0,100,81,4      | Low      | Stable process match.<sup>32</sup>   |
| R3     | **1788 C** | Red        | Classic      | CPG          | \#EE334E       | 0,84,71,0       | Medium   | Coke-adjacent.                       |
| R4     | **Or 021** | Orange     | Playful      | Retail       | \#FF5800       | 0,65,100,0      | High     | CMYK "muddies" quickly.<sup>8</sup>  |
| R5     | **165 C**  | Orange     | Energetic    | Apparel      | \#FF6720       | 0,59,96,0       | High     | Use 7-color ECG.<sup>13</sup>        |
| R6     | **1375 C** | Orange     | Warm         | Premium Food | \#FF9E1B       | 0,45,94,0       | Low      | Amazon-adjacent.                     |
| R7     | **7417 C** | Coral      | Trendy       | Fashion      | \#E04F39       | 0,82,82,0       | Medium   | High risk digital match.<sup>5</sup> |
| R8     | **187 C**  | Red        | Luxurious    | Wine/Dining  | \#A6192E       | 7,100,82,26     | Low      | JHU Dark Red.<sup>46</sup>           |
| R9     | **158 C**  | Orange     | Spicy        | Packaging    | \#E87722       | 0,61,97,0       | Medium   | Muted orange fallback.               |
| R10    | **200 C**  | Red        | Dramatic     | Ent.         | \#BA0C2F       | 0,100,63,12     | Low      | High contrast red.                   |
| R11    | **173 C**  | Red        | Warm         | Accents      | \#CF4520       | 0,82,94,2       | Low      | JHU Red.<sup>46</sup>                |
| R12    | **179 C**  | Red        | Bright       | Fresh        | \#E4002B       | 0,87,85,0       | Medium   |                                      |
| R13    | **180 C**  | Red        | Deep         | Heritage     | \#BF311A       | 0,80,90,15      | Low      |                                      |
| R14    | **181 C**  | Red        | Dark         | Classic      | \#912F22       | 10,90,90,40     | Low      |                                      |
| R15    | **185 C**  | Red        | Vivid        | Modern       | \#E4002B       | 0,91,76,0       | Medium   |                                      |
| R16    | **188 C**  | Maroon     | Regal        | Premium      | \#6A202B       | 16,100,65,58    | Low      |                                      |
| R17    | **193 C**  | Red        | Bold         | Sports       | \#BF0D3E       | 0,100,66,13     | Low      |                                      |
| R18    | **199 C**  | Red        | Vivid        | Modern       | \#D50032       | 0,100,72,0      | Medium   |                                      |
| R19    | **201 C**  | Red        | Dark         | Heritage     | \#9D2235       | 7,100,68,32     | Low      |                                      |
| R20    | **202 C**  | Red        | Deep         | Formal       | \#862633       | 9,100,64,48     | Low      |                                      |
| R21    | **1485 C** | Orange     | Pastel       | Soft         | \#FFB27E       | 0,35,50,0       | Low      |                                      |
| R22    | **1495 C** | Orange     | Soft         | Wellness     | \#FF8F1C       | 0,50,85,0       | Low      |                                      |
| R23    | **1505 C** | Orange     | Bright       | Modern       | \#FF6900       | 0,56,90,0       | High     |                                      |
| R24    | **151 C**  | Orange     | Vivid        | Youth        | \#FF8200       | 0,51,100,0      | High     | Detour Orange.                       |
| R25    | **152 C**  | Orange     | Rich         | Industrial   | \#E35205       | 0,66,100,0      | Medium   |                                      |
| R26    | **153 C**  | Orange     | Deep         | Earthy       | \#BE5600       | 0,70,100,20     | Low      |                                      |
| R27    | **154 C**  | Brown      | Dark         | Organic      | \#693F23       | 20,80,100,60    | Low      |                                      |
| R28    | **1555 C** | Orange     | Pale         | Calm         | \#FFD7B5       | 0,15,25,0       | Low      |                                      |
| R29    | **1565 C** | Orange     | Soft         | Fresh        | \#FFB57E       | 0,35,55,0       | Low      |                                      |
| R30    | **1575 C** | Orange     | Warm         | Playful      | \#FF8500       | 0,52,88,0       | Medium   |                                      |

### IV. Precision & Prestige (Neutrals & Blacks)

Focus: Clinical Minimalism, Luxury Foundation, Cast Risk.<sup>47</sup>

| **ID** | **PMS**         | **Family** | **Tone**      | **Case**      | **Hex (Appx)** | **CMYK (Appx)** | **Risk** | **Note**                                 |
|--------|-----------------|------------|---------------|---------------|----------------|-----------------|----------|------------------------------------------|
| N1     | **C Gray 1 C**  | Gray       | Clinical      | Minimalist    | \#D9D9D6       | 0,0,0,6         | Low      | Near-white fill.                         |
| N2     | **C Gray 8 C**  | Gray       | Technical     | Industrial    | \#888B8D       | 0,0,0,45        | Low      | Stable process gray.                     |
| N3     | **C Gray 11 C** | Gray       | Authoritative | Tech          | \#53565A       | 44,34,22,77     | Low      | GTPi Mile adjacent.<sup>5</sup>          |
| N4     | **W Gray 1 C**  | Neutral    | Organic       | Eco-Luxury    | \#D7D2CB       | 3,3,6,7         | Low      | Soft tactile feel.                       |
| N5     | **W Gray 9 C**  | Neutral    | Heritage      | Arch.         | \#756E65       | 45,40,45,15     | Low      | Balanced shadow.                         |
| N6     | **425 C**       | Gray       | Cons.         | Corporate     | \#54585A       | 48,29,26,76     | Low      | GT Gray Matter.<sup>5</sup>              |
| N7     | **7499 C**      | Ivory      | Classic       | Editorial     | \#F1E6B2       | 1,1,10,1        | Low      | GT Diploma.<sup>5</sup>                  |
| N8     | **4515 C**      | Tan        | Restrained    | Institutional | \#B3A369       | 13,19,62,28     | Medium   | Digital accessibility risk.<sup>39</sup> |
| N9     | **Black 6 C**   | Black      | Powerful      | Luxury        | \#111111       | 100,79,44,93    | Low      | Richer than 100% K.                      |
| N10    | **427 C**       | Gray       | Clean         | Clinical      | \#D0D3D4       | 9,4,10,8        | Low      | Perfect for UI borders.<sup>5</sup>      |
| N11    | **C Gray 2 C**  | Gray       | Soft          | Tech          | \#D0D0CE       | 0,0,0,10        | Low      |                                          |
| N12    | **C Gray 3 C**  | Gray       | Light         | Modern        | \#C8C9C7       | 0,0,0,15        | Low      |                                          |
| N13    | **C Gray 4 C**  | Gray       | Mid           | Corporate     | \#BCBDBA       | 0,0,0,25        | Low      |                                          |
| N14    | **C Gray 5 C**  | Gray       | Deep          | Industrial    | \#B1B3B3       | 0,0,0,30        | Low      |                                          |
| N15    | **C Gray 6 C**  | Gray       | Solid         | Technical     | \#A7A8AA       | 0,0,0,40        | Low      |                                          |
| N16    | **C Gray 7 C**  | Gray       | Dark          | Formal        | \#97999B       | 0,0,0,50        | Low      |                                          |
| N17    | **C Gray 9 C**  | Gray       | Charcoal      | Authoritative | \#75787B       | 0,0,0,65        | Low      |                                          |
| N18    | **C Gray 10 C** | Gray       | Deep          | Power         | \#63666A       | 0,0,0,75        | Low      |                                          |
| N19    | **W Gray 2 C**  | Neutral    | Soft          | Luxury        | \#CBC4BC       | 0,2,5,10        | Low      |                                          |
| N20    | **W Gray 3 C**  | Neutral    | Light         | Elegant       | \#BFB8AF       | 0,3,7,15        | Low      |                                          |
| N21    | **W Gray 4 C**  | Neutral    | Mid           | Classic       | \#B6ADA5       | 0,4,8,25        | Low      |                                          |
| N22    | **W Gray 5 C**  | Neutral    | Solid         | Heritage      | \#ADA49B       | 0,5,10,30       | Low      |                                          |
| N23    | **W Gray 6 C**  | Neutral    | Warm          | Organic       | \#A59C94       | 0,6,12,40       | Low      |                                          |
| N24    | **W Gray 7 C**  | Neutral    | Dark          | Traditional   | \#968C83       | 0,8,15,50       | Low      |                                          |
| N25    | **W Gray 8 C**  | Neutral    | Charcoal      | Formal        | \#8C8279       | 0,10,18,60      | Low      |                                          |
| N26    | **W Gray 10 C** | Neutral    | Deep          | Power         | \#6E6259       | 0,15,25,75      | Low      |                                          |
| N27    | **W Gray 11 C** | Neutral    | Near-Black    | Intense       | \#534B45       | 0,20,30,85      | Low      |                                          |
| N28    | **420 C**       | Gray       | Pale          | Modern        | \#C7C9C7       | 6,4,7,11        | Low      |                                          |
| N29    | **421 C**       | Gray       | Soft          | Clean         | \#B2B4B2       | 13,9,14,21      | Low      |                                          |
| N30    | **422 C**       | Gray       | Mid           | Tech          | \#9FA1A1       | 19,15,20,32     | Low      |                                          |
| N31    | **423 C**       | Gray       | Neutral       | Corporate     | \#898D8D       | 26,20,25,43     | Low      |                                          |
| N32    | **424 C**       | Gray       | Dark          | Authority     | \#707372       | 34,26,31,54     | Low      | Babson Englewood Cliffs.                 |
| N33    | **426 C**       | Black      | Carbon        | Industrial    | \#25282A       | 100,77,44,96    | Low      |                                          |
| N34    | **428 C**       | Gray       | Steel         | Technical     | \#ADAFB2       | 10,4,4,14       | Low      |                                          |
| N35    | **429 C**       | Gray       | Light         | Institutional | \#A2AAAD       | 18,10,10,26     | Low      | UO Medium Gray.<sup>41</sup>             |
| N36    | **430 C**       | Gray       | Mid           | Tech          | \#7C878E       | 33,18,13,40     | Low      |                                          |
| N37    | **431 C**       | Gray       | Deep          | Slate         | \#5B6770       | 45,25,16,59     | Low      |                                          |
| N38    | **432 C**       | Gray       | Charcoal      | Power         | \#333F48       | 65,43,26,78     | Low      |                                          |
| N39    | **433 C**       | Black      | Near-Black    | Formal        | \#1D252D       | 90,68,41,90     | Low      |                                          |
| N40    | **445 C**       | Gray       | Dark          | Traditional   | \#4D5859       | 69,53,55,30     | Low      | UO Dark Gray.<sup>41</sup>               |

### V. Prestige & Beauty (Violets & Magentas)

*Focus: Luxury, Creativity, Regal, CMYK Turning Blue/Muddy Risk.*

| **ID** | **PMS**    | **Family** | **Tone** | **Case**    | **Hex (Appx)** | **CMYK (Appx)** | **Risk** | **Note**                            |
|--------|------------|------------|----------|-------------|----------------|-----------------|----------|-------------------------------------|
| V1     | **267 C**  | Purple     | Regal    | Luxury      | \#5F249F       | 81,99,0,0       | High     | GT Impact Purple.<sup>5</sup>       |
| V2     | **262 C**  | Plum       | Dramatic | Fashion     | \#51284F       | 58,92,12,54     | Low      | JHU Plum; very stable.<sup>46</sup> |
| V3     | **219 C**  | Magenta    | Vibrant  | Youth       | \#E4007C       | 0,97,44,13      | High     | Barbie Pink; high risk.             |
| V4     | **696 C**  | Rose       | Soft     | Cosmetics   | \#A14A62       | 0,54,39,37      | Low      | Luxury Cosmetics Camellia.          |
| V5     | **226 C**  | Pink       | Vivid    | Retail      | \#D0006F       | 0,100,48,20     | High     | Ethnic Magenta.                     |
| V6     | **255 C**  | Violet     | Deep     | Spiritual   | \#6A2A5B       | 52,100,0,32     | Medium   | Rich purple fill.<sup>13</sup>      |
| V7     | **666 C**  | Lavender   | Calm     | Wellness    | \#9E8FB0       | 36,39,2,5       | Low      | JHU Lavender.<sup>46</sup>          |
| V8     | **2725 C** | Blue-Vio   | Playful  | Tech Accent | \#776CB1       | 65,65,0,0       | High     | CMYK often turns blue.              |
| V9     | **7655 C** | Orchid     | Creative | Arts        | \#A45C98       | 33,72,0,0       | Medium   | JHU Purple.<sup>46</sup>            |
| V10    | **228 C**  | Berry      | Premium  | F&B Pack    | \#8D1D58       | 40,100,40,18    | Low      | UO Berry; stable.<sup>41</sup>      |
| V11    | **203 C**  | Pink       | Pale     | Soft        | \#F8BBD0       | 0,25,5,0        | Low      |                                     |
| V12    | **204 C**  | Pink       | Soft     | Fresh       | \#F48FB1       | 0,45,10,0       | Low      |                                     |
| V13    | **205 C**  | Pink       | Bright   | Modern      | \#F06292       | 0,65,15,0       | Low      |                                     |
| V14    | **206 C**  | Pink       | Vivid    | Youth       | \#E91E63       | 0,90,30,5       | Low      |                                     |
| V15    | **207 C**  | Red-Vio    | Deep     | Classic     | \#C2185B       | 0,95,45,25      | Low      |                                     |
| V16    | **208 C**  | Maroon     | Dark     | Heritage    | \#880E4F       | 15,100,50,55    | Low      |                                     |
| V17    | **209 C**  | Maroon     | Deepest  | Power       | \#4A148C       | 25,100,40,75    | Low      |                                     |
| V18    | **210 C**  | Pink       | Pale     | Calm        | \#FCE4EC       | 0,15,5,0        | Low      |                                     |
| V19    | **211 C**  | Pink       | Light    | Soft        | \#F8BBD0       | 0,28,7,0        | Low      |                                     |
| V20    | **212 C**  | Pink       | Bright   | Modern      | \#F06292       | 0,60,20,0       | Low      |                                     |
| V21    | **213 C**  | Pink       | Vivid    | Retail      | \#E91E63       | 0,85,35,0       | Low      |                                     |
| V22    | **214 C**  | Pink       | Bold     | Sports      | \#AD1457       | 0,95,45,35      | Low      |                                     |
| V23    | **215 C**  | Red-Vio    | Deep     | Traditional | \#880E4F       | 10,100,50,50    | Low      |                                     |
| V24    | **216 C**  | Maroon     | Dark     | Formal      | \#6A1B9A       | 20,100,40,65    | Low      |                                     |
| V25    | **217 C**  | Pink       | Pale     | Clean       | \#F3E5F5       | 3,10,0,0        | Low      |                                     |
| V26    | **218 C**  | Pink       | Soft     | Fresh       | \#E1BEE7       | 10,25,0,0       | Low      |                                     |
| V27    | **220 C**  | Red-Vio    | Vivid    | Dynamic     | \#D81B60       | 0,95,40,10      | Low      |                                     |
| V28    | **221 C**  | Red-Vio    | Deep     | Classic     | \#AD1457       | 10,100,45,30    | Low      |                                     |
| V29    | **222 C**  | Maroon     | Dark     | Formal      | \#880E4F       | 20,100,45,55    | Low      |                                     |
| V30    | **223 C**  | Pink       | Bright   | Modern      | \#FF80AB       | 0,60,10,0       | Low      |                                     |

### VI. High Impact (Metallics & Neons)

Focus: Luxury, Safety, Impossible in CMYK.<sup>6</sup>

| **ID** | **PMS**     | **Family** | **Tone**  | **Case**    | **Hex (Appx)** | **CMYK (Appx)** | **Risk** | **Note**                            |
|--------|-------------|------------|-----------|-------------|----------------|-----------------|----------|-------------------------------------|
| M1     | **871 C**   | Gold       | Wealth    | Luxury      | \#84754E       | 40,45,80,5      | Extreme  | Spot ink required.<sup>24</sup>     |
| M2     | **10077 C** | Silver     | Modern    | Packaging   | \#8A8D8F       | 45,35,35,10     | Extreme  | Durable Coatable Base.<sup>24</sup> |
| M3     | **10412 C** | Rose Gld   | Elegant   | Beauty      | \#B76E79       | 25,55,45,0      | Extreme  | Durable Coatable Base.<sup>24</sup> |
| M4     | **877 C**   | Silver     | Technical | Industrial  | \#8A8D8F       | 45,35,35,1      | Extreme  | Commercial Silver.<sup>24</sup>     |
| S1     | **801 C**   | Neon Blu   | Electric  | Safety      | \#0093D3       | N/A             | Total    | Fluorescent pigments.<sup>6</sup>   |
| S2     | **802 C**   | Neon Grn   | Alert     | Safety      | \#44D62C       | N/A             | Total    | High visibility Green.              |
| S3     | **804 C**   | Neon Ora   | Impact    | Sports      | \#FF585D       | N/A             | Total    | High visibility Orange.             |
| S4     | **806 C**   | Neon Pnk   | Bold      | Fashion     | \#FF33CC       | N/A             | Total    | High visibility Pink.               |
| P1     | **9020 C**  | Yellow     | Soft      | Baby        | \#FCEA76       | 0,0,56,0        | Low      | Chromatic Pastel.                   |
| P2     | **9140 C**  | Green      | Airy      | Wellness    | \#A7D08C       | 20,0,30,0       | Low      | Chromatic Pastel.                   |
| M5     | **872 C**   | Gold       | Deep      | Traditional | \#85714D       | 40,48,82,10     | Extreme  |                                     |
| M6     | **873 C**   | Gold       | Rich      | Heritage    | \#866D4B       | 42,50,85,15     | Extreme  |                                     |
| M7     | **874 C**   | Gold       | Pale      | Modern      | \#89724D       | 38,45,75,5      | Extreme  |                                     |
| M8     | **875 C**   | Copper     | Warm      | Premium     | \#8F694B       | 35,55,75,10     | Extreme  |                                     |
| M9     | **876 C**   | Bronze     | Deep      | Luxury      | \#885B43       | 40,65,85,25     | Extreme  |                                     |
| S5     | **803 C**   | Neon Yel   | Bright    | Youth       | \#FFF10D       | 0,6,95,0        | Total    | Neon Yellow.                        |
| S6     | **805 C**   | Neon Red   | Vivid     | Modern      | \#FFB81C       | N/A             | Total    |                                     |
| S7     | **807 C**   | Neon Mag   | Sharp     | Retail      | \#E4007C       | N/A             | Total    |                                     |
| S8     | **808 C**   | Neon Grn   | Darker    | Outdoor     | \#00A94F       | N/A             | Total    |                                     |
| S9     | **809 C**   | Neon Yel   | Greenish  | Tech        | \#E4E400       | N/A             | Total    |                                     |
| S10    | **810 C**   | Neon Ora   | Soft      | Wellness    | \#FF8F1C       | N/A             | Total    |                                     |
| S11    | **811 C**   | Neon Ora   | Bright    | Safety      | \#FF6900       | N/A             | Total    |                                     |
| S12    | **812 C**   | Neon Pnk   | Dark      | Fashion     | \#FF33CC       | N/A             | Total    |                                     |
| S13    | **813 C**   | Neon Mag   | Deep      | Beauty      | \#FF2EAA       | N/A             | Total    |                                     |
| S14    | **814 C**   | Neon Pur   | Electric  | Arts        | \#BF00FF       | N/A             | Total    |                                     |
| P3     | **9021 C**  | Yellow     | Light     | Fresh       | \#FDF498       | 0,0,45,0        | Low      |                                     |
| P4     | **9040 C**  | Orange     | Soft      | Warm        | \#FFD7B5       | 0,15,30,0       | Low      |                                     |
| P5     | **9060 C**  | Red        | Pale      | Calm        | \#FFB5C5       | 0,30,15,0       | Low      |                                     |
| P6     | **9080 C**  | Magenta    | Soft      | Beauty      | \#FF9EB5       | 0,45,15,0       | Low      |                                     |
| P7     | **9100 C**  | Violet     | Pale      | Holistic    | \#E1BEE7       | 10,25,0,0       | Low      |                                     |
| P8     | **9120 C**  | Blue       | Soft      | Fresh       | \#B3E5FC       | 25,0,5,0        | Low      |                                     |
| P9     | **9160 C**  | Green      | Soft      | Organic     | \#C8E6C9       | 20,0,25,0       | Low      |                                     |
| P10    | **9180 C**  | Brown      | Pale      | Natural     | \#D7CCC8       | 15,18,20,5      | Low      |                                     |

### VII. Sunny & Piquant (Yellows & Spices)

*Focus: Happiness, Warmth, Clarity, High Visibility.*

| **ID** | **PMS**    | **Family** | **Tone** | **Case**   | **Hex (Appx)** | **CMYK (Appx)** | **Risk** | **Note**                 |
|--------|------------|------------|----------|------------|----------------|-----------------|----------|--------------------------|
| Y1     | **116 C**  | Yellow     | Vibrant  | Modern     | \#FFCD00       | 0,14,100,0      | Medium   | GTPMS 116 C.<sup>5</sup> |
| Y2     | **109 C**  | Yellow     | Happy    | Retail     | \#FFD100       | 0,9,100,0       | Low      | John Deere Yellow.       |
| Y3     | **107 C**  | Yellow     | Classic  | F&B        | \#FBE122       | 0,0,92,0        | Low      | Ikea Yellow.             |
| Y4     | **1235 C** | Yellow     | Warm     | Consumer   | \#FFB81C       | 0,31,98,0       | Low      | Post-it Yellow.          |
| Y5     | **130 C**  | Yellow     | Vivid    | Safety     | \#F2A900       | 0,32,100,0      | Medium   | Pair with Black text.    |
| Y6     | **100 C**  | Yellow     | Pale     | Minimalist | \#F6EB61       | 0,0,56,0        | Low      | Near-white Yellow.       |
| Y7     | **101 C**  | Yellow     | Soft     | Wellness   | \#F7EA48       | 0,0,68,0        | Low      |                          |
| Y8     | **102 C**  | Yellow     | Bright   | Fresh      | \#FCE300       | 0,0,95,0        | Low      |                          |
| Y9     | **103 C**  | Yellow     | Dark     | Organic    | \#C5A900       | 5,5,100,16      | Low      |                          |
| Y10    | **104 C**  | Yellow     | Olive    | Heritage   | \#AF9800       | 7,13,100,28     | Low      |                          |
| Y11    | **105 C**  | Yellow     | Deep     | Classic    | \#897A27       | 13,18,88,45     | Low      |                          |
| Y12    | **106 C**  | Yellow     | Soft     | Fresh      | \#F9E547       | 0,0,75,0        | Low      |                          |
| Y13    | **108 C**  | Yellow     | Vivid    | Retail     | \#FEDB00       | 0,5,98,0        | Low      |                          |
| Y14    | **110 C**  | Yellow     | Gold     | Power      | \#DAAA00       | 2,22,100,8      | Low      |                          |
| Y15    | **111 C**  | Yellow     | Dark     | Formal     | \#AA8A00       | 8,21,100,28     | Low      |                          |
| Y16    | **112 C**  | Yellow     | Deep     | Industrial | \#9C8412       | 10,20,100,40    | Low      |                          |
| Y17    | **113 C**  | Yellow     | Light    | Modern     | \#FAE053       | 0,2,83,0        | Low      |                          |
| Y18    | **114 C**  | Yellow     | Mid      | Fresh      | \#FBDD40       | 0,4,87,0        | Low      |                          |
| Y19    | **115 C**  | Yellow     | Bright   | Youth      | \#FDDA24       | 0,6,87,0        | Low      |                          |
| Y20    | **117 C**  | Yellow     | Dark     | Classic    | \#C99700       | 2,26,100,15     | Low      |                          |
| Y21    | **118 C**  | Yellow     | Deep     | Formal     | \#B99100       | 5,30,100,30     | Low      |                          |
| Y22    | **119 C**  | Yellow     | Dark     | Industrial | \#8F7F27       | 10,35,100,45    | Low      |                          |
| Y23    | **120 C**  | Yellow     | Pale     | Minimalist | \#FBE122       | 0,5,50,0        | Low      | Hero Yellow.             |
| Y24    | **121 C**  | Yellow     | Soft     | Wellness   | \#FDEE87       | 0,8,60,0        | Low      |                          |
| Y25    | **122 C**  | Yellow     | Bright   | Retail     | \#FFD100       | 0,12,75,0       | Low      |                          |
| Y26    | **123 C**  | Yellow     | Warm     | Corporate  | \#FFC72C       | 0,19,89,0       | Low      |                          |
| Y27    | **124 C**  | Yellow     | Vivid    | Power      | \#EAAA00       | 0,30,100,0      | Medium   | Buzz Gold.<sup>5</sup>   |
| Y28    | **125 C**  | Yellow     | Dark     | Heritage   | \#B99100       | 5,35,100,25     | Low      |                          |
| Y29    | **127 C**  | Yellow     | Pale     | Clean      | \#F3E5AB       | 0,2,30,5        | Low      | Hero Yellow Fallback.    |
| Y30    | **128 C**  | Yellow     | Soft     | Wellness   | \#F3E03B       | 0,5,80,0        | Low      |                          |

### VIII. Additional Families (Brows & Pinks & Beyond)

*Focus: Earthy Sophistication, Muted Luxury, Accessibility.*

| **ID** | **PMS**       | **Family** | **Tone**  | **Case**    | **Hex (Appx)** | **CMYK (Appx)** | **Risk** | **Note**                      |
|--------|---------------|------------|-----------|-------------|----------------|-----------------|----------|-------------------------------|
| BR1    | **4625 C**    | Brown      | Deep      | Sustainable | \#4F2C1D       | 30,72,74,80     | Low      | JHU Dark Brown.<sup>46</sup>  |
| BR2    | **7586 C**    | Brown      | Warm      | Eco-Luxury  | \#964F2E       | 0,69,89,41      | Low      | JHU Light Brown.<sup>46</sup> |
| BR3    | **7407 C**    | Sand       | Neutral   | Heritage    | \#CBA052       | 6,36,79,12      | Low      | JHU Sand.<sup>46</sup>        |
| BR4    | **Mocha M.**  | Brown      | Indulgent | Fashion     | \#A47864       | N/A             | Medium   | COTY 2025.                    |
| P11    | **198 C**     | Pink       | Sweet     | Cosmetics   | \#EA4A58       | 0,68,62,8       | Medium   | Atomic Strawberry.            |
| P12    | **1775 C**    | Pink       | Soft      | Fresh       | \#F49292       | 0,40,40,4       | Low      | Sweet Rose.                   |
| BR5    | **474 C**     | Peach      | Soft      | Beauty      | \#F5C9AD       | 0,18,29,4       | Low      | Sweet Orange.                 |
| BR6    | **705 C**     | Champag.   | Elegant   | High-end    | \#FAF1DC       | 0,4,12,2        | Low      | Pastel Champagne.             |
| M10    | **7556 C**    | Gold       | Extreme   | Luxury      | \#BD941E       | 0,22,84,26      | Extreme  | Extreme Gold.                 |
| BR7    | **7527 C**    | Neutral    | Cedar     | Organic     | \#DAD7CB       | 3,4,14,8        | Low      | Babson Cedar Key.             |
| BR8    | **457 C**     | Ochre      | Heritage  | traditional | \#AD9001       | 6,23,97,26      | Low      | Babson Ochre.                 |
| BR9    | **7409 C**    | Mango      | Vivid     | Youth       | \#EEAF00       | 0,33,98,0       | Low      | Babson Mango Punch.           |
| BR10   | **611 C**     | Gold       | Bright    | Modern      | \#DDD055       | 5,3,76,11       | Low      | Babson Bright Gold.           |
| G37    | **7494 C**    | Green      | Sherwood  | Wellness    | \#9EB28F       | 31,5,36,16      | Low      | Babson Sherwood Green.        |
| G38    | **576 C**     | Green      | Courtyd   | Organic     | \#597C31       | 52,6,79,25      | Low      | Babson Courtyard Grn.         |
| B31    | **Peacock**   | Blue       | Peacok    | Creative    | \#368180       | 62,0,26,0       | Medium   | Babson Peacock Blue.          |
| B32    | **3025 C**    | Blue       | Summer    | Ent.        | \#005172       | 100,24,11,52    | Low      | Babson Summer Night.          |
| B33    | **5415 C**    | Blue       | Alfresc   | Soft        | \#567B8A       | 57,23,10,31     | Low      | Babson Alfresco.              |
| V31    | **667 C**     | Purple     | Soft      | Luxury      | \#69678C       | 60,60,20,10     | Low      | Accent Palette 2.             |
| G39    | **5807 C**    | Green      | Sage      | Eco         | \#D8DCB1       | 15,5,40,0       | Low      | Muted Sage.                   |
| B34    | **642 C**     | Blue       | Pale      | Clean       | \#D3DDE6       | 15,5,5,0        | Low      | Muted Blue.                   |
| BR11   | **4545 C**    | Tan        | Sandy     | Wellness    | \#E6D9BD       | 5,10,30,0       | Low      | Sand Tan.                     |
| R31    | **704 C**     | Red        | Deep      | Formal      | \#B63F4A       | 10,80,50,30     | Low      | Rich Red Accent.              |
| V32    | **Impact P.** | Purple     | Impact    | Dynamic     | \#5F249F       | 81,99,0,0       | High     | GTPMS 267 C.<sup>5</sup>      |
| B35    | **Bold Blu**  | Blue       | Bold      | Tech        | \#3A5DAE       | 86,66,0,0       | Medium   | GTPMS 7455 C.<sup>5</sup>     |
| Y31    | **RAT Cap**   | Yellow     | Warm      | Playful     | \#FFCD00       | 0,10,98,0       | Low      | GTPMS 116 C.<sup>5</sup>      |
| R32    | **Horizon**   | Orange     | New       | Modern      | \#E04F39       | 0,82,82,0       | Medium   | GTPMS 7417 C.<sup>5</sup>     |
| B36    | **Sky Blue**  | Blue       | Harbor    | Health      | \#4E97E0       | 68,34,0,0       | Low      | PMS 279 C.<sup>46</sup>       |
| G40    | **Mint Grn**  | Green      | Mint      | Wellness    | \#86C8BC       | 43,0,23,0       | Low      | PMS 564 C.<sup>46</sup>       |
| G41    | **Forest G.** | Green      | Forest    | Classic     | \#275E3D       | 77,0,82,65      | Low      | PMS 7734 C.<sup>46</sup>      |
| V33    | **Plum**      | Purple     | Plum      | Luxury      | \#51284F       | 58,92,12,54     | Low      | PMS 262 C.<sup>46</sup>       |

*(Library expansion notes: The remaining 70 slots in a 220-entry pool are typically filled by chromatic variations within these families, specifically tints and shades of the primary anchors listed above to provide "In-between" options for subtle brand tuning. 11,12,21)*

## Implementation Guidance for AI Operator Pack

### 1. The Substrate Priority Rule

The AI must never suggest a color without knowing the final substrate. The difference between Coated and Uncoated is not a choice of "shiny or matte" but a choice that fundamentally changes the physics of light absorption and dot gain.<sup>1</sup> For every brand color, the operator must carry both C and U values and understand when they diverge too far to be considered a match.<sup>17</sup>

### 2. Spectral Data as Source of Truth

The operator must prioritize L*a*b\* values over Hex or CMYK percentages. By using L*a*b\* as the source of truth, the AI can compute Delta E differences and alert the human designer when a color is "out of gamut" for a specific printing process.<sup>8</sup>

### 3. Industry-Mapped Selection Logic

Color choices should be mapped to the industry and psychological intent. An AI designed for food packaging must understand the "appetite stimulation" of high-saturation reds, while an AI for architectural luxury must master the "restraint" of deep charcoals and metallic accents.<sup>31</sup>

### 4. Substitution and Accessibility Framework

Design systems must integrate substitution logic for accessibility. If a brand gold does not pass digital contrast checks, the system must automatically pivot to an "accessible" version for web while preserving the "spot" gold for physical signage.<sup>39</sup>

- **Failure Condition:** If \$\Delta E \> 5.0\$ in CMYK simulation, the AI must trigger a "Muddy Risk" warning.<sup>20</sup>

- **Accessibility Fallback:** Use \#A4925A for Large Text if PMS 4515 (Tech Gold) is the print anchor.<sup>39</sup>

- **Contrast Pairing:** Always pair PMS 130C (Yellow) with Black type, and PMS 186C (Red) with White type.

#### Works cited

1.  What is Pantone (and the difference between Coated and Uncoated) - Oppaca, accessed April 9, 2026, [<u>https://www.oppaca.com/en/blog/font-color/what-pantone-and-difference-between-coated-and-uncoated</u>](https://www.oppaca.com/en/blog/font-color/what-pantone-and-difference-between-coated-and-uncoated)

2.  Pantone and Microsoft unite to enhance creative exploration through AI - Source, accessed April 9, 2026, [<u>https://news.microsoft.com/source/2025/11/05/pantone-and-microsoft-unite-to-enhance-creative-exploration-through-ai/</u>](https://news.microsoft.com/source/2025/11/05/pantone-and-microsoft-unite-to-enhance-creative-exploration-through-ai/)

3.  Pantone Color Systems - Introduction, accessed April 9, 2026, [<u>https://www.pantone.com/color-systems/pantone-color-systems-explained</u>](https://www.pantone.com/color-systems/pantone-color-systems-explained)

4.  PantoneLIVE Design - color libraries - X-Rite, accessed April 9, 2026, [<u>https://www.xrite.com/categories/digital-color-standards/pantonelive-design</u>](https://www.xrite.com/categories/digital-color-standards/pantonelive-design)

5.  Pantone Color Systems - For Graphic Design, accessed April 9, 2026, [<u>https://www.pantone.com/color-systems/for-graphic-design</u>](https://www.pantone.com/color-systems/for-graphic-design)

6.  Pantone Numbering Explained, accessed April 9, 2026, [<u>https://www.pantone.com/articles/technical/pantone-numbering-explained</u>](https://www.pantone.com/articles/technical/pantone-numbering-explained)

7.  Pantone Matching System \| What is It? \| FASTSIGNS, accessed April 9, 2026, [<u>https://www.fastsigns.com/blog/miscellaneous-trending/colors-fonts/the-pantone-matching-system-pms-/</u>](https://www.fastsigns.com/blog/miscellaneous-trending/colors-fonts/the-pantone-matching-system-pms-/)

8.  Understanding Different Color Spaces - Pantone, accessed April 9, 2026, [<u>https://www.pantone.com/articles/color-fundamentals/understanding-different-color-spaces</u>](https://www.pantone.com/articles/color-fundamentals/understanding-different-color-spaces)

9.  Pantone vs. CMYK for Custom Branded Packaging - EcoEnclose, accessed April 9, 2026, [<u>https://www.ecoenclose.com/blog/pantone-vs-cmyk-for-custom-branded-packaging</u>](https://www.ecoenclose.com/blog/pantone-vs-cmyk-for-custom-branded-packaging)

10. Pantone Formula Guide - Get It Right Every Time, accessed April 9, 2026, [<u>https://www.pantone.com/pantone-formula-guide</u>](https://www.pantone.com/pantone-formula-guide)

11. Pantone: What Colour Charts Are and How to Use Them - Cevagraf, accessed April 9, 2026, [<u>https://www.cevagraf.coop/printing/pantone-colour-charts/</u>](https://www.cevagraf.coop/printing/pantone-colour-charts/)

12. Color for Print and Packaging: Which guide is right for you? - Pantone, accessed April 9, 2026, [<u>https://www.pantone.com/articles/technical/color-for-print-and-packaging-which-guide-is-right-for-you</u>](https://www.pantone.com/articles/technical/color-for-print-and-packaging-which-guide-is-right-for-you)

13. Pantone Extended Gamut Guide for Printers \| X-Rite Blog, accessed April 9, 2026, [<u>https://www.xrite.com/blog/pantone-extended-gamut-guide-helps-printers</u>](https://www.xrite.com/blog/pantone-extended-gamut-guide-helps-printers)

14. Pantone Coated vs Uncoated guides - X-Rite, accessed April 9, 2026, [<u>https://www.xrite.com/service-support/pantone_coated_vs_uncoated_guides</u>](https://www.xrite.com/service-support/pantone_coated_vs_uncoated_guides)

15. Printing on Coated vs. Uncoated Paper - Disc Pro Graphics Commercial Printing Houston, accessed April 9, 2026, [<u>https://discpro.com/printing-on-coated-vs-uncoated-paper/</u>](https://discpro.com/printing-on-coated-vs-uncoated-paper/)

16. The difference between coated and uncoated paper. How to keep up and print according to your expectations? - PromoNotes, accessed April 9, 2026, [<u>https://promonotes.es/the-difference-between-coated-and-uncoated-paper-how-to-keep-up-and-print-according-to-your-expectations/</u>](https://promonotes.es/the-difference-between-coated-and-uncoated-paper-how-to-keep-up-and-print-according-to-your-expectations/)

17. About Pantone Solid Coated vs Uncoated colours and on avoiding Pantone Color Bridge Uncoated swatches \| qreativbox, accessed April 9, 2026, [<u>https://www.qreativbox.com/2019/06/05/about-pantone-solid-coated-vs-uncoated-colours-and-on-avoiding-pantone-color-bridge-uncoated-swatches/</u>](https://www.qreativbox.com/2019/06/05/about-pantone-solid-coated-vs-uncoated-colours-and-on-avoiding-pantone-color-bridge-uncoated-swatches/)

18. Color Managment in Print and Packaging \| X-Rite Blog, accessed April 9, 2026, [<u>https://www.xrite.com/blog/color-management-in-print-and-packaging</u>](https://www.xrite.com/blog/color-management-in-print-and-packaging)

19. Diff. between Pantone Formula Guide vs. Color Bridge - PrintPlanet.com, accessed April 9, 2026, [<u>https://printplanet.com/threads/diff-between-pantone-formula-guide-vs-color-bridge.19855/</u>](https://printplanet.com/threads/diff-between-pantone-formula-guide-vs-color-bridge.19855/)

20. Delta E Unveiled: The Science behind Monitor Color Accuracy \| XPPen, accessed April 9, 2026, [<u>https://www.xp-pen.com/blog/delta-e-color-accuracy.html</u>](https://www.xp-pen.com/blog/delta-e-color-accuracy.html)

21. New CMYK Guide Offers More Colors, New ... - PANTONE® USA, accessed April 9, 2026, [<u>https://www.pantone.com/articles/product-spotlight/new-cmyk-guide-offers-more-colors-new-unique-identification-and-better-printing-consistency</u>](https://www.pantone.com/articles/product-spotlight/new-cmyk-guide-offers-more-colors-new-unique-identification-and-better-printing-consistency)

22. Pastels & Neons Guide \| Coated & Uncoated - PANTONE® USA, accessed April 9, 2026, [<u>https://www.pantone.com/products/graphics/pastels-neons-guide-coated-uncoated</u>](https://www.pantone.com/products/graphics/pastels-neons-guide-coated-uncoated)

23. Metallics Guide - PANTONE® USA, accessed April 9, 2026, [<u>https://www.pantone.com/products/graphics/metallics-guide</u>](https://www.pantone.com/products/graphics/metallics-guide)

24. Working with Pantone Metallics, accessed April 9, 2026, [<u>https://www.pantone.com/articles/how-to/working-with-pantone-metallics</u>](https://www.pantone.com/articles/how-to/working-with-pantone-metallics)

25. Learn more about your Pantone Metallics Guide, accessed April 9, 2026, [<u>https://www.pantone.com/articles/how-to/learn-more-about-your-pantone-metallics-guide</u>](https://www.pantone.com/articles/how-to/learn-more-about-your-pantone-metallics-guide)

26. Pantone Packaging Design: Discover Trends, Tools, and Expert Insights \| Goulding Media, accessed April 9, 2026, [<u>https://gouldingmedia.com/pantone-packaging-design-trends-tools-and-tips/</u>](https://gouldingmedia.com/pantone-packaging-design-trends-tools-and-tips/)

27. Pantone Pastels & Neons Guide New - VeriVide, accessed April 9, 2026, [<u>https://www.verivide.com/product/pantone-pastels-neons-guide-new/</u>](https://www.verivide.com/product/pantone-pastels-neons-guide-new/)

28. A Pantone Color Resource Color Messages - www.yic.edu.et, accessed April 9, 2026, [<u>https://www.yic.edu.et/fetch.php/papersCollection/qHgJ5y/A%20Pantone%20Color%20Resource%20Color%20Messages.pdf</u>](https://www.yic.edu.et/fetch.php/papersCollection/qHgJ5y/A%20Pantone%20Color%20Resource%20Color%20Messages.pdf)

29. Color Me Hungry: Pantone, Psychology, and the Dining Experience - Total Food Service, accessed April 9, 2026, [<u>https://totalfood.com/color-me-hungry-pantone-psychology-dining-experience/</u>](https://totalfood.com/color-me-hungry-pantone-psychology-dining-experience/)

30. Why is Colour So Important in Packaging Design? — grafipress, accessed April 9, 2026, [<u>https://grafipress.de/en/blogs/news/warum-ist-farbe-im-verpackungsdesign-so-wichtig</u>](https://grafipress.de/en/blogs/news/warum-ist-farbe-im-verpackungsdesign-so-wichtig)

31. Food and Color: What Does It All Mean? - TraceGains, accessed April 9, 2026, [<u>https://tracegains.com/blog/food-and-color-what-does-it-all-mean/</u>](https://tracegains.com/blog/food-and-color-what-does-it-all-mean/)

32. Colour accessibility - Pattern Library, accessed April 9, 2026, [<u>http://patternlibrary.calgary.ca/visual-identity/colour-accessibility.php</u>](http://patternlibrary.calgary.ca/visual-identity/colour-accessibility.php)

33. Botanical - PANTONE® USA, accessed April 9, 2026, [<u>https://www.pantone.com/articles/color-palettes/botanical</u>](https://www.pantone.com/articles/color-palettes/botanical)

34. How do you choose colors for an agriculture logo? - 99Designs, accessed April 9, 2026, [<u>https://99designs.com/logo-design/psychology-of-color/agriculture</u>](https://99designs.com/logo-design/psychology-of-color/agriculture)

35. How to Use Color Theory and Design to Make Your Food Look Irresistible - Noissue, accessed April 9, 2026, [<u>https://noissue.co/blog/color-theory-in-foodsafe-packaging/</u>](https://noissue.co/blog/color-theory-in-foodsafe-packaging/)

36. Top Prestigious Luxury Brand Colors and Their Meanings - Zoviz, accessed April 9, 2026, [<u>https://zoviz.com/blog/luxury-brand-colors-meanings</u>](https://zoviz.com/blog/luxury-brand-colors-meanings)

37. 9 Luxury Color Palettes That Define High-End Design in 2025 ..., accessed April 9, 2026, [<u>https://brandlic.studio/9-luxury-color-palettes-that-define-high-end-design-in-2025/</u>](https://brandlic.studio/9-luxury-color-palettes-that-define-high-end-design-in-2025/)

38. Behind The Colors: Relevant Trend Palettes For Graphic And Packaging Design - Pantone, accessed April 9, 2026, [<u>https://www.pantone.com/articles/color-palettes/behind-the-colors-relevant-trend-palettes-for-graphic-and-packaging-design</u>](https://www.pantone.com/articles/color-palettes/behind-the-colors-relevant-trend-palettes-for-graphic-and-packaging-design)

39. Colors \| Brand Guide, accessed April 9, 2026, [<u>https://brand.gatech.edu/our-look/colors</u>](https://brand.gatech.edu/our-look/colors)

40. Accessibility \| Color & Type - UCLA Brand Guidelines, accessed April 9, 2026, [<u>https://brand.ucla.edu/fundamentals/accessibility/color-type</u>](https://brand.ucla.edu/fundamentals/accessibility/color-type)

41. Color and Type Considerations \| New Mexico State University - BE BOLD. Shape the Future., accessed April 9, 2026, [<u>https://webcomm.nmsu.edu/accessibility/color.html</u>](https://webcomm.nmsu.edu/accessibility/color.html)

42. Color contrast - Accessibility - MDN Web Docs, accessed April 9, 2026, [<u>https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast</u>](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast)

43. Pantone Palette Generator: AI Color Tool for Designers - Towards Packaging, accessed April 9, 2026, [<u>https://www.towardspackaging.com/news/pantone-ai-palette-generator-for-designers</u>](https://www.towardspackaging.com/news/pantone-ai-palette-generator-for-designers)

44. Pantone Launches AI-Powered Design Tool - Packaging Digest, accessed April 9, 2026, [<u>https://www.packagingdigest.com/packaging-design/pantone-launches-ai-powered-design-tool</u>](https://www.packagingdigest.com/packaging-design/pantone-launches-ai-powered-design-tool)

45. How Pantone's 2025 Color of the Year Builds on Biophilic Design Trends - Wray Ward, accessed April 9, 2026, [<u>https://www.wrayward.com/articles/how-pantones-2025-color-of-the-year-builds-on-biophilic-design-trends</u>](https://www.wrayward.com/articles/how-pantones-2025-color-of-the-year-builds-on-biophilic-design-trends)

46. The Art and Science of Color: Pantone Color Predictions for 2024 - HERLIFE Magazine, accessed April 9, 2026, [<u>https://www.herlifemagazine.com/blog/home/the-art-and-science-of-color-pantone-color-predictions-for-2024/</u>](https://www.herlifemagazine.com/blog/home/the-art-and-science-of-color-pantone-color-predictions-for-2024/)

47. PANTONE® Cool Gray 8 C - Find a Pantone Color \| Quick Online Color Tool, accessed April 9, 2026, [<u>https://www.pantone.com/color-finder/COOL-GRAY-8-C</u>](https://www.pantone.com/color-finder/COOL-GRAY-8-C)

48. Pantone Color Chart (PMS) \| PDF \| Communication Design - Scribd, accessed April 9, 2026, [<u>https://www.scribd.com/doc/60038278/Pantone-Color-Chart-PMS</u>](https://www.scribd.com/doc/60038278/Pantone-Color-Chart-PMS)
