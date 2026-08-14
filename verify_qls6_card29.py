#!/usr/bin/env python3
"""Exact verifier for a real QLS(6) of cardinality 29.

The coordinate field is Q(tau), where
    123201*tau^2 - 202800*tau - 93848 = 0
and tau is the positive root.  All verification is exact and uses only the
Python standard library (fractions.Fraction).

The 5-dimensional vectors below are ray directions, not unit vectors.
Normalizing each direction and embedding it as (v,0) in R^6, while putting
f=(0,0,0,0,0,1) on every diagonal cell, produces the quantum Latin square.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt, sqrt
from typing import Iterable, List, Sequence, Tuple

# tau^2 = A*tau + B
A = Fraction(202800, 123201)
B = Fraction(93848, 123201)
DISC = 202800**2 + 4 * 123201 * 93848


@dataclass(frozen=True)
class QTau:
    """a + b*tau in Q(tau), represented in the basis (1,tau)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __init__(self, a=0, b=0):
        object.__setattr__(self, "a", a if isinstance(a, Fraction) else Fraction(a))
        object.__setattr__(self, "b", b if isinstance(b, Fraction) else Fraction(b))

    @staticmethod
    def coerce(value) -> "QTau":
        return value if isinstance(value, QTau) else QTau(value)

    def __add__(self, other):
        other = self.coerce(other)
        return QTau(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return QTau(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        # (a+b*t)(c+d*t), with t^2=A*t+B.
        return QTau(
            self.a * other.a + self.b * other.b * B,
            self.a * other.b + self.b * other.a + self.b * other.b * A,
        )

    __rmul__ = __mul__

    def inverse(self):
        # Multiplication by a+b*t has matrix
        # [[a, bB], [b, a+bA]] in the basis (1,t).
        det = self.a * (self.a + self.b * A) - self.b * self.b * B
        if det == 0:
            raise ZeroDivisionError("zero field element")
        return QTau((self.a + self.b * A) / det, -self.b / det)

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) * self.inverse()

    def __pow__(self, exponent: int):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = QTau(1)
        base = self
        n = exponent
        while n:
            if n & 1:
                result = result * base
            base = base * base
            n >>= 1
        return result

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def evaluate(self) -> float:
        tau_value = (2600 + 2 * sqrt(3590422)) / 3159
        return float(self.a) + float(self.b) * tau_value


Scalar = QTau
Vector = List[Scalar]
Cell = Tuple[int, int]


def q(a=0, b=0) -> Scalar:
    return QTau(a, b)


def vadd(*vectors: Sequence[Scalar]) -> Vector:
    result = [q() for _ in range(5)]
    for vector in vectors:
        result = [x + y for x, y in zip(result, vector)]
    return result


def vsub(left: Sequence[Scalar], right: Sequence[Scalar]) -> Vector:
    return [x - y for x, y in zip(left, right)]


def vscale(scalar, vector: Sequence[Scalar]) -> Vector:
    scalar = QTau.coerce(scalar)
    return [scalar * x for x in vector]


def lin(*terms: Tuple[object, Sequence[Scalar]]) -> Vector:
    return vadd(*(vscale(coefficient, vector) for coefficient, vector in terms))


def dot(left: Sequence[Scalar], right: Sequence[Scalar]) -> Scalar:
    return sum((x * y for x, y in zip(left, right)), q())


def determinant(matrix: Sequence[Sequence[Scalar]]) -> Scalar:
    """Exact determinant by Gaussian elimination over Q(tau)."""
    n = len(matrix)
    work = [list(row) for row in matrix]
    result = q(1)
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if not work[row][column].is_zero()),
            None,
        )
        if pivot is None:
            return q()
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result = result * pivot_value
        inverse_pivot = pivot_value.inverse()
        for j in range(column, n):
            work[column][j] = work[column][j] * inverse_pivot
        for row in range(column + 1, n):
            factor = work[row][column]
            if factor.is_zero():
                continue
            for j in range(column, n):
                work[row][j] = work[row][j] - factor * work[column][j]
    return result


def cross4(vectors: Sequence[Sequence[Scalar]]) -> Vector:
    """Five-dimensional generalized cross product of four vectors."""
    if len(vectors) != 4:
        raise ValueError("cross4 requires four vectors")
    result: Vector = []
    for deleted_column in range(5):
        minor = [
            [row[j] for j in range(5) if j != deleted_column]
            for row in vectors
        ]
        value = determinant(minor)
        result.append(-value if deleted_column % 2 else value)
    return result


def project_orthogonal(
    vector: Sequence[Scalar],
    orthogonal_basis_with_norms: Iterable[Tuple[Sequence[Scalar], Scalar]],
) -> Vector:
    result = list(vector)
    for basis_vector, squared_norm in orthogonal_basis_with_norms:
        result = vsub(
            result,
            vscale(dot(vector, basis_vector) / squared_norm, basis_vector),
        )
    return result


def proportional(left: Sequence[Scalar], right: Sequence[Scalar]) -> bool:
    """Exact projective equality, tested by all 2x2 minors."""
    return all(
        (left[i] * right[j] - left[j] * right[i]).is_zero()
        for i in range(5)
        for j in range(i)
    )


def build_directions() -> dict[Cell, Vector]:
    basis: List[Vector] = []
    for i in range(5):
        basis.append([q(1) if i == j else q() for j in range(5)])
    e0, e1, e2, e3, e4 = basis

    # Four rational rotations.
    a = lin((Fraction(4, 5), e3), (Fraction(3, 5), e4))
    p = lin((Fraction(-3, 5), e3), (Fraction(4, 5), e4))
    d = lin((Fraction(5, 13), e1), (Fraction(-12, 13), e2))
    t = lin((Fraction(12, 13), e1), (Fraction(5, 13), e2))
    qv = lin((Fraction(8, 17), t), (Fraction(15, 17), e4))
    r = lin((Fraction(15, 17), t), (Fraction(-8, 17), e4))

    # Orthogonal decomposition qv=X+H, with companion directions Y and U.
    X = lin((Fraction(96, 221), e1), (Fraction(12, 17), p))
    H = lin((Fraction(40, 221), e2), (Fraction(9, 17), a))
    Y = lin((Fraction(12, 17), e1), (Fraction(-96, 221), p))
    U = lin((Fraction(9, 17), e2), (Fraction(-40, 221), a))
    sigma = dot(X, X)  # 33552/48841
    rho = dot(H, H)    # 15289/48841
    S = vsub(vscale(rho, X), vscale(sigma, H))

    W = lin((32, e0), (-51, qv))
    Z = lin((51, e0), (32, qv))
    Bv = lin((51 * rho, e0), (32, H))
    Cv = lin((32, e0), (-51, H))

    tau = q(0, 1)
    T1 = lin((4, e0), (-3, t))
    T2 = lin((1, d), (tau, e3))

    # G is the projection of X onto span(e4,T1,T2)^perp.
    G = project_orthogonal(
        X,
        [(e4, q(1)), (T1, q(25)), (T2, q(1) + tau * tau)],
    )

    # K is identically perpendicular to e4,T1,T2,X.
    K = [q(1521, 600), q(1872), q(780, 2080), q(1920), q()]

    gu = dot(G, U)
    gy = dot(G, Y)
    L = vsub(vscale(gu, Y), vscale(gy, U))
    M = vadd(vscale(gy * rho, Y), vscale(gu * sigma, U))

    N3 = cross4([L, Bv, W, G])
    N4 = cross4([M, Cv, X, K])

    directions: dict[Cell, Vector] = {}
    for column, vector in zip([1, 2, 3, 4, 5], basis):
        directions[(0, column)] = vector

    directions.update(
        {
            (1, 0): lin((3, e0), (4, t)),
            (1, 2): vscale(-1, p),
            (1, 3): a,
            (1, 4): d,
            (1, 5): T1,
            (2, 0): lin((tau, d), (-1, e3)),
            (2, 1): qv,
            (2, 3): e0,
            (2, 4): r,
            (2, 5): T2,
            (3, 0): N3,
            (3, 1): L,
            (3, 2): Bv,
            (3, 4): W,
            (3, 5): G,
            (4, 0): N4,
            (4, 1): M,
            (4, 2): Cv,
            (4, 3): X,
            (4, 5): K,
            (5, 0): W,
            (5, 1): S,
            (5, 2): U,
            (5, 3): Y,
            (5, 4): Z,
        }
    )
    return directions


def verify() -> None:
    assert isqrt(DISC) ** 2 != DISC, "quadratic polynomial must be irreducible"
    directions = build_directions()
    assert len(directions) == 30

    # Every direction is nonzero.
    for cell, vector in directions.items():
        assert any(not coordinate.is_zero() for coordinate in vector), cell

    # Check all 120 pairwise orthogonality conditions in rows and columns.
    checks = 0
    for row in range(6):
        cells = [(row, column) for column in range(6) if column != row]
        for i in range(5):
            for j in range(i):
                assert dot(directions[cells[i]], directions[cells[j]]).is_zero(), (
                    "row",
                    row,
                    cells[i],
                    cells[j],
                )
                checks += 1
    for column in range(6):
        cells = [(row, column) for row in range(6) if row != column]
        for i in range(5):
            for j in range(i):
                assert dot(directions[cells[i]], directions[cells[j]]).is_zero(), (
                    "column",
                    column,
                    cells[i],
                    cells[j],
                )
                checks += 1
    assert checks == 120

    # Exact ray classification.
    groups: List[List[Cell]] = []
    for cell in sorted(directions):
        for group in groups:
            if proportional(directions[cell], directions[group[0]]):
                group.append(cell)
                break
        else:
            groups.append([cell])

    repeated = [group for group in groups if len(group) > 1]
    assert len(groups) == 28
    assert repeated == [[(0, 1), (2, 3)], [(3, 4), (5, 0)]]

    # Give compact phase-class labels, with D denoting the common diagonal ray.
    labels: dict[Cell, int] = {}
    for label, group in enumerate(groups):
        for cell in group:
            labels[cell] = label
    phase_matrix = []
    for row in range(6):
        phase_matrix.append(
            ["D" if row == column else labels[(row, column)] for column in range(6)]
        )

    tau_value = (2600 + 2 * sqrt(3590422)) / 3159
    print("Exact QLS(6), cardinality-29 verification PASSED")
    print(f"tau = {tau_value:.15f}")
    print(f"orthogonality checks: {checks}")
    print(f"off-diagonal ray classes: {len(groups)}")
    print(f"repeated off-diagonal classes: {repeated}")
    print("total cardinality: 28 + 1 common diagonal ray = 29")
    print("phase-class matrix:")
    for row in phase_matrix:
        print("  ", row)


if __name__ == "__main__":
    verify()
