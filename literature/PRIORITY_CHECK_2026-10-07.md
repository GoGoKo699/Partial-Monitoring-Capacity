# Targeted priority assessment: the central implication

**Updated 7 October 2026.** This bounded author-side comparison checks whether an existing theorem directly implies the equality in [THEOREM](../research/THEOREM.md). The subsequent [dependency audit](../research/PROOF_DEPENDENCIES.md) corrects its initial attribution: Leditzky–Datta–Smith, Definition 2.2 and Proposition 2.4, supplies both finite-dimensional converse cuts by regrouping registers. It supplements the preserved [prior-art ledger](PRIOR_ART.md), without certifying exhaustive priority.

## Verdict and exact comparison target

The initial four-source comparison below did not identify a covering theorem. The later degradable-state reduction now supplies the converse mechanism for the implication

```math
\mathcal N_{ED}=(\mathcal T_{B\to E}\otimes\mathrm{id}_D)\mathcal N_{BD}
\quad\Longrightarrow\quad
Q_{\rm meas}=\max_{\rho_A}\min\{S(B)-S(E),S(BD)-S(E)\}.
```

Here the helper receives the channel output $D$, may process it collectively, and sends only a classical outcome to the receiver $B$. The environment $E$ remains inaccessible. Neither preshared entanglement nor a coherent helper link is supplied. A covering result must recover this operational equality, including the optimization over collective measurements and correlated channel inputs.

The decisive additional source is [Leditzky–Datta–Smith, 1701.03081v4](https://arxiv.org/pdf/1701.03081v4), Eqs. (2.1)–(2.4), Definition 2.2 and Proposition 2.4 with its proof. The register groupings $RFD^n:B^n$ and $RF:B^nD^n$ give the two block bounds for arbitrary encoded inputs. Common-input averaging and the inherited assistance construction complete the capacity consequence. The symmetric-side-channel result remains a technique precedent. Partial environmental observation itself also has clear predecessors.

## Earlier primary-source comparison

| Candidate and primary source | Actual reading depth in this pass | Coverage and missing implication |
|---|---|---|
| Smith, Smolin and Winter, *The quantum capacity with symmetric side channels*, [arXiv:quant-ph/0607039](https://arxiv.org/pdf/quant-ph/0607039) | Section III.B, operational definition and Eq. (23); Theorem 6 and Eq. (33), PDF pages 4 and 6. Parsed primary text. | Theorem 6 says symmetric side channels do not improve a degradable channel's quantum capacity. The assistance channel is sender-controlled. Its proof provides a close entropy-contraction precedent. Applying it to $\mathcal N_B$ requires the actual complement $ED$, not $E$. Applying it to $\mathcal N_{BD}$ gives the coherent-delivery cut; applying it after a fixed helper measurement leaves measurement optimization unresolved. |
| Pereg, Deppe and Boche, *Quantum Broadcast Channels with Cooperating Decoders*, [arXiv:2011.09233](https://arxiv.org/pdf/2011.09233) | Section III.C and Figure 3 caption; Definition 6; Theorem 5, Eqs. (42)–(44), PDF pages 14–16 and 23–24. Parsed text, not a rendered-figure inspection. | The quantum-communication setting uses preshared decoder entanglement to turn classical conferencing into a coherent qubit pipe. Theorem 5 supplies regularized cutset and achievable bounds for that resource. Setting the quantum conferencing rate to zero does not preserve an unrestricted classical measurement-helper resource. The inspected result supplies no matching first cut under joint-register degradation. |
| Dutil and Hayden, *Assisted Entanglement Distillation*, [arXiv:1011.1972](https://arxiv.org/pdf/1011.1972) | Figure 2 caption and operational description; Propositions 5–6; Theorem 8 and opening proof, PDF pages 5 and 9–11. Parsed primary text. | Theorem 8 is the inherited mixed-state assistance minimum-cut lower bound. The task broadcasts the helper outcome to both recipients and allows recipient LOCC. The inspected upper bounds do not establish the present degrading-condition converse. Receiver-only channel achievability still requires the fixed flagged-channel construction described in the theorem. |
| Memarzadeh, Macchiavello and Mancini, *Recovering quantum information through partial access to the environment*, [arXiv:1101.3768](https://arxiv.org/pdf/1101.3768) | Abstract, introduction, Section II opening setup and conclusions; inspected capacity mentions. Parsed primary text. The full recovery optimization was not reproduced. | A direct conceptual precedent for partial environmental observation. The inspected result optimizes recovery entanglement fidelity for correlated qubit errors using observation of one environmental subsystem, including dependence on system size. It does not state the memoryless transmission-capacity equality under the present joint-register condition. |

## What this establishes

The required resource bookkeeping is real, but the register reduction shows that it does not require an independently new finite-dimensional converse inequality. The revised capacity attribution is a synthesis of known assistance and degradable-state results. The exact product-measurement maximum remains separate; the state-decomposition minima inspected in the later audit do not supply it.

The search used both available search engines and targeted recent results as well as the established anchors. Search coverage remains incomplete. No failed retrieval, absent keyword, or different title is treated as novelty evidence. No independent theoretical review is claimed.

The [dependency record](../research/PROOF_DEPENDENCIES.md) contains the correction, later primary-source reading depths and bounded stopping conclusion. The next task is in [CURRENT](../work_orders/CURRENT.md). Additional numerical checks are not evidence of priority.
