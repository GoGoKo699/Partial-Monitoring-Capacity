# Model, claim hierarchy and proof dependencies

**Repository import, 7 October 2026.** This maps the supplied 6 October consolidation; it adds no scientific result.

## Fixed communication resource

A memoryless isometry divides the input among receiver $B$, inaccessible field $E$ and helper field $D$. The encoder is predetermined and may use many inputs; the helper may jointly measure arbitrarily many $D$ outputs and sends the classical outcome only to the receiver. The decoder uses $B^n$ and that outcome. Unknown messages are not supplied to the helper. General encoders, including a discarded ancillary system, are included.

No preshared entanglement, coherent helper-to-receiver link, sender/receiver feedback, intermediate control, postselection or free two-way distillation is supplied. Helper quantum memory, collective circuit complexity, phase references and classical message length are unrestricted. Rank-one refinement is a proof reduction; a coarsened record can leave an additional unobserved quantum register in the complement.

The capacity is asymptotic entanglement transmission per original input. It is not a finite-code fidelity, average survival probability, secret-key capacity, or corrected-memory lifetime. An efficient helper receiver is an open constructive problem, not an uncounted premise.

## Central theorem and its two evaluations

| ID | Author-side statement | Proof route | Diagnostic suite |
|---|---|---|---|
| C1 | The joint-register degrading identity makes the minimum-cut assistance lower bound exact. | [THEOREM](THEOREM.md), Sections 1–2. | consolidation; qubit |
| C2 | Qubit splitting has an exact single-variable rate and positive capacity exactly when survival exceeds unobserved decay. | THEOREM, Section 3; [original rate excerpt](../archive/excerpts/QUANTUM_RATE.md). | threshold; qubit |
| C3 | Vacuum optical splitting has capacity $g(aN)-g(bN)$ when $a>b$, and zero otherwise, under an average incident-energy constraint. | THEOREM, Section 4; [OPTICAL_AUDIT](OPTICAL_AUDIT.md), Section 4. | optical |
| C4 | The optical rate deficit separates unused energy, thermal-reference contraction deficit and measurement deficit. | THEOREM, Section 5; [PROOF_AUDIT](PROOF_AUDIT.md). | consolidation |
| C5 | Antidegradability gives $F_e\le(d+1)/(2d)$ for a $d$-dimensional logical message on the zero-capacity side. | [rate excerpt](../archive/excerpts/QUANTUM_RATE.md), Section A3. | qubit |

C2 and C3 are evaluations of one capacity principle, not unrelated new projects. The threshold is not an assertion that the channel becomes entanglement-breaking. The fidelity ceiling is unconditional and is not the same metric as average state fidelity.

## Dependencies that must remain visible

**Joint simulation.** The map from $B$ to $E$ must leave $D$ and its correlations unchanged. A map reproducing only the inaccessible marginal is insufficient. The random-phase example in the supplied audit is a countercontrol, not a counterexample to the stated hypothesis.

**Refined complement.** The measured channel has output $BX$ and a complementary output $EY$ with a copy of the classical outcome. Degradability applies to every refined block measurement. Deleting a record without changing the complement invalidates the coherent-information expression.

**Two cuts and single-letterization.** The two upper bounds, concavity and many-use subadditivity must use the same input density matrix after marginal averaging. General encoding ancillas are covered by the explicit conditional-entropy argument, not a restriction to an isometric encoder.

**Achievability.** The assistance ensemble theorem selects a measurement on $D$. Grouping the inaccessible field with a mathematical reference does not grant access to either. Freeze the block measurement and use ordinary quantum coding over the resulting channel with a classical flag. No encoder-side outcome or two-way distillation is added.

**Optical limit.** The converse includes arbitrary entangled non-Gaussian inputs under an average energy bound. Finite photon support is used only in achievability, first fixing the cutoff and coding limit, then increasing the cutoff with explicit entropy-tail control. The environmental inputs remain vacuum. A thermal average encoded state is not an uncoded thermal communication scheme.

## What is not proved here

There is no efficient helper measurement, finite-block code attaining capacity, strong-converse exponent, limited-message tradeoff, finite-temperature capacity, calibration robustness theorem or detector implementation. The supplied results do not need those extensions to define their claim. Exhaustive priority and genuinely separate critical review remain incomplete.

The import preserves the stated proof status. Reproduction in a second environment is not independent theoretical review. Current reading depths are in [PRIOR_ART](../literature/PRIOR_ART.md); the next bounded task is in [CURRENT](../work_orders/CURRENT.md).
