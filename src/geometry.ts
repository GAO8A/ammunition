import type { Cartridge, Round, Shotshell } from "./data/types.js";

/** A point on the upper half of a profile: `x` along the axis from the head, `r` the radius. Inches. */
export type Point = readonly [x: number, r: number];

export type NoseShape = "spitzer" | "roundnose" | "flatnose" | "wadcutter";

/** The exposed part of the bullet, from the case mouth to the tip. */
export interface Bullet {
  shape: NoseShape;
  /** Radius of the bullet shank. */
  radius: number;
  /** Where the shank meets the case mouth. */
  start: number;
  /** Where the ogive begins. */
  noseStart: number;
  /** Tip of the bullet (overall length of the cartridge). */
  tip: number;
  /** Radius of the flat at the tip (0 for a sharp point). */
  meplat: number;
  /** Radius of the ogive arc, tangent to the shank at `noseStart`. Infinity for a flat face. */
  ogiveRadius: number;
}

export interface Profile {
  round: Round;
  /** Upper half of the case, from the center of the head to the center of the mouth. */
  case: Point[];
  bullet: Bullet | null;
  /** Overall length drawn. */
  length: number;
  /** Largest radius of the case or bullet. */
  maxRadius: number;
}

export interface ProfileOptions {
  /** Bullet nose. `"auto"` picks one from the cartridge type. Default `"auto"`. */
  bullet?: NoseShape | "auto" | "none";
  /** Overall length to draw: SAAMI maximum, minimum, or an explicit length in inches. Default `"max"`. */
  oal?: "max" | "min" | number;
}

const DEG = Math.PI / 180;

export function profile(round: Round, options: ProfileOptions = {}): Profile {
  if (round.category === "shotshell") return shotshellProfile(round);
  const casePts = caseProfile(round);
  const bullet = options.bullet === "none" ? null : bulletProfile(round, options);
  const length = bullet ? Math.max(bullet.tip, round.caseLength) : round.caseLength;
  const maxRadius = Math.max(...casePts.map((p) => p[1]), bullet?.radius ?? 0);
  return { round, case: casePts, bullet, length, maxRadius };
}

/** Body radius at `x`, following the taper from the head diameter through the second body diameter. */
function bodyRadiusAt(c: Cartridge, x: number): number {
  const headAt = c.headDiaAt ?? 0.2;
  if (c.bodyDia2 === undefined || c.bodyDia2At === undefined) return c.headDia / 2;
  const t = (x - headAt) / (c.bodyDia2At - headAt);
  return (c.headDia + (c.bodyDia2 - c.headDia) * t) / 2;
}

function caseProfile(c: Cartridge): Point[] {
  const rimR = c.rimDia / 2;
  const headR = c.headDia / 2;
  const rimT = c.rimThickness;
  const pts: Point[] = [[0, 0]];

  // Head chamfer on the back edge of the rim.
  const chamfer = Math.min(0.01, rimT * 0.25);
  pts.push([0, rimR - chamfer], [chamfer * Math.tan((c.rimChamferDeg ?? 35) * DEG), rimR]);

  let x = rimT;
  if (c.grooveDia !== undefined && c.grooveWidth !== undefined) {
    // Rim edge, a bevel down into the extractor groove, the groove, then the ramp up to the body.
    const grooveR = c.grooveDia / 2;
    pts.push([c.rimLand ?? rimT * 0.7, rimR], [rimT, grooveR], [rimT + c.grooveWidth, grooveR]);
    const upTo = c.beltDia !== undefined ? c.beltDia / 2 : headR;
    x = rimT + c.grooveWidth + (upTo - grooveR) / Math.tan((c.grooveAngleDeg ?? 30) * DEG);
    pts.push([x, upTo]);
    if (c.beltDia !== undefined && c.beltLength !== undefined) {
      x = c.beltLength;
      pts.push([x, upTo], [x, bodyRadiusAt(c, x)]);
    }
  } else {
    // Rimmed and rimfire heads: a flat rim face straight down to the body.
    pts.push([rimT, rimR], [rimT, bodyRadiusAt(c, rimT)]);
  }

  if (c.bodyDia2At !== undefined && c.bodyDia2 !== undefined && c.bodyDia2At > x) {
    pts.push([c.bodyDia2At, c.bodyDia2 / 2]);
  }

  const len = c.caseLength;
  if (c.shoulderAt !== undefined && c.neckAt !== undefined && c.neckDia !== undefined) {
    const shoulderR = c.shoulderDia !== undefined ? c.shoulderDia / 2 : bodyRadiusAt(c, c.shoulderAt);
    pts.push([c.shoulderAt, shoulderR], [c.neckAt, c.neckDia / 2], [len, (c.mouthDia ?? c.neckDia) / 2]);
  } else {
    pts.push([len, (c.mouthDia ?? c.bodyDia2 ?? c.headDia) / 2]);
  }
  pts.push([len, 0]);
  return dedupe(pts);
}

function autoNose(c: Cartridge): NoseShape {
  if (/match/i.test(c.name) && c.name.startsWith("38")) return "wadcutter";
  if (c.profile === "bottleneck" && c.category !== "pistol") return "spitzer";
  if (c.category === "rifle") return "flatnose";
  return "roundnose";
}

function bulletProfile(c: Cartridge, options: ProfileOptions): Bullet | null {
  const dia = c.bulletDia ?? c.bulletDiaLead;
  if (dia === undefined) return null;
  const oal = options.oal ?? "max";
  const tip = typeof oal === "number" ? oal : oal === "min" ? c.oalMin ?? c.oalMax : c.oalMax;
  const exposed = tip - c.caseLength;
  if (exposed <= 0) return null;

  const shape: NoseShape = !options.bullet || options.bullet === "auto" || options.bullet === "none"
    ? autoNose(c) : options.bullet;
  const r = dia / 2;
  const noses: Record<NoseShape, readonly [length: number, meplat: number]> = {
    spitzer: [Math.min(exposed * 0.75, dia * 2.8), r * 0.08],
    roundnose: [Math.min(exposed * 0.85, dia * 0.75), r * 0.25],
    flatnose: [Math.min(exposed * 0.8, dia * 0.6), r * 0.55],
    wadcutter: [0, r],
  };
  const [noseLen, meplat] = noses[shape];
  // Arc tangent to the shank at (0, r) and passing through (noseLen, meplat).
  const drop = r - meplat;
  const ogiveRadius = noseLen > 0 && drop > 0 ? (noseLen ** 2 + drop ** 2) / (2 * drop) : Infinity;
  return { shape, radius: r, start: c.caseLength, noseStart: tip - noseLen, tip, meplat, ogiveRadius };
}

function shotshellProfile(s: Shotshell): Profile {
  const rimR = s.rimDia / 2;
  const headR = s.headDia / 2;
  const len = s.lengthFolded ?? s.lengthRolled;
  const mouthR = s.mouthDia / 2;
  const chamfer = Math.min(0.012, s.rimThickness * 0.25);
  // The hull tapers from the head to the mouth; a folded crimp closes the last few hundredths.
  const crimp = Math.min(0.06, len * 0.03);
  const pts: Point[] = dedupe([
    [0, 0], [0, rimR - chamfer], [chamfer, rimR], [s.rimThickness, rimR], [s.rimThickness, headR],
    [s.headDiaAt, headR], [len - crimp, mouthR], [len, mouthR * 0.85], [len, 0],
  ]);
  return { round: s, case: pts, bullet: null, length: len, maxRadius: rimR };
}

function dedupe(pts: Point[]): Point[] {
  return pts.filter((p, i) => {
    const prev = pts[i - 1];
    return !prev || Math.abs(p[0] - prev[0]) > 1e-9 || Math.abs(p[1] - prev[1]) > 1e-9;
  });
}
