# Model, claim hierarchy and proof dependencies

**Updated 7 October 2026.** This maps the supplied 6 October consolidation, the [bounded claim assessment](CLAIM_ASSESSMENT_2026-10-07.md), the [qualitative product helper separation](PRODUCT_HELPER_GAP_2026-10-07.md) and its [exact capacity resolution](EXACT_PRODUCT_CAPACITY_2026-10-07.md). The unrestricted capacity formulas and resources are unchanged.

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
| C6 | At $(a,b,c)=(0.2,0.08,0.72)$, all predetermined product helper POVMs have capacity strictly below the unrestricted optimum, despite arbitrary sender/receiver block coding. | [Product helper gap](PRODUCT_HELPER_GAP_2026-10-07.md): degradable-channel additivity, compactness and strict entropy contraction. | Analytical result; original suites do not certify this proof. |
| C7 | For the qubit family with $a>b>0,c>0$, photon counting attains the capacity optimized over all predetermined product helper POVMs and all inputs. | [Exact product capacity](EXACT_PRODUCT_CAPACITY_2026-10-07.md): branch determinants, convex entropy difference and a counting chord bound. | Separate exact-arithmetic certificate for the example's scalar rate and gap; the analytical proof remains a dependency. |

C2 and C3 are evaluations of one capacity principle, not unrelated new projects. The threshold is not an assertion that the channel becomes entanglement-breaking. The fidelity ceiling is unconditional and is not the same metric as average state fidelity.

The reader-facing lead combines C1 with C7: the exact unrestricted capacity and the optimal predetermined product benchmark give a strict rate separation at the stated qubit split. C6 records the preceding qualitative proof, now strengthened by C7. C3 supplies the complementary optical energy/loss law; C4 and C5 remain supporting results. This ordering changes emphasis, not claims or proof dependencies.

[The physical picture](PHYSICAL_PICTURE.md) translates the optical law into a collection requirement at a chosen target rate. This is an algebraic consequence of C3. C7 strengthens C6 to an exact product benchmark and certifies the example's gap at approximately $0.11949910$ qubits/use. Every single-use POVM and predetermined use-varying schedule is included; outcome-adaptive local strategies and general separable block POVMs remain outside the claim. C7 is a qubit result, not an optical measurement-optimality theorem.

## Dependencies that must remain visible

**Joint simulation.** The map from $B$ to $E$ must leave $D$ and its correlations unchanged. A map reproducing only the inaccessible marginal is insufficient. The random-phase example in the supplied audit is a countercontrol, not a counterexample to the stated hypothesis.

**Refined complement.** The measured channel has output $BX$ and a complementary output $EY$ with a copy of the classical outcome. Degradability applies to every refined block measurement. Deleting a record without changing the complement invalidates the coherent-information expression.

**General helper instruments.** The [direct converse](CLAIM_ASSESSMENT_2026-10-07.md) retains the unresolved helper register and discarded encoder ancilla, proving the two upper bounds without rank-one refinement. Continuous optical records are handled by finite classical partitions. This does not make a coarse measured channel degradable or extend the exact deficit identity to coarse records.

**Two cuts and single-letterization.** The two upper bounds, concavity and many-use subadditivity must use the same input density matrix after marginal averaging. General encoding ancillas are covered by the explicit conditional-entropy argument, not a restriction to an isometric encoder.

**Achievability.** The assistance ensemble theorem selects a measurement on $D$. Grouping the inaccessible field with a mathematical reference does not grant access to either. Freeze the block measurement and use ordinary quantum coding over the resulting channel with a classical flag. No encoder-side outcome or two-way distillation is added.

**Optical limit.** The converse includes arbitrary entangled non-Gaussian inputs under an average energy bound. Finite photon support is used only in achievability, first fixing the cutoff and coding limit, then increasing the cutoff with explicit entropy-tail control. The environmental inputs remain vacuum. A thermal average encoded state is not an uncoded thermal communication scheme.

## What is not proved here

There is no efficient helper measurement, finite-block code attaining capacity, strong-converse exponent, limited-message tradeoff, finite-temperature capacity, calibration robustness theorem or detector implementation. The supplied results do not need those extensions to define their claim. Exhaustive priority and genuinely separate critical review remain incomplete.

The targeted assessment found no rate correction. Reproduction in a second environment is not independent theoretical review. Current reading depths are in [PRIOR_ART](../literature/PRIOR_ART.md) and the [dated priority check](../literature/PRIORITY_CHECK_2026-10-07.md); the next bounded task is in [CURRENT](../work_orders/CURRENT.md).
