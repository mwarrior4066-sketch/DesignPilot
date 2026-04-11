# Graphic Critique Example
Fixture: tests/fixtures/graphic-critique-pass.prompt.md
Validation result: tests/evals/graphic-critique-pass.eval.json

## Input Prompt
Critique this event poster. The headline is fighting the image, the sponsor block is too loud, and from a few feet away the date disappears.

## Selected Route and Loaded Skills
- Route: `rt_graphic_critique`
- Task contract: `graphic_critique`
- Mode: AUDIT
- Phase: communication
- Skills: `graphic-design-expert.md`, `type-system-expert.md`
- Known tensions: expressiveness vs legibility, brand tone vs message clarity

## Final Output
### Communication goal
The poster has one first job: tell someone what the event is and when it happens from a short viewing distance. The current composition spends too much attention on image drama and sponsor texture before the date and event name are secured.

### Composition failures
1. The image crop has strong energy, but it is competing with the headline instead of framing it. That weakens the focal winner.
2. The sponsor block is scaled and contrasted like a second headline. It should not rival the event title on the first read.
3. The date sits in a smaller, lower-contrast zone, so distance legibility collapses once the viewer steps back.
4. The type/image balance feels flattened because too many elements occupy similar emphasis bands. Rhythm and grouping are not guiding the scan.

### Rebuild moves
- Make the event title the dominant focal element and let the image support it rather than cross it.
- Increase the date’s scale and place it in the same visual grouping as the title so the first scan captures both message and timing.
- Demote the sponsor block by reducing contrast, shrinking its size band, and separating it from the primary information cluster.
- Use alignment and proportion to create a clearer top-to-bottom rhythm. The tradeoff is less expressive sponsor presence versus stronger event comprehension. Event comprehension should win because the artifact fails if the viewer cannot identify the message at poster distance.

### Distance and emphasis tradeoff
At thumbnail size or from several feet away, the headline and date should survive first. The crop and production size boundary should serve that priority rather than forcing the headline into a narrow leftover area. The obvious alternative is to keep the sponsor block loud for partner visibility, but that splits the focal path. Let the sponsor block recede so the event message can lead.

## Why This Passed
- It defines the communication goal before judging style.
- It names focal, rhythm, grouping, and distance-legibility failures.
- It resolves emphasis rather than asking every element to stay loud.
- It gives compositional moves a designer could execute immediately.

## What Would Have Failed
- Saying the poster just needs to pop more.
- Recommending a purely stylistic font swap without naming the focal winner.
- Claiming readability is fixed with no reason tied to distance or scan.

## Revision Pass
The weak draft focused on making the type more modern and adding brighter color. The corrected version diagnosed the failed focal order and rebuilt the emphasis structure around the communication goal.
