import { all, find } from "./data/index.js";
import type { Round } from "./data/types.js";
import { profile, type Bullet, type Point, type ProfileOptions } from "./geometry.js";

export interface RenderOptions extends ProfileOptions {
  /** Pixels per inch. Ignored when `width` or `height` is set. Default 100. */
  scale?: number;
  /** Fit the drawing to this many pixels along the cartridge axis. */
  width?: number;
  /** Fit the drawing to this many pixels across the cartridge. */
  height?: number;
  /** Head on the left (`"horizontal"`) or at the bottom (`"vertical"`). Default `"horizontal"`. */
  orientation?: "horizontal" | "vertical";
  /** Padding around the drawing, in pixels. Default 2. */
  padding?: number;
  stroke?: string;
  strokeWidth?: number;
  caseFill?: string;
  bulletFill?: string;
  /** Accessible title. Defaults to the cartridge name; `false` omits it. */
  title?: string | false;
  className?: string;
  /** Decimal places in path coordinates. Default 2. */
  precision?: number;
}

export class UnknownCartridgeError extends Error {
  constructor(public readonly query: string, public readonly suggestions: string[]) {
    super(`Unknown cartridge "${query}"` + (suggestions.length ? `. Did you mean ${suggestions.map((s) => `"${s}"`).join(", ")}?` : ""));
    this.name = "UnknownCartridgeError";
  }
}

export function resolve(round: Round | string): Round {
  if (typeof round !== "string") return round;
  const found = find(round);
  if (found) return found;
  const q = round.toLowerCase();
  const lead = q.match(/^[\d.]+/)?.[0];
  const suggestions = all
    .filter((r) => r.name.toLowerCase().includes(q) || (lead !== undefined && r.name.toLowerCase().startsWith(lead)))
    .slice(0, 3)
    .map((r) => r.name);
  throw new UnknownCartridgeError(round, suggestions);
}

const escape = (s: string) => s.replace(/[&<>"]/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[ch]!);

/** Render a cartridge or shotshell as a standalone SVG string. Throws `UnknownCartridgeError` for unknown names. */
export function render(round: Round | string, options: RenderOptions = {}): string {
  const p = profile(resolve(round), options);
  const vertical = options.orientation === "vertical";
  const pad = options.padding ?? 2;
  const scale = options.width !== undefined ? (options.width - 2 * pad) / p.length
    : options.height !== undefined ? (options.height - 2 * pad) / (2 * p.maxRadius)
    : options.scale ?? 100;
  const along = p.length * scale + 2 * pad;
  const across = 2 * p.maxRadius * scale + 2 * pad;
  const [w, h] = vertical ? [across, along] : [along, across];
  const digits = options.precision ?? 2;
  const fmt = (n: number) => String(Number(n.toFixed(digits)));

  // Map profile coordinates (x along the axis, y across it, upper half negative) to SVG pixels.
  // The vertical mapping is a rotation, not a reflection, so arc sweep flags stay valid.
  const at = (x: number, y: number) => {
    const [px, py] = vertical ? [w / 2 + y * scale, h - pad - x * scale] : [pad + x * scale, h / 2 + y * scale];
    return `${fmt(px)} ${fmt(py)}`;
  };

  const casePath = outline(p.case, at);
  const stroke = escape(options.stroke ?? "currentColor");
  const sw = options.strokeWidth ?? 1;
  const name = escape(p.round.name);
  const title = options.title === false ? "" : `<title>${escape(options.title ?? p.round.name)}</title>`;
  const cls = escape(["ammo", options.className].filter(Boolean).join(" "));

  let body = `<path class="ammo-case" d="${casePath}" fill="${escape(options.caseFill ?? "none")}"/>`;
  if (p.bullet) body = `<path class="ammo-bullet" d="${bulletPath(p.bullet, at, fmt, scale)}" fill="${escape(options.bulletFill ?? "none")}"/>` + body;

  return `<svg xmlns="http://www.w3.org/2000/svg" class="${cls}" role="img" aria-label="${name}" ` +
    `width="${fmt(w)}" height="${fmt(h)}" viewBox="0 0 ${fmt(w)} ${fmt(h)}">${title}` +
    `<g stroke="${stroke}" stroke-width="${sw}" stroke-linejoin="round" vector-effect="non-scaling-stroke">${body}</g></svg>`;
}

/** Close the upper half and its mirror image into one outline. */
function outline(pts: Point[], at: (x: number, y: number) => string): string {
  const top = pts.map(([x, r]) => at(x, -r));
  // The first and last points sit on the axis and are shared by both halves.
  const bottom = pts.slice(1, -1).reverse().map(([x, r]) => at(x, r));
  return `M${[...top, ...bottom].join("L")}Z`;
}

/** Shank from the case mouth, ogive to the meplat, across the tip, and back. Open at the mouth. */
function bulletPath(b: Bullet, at: (x: number, y: number) => string, fmt: (n: number) => string, scale: number): string {
  // Drawn clockwise, so both ogive arcs use sweep-flag 1. A wadcutter has a flat face instead.
  const R = fmt(b.ogiveRadius * scale);
  const nose = (x: number, y: number) => Number.isFinite(b.ogiveRadius) ? `A${R} ${R} 0 0 1 ${at(x, y)}` : `L${at(x, y)}`;
  return `M${at(b.start, -b.radius)}L${at(b.noseStart, -b.radius)}${nose(b.tip, -b.meplat)}` +
    `L${at(b.tip, b.meplat)}${nose(b.noseStart, b.radius)}L${at(b.start, b.radius)}`;
}
