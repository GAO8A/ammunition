"""ANSI/SAAMI Z299.2 Shotshell cartridge drawings (PDF pages 27-40).

Lengths carry the drawing's general tolerance (length_tol, -.250) unless the
uncrimped length states its own. head_dia is measured at head_dia_at, the
reference distance from the head where the 55° rim chamfer meets the body.
"""
from saami_common import SHOTSHELL_COLUMNS, Dataset

DATA = Dataset(SHOTSHELL_COLUMNS, dict(rim_chamfer_deg="55", head_dia_tol="-.0090", length_tol="-.250",
                                       notes="Rim radius .015 max; cap height optional"))
row = DATA.row

GAUGES = {
    "10": dict(rim_dia=".933", rim_dia_tol="-.027", rim_thickness=".0624", rim_thickness_tol="-.0160",
               rim_chamfer_basic_dia=".8900", head_dia=".8540", head_dia_at=".075",
               mouth_dia=".840", mouth_dia_tol="-.020"),
    "12": dict(rim_dia=".886", rim_dia_tol="-.021", rim_thickness=".0576", rim_thickness_tol="-.0140",
               rim_chamfer_basic_dia=".8500", head_dia=".8090", head_dia_at=".072",
               mouth_dia=".797", mouth_dia_tol="-.020"),
    "16": dict(rim_dia=".819", rim_dia_tol="-.019", rim_thickness=".0506", rim_thickness_tol="-.0140",
               rim_chamfer_basic_dia=".7850", head_dia=".7440", head_dia_at=".065",
               mouth_dia=".731", mouth_dia_tol="-.020"),
    "20": dict(rim_dia=".766", rim_dia_tol="-.018", rim_thickness=".0484", rim_thickness_tol="-.0140",
               rim_chamfer_basic_dia=".7300", head_dia=".6970", head_dia_at=".060",
               mouth_dia=".684", mouth_dia_tol="-.020"),
    "28": dict(rim_dia=".687", rim_dia_tol="-.017", rim_thickness=".0508", rim_thickness_tol="-.0140",
               rim_chamfer_basic_dia=".6550", head_dia=".6260", head_dia_at=".061",
               mouth_dia=".613", mouth_dia_tol="-.020"),
    "410": dict(rim_dia=".535", rim_dia_tol="-.016", rim_thickness=".0532", rim_thickness_tol="-.0140",
                rim_chamfer_basic_dia=".5050", head_dia=".4770", head_dia_at=".063",
                mouth_dia=".462", mouth_dia_tol="-.014"),
}

def shell(gauge, length, barrel, page, issued, revised, **lengths):
    unit = "Bore" if gauge == "410" else "Gauge"
    row(name=f'{gauge} {unit} {length}" {barrel}', gauge=gauge, shell_length=length, barrel=barrel,
        pdf_page=page, issued=issued, revised=revised, **GAUGES[gauge], **lengths)

shell("10", "3-1/2", "Smooth Bore", 27, "1988-08-01", "2018-12-24",
      length_folded="3.110", length_rolled="3.290", length_uncrimped="3.510")
shell("12", "2-3/4", "Smooth Bore", 28, "1979-05-29", "2018-12-24",
      length_folded="2.405", length_rolled="2.450", length_uncrimped="2.760", length_uncrimped_tol="-.100")
shell("12", "2-3/4", "Rifled", 29, "1991-08-26", "",
      length_rolled="2.450", length_uncrimped="2.760", length_uncrimped_tol="-.200")
shell("12", "3", "Smooth Bore", 30, "1979-05-29", "2018-12-24",
      length_folded="2.655", length_rolled="2.760", length_uncrimped="3.010", length_uncrimped_tol="-.100")
shell("12", "3", "Rifled", 31, "1979-05-29", "2010-06-16",
      length_rolled="2.760", length_uncrimped="3.010", length_uncrimped_tol="-.150")
shell("12", "3-1/2", "Smooth Bore", 32, "1988-08-01", "2018-12-24",
      length_folded="3.155", length_rolled="3.155", length_uncrimped="3.510")
shell("16", "2-3/4", "Smooth Bore", 33, "1979-05-29", "2018-12-24",
      length_folded="2.440", length_rolled="2.475", length_uncrimped="2.760", length_uncrimped_tol="-.100")
shell("20", "2-3/4", "Smooth Bore", 34, "1979-05-29", "2018-12-24",
      length_folded="2.445", length_rolled="2.550", length_uncrimped="2.760", length_uncrimped_tol="-.100")
shell("20", "2-3/4", "Rifled", 35, "1992-01-08", "2004-06-24",
      length_rolled="2.550", length_uncrimped="2.760", length_uncrimped_tol="-.100")
shell("20", "3", "Smooth Bore", 36, "1979-05-29", "2018-12-24",
      length_folded="2.695", length_rolled="2.800", length_uncrimped="3.010", length_uncrimped_tol="-.100")
shell("20", "3", "Rifled", 37, "2004-02-10", "",
      length_rolled="2.800", length_uncrimped="3.010", length_uncrimped_tol="-.150")
shell("28", "2-3/4", "Smooth Bore", 38, "1979-05-29", "2018-12-24",
      length_folded="2.500", length_rolled="2.560", length_uncrimped="2.760", length_uncrimped_tol="-.100")
shell("410", "2-1/2", "Smooth Bore", 39, "1979-05-29", "2018-12-24",
      length_folded="2.360", length_rolled="2.400", length_uncrimped="2.530", length_uncrimped_tol="-.100")
shell("410", "3", "Smooth Bore", 40, "1979-05-29", "2018-12-24",
      length_folded="2.840", length_rolled="2.900", length_uncrimped="3.010", length_uncrimped_tol="-.100")

# The 12 ga 2-3/4" rifled rim label overlaps another, so its text-layer glyphs interleave; confirmed by eye.
DATA.rows[2]["by_eye"] = ("rim_dia", "rim_dia_tol")
