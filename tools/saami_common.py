"""Shared engine for the transcribed SAAMI drawing datasets.

Each data_*.py module transcribes one SAAMI standard. Values are written as they
appear on the drawing (".394", "-.010"); the CSV normalises them to "0.394" /
"-0.010". All lengths are inches. Every value is cross-checked against the text
layer of the cartridge part of its PDF page.
"""
import csv, re
import pdfplumber

# Metallic cartridges (pistol, rifle, rimfire) share one schema.
CARTRIDGE_COLUMNS = [
    "name", "aliases", "pdf_page", "issued", "revised", "rim_type", "profile",
    "rim_dia", "rim_dia_tol", "rim_thickness", "rim_thickness_tol",
    "rim_land", "rim_land_tol", "rim_chamfer_deg", "rim_chamfer_tol_deg",
    "groove_dia", "groove_dia_tol", "groove_width", "groove_width_tol",
    "groove_angle_deg", "groove_angle_tol_deg",
    "belt_dia", "belt_length", "belt_length_tol",
    "body_dia_tol", "head_dia", "head_dia_at", "body_dia_2", "body_dia_2_at", "mouth_dia",
    "shoulder_dia", "shoulder_at", "shoulder_angle_deg",
    "datum_dia", "datum_at", "datum_at_tol", "neck_dia", "neck_at",
    "case_length", "case_length_tol",
    "bullet_dia", "bullet_dia_tol", "bullet_dia_lead", "bullet_dia_lead_tol",
    "oal_min", "oal_max", "notes",
]

SHOTSHELL_COLUMNS = [
    "name", "gauge", "shell_length", "barrel", "pdf_page", "issued", "revised",
    "rim_dia", "rim_dia_tol", "rim_thickness", "rim_thickness_tol",
    "rim_chamfer_deg", "rim_chamfer_basic_dia",
    "head_dia", "head_dia_tol", "head_dia_at",
    "mouth_dia", "mouth_dia_tol", "length_tol",
    "length_folded", "length_rolled", "length_uncrimped", "length_uncrimped_tol", "notes",
]

# Columns that are not printed on the drawing as-is (computed or descriptive).
UNCHECKED = {"name", "aliases", "pdf_page", "issued", "revised", "rim_type", "profile",
             "body_dia_2_at", "notes", "gauge", "shell_length", "barrel"}
TEXT_COLUMNS = {"name", "aliases", "notes", "gauge", "shell_length", "barrel"}

UNDERCUT = "Undercut ahead of rim is optional"


def at(*segments):
    """Distance from head for a chain of basic dimensions (.200 B + .500 B ...)."""
    return f"{sum(float(s) for s in segments):.4f}".rstrip("0")


class Dataset:
    def __init__(self, columns, defaults=None):
        self.columns = columns
        self.defaults = defaults or {}
        self.rows = []

    def row(self, **kw):
        self.rows.append({**self.defaults, **kw})


def norm(v):
    """'.394' -> '0.394', '-.010' -> '-0.010', '+20' -> '+20'."""
    return re.sub(r"(^|[+-])\.", r"\g<1>0.", v)


def cartridge_region_cut(page):
    """Top of the chamber part of a drawing page.

    The cartridge sits above a full-width rule (solid blue on most standards)
    or, failing that, above the boxed CHAMBER label.
    """
    h, w = page.height, page.width
    cuts = [e["top"] for e in page.edges
            if e["orientation"] == "h" and e["x1"] - e["x0"] > 0.6 * w and 0.3 * h < e["top"] < 0.75 * h]
    cuts += [wd["top"] for wd in page.extract_words()
             if wd["text"] == "CHAMBER" and wd["top"] > 0.25 * h]
    return min(cuts) if cuts else h * 0.5


def numbers_on_cartridge_part(page):
    top = page.crop((0, 0, page.width, cartridge_region_cut(page)))
    return set(re.findall(r"\d*\.\d+|\d+", top.extract_text() or ""))


def build(dataset, pdf_path, out_path):
    pdf = pdfplumber.open(pdf_path)
    problems = 0
    for r in dataset.rows:
        found = numbers_on_cartridge_part(pdf.pages[r["pdf_page"] - 1])
        # by_eye: columns converted from the drawing (e.g. 35°07'23" -> 35.1231),
        # so they cannot appear verbatim in the text layer.
        skip = UNCHECKED | set(r.get("by_eye", ()))
        for col, v in r.items():
            if col in skip or col == "by_eye" or v == "":
                continue
            if v.lstrip("+-") not in found:
                problems += 1
                print(f"NOT ON PAGE  p{r['pdf_page']} {r['name']}: {col}={v}")
        unknown = set(r) - set(dataset.columns) - {"by_eye"}
        if unknown:
            problems += 1
            print(f"UNKNOWN COLUMNS {r['name']}: {unknown}")

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=dataset.columns)
        w.writeheader()
        for r in dataset.rows:
            w.writerow({c: r.get(c, "") if c in TEXT_COLUMNS else norm(str(r.get(c, "")))
                        for c in dataset.columns})
    by_eye = sum(len(r.get("by_eye", ())) for r in dataset.rows)
    print(f"{len(dataset.rows)} rows written to {out_path}, {problems} problems, {by_eye} values verified by eye")
