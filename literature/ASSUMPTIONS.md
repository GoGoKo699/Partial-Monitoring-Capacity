# Scope and source-support boundary

The [proof-dependency record](../research/PROOF_DEPENDENCIES.md) gives the theorem's supporting arguments and targeted primary-source comparisons. Both finite-dimensional converse cuts follow from established degradable-state theory.

| Load-bearing item | Present basis | What is not inferred |
|---|---|---|
| Memoryless isometry and joint-register degradation | Explicit channel identity in THEOREM; qubit and passive-splitter operator checks. | Marginal degradability, Markov structure of every actual state, or a result for general noise. |
| Finite-dimensional upper bounds | Leditzky–Datta–Smith, Definition 2.2 and Proposition 2.4, applied to RFD:B and RF:BD; common-input single-letterization. | An independently new converse inequality, or automatic application of the finite-dimensional state theorem to infinite-dimensional systems. |
| Collective measurement and classical output to receiver | Assistance ensemble and fixed-flagged-channel coding argument; SVW05 and DH11 are attributed. | Free physical access to E, sender-side feedback, or an efficient helper circuit. |
| General encoders | Explicit discarded-ancilla argument in PROOF_AUDIT and standard coding converse. | Restriction to one-use or unentangled encodings. |
| Mean optical input energy | WQ18 Theorem 2 at fixed cutoff and helper block with summed photon Hamiltonian; thermal-reference converse and explicit entropy tails. | Peak photon limit, apparatus-energy accounting, or a nonvacuum input environment. |
| Continuous helper records | Finite trace-measure refinement for product qubit POVMs; finite partitions and finite-reference conditional-entropy continuity for the direct converse. | Subtraction of divergent differential entropies or an uncountable orthogonal-flag dilation. |
| Finite-message zero-side bound | Symmetric-extension/no-cloning argument in [PROOF_DEPENDENCIES, Section 4](../research/PROOF_DEPENDENCIES.md#4-boundary-cases-and-the-zero-side-fidelity-bound). | Tight fidelity at every parameter, conditional success, or average-state fidelity with the same number. |

The [source ledger](PRIOR_ART.md) and [dependency record](../research/PROOF_DEPENDENCIES.md) identify the primary-source passages supporting each comparison, including entries based only on abstracts or metadata. The [model map](../research/MODEL_AND_CLAIMS.md) specifies the communication resource. An efficient collective receiver is a separate constructive question.
