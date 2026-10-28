import { test } from "node:test";
import assert from "node:assert/strict";
import { all, find, profile, render, UnknownCartridgeError } from "../dist/index.js";

test("dataset sizes match the transcribed standards", () => {
  const count = (c) => all.filter((r) => r.category === c).length;
  assert.equal(count("rifle"), 131);
  assert.equal(count("pistol"), 36);
  assert.equal(count("rimfire"), 11);
  assert.equal(count("shotshell"), 14);
});

test("find() matches names and aliases loosely", () => {
  assert.equal(find("308 win")?.name, "308 Winchester");
  assert.equal(find(".308 WINCHESTER")?.name, "308 Winchester");
  assert.equal(find("9mm Luger +P")?.name, "9mm Luger");
  assert.equal(find("22 lr")?.category, "rimfire");
  assert.equal(find("44 Rem Mag", "pistol")?.category, "pistol");
  assert.equal(find("nope"), undefined);
});

test("unknown names throw with suggestions", () => {
  assert.throws(() => render("308 Winchestr"), (e) => e instanceof UnknownCartridgeError && e.suggestions.includes("308 Winchester"));
});

for (const round of all) {
  test(`profile is well formed: ${round.name}`, () => {
    const p = profile(round);
    const pts = p.case;
    assert.deepEqual(pts[0], [0, 0], "starts at the center of the head");
    assert.equal(pts.at(-1)[1], 0, "ends on the axis at the mouth");
    for (let i = 1; i < pts.length; i++) {
      assert.ok(pts[i][0] >= pts[i - 1][0] - 1e-9, `x never runs backwards (point ${i}: ${pts[i]} after ${pts[i - 1]})`);
      assert.ok(Number.isFinite(pts[i][0]) && Number.isFinite(pts[i][1]) && pts[i][1] >= 0, `finite point ${i}`);
    }
    if (p.bullet) {
      const b = p.bullet;
      assert.ok(b.start < b.tip && b.noseStart >= b.start && b.noseStart <= b.tip, "bullet sections in order");
      assert.ok(b.meplat >= 0 && b.meplat <= b.radius, "meplat within the shank");
    }
    const svg = render(round);
    assert.match(svg, /^<svg [^>]*viewBox="0 0 [\d.]+ [\d.]+"/);
    assert.doesNotMatch(svg, /NaN|undefined|Infinity/);
  });
}

test("options: size fitting, orientation, no bullet, colors", () => {
  const w = render("30-06 Springfield", { width: 300 });
  assert.match(w, /width="300"/);
  const h = render("30-06 Springfield", { height: 60 });
  assert.match(h, /height="60"/);
  const v = render("30-06 Springfield", { orientation: "vertical", scale: 50 });
  const [, vw, vh] = v.match(/width="([\d.]+)" height="([\d.]+)"/);
  assert.ok(Number(vh) > Number(vw), "vertical is taller than wide");
  assert.doesNotMatch(render("30-06 Springfield", { bullet: "none" }), /ammo-bullet/);
  assert.match(render("9mm", { stroke: "#a00", caseFill: "gold" }), /stroke="#a00".*fill="gold"/);
  assert.doesNotMatch(render("9mm", { title: false }), /<title>/);
  assert.match(render("9mm", { title: "<x>" }), /<title>&lt;x&gt;<\/title>/);
});

test("auto noses follow the cartridge type", () => {
  assert.equal(profile(find("308 Winchester")).bullet.shape, "spitzer");
  assert.equal(profile(find("45-70 Government")).bullet.shape, "flatnose");
  assert.equal(profile(find("9mm Luger")).bullet.shape, "roundnose");
  assert.equal(profile(find("38 Special Match")).bullet.shape, "wadcutter");
  assert.equal(profile(find("22 Long Rifle - Shot")).bullet, null);
});

test("geometry follows the SAAMI numbers", () => {
  const c = find("308 Winchester");
  const pts = profile(c).case;
  const at = (x) => pts.find((p) => Math.abs(p[0] - x) < 1e-9);
  assert.deepEqual(at(c.shoulderAt), [c.shoulderAt, c.shoulderDia / 2]);
  assert.deepEqual(at(c.neckAt), [c.neckAt, c.neckDia / 2]);
  assert.equal(Math.max(...pts.map((p) => p[0])), c.caseLength);
  assert.equal(profile(c).bullet.tip, c.oalMax);
  assert.equal(profile(c, { oal: "min" }).bullet.tip, c.oalMin);
});
