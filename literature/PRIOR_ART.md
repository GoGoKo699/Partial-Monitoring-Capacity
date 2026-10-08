# Prior-art comparison at the theorem boundary

The assistance and coding ingredients are established. Both finite-dimensional
converse cuts follow from Leditzky–Datta–Smith through the
[register reduction](../research/PROOF_DEPENDENCIES.md); the
[exact product optimum](../research/EXACT_PRODUCT_CAPACITY_2026-10-07.md)
requires the separate entropy-difference and chord argument. The
[targeted comparison](PRIORITY_CHECK_2026-10-07.md) and
[contribution assessment](../research/CONTRIBUTION_ASSESSMENT_2026-10-07.md)
map these ingredients to the communication resources. The comparisons below are
limited to the stated primary-source passages.

## Proof ingredients

**Leditzky–Datta–Smith, [Useful states and entanglement distillation](https://arxiv.org/abs/1701.03081v4).** Definition 2.2 and Proposition 2.4, including its proof, give the one-way distillation quantity for degradable states. The [register reduction](../research/PROOF_DEPENDENCIES.md) applies this result to both finite-dimensional converse cuts. The state-decomposition minimum in Theorem 2.8 does not optimize the helper's shared branch-entropy difference.

**Smolin–Verstraete–Winter, [Entanglement of assistance and multipartite state distillation](https://arxiv.org/abs/quant-ph/0505038), Theorems 1 and 8.** The pure-state assistance theorem supplies a helper measurement with the required average branch entropy. Theorem 8 and its proof turn a chosen environment measurement into a channel with a classical outcome register and apply ordinary quantum coding. Figure 1 sends the record only to the receiver, so receiver-only signaling is an established resource. The present channel additionally leaves an output $`E`$ inaccessible. Its converse uses the degradable-state reduction; its product-measurement optimum requires a separate argument.

**Dutil–Hayden, [Assisted Entanglement Distillation](https://arxiv.org/abs/1011.1972), Theorem 8.** The theorem gives the assistance lower bound

```math
\max\{I(A\rangle B),\min[I(AC\rangle B),I(A\rangle BC)]\}.
```

Its operational definition and theorem/proof text allow entanglement distillation between two recipients after the helper acts. The present channel construction uses an assistance ensemble and a fixed measured channel; it supplies no sender–receiver distillation link.

**Wilde–Qi, [Energy-constrained private and quantum capacities of quantum channels](https://arxiv.org/abs/1609.01997v2), Theorems 2 and 6.** The coding theorem and thermal-reference proof support energy-constrained achievability and the optical entropy method. Their channel and complement assumptions require care here: $`E`$ is not the full complement of $`B`$, because $`D`$ is a separate output. The joint-register converse establishes the needed bound, and coding applies to a fixed flagged channel at finite photon cutoff and helper block length. [PROOF_DEPENDENCIES](../research/PROOF_DEPENDENCIES.md#3-optical-identity-and-photon-budget-coding) gives these applications.

## Related resources and results

| Source | Basis of comparison | Relation to this model |
|---|---|---|
| Buscemi–Datta, [General theory of environment-assisted entanglement distillation](https://arxiv.org/abs/1009.4464) | Abstract, introduction and operational definition around PDF page 10; not the complete one-shot bounds. | The helper holds the full purification. This operational scope differs from assistance with an inaccessible residual output. |
| Grassl–Ji–Wei–Zeng, [Quantum Capacity Approaching Codes for the Detected-Jump Channel](https://arxiv.org/abs/1008.3350), PRA 82, 062324 | Primary bibliographic metadata and abstract. | A detected-jump coding precedent. The separate [product-measurement comparison](../research/CONTRIBUTION_ASSESSMENT_2026-10-07.md) identifies the fixed-basis capacity result and its relation to optimization over helper POVMs. |
| Devetak–Shor, [The capacity of a quantum channel for simultaneous transmission of classical and quantum information](https://arxiv.org/abs/quant-ph/0311131) | Appendix B, Eq. (18) and its proof, as specified in the [product reduction](../research/PRODUCT_HELPER_GAP_2026-10-07.md). | Supplies degradable-channel capacity and additivity. The product reduction also derives the particular total-correlation inequality; the encoder-ancilla argument is explicit in [PROOF_AUDIT](../research/PROOF_AUDIT.md). |
| Gregoratti–Werner, [Quantum Lost and Found](https://arxiv.org/abs/quant-ph/0209025) | Abstract and primary bibliographic metadata. | Environment-assisted correction provides the context for the random-phase control in [THEOREM](../research/THEOREM.md). The displayed countercontrol, rather than a further claim about the source's proof, shows why marginal degradability is insufficient. |
| Oskouei–Mancini–Winter, [Capacities of Gaussian quantum channels with passive environment assistance](https://arxiv.org/abs/2101.00602) | Primary abstract. | The helper sets the incoming environment state. This differs from measuring only the collected output of a vacuum splitter. |

## Contribution boundary

The capacity formula combines established assistance, degradable-state converse and coding ingredients under the joint-register hypothesis. The exact product benchmark separately optimizes the branch-entropy difference over every predetermined individual helper POVM and every qubit input in its stated domain.

The [resource comparison](PRIORITY_CHECK_2026-10-07.md) covers symmetric side channels, cooperating decoders and partial-access recovery. These source-specific comparisons do not establish exhaustive priority. The results specify asymptotic capacities with unrestricted helper processing; an efficient collective receiver is a separate constructive question.
