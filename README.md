# Stillwater

A night-pond ripple-physics puzzle. Click to send out expanding ripples whose
wavefronts push glowing wisps into lantern rings. Tap for a soft nudge, hold to
gather a stronger wave. Waves bend around stones, ride currents, and are dragged
around whirlpools. Some lanterns only accept a wisp of their own colour.

Play it here: **https://kosikvince-sys.github.io/stillwater/**

## Controls

- **Tap** behind a wisp for a gentle nudge.
- **Hold** to gather a stronger ripple, release to fire.
- **Shift + click** to stage a pending wave (repeat for more), then **Space** to
  release them all at the same instant.
- On a touchscreen, two fingers gather two waves at once.
- **R** restarts the level, **Esc** returns to the menu.

## Running locally

It is a single self-contained `index.html`, so you can just open it in a browser.
For the installable PWA (service worker, offline play) it needs to be served over
http rather than opened as a file:

```
python3 -m http.server
```

then visit the printed `localhost` address. The bundled `Stillwater Server.command`
does the same with a double-click.

## Development notes

- Everything lives in `index.html` (markup, styles, game in one `<script>`).
- Tuning constants are at the top of the script: `PUSH`, `RIPPLE_SPEED`,
  `CHARGE_TIME`, `POWER_MIN` / `POWER_MAX`, `WHIRL_STR`, and the per-level `ripples`
  budgets in `LEVELS`.
- `LEVELS` is the level list. Coordinates are fractions of the screen. Orbs and
  goals are `[x, y]` (goals take an optional colour tag), rocks and whirls are
  `[x, y, radius]` (whirls add a spin direction), flows are `[x, y, w, h, fx, fy]`.
- It is a PWA. **Bump the `CACHE` version in `sw.js` on every change**, otherwise
  installed users keep getting served the old cached files.
