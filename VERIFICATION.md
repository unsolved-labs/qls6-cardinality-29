# R011 verification contract

This document defines the public verification boundary for the R011 cardinality-29 quantum Latin square.

## One-command reproduction

From a clean checkout with Python 3.12:

```bash
python -m pip install -r requirements.txt
python verify_release.py
```

A successful run must end with:

```text
R011 release verification PASSED
```

CI runs the same release entry point.

## Verification layers

### A. Construction-level exact replay

```bash
python verify_qls6_card29.py
```

Properties:

- Python standard library only;
- exact rational arithmetic using `fractions.Fraction`;
- two-coordinate representation $a+b\tau$ of $\mathbb{Q}(\tau)$;
- reconstructs every off-diagonal direction from the formulas in `CONSTRUCTION.md`;
- checks nonzeroness, all row/column orthogonality identities, and exact ray classification.

This is the direct implementation of the displayed construction.

### B. Frozen exact certificate

The file

```text
certificate/qls6_card29_exact.json
```

contains all 30 off-diagonal directions after exact reduction into the basis $(1,\tau)$, where

$$
123201\tau^2-202800\tau-93848=0.
$$

The certificate contains rational numerator/denominator pairs only. It is deterministic and human-inspectable.

The bridge

```bash
python generate_exact_certificate.py \
  --check certificate/qls6_card29_exact.json
```

regenerates that file from the construction implementation and requires byte-for-byte agreement.

### C. Small certificate checker

```bash
python verify_certificate.py certificate/qls6_card29_exact.json
```

This is the smallest mathematical trust boundary in the repository.

It intentionally does **not** import `verify_qls6_card29.py` or any construction/generation code. It reads only the frozen exact coordinates and checks:

1. the expected quadratic relation;
2. all 30 directions are nonzero;
3. all 120 row/column pairwise orthogonality equations;
4. all 435 pairwise off-diagonal projective-equivalence decisions;
5. exactly 28 off-diagonal ray classes;
6. the two and only two repeated off-diagonal classes;
7. total cardinality $28+1=29$ after adjoining the common diagonal ray.

The checker uses only Python integer arithmetic and `fractions.Fraction`.

### D. Independent symbolic reconstruction

```bash
python verify_qls6_card29_sympy.py
```

This separately reconstructs the construction with SymPy and performs exact polynomial reduction modulo the defining quadratic.

Its dependency is pinned in `requirements.txt`.

This is independent at the symbolic-arithmetic implementation level, although it intentionally implements the same public construction formulas.

## What is and is not trusted

### Final exact trust boundary

For the frozen-certificate route:

- Python's integer arithmetic and `fractions.Fraction`;
- `verify_certificate.py`;
- the committed exact certificate;
- the elementary implication that five nonzero mutually orthogonal directions in $\mathbb{R}^5$, after normalization, form an orthonormal basis, and that adjoining one orthogonal diagonal direction yields the stated $\mathrm{QLS}(6)$.

The construction search/discovery process is **not** trusted.

### Additional confidence layers

The principal construction verifier and SymPy implementation independently reconstruct the public formulas. The deterministic generator ties those formulas to the frozen certificate. These are additional consistency checks, not hidden assumptions of the small certificate checker.

### Decimal export

`qls6_card29_vectors.json` is for numerical inspection only. It is not read by the exact verification chain and must not be cited as proof.

## Why this release does not claim Lean verification

A proof-assistant formalization was considered as part of the release-hardening audit. The mathematical claim is a finite explicit existence statement whose load-bearing data are 30 exact vectors in a quadratic number field. The repository now exposes those data as a frozen exact certificate and verifies them with a small checker whose logic is substantially narrower than the construction code.

A faithful Lean verification would need to encode the quadratic field, the 30 exact directions, all orthogonality/ray checks, and the final QLS/cardinality reduction. That work has **not** been completed, so the repository makes no Lean-verification claim.

The absence of Lean does not turn sampled or floating-point testing into proof: the public correctness claim rests on exact arithmetic throughout.

## Artifact integrity

`ARTIFACTS.sha256` records SHA-256 hashes for all public proof, manuscript, certificate, verification, metadata, and CI artifacts that form the release.

`verify_release.py` recomputes and checks every listed hash.

The manifest deliberately does not hash itself.

## Markdown rendering check

GitHub renders mathematical Markdown using `$...$`, `$$...$$`, or fenced `math` blocks. The release entry point rejects legacy parenthesized or bracketed TeX math delimiters in committed Markdown files.

This is a presentation check only; it does not affect mathematical validity.

## Review status

Machine verification is complete for the frozen repository artifacts.

Independent specialist review is **pending**. The repository must not change that status without public, auditable evidence tied to the exact artifact under review.
