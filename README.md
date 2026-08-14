# Order-six quantum Latin square of cardinality 29

This repository is the canonical artifact for Unsolved Labs release R011.

## Frozen claim

There exists a real quantum Latin square of order 6 with cardinality 29.

Let \(\tau\) be the positive root of

\[
123201\tau^2-202800\tau-93848=0.
\]

`CONSTRUCTION.md` gives an explicit algebraic construction in \(\mathbb R^6\subset\mathbb C^6\). Every row and every column is an orthonormal basis after normalization, and the 36 cells represent exactly 29 rays modulo global phase.

## Baseline and novelty boundary

Zhipeng Xu, *New Cardinalities for Quantum Latin Squares of Order Six*, arXiv:2607.11800v3 (revised 2026-08-04), constructs order-six quantum Latin squares of cardinalities 19, 21, 23, 25, 27, 32, and 35 and states that 29 is the single unresolved order-six cardinality after combining the known results.

Primary source: https://arxiv.org/abs/2607.11800v3

The release claim is only the explicit existence of a cardinality-29 QLS(6). It does not claim uniqueness, classification, or optimality of the algebraic representation.

## Exact verification

Principal verifier — Python standard library only:

```bash
python verify_qls6_card29.py
```

Independent reimplementation using SymPy:

```bash
python -m pip install -r requirements.txt
python verify_qls6_card29_sympy.py
```

The verifiers check exactly:

- all 30 off-diagonal directions are nonzero;
- all 120 within-row and within-column orthogonality equations vanish;
- all 435 pairwise projective-equivalence decisions among off-diagonal directions;
- exactly two repeated off-diagonal ray classes;
- 28 off-diagonal ray classes plus one common diagonal ray, hence cardinality 29.

`qls6_card29_vectors.json` is a decimal export for independent numerical inspection. It is not part of the mathematical trust boundary.

## Files

- `CONSTRUCTION.md` — explicit algebraic construction and proof outline.
- `verify_qls6_card29.py` — exact verifier over the quadratic field \(\mathbb Q(\tau)\), using only `fractions.Fraction`.
- `verify_qls6_card29_sympy.py` — independent symbolic reimplementation.
- `qls6_card29_vectors.json` — normalized high-precision vector export.
- `claim.json` — machine-readable frozen claim and verification contract.

## Review status

Machine verification is complete. Independent specialist review is pending.
