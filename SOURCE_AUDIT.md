# R011 source, literature, and novelty audit

This file records the public literature boundary used by Unsolved Labs release **R011**. It is intentionally conservative: it distinguishes the correctness of the explicit construction from historical priority.

## 1. Foundational definition

Quantum Latin squares were introduced by Benjamin Musto and Jamie Vicary:

- Benjamin Musto and Jamie Vicary, *Quantum Latin squares and unitary error bases*, Quantum Information and Computation 16 (2016), 1318-1332.
- DOI: https://doi.org/10.26421/QIC16.15-16-4
- arXiv: https://arxiv.org/abs/1504.02715

R011 uses the standard definition: an order-$n$ quantum Latin square is an $n\times n$ array of unit vectors in $\mathbb{C}^n$ whose rows and columns are orthonormal bases. Cardinality counts rays after identifying global phase.

## 2. Historical order-six snapshot used during construction

The repository was originally framed against:

- Zhipeng Xu, *New Cardinalities for Quantum Latin Squares of Order Six*, arXiv:2607.11800v3, revised 2026-08-04.
- https://arxiv.org/abs/2607.11800v3

At that revision, the public order-six spectrum described cardinality 29 as the remaining unresolved value after the other reported constructions.

This remains useful historical context, but it is **not** an accurate description of the literature after 2026-08-12.

## 3. Current parallel cardinality-29 result

On 2026-08-12, Aishwarya P. Das and Durgesh Kumar submitted:

- Aishwarya P. Das and Durgesh Kumar, *A Quantum Latin Square of Order Six with Cardinality 29*, arXiv:2608.12607.
- https://arxiv.org/abs/2608.12607

That paper proves existence of a real order-six quantum Latin square of cardinality 29 and states the resulting completion of the order-six cardinality spectrum.

The R011 GitHub repository was initialized on 2026-08-14:

- initial commit: `0b89294355f35236bb994f909acf194429f8c6cf`
- https://github.com/unsolved-labs/qls6-cardinality-29/commit/0b89294355f35236bb994f909acf194429f8c6cf

Therefore R011 **does not claim priority** for first resolving the cardinality-29 existence problem.

## 4. Relationship of the public constructions

The R011 construction in this repository is presented through a quadratic parameter $\tau$ satisfying

$$
123201\tau^2-202800\tau-93848=0,
$$

together with rational rotations, orthogonal projection, and generalized cross products.

The Das-Kumar arXiv construction is presented through a different punctured-array parameterization based on rational unit-circle parameters and orthogonal changes of basis.

This observation concerns the public formulas only. It is **not** a claim about discovery chronology, independence of research process, or priority.

## 5. Current claim boundary

The defensible public R011 claim is:

> The repository contains an explicit real $\mathrm{QLS}(6)$ of cardinality 29 and exact machine-verification artifacts proving that the displayed construction has the claimed row/column orthogonality and ray count.

The repository does not claim:

- first discovery of cardinality 29;
- first closure of the order-six spectrum;
- uniqueness or classification;
- a simpler construction than other public examples;
- any result about all cardinality-29 QLS constructions.

## 6. Re-audit rule

Because this is an active 2026 literature area, any future release or manuscript revision should re-check the cited arXiv records and related order-six spectrum papers before making novelty or "best known" statements. Correctness of the frozen construction is independent of that literature status.
