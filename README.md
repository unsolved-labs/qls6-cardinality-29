# Order-six quantum Latin square of cardinality 29

This repository is the canonical artifact for Unsolved Labs release **R011**.

## Result

There exists a **real quantum Latin square of order 6 with cardinality 29**.

The construction is defined over the quadratic field $\mathbb{Q}(\tau)$, where $\tau$ is the positive root of

$$
123201\tau^2-202800\tau-93848=0.
$$

Thirty nonzero off-diagonal directions are constructed in $\mathbb{R}^5$. After normalization they are embedded in $\mathbb{R}^6$ with zero sixth coordinate, while the same orthogonal unit vector is placed in all six diagonal cells. Exact arithmetic proves that every row and column is an orthonormal basis and that the 36 cells determine exactly 29 rays modulo global phase.

- **Manuscript:** [`manuscript/qls6_cardinality_29.pdf`](manuscript/qls6_cardinality_29.pdf)
- **LaTeX source:** [`manuscript/qls6_cardinality_29.tex`](manuscript/qls6_cardinality_29.tex)
- **Construction notes:** [`CONSTRUCTION.md`](CONSTRUCTION.md)
- **Statement crosswalk:** [`STATEMENT_AUDIT.md`](STATEMENT_AUDIT.md)
- **Verification contract:** [`VERIFICATION.md`](VERIFICATION.md)
- **Literature/provenance audit:** [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md)

## Current literature boundary

The historical comparison used when this artifact was assembled was Zhipeng Xu, arXiv:2607.11800v3 (revised 2026-08-04), whose then-current order-six spectrum left cardinality 29 unresolved.

That is no longer the current literature state. Aishwarya P. Das and Durgesh Kumar posted *A Quantum Latin Square of Order Six with Cardinality 29*, arXiv:2608.12607, on 2026-08-12, giving another explicit real cardinality-29 construction and closing the remaining order-six spectrum gap.

Accordingly, **R011 makes no priority claim for resolving cardinality 29**. Its public claim is the correctness of the explicit construction and exact verification contained in this repository. See [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md).

## Exact verification

The release has three complementary verification layers.

### 1. Construction verifier

Standard-library exact arithmetic in $\mathbb{Q}(\tau)$:

```bash
python verify_qls6_card29.py
```

This reconstructs the directions from the formulas in the construction and checks the complete finite claim.

### 2. Frozen-certificate verifier

A deterministic exact certificate contains the 30 off-diagonal directions as coordinates $a+b\tau$ with rational $a,b$:

```bash
python verify_certificate.py certificate/qls6_card29_exact.json
```

This checker intentionally **does not import the construction code**. It checks the frozen coordinate certificate directly using only Python integer arithmetic and `fractions.Fraction`.

The committed certificate is also regenerated from the construction and compared byte-for-byte:

```bash
python generate_exact_certificate.py \
  --check certificate/qls6_card29_exact.json
```

### 3. Independent symbolic reimplementation

A separately written SymPy implementation reconstructs the construction and reduces identities modulo the defining polynomial:

```bash
python -m pip install -r requirements.txt
python verify_qls6_card29_sympy.py
```

### One-command release check

```bash
python -m pip install -r requirements.txt
python verify_release.py
```

The release check verifies claim metadata, GitHub math syntax, the committed manuscript PDF signature, all exact construction/certificate checks, the independent SymPy replay, and the SHA-256 artifact manifest.

## What is checked

The exact verifiers establish:

- all 30 off-diagonal directions are nonzero;
- all 120 within-row and within-column pairwise orthogonality equations vanish;
- all $\binom{30}{2}=435$ off-diagonal projective-equivalence decisions;
- exactly two repeated off-diagonal ray classes:
  - $(0,1)\sim(2,3)$;
  - $(3,4)\sim(5,0)$;
- therefore the off-diagonal cells determine 28 rays;
- the common diagonal direction contributes one additional ray;
- hence the total cardinality is exactly 29.

`qls6_card29_vectors.json` is a decimal export for numerical inspection. It is **not** part of the exact trust boundary.

## Scope and non-claims

This repository proves existence of one explicit real $\mathrm{QLS}(6)$ of cardinality 29.

It does **not** claim:

- priority for first resolving cardinality 29;
- uniqueness or classification of cardinality-29 examples;
- optimality or simplicity of this algebraic representation;
- Lean or other proof-assistant verification;
- independent specialist review.

Independent specialist review remains **pending**.

## Repository structure

- `CLAIM.md` / `claim.json` - human- and machine-readable frozen claim.
- `CONSTRUCTION.md` - exact construction and proof outline in GitHub-renderable Markdown.
- `manuscript/` - paper-quality LaTeX manuscript, bibliography, PDF, and build instructions.
- `certificate/qls6_card29_exact.json` - frozen exact coordinate certificate.
- `verify_qls6_card29.py` - exact construction verifier using the Python standard library.
- `generate_exact_certificate.py` - deterministic construction-to-certificate bridge.
- `verify_certificate.py` - small data-driven exact certificate checker.
- `verify_qls6_card29_sympy.py` - independent SymPy reconstruction.
- `STATEMENT_AUDIT.md` - public claim to proof/checker mapping.
- `VERIFICATION.md` - reproduction instructions and trust boundary.
- `SOURCE_AUDIT.md` - frozen and current literature context.
- `ARTIFACTS.sha256` - integrity manifest.
- `.github/workflows/verify.yml` - clean-checkout CI.

## Research provenance

R011 is a public Unsolved Labs research artifact produced in a frontier-AI research workflow. Correctness is not inferred from that provenance; it is supported by the explicit proof manuscript and exact machine-verification layers above. No conventional human-authorship claim is implied by the repository metadata.
