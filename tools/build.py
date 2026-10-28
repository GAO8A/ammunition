"""Build one dataset CSV from its transcription module and the SAAMI PDF.

usage: build.py <dataset> <pdf> <out.csv>
  dataset: pistol | rifle | rimfire | shotshell
"""
import importlib, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from saami_common import build

dataset, pdf_path, out_path = sys.argv[1:4]
build(importlib.import_module(f"data_{dataset}").DATA, pdf_path, out_path)
