#!/usr/bin/env python3
"""Small exact checker for the frozen R011 QLS(6), cardinality-29 certificate.

Trust boundary:
  * Python integer arithmetic and fractions.Fraction;
  * this checker;
  * the committed JSON certificate.

The checker does not import the construction/generation code.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from math import isqrt
from pathlib import Path

A = Fraction(202800, 123201)
B = Fraction(93848, 123201)
DISC = 202800**2 + 4 * 123201 * 93848


@dataclass(frozen=True)
class QTau:
    a: Fraction
    b: Fraction

    @staticmethod
    def coerce(value):
        return value if isinstance(value, QTau) else QTau(Fraction(value), Fraction(0))

    def __add__(self, other):
        other = self.coerce(other)
        return QTau(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return QTau(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __mul__(self, other):
        other = self.coerce(other)
        return QTau(
            self.a * other.a + self.b * other.b * B,
            self.a * other.b + self.b * other.a + self.b * other.b * A,
        )

    __rmul__ = __mul__

    def is_zero(self):
        return self.a == 0 and self.b == 0


ZERO = QTau(Fraction(0), Fraction(0))


def parse_fraction(pair):
    if not (isinstance(pair, list) and len(pair) == 2):
        raise ValueError(f"invalid rational encoding: {pair!r}")
    numerator, denominator = pair
    if not isinstance(numerator, int) or not isinstance(denominator, int) or denominator == 0:
        raise ValueError(f"invalid rational encoding: {pair!r}")
    return Fraction(numerator, denominator)


def parse_scalar(obj):
    if set(obj) != {"a", "b"}:
        raise ValueError(f"invalid field element: {obj!r}")
    return QTau(parse_fraction(obj["a"]), parse_fraction(obj["b"]))


def dot(left, right):
    return sum((x * y for x, y in zip(left, right)), ZERO)


def proportional(left, right):
    return all(
        (left[i] * right[j] - left[j] * right[i]).is_zero()
        for i in range(5)
        for j in range(i)
    )


def load_certificate(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or data.get("release") != "R011":
        raise ValueError("unexpected certificate schema/release")
    if data.get("field", {}).get("minimal_polynomial") != [123201, -202800, -93848]:
        raise ValueError("unexpected minimal polynomial")
    directions = {}
    for entry in data.get("directions", []):
        cell = tuple(entry["cell"])
        if len(cell) != 2 or not all(isinstance(x, int) for x in cell):
            raise ValueError(f"invalid cell: {cell!r}")
        if cell[0] == cell[1] or not all(0 <= x < 6 for x in cell):
            raise ValueError(f"invalid off-diagonal cell: {cell!r}")
        if cell in directions:
            raise ValueError(f"duplicate cell: {cell!r}")
        coordinates = [parse_scalar(x) for x in entry["coordinates"]]
        if len(coordinates) != 5:
            raise ValueError(f"cell {cell!r} must have five coordinates")
        directions[cell] = coordinates
    return data, directions


def verify(path):
    if isqrt(DISC) ** 2 == DISC:
        raise AssertionError("minimal polynomial unexpectedly reducible over Q")

    data, directions = load_certificate(path)
    if len(directions) != 30:
        raise AssertionError(f"expected 30 off-diagonal directions, found {len(directions)}")

    for cell, vector in directions.items():
        if not any(not coordinate.is_zero() for coordinate in vector):
            raise AssertionError(f"zero direction at {cell}")

    checks = 0
    for row in range(6):
        cells = [(row, column) for column in range(6) if column != row]
        for i in range(5):
            for j in range(i):
                if not dot(directions[cells[i]], directions[cells[j]]).is_zero():
                    raise AssertionError(("row", row, cells[i], cells[j]))
                checks += 1

    for column in range(6):
        cells = [(row, column) for row in range(6) if row != column]
        for i in range(5):
            for j in range(i):
                if not dot(directions[cells[i]], directions[cells[j]]).is_zero():
                    raise AssertionError(("column", column, cells[i], cells[j]))
                checks += 1

    if checks != 120:
        raise AssertionError(f"expected 120 orthogonality checks, found {checks}")

    groups = []
    pair_tests = 0
    cells = sorted(directions)
    for i, cell in enumerate(cells):
        for other in cells[:i]:
            proportional(directions[cell], directions[other])
            pair_tests += 1
        for group in groups:
            if proportional(directions[cell], directions[group[0]]):
                group.append(cell)
                break
        else:
            groups.append([cell])

    repeated = [group for group in groups if len(group) > 1]
    expected_repeated = [[(0, 1), (2, 3)], [(3, 4), (5, 0)]]
    if pair_tests != 435:
        raise AssertionError(f"expected 435 pairwise ray tests, found {pair_tests}")
    if len(groups) != 28:
        raise AssertionError(f"expected 28 off-diagonal ray classes, found {len(groups)}")
    if repeated != expected_repeated:
        raise AssertionError(f"unexpected repeated classes: {repeated!r}")

    expected = data.get("expected", {})
    if expected.get("orthogonality_checks") != 120:
        raise AssertionError("certificate metadata disagrees on orthogonality count")
    if expected.get("off_diagonal_pairwise_ray_tests") != 435:
        raise AssertionError("certificate metadata disagrees on pairwise ray tests")
    if expected.get("off_diagonal_ray_classes") != 28:
        raise AssertionError("certificate metadata disagrees on ray-class count")
    if expected.get("total_cardinality") != 29:
        raise AssertionError("certificate metadata disagrees on total cardinality")

    print("Frozen exact-certificate verification PASSED")
    print("off-diagonal directions: 30")
    print("orthogonality checks: 120")
    print("pairwise ray tests: 435")
    print("off-diagonal ray classes: 28")
    print(f"repeated classes: {repeated}")
    print("total cardinality: 28 + 1 common diagonal ray = 29")


if __name__ == "__main__":
    certificate = sys.argv[1] if len(sys.argv) > 1 else "certificate/qls6_card29_exact.json"
    verify(certificate)
