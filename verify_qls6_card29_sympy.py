#!/usr/bin/env python3
"""Independent SymPy verifier for the cardinality-29 QLS(6)."""

from __future__ import annotations

import sympy as sp

T = sp.symbols("T")
P = sp.Poly(123201*T**2 - 202800*T - 93848, T, domain=sp.QQ)
Q = sp.Rational


def reduce_field(expr):
    expr = sp.cancel(sp.together(expr))
    numerator, denominator = sp.fraction(expr)
    nr = sp.rem(sp.Poly(numerator, T, domain=sp.QQ), P)
    dr = sp.rem(sp.Poly(denominator, T, domain=sp.QQ), P)
    inv = sp.invert(dr, P)
    return sp.factor(sp.rem(nr * inv, P).as_expr())


def zero(expr):
    return reduce_field(expr) == 0


def cross4(*vectors):
    matrix = sp.Matrix.hstack(*vectors).T
    return sp.Matrix([
        (-1)**column * matrix[:, [j for j in range(5) if j != column]].det()
        for column in range(5)
    ])


def proportional(v, w):
    return all(zero(v[i]*w[j] - v[j]*w[i]) for i in range(5) for j in range(i))


E = [sp.eye(5).col(i) for i in range(5)]
e0, e1, e2, e3, e4 = E

a = Q(4,5)*e3 + Q(3,5)*e4
p = -Q(3,5)*e3 + Q(4,5)*e4
d = Q(5,13)*e1 - Q(12,13)*e2
t = Q(12,13)*e1 + Q(5,13)*e2
q = Q(8,17)*t + Q(15,17)*e4
r = Q(15,17)*t - Q(8,17)*e4

X = Q(96,221)*e1 + Q(12,17)*p
H = Q(40,221)*e2 + Q(9,17)*a
Y = Q(12,17)*e1 - Q(96,221)*p
U = Q(9,17)*e2 - Q(40,221)*a
sigma = sp.factor(X.dot(X))
rho = sp.factor(H.dot(H))
S = rho*X - sigma*H

W = 32*e0 - 51*q
Z = 51*e0 + 32*q
B = 51*rho*e0 + 32*H
C = 32*e0 - 51*H
T1 = 4*e0 - 3*t
T2 = d + T*e3

G = (
    X
    - X.dot(e4)*e4
    - X.dot(T1)/25*T1
    - X.dot(T2)/(1+T**2)*T2
)
K = (600*T+1521)*e0 + 1872*e1 + (2080*T+780)*e2 + 1920*e3

gu, gy = G.dot(U), G.dot(Y)
L = gu*Y - gy*U
M = gy*rho*Y + gu*sigma*U
N3 = cross4(L, B, W, G)
N4 = cross4(M, C, X, K)

V = {}
for column, vector in zip([1,2,3,4,5], E):
    V[(0,column)] = vector
V.update({
    (1,0): 3*e0+4*t, (1,2): -p, (1,3): a, (1,4): d, (1,5): T1,
    (2,0): T*d-e3, (2,1): q, (2,3): e0, (2,4): r, (2,5): T2,
    (3,0): N3, (3,1): L, (3,2): B, (3,4): W, (3,5): G,
    (4,0): N4, (4,1): M, (4,2): C, (4,3): X, (4,5): K,
    (5,0): W, (5,1): S, (5,2): U, (5,3): Y, (5,4): Z,
})
V = {cell: sp.Matrix([reduce_field(x) for x in vector]) for cell, vector in V.items()}

assert len(V) == 30
assert all(any(not zero(x) for x in vector) for vector in V.values())

checks = 0
for row in range(6):
    cells = [(row,column) for column in range(6) if column != row]
    for i in range(5):
        for j in range(i):
            assert zero(V[cells[i]].dot(V[cells[j]])), ("row", row, cells[i], cells[j])
            checks += 1
for column in range(6):
    cells = [(row,column) for row in range(6) if row != column]
    for i in range(5):
        for j in range(i):
            assert zero(V[cells[i]].dot(V[cells[j]])), ("column", column, cells[i], cells[j])
            checks += 1
assert checks == 120

groups = []
for cell in sorted(V):
    for group in groups:
        if proportional(V[cell], V[group[0]]):
            group.append(cell)
            break
    else:
        groups.append([cell])

repeated = [group for group in groups if len(group) > 1]
assert len(groups) == 28
assert repeated == [[(0,1),(2,3)],[(3,4),(5,0)]]

print("Independent SymPy verification PASSED")
print("orthogonality checks:", checks)
print("off-diagonal classes:", len(groups))
print("repeated classes:", repeated)
print("total cardinality: 29")
