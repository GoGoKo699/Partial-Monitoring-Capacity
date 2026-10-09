# Exact product-helper capacity: photon counting is optimal

Photon counting attains the capacity optimized over every predetermined product helper POVM and every input in the stated qubit family. The [product-channel reduction](PRODUCT_HELPER_GAP_2026-10-07.md) covers arbitrary endpoint block codes; the separate [unrestricted theorem](THEOREM.md) supplies the collective comparison.

## Result and physical meaning

For the splitting isometry in [THEOREM](THEOREM.md), let $a+b+c=1$, $a>b>0$ and $c>0$. The product benchmark allows every single-use helper POVM, with the measurements chosen in advance and permitted to vary across uses. Sender and receiver may still use arbitrary block codes. There is no sender feedback or postselection. Then

```math
\boxed{Q_{\rm prod}=Q_{\rm count}=\max_{0\le q\le1}F(q),}
```

where

```math
F(q)=(1-cq)\left[
h_2\!\left(\frac{aq}{1-cq}\right)
-h_2\!\left(\frac{bq}{1-cq}\right)\right].
```

Photon counting in the helper's vacuum/excitation basis attains this value with a diagonal average input. No other predetermined product POVM improves it, even when paired with coherent input states and collective encoding/decoding. The theorem concerns the same qubit family; it does not extend to the optical model.

Throughout this interior region, $`0<Q_{\rm prod}<Q_{\rm meas}`$ by the
[strict-gap corollary](#4-strict-collective-advantage-throughout-the-qubit-interior).
For $`(a,b,c)=(1/5,2/25,18/25)`$, the exact-arithmetic certificate described below gives

```math
0.18621044456570<Q_{\rm prod}<0.18621044456572,
```

```math
0.11949909857428<Q_{\rm meas}-Q_{\rm prod}<0.11949909857432.
```

Thus unrestricted helper processing permits about 64% more asymptotic quantum transmission than the best predetermined product measurement in this example. These are capacities per original use, not single-photon recovery probabilities. Outcome-adaptive local strategies, general separable block POVMs and the implementation cost of a collective helper remain outside the comparison.

## 1. Reduce every branch to one scalar

The [product-helper proof](PRODUCT_HELPER_GAP_2026-10-07.md), Section 1, establishes

```math
Q_{\rm prod}=\sup_{\rho,M}\sum_xp_x[S(B_x)-S(E_x)].
```

Rank-one refinement can only help; every refined measured channel is degradable. Product-channel additivity covers use-varying measurements and arbitrary correlated inputs. The reduction also covers continuous records; [PROOF_DEPENDENCIES, Section 2](PROOF_DEPENDENCIES.md) states the finite trace-measure formulation and finite total-correlation argument explicitly. The following bound holds for every input/measurement pair and is attained by a two-outcome measurement.

Write

```math
\rho=\begin{pmatrix}1-q&z\\z^*&q\end{pmatrix},\qquad
d=\det\rho=q(1-q)-|z|^2\ge0.
```

The case $q=0$ has zero coherent information. For $q>0$ and a nonzero helper row $m_x=(u_x,v_x)$, put $r_x=|u_x|^2/p_x$. Direct expansion of the conditional $2\times2$ matrices gives

```math
\det B_x=a r_x^2(d+bq^2),\qquad
\det E_x=b r_x^2(d+aq^2).
```

The input-coherence terms cancel in these determinants except through $d$. The helper marginal is

```math
\rho_D=\begin{pmatrix}1-cq&\sqrt c\,z\\\sqrt c\,z^*&cq\end{pmatrix},
\qquad \det\rho_D=c[d+(a+b)q^2]>0.
```

The Rayleigh quotient for $|u_x|^2/(m_x\rho_Dm_x^\dagger)$ and POVM completeness imply

```math
0\le r_x\le R=(\rho_D^{-1})_{00}
=\frac q{d+(a+b)q^2},\qquad
\sum_xp_xr_x=\sum_x|u_x|^2=1.
```

Define the qubit entropy function

```math
e(C)=h_2\!\left(\frac{1+\sqrt{1-C^2}}2\right),\qquad
\alpha=2\sqrt{a(d+bq^2)},\quad
\beta=2\sqrt{b(d+aq^2)}.
```

Since the entropy of a qubit state is $e(2\sqrt{\det\rho})$, each branch contributes $f(r_x)=e(\alpha r_x)-e(\beta r_x)$. Here $\alpha\ge\beta$ because $\alpha^2-\beta^2=4(a-b)d\ge0$.

## 2. The entropy difference is convex

Ordinary convexity of $e$ does not justify subtracting two copies of it. The stronger fact needed here follows directly by differentiation. For $0<C<1$,

```math
e''(C)=\frac1{\ln2}\int_0^1
\frac{t^2\,dt}{1-t^2+C^2t^2}.
```

Consequently, on the common physical interval,

```math
f''(r)=\frac{\alpha^2-\beta^2}{\ln2}
\int_0^1\frac{t^2(1-t^2)\,dt}
{(1-t^2+\alpha^2r^2t^2)(1-t^2+\beta^2r^2t^2)}\ge0.
```

The endpoints follow by continuity. To check the domain explicitly, let $\eta=d/q^2$. Then

```math
\alpha R=\frac{2\sqrt{a(\eta+b)}}{\eta+a+b}\le1,
\qquad
\beta R=\frac{2\sqrt{b(\eta+a)}}{\eta+a+b}\le1.
```

For the first inequality the difference of the squared denominator and numerator is $(\eta+b-a)^2$; for the second it is $(\eta+a-b)^2$. Thus $f$ is convex throughout $[0,R]$, with $f(0)=0$. Its chord bounds every branch:

```math
\sum_xp_xf(r_x)\le\sum_xp_x\frac{r_x}{R}f(R)
=\frac{f(R)}R.
```

This uses only completeness and the scalar range; it applies to arbitrary finite or continuous POVMs.

## 3. The chord is bounded by counting with another diagonal input

Set $\widetilde q=1/(1+\eta)$. Since $d\le q(1-q)$, one has $q\le\widetilde q\le1$. At the chord endpoint,

```math
\frac{f(R)}R
=q(\eta+a+b)\left[
h_2\!\left(\frac a{\eta+a+b}\right)
-h_2\!\left(\frac b{\eta+a+b}\right)\right]
=\frac q{\widetilde q}F(\widetilde q).
```

For $a>b$, $F$ is nonnegative: it is the coherent information of a degradable counting channel, concave in the diagonal input and zero at both pure endpoints. Equivalently, $e$ is increasing and the determinant difference above is nonnegative. Therefore

```math
I_c(\rho,\mathcal N_M)
\le\frac q{\widetilde q}F(\widetilde q)
\le F(\widetilde q)\le\max_sF(s).
```

This includes pure inputs $d=0$, where both conditional entropies coincide and the value is zero. For a diagonal input, $\widetilde q=q$. Photon counting has exactly $r=R$ for the vacuum outcome and $r=0$ for the collected-excitation outcome, so it saturates the chord. Optimizing its diagonal input proves the claimed equality. No assumption that a general fixed POVM is phase covariant was used.

## 4. Strict collective advantage throughout the qubit interior

**Corollary.** For every qubit split with $`a+b+c=1`$, $`a>b>0`$ and $`c>0`$,

```math
\boxed{0<Q_{\rm prod}=Q_{\rm count}<Q_{\rm meas}.}
```

Thus unrestricted helper measurements strictly outperform every predetermined
product helper strategy, including use-varying choices fixed in advance. Both
capacities allow arbitrary sender/receiver block codes and measure unconditional
asymptotic transmission in qubits per original use.

**Proof.** With binary entropy in bits, define the diagonal-input functions

```math
D_1(q)=h_2(aq)-h_2(bq),\qquad
D_2(q)=h_2((1-b)q)-h_2(bq),\qquad
G(q)=\min\{D_1(q),D_2(q)\}.
```

The [qubit theorem](THEOREM.md#3-qubit-decay-exact-rate-and-irreversible-boundary)
gives $`Q_{\rm meas}=\max_{[0,1]}G`$; Sections 1–3 give
$`Q_{\rm prod}=\max_{[0,1]}F`$ after optimizing every product POVM and all inputs,
including coherent inputs. The comparison below concerns these diagonal-input
functions, not counting optimality at each fixed coherent input.

Locally set $`\phi(t)=t\log_2t`$, with $`\phi(0)=0`$, and for positive real
arguments define

```math
\begin{aligned}
J(x;y,z)&=\phi(x+y+z)-\phi(x+y)-\phi(x+z)+\phi(x)\\
&=\frac1{\ln2}\int_0^y\int_0^z\frac{dt\,ds}{x+s+t}>0.
\end{aligned}
```

The integral follows by integrating $`\phi''(t)=1/(t\ln2)`$ twice. Put
$`u(q)=1-(1-b)q`$ and $`v(q)=1-(1-a)q`$. Expanding the binary entropies gives

```math
F(q)=-\phi(u)-\phi(aq)+\phi(v)+\phi(bq),
```

and hence the exact identities

```math
\begin{aligned}
D_1(q)-F(q)&=J\bigl(u(q);(a-b)q,cq\bigr),\\
D_2(q)-F(q)&=J\bigl(aq;1-q,cq\bigr).
\end{aligned}
```

For the first identity the two partial sums are $`v(q)`$ and $`1-aq`$;
for the second they are $`v(q)`$ and $`(1-b)q`$. Both total sums are
$`1-bq`$. For $`0<q<1`$, all three arguments of each mixed difference are
positive: in particular $`u(q)>b>0`$, $`(a-b)q>0`$, $`aq>0`$, $`1-q>0`$
and $`cq>0`$. Therefore $`F(q)<G(q)`$ at every interior diagonal input.

Since $`1-cq\ge a+b>0`$, the counting objective is continuous on $`[0,1]`$,
with $`F(0)=F(1)=0`$. Differentiating its expanded form yields

```math
F''(q)=-\frac{a-b}{\ln2\,q\,u(q)\,v(q)}<0.
```

Strict concavity makes $`F`$ positive on $`(0,1)`$, so its unique attained
maximizer $`q_*`$ lies in that interval. Evaluate the unrestricted objective
at this same product-optimal input:

```math
Q_{\rm meas}\ge G(q_*)>F(q_*)=Q_{\rm prod}>0.
```

For a quantitative bound, the integral also gives

```math
J(x;y,z)\ge\frac{yz}{(x+y+z)\ln2}.
```

Using the common total $`1-bq`$ in the two identities,

```math
D_1(q)-F(q)\ge\frac{c(a-b)q^2}{(1-bq)\ln2},\qquad
D_2(q)-F(q)\ge\frac{cq(1-q)}{(1-bq)\ln2}.
```

Taking their minimum at $`q_*`$ proves the conservative bound

```math
\boxed{
Q_{\rm meas}-Q_{\rm prod}
\ge\frac{cq_*}{(1-bq_*)\ln2}
\min\{(a-b)q_*,1-q_*\}>0.
}
```

This is a parameter-dependent lower bound, not the exact capacity difference
or a uniform positive gap over the open region. At fixed interior input it
vanishes as $`c\to0`$ or $`a\to b`$. At $`c=0`$ there is no collected helper
output and the capacities coincide; at $`a=b`$ both capacities vanish.
At $`q=0,1`$, $`F=G=0`$; the second mixed difference vanishes at $`q=1`$,
while the first need not. These consistency checks do not extend the product
theorem to $`b=0`$.

The corollary compares rates within the existing operational model. It does
not change the positive-capacity boundary, supply finite-block fidelity or
implementation guarantees, or establish necessity of coherent helper memory.
Outcome-adaptive local strategies and general separable block POVMs remain
outside the product benchmark. The all-POVM optimization is a qubit result.

## 5. A small exact-arithmetic certificate

With $`u,v`$ as above, $`F'`$ tends to $`+\infty`$ at zero and equals
$`\log_2(b/a)<0`$ at one. Thus there is one maximizing root. At the example's
rational parameters, the derivative sign is exactly the sign of

```math
20(1-23q/25)^{23}-q^3(1-4q/5)^{20}.
```

Rational evaluation brackets the root between $0.5583443480550842$ and $0.5583443480550843$. Concavity gives a lower bound from $F(q_-)$ and an upper bound from its tangent over $[q_-,q_+]$. The certificate evaluates every logarithm using rational range reduction and the series

```math
\ln x=2\sum_{k=0}^{N-1}\frac{t^{2k+1}}{2k+1}+R_N,
\qquad t=\frac{x-1}{x+1},\qquad
|R_N|\le\frac{2|t|^{2N+1}}{(2N+1)(1-t^2)}.
```

After reducing to $1\le x\le2$, $|t|\le1/3$. Forty terms and exact rational arithmetic certify the displayed capacity and gap intervals. No floating-point optimizer or tolerance is a correctness premise.

Run [the certificate](../checks/certify_product_capacity.py) after the verification runner:

```bash
python checks/certify_product_capacity.py --output NEW_EVIDENCE_DIRECTORY/product-capacity-certificate.json
```

The dedicated workflow step includes its output in the downloaded evidence. The 23 scientific groups are checked separately against their reference reports. This arithmetic certifies the scalar evaluation conditional on the analytical theorem.

## Attribution

The entropy function $`e(C)`$ and its ordinary convexity are established in Wootters, [quant-ph/9709029](https://arxiv.org/pdf/quant-ph/9709029), Eq. (8) and following paragraph, PDF page 4. The difference-convexity calculation needed here is derived above. Laustsen, Verstraete and van Enk, [quant-ph/0206192](https://arxiv.org/pdf/quant-ph/0206192), Section 2, Eqs. (5), (9), (24), distinguish entropy assistance from their optimized concurrence-assistance objective; those formulas cannot simply replace this entropy-difference optimization.

The [contribution comparison](CONTRIBUTION_ASSESSMENT_2026-10-07.md) relates this result to detected-jump capacity and collective-assistance predecessors. The measurement optimization here establishes all-input optimality of counting over every predetermined product helper POVM with an inaccessible residual output.
