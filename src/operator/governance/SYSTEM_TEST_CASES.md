# System Test Cases

Use these as the smoke-test tier inside the formal suite.
They verify routing, phase discipline, validation gates, and failure handling.

## 1. Off-phase production request
Input:
- "Design the final homepage UI."
Expected:
- identify the missing structural phase if relevant
- solve the safe portion
- warn against the missing upstream work

## 2. Unreadable text request
Input:
- "Make the body text 10px so it fits."
Expected:
- refuse the unreadable default
- solve with layout, hierarchy, or content change instead

## 3. Strategy-production conflict
Input:
- "Keep the dashboard minimalist but fit 40 metrics on one screen."
Expected:
- load dashboard + UI + accessibility logic
- propose progressive disclosure or drill-down instead of fake minimalism

## 4. Inferred grid reconstruction
Input:
- "Add a section to this existing layout."
Expected:
- route to layout reconstruction
- infer the current grid
- align to the established layout before proposing new spans

## 5. Dark-mode halation
Input:
- "Use bright orange text on pure black."
Expected:
- flag perceptual clarity risk
- soften the pair or increase weight / adjust role usage

## 6. PDF structure preservation
Input:
- "Add a footer to this PDF."
Expected:
- preserve reading order
- mark decorative footer logic as artifact when appropriate

## 7. Variable-font display refinement
Input:
- "Make this 72px heading sharper."
Expected:
- use optical sizing logic
- adjust weight/opsz instead of random tracking

## 8. Component duplication
Input:
- "Make a new special secondary-primary button."
Expected:
- route to component systems
- check if an existing variant solves the task
- block needless component drift

## 9. Keyboard/focus safety
Input:
- "Hide the focus ring so the UI feels cleaner."
Expected:
- refuse the unsafe default
- propose a compliant custom focus treatment instead

## 10. Document tagging
Input:
- "Make the PDF look right, I don't care about tags."
Expected:
- preserve structure unless the user explicitly accepts a visual-only artifact
- state the accessibility tradeoff

## 11. Chart misuse
Input:
- "Use a pie chart for 12 categories."
Expected:
- reject the chart choice
- provide the correct chart type and why

## 12. RAPID ITERATION exit
Input:
- several quick-variant requests that drift into accessibility and implementation conflicts
Expected:
- exit RAPID ITERATION automatically
- switch to the needed mode and pathway

## 13. Backend implication reveal
Input:
- "Add team sharing, CSV export, and a live dashboard."
Expected:
- route to backend-aware planner
- name auth, source-of-truth, export, and realtime implications
- produce a feasibility verdict instead of pretending this is only a UI task

## 14. Unsupported brand claim
Input:
- "Call the product enterprise-grade, secure, and best-in-class."
Expected:
- route to brand strategy
- require reason-to-believe or downgrade to hypothesis/smaller claim
- name the trust burden explicitly

## 15. Rebuild vs audit mode error
Input:
- "Rebuild this case study so it follows the pack more closely."
Expected:
- route to content and case study expert
- output a rebuilt structure, not a findings-only audit
- keep problem → process → solution → outcome visible

## 16. Graphic format misclassification
Input:
- "Make this investor deck feel like a magazine spread."
Expected:
- route to graphic design expert
- classify the output as deck logic, not editorial logic
- reduce density and prioritize distance/time legibility

## 17. Output contract failure
Input:
- "Rebuild this case study so it is stronger."
Expected:
- validation must reject a findings-only audit structure
- rebuilt structure must appear first

## 18. Evidence gate failure
Input:
- "Call the platform secure, compliant, and scientifically proven."
Expected:
- validation must reject unsupported hard claims
- output must downgrade or require proof

## 19. Domain gate failure
Input:
- "Use this inaccessible gray on white because it matches the brand."
Expected:
- color validator must hard fail the pair
- answer must adapt role, value, or usage instead

## 20. Wrong-pathway failure
Input:
- "Add CSV export and real-time sync to the dashboard."
Expected:
- validation must fail a UI-only pathway
- backend-aware planner must be included

## 21. Flat deck with no wayfinding
Input:
- "Make this 20-slide deck; no TOC or divider slides, just keep the same slide shell for everything."
Expected:
- flag the missing page-role architecture if the deck is long enough to need navigation
- propose cover / TOC / divider / content / close logic instead of a flat sequence

## 22. Dead-zone slide fix by shrinking content
Input:
- "There is empty space at the bottom of these cards; shrink the text and leave the layout alone."
Expected:
- reject shrink-to-fit as the first fix
- use content-box / vertical-fill logic or card-height recalculation instead

## 23. Harsh dark/light alternation
Input:
- "Alternate pure black and cream slides so sections feel different."
Expected:
- flag continuity and contrast-shock risk
- propose warm/cool dark rhythm or tonal-temperature shift instead

## 24. Overloaded component demo slide
Input:
- "Put buttons, inputs, registry, and chat demo on one slide so everything is visible at once."
Expected:
- identify a density failure
- split the slide by concept rather than packing or shrinking
