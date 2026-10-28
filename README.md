# ammunition

SAAMI cartridge and shotshell dimensions, and SVG drawings generated from them.

- **192 rounds**: 131 centerfire rifle, 36 centerfire pistol, 11 rimfire and 14 shotshell, transcribed from the current SAAMI Z299 standards.
- **Drawn from the spec**: outlines are computed from the SAAMI dimensions themselves (rim, extractor groove, belt, body taper, shoulder, neck), not from stored point lists.
- **Zero dependencies**: works in Node, browsers and any framework, because `render()` returns a plain SVG string.

```bash
npm install ammunition
```

## Drawing

```js
import { render, draw } from "ammunition";

const svg = render("308 Win", { scale: 120, caseFill: "#f1dfa8" });   // SVG string

draw("#target", "9mm", { orientation: "vertical" });                  // browser: append to an element
```

Names are matched loosely against SAAMI names and common aliases: `"308 Win"`, `"308 Winchester"`, `".308WIN"`, `"45 ACP"`, `"22 LR"`. An unknown name throws `UnknownCartridgeError`, which carries `suggestions`.

| Option | Default | |
|---|---|---|
| `scale` | `100` | Pixels per inch. |
| `width` / `height` | | Fit along / across the cartridge instead of using `scale`. |
| `orientation` | `"horizontal"` | `"vertical"` puts the head at the bottom. |
| `bullet` | `"auto"` | `"spitzer"`, `"roundnose"`, `"flatnose"`, `"wadcutter"` or `"none"`. |
| `oal` | `"max"` | Overall length: `"max"`, `"min"` or inches. |
| `stroke`, `strokeWidth` | `currentColor`, `1` | |
| `caseFill`, `bulletFill` | `none` | Or style the `.ammo-case` and `.ammo-bullet` classes with CSS. |
| `title` | cartridge name | Accessible title; `false` to omit. |
| `padding`, `precision`, `className` | `2`, `2`, | |

`profile(round, options)` returns the underlying geometry (case points in inches and the bullet's ogive parameters) if you want to draw it yourself.

## Data

```js
import { find, rifle, pistol, rimfire, shotshell } from "ammunition/data";

find("6.5 Creedmoor");
// { name: "6.5 Creedmoor", rimType: "rimless", profile: "bottleneck", rimDia: 0.472, rimDiaTol: -0.01,
//   headDia: 0.4703, shoulderDia: 0.462, shoulderAngleDeg: 30, neckDia: 0.295, caseLength: 1.92, oalMax: 2.825, ... }
```

Lengths are inches, angles degrees, tolerances signed offsets as SAAMI states them, and `*At` positions are measured from the head. The raw CSVs are in [`data/`](data/), and the field meanings are documented in [`src/data/types.ts`](src/data/types.ts).

Each value was checked against the text of the SAAMI PDF it came from, with garbled spots confirmed on zoomed renders. The values were also cross-checked for consistency: on every bottleneck case, the body taper, shoulder angle and datum agree to within 0.0015". The transcriptions and their checks are in [`tools/`](tools/).

**Not covered by SAAMI, so approximated:** bullet nose shapes (SAAMI marks bullets as illustrative), shoulder and neck fillet radii, and the 22 LR shot crimp.

## Migrating from 0.x

`new Ammo({ element, name, bullet, stroke })` still works, but it is deprecated. Use `draw(element, name, options)` instead. `bullet: "rifle"` maps to `"spitzer"` and `"standard"` to `"roundnose"`. 0.x drew everything at 4×; `Ammo` keeps that at `scale: 400`. Cartridge names now follow the current SAAMI standards.

## Development

```bash
npm test          # regenerate src/data from data/*.csv, compile, run tests
```

To look at every drawing, serve the repository root and open `demo/gallery.html`.

## License

MIT. Dimensions are from SAAMI Z299.1–Z299.4 voluntary industry standards.
