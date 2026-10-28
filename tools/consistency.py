"""Cross-check redundant dimensions. The *Δ points on SAAMI drawings are theoretical sharp
corners, so the body line, shoulder line, datum and stated angle must agree.

usage: consistency.py <csv>...
"""
import csv, math, sys

def f(r, k):
    return float(r[k]) if r.get(k) else None

issues = 0
def report(path, r, msg):
    global issues
    issues += 1
    print(f"{path.split('_')[0]:7} p{r['pdf_page']:>3} {r['name']}: {msg}")

for path in sys.argv[1:]:
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        if "gauge" in r:
            continue
        h, h_at, b2, b2_at = f(r, "head_dia"), f(r, "head_dia_at") or .2, f(r, "body_dia_2"), f(r, "body_dia_2_at")
        s, s_at, d, d_at = f(r, "shoulder_dia"), f(r, "shoulder_at"), f(r, "datum_dia"), f(r, "datum_at")
        nk, n_at, ang = f(r, "neck_dia"), f(r, "neck_at"), f(r, "shoulder_angle_deg")
        # body taper extended to the shoulder should hit the shoulder diameter
        if b2 and s and s_at:
            pred = h + (b2 - h) * (s_at - h_at) / (b2_at - h_at)
            if abs(pred - s) > .0015:
                report(path, r, f"body line predicts shoulder dia {pred:.4f}, table says {s}")
        # shoulder line: angle, and datum lying on it
        if s and nk and s_at and n_at:
            calc = math.degrees(math.atan(((s - nk) / 2) / (n_at - s_at)))
            if ang and abs(calc - ang) > .4:
                report(path, r, f"shoulder angle from points {calc:.2f}°, table says {ang}°")
            if d and d_at:
                pred = s + (nk - s) * (d_at - s_at) / (n_at - s_at)
                if abs(pred - d) > .0015:
                    report(path, r, f"shoulder line at datum gives {pred:.4f}, datum is {d}")
        # case length past the neck start, OAL past case
        if n_at and f(r, "case_length") <= n_at:
            if abs(f(r, "case_length") - n_at) > 1e-6:
                report(path, r, "neck starts beyond case mouth")
print(f"{issues} inconsistencies")
