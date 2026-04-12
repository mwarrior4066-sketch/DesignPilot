## Architectural framing
Just convert it to React and use more hooks. The page will probably be fine.

## Boundary and state model
Put everything on the client for speed and componentize it later.

## Rendering and mutation strategy
Use optimistic updates and a useEffect for loading.

## Risks and safer path
Production-ready after cleanup.
