"""Geometric sanity checks for the cartridge CSVs (pistol, rifle, rimfire) and shotshells.

usage: sanity.py <csv>...
"""
import csv, sys

def check_cartridge(r):
    g = lambda k: float(r[k]) if r[k] else None
    out = [("rim_thickness > rim_land", g("rim_land") is None or g("rim_thickness") > g("rim_land"))]
    if g("groove_dia") and g("groove_width"):
        out.append(("rim_dia > groove_dia", g("rim_dia") > g("groove_dia")))
    if g("body_dia_2"):
        out.append(("head >= body_2", g("head_dia") >= g("body_dia_2")))
    if g("mouth_dia") and not g("neck_dia"):
        out.append(("body >= mouth", (g("body_dia_2") or g("head_dia")) >= g("mouth_dia")))
    if g("shoulder_at"):
        out.append(("shoulder <= datum <= neck <= case",
                    g("shoulder_at") <= g("datum_at") <= g("neck_at") <= g("case_length")))
        if g("shoulder_dia"):
            out.append(("shoulder_dia > datum_dia > neck_dia",
                        g("shoulder_dia") > g("datum_dia") > g("neck_dia")))
        if g("body_dia_2"):
            out.append(("body_2 >= shoulder_dia", g("body_dia_2") >= (g("shoulder_dia") or 0)))
    bullet = g("bullet_dia") or g("bullet_dia_lead")
    mouth = g("neck_dia") or g("mouth_dia") or g("body_dia_2") or g("head_dia")
    if bullet:
        out.append(("bullet < mouth", bullet < mouth))
    if g("oal_min"):
        out.append(("case < oal_min <= oal_max", g("case_length") < g("oal_min") <= g("oal_max")))
    else:
        out.append(("case < oal_max", g("case_length") < g("oal_max")))
    d = g("rim_dia") - (g("belt_dia") or g("head_dia"))
    # Rims up to .010 under the head (9.3x62, 370 Sako, 376 Steyr) are conventionally called rimless.
    kind = "rebated" if d < -0.010 else "rimmed" if d > 0.03 else "semi-rimmed" if d > 0.012 else "rimless"
    if r["rim_type"] == "belted":
        kind = "belted" if g("belt_dia") else "belted?"
    out.append((f"rim_type {r['rim_type']} ~ {kind}", kind == r["rim_type"]))
    return out

def check_shotshell(r):
    g = lambda k: float(r[k]) if r[k] else None
    return [("rim > head > mouth", g("rim_dia") > g("head_dia") > g("mouth_dia")),
            ("rolled <= uncrimped", g("length_rolled") <= g("length_uncrimped")),
            ("folded <= rolled", g("length_folded") is None or g("length_folded") <= g("length_rolled"))]

# Known, correct deviations from the heuristics above.
EXPECTED = {
    ("38 Special Match", "case < oal_min <= oal_max"),   # wadcutter seated flush with the mouth
    ("30 Remington AR", "rim_type rebated ~ rimless"),   # rim .008 under head; designated rebated
}

bad = 0
for path in sys.argv[1:]:
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    check = check_shotshell if "gauge" in rows[0] else check_cartridge
    for r in rows:
        for name, ok in check(r):
            if not ok and (r["name"], name) not in EXPECTED:
                bad += 1
                print(f"FAIL {path} {r['name']}: {name}")
print(f"{bad} failures")
