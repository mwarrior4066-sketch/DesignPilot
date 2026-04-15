# Strict Graphic Design Expert for DesignPilot

## Research foundations and standards base

A “strict graphic design expert” for production work is less a style oracle than a decision system that repeatedly answers: what must be perceived, by whom, at what distance/time, under what brand constraints, with what tolerance for ambiguity. The highest-leverage research for such a system clusters into three kinds of sources:

Perception & legibility standards (measurable constraints).
When the medium is viewed at distance or under time pressure, typography and contrast stop being taste and become physics + human vision. The contrast ratio thresholds in the W3C[1] Web Content Accessibility Guidelines (WCAG) specify 4.5:1 for normal text and 3:1 for large text (AA), with 7:1 and 4.5:1 (AAA). WCAG also specifies that logotypes are exempt from the contrast requirement. [2] WebAIM summarizes the same thresholds and clarifies what “large text” means in practice (e.g., 18pt regular, 14pt bold). [3]

For distance-driven environments, signage research provides direct “distance → letter height” models. The Federal Highway Administration[4] MUTCD recommends a minimum ratio of 1 inch of letter height per 30 feet of legibility distance for word messages. [5] The United States Sign Council Foundation[6] formalizes this as a Legibility Index (feet per inch of capital letter height), gives a practical computation (VRD / LI = letter height), and documents that ALL CAPS requires ~15% more letter height than mixed case with initial caps. [7]

For a deeper optical basis, the Gerald L. Howett[8] National Bureau of Standards report ties legibility to visual angle and “critical detail” (stroke width), noting that for “20/20 vision at 20 feet,” a stroke width of 1 minute of arc is required, and Snellen letter height corresponds to 5 minutes of arc (with more typical letter styles potentially requiring more). [9]

Communication structure & typographic composition (operational layout rules).
Classic typography sources are unusually actionable because they encode design as constraints and measurable “measures” (line length, spacing, rhythm). Robert Bringhurst[10]’s Elements of Typographic Style is commonly cited for a comfortable single-column line length of ~45–75 characters. [11] Matthew Butterick[12]’s Practical Typography provides similarly operational thresholds: line spacing 120–145% of point size and average line length 45–90 characters. [13] Emil Ruder[14] emphasizes readability as a first principle, stating that “lines of more than sixty letters are difficult to read” and that spacing between words/characters/lines must be proportioned judiciously. [15]

System-led identity implementation (how brands become repeatable).
Brand systems become “production-level” when they provide measurable constraints: clear space, minimum size, permitted variants, color specs, and deployment logic across contexts. NASA[16] explicitly frames its graphics standards as establishing a “clear and consistent visual identity,” and the standards manual argues for simplicity and avoiding clutter in signage. [17] Corporate brand manuals frequently specify clear space and minimum size numerically: UC Davis Health requires a 0.25-inch minimum clear space and 0.25-inch minimum logo height in print contexts. [18] Delta Air Lines specifies clear space in terms of the mark’s cap-height and gives a minimum print size (“no smaller than 8p in width”). [19]

These sources (vision/standards + typography/composition + identity systems) are the right “bedrock” for a strict agent because they support threshold-based critiques (too small, too low contrast, too dense, too noisy, too many simultaneous focal points) rather than inspirational adjectives.

## Format taxonomy and decision model

This agent must reliably distinguish (and enforce) different format logics. The most important discriminator is not “style,” but the communication contract: reading time, viewing distance, and whether the audience can re-read.

Expressive graphic design
Contract: meaning can be partial/poetic; ambiguity is allowed if it supports affect or authorship. The agent still must control legibility of mandatory information (date/time/location/CTA) unless the brief explicitly prioritizes disruption.

Information-led graphic design
Contract: comprehension and retrieval dominate; the layout must reduce “search cost” and cognitive load. This aligns with research-based reduction of extraneous material and explicit signaling of structure (see slides and learning research below). [20]

Campaign / promotional (including OOH and social ads)
Contract: ultra-short attention windows; the design has to “land” instantly. Outdoor advertising research cited by Outdoor Advertising Association of America[21] notes that typical glances at digital billboards are under ~1 second and reports driver-risk findings that increase when glances exceed ~2 seconds (citing VTTI/NHTSA/FHWA context). [22] This implies hard constraints: one primary message, one brand, one action.

Editorial / print design
Contract: sustained reading; success depends on typographic rhythm, line length, line spacing, and multi-page unity. Ruder’s emphasis on readability and proportional spacing is directly aligned with this contract. [15] Editorial also depends on spread logic and book mechanics: Jost Hochuli[23] and Robin Kinross[24] describe book typography as inherently tied to the spine axis and the double-page spread as a typographic unit. [25]

Presentation / keynote design
Contract: shared viewing at distance; comprehension is time-based, not self-paced reading. Learning research by Richard E. Mayer[26] finds better transfer when irrelevant words/pictures/sounds are excluded (coherence), when organization cues are added (signaling), and when redundant on-screen text is avoided in certain narration+graphic conditions (redundancy), among other effects. [27] Business-facing slide guidelines operationalize the same idea into minimum type size: Microsoft’s commentary on the “10-20-30” rule recommends avoiding fonts smaller than ~30pt (and mentions 24pt as an accessibility guideline). [28]

System-led brand graphics
Contract: consistency across outputs; variance is constrained. This is the “manual logic” exemplified by NASA’s standards and other identity manuals (clear space, minimum size, consistent typography, avoid clutter). [29]

## Rule modules for the required research topics

Below are the 10 modules in the required template. Each module assumes the agent has access to: format type, physical size/aspect, viewing distance(s), viewing time, content inventory, brand constraints, and production medium (print/screen/signage).

### Topic one: composition systems and focal hierarchy

Definition.
A composition system is the set of spatial rules (grid, alignment fields, proportions, rhythm) used to place elements; focal hierarchy is the priority ordering of attention (what is seen first, second, third) created by scale, contrast, position, and spacing. Ruder frames typography as imposing “determined order” and foregrounds clear readability and measurable text mass. [15]

Why it matters for a Graphic Design Expert.
Production outcomes fail when a viewer cannot infer a reading order quickly, or when multiple elements compete as “first.” Clutter research defines clutter as excess items (or their organization) that degrade task performance-exactly the failure mode of broken focal hierarchy. [30]

Default rules.
The agent enforces a single dominant focal node per “view” (poster face, slide, page-as-gesture), then a controlled cascade.

- MUST declare a focal goal explicitly: “Primary: [message/asset]; Secondary: [support]; Tertiary: [details].”
- MUST choose one of three composition archetypes based on format and density:
- Single-field (one column/one frame): best for posters, OOH, hero slides.
- Dual-field (image field + text field): best for campaigns, editorial openers.
- Multi-field modular (grid modules): best for editorial spreads, dense decks, system graphics.
- MUST make the first read possible using at least two redundant cues (e.g., size + position; contrast + whitespace), because single-cue hierarchy is fragile across printing/display variance. (This is consistent with signaling/cueing logic in multimedia learning: adding cues that highlight organization improves learning. [31])
Exception rules.
- Expressive exception: allow multiple competing focal points only if the intended effect is “restlessness/fragmentation” and the content does not demand fast extraction. If mandatory info exists, it must still have a stable local hierarchy (e.g., a quiet info block).
- Brand exception: if brand rules constrain scale/contrast (e.g., subdued palette), use spacing and positioning as the primary hierarchy drivers.

Fallback logic.
If the agent cannot confidently resolve hierarchy from the brief, it defaults to information safety: 1) isolate a primary message block, 2) place it top-left (LTR locales) or optical top, 3) allocate maximum whitespace around it, 4) demote all other elements.

Failure conditions.
- Viewer cannot identify “what this is” within the format’s expected time window (see Topic two decision thresholds).
- More than one element reads as “headline” at the same distance.
- Background texture/image creates competing saliency (clutter) such that attention cannot be reliably directed. [32]

Measurable thresholds.
- Focal count: 1 dominant focal per view; 2 is acceptable only if their roles are clearly differentiated (e.g., headline + hero image) and one is subordinate by measurable contrast or size.
- Saliency risk proxy: if the design uses many disparate colors and high-contrast edges in a way that makes it “difficult to add a new salient item,” that matches the “feature congestion” framing of clutter-treat as high noise risk and simplify. [32]

Implementation guidance for an AI operator pack.
- Build a Focal Graph representation: nodes = elements; edges = dependencies; each node has attributes (size, contrast ratio, distance legibility, semantic weight, brand rigidity).
- Run a “dominant node” selection: maximize (semantic priority × legibility score × contrast score) subject to brand constraints.
- Enforce a “no rival nodes” rule: if any node’s saliency score is within ~10–15% of the dominant node, the operator must either demote it (reduce size/contrast, move out of prime positions) or upgrade the design into a deliberate “dual focal” composition with explicit separation.

Test cases.
1) A poster has a large background photo with a bright highlight crossing behind the headline: agent must detect competing saliency and force a text panel, blur, or tonal overlay (while maintaining contrast thresholds). [2]
2) A slide has two equal-sized headlines: agent must merge, demote one, or split into two slides using Mayer’s segmenting/coherence logic. [20]

### Topic two: poster vs editorial vs deck vs campaign decision models

Definition.
A decision model maps the brief and context into a format logic (poster, editorial, deck, campaign, system). It includes constraints like viewing distance, reading time, revision cycles, and whether the viewer can dwell/re-read.

Why it matters for a Graphic Design Expert.
Most production failures are category errors: designing a deck like a magazine (too dense), an editorial spread like a poster (too shallow), or a campaign asset like a UI (too many options).

Default rules.
The agent classifies format logic using these primary discriminators:

- Viewing time: momentary (≤2s), short (2–10s), medium (10–60s), long (minutes).
- Digital billboard glance durations are typically <1s and crash risk rises with glances >2s, supporting “momentary” logic for roadside. [22]
- Viewing distance: near (handheld/reading), mid (room), far (signage/outdoor).
- MUTCD’s 1 inch per 30 feet letter-height guidance implies distance-first constraints for roadway-type contexts. [5]
- Re-readability: can the viewer pause/return? (editorial yes; billboard no; live keynote mostly no).
Format mappings: - Campaign / OOH if viewing time is momentary/short and distance is mid/far. [33]
- Poster if audience is usually stationary but not committed to long reading; poster guidance emphasizes legibility at ~2m and avoiding excessive text. [34]
- Editorial if long reading and multi-page continuity are required; Hochuli and Ruder emphasize unity, rhythm, and the book/spread mechanism. [35]
- Deck if live viewing + spoken narration + sequential reveal; Mayer’s effects strongly support reducing extraneous material and using signaling/contiguity. [27]
- System-led if output must be repeatable across many instances; NASA and other manuals define this as codified standards. [36]

Exception rules.
- A deck can be “editorial” only if it is intended for asynchronous reading (e.g., emailed as a document). Then it becomes a “slide-document hybrid,” and editorial line-length/spacing rules become relevant.
- A poster can be “campaign momentary” if it’s placed in transit/fast movement zones; then apply billboard-like brevity rules.

Fallback logic.
If unclear, the agent defaults to the shortest likely viewing time (safety), because it is easier to add depth later than to salvage unreadable density.

Failure conditions.
- Audience feedback indicates “I can’t read this from the back” (deck failure).
- Readers must stop and parse when context expects scanning (campaign failure).
- Layout rhythm causes eye fatigue or loses place (editorial failure). [37]

Measurable thresholds.
- Campaign momentary rule: primary message + brand + CTA must be understandable within ~1–2 seconds in roadside contexts (supported by glance-duration research and 2-second risk threshold). [22]
- Deck minimum type: avoid fonts <30pt as a default distance legibility floor; accessibility references often cite 24pt minimum. [28]
- Poster legibility baseline: body text should be legible from ~2m; a cited poster handout suggests 30pt as a starting point for 2m legibility. [38]

Implementation guidance for an AI operator pack.
- Implement a Format Classifier that outputs: {format_logic, viewing_time_class, distance_class, rereadability, density_budget}.
- The classifier must also output a rejection warning when inputs mismatch: “Requested content volume exceeds density budget for campaign momentary-recommend editorial or multi-asset campaign set.”

Test cases.
1) Client wants “a single billboard with our mission statement paragraph”: agent must classify as campaign momentary, flag density mismatch, propose a two-layer system (billboard headline + QR landing). [22]
2) Client wants investor deck with 12 bullet points per slide: agent classifies as deck, invokes coherence/segmenting and forces split across slides. [20]

### Topic three: hierarchy depth and information grouping

Definition.
Hierarchy depth is the number of distinct levels (H1/H2/body/captions/footnotes, etc.) and the relationships between them. Grouping is the chunking of related items into perceivable units.

Why it matters for a Graphic Design Expert.
Comprehension depends on controlling cognitive load and allowing the viewer to build a stable mental model. Multimedia learning research shows that signaling structure improves learning, and coherence (removing extraneous material) improves transfer. [39] Working memory capacity is limited; classic and modern readings discuss small “slot” counts (Miller’s 7±2, Cowan’s ~4). [40]

Default rules.
- MUST set a maximum hierarchy depth per “view”: - Campaign/OOH: depth ≤2 (headline + brand/CTA).
- Poster/deck: depth ≤3–4 (headline, subhead, body, caption) depending on distance and time.
- Editorial: depth can be deeper, but must preserve regular rhythm and consistent labeling. - MUST group by meaning first, then align group boundaries visually (spacing, rules, background panels).
- SHOULD keep consistent typographic roles across the system (e.g., all H2s same size/weight) as poster guidance explicitly recommends for headings at the same importance level. [38]

Exception rules.
- Deep hierarchy is allowed in reference materials (appendix, spec sheets) where rereadability is high, but must be supported by a strong grid and navigational cues.

Fallback logic.
If hierarchy is not specified, the agent constructs a default schema:
H1 (one sentence) → supporting triad (≤3 bullets/claims) → details (caption/footnote) → CTA.

Failure conditions.
- Viewer cannot tell what is heading vs body (role ambiguity).
- Too many same-weight elements create “flat hierarchy.”
- Excessive choice sets slow decisions and increase search time (consistent with Hick-style decision-cost framing, though that literature is often applied to UI). [41]

Measurable thresholds.
- Chunk count per grouping field: target ≤4–5 primary chunks per view (aligned with modern working-memory discussions around ~4 chunks). [42]
- Line length and spacing thresholds for deep reading (editorial): 45–75 characters per line (Bringhurst) and 120–145% leading (Butterick) to support continuous reading. [43]

Implementation guidance for an AI operator pack.
- Require a Content Inventory with semantic tags: {title, claim, evidence, caption, metadata, CTA}.
- Map tags to typographic roles, then enforce role consistency checks (same tag → same styling).
- Add a “Hierarchy Compression” function: if content exceeds allowed depth, automatically propose: split into pages/slides, collapse subpoints, or move details into notes/QR/appendix.

Test cases.
1) Poster has 6 sections with similar headings: agent must enforce consistent heading styling and reduce section count or clustering. [38]
2) Editorial opener page uses 5 different typefaces: agent flags role confusion and pushes toward role-based system with limited styles.

### Topic four: image-text balance and visual pacing

Definition.
Image-text balance is the proportional and functional relationship between imagery and typography; pacing is the rhythm of alternation between dense and sparse zones, large and small, loud and quiet.

Why it matters for a Graphic Design Expert.
Balance and pacing determine whether the viewer can scan and then read without fatigue. Typographic guidance stresses readable “text mass” and proportioned spacing. [44] Poster guidance explicitly warns against excessive text and suggests allocating significant whitespace and figure area. [38]

Default rules.
- MUST pick a dominant mode per view: “type-led” or “image-led.” If both are equal, declare “dual-led” and separate into distinct fields.
- Poster default: keep text low and space generous; one poster guideline proposes an approximate distribution of ~20% text, 40% figures, 40% space (as a starting point, not a universal law). [38]
- Editorial default: use typographic rhythm rules (line length + line spacing) to make long reading comfortable. [43]
- Deck default: reduce simultaneous text+graphics complexity to honor coherence and signaling; avoid turning a slide into a page of prose. [45]

Exception rules.
- A “type-only” campaign asset can outperform image-led designs when the message is short and urgency is high (distance legibility and contrast become the dominant success criterion).
- Dense text is acceptable in an appendix slide only if it is labeled as “reference” and not intended for live presentation.

Fallback logic.
If uncertain, default to: 1) a large primary message,
2) one supporting image or diagram,
3) small caption/CTA,
4) generous whitespace.

Failure conditions.
- Image steals attention from required reading (competing saliency). [32]
- Text is placed on high-frequency imagery without sufficient contrast, violating readability standards. [46]
- Visual pacing is monotone (no variation in scale/spacing), creating scan fatigue.

Measurable thresholds.
- Contrast ratio for text over images: ≥4.5:1 (normal) or ≥3:1 (large) as a minimum baseline for readable text. [2]
- Poster text proportion starting point: ~20% text, with strong whitespace allocation (as cited above). [38]

Implementation guidance for an AI operator pack.
- Compute an Area Budget per view: {text_area%, image_area%, whitespace%} and validate against the selected format logic.
- Run a “text-on-image risk” check: if background local contrast variance is high (feature congestion proxy), enforce image treatment (blur/darken panel) or relocate text. [32]

Test cases.
1) Campaign Instagram story uses a busy photo; CTA becomes unreadable-agent must insert a solid panel and enforce contrast. [47]
2) Editorial spread has two full-bleed images and 800 words-agent must convert to a modular multi-page layout driven by reading rhythm.

### Topic five: distance legibility and display communication

Definition.
Distance legibility is whether essential text and symbols can be read at intended distances and angles; display communication is the design of artifacts meant to be perceived quickly in space (signage, posters, projected slides, OOH).

Why it matters for a Graphic Design Expert.
Distance failures are catastrophic: if the headline cannot be read, the design has failed regardless of style. The NBS report and USSC standards make legibility explicitly distance-dependent. [48]

Default rules.
- MUST require explicit input: maximum viewing distance(s), minimum viewing time, and medium (print/screen/sign).
- MUST choose one of three legibility models: 1) Roadway/signage model: MUTCD 1 inch per 30 feet baseline; adjust up for complexity. [49]
2) USSC Legibility Index model: letter height (in) = VRD (ft) / LI; treat LI=30 as average baseline and reduce to ~20 in complex environments (USSC describes deterioration with complexity). [50]
3) Poster/deck point-size model: use tested starting points (e.g., 2m ≈ 30pt) and validate by distance testing. [51]
- SHOULD prefer mixed case for long words; USSC documents increased letter height needs for all-caps. [52]

Exception rules.
- Logotype exception: WCAG notes logos/logotypes have no contrast requirement; brand marks may intentionally violate text contrast norms, but supporting copy cannot. [2]
- Expressive exception: deliberate illegibility is permitted only if no essential information is carried by that illegible element.

Fallback logic.
If distance is unknown, assume worst-case reasonable: - Deck: “back of room” and default to ≥30pt. [28]
- Poster: assume 2m baseline and use ≥30pt body. [38]
- OOH: use MUTCD ratio or USSC LI model with conservative adjustments. [49]

Failure conditions.
- Text readable only at production zoom, not at intended distance.
- Excess stroke fineness or low contrast prevents recognition; Howett’s model emphasizes stroke width as critical detail. [53]
- Too much visual complexity reduces detection distance; USSC documents “legibility index deterioration” in high-stimulus environments. [52]

Measurable thresholds.
- Roadway legibility baseline: 1 inch letter height per 30 feet legibility distance. [5]
- All caps penalty: ~15% increase in required letter height compared to mixed case. [52]
- Poster legibility starting points: 2m ≈ 30pt, 3m ≈ 48pt, 4m ≈ 60pt, 5m ≈ 72pt (starting points, to be tested). [38]
- Contrast minimums: 4.5:1 normal, 3:1 large (AA). [47]

Implementation guidance for an AI operator pack.
- Include a Legibility Calculator module: - inputs: distance, medium, type category (headline/body), caps style, environment complexity
- outputs: minimum cap height and recommended point size ranges
- Enforce a “distance test” step: render at expected physical size (or simulate) and require a back-of-room/2m check.

Test cases.
1) Slide uses 18pt bullets in a large room: agent must fail the design against distance-first rule and enforce ≥30pt or split content. [28]
2) OOH poster uses all-caps condensed type for a long sentence: agent flags all-caps penalty + crowding risk and requires shorter copy or larger letters. [54]

### Topic six: expressive exception rules vs information clarity

Definition.
Expressive exception rules specify when it is worth breaking clarity norms and what safeguards remain mandatory.

Why it matters for a Graphic Design Expert.
Without explicit exception rules, “expressive” becomes an excuse for failure. Ruder explicitly warns that readability is primary and that arbitrary formal games can destroy typography’s purpose. [15] Mayer’s coherence principle likewise shows that irrelevant additions harm understanding; exceptions must be deliberate. [55]

Default rules.
- MUST identify which content is non-negotiable (dates, location, CTA, key numbers).
- MUST keep non-negotiable content within clarity thresholds (contrast, size, hierarchy). [56]
- MAY allow expressive distortion (overlap, rotation, texture, low contrast) only for non-critical elements.

Exception rules.
- Exception allowed when the communication gain exceeds clarity loss: - If the piece’s goal is brand affect, cultural capital, or artistic authorship, limited ambiguity is acceptable.
- If distribution context provides rereadability (gallery poster viewed up close), you can shift toward expressive density.
- Exception not allowed when: - the audience is moving fast (OOH) or cannot re-read (live talk), given short glance windows and coherence needs. [57]

Fallback logic.
If the agent is uncertain whether expressive distortion is acceptable, it defaults to clarity and suggests adding expression via non-legibility-threatening channels: composition tension, cropping, rhythm, controlled palette.

Failure conditions.
- Essential info cannot be read at target distance/contrast. [58]
- Ornamentation increases clutter such that performance degrades (matches clutter definition). [59]

Measurable thresholds.
- Non-negotiable text must meet contrast minimums (4.5:1 normal, 3:1 large). [47]
- If expressive layers increase local variability (feature congestion) such that a new salient item would be hard to add, treat as high clutter risk and simplify. [32]

Implementation guidance for an AI operator pack.
- Implement an Exception Gate: 1) classify context (momentary vs rereadable)
2) identify mandatory info blocks
3) lock mandatory blocks to clarity constraints
4) allow expressive operations only outside locked zones
- Require the agent to output a justification sentence: “Grid break justified because [communication gain], cost mitigated by [safeguard].”

Test cases.
1) Experimental poster wants dense texture behind the date/time: agent must lock info block and relocate/overlay to keep contrast. [47]
2) Brand wants “edgy” deck with overlapping text: agent rejects for live presentation and proposes expressive cover slide + clear content slides. [60]

### Topic seven: typographic dominance and supporting graphic systems

Definition.
Typographic dominance is when type carries the primary message and structure; supporting systems are grids, rules, icons, and color/spacing tokens that keep outputs consistent.

Why it matters for a Graphic Design Expert.
Typography is the highest-bandwidth channel in most graphic design; it governs hierarchy, rhythm, and reading order. Ruder’s “primacy of readability” and insistence on proportioned spacing highlights the centrality of type. [15] Brand manuals demonstrate how supporting systems (clear space, minimum size) protect recognizability and consistency. [61]

Default rules.
- MUST define a role-based type system: {display, headline, subhead, body, caption, metadata}.
- SHOULD constrain variety: prefer few font families; vary via size/weight/spacing rather than swapping typefaces. Poster guidance warns against using different fonts just to highlight points. [38]
- MUST maintain readable line length and leading for body text where sustained reading is expected. [43]

Exception rules.
- Type experimentation is allowed in expressive contexts, but must not collapse roles (headline must still read as headline) unless the goal is deliberate disruption and not informational clarity.

Fallback logic.
If brand typography is unspecified: select a legible core family and implement hierarchy via scale, weight, and spacing; keep line length/leading in target ranges for reading contexts. [62]

Failure conditions.
- Too many typographic styles create role ambiguity.
- Line length too long/short damages readability. [63]
- Underlined or faux-emphasis techniques reduce clarity (Butterick treats these as key typographic pitfalls). [64]

Measurable thresholds.
- Body line length: 45–75 characters (single column) or 45–90 characters broadly depending on system. [65]
- Body leading: 120–145% of point size. [66]
- Poster constraints: avoid excessive text; use bullets and breathe space. [38]

Implementation guidance for an AI operator pack.
- Create a Type Scale Generator constrained by: - minimum point sizes from legibility module
- max line length
- leading ratio
- Add a “typographic audit” pass: count distinct sizes/weights/styles; flag if roles exceed allowed variety for format.

Test cases.
1) Editorial layout uses 90–110 characters per line; agent must reflow into columns or increase margins to restore measure. [67]
2) Poster uses 6 fonts: agent must collapse to role-based system and enforce spacing emphasis rather than font changes. [38]

### Topic eight: grid use and intentional grid-breaking

Definition.
A grid is an underlying structural system (columns, modules, baseline) that organizes content. Grid-breaking is deliberate violation of that system for emphasis, motion, or expression.

Why it matters for a Graphic Design Expert.
Grids enable consistency and variation within a system (essential for editorial and brand systems). Ruder describes basing layout on a grid of squares for complex pages, increasing possible variations. [15] Josef Müller-Brockmann[68]’s commonly cited framing that the grid is “an aid, not a guarantee… an art that requires practice” supports the idea that grids are tools, not prisons. [69] Timothy Samara[70]’s Making and Breaking the Grid is explicitly structured around understanding rules to use them-and then breaking them effectively. [71]

Default rules.
- MUST choose grid type by format: - Editorial: column + baseline-driven systems. [72]
- Poster/campaign: simpler fields with strong alignment axes.
- Brand systems: modular grids that can scale across applications. - MUST align related items to consistent edges; spacing becomes the primary “glue.”

Exception rules.
Grid-breaking is allowed when: - it creates measurable communication gain (stronger emphasis, clearer grouping, improved scan path), and
- it does not break legibility constraints (size, contrast). [56]

Fallback logic.
If grid decisions stall: enforce a simple column grid, align everything, then selectively break one element for emphasis.

Failure conditions.
- Grid exists but is inconsistent (arbitrary alignments).
- Grid-breaking produces chaos rather than controlled tension (Tschichold warns asymmetry must not degenerate into unrest or chaos). [73]

Measurable thresholds.
- Break count: ≤1 major grid break per view unless the system is explicitly expressive and the hierarchy remains intact.
- Baseline integrity (editorial): consistent rhythm across pages/spreads; Ruder references “linear register” as a postulate of typographic unity. [15]

Implementation guidance for an AI operator pack.
- Represent grid as constraints in a solver: margins, columns, gutters, baseline.
- Allow “break tokens” with budget: each break must cite its purpose (“increase focal emphasis,” “connect image and caption,” etc.) and must pass legibility checks.

Test cases.
1) Campaign poster: agent breaks grid by letting headline overlap image for urgency while preserving contrast via overlay. [74]
2) Editorial spread: agent breaks grid for a pull quote but keeps baseline for body text intact. [75]

### Topic nine: contrast, emphasis, and visual noise control

Definition.
Contrast is difference that creates visibility and hierarchy (tone, color, scale, weight). Emphasis is the intentional allocation of attention. Visual noise is “non-signal” that competes with or obscures the message.

Why it matters for a Graphic Design Expert.
Noise is a major driver of failure: clutter degrades performance at visually relevant tasks. Feature congestion describes clutter as too many features “clamoring for attention” so there’s little room for a new salient item. [76] Contrast is also governed by standards (WCAG) and is not optional for readable information. [2]

Default rules.
- MUST ensure contrast minimums for text unless content is purely decorative. [47]
- MUST treat busy textures, gradients, and high edge density behind text as noise sources; mitigate via panels, blur, or image selection.
- SHOULD reduce non-informational ornamentation in information-led contexts, consistent with coherence logic (exclude extraneous words/pictures). [77]

Exception rules.
- Logos/logotypes may violate contrast requirements (WCAG), but supporting text cannot. [47]
- Expressive designs may use noise intentionally, but must protect mandatory reading zones.

Fallback logic.
If noise is high: remove elements until the primary message is dominant; then reintroduce only those that add meaning.

Failure conditions.
- Text contrast below minimum. [47]
- Too many colors; poster guidance suggests max three colors for a clean look (starting guideline). [38]
- Visual search becomes hard because feature space is congested. [32]

Measurable thresholds.
- Contrast: 4.5:1 normal text, 3:1 large text (AA). [2]
- Color count starting point (poster): ≤3 colors to avoid chaotic look (context-dependent). [38]
- Clutter proxy: if more than ~3–4 distinct high-contrast “attention magnets” appear in one view, treat as clutter risk and simplify (aligned with feature congestion framing). [32]

Implementation guidance for an AI operator pack.
- Build a Contrast Validator (WCAG ratios, large-text detection). [78]
- Build a Noise Audit using feature-congestion-inspired heuristics: - count distinct saturated hues
- count high-contrast edge clusters
- detect text-over-texture risk
- Force output of a diagnostic: “over-styled and under-informative” = high noise score + low information hierarchy clarity.

Test cases.
1) Poster uses thin white text over bright photo: agent fails contrast and applies overlay/panel. [47]
2) Deck uses decorative background patterns on every slide: agent invokes coherence to remove extraneous visuals. [77]

### Topic ten: failure modes in graphic communication

Definition.
Failure modes are recurring patterns where a design fails its communication contract.

Why it matters for a Graphic Design Expert.
Strictness requires the agent to name and diagnose failure modes with criteria, not vibes. The sources above imply many concrete failures: unreadable lines, poor spacing, clutter degrading performance, distance illegibility, and extraneous material harming understanding. [79]

Default rules.
The agent maintains a failure-mode library and actively checks it during critique.

Key failure modes (with operational checks): - Category error (wrong format logic): deck treated as editorial, billboard treated as brochure. [57]
- Hierarchy collapse: too many equal-weight elements; no dominant focal. [59]
- Distance illegibility: type below minimum size for target distance. [80]
- Contrast failure: below minimum ratio. [78]
- Measure/leading failure: long lines or improper spacing reduce readability. [37]
- Clutter/noise overload: feature congestion too high; attention cannot be directed. [76]
- Inconsistent system: brand clear space/min sizes violated. [61]

Exception rules.
In expressive works, the agent can “accept” some failures if and only if the brief explicitly trades comprehension for affect-and mandatory info is still protected.

Fallback logic.
If multiple failure modes are triggered, prioritize fixes in this order: 1) distance legibility, 2) contrast, 3) hierarchy clarity, 4) clutter reduction, 5) typographic measure/leading, 6) brand compliance, 7) expressive refinements.

Measurable thresholds.
Failures are triggered when: - contrast < WCAG minimums, [47]
- letter height below MUTCD ratio or USSC LI calculation for stated distance, [49]
- poster/deck text below cited baseline sizes (30pt at 2m; ~30pt deck minimum), [51]
- editorial line length >75–90 chars in body text, or leading outside ~120–145% (default reading contexts). [81]

Implementation guidance for an AI operator pack.
- Create a Critique Output Schema: - “Format mismatch” warnings
- “Legibility violations” with numeric evidence
- “Hierarchy issues” with focal graph summary
- “Noise/clutter warnings”
- “Brand compliance issues” (clear space, min size)
- “Fix plan” ordered by severity

Test cases.
1) Brand poster violates minimum logo clear space: agent flags and corrects using the clearspace rule. [18]
2) Data-heavy slide contains decorative icons and textures: agent flags chartjunk/noise and invokes coherence to remove extraneous elements. [82]

## Operator-pack implementation architecture

A modular operator pack should implement these “engines,” each with deterministic checks:

Format Classifier Engine.
Inputs: audience context (moving vs stationary), viewing distance, viewing time, rereadability, medium.
Outputs: one of the 6 format logics + a density budget.
Hard references: OOH glance constraints and risk threshold (campaign), distance letter-height rules (signage), slide learning/comprehension constraints (deck). [83]

Hierarchy Constructor.
Inputs: content inventory + semantic priorities.
Outputs: hierarchy roles and grouping plan.
Hard references: signaling/coherence principles support explicit structuring; working memory limits motivate chunk budgets. [84]

Composition Planner.
Inputs: hierarchy + format logic + grid policy.
Outputs: grid choice, focal placement, alignment constraints.

Legibility Validator.
Checks:
- contrast ratios (WCAG), [78]
- type size vs distance (MUTCD/USSC + poster/deck baselines), [85]
- all-caps penalty adjustments. [52]

Noise / Clutter Auditor.
Implements a proxy of feature congestion: too many competing features reduce ability to direct attention. [32]

Brand System Enforcer.
Checks clear space and minimum size (where brand tokens exist), using explicit numeric rules where manuals specify them. [86]

Exception Gate.
Explicitly encodes when breaking clarity rules is allowed and how safeguards apply. [87]

## Deliverable file specs

Each file below is intended to be a portable module in a larger operator pack. The “what it should not contain” sections are as important as what it should contain, because they prevent drift into generic advice.

### graphic-design-expert.md

Purpose.
Defines the agent’s identity, responsibilities, format taxonomy, global rules, and output schema (how it speaks and what it must report).

What it should contain.
Format logic classifier rules; the universal constraints (contrast, legibility); the “MUST/SHOULD/MAY” language; critique schema; severity ordering for fixes.

What it should not contain.
Moodboards, trend talk, or unexplained “make it bold” guidance. No brand-specific assets.

What it depends on.
All other modules, plus brand tokens/data if available.

What skills it should hand off to.
Hands off to composition/hierarchy, legibility, image-type balance, and exception modules to do the actual construction and validation.

### composition-and-hierarchy-rules.md

Purpose.
Operational rules for composition systems, focal hierarchy, hierarchy depth, information grouping, grids, and intentional grid-breaking.

What it should contain.
Focal graph method; hierarchy depth budgets by format; grid selection rules; grid-break budget; failure triggers.

What it should not contain.
Brand logo guidelines and contrast math (belongs in legibility module).

What it depends on.
Format classifier output; content inventory.

What skills it should hand off to.
Hands off to layout generation and critique modules.

### poster-editorial-deck-decision-rules.md

Purpose.
Decision tree and classification logic to prevent category errors.

What it should contain.
Viewing time/distance decision rules; density budgets; what “poster logic vs deck logic vs editorial logic” means in constraints.

What it should not contain.
Low-level typography measures (belongs in legibility/typography modules).

What it depends on.
Minimum inputs: medium, viewing distance, viewing time, rereadability.

What skills it should hand off to.
Hands off to specific layout engines (poster, editorial, deck, campaign).

### distance-legibility-rules.md

Purpose.
Quantified legibility rules (type size, letter height, contrast expectations) across print, signage, and presentation.

What it should contain.
MUTCD ratio; USSC Legibility Index computation; all-caps penalty; WCAG contrast thresholds; poster/deck baseline point-size starting points.

What it should not contain.
Composition advice beyond what is required for legibility.

What it depends on.
Viewing distance/time; output size; medium.

What skills it should hand off to.
Hands off to type system builder and validation routines.

### image-type-balance-rules.md

Purpose.
Operational rules for managing image/text dominance, pacing, and text-on-image risk.

What it should contain.
Area budgets by format; risk checks for busy backgrounds; pacing patterns; fallback templates.

What it should not contain.
Brand clear space or grid math.

What it depends on.
Content inventory; selected format logic; chosen imagery.

What skills it should hand off to.
Hands off to layout generator and noise auditor.

### expressive-exception-rules.md

Purpose.
Defines when/why/how clarity rules can be broken.

What it should contain.
Exception gate, mandatory info locking, expressive operations allowed, and justification templates.

What it should not contain.
General essays about art; no vague “be edgy.”

What it depends on.
Format logic + brief priorities.

What skills it should hand off to.
Hands off to critique engine to explain tradeoffs.

### graphic-design-test-cases.md

Purpose.
A battery of test prompts + expected evaluation criteria to stress the operator.

What it should contain.
Edge cases that trigger format mismatch, legibility violations, clutter/noise, hierarchy collapse, grid-breaking decisions; pass/fail criteria.

What it should not contain.
Example images or final designs (tests must be portable).

What it depends on.
All rule modules.

What skills it should hand off to.
Hands off to QA/evaluation harness for regression testing.

## Operating spec and decision tools

### A. condensed operating spec

Agent mandate.
Produce production-level decisions for composition, hierarchy, focal structure, posters, decks, campaigns, editorial layouts, image/type balance, distance legibility, expressive vs informational tradeoffs, rhythm, contrast/emphasis, and brand-consistent systems.

Non-negotiables (hard constraints).
Text contrast must meet WCAG minimums for readable content (4.5:1 normal, 3:1 large; logotype exception allowed only for the logo itself). [78]
Distance-driven type must meet letter-height models (MUTCD 1 inch/30 ft baseline or USSC legibility index), with all-caps penalty where applicable. [49]
For live presentation contexts, default to large type (avoid <30pt) and reduce extraneous content (coherence/signaling). [88]
Editorial reading contexts must maintain readable measure and leading (45–75ish chars/line; 120–145% leading as baseline). [89]

Primary operating loop (every artifact).
1) Classify format logic.
2) Inventory content and mark mandatory info.
3) Allocate hierarchy roles + chunk budgets.
4) Choose composition archetype + grid.
5) Build type system within legibility constraints.
6) Place image and text fields, enforce area budgets.
7) Run validation: legibility (contrast/size), hierarchy clarity, noise/clutter, brand compliance.
8) If expressive: run exception gate; lock mandatory info zones.
9) Output critique statements with numeric evidence and a fix order.

Required critique voice (examples).
- “This needs poster logic, not UI logic.”
- “This deck needs distance-first hierarchy, not editorial density.”
- “This is over-styled and under-informative: clutter is competing with signal.” [90]
- “We can break the grid here because the communication gain (emphasis on X) outweighs the cost, and legibility remains compliant.” [91]

### B. graphic-format decision tree

1) Is the viewer moving fast or glancing briefly?
Yes → campaign/OOH logic (momentary). Use one message + one action; enforce distance legibility and contrast strictly. [92]
No → go to 2.

2) Is it presented live to an audience at room distance?
Yes → deck logic. Default to ≥30pt, segment content, minimize extraneous visuals, use signaling. [88]
No → go to 3.

3) Is the primary behavior sustained reading (minutes), often multi-page?
Yes → editorial logic. Enforce readable measure and leading; maintain multi-page unity and spread logic. [93]
No → go to 4.

4) Is it a single artifact meant to be read standing, ~1–3 meters, with light rereading?
Yes → poster logic. Minimize text, maintain legibility at distance, allocate whitespace generously. [34]
No → go to 5.

5) Must it be repeatable across many outputs with strict consistency?
Yes → system-led brand graphics. Apply standards: clear space, min size, consistent type and components. [36]
No → default to information-led or expressive based on brief priorities, but keep mandatory info compliant.

### C. hierarchy checklist

- Is there exactly one primary message per view (or a clearly separated dual focal layout)?
- Can a viewer identify “what this is” within the context’s time window (≤2s campaign; seconds-to-minutes otherwise)? [22]
- Are headings of equal importance styled consistently? [38]
- Is hierarchy depth within budget for the format (campaign ≤2; deck/poster ≤3–4 unless reference)? [84]
- Does body text meet readable measure and leading where long reading is expected? [89]
- Is mandatory info protected from expressive distortion (locked zones)?
### D. composition audit checklist

- Does the composition system match the format (single-field / dual-field / modular)?
- Are alignments intentional and consistent (or intentionally broken with justification)? [94]
- Are there “attention magnets” (high-contrast edges, saturated colors) competing with the focal message (feature congestion risk)? [76]
- Is text placed over imagery only when contrast remains compliant (or text has a panel/overlay)? [47]
- Does whitespace function as structure (not leftover gaps)?
- For multi-page/editorial: does the spread read as a unit and preserve rhythm/unity? [35]
### E. stress-test prompts

1) Design a highway-adjacent campaign poster for a charity with a required disclaimer paragraph. Enforce “momentary campaign” logic without losing compliance. [33]
2) Convert a dense magazine feature opener into a keynote opening slide while preserving tone; explain what must be removed under coherence/signaling principles. [45]
3) A client insists on ALL CAPS for a long venue name on wayfinding signs. Apply the all-caps legibility penalty and propose alternatives. [52]
4) Build an editorial spread with 1,200 words and 6 images; enforce readable measure and line spacing, then justify column count. [43]
5) Redesign a poster where body text is 14pt but needs to be legible from 2m; correct typographic scale using distance baselines. [38]
6) Diagnose a campaign asset: “over-styled and under-informative.” Provide evidence using clutter/feature congestion logic. [30]
7) Design a slide with a complex diagram and narration; apply redundancy and contiguity principles-decide what text moves to speaker notes. [20]
8) Enforce brand compliance: logo must appear on a poster with only 0.1" margin available; apply clear space rules and propose a compliant layout. [18]
9) Create a system-led template for 20 campaign variants (same brand, different messages). Specify which elements are fixed vs variable. [95]
10) A poster uses a busy photo as background; headline fails contrast. Fix without changing the photo. [47]
11) Decide whether a grid break is justified: headline overlaps the margin and bleeds off-page to increase urgency. Provide the justification and safeguards. [91]
12) A deck is intended to be emailed as a PDF (asynchronous reading). Reclassify as slide-document hybrid and adjust typography accordingly. [96]
13) A campaign wants to include 5 partner logos. Enforce hierarchy and brand clear space; propose layout that doesn’t turn into a logo soup. [61]
14) Create an editorial table of contents page where users must find sections fast; apply grid + hierarchy + low clutter. [97]
15) Design a poster where type is dominant but must integrate with illustration; choose whether to harmonize or contrast line intensity. [15]
16) A client requests “make it bold” for everything. Convert into measurable decisions: hierarchy depth, contrast, scale ratios, and noise reduction. [98]
17) Build a signage spec using USSC LI=30 for 600 ft viewing distance; compute letter height and explain mixed-case vs all-caps impacts. [7]
18) A poster needs to work both as print (3ft wide) and as a phone ad. Choose a system-led layout with responsive hierarchy and explain tradeoffs. [99]
19) Diagnose an editorial page: “eye keeps losing its place.” Apply measure/leading fixes and justify with typographic sources. [100]
20) A campaign billboard must include a QR code + CTA; ensure the hierarchy still works in <2 seconds. [22]
21) A deck slide uses 10 colors for decoration; reduce palette and show how color becomes a signal, not noise. [101]
22) Create a strict brand lockup rule: minimum logo size and clear space, using numeric constraints from a real manual; then show how to adapt when space is constrained. [61]
23) Convert a dense research poster into a series of 5 social slides; decide how hierarchy and pacing change. [102]
24) Design a typographic poster in which the headline is intentionally fragmented; keep event details legible and compliant. [56]
25) A brand system demands minimalism; stakeholders want “more energy.” Add energy via rhythm/grid-breaking rather than ornament-justify. [103]

[1] [2] [12] [21] [47] [56] [58] [74] [78] [98] Web Content Accessibility Guidelines (WCAG) 2.2

https://www.w3.org/TR/WCAG22/?utm_source=chatgpt.com

[3] Contrast Checker

https://webaim.org/resources/contrastchecker/?utm_source=chatgpt.com

[4] [15] [37] [44] [63] [72] [75] [79] [87] [93] [97] https://www.neugraphic.com/ruder/ruder-text2.html

https://www.neugraphic.com/ruder/ruder-text2.html

[5] [10] [49] [80] [85] 2009 Edition Chapter 2A. General - MUTCD

https://mutcd.fhwa.dot.gov/htm/2009/part2/part2a.htm?utm_source=chatgpt.com

[6] [13] [62] [66] [96] [100] https://practicaltypography.com/line-spacing.html

https://practicaltypography.com/line-spacing.html

[7] https://files.secure.website/wscfus/7691102/uploads/USSC_Sign_Legibility_Rules_of_Thumb.pdf

https://files.secure.website/wscfus/7691102/uploads/USSC_Sign_Legibility_Rules_of_Thumb.pdf

[8] [30] [32] [59] [76] [90] https://web.mit.edu/rruth/www/Papers/RosenholtzEtAlCHI2005Clutter.pdf

https://web.mit.edu/rruth/www/Papers/RosenholtzEtAlCHI2005Clutter.pdf

[9] [48] [53] https://www.govinfo.gov/content/pkg/GOVPUB-C13-ff8dc22d75e66f29ebdb2bb2085ee683/pdf/GOVPUB-C13-ff8dc22d75e66f29ebdb2bb2085ee683.pdf

https://www.govinfo.gov/content/pkg/GOVPUB-C13-ff8dc22d75e66f29ebdb2bb2085ee683/pdf/GOVPUB-C13-ff8dc22d75e66f29ebdb2bb2085ee683.pdf

[11] [26] [43] [65] [67] [81] [89] 2.1.2 Choose a comfortable measure

https://webtypography.net/2.1.2?utm_source=chatgpt.com

[14] [34] [38] [51] [99] [101] [102] https://e-smi.eu/wp-content/uploads/HOW-TO_Science_Poster_Design_and_Layout-1.pdf

https://e-smi.eu/wp-content/uploads/HOW-TO_Science_Poster_Design_and_Layout-1.pdf

[16] [20] [27] [31] [39] [45] [60] [84] https://www.hartford.edu/faculty-staff/faculty/fcld/_files/12%20Principles%20of%20Multimedia%20Learning.pdf

https://www.hartford.edu/faculty-staff/faculty/fcld/_files/12%20Principles%20of%20Multimedia%20Learning.pdf

[17] [29] [36] [70] [95] https://www.nasa.gov/nasa-brand-center/brand-guidelines/

https://www.nasa.gov/nasa-brand-center/brand-guidelines/

[18] [61] [86] https://health.ucdavis.edu/graphicstandards/pdf/spacing_clearspace_guide.pdf

https://health.ucdavis.edu/graphicstandards/pdf/spacing_clearspace_guide.pdf

[19] https://news.delta.com/delta-air-lines-logos-and-brand-guidelines

https://news.delta.com/delta-air-lines-logos-and-brand-guidelines

[22] [33] [57] [83] [92] https://oaaa.org/wp-content/uploads/2022/09/A-to-Z_Rebranded2018.pdf

https://oaaa.org/wp-content/uploads/2022/09/A-to-Z_Rebranded2018.pdf

[23] [64] https://practicaltypography.com/summary-of-key-rules.html

https://practicaltypography.com/summary-of-key-rules.html

[24] [46] Understanding Success Criterion 1.4.3: Contrast (Minimum)

https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html?utm_source=chatgpt.com

[25] [35] https://philipdibello.com/sva/2022-2023/type/fall/links/Jost-Hochuli-Robin-Kinross-Designing-Books-An-Introduction-1996.pdf

https://philipdibello.com/sva/2022-2023/type/fall/links/Jost-Hochuli-Robin-Kinross-Designing-Books-An-Introduction-1996.pdf

[28] [88] https://www.microsoft.com/en-us/microsoft-365-life-hacks/presentations/10-20-30-rule-of-powerpoint

https://www.microsoft.com/en-us/microsoft-365-life-hacks/presentations/10-20-30-rule-of-powerpoint

[40] https://labs.la.utexas.edu/gilden/files/2016/04/MagicNumberSeven-Miller1956.pdf

https://labs.la.utexas.edu/gilden/files/2016/04/MagicNumberSeven-Miller1956.pdf

[41] https://thedecisionlab.com/reference-guide/design/hicks-law

https://thedecisionlab.com/reference-guide/design/hicks-law

[42] https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/magical-number-4-in-shortterm-memory-a-reconsideration-of-mental-storage-capacity/44023F1147D4A1D44BDC0AD226838496

https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/magical-number-4-in-shortterm-memory-a-reconsideration-of-mental-storage-capacity/44023F1147D4A1D44BDC0AD226838496

[50] [52] [54] [68] https://usscfoundation.org/wp-content/uploads/2018/03/USSC-Guideline-Standards-for-On-Premise-Signs-2018.pdf

https://usscfoundation.org/wp-content/uploads/2018/03/USSC-Guideline-Standards-for-On-Premise-Signs-2018.pdf

[55] [77] [82] Coherence Principle (Chapter 4) - Multimedia Learning

https://www.cambridge.org/core/books/multimedia-learning/coherence-principle/4E80B70CB76E2166B76E5653EBDE7D3E?utm_source=chatgpt.com

[69] [91] [94] [103] https://designopendata.wordpress.com/portfolio/grid-systems/

https://designopendata.wordpress.com/portfolio/grid-systems/

[71] Making and Breaking the Grid, Second Edition, Updated ...

https://books.google.com/books/about/Making_and_Breaking_the_Grid_Second_Edit.html?id=GpYuDwAAQBAJ&utm_source=chatgpt.com

[73] https://designandtheory.files.wordpress.com/2017/01/tischold-new-typography.pdf

https://designandtheory.files.wordpress.com/2017/01/tischold-new-typography.pdf
