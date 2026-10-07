# A strict gap for predetermined product helper measurements

**7 October 2026. Author-side analytical result.** This resolves the bounded resource question for the existing qubit example. It supplements [THEOREM](THEOREM.md), without changing its capacity formula or communication resources. It is not independent scientific review.

**Subsequent result:** [EXACT_PRODUCT_CAPACITY](EXACT_PRODUCT_CAPACITY_2026-10-07.md) proves that counting is optimal over this entire product class and certifies the gap's size. The qualitative proof below remains valid; its original unresolved questions at the end record the earlier pass.

## Statement and scope

For the qubit isometry

```math
|0\rangle\mapsto|000\rangle_{BED},\qquad
|1\rangle\mapsto\sqrt a|100\rangle+\sqrt b|010\rangle+\sqrt c|001\rangle,
```

fix $(a,b,c)=(1/5,2/25,18/25)$. Define $Q_{\rm prod}$ by restricting the helper to a product of single-use POVMs chosen in advance. The POVMs may differ between uses and between code lengths; all single-use POVMs are allowed, including continuous outcomes. The sender and receiver retain arbitrary block encoding and decoding. The helper sends its record only to the receiver, with every outcome included in the transmission error.

**Proposition.** There is a strictly positive, unquantified $\delta$ such that

```math
Q_{\rm prod}=Q_{\rm meas}-\delta
<Q_{\rm meas}
=h_2(5/28)-h_2(1/14)\simeq0.30570954.
```

Photon counting supplies the previously evaluated lower bound $Q_{\rm prod}\ge Q_{\rm count}\simeq0.18621044$. The proof does **not** identify counting as optimal or identify $0.30570954-0.18621044$ as the product-measurement gap. It excludes arbitrarily close attainment by the entire stipulated product class, not just equality for each particular measurement.

Outcome-adaptive choices of later helper measurements and general separable block POVMs are outside this benchmark. Thus the conclusion is a strict advantage of unrestricted helper measurements over predetermined product measurements; it is not a theorem that coherent helper storage is necessary against every adaptive local strategy.

## 1. The correct product capacity optimization

Refining a single-use POVM into rank-one effects gives the receiver additional classical information, which it can ignore. Write the refined rows as $m_x$, with $\sum_xm_x^\dagger m_x=I_D$, and let

```math
W_x=(I_{BE}\otimes m_x)V,\qquad
\mathcal N_M(\rho)=\sum_x\operatorname{Tr}_E(W_x\rho W_x^\dagger)\otimes|x\rangle\langle x|.
```

A complementary output is $EY$, with the same classical flag. The joint-register identity gives the degrading map $\mathcal A_{b/a}\otimes\mathrm{id}_{X\to Y}$, where $\mathcal A_t$ denotes amplitude damping with survival $t$. Therefore every refined measured channel is degradable and

```math
I_c(\rho,\mathcal N_M)=\sum_xp_x[S(B_x)-S(E_x)].
```

The input $\rho$ here is an arbitrary qubit density matrix. No diagonal-input assumption is made for a fixed POVM.

For different predetermined measurements $M_1,\ldots,M_n$, degradability gives

```math
I_c\!\left(\rho_{A^n},\bigotimes_i\mathcal N_{M_i}\right)
\le\sum_i I_c(\rho_{A_i},\mathcal N_{M_i}).
```

To see the inequality, put $O_i=B_iX_i$ and $C_i=E_iY_i$. The difference between the right and left sides is $T(O_1:\cdots:O_n)-T(C_1:\cdots:C_n)\ge0$, where $T$ is total correlation, the relative entropy to the product of the marginals. The local degrading maps imply its contraction. The arbitrary-encoder converse in THEOREM, Section 2, also applies: discarding an encoder ancilla cannot increase the relevant coherent information for these degradable channels. Hence correlated inputs and general encoders do not evade this bound.

For continuous records, use conditional cq entropies for the displayed coherent information and relative entropy for $T$. Both output total correlations are finite because data processing bounds them by the total correlation of the finite-dimensional input. No differential entropy is subtracted. A general qubit POVM has a positive matrix density relative to its finite trace measure; spectral refinement supplies rank-one densities.

It follows that the product capacity is the supremum of the single-use expression. Section 2 shows this supremum is attained by a finite POVM; repeating that measurement and applying ordinary degradable-channel coding [DS05] gives the reverse inequality. Thus

```math
Q_{\rm prod}=\max_{\rho,M\ {\rm rank\ one}} I_c(\rho,\mathcal N_M).
```

## 2. Compactness: at most five outcomes suffice

For fixed $\rho$, write each effect as $wP(\mathbf n)$, with $P(\mathbf n)=(I+\mathbf n\cdot\boldsymbol\sigma)/2$ and $\mathbf n\in S^2$. Completeness is

```math
\sum_x w_x=2,\qquad \sum_xw_x\mathbf n_x=0.
```

Let $k_\rho(\mathbf n)$ be the unnormalized coherent-information contribution from the unit-trace effect $P(\mathbf n)$. Its contribution at weight $w$ is $wk_\rho(\mathbf n)$. This function is continuous jointly in $\rho,\mathbf n$: if the outcome probability tends to zero, the contribution tends to zero since $|p[S(B)-S(E)]|\le p$ for qubits.

The normalized weights $w_x/2$ define a probability measure. Its three Bloch moments and payoff form a point in the convex hull of

```math
\{(\mathbf n,k_\rho(\mathbf n)):\mathbf n\in S^2\}\subset\mathbb R^4.
```

This set is compact. Carathéodory's theorem reproduces that point with at most five elements, preserving completeness and the payoff for this input. The argument includes continuous POVMs; it does not assert that their entire measured channels are identical.

Consequently it suffices to optimize over five weights, five unit Bloch vectors and the input density matrix, subject to the closed completeness constraints. Allow zero weights. This is a compact domain and the objective is continuous, so its maximum exists. Five is a sufficient bound; no minimal-outcome claim is needed.

## 3. Strict entropy contraction and the unique unrestricted input

The linear action of $\mathcal A_t$ on differences of qubit Bloch vectors is $\operatorname{diag}(\sqrt t,\sqrt t,t)$. For $0<t<1$,

```math
\|\mathcal A_t(\omega)-\mathcal A_t(\sigma)\|_1
\le\sqrt t\,\|\omega-\sigma\|_1.
```

If equality held in relative-entropy data processing for two distinct states with finite relative entropy, Petz's equality theorem would provide a channel recovering both. Trace-norm contraction by that recovery would contradict the strict inequality above. The equality theorem and its ensemble consequence are stated in [HJPW04], Theorem 3 and Example 4. Therefore, for a nonconstant ensemble with full-rank average,

```math
\chi(\{p_x,\omega_x\})-
\chi(\{p_x,\mathcal A_t(\omega_x)\})>0.
```

For $s=a$ or $s=1-b$, define $D_s(\rho)=S(\mathcal A_s\rho)-S(\mathcal A_b\rho)$. The two cuts in THEOREM are exactly these functions: the $BD$ output is an isometric embedding of $\mathcal A_{1-b}\rho$, with excited vector $(\sqrt a|10\rangle+\sqrt c|01\rangle)/\sqrt{1-b}$.

Each $D_s$ is strictly concave. Its concavity difference for two distinct inputs is the Holevo loss under $\mathcal A_{b/s}$. The preceding lemma applies because $0<b/s<1$, $\mathcal A_s$ is injective, and the average of two distinct qubit states has full rank. Thus

```math
f(\rho)=\min\{D_a(\rho),D_{1-b}(\rho)\}
```

is strictly concave too. Both cuts are phase invariant, so averaging opposite input phases strictly improves any input with nonzero coherence. The unrestricted maximizer is uniquely diagonal.

The established scalar crossover is $q_*=1/(1+a-b)=25/28$. On its left the active cut is $h_2(aq)-h_2(bq)$; on its right it is $h_2((1-b)q)-h_2(bq)$. Their one-sided derivatives at $q_*$ are

```math
f'_-(q_*)=\frac1{25}\log_2\frac{(23/5)^5}{13^2}>0,
\qquad
f'_+(q_*)=-\frac{23}{25}\log_2\frac{23}{5}-\frac2{25}\log_2 13<0.
```

Concavity of each cut establishes the unique maximum

```math
\rho_*=\operatorname{diag}(3/28,25/28),\qquad
D_a(\rho_*)=D_{1-b}(\rho_*)=Q_{\rm meas}.
```

This symmetry argument concerns the unrestricted upper bound $f$, not the input optimization for an arbitrary measured channel.

## 4. No rank-one helper measurement can saturate at that input

For diagonal input with excitation probability $q=q_*$ and a nonzero row $m=(u,v)$, the unnormalized conditional receiver state $\sigma_B$ obeys

```math
p=(1-cq)|u|^2+cq|v|^2,\qquad
(\sigma_B)_{11}=aq|u|^2,\qquad
(\sigma_B)_{01}=q\sqrt{ac}\,vu^*.
```

The average receiver state is $\bar B=\operatorname{diag}(1-aq,aq)$. Suppose $\sigma_B=p\bar B$. Its excited population requires $p=|u|^2$, while its off-diagonal entry requires $vu^*=0$. If $u=0$, then $p=cq|v|^2>0$, contradicting $p=|u|^2$. If $u\ne0$, then $v=0$ and $p=(1-cq)|u|^2\ne|u|^2$. Thus no nonzero rank-one outcome has $B_x=\bar B$.

The receiver ensemble is therefore nonconstant. Since $E_x=\mathcal A_{b/a}(B_x)$, strict Holevo contraction gives

```math
I_c(\rho_*,\mathcal N_M)
=D_a(\rho_*)-[I(X;B)-I(X;E)]
<Q_{\rm meas}
```

for every finite rank-one POVM. For any other input, the common-cut bound already gives $I_c(\rho,\mathcal N_M)\le f(\rho)<Q_{\rm meas}$. The joint input/POVM maximum exists by Section 2 and hence is strictly smaller than $Q_{\rm meas}$. This proves the proposition, including the uniform gap over use-varying predetermined product measurements.

## Original conclusion and next task (now completed)

Collective gains in assistance are established [SVW05, Section III, Example 4]. That paper's Theorem 8 also supplies the fixed-block-measurement coding construction. [DJ10, concluding paragraph] expressly compares fixed-basis detected-jump capacity with unrestricted environment-assisted amplitude damping. Neither inspected passage optimizes all product POVMs with the present residual inaccessible output. The additional result here is the stated separation at $b=0.08$, despite unrestricted sender/receiver block coding. This targeted comparison is not exhaustive priority clearance.

The proof is qualitative. The exact product capacity, a numerical lower bound on $\delta$, an optimal product POVM and the outcome-adaptive benchmark remain undetermined. The original 23 numerical check groups reproduce the previously established identities and rates; they are not a numerical certificate for the new compactness or strictness argument. No new numerical optimization is used as proof.

The next bounded task is to obtain a certified numerical upper bound on $Q_{\rm prod}$ in this same example, using the finite optimization above or a stronger analytical inequality. A local optimizer alone cannot provide that certificate. Do not broaden the model to pursue it.

## Primary sources and reading depth

- [HJPW04] P. Hayden, R. Jozsa, D. Petz and A. Winter, *Structure of states which satisfy strong subadditivity of quantum entropy with equality*, [arXiv:quant-ph/0304007](https://arxiv.org/pdf/quant-ph/0304007). Theorem 3 and Example 4, PDF pages 3–4: recovery characterization of equality and the Holevo consequence. Parsed primary text inspected.
- [DS05] I. Devetak and P. W. Shor, *The capacity of a quantum channel for simultaneous transmission of classical and quantum information*, [arXiv:quant-ph/0311131](https://arxiv.org/pdf/quant-ph/0311131). Appendix B, Eq. (18) and its proof, PDF page 13: degradable-channel capacity/additivity. Parsed primary text inspected; the product inequality used above is also derived directly.
- [SVW05] J. A. Smolin, F. Verstraete and A. Winter, *Entanglement of assistance and multipartite state distillation*, [arXiv:quant-ph/0505038](https://arxiv.org/pdf/quant-ph/0505038). Section III, Example 4 and Section IV, Theorem 8/proof, PDF pages 3 and 5: explicit assistance superadditivity and measured-channel coding. These passages were reread in parsed primary text.
- [DJ10] M. Grassl, Z. Ji, Z. Wei and B. Zeng, *Quantum Capacity Approaching Codes for the Detected-Jump Channel*, [arXiv:1008.3350](https://arxiv.org/pdf/1008.3350). Eqs. (5)–(8), (16) and concluding paragraph, PDF pages 2–4: fixed detected-jump channel and its capacity comparison. This reading does not reproduce the code construction.
