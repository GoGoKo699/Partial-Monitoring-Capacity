# Prior-work comparison: the capacity implication

This source comparison checks the operational equality in
[THEOREM](../research/THEOREM.md). Leditzky–Datta–Smith, Definition 2.2 and
Proposition 2.4, supply both finite-dimensional converse cuts by regrouping
registers, as derived in [PROOF_DEPENDENCIES](../research/PROOF_DEPENDENCIES.md).
The [source ledger](PRIOR_ART.md) identifies the supporting passages and the scope of each comparison.

## Exact comparison target

The degradable-state reduction supplies the converse mechanism for the implication

```math
\mathcal N_{ED}=(\mathcal T_{B\to E}\otimes\mathrm{id}_D)\mathcal N_{BD}
\quad\Longrightarrow\quad
Q_{\rm meas}=\max_{\rho_A}\min\{S(B)-S(E),S(BD)-S(E)\}.
```

Here the helper receives the channel output $`D`$, may process it collectively, and sends only a classical outcome to the receiver $`B`$. The environment $`E`$ remains inaccessible. Neither preshared entanglement nor a coherent helper link is supplied. The operational equality includes optimization over collective helper measurements and correlated channel inputs.

[Leditzky–Datta–Smith, 1701.03081v4](https://arxiv.org/pdf/1701.03081v4), Eqs. (2.1)–(2.4), Definition 2.2 and Proposition 2.4 with its proof, provide the state-converse result. The register groupings $`RFD^n:B^n`$ and $`RF:B^nD^n`$ give the two block bounds for arbitrary encoded inputs. Common-input averaging and the assistance construction complete the capacity consequence. Symmetric-side-channel methods provide a related entropy-contraction argument, and partial environmental observation has direct conceptual predecessors.

## Related primary-source results

| Primary source | Passages supporting the comparison | Resource and theorem relation |
|---|---|---|
| Smith, Smolin and Winter, *The quantum capacity with symmetric side channels*, [arXiv:quant-ph/0607039](https://arxiv.org/pdf/quant-ph/0607039) | Section III.B, operational definition and Eq. (23); Theorem 6 and Eq. (33), PDF pages 4 and 6. | Theorem 6 says symmetric side channels do not improve a degradable channel's quantum capacity. The assistance channel is sender-controlled. Its proof provides an entropy-contraction precedent. Applying it to $`\mathcal N_B`$ requires the actual complement $`ED`$, not $`E`$. Applying it to $`\mathcal N_{BD}`$ gives the coherent-delivery cut; applying it after a fixed helper measurement leaves measurement optimization unresolved. |
| Pereg, Deppe and Boche, *Quantum Broadcast Channels with Cooperating Decoders*, [arXiv:2011.09233](https://arxiv.org/pdf/2011.09233) | Section III.C and Figure 3 caption; Definition 6; Theorem 5, Eqs. (42)–(44), PDF pages 14–16 and 23–24. | The quantum-communication setting uses preshared decoder entanglement to turn classical conferencing into a coherent qubit pipe. Theorem 5 supplies regularized cutset and achievable bounds for that resource. Setting the quantum conferencing rate to zero does not preserve an unrestricted classical measurement-helper resource. These bounds do not give the first cut under joint-register degradation. |
| Dutil and Hayden, *Assisted Entanglement Distillation*, [arXiv:1011.1972](https://arxiv.org/pdf/1011.1972) | Figure 2 caption and operational description; Propositions 5–6; Theorem 8 and opening proof, PDF pages 5 and 9–11. | Theorem 8 gives the mixed-state assistance minimum-cut lower bound. The task broadcasts the helper outcome to both recipients and allows recipient LOCC. These upper bounds do not establish the degrading-condition converse. Receiver-only channel achievability uses the fixed flagged-channel construction described in [THEOREM](../research/THEOREM.md). |
| Memarzadeh, Macchiavello and Mancini, *Recovering quantum information through partial access to the environment*, [arXiv:1101.3768](https://arxiv.org/pdf/1101.3768) | Abstract, introduction, Section II opening setup and conclusions; capacity discussion. This comparison concerns the operational setup, not a derivation of the full recovery optimization. | A direct conceptual precedent for partial environmental observation. The recovery objective is entanglement fidelity for correlated qubit errors using one environmental subsystem, including dependence on system size. This differs from memoryless transmission capacity under the joint-register condition. |

## Relation to the product benchmark

The capacity equality is a synthesis of assistance and degradable-state results under the stated communication resources. The exact product-measurement maximum requires an additional optimization: it bounds a shared branch-entropy difference over physically allowed helper measurements. The state-decomposition minima in the degradable-state literature optimize a different quantity.

The [exact product proof](../research/EXACT_PRODUCT_CAPACITY_2026-10-07.md) gives that maximum for predetermined qubit helper measurements. The [dependency record](../research/PROOF_DEPENDENCIES.md) supplies the register reduction and further source comparisons; the [model map](../research/MODEL_AND_CLAIMS.md) fixes the operational scope.
