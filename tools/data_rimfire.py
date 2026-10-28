"""SAAMI Z299.1-R2026 Rimfire cartridge drawings (PDF pages 15-25).

Rimfire heads have no chamfer or extractor groove; the rim edge radii and the
fillet ahead of the rim are recorded in notes.
"""
from saami_common import CARTRIDGE_COLUMNS, Dataset

DATA = Dataset(CARTRIDGE_COLUMNS, dict(rim_type="rimmed", body_dia_tol="-.004"))
row = DATA.row

row(name="17 Mach 2", aliases="17 M 2", pdf_page=15, issued="2004-06-23", revised="2026-01-28",
    profile="bottleneck",
    rim_dia=".278", rim_dia_tol="-.012", rim_thickness=".043", rim_thickness_tol="-.007",
    head_dia=".226", shoulder_at=".5602", shoulder_angle_deg="20",
    datum_dia=".2046", datum_at=".5896", datum_at_tol="-.0100", neck_dia=".190", neck_at=".6097",
    case_length=".714", case_length_tol="-.008",
    bullet_dia=".1725", bullet_dia_tol="-.0035", oal_min=".965", oal_max="1.000",
    notes="Body cylindrical; rim radii 2X .015+.005; fillet ahead of rim .007 R max; "
          "shoulder radius .025+.025; neck radius .050 max")
row(name="17 Hornady Magnum Rimfire", aliases="17 HMR", pdf_page=16, issued="2002-06-25", revised="2025-02-06",
    profile="bottleneck",
    rim_dia=".294", rim_dia_tol="-.012", rim_thickness=".050", rim_thickness_tol="-.008",
    head_dia=".242", shoulder_at=".8740", shoulder_angle_deg="25",
    datum_dia=".215", datum_at=".903", datum_at_tol="-.010", neck_dia=".193", neck_at=".9266",
    case_length="1.064", case_length_tol="-.008",
    bullet_dia=".1725", bullet_dia_tol="-.0035", oal_min="1.330", oal_max="1.365",
    notes="Body cylindrical; rim radii 2X .015+.005; fillet ahead of rim .007 R max; "
          "shoulder radius .010+.020; neck radius .050 max")
row(name="17 Winchester Super Magnum", aliases="17 WSM", pdf_page=17, issued="2015-07-24", revised="2025-01-19",
    profile="bottleneck",
    rim_dia=".333", rim_dia_tol="-.009", rim_thickness=".066", rim_thickness_tol="-.005",
    head_dia=".269", shoulder_at=".9619", shoulder_angle_deg="20",
    datum_dia=".234", datum_at="1.010", datum_at_tol="-.010", neck_dia=".197", neck_at="1.0608",
    case_length="1.200", case_length_tol="-.008",
    bullet_dia=".1725", bullet_dia_tol="-.0035", oal_min="1.440", oal_max="1.590",
    notes="Body cylindrical; rim radii 2X .025+.005; fillet ahead of rim .012-.003 R; "
          "shoulder radius .060+.050; neck radius .010 max")
row(name="21 Sharp", pdf_page=18, issued="2023-06-06", revised="2025-01-19", profile="straight",
    rim_dia=".278", rim_dia_tol="-.012", rim_thickness=".043", rim_thickness_tol="-.007",
    head_dia=".226", case_length=".613", case_length_tol="-.008",
    bullet_dia=".2105", bullet_dia_tol="-.0035", oal_min=".965", oal_max="1.000",
    notes="Body cylindrical; rim radii 2X .015+.010")
row(name="22 Short", aliases="22 S; 22 Short CB; 22 Short Gallery", pdf_page=19,
    issued="1979-05-29", revised="2026-01-28", profile="straight",
    rim_dia=".278", rim_dia_tol="-.012", rim_thickness=".043", rim_thickness_tol="-.007",
    head_dia=".226", case_length=".421", case_length_tol="-.008",
    bullet_dia=".225", bullet_dia_tol="-.004", oal_min=".660", oal_max=".695",
    notes="Body cylindrical; heeled bullet; rim radii 2X .015+.010")
row(name="22 Long", aliases="22 L", pdf_page=20, issued="1979-05-29", revised="2025-01-19", profile="straight",
    rim_dia=".278", rim_dia_tol="-.012", rim_thickness=".043", rim_thickness_tol="-.007",
    head_dia=".226", case_length=".613", case_length_tol="-.008",
    bullet_dia=".225", bullet_dia_tol="-.004", oal_min=".853", oal_max=".888",
    notes="Body cylindrical; heeled bullet; rim radii 2X .015+.005")
row(name="22 Long Rifle - Match", aliases="22 LR", pdf_page=21, issued="1979-05-29", revised="2026-01-28",
    profile="straight",
    rim_dia=".278", rim_dia_tol="-.012", rim_thickness=".043", rim_thickness_tol="-.007",
    head_dia=".226", case_length=".613", case_length_tol="-.008",
    bullet_dia=".2255", bullet_dia_tol="-.0040", oal_min=".950", oal_max="1.000",
    notes="Body cylindrical; heeled bullet; rim radii 2X .015+.010")
row(name="22 Long Rifle - Sporting", aliases="22 LR", pdf_page=22, issued="1979-05-29", revised="2025-01-19",
    profile="straight",
    rim_dia=".278", rim_dia_tol="-.012", rim_thickness=".043", rim_thickness_tol="-.007",
    head_dia=".226", case_length=".613", case_length_tol="-.008",
    bullet_dia=".2255", bullet_dia_tol="-.0040", oal_min=".950", oal_max="1.000",
    notes="Body cylindrical; heeled bullet; rim radii 2X .015+.010")
row(name="22 Long Rifle - Shot", aliases="22 LR", pdf_page=23, issued="1979-05-29", revised="2025-01-19",
    profile="straight",
    rim_dia=".278", rim_dia_tol="-.012", rim_thickness=".043", rim_thickness_tol="-.007",
    head_dia=".226", mouth_dia=".217", case_length=".7078", oal_min=".955", oal_max=".990",
    notes="Body cylindrical; shot load, no bullet; 4°30' B crimp taper starts at .6506; "
          "mouth_dia is the crimp diameter .217-.005; case_length is a reference dimension; "
          "rim radii 2X .015+.010")
row(name="22 Winchester Rimfire", aliases="22 WRF", pdf_page=24, issued="2006-06-28", revised="2025-01-19",
    profile="straight",
    rim_dia=".300", rim_dia_tol="-.012", rim_thickness=".050", rim_thickness_tol="-.008",
    head_dia=".2454", head_dia_at=".100", body_dia_2=".2436", body_dia_2_at=".900",
    mouth_dia=".2435", case_length=".965", case_length_tol="-.020",
    bullet_dia=".2285", bullet_dia_tol="-.0040", oal_min="1.145", oal_max="1.180",
    notes="Diameter at rim front .2455 (reference); rim radius .015+.010")
row(name="22 Winchester Magnum Rimfire", aliases="22 WMR", pdf_page=25, issued="1979-05-29", revised="2025-01-19",
    profile="straight",
    rim_dia=".294", rim_dia_tol="-.012", rim_thickness=".050", rim_thickness_tol="-.008",
    head_dia=".242", case_length="1.055", case_length_tol="-.008",
    bullet_dia=".2245", bullet_dia_tol="-.0040", oal_min="1.315", oal_max="1.350",
    notes="Body cylindrical; rim radii 2X .015+.005")
