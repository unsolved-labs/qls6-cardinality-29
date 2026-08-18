#!/usr/bin/env python3
"""Generate or check the frozen exact R011 certificate from the construction code.

This script is a bridge from the construction implementation to the committed certificate.
It is not part of the final certificate checker's trust boundary.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path

from verify_qls6_card29 import build_directions


def fraction_pair(value: Fraction):
    return [value.numerator, value.denominator]


def serialize():
    directions = build_directions()
    data = {
        "schema_version": 1,
        "release": "R011",
        "description": "Exact off-diagonal ray directions for a real QLS(6) of cardinality 29.",
        "field": {
            "basis": ["1", "tau"],
            "minimal_polynomial": [123201, -202800, -93848],
            "relation": "123201*tau^2 - 202800*tau - 93848 = 0",
        },
        "embedding": {
            "off_diagonal": "(v,0) in R^6",
            "diagonal": "[0,0,0,0,0,1]",
            "normalization": "Each nonzero off-diagonal direction is normalized independently.",
        },
        "expected": {
            "nonzero_off_diagonal_directions": 30,
            "orthogonality_checks": 120,
            "off_diagonal_pairwise_ray_tests": 435,
            "off_diagonal_ray_classes": 28,
            "repeated_off_diagonal_classes": [[[0, 1], [2, 3]], [[3, 4], [5, 0]]],
            "total_cardinality": 29,
        },
        "directions": [],
    }
    for cell in sorted(directions):
        coordinates = []
        for scalar in directions[cell]:
            coordinates.append({
                "a": fraction_pair(scalar.a),
                "b": fraction_pair(scalar.b),
            })
        data["directions"].append({"cell": list(cell), "coordinates": coordinates})
    return data


def canonical_text():
    return json.dumps(serialize(), sort_keys=True, separators=(",", ":")) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=None)
    parser.add_argument("--check", default=None)
    args = parser.parse_args()

    if bool(args.output) == bool(args.check):
        parser.error("choose exactly one of --output or --check")

    generated = canonical_text()
    if args.output:
        Path(args.output).write_text(generated, encoding="utf-8")
        print(f"wrote {args.output}")
        return

    committed = Path(args.check).read_text(encoding="utf-8")
    if committed != generated:
        raise SystemExit(
            "certificate mismatch: regenerate with "
            f"`python {Path(__file__).name} --output {args.check}`"
        )
    print("construction-to-certificate comparison PASSED")


if __name__ == "__main__":
    main()
