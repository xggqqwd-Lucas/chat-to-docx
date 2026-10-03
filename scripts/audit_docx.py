#!/usr/bin/env python3
"""Audit a DOCX for chat artifacts, mojibake, and editable equations."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
SUSPICIOUS = ("\ufffd", "\ue200cite", "\ue200navlist")


def audit(path: Path) -> dict:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    text_xml = xml.decode("utf-8", errors="replace")
    root = ET.fromstring(xml)
    texts = [node.text or "" for node in root.iter(f"{{{W_NS}}}t")]
    visible = "".join(texts)
    equations = sum(1 for _ in root.iter(f"{{{M_NS}}}oMath"))
    findings = {marker: visible.count(marker) + text_xml.count(marker) for marker in SUSPICIOUS}
    raw_latex = len(re.findall(r"(?:\\\[|\\\]|\$\$|\\begin\{|\\frac\{|\\sum_|\\int_)", visible))
    return {
        "path": str(path.resolve()),
        "paragraph_markers": text_xml.count("<w:p"),
        "equation_count": equations,
        "raw_latex_markers": raw_latex,
        "suspicious": findings,
        "clean": raw_latex == 0 and all(value == 0 for value in findings.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--expect-equations", type=int)
    args = parser.parse_args()
    report = audit(args.docx)
    if args.expect_equations is not None:
        report["equation_count_matches"] = report["equation_count"] == args.expect_equations
        report["clean"] = report["clean"] and report["equation_count_matches"]
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"DOCX: {report['path']}")
        print(f"Editable equations: {report['equation_count']}")
        print(f"Raw LaTeX markers: {report['raw_latex_markers']}")
        for marker, count in report["suspicious"].items():
            safe_marker = marker.encode("unicode_escape").decode("ascii")
            print(f"{safe_marker}: {count}")
        print("PASS" if report["clean"] else "FAIL")
    return 0 if report["clean"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
