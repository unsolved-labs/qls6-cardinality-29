# Exact construction for R011

This document gives the exact algebraic construction behind Unsolved Labs release **R011**. For a paper-style presentation, context, and references, see [`manuscript/qls6_cardinality_29.pdf`](manuscript/qls6_cardinality_29.pdf).

The public claim is existence of one real quantum Latin square of order six with cardinality 29. No priority, uniqueness, classification, or coordinate-optimality claim is made.

## 1. Parameter and diagonal extension

Let

$$
P(T)=123201T^2-202800T-93848
$$

and let

$$
\tau=\frac{2600+2\sqrt{3590422}}{3159}
      =2.0226912886470269906\ldots
$$

be the positive root of $P$.

We construct 30 nonzero ray directions in $\mathbb{R}^5$. For each off-diagonal cell $(i,j)$, normalize its direction $V_{ij}$ and set

$$
\phi_{ij}=\frac{(V_{ij},0)}{\lVert V_{ij}\rVert}\in\mathbb{R}^6.
$$

On every diagonal cell put

$$
f=(0,0,0,0,0,1)^{\mathsf T}.
$$

Thus it is enough to prove that every punctured row and column of $V$ is an orthogonal basis of $\mathbb{R}^5$ and that the 30 off-diagonal cells determine exactly 28 rays.

## 2. Rational rotations

Let $e_0,\ldots,e_4$ be the standard orthonormal basis of $\mathbb{R}^5$. Define

$$
a=\frac{4e_3+3e_4}{5},
\qquad
p=\frac{-3e_3+4e_4}{5},
$$

$$
d=\frac{5e_1-12e_2}{13},
\qquad
t=\frac{12e_1+5e_2}{13},
$$

and

$$
q=\frac{8t+15e_4}{17},
\qquad
r=\frac{15t-8e_4}{17}.
$$

Split $q=X+H$ by

$$
X=\frac{96}{221}e_1+\frac{12}{17}p,
\qquad
H=\frac{40}{221}e_2+\frac{9}{17}a,
$$

and introduce orthogonal companion directions

$$
Y=\frac{12}{17}e_1-\frac{96}{221}p,
\qquad
U=\frac{9}{17}e_2-\frac{40}{221}a.
$$

Then

$$
\sigma=\langle X,X\rangle=\frac{33552}{48841},
\qquad
\rho=\langle H,H\rangle=\frac{15289}{48841},
\qquad
\sigma+\rho=1.
$$

Put

$$
S=\rho X-\sigma H,
$$

$$
W=32e_0-51q,
\qquad
Z=51e_0+32q,
$$

and

$$
B=51\rho e_0+32H,
\qquad
C=32e_0-51H.
$$

## 3. The quadratic compatibility block

Define

$$
T_1=4e_0-3t,
\qquad
T_2=d+\tau e_3.
$$

The vectors $e_4,T_1,T_2$ are mutually orthogonal, with squared norms $1$, $25$, and $1+\tau^2$. Let

$$
G=X-\langle X,e_4\rangle e_4
  -\frac{\langle X,T_1\rangle}{25}T_1
  -\frac{\langle X,T_2\rangle}{1+\tau^2}T_2.
$$

Thus $G$ is the orthogonal projection of $X$ onto
$\operatorname{span}(e_4,T_1,T_2)^\perp$.

Define

$$
K=(600\tau+1521)e_0
  +1872e_1
  +(2080\tau+780)e_2
  +1920e_3.
$$

Exact reduction modulo $P(\tau)=0$ gives

$$
K\perp e_4,\quad K\perp T_1,\quad K\perp T_2,\quad K\perp X.
$$

Since $G$ is the projection of $X$ onto the common orthogonal complement of $e_4,T_1,T_2$, it follows that $K\perp G$.

Set

$$
g_U=\langle G,U\rangle,
\qquad
g_Y=\langle G,Y\rangle,
$$

$$
L=g_UY-g_YU,
$$

and

$$
M=g_Y\rho Y+g_U\sigma U.
$$

For four vectors $v_1,\ldots,v_4\in\mathbb{R}^5$, let
$\operatorname{cr}(v_1,v_2,v_3,v_4)$ denote the five-dimensional generalized cross product whose $j$-th coordinate is $(-1)^j$ times the determinant obtained by deleting column $j$ from the $4\times5$ matrix with rows $v_i^{\mathsf T}$. Define

$$
N_3=\operatorname{cr}(L,B,W,G),
\qquad
N_4=\operatorname{cr}(M,C,X,K).
$$

All displayed directions are nonzero in $\mathbb{Q}(\tau)^5$.

## 4. Off-diagonal array

The punctured array of directions is

$$
V=
\begin{pmatrix}
- & e_0 & e_1 & e_2 & e_3 & e_4\\
3e_0+4t & - & -p & a & d & T_1\\
\tau d-e_3 & q & - & e_0 & r & T_2\\
N_3 & L & B & - & W & G\\
N_4 & M & C & X & - & K\\
W & S & U & Y & Z & -
\end{pmatrix}.
$$

The committed exact certificate
[`certificate/qls6_card29_exact.json`](certificate/qls6_card29_exact.json)
stores these 30 directions after exact reduction into the basis $(1,\tau)$ of $\mathbb{Q}(\tau)$.

## 5. Orthogonality argument

The rational rotations immediately give orthogonality of rows 0, 1, and 2. The decomposition

$$
q=X+H
$$

together with the orthogonal pairs $(X,Y)$ and $(H,U)$ gives the orthogonality relations needed for row 5 and columns 1 through 4.

Column 5 consists of

$$
e_4,\ T_1,\ T_2,\ G,\ K.
$$

By construction $G\perp e_4,T_1,T_2$, while $K\perp e_4,T_1,T_2,X$ and hence $K\perp G$.

The remaining scalar closures are exactly where the defining quadratic is used. In row 3,

$$
\langle B,G\rangle
=
\frac{4608\,P(\tau)}
     {206353225(1+\tau^2)}
=0.
$$

In row 4,

$$
\langle M,K\rangle
=
-\frac{154607616(200\tau+507)P(\tau)}
       {171334463657825(1+\tau^2)}
=0.
$$

The definitions of $L,M,N_3,N_4$ force the remaining row-3 and row-4 products to vanish.

A convenient way to recover column 0 is the frame identity. The five normalized off-diagonal vectors in each row form an orthonormal basis of $\mathbb{R}^5$, so summing their rank-one projectors over all six rows gives $6I_5$. Columns 1 through 5 contribute $5I_5$. Therefore column 0 has frame operator $I_5$; because it contains five vectors in dimension five, it is an orthonormal basis.

The machine verifiers do not rely on this shortcut: they check all 120 pairwise row/column orthogonality equations exactly.

Appending the common diagonal vector $f$ completes every row and column to an orthonormal basis of $\mathbb{R}^6$.

## 6. Cardinality certificate

Exact projective equality over $\mathbb{Q}(\tau)$ is tested by all $2\times2$ minors for every pair of off-diagonal directions. There are

$$
\binom{30}{2}=435
$$

such pairwise decisions.

Exactly two off-diagonal ray classes repeat:

$$
V_{01}\sim V_{23},
\qquad
V_{34}\sim V_{50}.
$$

The first repetition is literally $e_0=e_0$ and the second is literally $W=W$. No other off-diagonal pair is proportional.

A phase-class labeling is

$$
\begin{pmatrix}
D&0&1&2&3&4\\
5&D&6&7&8&9\\
10&11&D&0&12&13\\
14&15&16&D&17&18\\
19&20&21&22&D&23\\
17&24&25&26&27&D
\end{pmatrix},
$$

where $D$ denotes the common diagonal ray. Hence the 30 off-diagonal cells determine 28 rays and the diagonal contributes one additional ray:

$$
\operatorname{card}(\Phi)=28+1=29.
$$

## 7. Exact verification

For the construction-level exact replay:

```bash
python verify_qls6_card29.py
```

For the small data-driven certificate checker:

```bash
python verify_certificate.py certificate/qls6_card29_exact.json
```

For the independently written symbolic reconstruction:

```bash
python -m pip install -r requirements.txt
python verify_qls6_card29_sympy.py
```

For the complete release contract:

```bash
python -m pip install -r requirements.txt
python verify_release.py
```

See [`VERIFICATION.md`](VERIFICATION.md) for the trust boundary and [`STATEMENT_AUDIT.md`](STATEMENT_AUDIT.md) for the claim-to-checker crosswalk.
