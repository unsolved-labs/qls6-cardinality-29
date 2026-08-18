# R011 frozen claim

## Claim

There exists a real quantum Latin square of order 6 with cardinality 29.

More explicitly, the repository gives a $6\times6$ array $\Phi=(\phi_{ij})$ of unit vectors in $\mathbb{R}^6\subset\mathbb{C}^6$ such that:

1. every row of $\Phi$ is an orthonormal basis of $\mathbb{R}^6$;
2. every column of $\Phi$ is an orthonormal basis of $\mathbb{R}^6$;
3. after identifying vectors that differ by a nonzero complex phase, the 36 cells represent exactly 29 rays.

The construction uses the positive real root $\tau$ of

$$
123201\tau^2-202800\tau-93848=0.
$$

The off-diagonal cells are normalized nonzero directions in $\mathbb{R}^5$ embedded into the first five coordinates of $\mathbb{R}^6$; all diagonal cells use one common orthogonal unit vector.

## Exact finite consequences checked by the release

- 30 nonzero off-diagonal directions;
- 120 row/column pairwise orthogonality identities;
- 435 off-diagonal pairwise ray-equivalence decisions;
- 28 off-diagonal ray classes;
- exactly two repeated off-diagonal classes:
  - $(0,1)\sim(2,3)$;
  - $(3,4)\sim(5,0)$;
- 29 total ray classes after adding the common diagonal ray.

## Provenance and priority boundary

The displayed R011 construction was independently obtained in the Unsolved Labs frontier-AI research workflow. A separate cardinality-29 construction by Das and Kumar was publicly posted on arXiv on 2026-08-12, before R011's surviving public Git history begins on 2026-08-14.

Accordingly, independence of discovery is recorded, while no claim of first public disclosure is made. See [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md).

## Non-claims

R011 does not claim:

- first public disclosure of a cardinality-29 construction;
- uniqueness or classification;
- optimality of the coordinates or construction method;
- Lean/proof-assistant verification;
- that the decimal vector export is an exact proof artifact;
- completed independent specialist review.
