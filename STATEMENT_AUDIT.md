# R011 statement audit

This file maps each public R011 claim to the human proof and the exact machine checks that support it.

## Trust layers

| Layer | Role | Depends on construction formulas? |
|---|---|---|
| `manuscript/qls6_cardinality_29.pdf` | Human-readable mathematical argument and literature context | Yes |
| `verify_qls6_card29.py` | Exact reconstruction and verification in $\mathbb{Q}(\tau)$ using Python standard library only | Yes |
| `generate_exact_certificate.py` | Deterministic bridge from construction code to the frozen coordinate certificate | Yes |
| `certificate/qls6_card29_exact.json` | Frozen exact coordinates for the 30 off-diagonal directions | No executable logic |
| `verify_certificate.py` | Small data-driven exact checker over the frozen coordinates | **No** |
| `verify_qls6_card29_sympy.py` | Separately written symbolic reconstruction using SymPy polynomial reduction | Yes, independently reimplemented |
| `verify_release.py` | One-command orchestration, metadata/rendering/hash checks | No mathematical logic beyond consistency checks |

The certificate checker is deliberately separated from construction/generation code. It provides a small final trust boundary for the finite existence claim.

## Claim crosswalk

| Public statement | Human proof location | Exact machine obligation |
|---|---|---|
| $\tau$ satisfies $123201\tau^2-202800\tau-93848=0$ and defines a quadratic field | Manuscript §3; `CONSTRUCTION.md` §1 | `verify_qls6_card29.py` checks the discriminant is nonsquare and performs all arithmetic modulo the quadratic relation; `verify_certificate.py` checks the same frozen minimal polynomial |
| There are exactly 30 off-diagonal directions | Manuscript §4 | All three exact verification paths require exactly 30 off-diagonal cells |
| Every off-diagonal direction is nonzero | Manuscript §4-§5 | Principal verifier, certificate verifier, and SymPy verifier all test nonzeroness |
| Every punctured row is an orthogonal basis of $\mathbb{R}^5$ | Manuscript §5 | Exact row dot products in all verification paths |
| Every punctured column is an orthogonal basis of $\mathbb{R}^5$ | Manuscript §5 | Exact column dot products in all verification paths |
| The complete finite orthogonality audit has 120 pairwise checks | Manuscript §7 | Principal verifier, certificate verifier, and SymPy verifier all require exactly 120 |
| Appending the common diagonal vector gives a real $\mathrm{QLS}(6)$ | Manuscript §2 and §5 | Follows from the exact punctured-row/column checks plus the explicit orthogonal sixth-coordinate embedding; the certificate records this embedding convention |
| Pairwise off-diagonal ray equality is tested exhaustively | Manuscript §6 | `verify_certificate.py` performs all $\binom{30}{2}=435$ pairwise projective tests; the other two verifiers compute the same classification |
| Exactly two off-diagonal ray classes repeat | Manuscript §6 | All exact verifiers require `[(0,1),(2,3)]` and `[(3,4),(5,0)]` as the only repeated classes |
| The off-diagonal cells determine 28 rays | Manuscript §6 | All exact verifiers require exactly 28 off-diagonal classes |
| The full QLS has cardinality 29 | Manuscript Theorem 1 / §6 | 28 off-diagonal classes + one common diagonal ray; frozen in `claim.json` and checked by `verify_release.py` |
| The decimal JSON is not part of the proof trust boundary | Manuscript verification section; README | No exact verifier reads `qls6_card29_vectors.json` |
| R011 makes no priority claim | Manuscript introduction/related work; `SOURCE_AUDIT.md` | Literature/provenance claim, not a machine theorem; `claim.json` freezes the non-claim |
| Independent specialist review is pending | README / `claim.json` | `verify_release.py` requires `review_status` to remain `pending` unless the metadata is intentionally revised with public evidence |

## Statement identity rule

The canonical theorem statement is:

> There exists a real quantum Latin square of order 6 with cardinality 29.

Any stronger public wording must be justified separately. In particular, the following are **not** theorem-equivalent and must not be substituted without new evidence:

- "the first cardinality-29 QLS(6)";
- "the unique cardinality-29 QLS(6)";
- "an optimal cardinality-29 construction";
- "Lean-verified cardinality 29";
- "independently specialist-verified";
- "the result that first closed the order-six spectrum."

## Formalization boundary

R011 does not currently claim Lean verification. The finite theorem has instead been reduced to a frozen exact coordinate certificate checked by a small standard-library program, with a separate construction verifier and independent SymPy reconstruction.

A future proof-assistant development would only strengthen the public claim if it faithfully connected the exact certificate or construction formulas to the same theorem statement. A partial formalization of generic QLS definitions alone must not be presented as formal verification of R011.
