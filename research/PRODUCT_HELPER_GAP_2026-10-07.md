# Product-helper capacity reduction

The product benchmark permits every single-use helper POVM, including continuous
outcomes, chosen in advance and allowed to vary across uses. Sender and receiver
retain arbitrary block codes; the helper sends only a classical record to the receiver.
All outcomes contribute to unconditional transmission error. The qubit regime is
$`a+b+c=1,\ a>b>0,\ c>0`$.

## 1. The correct product capacity optimization

Refining a single-use POVM into rank-one effects gives the receiver additional classical information, which it can ignore. Write the refined rows as $m_x$, with $\sum_xm_x^\dagger m_x=I_D$, and let

```math
W_x=(I_{BE}\otimes m_x)V,\qquad
\mathcal N_M(\rho)=\sum_x\mathrm{Tr}_E(W_x\rho W_x^\dagger)\otimes|x\rangle\langle x|.
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

These inequalities give the product-helper converse as a supremum of the single-use
coherent information. The [exact product proof](EXACT_PRODUCT_CAPACITY_2026-10-07.md)
bounds that supremum by the counting maximum and attains it with a finite two-outcome
POVM and diagonal input. Repeating counting and applying ordinary degradable-channel
coding gives achievability. Thus

```math
Q_{\rm prod}=\sup_{\rho,M}I_c(\rho,\mathcal N_M)
=Q_{\rm count}=\max_{0\le q\le1}F(q).
```

Outcome-adaptive local measurements and general separable block POVMs are outside this
benchmark. Both rates in the individual-versus-collective comparison allow arbitrary
sender/receiver block codes.

## Sources and the earlier qualitative route

[Devetak–Shor, quant-ph/0311131](https://arxiv.org/pdf/quant-ph/0311131), Appendix B,
Eq. (18) and its proof, supplies degradable-channel capacity and additivity. Those
primary passages were inspected; the product inequality is also derived above.
The [dependency record](PROOF_DEPENDENCIES.md#2-why-this-does-not-settle-the-product-measurement-optimum)
specifies the finite trace-measure formulation and continuous-record argument.

The [archived qualitative proof](../archive/editorial/2026-10-07-pre-release/research/PRODUCT_HELPER_GAP_2026-10-07.md)
retains the preceding compactness and strict-contraction argument, its source-reading
depths and its historical open questions. The exact chord proof gives the stronger
counting optimum without those compactness or equality-recovery steps.
