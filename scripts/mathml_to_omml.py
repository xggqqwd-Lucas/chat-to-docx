#!/usr/bin/env python3
"""Convert Presentation MathML to editable Word OMML."""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
from typing import Optional

from lxml import etree


COMMON_XSL_PATHS = (
    Path(r"C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL"),
    Path(r"C:\Program Files (x86)\Microsoft Office\root\Office16\MML2OMML.XSL"),
)


def find_mml2omml() -> Path:
    for path in COMMON_XSL_PATHS:
        if path.is_file():
            return path
    raise FileNotFoundError("MML2OMML.XSL was not found in the common Office paths")


def mathml_to_omml(mathml: str, xsl_path: Optional[Path] = None):
    xsl_path = Path(xsl_path) if xsl_path else find_mml2omml()
    transform = etree.XSLT(etree.parse(str(xsl_path)))
    root = etree.fromstring(mathml.encode("utf-8"))
    return deepcopy(transform(root).getroot())


def append_display_equation(paragraph, mathml: str, xsl_path: Optional[Path] = None):
    paragraph._p.append(mathml_to_omml(mathml, xsl_path))
    return paragraph


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mathml_file", nargs="?", type=Path)
    parser.add_argument("--xsl", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        mathml = '<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><mi>x</mi><mo>=</mo><mn>1</mn></mrow></math>'
    elif args.mathml_file:
        mathml = args.mathml_file.read_text(encoding="utf-8")
    else:
        parser.error("provide mathml_file or --self-test")
    omml = mathml_to_omml(mathml, args.xsl)
    print(etree.tostring(omml, encoding="unicode", pretty_print=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

