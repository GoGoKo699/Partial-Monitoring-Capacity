# Model, claim hierarchy and proof dependencies

The [capacity theorem](THEOREM.md) and [exact product optimum](EXACT_PRODUCT_CAPACITY_2026-10-07.md)
give the unrestricted and predetermined individual-measurement rates. The
[dependency record](PROOF_DEPENDENCIES.md) supplies the established converse
attribution, optical coding and continuous-record arguments.

## Fixed communication resource

A memoryless isometry divides the input among receiver $B$, inaccessible field $E$ and helper field $D$. The encoder is predetermined and may use many inputs; the helper may jointly measure arbitrarily many $D$ outputs and sends the classical outcome only to the receiver. The decoder uses $B^n$ and that outcome. Unknown messages are not supplied to the helper. General encoders, including a discarded ancillary system, are included.

No preshared entanglement, coherent helper-to-receiver link, sender/receiver feedback, intermediate control, postselection or free two-way distillation is supplied. Helper quantum memory, collective circuit complexity, phase references and classical message length are unrestricted. Rank-one refinement is a proof reduction; a coarsened record can leave an additional unobserved quantum register in the complement.

The capacity is asymptotic entanglement transmission per original input. It is not a finite-code fidelity, average survival probability, secret-key capacity, or corrected-memory lifetime. An efficient helper receiver is an open constructive problem, not an uncounted premise.

## Central theorem and its two evaluations

| ID | Author-side statement | Proof route | Diagnostic suite |
|---|---|---|---|
| C1 | The joint-register degrading identity makes the minimum-cut assistance lower bound exact. | [THEOREM](THEOREM.md), Sections 1–2; both finite-dimensional cuts follow from established degradable-state theory via [the register reduction](PROOF_DEPENDENCIES.md). | consolidation; qubit |
| C2 | Qubit splitting has an exact single-variable rate and positive capacity exactly when survival exceeds unobserved decay. | THEOREM, Section 3; [original rate excerpt](../archive/excerpts/QUANTUM_RATE.md). | threshold; qubit |
| C3 | Vacuum optical splitting has capacity $g(aN)-g(bN)$ when $a>b$, and zero otherwise, under an average incident-energy constraint. | THEOREM, Section 4; [optical dependencies](PROOF_DEPENDENCIES.md#3-optical-identity-and-photon-budget-coding) and [preserved tail calculation](../archive/imported/OPTICAL_AUDIT.md), Sections 4.2–4.3. | optical |
| C4 | The optical rate deficit separates unused energy, thermal-reference contraction deficit and measurement deficit. | THEOREM, Section 5; [PROOF_AUDIT](PROOF_AUDIT.md). | consolidation |
| C5 | Antidegradability gives $F_e\le(d+1)/(2d)$ for a logical message of dimension $`d`$ on the zero-capacity side. | [rate excerpt](../archive/excerpts/QUANTUM_RATE.md), Section A3. | qubit |
| C6 | At $`(a,b,c)=(0.2,0.08,0.72)`$, all predetermined product helper POVMs have capacity strictly below the unrestricted optimum, despite arbitrary sender/receiver block coding. | Corollary of C1 and C7; the [earlier qualitative proof](../archive/editorial/2026-10-07-pre-release/research/PRODUCT_HELPER_GAP_2026-10-07.md) is retained as history. | Separate rational certificate for the scalar gap; analytical capacity proofs supply the comparison. |
| C7 | For the qubit family with $a>b>0,c>0$, photon counting attains the capacity optimized over all predetermined product helper POVMs and all inputs. | [Exact product capacity](EXACT_PRODUCT_CAPACITY_2026-10-07.md): branch determinants, convex entropy difference and a counting chord bound. | Separate exact-arithmetic certificate for the example's scalar rate and gap; the analytical proof remains a dependency. |

C2 and C3 are evaluations of one capacity principle, not unrelated new projects. The threshold is not an assertion that the channel becomes entanglement-breaking. The fidelity ceiling is unconditional and is not the same metric as average state fidelity.

The central comparison combines C1 with C7: the exact unrestricted capacity and the optimal predetermined product benchmark give a strict rate separation at the stated qubit split. C6 is the example corollary of these two exact results. C3 supplies the complementary optical energy/loss law; C4 and C5 remain supporting results.

[The physical picture](PHYSICAL_PICTURE.md) translates the optical law into a collection requirement at a chosen target rate. This is an algebraic consequence of C3. C7 strengthens C6 to an exact product benchmark and certifies the example's gap at approximately $0.11949910$ qubits/use. Every single-use POVM and predetermined use-varying schedule is included; outcome-adaptive local strategies and general separable block POVMs remain outside the claim. C7 is a qubit result, not an optical measurement-optimality theorem.

## Dependencies that must remain visible

**Joint simulation.** The map from $B$ to $E$ must leave $D$ and its correlations unchanged. A map reproducing only the inaccessible marginal is insufficient. The random-phase example in the supplied audit is a countercontrol, not a counterexample to the stated hypothesis.

**Established state converse.** Leditzky–Datta–Smith, Definition 2.2 and Proposition 2.4, give both finite-dimensional upper bounds by grouping $RFD^n:B^n$ and $RF:B^nD^n$. This is a converse relaxation of the actual task, not permission for new communication or access. C1 is a synthesis of established assistance and state-converse ingredients; C7 still needs its separate measurement optimization.

**Refined complement.** The measured channel has output $BX$ and a complementary output $EY$ with a copy of the classical outcome. Degradability applies to every refined block measurement. Deleting a record without changing the complement invalidates the coherent-information expression.

**General helper instruments.** The [direct converse](CLAIM_ASSESSMENT_2026-10-07.md) retains the unresolved helper register and discarded encoder ancilla, proving the two upper bounds without rank-one refinement. Continuous optical records are handled by finite classical partitions. This does not make a coarse measured channel degradable or extend the exact deficit identity to coarse records.

**Two cuts and single-letterization.** The two upper bounds, concavity and many-use subadditivity must use the same input density matrix after marginal averaging. General encoding ancillas are covered by the explicit conditional-entropy argument, not a restriction to an isometric encoder.

**Achievability.** The assistance ensemble theorem selects a measurement on $D$. Grouping the inaccessible field with a mathematical reference does not grant access to either. Freeze the block measurement and use ordinary quantum coding over the resulting channel with a classical flag. No encoder-side outcome or two-way distillation is added.

**Optical limit.** The converse includes arbitrary entangled non-Gaussian inputs under an average energy bound. The full Fock-space Weyl identity and fixed-cutoff/block application of Wilde–Qi's energy-constrained coding theorem are explicit in [PROOF_DEPENDENCIES](PROOF_DEPENDENCIES.md). Finite photon support is used only in achievability, first fixing the cutoff and coding limit, then increasing the cutoff with explicit entropy-tail control. The environmental inputs remain vacuum. A thermal average encoded state is not an uncoded thermal communication scheme.

## Scope and interpretation

The results are asymptotic capacities with unrestricted helper resources. The product
benchmark is predetermined and excludes adaptive local strategies and separable block
POVMs. Counting optimality is after input optimization and applies to the qubit family.
The optical law assumes vacuum environmental inputs and an average signal-energy bound.
The fidelity ceiling is unconditional; no strong-converse exponent is asserted.

[The contribution comparison](CONTRIBUTION_ASSESSMENT_2026-10-07.md) and
[source ledger](../literature/PRIOR_ART.md) specify inherited results and reading depths.
[VERIFICATION](../VERIFICATION.md) explains the distinction between analytical claims,
diagnostic reproduction and review.
