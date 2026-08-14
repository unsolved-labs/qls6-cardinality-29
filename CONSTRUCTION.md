# An exact real quantum Latin square of order six and cardinality 29

**Status:** exact construction with public arithmetic verification. Independent specialist review is pending.

## 1. Statement

Let

\[
P(T)=123201T^2-202800T-93848
\]

and let

\[
\tau=\frac{2600+2\sqrt{3590422}}{3159}
      =2.0226912886470269906\ldots
\]

be the positive root of \(P\). The construction below gives 30 nonzero ray directions in \(\mathbb R^5\). Normalize each direction, append a sixth coordinate equal to zero, and put

\[
f=(0,0,0,0,0,1)^\mathsf T
\]

in all six diagonal cells. The resulting \(6\times6\) array is a quantum Latin square in \(\mathbb R^6\subset\mathbb C^6\) with cardinality 29.

## 2. Building blocks

Let \(e_0,\ldots,e_4\) be the standard orthonormal basis of \(\mathbb R^5\). Define

\[
 a=\frac{4e_3+3e_4}{5},\qquad
 p=\frac{-3e_3+4e_4}{5},
\]

\[
 d=\frac{5e_1-12e_2}{13},\qquad
 t=\frac{12e_1+5e_2}{13},
\]

and

\[
 q=\frac{8t+15e_4}{17},\qquad
 r=\frac{15t-8e_4}{17}.
\]

Split \(q=X+H\) by setting

\[
 X=\frac{96}{221}e_1+\frac{12}{17}p,
 \qquad
 H=\frac{40}{221}e_2+\frac9{17}a,
\]

and introduce their orthogonal companions

\[
 Y=\frac{12}{17}e_1-\frac{96}{221}p,
 \qquad
 U=\frac9{17}e_2-\frac{40}{221}a.
\]

Then

\[
\sigma=\langle X,X\rangle=\frac{33552}{48841},
\qquad
\rho=\langle H,H\rangle=\frac{15289}{48841},
\qquad \sigma+\rho=1.
\]

Define

\[
 S=\rho X-\sigma H,
\]

\[
 W=32e_0-51q,\qquad Z=51e_0+32q,
\]

and

\[
 B=51\rho e_0+32H,\qquad C=32e_0-51H.
\]

Next put

\[
 T_1=4e_0-3t,\qquad T_2=d+\tau e_3.
\]

The three vectors \(e_4,T_1,T_2\) are mutually orthogonal, with squared norms \(1,25,1+\tau^2\). Let

\[
 G=X-\langle X,e_4\rangle e_4
   -\frac{\langle X,T_1\rangle}{25}T_1
   -\frac{\langle X,T_2\rangle}{1+\tau^2}T_2.
\]

Thus \(G\) is the orthogonal projection of \(X\) onto
\(\operatorname{span}(e_4,T_1,T_2)^\perp\).

Define the additional direction

\[
 K=(600\tau+1521)e_0+1872e_1+(2080\tau+780)e_2+1920e_3.
\]

It satisfies, identically in \(\tau\),

\[
K\perp e_4,T_1,T_2,X.
\]

Finally, let

\[
g_U=\langle G,U\rangle,\qquad g_Y=\langle G,Y\rangle,
\]

\[
L=g_UY-g_YU,
\]

and

\[
M=g_Y\rho Y+g_U\sigma U.
\]

For four vectors \(v_1,\ldots,v_4\in\mathbb R^5\), write
\(\operatorname{cr}(v_1,v_2,v_3,v_4)\) for their generalized cross product: its \(j\)-th coordinate is \((-1)^j\) times the determinant obtained by deleting column \(j\) from the \(4\times5\) matrix with rows \(v_i^\mathsf T\). Set

\[
N_3=\operatorname{cr}(L,B,W,G),
\qquad
N_4=\operatorname{cr}(M,C,X,K).
\]

All the displayed directions are nonzero at the chosen root \(\tau\).

## 3. The array of ray directions

Use the following \(5\)-dimensional directions off the diagonal:

\[
V=\begin{pmatrix}
- & e_0 & e_1 & e_2 & e_3 & e_4\\
3e_0+4t & - & -p & a & d & T_1\\
\tau d-e_3 & q & - & e_0 & r & T_2\\
N_3 & L & B & - & W & G\\
N_4 & M & C & X & - & K\\
W & S & U & Y & Z & -
\end{pmatrix}.
\]

For \(i\ne j\), let

\[
\phi_{ij}=\frac{(V_{ij},0)}{\|V_{ij}\|}\in\mathbb R^6,
\]

and let \(\phi_{ii}=f\).

## 4. Why the quantum Latin conditions hold

The rational rotations make rows 0, 1 and 2 orthogonal immediately. The decomposition

\[
q=X+H,
\]

with \(X,Y\) orthogonal and of squared norm \(\sigma\), and \(H,U\) orthogonal and of squared norm \(\rho\), gives the orthogonality of row 5 and columns 1--4.

Column 5 consists of the directions

\[
e_4,\ T_1,\ T_2,\ G,\ K.
\]

By construction, \(G\perp e_4,T_1,T_2\), while \(K\perp e_4,T_1,T_2,X\). Since \(G\) is the projection of \(X\) onto their common orthogonal complement, \(K\perp G\).

The only nontrivial scalar closure in row 3 reduces to

\[
\langle B,G\rangle
=\frac{4608\,P(\tau)}{206353225(1+\tau^2)}=0.
\]

The corresponding row-4 closure reduces to

\[
\langle M,K\rangle
=-\frac{154607616(200\tau+507)P(\tau)}
 {171334463657825(1+\tau^2)}=0.
\]

The remaining row-3 and row-4 products vanish from the definitions of \(L,M,N_3,N_4\) and the mutually orthogonal subspaces above. Thus all six rows are orthogonal after normalization, and columns 1 through 5 are orthogonal after normalization.

Column 0 then follows either by direct exact calculation or by the frame identity. Summing the rank-one projectors over all six rows gives \(6I_5\). Columns 1 through 5 contribute \(5I_5\), so the five normalized vectors in column 0 have frame operator \(I_5\) and hence form an orthonormal basis.

Appending the common diagonal vector \(f\) completes every row and column to an orthonormal basis of \(\mathbb R^6\).

## 5. Cardinality certificate

Exact proportionality testing in \(\mathbb Q(\tau)\), using all \(2\times2\) minors for every pair of off-diagonal directions, finds exactly two repeated classes:

\[
V_{01}\sim V_{23},\qquad V_{34}\sim V_{50}.
\]

Here the first equality is literally \(e_0=e_0\), and the second is literally \(W=W\). No other pair is proportional. The phase-class matrix is

\[
\begin{pmatrix}
D&0&1&2&3&4\\
5&D&6&7&8&9\\
10&11&D&0&12&13\\
14&15&16&D&17&18\\
19&20&21&22&D&23\\
17&24&25&26&27&D
\end{pmatrix},
\]

where \(D\) denotes the common diagonal ray. Therefore the 30 off-diagonal cells give 28 ray classes, and the diagonal contributes one more:

\[
\operatorname{card}(\Phi)=28+1=29.
\]

## 6. Exact verification

Run

```bash
python verify_qls6_card29.py
```

The verifier uses only `fractions.Fraction` and a two-coordinate implementation of the quadratic field \(\mathbb Q(\tau)\). It checks:

- irreducibility of the defining quadratic;
- nonzeroness of all 30 directions;
- all 120 within-row and within-column orthogonality equations;
- all 435 off-diagonal pairwise proportionality decisions;
- the two repeated classes and total cardinality 29.

The JSON file supplies normalized decimal vectors for independent numerical replay; it is not the source of mathematical validity.
