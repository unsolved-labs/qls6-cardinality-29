# R011 source, literature, independence, and novelty audit

This file records the public literature and provenance boundary used by Unsolved Labs release **R011**. It distinguishes three separate questions: correctness of the explicit construction, independence of the discovery process, and priority of public disclosure.

## 1. Foundational definition

Quantum Latin squares were introduced by Benjamin Musto and Jamie Vicary:

- Benjamin Musto and Jamie Vicary, *Quantum Latin squares and unitary error bases*, Quantum Information and Computation 16 (2016), 1318-1332.
- DOI: https://doi.org/10.26421/QIC16.15-16-4
- arXiv: https://arxiv.org/abs/1504.02715

R011 uses the standard definition: an order-$n$ quantum Latin square is an $n\times n$ array of unit vectors in $\mathbb{C}^n$ whose rows and columns are orthonormal bases. Cardinality counts rays after identifying global phase.

## 2. Historical order-six snapshot used during construction

The research workflow was originally framed against:

- Zhipeng Xu, *New Cardinalities for Quantum Latin Squares of Order Six*, arXiv:2607.11800v3, revised 2026-08-04.
- https://arxiv.org/abs/2607.11800v3

At that revision, the public order-six spectrum described cardinality 29 as the remaining unresolved value after the other reported constructions.

This remains useful historical context, but it is **not** an accurate description of the literature after 2026-08-12.

## 3. Public-disclosure chronology

On 2026-08-12, Aishwarya P. Das and Durgesh Kumar submitted:

- Aishwarya P. Das and Durgesh Kumar, *A Quantum Latin Square of Order Six with Cardinality 29*, arXiv:2608.12607.
- https://arxiv.org/abs/2608.12607

That paper proves existence of a real order-six quantum Latin square of cardinality 29 and states the resulting completion of the order-six cardinality spectrum.

The surviving public Git history for R011 begins on 2026-08-14:

- GitHub Pages reservation commit `a89a1bb9f41599eba72bab0d9b3c22276b7cf5bb`, with `reservedAt` 2026-08-14T06:48:00Z;
- GitHub Pages publication commit `32ce6437945cc6726e80c268727f9176cd163f34`, whose release manifest records `publishedAt` 2026-08-14T07:20:45Z;
- canonical repository initial commit `0b89294355f35236bb994f909acf194429f8c6cf`, also on 2026-08-14.

Therefore R011 **does not claim first public disclosure** of a cardinality-29 construction or first public closure of the order-six spectrum.

## 4. Independence and relationship of the constructions

R011 was **independently obtained** in the Unsolved Labs frontier-AI research workflow rather than derived from the Das-Kumar construction.

The public formulas are also materially different. R011 is organized around the quadratic parameter $\tau$ satisfying

$$
123201\tau^2-202800\tau-93848=0,
$$

together with its own rational rotations, orthogonal projection, generalized cross products, compatibility identities, and exact ray-class certificate.

The Das-Kumar arXiv construction uses a different punctured-array parameterization based on rational unit-circle parameters and orthogonal changes of basis.

Both constructions use the natural high-level reduction of placing a common diagonal ray and solving a punctured $6\times6$ orthogonality problem in $\mathbb{R}^5$. Shared use of that reduction does not make the explicit constructions identical.

**Independence of discovery and priority of public disclosure are separate claims.** R011 records the former and does not claim the latter.

## 5. Current claim boundary

The defensible public R011 claim is:

> R011 is an independently obtained explicit real $\mathrm{QLS}(6)$ of cardinality 29, accompanied by exact machine-verification artifacts proving that the displayed construction has the claimed row/column orthogonality and ray count.

The repository does not claim:

- first public disclosure of cardinality 29;
- first public closure of the order-six spectrum;
- uniqueness or classification;
- a simpler construction than other public examples;
- any result about all cardinality-29 QLS constructions.

## 6. Re-audit rule

Because this is an active 2026 literature area, any future release or manuscript revision should re-check the cited arXiv records and related order-six spectrum papers before making novelty, priority, or "best known" statements. Correctness of the frozen construction and the recorded independence of its research provenance are separate from publication priority.
