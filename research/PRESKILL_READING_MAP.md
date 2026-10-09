# From Preskill to the capacity proofs

**One tutorial, four worked bridges.** The question throughout is: how can joint measurements of a collected field improve quantum transmission when the helper sends only a classical record?

Start with [the physical picture](PHYSICAL_PICTURE.md) or return to [the repository overview](../README.md). This guide assumes familiarity with density matrices, partial traces, purification and POVMs. It supplies a route through the existing proofs, not a new result.

> John Preskill, **Quantum Shannon Theory**, Chapter 10, **2025 revision, arXiv v5**.
>
> [Versioned record](https://arxiv.org/abs/1604.07450v5) · [Author chapter](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf)

This is the sole tutorial anchor. The chapter is labeled June 2025; arXiv v5 was submitted on 8 July 2025. Read the selections below before their matching bridge. Original research papers are credited in the linked proofs; their additional ingredients are explained locally. The chapter is linked, not redistributed.

## Reading route

| Preskill selection | What to understand | Continue here |
|---|---|---|
| Sections 10.6.1–10.6.3; 10.7.1–10.7.3 | Classical–quantum states, coherent information, complementary channels and degradability | [1. The measurement record and its complement](#1-the-measurement-record-and-its-complement) |
| Sections 10.2.1–10.2.4; 10.8–10.9.4 | Entropy, strong subadditivity, data processing, decoupling and coding without borrowed entanglement | [2. Two cuts and a matching construction](#2-two-cuts-and-a-matching-construction) |
| Section 10.7.3; Exercise 10.18 | Degradable-channel additivity and the amplitude-damping example | [3. Why counting is the best individual measurement](#3-why-counting-is-the-best-individual-measurement) |
| Entropy and coding material above | Which finite-dimensional arguments need an energy-constrained extension | [4. The optical energy limit](#4-the-optical-energy-limit) |

Preskill's entanglement-assisted communication resource includes preshared sender–receiver entanglement. This project supplies no such resource: a helper measures the collected output and sends a classical record only to the receiver. Keep that distinction when reading Section 10.8.1.

## 1. The measurement record and its complement

**Goal:** identify the actual channel seen by the decoder and the environment needed to compute its coherent information.

Let $`V:A\to BED`$ be the splitting isometry. The receiver holds $`B`$, the inaccessible field is $`E`$, and the helper holds $`D`$. The hypothesis is

```math
\mathcal N_{ED}=(\mathcal T_{B\to E}\otimes\mathrm{id}_D)\mathcal N_{BD}.
```

This equality preserves correlations with $`D`$ and arbitrary references. Matching only the $`E`$ marginal would not imply the conditional statement below.

### A counting example

For the qubit splitter, $`V|0\rangle=|000\rangle`$ and $`V|1\rangle=\sqrt a|100\rangle+\sqrt b|010\rangle+\sqrt c|001\rangle`$, in $`BED`$ order, with $`a+b+c=1`$. Measure $`D`$ in its vacuum/excitation basis. The resulting maps from $`A`$ to $`BE`$ are

```math
\begin{aligned}
W_0|0\rangle&=|00\rangle,&
W_0|1\rangle&=\sqrt a|10\rangle+\sqrt b|01\rangle,\\
W_1|0\rangle&=0,&
W_1|1\rangle&=\sqrt c|00\rangle.
\end{aligned}
```

For the diagonal input $`\rho_q=(1-q)|0\rangle\langle0|+q|1\rangle\langle1|`$, the probabilities are $`p_0=1-cq`$ and $`p_1=cq`$. When $`p_0>0`$, the no-count branch has excitation probabilities $`aq/(1-cq)`$ and $`bq/(1-cq)`$ in $`B`$ and $`E`$. In the count branch both are vacuum. The decoder knows which branch occurred; it receives a classical label alongside $`B`$.

### Copy the classical label into the dilation

For any finite rank-one-refined helper POVM, let its rows $`m_x:D\to\mathbb C`$ satisfy $`\sum_xm_x^\dagger m_x=I_D`$. Define

```math
W_x=(I_{BE}\otimes m_x)V,\qquad
J=\sum_xW_x\otimes|x\rangle_X|x\rangle_Y.
```

Completeness gives $`J^\dagger J=I_A`$. Tracing out $`EY`$ gives the receiver output; reversing the trace gives its complement:

```math
\begin{aligned}
\mathcal N_M(\rho)&=\sum_xp_x\rho_{B|x}\otimes|x\rangle\langle x|_X,\\
\mathcal N_M^c(\rho)&=\sum_xp_x\rho_{E|x}\otimes|x\rangle\langle x|_Y.
\end{aligned}
```

Here $`p_x=\mathrm{Tr}(W_x\rho W_x^\dagger)`$, with normalized conditional states when $`p_x>0`$. The orthogonal labels remove cross terms. They copy a classical outcome, not an unknown quantum state.

Applying the helper row to the joint identity commutes with $`\mathcal T`$, which acts only on $`B`$. Hence $`\mathcal T(\rho_{B|x})=\rho_{E|x}`$. Acting with $`\mathcal T`$ and relabeling $`X`$ as $`Y`$ simulates the complement: the refined measured channel is degradable. It grants no access to the physical $`E`$. For a measurement on $`D^n`$, use $`V^{\otimes n}`$ and $`\mathcal T^{\otimes n}`$.

For a finite classical alphabet,

```math
S(BX)=H(p)+\sum_xp_xS(B_x),\qquad
S(EY)=H(p)+\sum_xp_xS(E_x).
```

The two classical entropies cancel, so $`I_c=S(B|X)-S(E|X)`$. In the counting example this is exactly the function $`F(q)`$ in Bridge 3.

**Checkpoint:** why is $`E`$ alone not the complement? The measurement record also leaks into $`Y`$. A coarse record can additionally leave a quantum register $`G`$, giving complement $`EGY`$. Omitting it invalidates the displayed subtraction. The original unmeasured channel to $`B`$ instead has complement $`ED`$.

[PROOF_AUDIT](PROOF_AUDIT.md) gives the detailed dilation. The [direct converse](CLAIM_ASSESSMENT_2026-10-07.md) retains unresolved helper outputs and discarded encoder ancillas. Continuous records use finite partitions or conditional-entropy integrals, not subtraction of divergent differential entropies; see [PROOF_DEPENDENCIES](PROOF_DEPENDENCIES.md).

## 2. Two cuts and a matching construction

**Goal:** understand why the rate is the smaller of two entropy differences evaluated on the same input, and how a helper measurement attains it.

### Upper bounds with general encoders

Purify an arbitrary encoded input as $`RFA^n`$: $`R`$ is the reference, and $`F`$ is the system discarded by the encoder. After the channel, $`RFB^nE^nD^n`$ is pure.

Both finite-dimensional cuts follow from **Leditzky–Datta–Smith's degradable-state theorem**, Definition 2.2 and Proposition 2.4, as explained in [PROOF_DEPENDENCIES, Section 1](PROOF_DEPENDENCIES.md). For a degradable state on $`LK`$, its optimized one-way distillation quantity is $`D_{\to}^{(1)}=I(L\rangle K)`$. Apply it to two enlarged tasks:

| Grouping $`L:K`$ | Purifier | Upper bound on decoded coherent information |
|---|---|---|
| $`RFD^n:B^n`$ | $`E^n`$ | $`S(B^n)-S(E^n)`$ |
| $`RF:B^nD^n`$ | $`E^n`$ | $`S(B^nD^n)-S(E^n)`$ |

The joint identity supplies degradability in the first row. In the second, discard $`D^n`$ and then apply $`\mathcal T^{\otimes n}`$. These are upper-bound relaxations: they do not give the actual helper access to $`R`$ or $`F`$, or a coherent link to the receiver. Retaining $`F`$ is what includes general encoders.

The refined-channel calculation from Bridge 1 offers a useful view of the first cut:

```math
I_c=S(B^n)-S(E^n)-[I(X;B^n)-I(X;E^n)]
\le S(B^n)-S(E^n).
```

Data processing makes the bracket nonnegative. The second cut hypothetically delivers $`B^nD^n`$ coherently; measuring $`D^n`$ is then receiver processing. These calculations explain the entropy terms, while the state-theorem reduction supplies the general-encoder bound.

Subadditivity across uses and concavity, proved in [THEOREM, Section 2](THEOREM.md), bound both cuts using the same average input marginal $`\bar\rho`$. Thus

```math
Q_{\rm meas}\le
\max_{\rho_A}\left[\min\{S(B),S(BD)\}-S(E)\right].
```

Optimizing each cut separately could yield a weaker bound because their maximizing inputs need not coincide.

### The helper ensemble, then ordinary coding

Preskill explains how coherent information becomes a transmission rate. The extra helper ingredient is the **Smolin–Verstraete–Winter assistance ensemble theorem**, with the receiver-only construction credited in [THEOREM](THEOREM.md).

Purify $`\rho_A`$ by $`R`$ and use the mathematical grouping $`B|(RE)|D`$. The inherited theorem selects a measurement on $`D^m`$ with average branch entropy of $`B^m`$ approaching $`m\min\{S(B),S(BD)\}`$. This grouping grants no operation on $`R`$ or $`E`$. Concavity bounds the average branch entropy of $`E^m`$ by $`mS(E)`$.

Freeze that helper measurement at block length $`m`$. It defines a flagged channel from $`A^m`$ to $`B^mX`$. Encode unknown quantum messages across $`k`$ repeated uses of this fixed channel, take the coding limit in $`k`$, and divide the rate by $`m`$ to return to original channel uses. Increasing $`m`$ then approaches the desired entropy difference. The helper record goes only to the decoder. All outcomes, including atypical and failure outcomes, remain in the channel; none is postselected away.

This matches the upper bound without encoder knowledge of the outcome or preshared entanglement.

**Checkpoint:** what are the two block lengths doing? The helper block $`m`$ builds a favorable channel; the coding block $`k`$ transmits through repeated uses of that channel. Their roles are distinct. The full operational converse and construction are in [PROOF_DEPENDENCIES](PROOF_DEPENDENCIES.md) and [THEOREM](THEOREM.md).

## 3. Why counting is the best individual measurement

**Goal:** rule out every better predetermined single-use POVM, while still allowing arbitrary endpoint block codes.

Work in the qubit regime $`a>b>0,c>0`$. Preskill's degradable-channel additivity reduces predetermined product helper measurements to a one-use optimization. Measurements may vary between uses; the sender and receiver may use arbitrary block codes. Outcome-adaptive local strategies and general separable block POVMs are outside this reduction.

For the diagonal input in Bridge 1, counting gives

```math
F(q)=(1-cq)\left[
h_2\!\left(\frac{aq}{1-cq}\right)
-h_2\!\left(\frac{bq}{1-cq}\right)\right],
\qquad 0\le q\le1.
```

Here $`h_2`$ is binary entropy in bits. The no-count branch supplies both entropies; the count branch contributes zero. The remaining question is whether another POVM and a coherent input can do better.

Write an arbitrary input as

```math
\rho=\begin{pmatrix}1-q&z\\z^*&q\end{pmatrix},
\qquad d=q(1-q)-|z|^2\ge0.
```

The [exact product proof, Sections 1–3](EXACT_PRODUCT_CAPACITY_2026-10-07.md) computes branch determinants and expresses each entropy difference as $`f(r_x)`$. For $`q>0`$, the scalar satisfies

```math
0\le r_x\le r_{\max}=\frac q{d+(a+b)q^2},
\qquad \sum_xp_xr_x=1.
```

The proof establishes convexity of the **difference** $`f`$, with $`f(0)=0`$. Convexity of the individual entropy function would not suffice. The straight chord from zero to the endpoint therefore gives

```math
\sum_xp_xf(r_x)\le
\sum_xp_x\frac{r_x}{r_{\max}}f(r_{\max})
=\frac{f(r_{\max})}{r_{\max}}.
```

Set $`\widetilde q=1/(1+d/q^2)`$. Positivity of the input gives $`q\le\widetilde q\le1`$, and the endpoint becomes

```math
I_c(\rho,\mathcal N_M)
\le\frac q{\widetilde q}F(\widetilde q)
\le\max_{0\le s\le1}F(s).
```

The last step uses $`F\ge0`$ and $`q/\widetilde q\le1`$; the $`q=0`$ input has zero rate. For a diagonal input, $`\widetilde q=q`$. Counting has branch scalars at the two chord endpoints, so it saturates the bound. Consequently,

```math
Q_{\rm prod}=Q_{\rm count}=\max_qF(q).
```

This is counting optimality **after optimizing the input**. It does not claim counting is best for every fixed coherent input. The full proof defines $`f`$, derives its second derivative and treats continuous POVMs.

The [strict-gap corollary](EXACT_PRODUCT_CAPACITY_2026-10-07.md#4-strict-collective-advantage-throughout-the-qubit-interior)
compares the two entropy objectives at the product-optimal input and gives
$`0<Q_{\rm prod}<Q_{\rm meas}`$ throughout $`a+b+c=1,\ a>b>0,\ c>0`$.
At $`(a,b,c)=(0.2,0.08,0.72)`$, the product and unrestricted capacities are approximately $`0.18621044`$ and $`0.30570954`$ qubits/use. The [rational certificate](../checks/certify_product_capacity.py) verifies the scalar rate and gap enclosures conditional on the analytical reduction; it does not certify the proof over all POVMs.

**Checkpoint:** which step rules out a better individual detector, and which allows arbitrary endpoint coding? The all-input chord bound answers the first; degradable product-channel additivity answers the second.

## 4. The optical energy limit

**Goal:** distinguish an all-input energy-constrained converse from an achievable rate built using thermal average inputs.

The optical splitter has vacuum environmental inputs and an average incident signal budget of $`N`$ photons per original mode. Its thermal average input is

```math
\tau_N=\sum_{j=0}^{\infty}
\frac{N^j}{(N+1)^{j+1}}|j\rangle\langle j|,
\qquad
S(\tau_N)=g(N)=(N+1)\log_2(N+1)-N\log_2N.
```

For this input, $`S(B)=g(aN)`$ and $`S(E)=g(bN)`$. A passive transformation of the joint output $`BD`$ places its signal in one populated mode and leaves the other mode in vacuum, so $`S(BD)=g((a+c)N)=g((1-b)N)`$. It is not the sum of the two marginal entropies. Because $`a+c\ge a`$ and $`g`$ is increasing, the first cut is the smaller one.

This evaluates a candidate rate. Establishing the capacity requires both sides:

| Step | What must be justified |
|---|---|
| Converse for all admissible codes | The full Fock-space joint identity and thermal-reference relative-entropy contraction bound arbitrary entangled, non-Gaussian inputs under the average budget. |
| Achievability | Finite photon cutoffs, a fixed helper block and energy-constrained coding approach the thermal rate with explicit entropy-tail control. |

For achievability at $`N>0`$, first fix a cutoff $`K`$ and helper block $`m`$. The normalized truncated thermal input has mean $`N_K<N`$. The resulting finite-dimensional flagged channel uses the additive input photon observable with mean $`mN_K<mN`$. The energy-constrained coding theorem applies with this slack. Take the coding limit for that fixed channel, then enlarge the helper block as required by the assistance theorem, and only afterward send $`K\to\infty`$. At finite cutoff retain both entropy cuts; do not assume their thermal ordering before the limit.

[PROOF_DEPENDENCIES, Section 3](PROOF_DEPENDENCIES.md) supplies the fixed-cutoff/block application of Wilde–Qi's coding theorem and the entropy-tail bounds. Trace-distance convergence alone does not imply entropy convergence in infinite dimensions. A thermal average coded input is not a thermal bath.

The result is

```math
Q_{\rm optical}(N)=
\begin{cases}
g(aN)-g(bN),&a>b,\\
0,&a\le b.
\end{cases}
```

It is zero at $`N=0`$. For fixed $`a>b>0`$, it approaches $`\log_2(a/b)`$ as energy grows. This optical ceiling does not establish counting optimality for optical measurements.

**Checkpoint:** does choosing a thermal input restrict the converse to Gaussian codes? No. The converse is all-input; the thermal family is used to approach its bound. The cutoff is a proof device for achievability, not a maximum photon number imposed on the capacity problem.

## Continue by question

| Question | Read |
|---|---|
| What are the operational permissions and exclusions? | [Model and claims](MODEL_AND_CLAIMS.md) |
| Where is the complete capacity argument? | [Theorem](THEOREM.md) |
| Which ingredients are inherited, and how are they applied? | [Proof dependencies](PROOF_DEPENDENCIES.md) |
| How are arbitrary helper POVMs bounded? | [Exact product capacity](EXACT_PRODUCT_CAPACITY_2026-10-07.md) |
| What does the numerical evidence establish? | [Verification policy](../VERIFICATION.md) |

Work through each checkpoint in your own words and then follow the corresponding full proof.
