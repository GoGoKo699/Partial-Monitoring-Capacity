# Proof dependencies and scope

The capacity formulas and communication resources are unchanged. The finite-dimensional converse has a stronger prior-art reduction than the earlier comparison identified: both cuts follow from the established one-way distillation theorem for degradable states after regrouping registers. The exact product-measurement optimum remains a separate optimization. This record supplies that attribution correction and makes the continuous-measurement and optical coding dependencies explicit.

## 1. Finite-dimensional converse: a degradable-state reduction

Leditzky, Datta and Smith, [*Useful states and entanglement distillation*](https://arxiv.org/abs/1701.03081v4), Definition 2.2 and Proposition 2.4, establish

```math
D_{\to}^{(1)}(\omega_{LK})=I(L\rangle K)_\omega
```

for a finite-dimensional degradable state. Here $D_{\to}^{(1)}=\max_{\mathcal J}I(L'\rangle KM)$, where $\mathcal J:L\to L'M$ is an instrument and its classical record $M$ is sent to $K$. Subsequent receiver decoding cannot increase coherent information. Degradability means that a channel on $K$ reproduces the purifying system while preserving its correlations with $L$. The single-copy optimized statement is enough for the following application; no regularization limit is needed for either block bound.

First take a finite helper record. Purify an arbitrary encoded input as $RFA^n$, retaining its discarded encoder system $F$. After $V^{\otimes n}$, the state $\omega_{RFB^nE^nD^n}$ is pure. Let $\widehat B$ denote the decoded logical output. The following register identifications are an application of that existing proposition to this communication task. Normal continuous records follow through the finite-partition argument in Section 3, also valid for finite-dimensional outputs.

**First cut.** Take $L=RFD^n$, $K=B^n$, with purifier $E^n$. The channel hypothesis, including reference $RF$, gives

```math
\omega_{RFD^nE^n}
=(\operatorname{id}_{RFD^n}\otimes\mathcal T^{\otimes n})
  (\omega_{RFD^nB^n}).
```

Thus $\omega_{LK}$ is degradable. The permitted helper measurement and discarding $F$ are an instrument from $L$ to $R$ and a classical message. The actual protocol is a subset of the enlarged one-way task; allowing joint access to $RFD^n$ is used only for this upper bound. Receiver decoding is included in the allowed processing. Therefore

```math
I(R\rangle\widehat B)
\le D_{\to}^{(1)}(\omega_{RFD^n:B^n})
=S(B^n)-S(E^n).
```

**Second cut.** Take $L=RF$, $K=B^nD^n$, again with purifier $E^n$. Its degrading map is $\mathcal T^{\otimes n}\circ\operatorname{Tr}_{D^n}$. Discarding $F$ acts on $L$; the helper measurement and decoding now belong to $K$'s local operation. The same proposition yields

```math
I(R\rangle\widehat B)\le S(B^nD^n)-S(E^n).
```

The two applications concern the same encoded state. The concavity, product-map subadditivity and common-input averaging in [THEOREM, Section 2](THEOREM.md) give the finite-dimensional capacity upper bound $Q_*$. If the decoded state is at trace distance $\delta_n$ from a maximally entangled state of dimension $d_n$, conditional-entropy continuity gives

```math
(1-2\delta_n)\log_2d_n-g_2(\delta_n)
\le I(R\rangle\widehat B)\le nQ_*,
\qquad g_2(\delta)=(1+\delta)h_2\!\left(\frac{\delta}{1+\delta}\right).
```

For $\delta_n\to0$, division by $n$ supplies the operational converse without first assuming $\log d_n=O(n)$. The inherited assistance ensemble and fixed-measurement coding construction give the reverse inequality. Atypical and failure outcomes are included in the completed helper POVM; their vanishing weight is absorbed into the ensemble entropy error, rather than postselected away. The result is therefore a capacity consequence assembled from established ingredients under the stated register-preserving hypothesis. Its proof does not require an independently new converse inequality.

The explicit refined-channel proof remains useful: it identifies the real complement, explains the measurement deficit and supports the product-measurement reduction. The [direct converse](CLAIM_ASSESSMENT_2026-10-07.md) also remains useful for coarse records and finite-energy optical systems. The cited state theorem is finite dimensional; it does not replace those infinite-dimensional arguments automatically.

**Attribution correction.** The [earlier contribution assessment at revision 6655613](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/blob/66556130d6c308653f2e34f6730d2990efb3b30a/research/CONTRIBUTION_ASSESSMENT_2026-10-07.md) presented the partial-access converse as an additional substantive implication not supplied by the inspected predecessors. The reduction above narrows that assessment. The exact helper-capacity formula was not located as a stated theorem in the new source, but that absence does not make its converse mechanism new. No rate, domain, protected source or reference report is corrected.

## 2. Why this does not settle the product-measurement optimum

The same source's Proposition 2.7 establishes convexity for suitable mixtures under its tensor-product hypothesis; Theorem 2.8 then gives an upper bound through a **minimum** over degradable/antidegradable decompositions. The helper problem instead maximizes a shared branch-entropy difference over physically allowed measurements. That minimum controls a state-distillation bound and supplies no ordering of the physically allowed helper measurement averages. The [exact product proof](EXACT_PRODUCT_CAPACITY_2026-10-07.md) still needs its determinant calculation, difference-convexity inequality and counting chord bound.

For completeness, the continuous-outcome extension can be stated without an uncountable orthogonal-flag isometry. For a qubit POVM $M$, use its finite trace measure $\mu(S)=\operatorname{Tr}M(S)$, with $\mu(\Omega)=2$. Its positive matrix density admits spectral refinement into rows $m_j(x)$. For fixed input, define the branch probabilities relative to $\mu$ and replace each sum in the chord proof by $\int\sum_j\,d\mu(x)$. The determinant and Rayleigh bounds hold pointwise, and completeness gives $\int\sum_j p_j(x)r_j(x)\,d\mu(x)=1$. Qubit conditional entropies are bounded, so the integrals are well defined. Branches with zero probability contribute zero.

For predetermined measurements on different uses, the additivity difference is the contraction of total correlation from receiver outputs to complementary outputs. Both total correlations are finite by data processing from the finite-dimensional input. One may cancel the common classical correlation term using conditional entropies, without assigning a differential entropy to the outcome. General encoder ancillas are covered by the same conditional weak-monotonicity argument as in the direct proof.

Achievability uses the finite two-outcome counting measurement. Thus the exact equality needs no separate continuous-output coding theorem and no compactness argument. The earlier compactness proof remains a historical route to the qualitative gap, rather than a dependency of the stronger chord proof.

## 3. Optical identity and photon-budget coding

### Full Fock-space identity

Let $W(z)=\exp(z\hat a^\dagger-z^*\hat a)$. For the vacuum splitter,

```math
\mathcal N_{BD}^{*}[W(z)\otimes W(w)]
=\exp\!\left[-\frac{|z|^2+|w|^2-|\sqrt a\,z+\sqrt c\,w|^2}{2}\right]
W(\sqrt a\,z+\sqrt c\,w).
```

The attenuation channel obeys

```math
\mathcal L_t^{*}[W(z)]
=e^{-(1-t)|z|^2/2}W(\sqrt t\,z).
```

For $a\ge b$ and $a>0$, composing with $t=b/a$ replaces $a$ by $b$ in the first expression. Equality on the Weyl operators determines the normal channels, hence proves the joint-register identity on the entire Fock space and with arbitrary references. This includes non-Gaussian inputs and input coherences. Reversing $a,b$ gives the zero-capacity side; $a=b=0$ is handled directly.

### All-input converse and finite records

For total incident mean energy $n\bar N$, finite-energy output entropies and the thermal logarithm give

```math
D(\rho_{B^n}\Vert\tau_{a\bar N}^{\otimes n})
=n g(a\bar N)-S(B^n),
```

and the analogous identity for $E^n$. Relative-entropy contraction under product attenuation bounds their difference. Uniform energy allocation, Gaussianity and independent inputs are unnecessary. The cases $b=0$ and $\bar N=0$ use their direct vacuum/maximum-entropy forms.

The direct converse retains the unresolved helper register $G$ and discarded encoder register $F$. For a finite message reference $R$, its conditional entropies remain finite under the physical mean-energy bound. For a normal classical record on a standard Borel outcome space, the conditional averages of the normal cq state field over nested generating finite partitions converge to that field in integrated trace norm. The finite-reference conditional-entropy continuity bound then passes both cuts to the full record. See [CLAIM_ASSESSMENT](CLAIM_ASSESSMENT_2026-10-07.md) and [Winter, Lemma 2](https://arxiv.org/abs/1507.07775). No photon cutoff is imposed on competing codes.

### Energy-constrained achievability

Fix $N>0$ and photon cutoff $K$. For the normalized truncated thermal state $\tau_N^{(K)}$, set $r=N/(1+N)$ and $\epsilon_K=r^{K+1}$. Its mean is

```math
N_K=N-\frac{(K+1)\epsilon_K}{1-\epsilon_K}<N.
```

Next fix a helper block of $m$ modes and a finite-outcome assistance measurement. Restrict its flagged channel to $\mathcal H_K^{\otimes m}$ and use the input Hamiltonian

```math
H_{K,m}=\sum_{j=1}^{m}\hat n_j,
\qquad
\operatorname{Tr}[H_{K,m}(\tau_N^{(K)})^{\otimes m}]=mN_K<mN.
```

[Wilde–Qi, Theorem 2](https://arxiv.org/abs/1609.01997v2), applied to this fixed finite channel with budget $mN$, supplies energy-constrained codes achieving its coherent information. The finite input and output spaces satisfy its Gibbs and finite-output-entropy conditions. Divide the rate by $m$. The helper POVM can be extended outside the supported subspace by an additional outcome that never occurs for these codes. This explicitly supplies the energy constraint; it is not an inference that an arbitrary unconstrained code happens to meet it.

Take the coding limit while $K,m$ are fixed. Only afterward increase $K$, choosing a suitable finite $m$ for each cutoff. To check the entropy limit, let $H_s^{(K)}=S(\mathcal L_s(\tau_N^{(K)}))$. The discarded thermal component has conditional mean $K+1+N$, so entropy concavity and the entropy-of-mixture upper bound give

```math
\frac{g(sN)-h_2(\epsilon_K)-\epsilon_Kg(s(K+1+N))}{1-\epsilon_K}
\le H_s^{(K)}\le\frac{g(sN)}{1-\epsilon_K}.
```

The geometric tail makes both bounds tend to $g(sN)$. At finite $K$, retain the full minimum $\min\{H_a^{(K)},H_{1-b}^{(K)}\}$; no entropy ordering for truncated inputs is assumed. In the thermal limit, $g((1-b)N)\ge g(aN)$, giving the stated optical rate. Thermal refers to the average coded input; the environmental inputs stay vacuum.

## 4. Boundary cases and the zero-side fidelity bound

For the qubit family with $a>b$, the left scalar branch has

```math
\frac{d^2}{dq^2}[h_2(aq)-h_2(bq)]
=\frac{b-a}{\ln2\,q(1-aq)(1-bq)}<0.
```

For $q\ge q_c=1/(1+a-b)$, $(1-b)q\ge1/2$ and $bq<1/2$, so the right branch is nonincreasing. This verifies the crossover/unique-root rule, including $b=0$ by limits. At $c=0$ the two cuts are identical. At $a=b=0,c=1$, the receiver has a fixed quantum state plus a classical record and zero quantum capacity; no attenuation ratio is used.

For $a\le b$, reverse joint attenuation constructs a second receiver with the same reference marginal, even for coarse records and general encoders. Applying the same outcome-dependent decoder to both gives equal logical marginals. For a maximally entangled $d$-dimensional logical input, the two maximally entangled projectors satisfy $\|P+Q\|_\infty=1+1/d$, hence

```math
2F_e\le1+1/d.
```

This bounds unconditional entanglement fidelity, with every measurement outcome included. It is neither a postselected success bound nor a strong converse forcing fidelity to zero.

For the optical model, $N=0$ always gives zero capacity. For $R>0$ and $0<a<1$, the target rate is attainable at some finite energy exactly when $b<a2^{-R}$. Equality with $b>0$ reaches the target only as an infinite-energy limit. At $b=0$, every finite target is attainable. These are consequences of the existing energy law, not further capacity theorems.

## 5. Primary-source checks and the stopping boundary

| Source | Passages inspected and consequence |
|---|---|
| [Leditzky–Datta–Smith, 1701.03081v4](https://arxiv.org/pdf/1701.03081v4) | Eqs. (2.1)–(2.4), Definition 2.2, Proposition 2.4 and complete proof, printed pp. 5–8; Proposition 2.7, Theorem 2.8 and Proposition 2.9. Supplies both finite-dimensional cuts through the explicit regrouping above; its decomposition minimum does not settle the helper maximum. |
| [Ahmed–Smith–Wu, 2603.23417](https://arxiv.org/pdf/2603.23417) | Definitions II.2/III.1, Eq. (17), Propositions III.2–III.3 and relevant proofs. Led to the older state theorem; the attribution belongs to that older result. The weaker state conditions do not order helper measurements. |
| [Tang–Zhu–Bai–Wang, 2609.28592](https://arxiv.org/pdf/2609.28592) | Theorems 4.1–4.2, Proposition 6.4 and proof, Appendix B. Formation-cost minimization and classical-capacity additivity do not give the shared entropy-difference maximum; ordinary entropy-function convexity is insufficient. |
| [Relaying Quantum Information, 2507.06770v2](https://arxiv.org/pdf/2507.06770v2) | Operational definition, Theorems 2–4, Remarks 2–3 and Appendix C reductions. An active causal relay and achievable bounds do not supply the present measurement optimization. |
| [Wilde–Qi, 1609.01997v2](https://arxiv.org/pdf/1609.01997v2) | Theorem 2 and its coding proof; Theorem 6 and its thermal-reference proof. These support the fixed-$K,m$ energy-constrained coding step and inherited entropy method. |
| [Winter, 1507.07775](https://arxiv.org/pdf/1507.07775) | Lemma 2 and proof. Its finite-reference continuity bound controls passage from finite partitions to the full classical record. |

These are targeted primary-text checks, not exhaustive priority clearance or independent peer review. The analytical rederivation found no rate correction. The material change is the converse attribution, together with the explicit coding and measurable-limit details above. All 23 original diagnostic groups and the separate rational scalar certificate remain distinct from these analytical arguments.

The fixed claim package has no identified unresolved mathematical prerequisite. Adaptive-helper capacity, optical product optimality, finite-block constructions, bounded helper resources and nonvacuum environments are outside it. Further work should present the existing claims with these dependencies and boundaries, reopening research only for a concrete proof or source objection.
