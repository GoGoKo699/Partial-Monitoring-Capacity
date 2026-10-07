# From quantum Shannon theory to the two capacity proofs

**7 October 2026. A learning guide to the existing author-side results.** Start with [the physical picture](PHYSICAL_PICTURE.md). The question to carry through the reading is: how can joint measurements of a collected field improve quantum transmission when the helper sends only a classical record?

Use one tutorial anchor: John Preskill, *Quantum Shannon Theory*, Chapter 10, **2025 revision, arXiv v5** ([official chapter](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf), [versioned record](https://arxiv.org/abs/1604.07450v5)). The chapter is labeled June 2025; arXiv v5 was submitted on 8 July 2025. Read the selected sections below before their matching proof steps. The chapter supplies the information-theory language; the bridges here explain the additional dependencies in this repository. No copy of the chapter is redistributed.

## Reading map

| Preskill selection | What to understand | Then read here |
|---|---|---|
| §§10.2.1–10.2.4 | Entropy, concavity, strong subadditivity and mutual-information data processing. | The two upper bounds in [THEOREM, Section 2](THEOREM.md). |
| §§10.6.1–10.6.3 | Classical–quantum states, measurement records and Holevo information. | The worked flag/complement construction below. |
| §§10.7.1–10.7.3; Exercise 10.18 | Coherent information, complementary channels, degradability and additivity; amplitude damping as an example. | [THEOREM, Sections 2–3](THEOREM.md), then Section 1 of the [product-helper proof](PRODUCT_HELPER_GAP_2026-10-07.md). |
| §§10.8–10.9.4 | Decoupling and channel coding; how §10.9.4 removes borrowed entanglement. | Receiver-only achievability in [THEOREM, Section 2](THEOREM.md). |

For the first checkpoint, use the first three rows. Defer the coding sections until Section 3 below and the optical bridge until Section 5.

Preskill's entanglement-assisted communication resource includes preshared sender–receiver entanglement. This project supplies no such resource: a helper measures the collected output and sends a classical record only to the receiver. Keep that distinction when reading §10.8.1. The helper-ensemble theorem, joint-register converse, product-measurement optimization and optical entropy-tail argument remain explicit bridges to the research proofs.

## 1. Work through the classical flag and the actual complement

In finite dimensions, let $V:A\to BED$ be the splitting isometry. The receiver holds $B$, the inaccessible field is $E$, and the helper holds $D$. The hypothesis is

```math
\mathcal N_{ED}=(\mathcal T_{B\to E}\otimes\mathrm{id}_D)\mathcal N_{BD}.
```

The equality preserves correlations with $D$ and arbitrary references. Matching only the $E$ marginal would not imply the conditional statement used below.

First consider a finite, rank-one-refined helper POVM. Its rows $m_x:D\to\mathbb C$ satisfy $\sum_xm_x^\dagger m_x=I_D$. Define

```math
W_x=(I_{BE}\otimes m_x)V,\qquad
J=\sum_xW_x\otimes|x\rangle_X|x\rangle_Y.
```

Completeness gives $J^\dagger J=I_A$. Treat $BX$ as the receiver output and trace out $EY$; the orthogonal $Y$ labels remove cross terms between different outcomes. Reversing the trace gives the complementary output $EY$:

```math
\begin{aligned}
\mathcal N_M(\rho)&=\sum_xp_x\rho_{B|x}\otimes|x\rangle\langle x|_X,\\
\mathcal N_M^c(\rho)&=\sum_xp_x\rho_{E|x}\otimes|x\rangle\langle x|_Y.
\end{aligned}
```

Here $p_x=\operatorname{Tr}(W_x\rho W_x^\dagger)$, and the conditional states are normalized when $p_x>0$. The labels copy a classical outcome, not an unknown quantum state. The complement keeps a copy even though the receiver also knows the outcome.

Applying the helper row to the joint identity commutes with $\mathcal T$, which acts only on $B$. Thus $\mathcal T(\rho_{B|x})=\rho_{E|x}$ for each outcome. Acting with $\mathcal T$ on $B$ and relabeling $X$ as $Y$ simulates the whole complement: the refined measured channel is degradable. This produces a simulated $E'$ with the correct complementary marginal; it grants no access to the physical $E$. For a collective measurement on $D^n$, the same argument uses $V^{\otimes n}$ and $\mathcal T^{\otimes n}$.

For this finite classical alphabet, block-state entropy gives

```math
S(BX)=H(p)+\sum_xp_xS(B_x),\qquad
S(EY)=H(p)+\sum_xp_xS(E_x).
```

The two classical entropies cancel, leaving $I_c=S(B|X)-S(E|X)$. They cancel because the dilation includes both flags; omitting the complementary flag would change the calculation.

**Two boundaries to check.** The original channel to $B$ has complement $ED$, so simulating $E$ alone does not make that original channel degradable. Also, a coarse helper record can leave a residual quantum register $G$: its complement is generally $EGY$. The $E$-only subtraction above is then unjustified. The [direct converse](CLAIM_ASSESSMENT_2026-10-07.md) retains $G$ and the discarded encoder ancilla $F$, and uses weak monotonicity rather than assuming coarse-channel degradability. Continuous optical records are handled by finite partitions, not by subtracting divergent differential entropies.

**First reading checkpoint:** reconstruct $J$, trace out each side, and explain why the joint identity survives conditioning. Then explain why tracing out part of the record does not preserve the displayed coherent-information formula. Use [PROOF_AUDIT](PROOF_AUDIT.md) to check the answer.

## 2. See why both entropy cuts use the same input

For a refined measured block channel, the first upper bound is

```math
I_c=S(B^n)-S(E^n)-[I(X;B^n)-I(X;E^n)]
\le S(B^n)-S(E^n).
```

The bracket is nonnegative by the conditional degrading map and data processing. The second bound comes from hypothetically delivering $B^nD^n$ coherently: measuring $D^n$ and retaining its classical outcome is receiver processing, so

```math
I_c\le S(B^nD^n)-S(E^n).
```

This stronger resource is used only for an upper bound. It is not granted to the actual helper. To finish the converse, [THEOREM, Section 2](THEOREM.md) proves subadditivity across uses and concavity for both entropy differences. Both are bounded using the same average input marginal $\bar\rho$. This gives

```math
Q_{\rm meas}\le\max_\rho[\min\{S(B),S(BD)\}-S(E)],
```

not a separate optimization of each cut. The direct converse cited above supplies the general-encoder step: discarding $F$ cannot evade these bounds. Reading only the refined-channel entropy calculation does not establish that step.

## 3. Separate the inherited ensemble theorem from ordinary coding

Preskill's coding discussion explains how coherent information becomes a transmission rate. It does not supply the helper measurement needed here. The additional ingredient is the Smolin–Verstraete–Winter assistance ensemble theorem, credited with its original source in [THEOREM](THEOREM.md).

Purify $\rho_A$ by $R$ and use the mathematical grouping $B|(RE)|D$. The inherited theorem selects a measurement on $D^n$ with average branch entropy of $B^n$ approaching $n\min\{S(B),S(BD)\}$. Grouping $RE$ grants no operation on either system. Concavity separately bounds the average branch entropy of $E^n$ by $nS(E)$. Their difference approaches the objective above.

Now freeze that helper block measurement and apply ordinary quantum coding to repeated uses of the resulting flagged channel, dividing the rate by the helper block length. The flag goes only to the decoder. This is the ensemble-then-channel construction explained in the repository's receiver-only achievability proof, citing SVW Theorems 1 and 8. It neither requires the encoder to learn the outcome nor consumes preshared entanglement.

## 4. Follow the product optimum through its chord bound

Read [EXACT_PRODUCT_CAPACITY, Sections 1–3](EXACT_PRODUCT_CAPACITY_2026-10-07.md) after the degradable-channel material, for the qubit regime $a>b>0,c>0$. Additivity reduces predetermined product helper measurements to a one-use optimization, even when endpoint codes span many uses. It does not cover outcome-adaptive local strategies or general separable block POVMs.

The remaining optimization is a repository-specific argument. Branch determinants reduce the two conditional qubit entropies to one scalar $r_x$, with $0\le r_x\le R$ and $\sum_xp_xr_x=1$. The proof establishes convexity of their **difference** $f(r)$ and $f(0)=0$. Convexity of the individual entropy function alone would not suffice. The chord gives $\sum_xp_xf(r_x)\le f(R)/R$.

For input excitation $q$ and determinant $d$, the proof then chooses $\widetilde q=1/(1+d/q^2)\ge q$ for $q>0$, obtaining

```math
I_c(\rho,\mathcal N_M)\le\frac q{\widetilde q}F(\widetilde q)
\le\max_{0\le s\le1}F(s),
```

Here $F$ is the nonnegative counting objective defined there, and $q/\widetilde q\le1$ justifies the second inequality. Counting with a diagonal input saturates the chord. The conclusion is counting optimality **after optimizing the input**; it does not claim that counting is best for every fixed coherent input.

At $(a,b,c)=(0.2,0.08,0.72)$, the product and unrestricted capacities are approximately $0.18621044$ and $0.30570954$ qubits/use. The [rational certificate](../checks/certify_product_capacity.py) verifies the scalar rate and gap enclosures, conditional on the analytical reduction. It does not certify the proof over all POVMs.

**Second reading checkpoint:** identify the exact step that rules out a better predetermined individual measurement, then identify the different step that allows arbitrary endpoint block coding. The answers are the all-input chord bound and degradable product-channel additivity, respectively.

## 5. Keep the optical limit as a separate bridge

The finite-dimensional chapter is not a substitute for the energy argument. In [OPTICAL_AUDIT, Sections 4.2–4.3](OPTICAL_AUDIT.md), the converse bounds arbitrary, possibly entangled non-Gaussian inputs under the average incident photon budget. Thermal-reference relative-entropy contraction gives the all-input upper bound.

Only achievability truncates the thermal average input. First fix a finite photon cutoff and helper block, then take the coding limit with energy slack, and only afterward increase the cutoff using explicit entropy-tail bounds. Trace-distance convergence alone is insufficient to assert entropy convergence in infinite dimensions. The environmental inputs remain vacuum; a thermal average coded input is not a thermal bath.

The resulting optical rate is $g(aN)-g(bN)$ for $a>b$, and zero otherwise, with $g(x)=(x+1)\log_2(x+1)-x\log_2x$. For fixed $a>b>0$, it approaches $\log_2(a/b)$ as energy grows. This supports the physical story; it does not extend the qubit counting-optimality theorem to optical measurements.

## Where to stop this pass

Begin with the first checkpoint and explain it in your own words before moving through the two cuts and the product chord. The research claims, limitations and attributions remain in the linked proofs and [model map](MODEL_AND_CLAIMS.md). This guide adds a learning route, not a new result or independent proof review. The next task is to work through that first checkpoint with the author; no scientific expansion is needed.
