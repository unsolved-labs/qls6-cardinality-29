#!/usr/bin/env python3
"""One-command verification entry point for Unsolved Labs R011."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(*args):
    print("+", " ".join(str(x) for x in args), flush=True)
    subprocess.run([str(x) for x in args], cwd=ROOT, check=True)


def check_artifacts():
    manifest = ROOT / "ARTIFACTS.sha256"
    expected = {}
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw or raw.startswith("#"):
            continue
        digest, path = raw.split(maxsplit=1)
        expected[path] = digest
    for path, digest in expected.items():
        data = (ROOT / path).read_bytes()
        actual = hashlib.sha256(data).hexdigest()
        if actual != digest:
            raise SystemExit(f"artifact hash mismatch for {path}: {actual} != {digest}")
    print(f"artifact hash verification PASSED ({len(expected)} files)")


def check_claim():
    claim = json.loads((ROOT / "claim.json").read_text(encoding="utf-8"))
    if claim.get("release") != "R011":
        raise SystemExit("claim.json release must be R011")
    if claim.get("expected", {}).get("total_cardinality") != 29:
        raise SystemExit("claim.json must freeze total_cardinality=29")
    if claim.get("review_status") != "pending":
        raise SystemExit("review_status must remain pending absent public review evidence")
    print("claim metadata verification PASSED")


def check_markdown_math():
    legacy = re.compile(r"\\\(|\\\)|\\\[|\\\]")
    offenders = []
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if legacy.search(text):
            offenders.append(str(path.relative_to(ROOT)))
    if offenders:
        raise SystemExit(
            "legacy GitHub math delimiters found in: " + ", ".join(offenders)
        )
    print("GitHub Markdown math-delimiter lint PASSED")


def check_pdf():
    pdf = ROOT / "manuscript" / "qls6_cardinality_29.pdf"
    if not pdf.exists():
        raise SystemExit("committed manuscript PDF is missing")
    if not pdf.read_bytes().startswith(b"%PDF-"):
        raise SystemExit("committed manuscript PDF is not a PDF file")
    print("manuscript PDF presence/signature check PASSED")


def main():
    check_claim()
    check_markdown_math()
    check_pdf()
    run(sys.executable, "verify_qls6_card29.py")
    run(
        sys.executable,
        "generate_exact_certificate.py",
        "--check",
        "certificate/qls6_card29_exact.json",
    )
    run(sys.executable, "verify_certificate.py", "certificate/qls6_card29_exact.json")
    run(sys.executable, "verify_qls6_card29_sympy.py")
    check_artifacts()
    print("R011 release verification PASSED")


if __name__ == "__main__":
    main()
