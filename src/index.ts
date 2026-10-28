import { render, resolve, type RenderOptions } from "./svg.js";

export { render, resolve, UnknownCartridgeError, type RenderOptions } from "./svg.js";
export { profile, type Bullet, type NoseShape, type Point, type Profile, type ProfileOptions } from "./geometry.js";
export { all, find, pistol, rifle, rimfire, shotshell, type Cartridge, type Round, type Shotshell } from "./data/index.js";

/**
 * Render into a DOM element (or the first element matching a selector) and return the new `<svg>`.
 * Browser only.
 */
export function draw(target: Element | string, name: string, options?: RenderOptions): SVGSVGElement {
  const el = typeof target === "string" ? document.querySelector(target) : target;
  if (!el) throw new Error(`draw(): no element matches "${String(target)}"`);
  el.insertAdjacentHTML("beforeend", render(resolve(name), options));
  return el.lastElementChild as SVGSVGElement;
}

/**
 * The 0.x API: `new Ammo({ element, name, bullet, stroke })`. Prefer `draw()` or `render()`.
 * `bullet: "rifle"` maps to a spitzer nose and `"standard"` to a round nose.
 * @deprecated
 */
export class Ammo {
  readonly svg: SVGSVGElement;
  constructor(config: { element: Element | string; name: string; bullet?: "rifle" | "standard"; stroke?: string }) {
    const bullet = config.bullet === "rifle" ? "spitzer" : config.bullet === "standard" ? "roundnose" : "auto";
    this.svg = draw(config.element, config.name, { bullet, stroke: config.stroke ?? "#333", scale: 400 });
  }
}
