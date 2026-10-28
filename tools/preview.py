"""Build preview.html: every row of the four CSVs drawn as a profile outline at one shared scale.

A quick visual check of the transcribed data, not the real renderer.
usage: preview.py <out.html>
"""
import csv, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETS = [("Rifle", "rifle_cartridges.csv"), ("Pistol", "pistol_cartridges.csv"),
        ("Rimfire", "rimfire_cartridges.csv"), ("Shotshell", "shotshells.csv")]

data = {label: list(csv.DictReader(open(os.path.join(ROOT, "data", f), encoding="utf-8"))) for label, f in SETS}

HTML = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cartridge Data Preview</title>
<style>
:root { --bg:#fafaf8; --fg:#222; --muted:#777; --case:#b8860b; --bullet:#8a5a44; --line:#ddd; --bad:#c62828; }
@media (prefers-color-scheme: dark) { :root { --bg:#16171a; --fg:#e6e6e6; --muted:#999; --case:#e0b040; --bullet:#c99178; --line:#333; } }
body { margin:0; padding:16px; background:var(--bg); color:var(--fg); font:13px/1.4 system-ui, sans-serif; }
h1 { font-size:18px; margin:0 0 4px; } h2 { font-size:15px; margin:24px 0 8px; border-bottom:1px solid var(--line); padding-bottom:4px; }
.note { color:var(--muted); margin-bottom:12px; }
.grid { display:flex; flex-wrap:wrap; gap:6px 18px; }
.cell { display:flex; flex-direction:column; }
.cell svg { display:block; }
.name { font-size:11px; color:var(--muted); max-width:260px; }
.cell.warn .name { color:var(--bad); font-weight:600; }
svg path.case { fill:none; stroke:var(--case); stroke-width:1.2; vector-effect:non-scaling-stroke; }
svg path.bullet { fill:none; stroke:var(--bullet); stroke-width:1; stroke-dasharray:3 2; vector-effect:non-scaling-stroke; }
svg line.axis { stroke:var(--line); vector-effect:non-scaling-stroke; }
</style></head><body>
<h1>Cartridge data preview</h1>
<div class="note">Every CSV row drawn from its dimensions at one shared scale (PX px per inch). Case outline is solid,
the bullet is dashed (SAAMI gives no nose shape, so it is a generic ogive to OAL max). Red names failed a geometry check while drawing.</div>
<div id="out"></div>
<script>
const DATA = __DATA__;
const PX = 110;
const n = v => (v === "" || v == null) ? null : parseFloat(v);

// Top-half outline of a metallic case as [x, r] points, x from the head.
function caseProfile(c) {
  const rimR = n(c.rim_dia)/2, headR = n(c.head_dia)/2, rimT = n(c.rim_thickness);
  const land = n(c.rim_land) ?? rimT * 0.7;
  const ch = Math.min(0.012, rimT * 0.25);
  const p = [[0, 0], [0, rimR - ch], [ch, rimR], [land, rimR]];
  const grooveR = n(c.groove_dia)/2, gw = n(c.groove_width);
  let x = rimT;
  if (grooveR && gw) {                        // extractor groove (rimless, rebated, belted, semi-rimmed)
    p.push([rimT, grooveR], [rimT + gw, grooveR]);
    x = rimT + gw;
    const upTo = n(c.belt_dia) ? n(c.belt_dia)/2 : headR;
    const ang = (n(c.groove_angle_deg) ?? 35) * Math.PI / 180;
    x += (upTo - grooveR) / Math.tan(ang);
    p.push([x, upTo]);
    if (n(c.belt_dia)) { x = n(c.belt_length); p.push([x, upTo], [x, headR]); }
  } else {
    p.push([rimT, rimR], [rimT, headR]);      // rimmed / rimfire: flat rim face
  }
  const headAt = n(c.head_dia_at) ?? 0.2;
  if (headAt > x) p.push([headAt, headR]);
  if (n(c.body_dia_2)) p.push([n(c.body_dia_2_at), n(c.body_dia_2)/2]);
  const len = n(c.case_length);
  if (n(c.shoulder_at)) {
    const sR = (n(c.shoulder_dia) ?? n(c.body_dia_2) ?? n(c.head_dia))/2;
    p.push([n(c.shoulder_at), sR], [n(c.neck_at), n(c.neck_dia)/2]);
    p.push([len, (n(c.mouth_dia) ?? n(c.neck_dia))/2]);
  } else {
    p.push([len, (n(c.mouth_dia) ?? n(c.body_dia_2) ?? n(c.head_dia))/2]);
  }
  p.push([len, 0]);
  return p;
}

function bulletProfile(c) {
  const d = n(c.bullet_dia) ?? n(c.bullet_dia_lead);
  const oal = n(c.oal_max), len = n(c.case_length);
  if (!d || !oal) return null;
  const r = d/2, nose = Math.min(oal - len, r * 4);
  const base = oal - nose;
  return { r, len, base, oal };
}

function shellProfile(s) {
  const rimR = n(s.rim_dia)/2, headR = n(s.head_dia)/2, len = n(s.length_uncrimped);
  return [[0,0],[0,rimR],[n(s.rim_thickness),rimR],[n(s.rim_thickness),headR],[n(s.head_dia_at),headR],
          [len, n(s.mouth_dia)/2],[len,0]];
}

function check(c, p) {
  const bad = [];
  for (let i = 1; i < p.length; i++) if (p[i][0] < p[i-1][0] - 1e-9) bad.push(`x goes backwards at point ${i}`);
  for (const [x, r] of p) if (!isFinite(x) || !isFinite(r)) { bad.push("missing value"); break; }
  return bad;
}

const toPath = (pts, sx, cy) => {
  const top = pts.map(([x, r]) => [x*sx, cy - r*sx]);
  const bot = pts.slice().reverse().map(([x, r]) => [x*sx, cy + r*sx]);
  return "M" + top.concat(bot).map(([a, b]) => a.toFixed(1) + " " + b.toFixed(1)).join(" L") + " Z";
};

const out = document.getElementById("out");
for (const [label, rows] of Object.entries(DATA)) {
  const h = document.createElement("h2"); h.textContent = `${label} (${rows.length})`; out.appendChild(h);
  const grid = document.createElement("div"); grid.className = "grid"; out.appendChild(grid);
  const isShell = label === "Shotshell";
  for (const c of rows) {
    const pts = isShell ? shellProfile(c) : caseProfile(c);
    const b = isShell ? null : bulletProfile(c);
    const maxR = Math.max(...pts.map(q => q[1]));
    const W = ((isShell ? n(c.length_uncrimped) : (n(c.oal_max) ?? n(c.case_length))) + 0.05) * PX;
    const H = maxR * 2 * PX + 8, cy = H/2;
    let svg = `<svg width="${W.toFixed(0)}" height="${H.toFixed(0)}" viewBox="0 0 ${W.toFixed(1)} ${H.toFixed(1)}">`;
    svg += `<line class="axis" x1="0" y1="${cy}" x2="${W}" y2="${cy}"/>`;
    svg += `<path class="case" d="${toPath(pts, PX, cy)}"/>`;
    if (b) {
      const s = PX;
      svg += `<path class="bullet" d="M${b.len*s} ${cy-b.r*s} L${b.base*s} ${cy-b.r*s} Q${b.oal*s} ${cy-b.r*s} ${b.oal*s} ${cy} Q${b.oal*s} ${cy+b.r*s} ${b.base*s} ${cy+b.r*s} L${b.len*s} ${cy+b.r*s}"/>`;
    }
    svg += "</svg>";
    const problems = check(c, pts);
    const cell = document.createElement("div");
    cell.className = "cell" + (problems.length ? " warn" : "");
    cell.title = problems.join("; ") || `${c.rim_type ?? ""} ${c.profile ?? ""}`.trim();
    cell.innerHTML = svg + `<div class="name">${c.name} <span>p${c.pdf_page}</span></div>`;
    grid.appendChild(cell);
  }
}
</script></body></html>"""

with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write(HTML.replace("__DATA__", json.dumps(data)).replace("PX px", "110 px"))
print("wrote", sys.argv[1])
