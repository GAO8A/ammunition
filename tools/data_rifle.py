"""SAAMI Z299.4-2025 Centerfire Rifle cartridge drawings (PDF pages 44-174).

Toleranced values are written "value tol" (rim_dia=".441 -.010") and split into
the value and *_tol columns.
"""
from saami_common import CARTRIDGE_COLUMNS, UNDERCUT, Dataset, at

DATA = Dataset(CARTRIDGE_COLUMNS, dict(rim_chamfer_deg="35", rim_chamfer_tol_deg="+20", head_dia_at=".200"))

TOLERANCED = {"rim_dia", "rim_thickness", "rim_land", "groove_dia", "groove_width", "groove_angle_deg",
              "belt_length", "datum_at", "case_length", "bullet_dia", "bullet_dia_lead"}

def row(**kw):
    out = {}
    for k, v in kw.items():
        if k in TOLERANCED and " " in v:
            tol_col = "groove_angle_tol_deg" if k == "groove_angle_deg" else f"{k}_tol"
            v, out[tol_col] = v.split()
        out[k] = v
    DATA.row(**out)

STD_RADII = "Shoulder radius .030+.050; neck radius .125 max"

row(name="6mm Advanced Rifle Cartridge", aliases="6mm ARC", pdf_page=44, issued="2020-01-20", revised="2021-11-17",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".441 -.010", rim_thickness=".059 -.010", rim_land=".044 -.010", groove_dia=".376 -.020",
    groove_width=".047 +.010", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".4410", body_dia_2=".4315", body_dia_2_at=at(".200", ".800"),
    shoulder_dia=".4301", shoulder_at="1.1207", shoulder_angle_deg="30",
    datum_dia=".350", datum_at="1.190 -.007", neck_dia=".274", neck_at="1.2558",
    case_length="1.490 -.020", bullet_dia=".2433 -.0030", oal_min="2.135", oal_max="2.260", notes=STD_RADII)
row(name="6mm Creedmoor", aliases="6mm CM", pdf_page=45, issued="2017-06-14", revised="2021-11-17",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".472 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4629", body_dia_2_at=at(".200", "1.150"),
    shoulder_dia=".4620", shoulder_at="1.4901", shoulder_angle_deg="30",
    datum_dia=".400", datum_at="1.5438 -.0070", neck_dia=".276", neck_at="1.6512",
    case_length="1.920 -.020", bullet_dia=".2434 -.0030", oal_min="2.550", oal_max="2.800", notes=STD_RADII)
row(name="6mm GT", pdf_page=46, issued="2022-01-16", revised="",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".471 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4601", body_dia_2_at=at(".200", "1.000"),
    shoulder_dia=".4590", shoulder_at="1.3040", shoulder_angle_deg="35",
    datum_dia=".375", datum_at="1.364 -.007", neck_dia=".273", neck_at="1.4368",
    case_length="1.725 -.020", bullet_dia=".2433 -.0030", oal_min="2.515", oal_max="2.640", notes=STD_RADII)
row(name="6mm Remington", aliases="6mm Rem", pdf_page=47, issued="1979-05-29", revised="2021-11-17",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.011", rim_thickness=".049 -.011", rim_land=".034 -.010", groove_dia=".408 -.020",
    groove_width=".037 +.010", groove_angle_deg="34 -6", body_dia_tol="-.008",
    head_dia=".4711", body_dia_2=".4308", body_dia_2_at=at(".200", "1.475"),
    shoulder_dia=".4294", shoulder_at="1.7249", shoulder_angle_deg="26",
    datum_dia=".375", datum_at="1.7807 -.0070", neck_dia=".276", neck_at="1.8822",
    case_length="2.233 -.020", bullet_dia=".2435 -.0030", oal_min="2.730", oal_max="2.825",
    notes="Shoulder radius .025+.050; neck radius .100 max")
row(name="6.5 Creedmoor", aliases="6.5 CM", pdf_page=48, issued="2009-06-17", revised="2021-11-16",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".472 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4629", body_dia_2_at=at(".200", "1.150"),
    shoulder_dia=".4620", shoulder_at="1.4901", shoulder_angle_deg="30",
    datum_dia=".400", datum_at="1.5438 -.0070", neck_dia=".295", neck_at="1.6347",
    case_length="1.920 -.020", bullet_dia=".2644 -.0030", oal_min="2.700", oal_max="2.825", notes=STD_RADII)
row(name="6.5 Grendel", aliases="6.5 Gren", pdf_page=49, issued="2011-01-17", revised="2021-11-18",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".441 -.010", rim_thickness=".059 -.010", rim_land=".044 -.010", groove_dia=".378 -.020",
    groove_width=".047 +.010", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".4410", body_dia_2=".4318", body_dia_2_at=at(".200", ".800"),
    shoulder_dia=".4301", shoulder_at="1.1507", shoulder_angle_deg="30",
    datum_dia=".350", datum_at="1.220 -.007", neck_dia=".2930", neck_at="1.2694",
    case_length="1.520 -.020", bullet_dia=".2643 -.0030", oal_min="2.135", oal_max="2.260",
    notes="Shoulder radius .030+.050; neck radius .050 max; drawing is watermarked as superseded by an updated drawing")
row(name="6.5 Precision Rifle Cartridge", aliases="6.5 PRC", pdf_page=50, issued="2018-06-13", revised="2021-11-18",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".532 -.010", rim_thickness=".050 -.010", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="35 -6", body_dia_tol="-.008",
    head_dia=".5320", body_dia_2=".5166", body_dia_2_at=at(".200", "1.300"),
    shoulder_dia=".5158", shoulder_at="1.5687", shoulder_angle_deg="30",
    datum_dia=".420", datum_at="1.6517 -.0070", neck_dia=".297", neck_at="1.7582",
    case_length="2.030 -.020", bullet_dia=".2644 -.0030", oal_min="2.755", oal_max="2.955", notes=STD_RADII)
row(name="6.5 Weatherby Rebated Precision Magnum", aliases="6.5 Wby RPM", pdf_page=51,
    issued="2020-09-23", revised="2021-11-18", rim_type="rebated", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".040 +.010", groove_angle_deg="40 -6", body_dia_tol="-.008",
    head_dia=".5000", body_dia_2=".4780", body_dia_2_at=at(".200", "1.650"),
    shoulder_dia=".4739", shoulder_at="2.1603", shoulder_angle_deg="35",
    datum_dia=".400", datum_at="2.213 -.007", neck_dia=".295", neck_at="2.288",
    case_length="2.570 -.020", bullet_dia=".2643 -.0030", oal_min="3.200", oal_max="3.340",
    notes="Shoulder radius .039+.050; neck radius .100 max")
row(name="6.5-284 Norma", pdf_page=52, issued="2019-06-18", revised="2024-10-11",
    rim_type="rebated", profile="bottleneck",
    rim_dia=".4728 -.0100", rim_thickness="0.054 -.010", rim_land=".040 -.010", groove_dia=".4091 -.0200",
    groove_width=".040 +.010", groove_angle_deg="40 -6", body_dia_tol="-.008",
    head_dia=".5000", body_dia_2=".4759", body_dia_2_at=at(".200", "1.500"),
    shoulder_dia=".4748", shoulder_at="1.7708", shoulder_angle_deg="35.1231",
    datum_dia=".385", datum_at="1.8350 -.0071", neck_dia=".2965", neck_at="1.8975",
    case_length="2.1701 -.0201", bullet_dia=".2642 -.0030", oal_min="2.8740", oal_max="3.2283",
    by_eye=("shoulder_angle_deg",),
    notes="Metric-origin drawing (mm primary; inch values used here); shoulder angle 35°07'23\" B; "
          "shoulder radius .030 min; neck radius .125 max")
row(name="6.5-300 Weatherby Magnum", aliases="6.5-300 Wby Mag", pdf_page=53, issued="2017-01-16", revised="2024-01-21",
    rim_type="belted", profile="bottleneck",
    rim_dia=".5315 -.0100", rim_thickness=".051 -.011", rim_land=".039 -.010", groove_dia=".457 -.020",
    groove_width=".049 +.010", groove_angle_deg="45", belt_dia=".5315", belt_length=".219 -.008",
    body_dia_tol="-.008", head_dia=".5117", head_dia_at=".250", body_dia_2=".4949", body_dia_2_at=at(".250", "1.750"),
    shoulder_dia=".4920", shoulder_at="2.2986",
    datum_dia=".4107", datum_at="2.3924 -.0080", neck_dia=".295", neck_at="2.5255",
    case_length="2.825 -.020", bullet_dia=".2644 -.0030", oal_min="3.450", oal_max="3.600",
    notes="Belt dia tol -.0050; head dia tol -.0040; radiused (venturi) shoulder: "
          "shoulder radius .125+.005, neck radius .182-.005, no shoulder angle")
row(name="6.5x55 Swedish", aliases="6.5x55", pdf_page=54, issued="1993-07-28", revised="2021-12-03",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".4803 -.0100", rim_thickness=".0591 -.0100", rim_land=".039 -.010", groove_dia=".4134 -.0200",
    groove_width=".0354 +.0100", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".4782", body_dia_2=".4364", body_dia_2_at=at(".200", "1.450"),
    shoulder_dia=".4346", shoulder_at="1.7122", shoulder_angle_deg="25.25",
    datum_dia=".365", datum_at="1.786 -.007", neck_dia=".2992", neck_at="1.8558", mouth_dia=".2965",
    case_length="2.165 -.020", bullet_dia=".2642 -.0030", oal_min="2.755", oal_max="2.955",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 25°15' B; neck tapers from .2992 to .2965 at mouth; "
          "shoulder radius .102+.030; neck radius .122 max")
row(name="6.8 True Velocity Composite", aliases="6.8 TVC", pdf_page=55, issued="2022-01-16", revised="2023-06-27",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".472 -.010", rim_thickness=".054 -.010", rim_land=".041 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4705", body_dia_2=".4626", body_dia_2_at=at(".200", "1.500"),
    shoulder_dia=".4619", shoulder_at="1.8234", shoulder_angle_deg="30",
    datum_dia=".392", datum_at="1.884 -.007", neck_dia=".318", neck_at="1.9481", case_length="1.9481",
    bullet_dia=".2777 -.0030", oal_min="2.685", oal_max="2.810",
    notes="Polymer case with no neck: the shoulder ends at the mouth, so neck_at = case_length (reference); "
          "SAAMI warns MAP above 65,000 psi; shoulder radius .135+.030; mouth radius .006 max")
row(name="6.8 Western", pdf_page=56, issued="2020-09-23", revised="2021-11-17",
    rim_type="rebated", profile="bottleneck",
    rim_dia=".535 -.010", rim_thickness=".054 -.010", rim_land=".040 -.010", groove_dia=".480 -.020",
    groove_width=".040 +.010", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".5550", body_dia_2=".5391", body_dia_2_at=at(".200", "1.300"),
    shoulder_dia=".5381", shoulder_at="1.5835", shoulder_angle_deg="35",
    datum_dia=".445", datum_at="1.650 -.007", neck_dia=".314", neck_at="1.7435",
    case_length="2.020 -.020", bullet_dia=".278 -.003", oal_min="2.755", oal_max="2.955",
    notes="Shoulder radius .050+.050; neck radius .100 max")
row(name="6.8mm Remington SPC", aliases="6.8mm Rem SPC", pdf_page=57, issued="2004-06-23", revised="2022-10-26",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".422 -.010", rim_thickness=".049 -.011", rim_land=".034 -.010", groove_dia=".358 -.020",
    groove_width=".033 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4207", body_dia_2=".4032", body_dia_2_at=at(".200", "1.000"),
    shoulder_dia=".4014", shoulder_at="1.3012", shoulder_angle_deg="23",
    datum_dia=".360", datum_at="1.350 -.007", neck_dia=".306", neck_at="1.4136",
    case_length="1.6864 -.0200", bullet_dia=".278 -.003", oal_min="2.000", oal_max="2.260",
    notes="Shoulder radius .025+.050; neck radius .100 max")
row(name="7mm Mauser", aliases="7x57; 7mm (7 x 57)", pdf_page=58, issued="1979-05-29", revised="2022-10-04",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".049 -.010", rim_land=".034 -.010", groove_dia=".409 -.020",
    groove_width=".033 +.010", groove_angle_deg="32 -6", body_dia_tol="-.008",
    head_dia=".4711", body_dia_2=".4315", body_dia_2_at=at(".200", "1.450"),
    shoulder_dia=".4294", shoulder_at="1.7277", shoulder_angle_deg="20.75",
    datum_dia=".375", datum_at="1.7995 -.007", neck_dia=".3243", neck_at="1.8664", mouth_dia=".3207",
    case_length="2.235 -.020", bullet_dia=".2845 -.0030", oal_min="2.850", oal_max="3.065",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 20°45' B; neck tapers from .3243 to .3207 at mouth; "
          "shoulder radius .030+.050; neck radius .150 max")
row(name="7mm Precision Rifle Cartridge", aliases="7mm PRC", pdf_page=59, issued="2022-06-07", revised="",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".532 -.010", rim_thickness=".050 -.010", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="35 -6", body_dia_tol="-.008",
    head_dia=".5320", body_dia_2=".5187", body_dia_2_at=at(".200", "1.500"),
    shoulder_dia=".5176", shoulder_at="1.8194", shoulder_angle_deg="30",
    datum_dia=".420", datum_at="1.904 -.007", neck_dia=".317", neck_at="1.9932",
    case_length="2.280 -.020", bullet_dia=".2844 -.0030", oal_min="3.090", oal_max="3.340", notes=STD_RADII)
row(name="7mm Remington Magnum", aliases="7mm Rem Mag", pdf_page=60, issued="1980-04-21", revised="2021-12-06",
    rim_type="belted", profile="bottleneck",
    rim_dia=".532 -.010", rim_thickness=".050 -.011", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="35 -6", belt_dia=".532", belt_length=".220 -.008",
    body_dia_tol="-.008", head_dia=".5127", head_dia_at=".250", body_dia_2=".4918", body_dia_2_at=at(".250", "1.720"),
    shoulder_dia=".4909", shoulder_at="2.0401", shoulder_angle_deg="25",
    datum_dia=".420", datum_at="2.1162 -.0070", neck_dia=".315", neck_at="2.2288",
    case_length="2.500 -.020", bullet_dia=".2845 -.0030", oal_min="3.150", oal_max="3.290",
    notes="Belt dia .532-.005 cylindrical; shoulder radius .040+.050; neck radius .150 max")
row(name="7mm Remington Short Action Ultra Magnum", aliases="7mm Rem SA Ultra Mag; 7mm RSAUM", pdf_page=61,
    issued="2002-02-01", revised="2021-12-06", rim_type="rebated", profile="bottleneck",
    rim_dia=".534 -.010", rim_thickness=".050 -.011", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="32 -6", body_dia_tol="-.008",
    head_dia=".5500", body_dia_2=".5357", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".5347", shoulder_at="1.5383", shoulder_angle_deg="30",
    datum_dia=".460", datum_at="1.603 -.007", neck_dia=".320", neck_at="1.7242",
    case_length="2.035 -.020", bullet_dia=".2845 -.0030", oal_min="2.450", oal_max="2.825", notes=STD_RADII)
row(name="7mm Remington Ultra Magnum", aliases="7mm Rem Ultra Mag; 7mm RUM", pdf_page=62,
    issued="2002-02-01", revised="2021-12-07", rim_type="rebated", profile="bottleneck",
    rim_dia=".534 -.010", rim_thickness=".050 -.011", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="32 -6", body_dia_tol="-.008",
    head_dia=".5500", body_dia_2=".5300", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".5250", shoulder_at="2.3873", shoulder_angle_deg="30",
    datum_dia=".420", datum_at="2.4782 -.0070", neck_dia=".322", neck_at="2.5631",
    case_length="2.850 -.020", bullet_dia=".2845 -.0030", oal_min="3.450", oal_max="3.600",
    notes="Shoulder radius .050+.030; neck radius .125 max")
row(name="7mm Weatherby Magnum", aliases="7mm Wby Mag", pdf_page=63, issued="1991-06-04", revised="2024-01-21",
    rim_type="belted", profile="bottleneck",
    rim_dia=".5315 -.0100", rim_thickness=".051 -.011", rim_land=".034 -.010", groove_dia=".457 -.020",
    groove_width=".049 +.010", groove_angle_deg="45", belt_dia=".532", belt_length=".219 -.006",
    body_dia_tol="-.006", head_dia=".5117", head_dia_at=".250", body_dia_2=".4921", body_dia_2_at=at(".250", "1.750"),
    shoulder_dia=".492", shoulder_at="2.012",
    datum_dia=".4086", datum_at="2.1073 -.0080", neck_dia=".314", neck_at="2.218",
    case_length="2.549 -.012", bullet_dia=".2843 -.0030", oal_min="3.100", oal_max="3.360",
    notes="Belt dia .532-.005 cylindrical; head dia tol -.004; radiused (venturi) shoulder: "
          "shoulder radius .125+.005, neck radius .151-.005, no shoulder angle")
row(name="7mm Winchester Short Magnum", aliases="7mm WSM", pdf_page=64, issued="2002-06-26", revised="2022-01-11",
    rim_type="rebated", profile="bottleneck",
    rim_dia=".535 -.010", rim_thickness=".054 -.010", rim_land=".040 -.010", groove_dia=".480 -.020",
    groove_width=".040 +.010", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".5550", body_dia_2=".5400", body_dia_2_at=at(".200", "1.300"),
    shoulder_dia=".5377", shoulder_at="1.7018", shoulder_angle_deg="35",
    datum_dia=".445", datum_at="1.768 -.007", neck_dia=".321", neck_at="1.8565",
    case_length="2.100 -.020", bullet_dia=".2845 -.0030", oal_min="2.560", oal_max="2.860",
    notes="Shoulder radius .050+.050; neck radius .100 max")
row(name="7mm-08 Remington", aliases="7mm-08 Rem", pdf_page=65, issued="1980-04-21", revised="2022-02-18",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4553", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4540", shoulder_at="1.5598", shoulder_angle_deg="20",
    datum_dia=".400", datum_at="1.634 -.007", neck_dia=".315", neck_at="1.7508",
    case_length="2.035 -.020", bullet_dia=".2845 -.0030", oal_min="2.530", oal_max="2.800",
    notes="Shoulder radius .030+.030; neck radius .125 max")
row(name="7x64 Brenneke", aliases="7 x 64", pdf_page=66, issued="1993-07-28", revised="2024-06-17",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".4705 -.0100", rim_thickness=".051 -.010", rim_land=".039 -.010", groove_dia=".413 -.020",
    groove_width=".039 +.010", groove_angle_deg="36.8667", groove_angle_tol_deg="-6", body_dia_tol="-.008",
    head_dia=".4649", body_dia_2=".4291", body_dia_2_at=at(".200", "1.650"),
    shoulder_dia=".4253", shoulder_at="2.0276", shoulder_angle_deg="20.25",
    datum_dia=".375", datum_at="2.0957 -.0070", neck_dia=".313", neck_at="2.1797",
    case_length="2.5197 -.0200", bullet_dia=".2854 -.0030", oal_min="3.150", oal_max="3.307",
    by_eye=("groove_angle_deg", "shoulder_angle_deg"),
    notes="Groove angle 36°52'-6°; shoulder angle 20°15' B; shoulder radius .020+.050; neck radius .125 max")
row(name="7.62x39", aliases="7.62 x 39", pdf_page=67, issued="1988-08-01", revised="2022-02-28",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".447 -.010", rim_thickness=".057 -.010", rim_land=".042 -.010", groove_dia=".376 -.010",
    groove_width=".047 +.010", groove_angle_deg="48 -6", body_dia_tol="-.008",
    head_dia=".4430", body_dia_2=".4002", body_dia_2_at=at(".200", ".9083"),
    shoulder_dia=".3960", shoulder_at="1.1985", shoulder_angle_deg="17.5",
    datum_dia=".3622", datum_at="1.252 -.007", neck_dia=".339", neck_at="1.2888", mouth_dia=".337",
    case_length="1.528 -.015", bullet_dia=".311 -.002", oal_min="2.150", oal_max="2.200",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 17°30' B; neck tapers from .339 to .337 at mouth; "
          "shoulder radius .030+.050; neck radius .118 max")
row(name="8mm Mauser", aliases="8x57; 8mm (8 x 57)", pdf_page=68, issued="1980-04-21", revised="2022-03-02",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".049 -.010", rim_land=".034 -.010", groove_dia=".409 -.020",
    groove_width=".033 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4698", body_dia_2=".4340", body_dia_2_at=at(".200", "1.500"),
    shoulder_dia=".4310", shoulder_at="1.8273", shoulder_angle_deg="20.8",
    datum_dia=".392", datum_at="1.8786 -.0070", neck_dia=".3507", neck_at="1.9330", mouth_dia=".3493",
    case_length="2.240 -.020", bullet_dia=".323 -.003", oal_min="2.815", oal_max="3.250",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 20°48' B; neck tapers from .3507 to .3493 at mouth; "
          "shoulder radius .045+.050; neck radius .050 max")
row(name="9.3x62", aliases="9.3 x 62", pdf_page=69, issued="2013-01-14", revised="2022-03-07",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".470 -.010", rim_thickness=".051 -.010", rim_land=".039 -.010", groove_dia=".413 -.020",
    groove_width=".039 +.010", groove_angle_deg="42 -6", body_dia_tol="-.008",
    head_dia=".4754", body_dia_2=".4513", body_dia_2_at=at(".200", "1.800"),
    shoulder_dia=".4508", shoulder_at="2.0390", shoulder_angle_deg="17.4747",
    datum_dia=".420", datum_at="2.0879 -.0070", neck_dia=".3906", neck_at="2.1347",
    case_length="2.441 -.020", bullet_dia=".3661 -.0030", oal_max="3.291",
    by_eye=("shoulder_angle_deg",),
    notes="Metric-origin drawing (mm primary; inch values used here); shoulder angle 17°28'29\" B; "
          "only a maximum overall length is specified; shoulder radius .020+.050; neck radius .020 max")
row(name="17 Hornet", pdf_page=70, issued="2012-06-06", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".350 -.010", rim_thickness=".065 -.010", rim_land=".050 -.010", groove_dia=".2989",
    body_dia_tol="-.008", head_dia=".2982", body_dia_2=".2945", body_dia_2_at=at(".200", ".750"),
    shoulder_dia=".2940", shoulder_at="1.0471", shoulder_angle_deg="25",
    datum_dia=".240", datum_at="1.105 -.015", neck_dia=".194", neck_at="1.1543",
    case_length="1.350 -.020", bullet_dia=".1725 -.0030", oal_min="1.595", oal_max="1.720",
    notes="groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; shoulder radius .025+.050; neck radius .075 max")
REM_223_HEAD = dict(rim_type="rimless", profile="bottleneck",
    rim_dia=".378 -.010", rim_thickness=".045 -.010", rim_land=".027 -.010", groove_dia=".332 -.020",
    groove_width=".030 +.010", groove_angle_deg="25 -6", body_dia_tol="-.008", head_dia=".3759")
row(name="17 Remington", aliases="17 Rem", pdf_page=71, issued="1980-04-21", revised="2022-03-16", **REM_223_HEAD,
    body_dia_2=".3584", body_dia_2_at=at(".200", "1.000"),
    shoulder_dia=".3558", shoulder_at="1.3511", shoulder_angle_deg="23",
    datum_dia=".330", datum_at="1.3814 -.0070", neck_dia=".199", neck_at="1.5357",
    case_length="1.796 -.020", bullet_dia=".1725 -.0030", oal_min="2.090", oal_max="2.150",
    notes="Shoulder radius .025+.050; neck radius .100 max")
row(name="17 Remington Fireball", aliases="17 Rem Fireball", pdf_page=72, issued="2007-06-13", revised="2022-03-17",
    **REM_223_HEAD, body_dia_2=".3663", body_dia_2_at=at(".200", ".800"),
    shoulder_dia=".3655", shoulder_at="1.0648", shoulder_angle_deg="30",
    datum_dia=".300", datum_at="1.1215 -.0070", neck_dia=".204", neck_at="1.2046",
    case_length="1.410 -.020", bullet_dia=".1725 -.0030", oal_min="1.660", oal_max="1.830",
    notes="Shoulder radius .025+.050; neck radius .100 max")
row(name="204 Ruger", pdf_page=73, issued="2004-06-23", revised="2023-04-24", **REM_223_HEAD,
    body_dia_2=".3615", body_dia_2_at=at(".200", "1.200"),
    shoulder_dia=".3598", shoulder_at="1.5386", shoulder_angle_deg="30",
    datum_dia=".330", datum_at="1.5645 -.0070", neck_dia=".231", neck_at="1.6502",
    case_length="1.850 -.020", bullet_dia=".2045 -.0030", oal_min="2.125", oal_max="2.260",
    notes="Drawing prints rim dia mm as (8.43 - 0.25), apparently a typo for 9.60; "
          "shoulder radius .025+.050; neck radius .100 max")
row(name="218 Bee", pdf_page=74, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".408 -.010", rim_thickness=".065 -.010", rim_land=".050 -.010", groove_dia=".3491",
    body_dia_tol="-.008", head_dia=".3465", body_dia_2=".3335", body_dia_2_at=at(".200", ".665"),
    shoulder_dia=".3324", shoulder_at=".9233", shoulder_angle_deg="15",
    datum_dia=".2875", datum_at="1.007 -.015", neck_dia=".2435", neck_at="1.0891", mouth_dia=".242",
    case_length="1.345 -.020", bullet_dia=".2245 -.0030", oal_min="1.645", oal_max="1.680",
    notes="groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; neck tapers from .2435 to .242 at mouth; shoulder radius .025+.050; neck radius .100 max")
row(name="22 Advanced Rifle Cartridge", aliases="22 ARC", pdf_page=75, issued="2024-01-21", revised="",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".441 -.010", rim_thickness=".059 -.010", rim_land=".044 -.010", groove_dia=".378 -.020",
    groove_width=".047 +.010", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".4410", body_dia_2=".4315", body_dia_2_at=at(".200", ".800"),
    shoulder_dia=".4297", shoulder_at="1.1510", shoulder_angle_deg="30",
    datum_dia=".350", datum_at="1.220 -.007", neck_dia=".253", neck_at="1.3040",
    case_length="1.525 -.020", bullet_dia=".2244 -.0030", oal_min="2.060", oal_max="2.260", notes=STD_RADII)
row(name="22 Creedmoor", aliases="22 CM", pdf_page=76, issued="2024-01-21", revised="",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".472 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4629", body_dia_2_at=at(".200", "1.150"),
    shoulder_dia=".4620", shoulder_at="1.4901", shoulder_angle_deg="30",
    datum_dia=".400", datum_at="1.5438 -.007", neck_dia=".256", neck_at="1.6685",
    case_length="1.920 -.020", bullet_dia=".224 -.003", oal_min="2.450", oal_max="2.700",
    notes=STD_RADII + "; drawing is watermarked as superseded by an updated drawing")
row(name="22 Hornet", pdf_page=77, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".350 -.010", rim_thickness=".065 -.010", rim_land=".050 -.010", groove_dia=".2989",
    body_dia_tol="-.008", head_dia=".2952", body_dia_2=".2787", body_dia_2_at=at(".200", ".600"),
    shoulder_dia=".2773", shoulder_at=".8527", shoulder_angle_deg="5.6333",
    datum_dia=".262", datum_at=".930 -.015", neck_dia=".2448", neck_at="1.0172", mouth_dia=".2425",
    case_length="1.403 -.020", bullet_dia=".2245 -.0030", oal_min="1.630", oal_max="1.723",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 5°38' B; groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; neck tapers from .2448 to .2425 at mouth; shoulder radius .500+.100; neck radius .875 max")
row(name="22 Nosler", pdf_page=78, issued="2017-01-17", revised="2022-03-29",
    rim_type="rebated", profile="bottleneck",
    rim_dia=".378 -.010", rim_thickness=".045 -.010", rim_land=".027 -.010", groove_dia=".332 -.020",
    groove_width=".030 +.010", groove_angle_deg="27 -3", body_dia_tol="-.008",
    head_dia=".4207", body_dia_2=".4032", body_dia_2_at=at(".200", "1.000"),
    shoulder_dia=".3999", shoulder_at="1.3895", shoulder_angle_deg="30",
    datum_dia=".330", datum_at="1.450 -.007", neck_dia=".255", neck_at="1.5150",
    case_length="1.760 -.020", bullet_dia=".2245 -.0030", oal_min="2.135", oal_max="2.260",
    notes="Shoulder radius .025+.050; neck radius .100 max")
row(name="22-250 Remington", aliases="22-250 Rem", pdf_page=79, issued="1979-05-29", revised="2022-03-30",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".049 -.010", rim_land=".034 -.010", groove_dia=".409 -.020",
    groove_width=".033 +.010", groove_angle_deg="34 -6", body_dia_tol="-.008",
    head_dia=".4668", body_dia_2=".4172", body_dia_2_at=at(".200", "1.240"),
    shoulder_dia=".4142", shoulder_at="1.5148", shoulder_angle_deg="28",
    datum_dia=".347", datum_at="1.578 -.007", neck_dia=".256", neck_at="1.6636", mouth_dia=".254",
    case_length="1.912 -.020", bullet_dia=".2245 -.0030", oal_min="2.290", oal_max="2.350",
    notes="Neck tapers from .256 to .254 at mouth; shoulder radius .100+.050; neck radius .100 max")
row(name="220 Swift", pdf_page=80, issued="1988-08-01", revised="2022-03-30",
    rim_type="semi-rimmed", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".049 -.010", rim_land=".034 -.010", groove_dia=".426 -.020",
    groove_width=".025 +.010", groove_angle_deg="15 -6", body_dia_tol="-.008",
    head_dia=".4449", body_dia_2=".4055", body_dia_2_at=at(".200", "1.400"),
    shoulder_dia=".4020", shoulder_at="1.7227", shoulder_angle_deg="21",
    datum_dia=".335", datum_at="1.810 -.007", neck_dia=".2615", neck_at="1.9057", mouth_dia=".260",
    case_length="2.205 -.020", bullet_dia=".2245 -.0030", oal_min="2.650", oal_max="2.680",
    notes="Neck tapers from .2615 to .260 at mouth; shoulder radius .030+.050; neck radius .100 max")
row(name="221 Remington Fireball", aliases="221 Rem FB; 221 Rem Fireball", pdf_page=81,
    issued="1979-05-29", revised="2022-03-30", **REM_223_HEAD,
    body_dia_2=".3619", body_dia_2_at=at(".200", ".800"),
    shoulder_dia=".3607", shoulder_at="1.0707", shoulder_angle_deg="23",
    datum_dia=".330", datum_at="1.1068 -.0070", neck_dia=".253", neck_at="1.1975",
    case_length="1.400 -.020", bullet_dia=".2245 -.0030", oal_min="1.780", oal_max="1.830",
    notes="Rifle drawing; same case as the pistol standard. Drawing prints .800 B as (30.32) mm, "
          "apparently a typo for 20.32; shoulder radius .025+.025; neck radius .100 max")
row(name="222 Remington", aliases="222 Rem", pdf_page=82, issued="1979-05-29", revised="2022-03-31",
    **{**REM_223_HEAD, "groove_width": ".025 +.015"},
    body_dia_2=".3584", body_dia_2_at=at(".200", "1.000"),
    shoulder_dia=".3573", shoulder_at="1.2645", shoulder_angle_deg="23",
    datum_dia=".330", datum_at="1.2966 -.0070", neck_dia=".253", neck_at="1.3873",
    case_length="1.700 -.020", bullet_dia=".2245 -.0030", oal_min="2.040", oal_max="2.130",
    notes="Shoulder radius .025+.050; neck radius .100 max")
row(name="222 Remington Magnum", aliases="222 Rem Mag", pdf_page=83, issued="1980-04-21", revised="2022-04-04",
    **{**REM_223_HEAD, "head_dia": ".3754"},
    body_dia_2=".3580", body_dia_2_at=at(".200", "1.200"),
    shoulder_dia=".3571", shoulder_at="1.4636", shoulder_angle_deg="23",
    datum_dia=".330", datum_at="1.4955 -.0070", neck_dia=".253", neck_at="1.5862",
    case_length="1.850 -.020", bullet_dia=".2245 -.0030", oal_min="2.220", oal_max="2.280",
    notes="Shoulder radius .025+.050; neck radius .100 max")
row(name="223 Remington", aliases="223 Rem", pdf_page=84, issued="1980-04-21", revised="2023-09-25",
    **REM_223_HEAD, body_dia_2=".3584", body_dia_2_at=at(".200", "1.000"),
    shoulder_dia=".3542", shoulder_at="1.4381", shoulder_angle_deg="23",
    datum_dia=".330", datum_at="1.4666 -.0070", neck_dia=".253", neck_at="1.5573",
    case_length="1.760 -.030", bullet_dia=".2245 -.0030", oal_min="2.125", oal_max="2.260",
    notes="Shoulder radius .025+.050; neck radius .100 max")
row(name="223 Winchester Super Short Magnum", aliases="223 WSSM", pdf_page=85, issued="1980-04-21", revised="2022-04-04",
    rim_type="rebated", profile="bottleneck",
    rim_dia=".535 -.010", rim_thickness=".054 -.010", rim_land=".040 -.010", groove_dia=".480 -.020",
    groove_width=".040 +.010", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".5550", body_dia_2=".5461", body_dia_2_at=at(".200", ".800"),
    shoulder_dia=".5444", shoulder_at="1.1499", shoulder_angle_deg="28",
    datum_dia=".445", datum_at="1.2434 -.0070", neck_dia=".272", neck_at="1.4061",
    case_length="1.670 -.020", bullet_dia=".2245 -.0030", oal_min="2.060", oal_max="2.360",
    notes="Issued date printed as 04/21/1980 on the drawing; shoulder radius .050+.050; neck radius .130 max")
row(name="224 Valkyrie", aliases="224 VLK", pdf_page=86, issued="2018-01-22", revised="2021-11-16",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".422 -.010", rim_thickness=".049 -.010", rim_land=".034 -.010", groove_dia=".358 -.020",
    groove_width=".033 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4207", body_dia_2=".4067", body_dia_2_at=at(".200", ".800"),
    shoulder_dia=".4031", shoulder_at="1.2033", shoulder_angle_deg="30",
    datum_dia=".340", datum_at="1.258 -.007", neck_dia=".256", neck_at="1.3307",
    case_length="1.600 -.020", bullet_dia=".2245 -.0030", oal_min="2.000", oal_max="2.260", notes=STD_RADII)
row(name="243 Winchester", aliases="243 Win", pdf_page=87, issued="1979-05-29", revised="2022-04-05",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4553", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4540", shoulder_at="1.5598", shoulder_angle_deg="20",
    datum_dia=".400", datum_at="1.634 -.007", neck_dia=".276", neck_at="1.8043",
    case_length="2.045 -.020", bullet_dia=".243 -.003", oal_min="2.540", oal_max="2.710", notes=STD_RADII)
WSSM_HEAD = dict(rim_type="rebated", profile="bottleneck",
    rim_dia=".535 -.010", rim_thickness=".054 -.010", rim_land=".040 -.010", groove_dia=".480 -.020",
    groove_width=".040 +.010", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".5550", body_dia_2=".5461", body_dia_2_at=at(".200", ".800"))
row(name="243 Winchester Super Short Magnum", aliases="243 WSSM", pdf_page=88, issued="2004-02-11", revised="2022-04-06",
    **WSSM_HEAD, shoulder_dia=".5444", shoulder_at="1.1499", shoulder_angle_deg="28",
    datum_dia=".445", datum_at="1.2434 -.0070", neck_dia=".287", neck_at="1.3920",
    case_length="1.670 -.020", bullet_dia=".243 -.003", oal_min="2.060", oal_max="2.360",
    notes="Shoulder radius .050+.050; neck radius .150 max")
row(name="25 Winchester Super Short Magnum", aliases="25 WSSM", pdf_page=89, issued="2004-06-23", revised="2022-04-06",
    **WSSM_HEAD, shoulder_dia=".5443", shoulder_at="1.1574", shoulder_angle_deg="30",
    datum_dia=".445", datum_at="1.2434 -.0070", neck_dia=".299", neck_at="1.3698",
    case_length="1.670 -.020", bullet_dia=".2575 -.0030", oal_min="2.175", oal_max="2.360",
    notes="Shoulder radius .050+.050; neck radius .130 max")
row(name="25-06 Remington", aliases="25-06 Rem", pdf_page=90, issued="1979-05-29", revised="2022-04-06",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".049 -.010", rim_land=".034 -.010", groove_dia=".409 -.020",
    groove_width=".033 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4698", body_dia_2=".4426", body_dia_2_at=at(".200", "1.650"),
    shoulder_dia=".4410", shoulder_at="1.9480", shoulder_angle_deg="17.5",
    datum_dia=".375", datum_at="2.0526 -.0070", neck_dia=".291", neck_at="2.1858", mouth_dia=".290",
    case_length="2.494 -.020", bullet_dia=".2575 -.0030", oal_min="3.010", oal_max="3.250",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 17°30' B; neck tapers from .291 to .290 at mouth; "
          "shoulder radius .050+.050; neck radius .100 max")
row(name="25-20 Winchester", aliases="25-20 Win", pdf_page=91, issued="1980-04-21", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".408 -.010", rim_thickness=".065 -.010", rim_land=".050 -.010", groove_dia=".3492",
    body_dia_tol="-.008", head_dia=".3465", body_dia_2=".3350", body_dia_2_at=at(".200", ".570"),
    shoulder_dia=".3332", shoulder_at=".8573", shoulder_angle_deg="16.5667",
    datum_dia=".312", datum_at=".893 -.015", neck_dia=".2765", neck_at=".9527", mouth_dia=".2738",
    case_length="1.330 -.025", bullet_dia=".258 -.003", oal_min="1.530", oal_max="1.592",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 16°34' B; groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; neck tapers from .2765 to .2738 at mouth; shoulder radius .100 min; neck radius .185 max")
row(name="25-35 Winchester", aliases="25-35 Win", pdf_page=92, issued="1991-01-18", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".506 -.020", rim_thickness=".063 -.010", rim_land=".048 -.010", groove_dia=".4224",
    body_dia_tol="-.008", head_dia=".4163", body_dia_2=".3699", body_dia_2_at=at(".200", "1.050"),
    shoulder_dia=".3642", shoulder_at="1.3799", shoulder_angle_deg="11.5667",
    datum_dia=".325", datum_at="1.4756 -.0150", neck_dia=".2883", neck_at="1.5653", mouth_dia=".2816",
    case_length="2.043 -.025", bullet_dia=".258 -.003", oal_min="2.505", oal_max="2.550",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 11°34' B; groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; neck tapers from .2883 to .2816 at mouth; shoulder radius .740 min; neck radius .500 max")
MAUSER_HEAD = dict(rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".049 -.010", rim_land=".034 -.010", groove_dia=".409 -.020",
    groove_width=".033 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008")
row(name="250 Savage", aliases="250 Sav", pdf_page=93, issued="1979-05-29", revised="2022-05-02", **MAUSER_HEAD,
    head_dia=".4668", body_dia_2=".4187", body_dia_2_at=at(".200", "1.200"),
    shoulder_dia=".4142", shoulder_at="1.5118", shoulder_angle_deg="26.5",
    datum_dia=".347", datum_at="1.5792 -.0070", neck_dia=".2887", neck_at="1.6377", mouth_dia=".2856",
    case_length="1.912 -.020", bullet_dia=".258 -.003", oal_min="2.320", oal_max="2.515",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 26°30' B; neck tapers from .2887 to .2856 at mouth; "
          "shoulder radius .100+.050; neck radius .100 max")
row(name="257 Roberts", aliases="257 Rob; 257 Roberts +P; 257 Rob +P", pdf_page=94, issued="1979-05-29", revised="",
    **MAUSER_HEAD, head_dia=".4711", body_dia_2=".4310", body_dia_2_at=at(".200", "1.470"),
    shoulder_dia=".4294", shoulder_at="1.7277", shoulder_angle_deg="20.75",
    datum_dia=".375", datum_at="1.7995 -.0070", neck_dia=".290", neck_at="1.9117",
    case_length="2.233 -.020", bullet_dia=".258 -.003", oal_min="2.620", oal_max="2.780",
    by_eye=("shoulder_angle_deg",),
    notes="Revised date is clipped on the drawing (05/02/20..); shoulder angle 20°45' B; "
          "shoulder radius .030+.050; neck radius .100 max")
row(name="257 Weatherby Magnum", aliases="257 Wby Mag", pdf_page=95, issued="1991-06-04", revised="2024-01-21",
    rim_type="belted", profile="bottleneck",
    rim_dia=".5315 -.010", rim_thickness=".051 -.011", rim_land=".034 -.010", groove_dia=".457 -.020",
    groove_width=".049 +.010", groove_angle_deg="45", belt_dia=".532", belt_length=".219 -.006",
    body_dia_tol="-.004", head_dia=".5117", head_dia_at=".250", body_dia_2=".4920", body_dia_2_at=at(".250", "1.750"),
    shoulder_dia=".492", shoulder_at="2.012",
    datum_dia=".3963", datum_at="2.1127 -.0080", neck_dia=".285", neck_at="2.230",
    case_length="2.549 -.012", bullet_dia=".2573 -.0030", oal_min="3.049", oal_max="3.209",
    notes="Belt dia .532-.005 cylindrical; head dia tol -.004; radiused (venturi) shoulder: "
          "shoulder radius .125+.005, neck radius .1513-.0050, no shoulder angle")
row(name="26 Nosler", pdf_page=96, issued="2014-01-02", revised="2022-05-03",
    rim_type="rebated", profile="bottleneck",
    rim_dia=".534 -.010", rim_thickness=".050 -.011", rim_land=".035 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="32 -6", body_dia_tol="-.008",
    head_dia=".5500", body_dia_2=".5300", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".5275", shoulder_at="2.1659", shoulder_angle_deg="35",
    datum_dia=".420", datum_at="2.2427 -.0070", neck_dia=".297", neck_at="2.3305",
    case_length="2.590 -.020", bullet_dia=".2645 -.0030", oal_min="3.160", oal_max="3.340", notes=STD_RADII)
row(name="260 Remington", aliases="260 Rem", pdf_page=97, issued="1997-01-29", revised="2022-05-03",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4553", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4540", shoulder_at="1.5598", shoulder_angle_deg="20",
    datum_dia=".400", datum_at="1.634 -.007", neck_dia=".297", neck_at="1.7755",
    case_length="2.035 -.020", bullet_dia=".2645 -.0030", oal_min="2.530", oal_max="2.800", notes=STD_RADII)
BELTED_MAG_HEAD = dict(rim_type="belted", profile="bottleneck",
    rim_dia=".532 -.010", rim_thickness=".050 -.011", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="35 -6", belt_dia=".532", belt_length=".220 -.008",
    body_dia_tol="-.008", head_dia=".5127", head_dia_at=".250")
row(name="264 Winchester Magnum", aliases="264 Win Mag", pdf_page=98, issued="1980-04-21", revised="2020-08-29",
    **BELTED_MAG_HEAD, body_dia_2=".4921", body_dia_2_at=at(".250", "1.700"),
    shoulder_dia=".4910", shoulder_at="2.0401", shoulder_angle_deg="25",
    datum_dia=".420", datum_at="2.1162 -.0070", neck_dia=".299", neck_at="2.2459", mouth_dia=".298",
    case_length="2.500 -.020", bullet_dia=".265 -.003", oal_min="3.160", oal_max="3.340",
    notes="Belt dia .532-.005 cylindrical; neck tapers from .299 to .298 at mouth; "
          "shoulder radius .040+.050; neck radius .125 max")
NOSLER_HEAD = dict(rim_type="rebated", profile="bottleneck",
    rim_dia=".534 -.010", rim_thickness=".050 -.011", rim_land=".035 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="32 -6", body_dia_tol="-.008",
    head_dia=".5500", body_dia_2=".5300", body_dia_2_at=at(".200", "1.750"))
row(name="27 Nosler", pdf_page=99, issued="2015-01-26", revised="2022-05-04", **NOSLER_HEAD,
    shoulder_dia=".5282", shoulder_at="2.1087", shoulder_angle_deg="35",
    datum_dia=".420", datum_at="2.186 -.007", neck_dia=".314", neck_at="2.2617",
    case_length="2.590 -.020", bullet_dia=".278 -.003", oal_min="3.160", oal_max="3.340", notes=STD_RADII)
WBY_HEAD = dict(rim_type="belted", profile="bottleneck",
    rim_dia=".5315 -.010", rim_thickness=".051 -.011", rim_land=".034 -.010", groove_dia=".457 -.020",
    groove_width=".049 +.010", groove_angle_deg="45", belt_dia=".532", belt_length=".219 -.006",
    body_dia_tol="-.004", head_dia=".5117", head_dia_at=".250", body_dia_2=".4921", body_dia_2_at=at(".250", "1.750"))
row(name="270 Weatherby Magnum", aliases="270 Wby Mag", pdf_page=100, issued="1994-01-12", revised="2024-01-21",
    **WBY_HEAD, shoulder_dia=".492", shoulder_at="2.012",
    datum_dia=".4053", datum_at="2.1089 -.0080", neck_dia=".305", neck_at="2.2210",
    case_length="2.549 -.012", bullet_dia=".2773 -.0030", oal_min="3.157", oal_max="3.295",
    notes="Belt dia .532-.005 cylindrical; head dia tol -.004; radiused (venturi) shoulder: "
          "shoulder radius .125+.005, neck radius .1503-.0050, no shoulder angle")
row(name="270 Winchester", aliases="270 Win", pdf_page=101, issued="1979-05-29", revised="2022-05-04",
    **MAUSER_HEAD, head_dia=".4698", body_dia_2=".4426", body_dia_2_at=at(".200", "1.650"),
    shoulder_dia=".4410", shoulder_at="1.9480", shoulder_angle_deg="17.5",
    datum_dia=".375", datum_at="2.0526 -.0070", neck_dia=".310", neck_at="2.1557", mouth_dia=".308",
    case_length="2.540 -.020", bullet_dia=".278 -.003", oal_min="3.065", oal_max="3.340",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 17°30' B; neck tapers from .310 to .308 at mouth; "
          "shoulder radius .030+.050; neck radius .150 max")
WSM_HEAD = dict(rim_type="rebated", profile="bottleneck",
    rim_dia=".535 -.010", rim_thickness=".054 -.010", rim_land=".040 -.010", groove_dia=".480 -.020",
    groove_width=".040 +.010", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".5550", body_dia_2=".5400", body_dia_2_at=at(".200", "1.300"))
row(name="270 Winchester Short Magnum", aliases="270 WSM", pdf_page=102, issued="2002-02-01", revised="2021-11-15",
    **WSM_HEAD, shoulder_dia=".5381", shoulder_at="1.664", shoulder_angle_deg="35",
    datum_dia=".445", datum_at="1.730 -.007", neck_dia=".314", neck_at="1.8235",
    case_length="2.100 -.020", bullet_dia=".278 -.003", oal_min="2.560", oal_max="2.860",
    notes="Shoulder radius .050+.050; neck radius .100 max")
row(name="277 SIG Fury", pdf_page=103, issued="2020-09-23", revised="2022-05-04",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".472 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".408 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4623", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4611", shoulder_at="1.6311", shoulder_angle_deg="30",
    datum_dia=".400", datum_at="1.684 -.005", neck_dia=".310", neck_at="1.7619",
    case_length="2.015 -.020", bullet_dia=".278 -.003", oal_min="2.700", oal_max="2.825",
    notes="SAAMI warns MAP above 65,000 psi; " + STD_RADII)
row(name="28 Nosler", pdf_page=104, issued="2015-01-18", revised="2022-05-05", **NOSLER_HEAD,
    shoulder_dia=".5275", shoulder_at="2.1662", shoulder_angle_deg="35",
    datum_dia=".420", datum_at="2.243 -.007", neck_dia=".320", neck_at="2.3144",
    case_length="2.590 -.020", bullet_dia=".2845 -.0030", oal_min="3.160", oal_max="3.340", notes=STD_RADII)
row(name="280 Ackley Improved", aliases="280 Ack Imp; 280 AI", pdf_page=105, issued="2008-02-01", revised="2022-05-05",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".472 -.010", rim_thickness=".049 -.010", rim_land=".034 -.010", groove_dia=".409 -.020",
    groove_width=".033 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4685", body_dia_2=".4552", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".4541", shoulder_at="2.0966", shoulder_angle_deg="40",
    datum_dia=".375", datum_at="2.1437 -.0060", neck_dia=".315", neck_at="2.1795",
    case_length="2.525 -.012", bullet_dia=".2845 -.0030", oal_min="3.136", oal_max="3.330",
    notes="Shoulder radius .039+.025; neck radius .069 max")
row(name="280 Remington", aliases="280 Rem; 7mm Express Remington; 7mm Exp Rem", pdf_page=106,
    issued="1986-06-20", revised="2022-05-05",
    **{**MAUSER_HEAD, "rim_thickness": ".049 -.010"},
    head_dia=".4700", body_dia_2=".4420", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".4412", shoulder_at="1.9992", shoulder_angle_deg="17.5",
    datum_dia=".375", datum_at="2.1042 -.0070", neck_dia=".315", neck_at="2.1993",
    case_length="2.540 -.020", bullet_dia=".2845 -.0030", oal_min="3.150", oal_max="3.330",
    by_eye=("shoulder_angle_deg",),
    notes="Previously designated 7mm Express Remington; rim thickness mm printed as (1.24-0.28); "
          "shoulder angle 17°30' B; shoulder radius .025+.050; neck radius .100 max")
row(name="284 Winchester", aliases="284 Win", pdf_page=107, issued="1979-05-29", revised="2022-05-05",
    rim_type="rebated", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".040 +.010", groove_angle_deg="40 -6", body_dia_tol="-.008",
    head_dia=".5000", body_dia_2=".4776", body_dia_2_at=at(".200", "1.400"),
    shoulder_dia=".4748", shoulder_at="1.7749", shoulder_angle_deg="35",
    datum_dia=".420", datum_at="1.814 -.007", neck_dia=".320", neck_at="1.8854",
    case_length="2.170 -.020", bullet_dia=".284 -.003", oal_min="2.765", oal_max="2.800",
    notes="Rim thickness mm printed as (1.37-0.28); " + STD_RADII)
row(name="30 Carbine", aliases="30 Carb", pdf_page=108, issued="1979-05-29", revised="2022-05-16",
    rim_type="rimless", profile="straight",
    rim_dia=".360 -.010", rim_thickness=".050 -.010", rim_land=".035 -.010", groove_dia=".310 -.020",
    groove_width=".033 +.017", groove_angle_deg="37 -11", body_dia_tol="-.008",
    head_dia=".3548", body_dia_2=".3387", body_dia_2_at=at(".200", ".670"), mouth_dia=".336",
    case_length="1.290 -.010", bullet_dia=".309 -.003", oal_min="1.625", oal_max="1.680",
    notes="Tapered body to .336 at .9824 from head, then cylindrical to the mouth; round-nose bullet")
row(name="30 Nosler", pdf_page=109, issued="2015-01-19", revised="2022-05-18", **NOSLER_HEAD,
    shoulder_dia=".5281", shoulder_at="2.1148", shoulder_angle_deg="35",
    datum_dia=".420", datum_at="2.192 -.007", neck_dia=".344", neck_at="2.2463",
    case_length="2.556 -.020", bullet_dia=".309 -.003", oal_min="3.160", oal_max="3.340", notes=STD_RADII)
row(name="30 Remington AR", aliases="30 Rem AR", pdf_page=110, issued="2009-06-17", revised="2022-05-18",
    rim_type="rebated", profile="bottleneck",
    rim_dia=".492 -.010", rim_thickness=".054 -.011", rim_land=".039 -.010", groove_dia=".428 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".5000", body_dia_2=".4907", body_dia_2_at=at(".200", ".700"),
    shoulder_dia=".4885", shoulder_at="1.0681", shoulder_angle_deg="25",
    datum_dia=".400", datum_at="1.163 -.007", neck_dia=".342", neck_at="1.2252", mouth_dia=".341",
    case_length="1.530 -.020", bullet_dia=".309 -.003", oal_min="2.000", oal_max="2.260",
    notes="Neck tapers from .342 to .341 at mouth; " + STD_RADII)
row(name="30 Thompson Center", aliases="30 TC", pdf_page=111, issued="2008-02-01", revised="2025-02-05",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4648", body_dia_2_at=at(".200", "1.150"),
    shoulder_dia=".4640", shoulder_at="1.5120", shoulder_angle_deg="30",
    datum_dia=".400", datum_at="1.5674 -.0070", neck_dia=".337", neck_at="1.6220",
    case_length="1.920 -.020", bullet_dia=".309 -.003", oal_min="2.560", oal_max="2.660", notes=STD_RADII)
row(name="30-06 Springfield", aliases="30-06 Sprg", pdf_page=112, issued="1979-05-29", revised="2022-05-19",
    **MAUSER_HEAD, head_dia=".4698", body_dia_2=".4426", body_dia_2_at=at(".200", "1.650"),
    shoulder_dia=".4410", shoulder_at="1.9480", shoulder_angle_deg="17.5",
    datum_dia=".375", datum_at="2.0526 -.0070", neck_dia=".3397", neck_at="2.1086",
    case_length="2.494 -.020", bullet_dia=".309 -.003", oal_min="2.940", oal_max="3.340",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 17°30' B; shoulder radius .050+.050; neck radius .100 max")
row(name="30-30 Winchester", aliases="30-30 Win", pdf_page=113, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".506 -.010", rim_thickness=".063 -.010", rim_land=".048 -.010", groove_dia=".4215",
    body_dia_tol="-.008", head_dia=".4195", body_dia_2=".4026", body_dia_2_at=at(".200", "1.150"),
    shoulder_dia=".4013", shoulder_at="1.4405", shoulder_angle_deg="15.65",
    datum_dia=".375", datum_at="1.4874 -.0150", neck_dia=".3331", neck_at="1.5622", mouth_dia=".3301",
    case_length="2.0395 -.0200", bullet_dia=".309 -.003", oal_min="2.450", oal_max="2.550",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 15°39' B; groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; neck tapers from .3331 to .3301 at mouth; shoulder radius .180 min; neck radius .460 max")
row(name="30-40 Krag", pdf_page=114, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck", rim_chamfer_deg="40", rim_chamfer_tol_deg="+25",
    rim_dia=".545 -.010", rim_thickness=".064 -.010", rim_land=".049 -.010", groove_dia=".4611",
    body_dia_tol="-.008", head_dia=".4577", body_dia_2=".4222", body_dia_2_at=at(".200", "1.400"),
    shoulder_dia=".4190", shoulder_at="1.7250", shoulder_angle_deg="21.1",
    datum_dia=".375", datum_at="1.7821 -.0150", neck_dia=".3389", neck_at="1.8289", mouth_dia=".338",
    case_length="2.314 -.020", bullet_dia=".309 -.003", oal_min="2.965", oal_max="3.089",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 21°6' B; head chamfer 40°+25°; groove_dia is the reference diameter of the optional "
          "undercut; " + UNDERCUT + "; neck tapers from .3389 to .338 at mouth; "
          "shoulder radius .155+.050; neck radius .160 max")
row(name="300 AAC Blackout", aliases="300 BLK", pdf_page=115, issued="2011-01-17", revised="2022-05-20",
    **{**REM_223_HEAD, "body_dia_tol": "-.005"},
    body_dia_2=".3619", body_dia_2_at=at(".200", ".800"),
    shoulder_dia=".3607", shoulder_at="1.0707", shoulder_angle_deg="23",
    datum_dia=".3512", datum_at="1.0818 -.0070", neck_dia=".334", neck_at="1.1021",
    case_length="1.368 -.020", bullet_dia=".309 -.003", oal_min="1.780", oal_max="2.260",
    notes="Shoulder radius .025+.025; neck radius .050 max")
row(name="300 HAM'R", aliases="300 HAMR", pdf_page=116, issued="2020-01-20", revised="2023-06-06",
    **REM_223_HEAD, body_dia_2=".3660", body_dia_2_at=at(".200", "1.000"),
    shoulder_dia=".3646", shoulder_at="1.3411", shoulder_angle_deg="30",
    datum_dia=".3512", datum_at="1.3527 -.0070", neck_dia=".332", neck_at="1.3693",
    case_length="1.603 -.015", bullet_dia=".309 -.003", oal_min="2.165", oal_max="2.260",
    notes="Rim thickness mm printed as (1.43-0.25), apparently a typo for 1.14; "
          "shoulder radius .018+.025; neck radius .025 max")
row(name="300 Holland & Holland Magnum", aliases="300 H&H Mag", pdf_page=117, issued="1980-04-21", revised="2022-05-20",
    **{**BELTED_MAG_HEAD, "head_dia": ".5120"}, body_dia_2=".4567", body_dia_2_at=at(".250", "1.650"),
    shoulder_dia=".4498", shoulder_at="2.1046", shoulder_angle_deg="8.5",
    datum_dia=".375", datum_at="2.355 -.007", neck_dia=".338", neck_at="2.4788",
    case_length="2.850 -.030", bullet_dia=".309 -.003", oal_min="3.420", oal_max="3.600",
    by_eye=("shoulder_angle_deg",),
    notes="Belt dia .532-.005 cylindrical; shoulder angle 8°30' B; shoulder radius .100+.050; neck radius .100 max")
row(name="300 Norma Magnum", aliases="300 NM", pdf_page=118, issued="2020-09-23", revised="2024-10-11",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".588 -.010", rim_thickness=".060 -.011", rim_land=".040 -.010", groove_dia=".521 -.020",
    groove_width=".037 +.010", groove_angle_deg="50 -6", body_dia_tol="-.008",
    head_dia=".5845", body_dia_2=".5631", body_dia_2_at=at(".200", "1.650"),
    shoulder_dia=".5626", shoulder_at="1.8921", shoulder_angle_deg="20.5",
    datum_dia=".4550", datum_at="2.0360 -.0070", neck_dia=".3429", neck_at="2.1859", mouth_dia=".3417",
    case_length="2.492 -.020", bullet_dia=".3083 -.0030", oal_min="3.556", oal_max="3.681",
    by_eye=("shoulder_angle_deg",),
    notes="Metric-origin drawing (mm primary; inch values used here); shoulder angle 20°30' B; "
          "neck tapers from .3429 to .3417 at mouth; shoulder radius .030+.050; neck radius .098 max")
PRC_HEAD = dict(rim_type="rimless", profile="bottleneck",
    rim_dia=".532 -.010", rim_thickness=".050 -.010", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="35 -6", body_dia_tol="-.008", head_dia=".5320")
row(name="300 Precision Rifle Cartridge", aliases="300 PRC", pdf_page=119, issued="2018-06-13", revised="2022-02-17",
    **PRC_HEAD, body_dia_2=".5165", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".5150", shoulder_at="2.1217", shoulder_angle_deg="30",
    datum_dia=".420", datum_at="2.204 -.007", neck_dia=".341", neck_at="2.2724",
    case_length="2.580 -.020", bullet_dia=".3084 -.0030", oal_min="3.575", oal_max="3.700", notes=STD_RADII)
RUM_HEAD = dict(rim_type="rebated", profile="bottleneck",
    rim_dia=".534 -.010", rim_thickness=".050 -.011", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="32 -6", body_dia_tol="-.008", head_dia=".5500")
row(name="300 Remington Short Action Ultra Magnum", aliases="300 Rem SA Ultra Mag; 300 RSAUM", pdf_page=120,
    issued="2002-02-01", revised="2022-05-25", **RUM_HEAD,
    body_dia_2=".5357", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".5347", shoulder_at="1.5383", shoulder_angle_deg="30",
    datum_dia=".460", datum_at="1.603 -.007", neck_dia=".344", neck_at="1.7035",
    case_length="2.015 -.020", bullet_dia=".309 -.003", oal_min="2.450", oal_max="2.825", notes=STD_RADII)
row(name="300 Remington Ultra Magnum", aliases="300 Rem Ultra Mag; 300 RUM", pdf_page=121,
    issued="1999-01-07", revised="2022-05-26", **RUM_HEAD,
    body_dia_2=".5300", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".5250", shoulder_at="2.3873", shoulder_angle_deg="30",
    datum_dia=".420", datum_at="2.4782 -.0070", neck_dia=".344", neck_at="2.5440",
    case_length="2.850 -.020", bullet_dia=".309 -.003", oal_min="3.450", oal_max="3.600", notes=STD_RADII)
RCM_HEAD = dict(**{**PRC_HEAD, "rim_thickness": ".050 -.010"}, body_dia_2=".5167", body_dia_2_at=at(".200", "1.300"),
    shoulder_dia=".5150", shoulder_at="1.6434", shoulder_angle_deg="30",
    datum_dia=".420", datum_at="1.7257 -.0070", neck_at="1.7950", case_length="2.100 -.020")
row(name="300 Ruger Compact Magnum", aliases="300 RCM", pdf_page=122, issued="2008-12-30", revised="2022-05-26",
    **RCM_HEAD, neck_dia=".340", bullet_dia=".309 -.003", oal_min="2.715", oal_max="2.840",
    notes="SAAMI notes an IP-rights assurance on this cartridge; " + STD_RADII)
row(name="300 Savage", aliases="300 Sav", pdf_page=123, issued="1979-05-29", revised="2022-05-27",
    **MAUSER_HEAD, head_dia=".4706", body_dia_2=".4485", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4466", shoulder_at="1.5586", shoulder_angle_deg="30",
    datum_dia=".3968", datum_at="1.6017 -.0070", neck_dia=".3407", neck_at="1.6503", mouth_dia=".339",
    case_length="1.871 -.020", bullet_dia=".309 -.003", oal_min="2.495", oal_max="2.600",
    notes="Neck tapers from .3407 to .339 at mouth; " + STD_RADII)
row(name="300 Weatherby Magnum", aliases="300 Wby Mag", pdf_page=124, issued="1990-02-01", revised="2024-01-21",
    **{**WBY_HEAD, "rim_dia": ".5315 -.0100", "rim_land": ".039 -.010", "belt_dia": ".5315",
       "body_dia_2": ".4949"},
    shoulder_dia=".4917", shoulder_at="2.2980",
    datum_dia=".4276", datum_at="2.3838 -.0080", neck_dia=".337", neck_at="2.5040",
    case_length="2.825 -.012", bullet_dia=".3083 -.0030", oal_min="3.390", oal_max="3.560",
    notes="Belt dia .5315-.0100 cylindrical; head dia tol -.0040; radiused (venturi) shoulder: "
          "shoulder radius .125+.005, neck radius .182-.005, no shoulder angle")
row(name="300 Winchester Magnum", aliases="300 Win Mag", pdf_page=125, issued="1980-04-21", revised="2022-05-31",
    **{**BELTED_MAG_HEAD, "head_dia": ".5126"}, body_dia_2=".4915", body_dia_2_at=at(".250", "1.750"),
    shoulder_dia=".4891", shoulder_at="2.1959", shoulder_angle_deg="25",
    datum_dia=".420", datum_at="2.270 -.007", neck_dia=".3397", neck_at="2.3561",
    case_length="2.620 -.020", bullet_dia=".309 -.003", oal_min="3.215", oal_max="3.340",
    notes="Belt dia .532-.005 cylindrical; shoulder radius .040+.050; neck radius .100 max")
row(name="300 Winchester Short Magnum", aliases="300 WSM", pdf_page=126, issued="2001-06-13", revised="2022-06-01",
    **WSM_HEAD, shoulder_dia=".5381", shoulder_at="1.6635", shoulder_angle_deg="35",
    datum_dia=".445", datum_at="1.730 -.007", neck_dia=".344", neck_at="1.8021",
    case_length="2.100 -.020", bullet_dia=".309 -.003", oal_min="2.560", oal_max="2.860",
    notes="Shoulder radius .050+.050; neck radius .100 max")
row(name="303 British", aliases="303 Brit", pdf_page=127, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".540 -.015", rim_thickness=".064 -.010", rim_land=".049 -.010", groove_dia=".4601",
    body_dia_tol="-.008", head_dia=".4554", body_dia_2=".4126", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4010", shoulder_at="1.7901", shoulder_angle_deg="16.9667",
    datum_dia=".375", datum_at="1.8326 -.0150", neck_dia=".340", neck_at="1.8900", mouth_dia=".338",
    case_length="2.222 -.020", bullet_dia=".3125 -.0030", oal_min="2.915", oal_max="3.075",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 16°58' B; groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; neck tapers from .340 to .338 at mouth; shoulder radius .090+.050; neck radius .090 max")
MARLIN_HEAD = dict(rim_type="rimmed", profile="bottleneck",
    rim_dia=".506 -.010", rim_thickness=".063 -.010", rim_land=".048 -.010", groove_dia=".410 -.020",
    groove_width=".018 +.010", groove_angle_deg="25 -6", body_dia_tol="-.008", head_dia=".4703")
row(name="307 Winchester", aliases="307 Win", pdf_page=128, issued="1983-11-08", revised="2022-06-02",
    **MARLIN_HEAD, body_dia_2=".4553", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4540", shoulder_at="1.5598", shoulder_angle_deg="20",
    datum_dia=".400", datum_at="1.634 -.007", neck_dia=".3435", neck_at="1.7116",
    case_length="2.015 -.020", bullet_dia=".309 -.003", oal_min="2.530", oal_max="2.560", notes=STD_RADII)
row(name="308 Marlin Express", aliases="308 Mar Exp", pdf_page=129, issued="2007-06-13", revised="2022-06-03",
    **MARLIN_HEAD, body_dia_2=".4554", body_dia_2_at=at(".200", "1.150"),
    shoulder_dia=".4539", shoulder_at="1.4649", shoulder_angle_deg="20",
    datum_dia=".400", datum_at="1.539 -.007", neck_dia=".337", neck_at="1.6255",
    case_length="1.920 -.020", bullet_dia=".3085 -.0030", oal_min="2.450", oal_max="2.600",
    notes="Shoulder radius .030+.050; neck radius .100 max")
row(name="308 Winchester", aliases="308 Win", pdf_page=130, issued="1979-05-29", revised="2022-06-03",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4553", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4540", shoulder_at="1.5598", shoulder_angle_deg="20",
    datum_dia=".400", datum_at="1.634 -.007", neck_dia=".3435", neck_at="1.7116",
    case_length="2.015 -.020", bullet_dia=".309 -.003", oal_min="2.490", oal_max="2.810", notes=STD_RADII)
row(name="32 Winchester Special", aliases="32 Win Spl", pdf_page=131, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".506 -.010", rim_thickness=".063 -.010", rim_land=".048 -.010", groove_dia=".4219",
    body_dia_tol="-.008", head_dia=".4199", body_dia_2=".4034", body_dia_2_at=at(".200", "1.110"),
    shoulder_dia=".4014", shoulder_at="1.4461", shoulder_angle_deg="14.5167",
    datum_dia=".375", datum_at="1.497 -.015", neck_dia=".3456", neck_at="1.5538", mouth_dia=".343",
    case_length="2.040 -.020", bullet_dia=".322 -.003", oal_min="2.480", oal_max="2.565",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 14°31' B; groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; neck tapers from .3456 to .343 at mouth; shoulder radius .150+.050; neck radius .300 max")
row(name="32-20 Winchester", aliases="32-20 Win", pdf_page=132, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".408 -.010", rim_thickness=".065 -.010", rim_land=".050 -.010", groove_dia=".3535",
    body_dia_tol="-.008", head_dia=".3517", body_dia_2=".3429", body_dia_2_at=at(".200", ".645"),
    shoulder_dia=".3424", shoulder_at=".8812", shoulder_angle_deg="5.7",
    datum_dia=".332", datum_at=".9333 -.0150", neck_dia=".3309", neck_at=".9388", mouth_dia=".3266",
    case_length="1.315 -.040", bullet_dia=".3125 -.0030", oal_min="1.540", oal_max="1.592",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 5°42' B; groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; neck tapers from .3309 to .3266 at mouth; shoulder radius .030 min; neck radius .100 max")
row(name="325 Winchester Short Magnum", aliases="325 WSM", pdf_page=133, issued="2005-06-22", revised="2022-07-27",
    **WSM_HEAD, shoulder_dia=".5381", shoulder_at="1.6635", shoulder_angle_deg="35",
    datum_dia=".445", datum_at="1.730 -.007", neck_dia=".358", neck_at="1.7921",
    case_length="2.100 -.020", bullet_dia=".3235 -.0030", oal_min="2.560", oal_max="2.860",
    notes="Shoulder radius .050+.050; neck radius .100 max")
row(name="33 Nosler", pdf_page=134, issued="2015-01-19", revised="2022-02-08", **NOSLER_HEAD,
    shoulder_dia=".5292", shoulder_at="2.0163", shoulder_angle_deg="35",
    datum_dia=".440", datum_at="2.080 -.007", neck_dia=".370", neck_at="2.1300",
    case_length="2.460 -.020", bullet_dia=".3390 -.0030", oal_min="3.160", oal_max="3.340", notes=STD_RADII)
row(name="338 Federal", aliases="338 Fed", pdf_page=135, issued="2006-06-28", revised="2022-02-08",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4553", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4540", shoulder_at="1.5603", shoulder_angle_deg="20",
    datum_dia=".420", datum_at="1.607 -.007", neck_dia=".370", neck_at="1.6757",
    case_length="2.015 -.020", bullet_dia=".339 -.003", oal_min="2.490", oal_max="2.820", notes=STD_RADII)
row(name="338 Lapua Magnum", aliases="338 Lapua Mag", pdf_page=136, issued="2013-01-14", revised="2022-03-08",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".5878 -.010", rim_thickness=".060 -.011", rim_land=".040 -.010", groove_dia=".5213 -.020",
    groove_width=".035 +.010", groove_angle_deg="50.08", groove_angle_tol_deg="-6", body_dia_tol="-.008",
    head_dia=".5854", body_dia_2=".5454", body_dia_2_at=at(".200", "1.900"),
    shoulder_dia=".5441", shoulder_at="2.1614", shoulder_angle_deg="19.9983",
    datum_dia=".476", datum_at="2.2550 -.0070", neck_dia=".3724", neck_at="2.3972", mouth_dia=".3705",
    case_length="2.7244 -.0201", bullet_dia=".3390 -.003", oal_min="3.5610", oal_max="3.6811",
    by_eye=("groove_angle_deg", "shoulder_angle_deg"),
    notes="Metric-origin drawing (mm primary; inch values used here); groove angle 50°04'48\"-6°; "
          "shoulder angle 19°59'54\" B; neck tapers from .3724 to .3705 at mouth; "
          "shoulder radius .031 min; neck radius .098 max")
row(name="338 Marlin Express", aliases="338 Mar Exp", pdf_page=137, issued="2009-06-17", revised="2023-07-21",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".553 -.010", rim_thickness=".050 -.010", rim_land=".034 -.010", groove_dia=".441 -.020",
    groove_width=".039 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".5061", body_dia_2=".4941", body_dia_2_at=at(".200", "1.150"),
    shoulder_dia=".4930", shoulder_at="1.4578", shoulder_angle_deg="25",
    datum_dia=".420", datum_at="1.536 -.007", neck_dia=".368", neck_at="1.5918",
    case_length="1.890 -.020", bullet_dia=".3385 -.0030", oal_min="2.450", oal_max="2.600",
    notes="Shoulder radius .040+.050; neck radius .125 max")
row(name="338 Norma Magnum", aliases="338 NM", pdf_page=138, issued="2020-09-24", revised="2024-10-11",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".588 -.010", rim_thickness=".060 -.011", rim_land=".040 -.010", groove_dia=".521 -.020",
    groove_width=".037 +.010", groove_angle_deg="50 -6", body_dia_tol="-.008",
    head_dia=".5848", body_dia_2=".5715", body_dia_2_at=at(".200", "1.600"),
    shoulder_dia=".5709", shoulder_at="1.8811", shoulder_angle_deg="20.5",
    datum_dia=".4750", datum_at="2.0093 -.0070", neck_dia=".370", neck_at="2.1496", mouth_dia=".369",
    case_length="2.492 -.0200", bullet_dia=".3386 -.0030", oal_min="3.556", oal_max="3.681",
    by_eye=("shoulder_angle_deg",),
    notes="Metric-origin drawing (mm primary; inch values used here); groove width tol printed as +.01; "
          "shoulder angle 20°30' B; neck tapers from .370 to .369 at mouth; "
          "shoulder radius .030+.050; neck radius .098 max")
row(name="338 Remington Ultra Magnum", aliases="338 Rem Ultra Mag; 338 RUM", pdf_page=139,
    issued="1999-06-08", revised="2022-02-11", **RUM_HEAD,
    body_dia_2=".5300", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".5260", shoulder_at="2.2958", shoulder_angle_deg="30",
    datum_dia=".460", datum_at="2.353 -.007", neck_dia=".371", neck_at="2.4301",
    case_length="2.760 -.020", bullet_dia=".3383 -.0030", oal_min="3.450", oal_max="3.600", notes=STD_RADII)
row(name="338 Ruger Compact Magnum", aliases="338 RCM", pdf_page=140, issued="2008-12-30", revised="2022-02-11",
    **PRC_HEAD, body_dia_2=".5170", body_dia_2_at=at(".200", "1.265"),
    shoulder_dia=".5158", shoulder_at="1.5688", shoulder_angle_deg="30",
    datum_dia=".450", datum_at="1.6258 -.0070", neck_dia=".370", neck_at="1.6951", mouth_dia=".369",
    case_length="2.015 -.020", bullet_dia=".339 -.003", oal_min="2.715", oal_max="2.840",
    notes="Neck tapers from .370 to .369 at mouth; " + STD_RADII)
row(name="338 Weatherby Rebated Precision Magnum", aliases="338 Wby RPM", pdf_page=141, issued="2022-01-16", revised="",
    rim_type="rebated", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".040 +.010", groove_angle_deg="40 -6", body_dia_tol="-.008",
    head_dia=".5000", body_dia_2=".4780", body_dia_2_at=at(".200", "1.650"),
    shoulder_dia=".4739", shoulder_at="2.1595", shoulder_angle_deg="35",
    datum_dia=".420", datum_at="2.198 -.007", neck_dia=".364", neck_at="2.2380",
    case_length="2.550 -.020", bullet_dia=".3383 -.0030", oal_min="3.250", oal_max="3.380",
    notes="Shoulder radius .030+.050; neck radius .100 max")
row(name="338 Winchester Magnum", aliases="338 Win Mag", pdf_page=142, issued="1980-04-21", revised="2022-02-15",
    **BELTED_MAG_HEAD, body_dia_2=".4925", body_dia_2_at=at(".250", "1.670"),
    shoulder_dia=".4910", shoulder_at="2.0400", shoulder_angle_deg="25",
    datum_dia=".420", datum_at="2.1162 -.0070", neck_dia=".370", neck_at="2.1698", mouth_dia=".369",
    case_length="2.500 -.020", bullet_dia=".339 -.003", oal_min="3.180", oal_max="3.340",
    notes="Belt dia .532-.005 cylindrical; neck tapers from .370 to .369 at mouth; neck_at mm printed as "
          "(57.113), inconsistent with 2.1698 in (the inch value matches the 25° shoulder geometry); "
          "shoulder radius .040+.050; neck radius .125 max")
row(name="340 Weatherby Magnum", aliases="340 Wby Mag", pdf_page=143, issued="1994-01-12", revised="2024-01-21",
    **{**WBY_HEAD, "rim_dia": ".5315 -.0100", "rim_land": ".039 -.005", "belt_dia": ".5315",
       "body_dia_2": ".4949"},
    shoulder_dia=".4920", shoulder_at="2.2986",
    datum_dia=".4395", datum_at="2.3763 -.0080", neck_dia=".366", neck_at="2.4850",
    case_length="2.825 -.012", bullet_dia=".3383 -.0030", oal_min="3.585", oal_max="3.700",
    notes="Belt dia .5315-.0050 cylindrical; head dia tol -.0040; rim thickness mm printed as (1.30-0.28); "
          "OAL min mm printed as (87.63), inconsistent with 3.585 in; radiused (venturi) shoulder: "
          "shoulder radius .125+.005, neck radius .182-.005, no shoulder angle")
row(name="348 Winchester", aliases="348 Win", pdf_page=144, issued="1979-05-29", revised="2023-10-05",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".610 -.010", rim_thickness=".070 -.010", rim_land=".055 -.010", groove_dia=".5529",
    body_dia_tol="-.008", head_dia=".5474", body_dia_2=".4872", body_dia_2_at=at(".200", "1.400"),
    shoulder_dia=".4851", shoulder_at="1.6499", shoulder_angle_deg="19.0667",
    datum_dia=".4339", datum_at="1.7239 -.0150", neck_dia=".3785", neck_at="1.8040", mouth_dia=".3757",
    case_length="2.255 -.020", bullet_dia=".3495 -.003", oal_min="2.770", oal_max="2.795",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 19°4' B; groove_dia is the reference diameter ahead of the rim; "
          "neck tapers from .3785 to .3757 at mouth; shoulder radius .030+.050; neck radius .100 max")
row(name="35 Remington", aliases="35 Rem", pdf_page=145, issued="1980-04-21", revised="2022-07-28",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".460 -.010", rim_thickness=".050 -.011", rim_land=".034 -.010", groove_dia=".400 -.020",
    groove_width=".030 +.010", groove_angle_deg="34 -6", body_dia_tol="-.008",
    head_dia=".4574", body_dia_2=".4282", body_dia_2_at=at(".200", "1.240"),
    shoulder_dia=".4259", shoulder_at="1.5393", shoulder_angle_deg="23.4167",
    datum_dia=".405", datum_at="1.5634 -.0070", neck_dia=".3869", neck_at="1.5843", mouth_dia=".3838",
    case_length="1.920 -.020", bullet_dia=".359 -.003", oal_min="2.460", oal_max="2.525",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 23°25' B; neck tapers from .3869 to .3838 at mouth; "
          "shoulder radius .025+.050; neck radius .050 max")
row(name="35 Whelen", pdf_page=146, issued="1988-01-08", revised="2022-07-28",
    **MAUSER_HEAD, head_dia=".4698", body_dia_2=".4426", body_dia_2_at=at(".200", "1.650"),
    shoulder_dia=".4410", shoulder_at="1.9480", shoulder_angle_deg="17.5",
    datum_dia=".415", datum_at="1.9892 -.0070", neck_dia=".388", neck_at="2.0320",
    case_length="2.494 -.020", bullet_dia=".359 -.003", oal_min="2.970", oal_max="3.340",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 17°30' B; shoulder radius .050+.050; neck radius .100 max")
row(name="350 Legend", aliases="350 LGND", pdf_page=147, issued="2019-01-21", revised="2022-08-01",
    rim_type="rebated", profile="straight",
    rim_dia=".378 -.010", rim_thickness=".045 -.010", rim_land=".027 -.010", groove_dia=".332 -.020",
    groove_width=".030 +.010", groove_angle_deg="25 -6", body_dia_tol="-.008",
    head_dia=".3900", body_dia_2=".3792", body_dia_2_at=at(".200", "1.350"), mouth_dia=".3780",
    case_length="1.710 -.010", bullet_dia=".357 -.003", oal_min="2.125", oal_max="2.260",
    notes="Straight-wall case with rebated rim")
row(name="356 Winchester", aliases="356 Win", pdf_page=148, issued="1983-11-08", revised="2023-07-25",
    **MARLIN_HEAD, body_dia_2=".4553", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4540", shoulder_at="1.5598", shoulder_angle_deg="20",
    datum_dia=".420", datum_at="1.6065 -.0070", neck_dia=".388", neck_at="1.6505",
    case_length="2.015 -.020", bullet_dia=".3585 -.0030", oal_min="2.530", oal_max="2.560",
    notes=UNDERCUT + "; shoulder radius .030+.050; neck radius .100 max")
row(name="358 Winchester", aliases="358 Win", pdf_page=149, issued="1979-05-29", revised="2022-08-03",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.020",
    groove_width=".055 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4703", body_dia_2=".4553", body_dia_2_at=at(".200", "1.250"),
    shoulder_dia=".4540", shoulder_at="1.5598", shoulder_angle_deg="20",
    datum_dia=".420", datum_at="1.6065 -.0070", neck_dia=".388", neck_at="1.6505",
    case_length="2.015 -.020", bullet_dia=".3585 -.0030", oal_min="2.730", oal_max="2.780",
    notes="Shoulder radius .030+.050; neck radius .100 max")
row(name="360 Buckhammer", aliases="360 BHMR", pdf_page=150, issued="2023-01-15", revised="2023-02-10",
    rim_type="rimmed", profile="straight",
    rim_dia=".506 -.010", rim_thickness=".063 -.010", rim_land=".048 -.010", groove_dia=".4229",
    body_dia_tol="-.008", head_dia=".4195", body_dia_2=".3860", body_dia_2_at=at(".200", "1.350"),
    mouth_dia=".3798", case_length="1.800 -.020", bullet_dia=".359 -.003", oal_min="2.350", oal_max="2.500",
    notes="groove_dia is the reference diameter of the optional undercut; " + UNDERCUT)
row(name="370 Sako Magnum", aliases="370 Sako Mag; 9.3x66 Sako", pdf_page=151, issued="2010-01-14", revised="2024-10-11",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".470 -.010", rim_thickness=".051 -.010", rim_land=".039 +.010", groove_dia=".413 -.020",
    groove_width=".039 +.010", groove_angle_deg="41 -6", body_dia_tol="-.008",
    head_dia=".4766", body_dia_2=".4533", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".4500", shoulder_at="2.1968", shoulder_angle_deg="17.4628",
    datum_dia=".420", datum_at="2.2440 -.0070", neck_dia=".391", neck_at="2.2906",
    case_length="2.600 -.020", bullet_dia=".366 -.003", oal_min="3.221", oal_max="3.346",
    by_eye=("shoulder_angle_deg",),
    notes="Metric-origin drawing (mm primary; inch values used here); general diameter tol -.008; "
          "rim land printed as 1.00+0.25 (.039+.010); OAL printed as MIN-MIN, read as min-max; "
          "shoulder angle 17°27'46\" B; shoulder radius .020+.050; neck radius .020 max")
row(name="375 Holland & Holland Magnum", aliases="375 H&H Mag", pdf_page=152, issued="1980-04-21", revised="2022-08-03",
    **{**BELTED_MAG_HEAD, "head_dia": ".5121"}, body_dia_2=".4630", body_dia_2_at=at(".250", "1.650"),
    shoulder_dia=".4478", shoulder_at="2.4122", shoulder_angle_deg="15",
    datum_dia=".420", datum_at="2.464 -.007", neck_dia=".402", neck_at="2.4976",
    case_length="2.850 -.020", bullet_dia=".376 -.003", oal_min="3.475", oal_max="3.600",
    notes="Belt dia .532-.005 cylindrical; shoulder radius .100+.050; neck radius .100 max")
row(name="375 Remington Ultra Magnum", aliases="375 Rem Ultra Mag; 375 RUM", pdf_page=153,
    issued="2001-01-10", revised="2022-08-05", **RUM_HEAD,
    body_dia_2=".5300", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".5250", shoulder_at="2.3872", shoulder_angle_deg="30",
    datum_dia=".465", datum_at="2.4392 -.0070", neck_dia=".405", neck_at="2.4912",
    case_length="2.850 -.020", bullet_dia=".376 -.003", oal_min="3.540", oal_max="3.600", notes=STD_RADII)
row(name="375 Ruger", pdf_page=154, issued="2007-06-13", revised="2022-08-05",
    **{**PRC_HEAD, "rim_thickness": ".050 -.011"}, body_dia_2=".5170", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".5150", shoulder_at="2.1797", shoulder_angle_deg="30",
    datum_dia=".465", datum_at="2.223 -.007", neck_dia=".405", neck_at="2.2750",
    case_length="2.580 -.020", bullet_dia=".376 -.003", oal_min="3.280", oal_max="3.340", notes=STD_RADII)
row(name="375 Winchester", aliases="375 Win", pdf_page=155, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="straight",
    rim_dia=".506 -.010", rim_thickness=".063 -.010", rim_land=".048 -.010",
    body_dia_tol="-.008", head_dia=".4198", body_dia_2=".400", body_dia_2_at=at(".200", "1.600"), mouth_dia=".400",
    case_length="2.020 -.020", bullet_dia=".376 -.003", oal_min="2.530", oal_max="2.560",
    notes="Tapered body to .400 at 1.800 from head, then cylindrical to the mouth; " + UNDERCUT)
row(name="376 Steyr", pdf_page=156, issued="2016-02-24", revised="2024-10-11",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".496 -.010", rim_thickness=".051 -.010", rim_land=".039 -.010", groove_dia=".441 -.020",
    groove_width=".039 +.010", groove_angle_deg="43 -6", body_dia_tol="-.008",
    head_dia=".5057", body_dia_2=".4798", body_dia_2_at=at(".200", "1.400"),
    shoulder_dia=".4744", shoulder_at="1.8933", shoulder_angle_deg="17.535",
    datum_dia=".445", datum_at="1.9398 -.0070", neck_dia=".4028", neck_at="2.0066",
    case_length="2.362 -.020", bullet_dia=".376 -.003", oal_min="3.050", oal_max="3.110",
    by_eye=("shoulder_angle_deg",),
    notes="Metric-origin drawing (mm primary; inch values used here); general diameter tol -.008; "
          "shoulder angle 17°32'6\" B; shoulder radius .100+.050; neck radius .100 max")
row(name="38-40 Winchester", aliases="38-40 Win", pdf_page=157, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".525 -.010", rim_thickness=".065 -.010", rim_land=".050 -.010", groove_dia=".4695",
    body_dia_tol="-.008", head_dia=".4671", body_dia_2=".4562", body_dia_2_at=at(".200", ".613"),
    shoulder_dia=".4543", shoulder_at=".9224", shoulder_angle_deg="6.8",
    datum_dia=".435", datum_at="1.0031 -.0150", neck_dia=".4181", neck_at="1.0740", mouth_dia=".4167",
    case_length="1.305 -.020", bullet_dia=".4005 -.0030", oal_min="1.560", oal_max="1.592",
    by_eye=("shoulder_angle_deg",),
    notes="Shoulder angle 6°48' B; groove_dia is the reference diameter of the optional undercut; " + UNDERCUT +
          "; neck tapers from .4181 to .4167 at mouth; shoulder radius .690 min; neck radius .540 max")
row(name="38-55 Winchester", aliases="38-55 Win", pdf_page=158, issued="1980-04-21", revised="2023-02-10",
    rim_type="rimmed", profile="straight",
    rim_dia=".506 -.010", rim_thickness=".063 -.010", rim_land=".048 -.010", groove_dia=".4210",
    body_dia_tol="-.008", head_dia=".4191", body_dia_2=".3938", body_dia_2_at=at(".200", "1.813"),
    mouth_dia=".3928", case_length="2.085 -.020", bullet_dia=".377 -.003", oal_min="2.470", oal_max="2.510",
    by_eye=("body_dia_2",),
    notes="Drawing prints body_dia_2 as .3838 (10.003 mm); the mm value converts to .3938, which fits "
          "the taper to the .3928 mouth, so .3938 is used; groove_dia is the reference diameter of the "
          "optional undercut; " + UNDERCUT)
row(name="400 Legend", aliases="400 LGND", pdf_page=159, issued="2023-01-15", revised="",
    rim_type="rebated", profile="straight",
    rim_dia=".422 -.010", rim_thickness=".049 -.010", rim_land=".034 -.010", groove_dia=".358 -.020",
    groove_width=".033 +.010", groove_angle_deg="36 -6", body_dia_tol="-.008",
    head_dia=".4400", body_dia_2=".4276", body_dia_2_at=at(".200", "1.350"), mouth_dia=".4267",
    case_length="1.650 -.010", bullet_dia=".4005 -.0030", oal_min="2.125", oal_max="2.260")
row(name="405 Winchester", aliases="405 Win", pdf_page=160, issued="1998-01-24", revised="2023-02-10",
    rim_type="rimmed", profile="straight",
    rim_dia=".543 -.010", rim_thickness=".073 -.010", rim_land=".058 -.010", groove_dia=".4617",
    body_dia_tol="-.008", head_dia=".4604", body_dia_2=".4399", body_dia_2_at=at(".200", "2.000"),
    mouth_dia=".4360", case_length="2.583 -.020", bullet_dia=".4115 -.0030", oal_min="3.050", oal_max="3.175",
    notes="groove_dia is the reference diameter of the optional undercut; " + UNDERCUT)
row(name="416 Remington Magnum", aliases="416 Rem Mag", pdf_page=161, issued="1989-07-21", revised="2022-08-15",
    **{**BELTED_MAG_HEAD, "head_dia": ".5126"}, body_dia_2=".4915", body_dia_2_at=at(".250", "1.750"),
    shoulder_dia=".4868", shoulder_at="2.3890", shoulder_angle_deg="25",
    datum_dia=".4665", datum_at="2.4108 -.0070", neck_dia=".448", neck_at="2.4306", mouth_dia=".447",
    case_length="2.850 -.020", bullet_dia=".416 -.003", oal_min="3.350", oal_max="3.600",
    notes="Belt dia .532-.005 cylindrical; neck tapers from .448 to .447 at mouth; "
          "shoulder radius .040+.050; neck radius .100 max")
row(name="416 Rigby", pdf_page=162, issued="1989-09-08", revised="2022-08-16",
    rim_type="rimless", profile="bottleneck",
    rim_dia=".5902 -.0100", rim_thickness=".065 -.010", rim_land=".050 -.010", groove_dia=".500 -.020",
    groove_width=".031 +.010", groove_angle_deg="45", body_dia_tol="-.008",
    head_dia=".5812", head_dia_at=".500", body_dia_2=".5480", body_dia_2_at=at(".500", "1.500"),
    shoulder_dia=".5401", shoulder_at="2.3557", shoulder_angle_deg="45",
    datum_dia=".496", datum_at="2.3778 -.0070", neck_dia=".4468", neck_at="2.4024", mouth_dia=".4461",
    case_length="2.900 -.020", bullet_dia=".4165 -.0030", oal_min="3.550", oal_max="3.750",
    notes="Head diameter measured at .500 B from the head; neck tapers from .4468 to .4461 at mouth; "
          "shoulder radius .059+.020; neck radius .059 max")
row(name="416 Ruger", pdf_page=163, issued="2009-06-17", revised="2022-08-17",
    **{**PRC_HEAD, "rim_thickness": ".050 -.011"}, body_dia_2=".5170", body_dia_2_at=at(".200", "1.750"),
    shoulder_dia=".5150", shoulder_at="2.1797", shoulder_angle_deg="30",
    datum_dia=".490", datum_at="2.2014 -.0070", neck_dia=".444", neck_at="2.2412", mouth_dia=".443",
    case_length="2.580 -.020", bullet_dia=".4165 -.0030", oal_min="3.215", oal_max="3.340",
    notes="Neck tapers from .444 to .443 at mouth; " + STD_RADII)
row(name="416 Weatherby Magnum", aliases="416 Wby Mag", pdf_page=164, issued="1994-01-12", revised="2024-01-21",
    rim_type="belted", profile="bottleneck",
    rim_dia=".579 -.010", rim_thickness=".063 -.011", rim_land=".049 +.010", groove_dia=".495 -.020",
    groove_angle_deg="45", belt_dia=".6035", belt_length=".252 -.006",
    body_dia_tol="-.004", head_dia=".5817", head_dia_at=".280", body_dia_2=".5642", body_dia_2_at=at(".280", "1.750"),
    shoulder_dia=".561", shoulder_at="2.345",
    datum_dia=".5093", datum_at="2.4228 -.0080", neck_dia=".444", neck_at="2.521",
    case_length="2.913 -.012", bullet_dia=".416 -.003", oal_min="3.650", oal_max="3.750",
    notes="Belt dia .6035-.0040 cylindrical (larger than the rim); head dia tol -.0040; groove width "
          "printed as .049+.010 and stored in rim_land; no separate rim land width given; radiused (venturi) "
          "shoulder: shoulder radius .125+.005, neck radius .164-.005, no shoulder angle")
row(name="44 Remington Magnum (Rifle)", aliases="44 Rem Mag", pdf_page=165, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="straight",
    rim_dia=".514 -.010", rim_thickness=".060 -.011", rim_land=".044 -.010", groove_dia=".4570",
    body_dia_tol="-.005", head_dia=".4569", body_dia_2=".4561", body_dia_2_at=at(".200", "1.000"),
    mouth_dia=".4560", case_length="1.285 -.020", bullet_dia=".432 -.003", oal_min="1.535", oal_max="1.610",
    notes="Rifle drawing (the pistol standard has its own); groove_dia is the reference diameter of the "
          "optional undercut; " + UNDERCUT)
row(name="44-40 Winchester", aliases="44-40 Win", pdf_page=166, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".525 -.010", rim_thickness=".065 -.010", rim_land=".050 -.010", groove_dia=".4712",
    body_dia_tol="-.008", head_dia=".4689", body_dia_2=".4580", body_dia_2_at=at(".200", ".653"),
    shoulder_dia=".4568", shoulder_at=".9275", shoulder_angle_deg="4",
    datum_dia=".446", datum_at="1.0044 -.0150", neck_dia=".4443", neck_at="1.0166", mouth_dia=".443",
    case_length="1.305 -.020", bullet_dia=".427 -.003", oal_min="1.540", oal_max="1.592",
    notes="Drawing is watermarked as revised (superseded); groove_dia is the reference diameter of the optional "
          "undercut; " + UNDERCUT + "; neck tapers from .4443 to .443 at mouth; "
          "shoulder radius .200 min; neck radius .200 max")
row(name="444 Marlin", aliases="444 Mar", pdf_page=167, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="straight",
    rim_dia=".514 -.010", rim_thickness=".063 -.010", rim_land=".048 -.010", groove_dia=".450 -.020",
    groove_width=".025 +.010", groove_angle_deg="45 -6", body_dia_tol="-.008",
    head_dia=".4698", body_dia_2=".4549", body_dia_2_at=at(".200", "1.800"), mouth_dia=".4530",
    case_length="2.225 -.020", bullet_dia=".4305 -.0030", oal_min="2.500", oal_max="2.570", notes=UNDERCUT)
row(name="45-70 Government", aliases="45-70 Govt", pdf_page=168, issued="1979-05-29", revised="2023-02-10",
    rim_type="rimmed", profile="straight",
    rim_dia=".608 -.010", rim_thickness=".070 -.010", rim_land=".055 -.010", groove_dia=".5055",
    body_dia_tol="-.008", head_dia=".5039", body_dia_2=".4813", body_dia_2_at=at(".200", "1.800"),
    mouth_dia=".4800", case_length="2.105 -.020", bullet_dia=".458 -.003", oal_min="2.490", oal_max="2.550",
    notes="groove_dia is the reference diameter of the optional undercut; " + UNDERCUT)
row(name="450 Bushmaster", aliases="450 BM", pdf_page=169, issued="2008-02-01", revised="2022-08-23",
    rim_type="rebated", profile="straight",
    rim_dia=".473 -.010", rim_thickness=".054 -.010", rim_land=".039 -.010", groove_dia=".409 -.010",
    groove_width=".040 +.010", groove_angle_deg="40 -6", body_dia_tol="-.008",
    head_dia=".5000", body_dia_2=".4820", body_dia_2_at=at(".200", "1.350"), mouth_dia=".4800",
    case_length="1.700 -.010", bullet_dia=".4525 -.0030", oal_min="2.000", oal_max="2.260")
row(name="450 Marlin", pdf_page=170, issued="2001-01-10", revised="2022-08-23",
    rim_type="belted", profile="straight",
    rim_dia=".532 -.010", rim_thickness=".050 -.011", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="35 -6", belt_dia=".532", belt_length=".252 -.006",
    body_dia_tol="-.008", head_dia=".5121", head_dia_at=".280", body_dia_2=".4825", body_dia_2_at=at(".280", "1.720"),
    mouth_dia=".4808", case_length="2.100 -.020", bullet_dia=".4583 -.0030", oal_min="2.490", oal_max="2.550",
    notes="Belt dia .532-.010 cylindrical")
row(name="458 Lott", pdf_page=171, issued="1998-06-04", revised="2024-01-21",
    rim_type="belted", profile="straight",
    rim_dia=".532 -.010", rim_thickness=".050 -.011", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="35 -6", belt_dia=".532", belt_length=".220 -.008",
    body_dia_tol="-.008", head_dia=".5127", head_dia_at=".250", body_dia_2=".4835", body_dia_2_at=at(".250", "2.350"),
    mouth_dia=".4810", case_length="2.800 -.020", bullet_dia=".459 -.003", oal_min="3.400", oal_max="3.600",
    notes="Belt dia .532-.005 cylindrical; belt length mm printed as (5.59-0.15)")
row(name="458 Winchester Magnum", aliases="458 Win Mag", pdf_page=172, issued="1980-04-21", revised="2023-02-22",
    rim_type="belted", profile="straight",
    rim_dia=".532 -.010", rim_thickness=".050 -.011", rim_land=".034 -.010", groove_dia=".475 -.020",
    groove_width=".037 +.010", groove_angle_deg="35 -6", belt_dia=".532", belt_length=".220 -.008",
    body_dia_tol="-.008", head_dia=".5126", head_dia_at=".250", body_dia_2=".4825", body_dia_2_at=at(".250", "2.150"),
    mouth_dia=".4811", case_length="2.500 -.020", bullet_dia=".459 -.003", oal_min="3.280", oal_max="3.340",
    notes="Belt dia .532-.005 cylindrical")
row(name="470 Nitro Express", aliases="470 NE", pdf_page=173, issued="1989-09-08", revised="2023-02-10",
    rim_type="rimmed", profile="bottleneck",
    rim_dia=".6551 -.0100", rim_thickness=".040 -.010", rim_land=".028 -.010", groove_dia=".5728",
    body_dia_tol="-.008", head_dia=".5648", head_dia_at=".500", body_dia_2=".5388", body_dia_2_at=at(".500", "1.500"),
    shoulder_dia=".5321", shoulder_at="2.3850", shoulder_angle_deg="7.4025",
    datum_dia=".522", datum_at="2.424 -.015", neck_dia=".5059", neck_at="2.4860", mouth_dia=".5039",
    case_length="3.250 -.020", bullet_dia=".4744 -.0030", oal_min="3.850", oal_max="3.980",
    by_eye=("shoulder_angle_deg",),
    notes="Head diameter measured at .500 B; shoulder angle 7°24'9\" B; groove_dia is the reference diameter of "
          "the optional undercut; " + UNDERCUT + "; neck tapers from .5059 to .5039 at mouth; "
          "shoulder radius .250+.020; neck radius .500 max")
row(name="500 Nitro Express 3\"", aliases="500 NE 3\"", pdf_page=174, issued="2016-02-24", revised="2023-02-10",
    rim_type="rimmed", profile="straight",
    rim_dia=".655 -.010", rim_thickness=".040 -.010", rim_land=".028 -.010", groove_dia=".5740",
    body_dia_tol="-.008", head_dia=".5717", body_dia_2=".5333", body_dia_2_at=at(".200", "2.700"),
    mouth_dia=".5319", case_length="3.000 -.020", bullet_dia=".510 -.003", oal_min="3.500", oal_max="3.750",
    notes="Metric-origin drawing (mm primary; inch values used here); general diameter tol -.008; "
          "groove_dia is the reference diameter of the optional undercut; " + UNDERCUT)

# Values confirmed on a zoomed render whose text layer is garbled (watermark glyphs
# interleaved, "*" merged into ".430*8", or rotated labels extracted backwards).
VERIFIED_BY_EYE = {
    "6mm GT": ("oal_min",),
    "6mm Remington": ("body_dia_2",),
    "6.5 Grendel": ("oal_min",),
    "300 AAC Blackout": ("oal_min",),
    "300 Remington Short Action Ultra Magnum": ("rim_land",),
    "338 Lapua Magnum": ("neck_at", "oal_min"),
    "338 Norma Magnum": ("rim_dia", "groove_dia", "groove_dia_tol"),
}
for r in DATA.rows:
    r["by_eye"] = tuple(r.get("by_eye", ())) + VERIFIED_BY_EYE.get(r["name"], ())

