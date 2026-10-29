# Thirty milestones for partial monitoring capacity

[Overview](../README.md) · [Preskill bridge](PRESKILL_READING_MAP.md) · [Exact statements](MODEL_AND_CLAIMS.md)

The central question is how a classical record from part of a lost field changes
quantum transmission, and why collective helper measurements can outperform
every predetermined individual measurement in the qubit model. These are
project-defined understanding targets, independent of any reader's prior study.

The map has **12 background/preliminaries milestones** and **18 narrative/innovation
milestones**. The background assembles states, records, entropy, coding and energy
into the operational task. The narrative follows the two capacity bounds and
their construction, the separate qubit measurement optimization, and the optical
evaluation. Its final comparison connects the sister detector project while
keeping this repository's qubit result central. Neither phase is a list of every
technical lemma.

The sole educational anchor is **John Preskill, Quantum Shannon Theory, Chapter
10, 2025 revision, arXiv:1604.07450v5**. The
[reading map](PRESKILL_READING_MAP.md#reading-route) selects relevant sections and
supplies four worked bridges. The primary papers cited by the proofs retain
their research attribution; they are not additional required tutorial anchors.

## Background and preliminaries: M01–M12

### M01 — State, subsystem and reference

- **Question:** What information can a reduced density matrix hide?
- **Understanding target:** Explain partial trace and purification, and distinguish a mathematical reference from a system available to the helper.
- **Dependencies and story role:** None; establish the objects carried through the argument.
- **Conceptual connection:** Correlations, rather than output populations alone, determine quantum transmission.
- **Sources:** Preskill Sections 10.2.1–10.2.4; [physical picture](PHYSICAL_PICTURE.md).

### M02 — Three destinations for one input

- **Question:** Which part of the lost field can affect the decoder?
- **Understanding target:** Identify receiver $`B`$, inaccessible output $`E`$ and helper output $`D`$ in the splitting isometry.
- **Dependencies and story role:** M01; place the abstract state in the physical task.
- **Conceptual connection:** Collection changes access to an output, not the fractions already reaching the receiver.
- **Sources:** [Physical picture](PHYSICAL_PICTURE.md); [model](MODEL_AND_CLAIMS.md#fixed-communication-resource).

### M03 — Transmitting entanglement unconditionally

- **Question:** What does a capacity rate promise?
- **Understanding target:** Relate logical reference preservation, vanishing unconditional error and qubits per original channel use; distinguish this from a successful branch probability.
- **Dependencies and story role:** M01, M02; define the operational objective.
- **Conceptual connection:** Every outcome and failed trial remains in the denominator.
- **Sources:** Preskill Sections 10.7.1–10.7.3; [model](MODEL_AND_CLAIMS.md#fixed-communication-resource).

### M04 — A measurement makes a channel with a record

- **Question:** What remains after the helper measures its output?
- **Understanding target:** Explain POVM effects, conditional states and the receiver's classical outcome label.
- **Dependencies and story role:** M02; identify the helper's permitted action.
- **Conceptual connection:** A measured quantum output becomes a classical side channel coupled to the receiver state.
- **Sources:** Preskill Sections 10.6.1–10.6.3; [Bridge 1](PRESKILL_READING_MAP.md#1-the-measurement-record-and-its-complement).

### M05 — Entropy with a classical flag

- **Question:** How does an orthogonal outcome label enter the output entropy?
- **Understanding target:** Explain the Shannon entropy plus average branch-entropy decomposition for a classical–quantum state.
- **Dependencies and story role:** M01, M04; provide the entropy bookkeeping used in both benchmarks.
- **Conceptual connection:** Copied records can cancel in an entropy difference while still belonging to the channel dilation.
- **Sources:** Preskill Sections 10.2.1–10.2.4 and 10.6.1–10.6.3; [Bridge 1](PRESKILL_READING_MAP.md#copy-the-classical-label-into-the-dilation).

### M06 — Coherent information and a true complement

- **Question:** Which entropy difference can support quantum communication?
- **Understanding target:** Identify coherent information using the actual complementary output and distinguish a one-input quantity from an asymptotic optimized capacity.
- **Dependencies and story role:** M03, M05; connect state entropies to communication.
- **Conceptual connection:** Changing what the decoder receives also changes what is discarded.
- **Sources:** Preskill Sections 10.7.1–10.7.3; [proof audit](PROOF_AUDIT.md).

### M07 — Data processing and conditional entropy

- **Question:** Why can receiver processing not manufacture missing quantum information?
- **Understanding target:** Explain the role of strong subadditivity and data processing in converse bounds.
- **Dependencies and story role:** M05, M06; introduce the direction of the upper-bound arguments.
- **Conceptual connection:** A simulated output or a relaxed task supplies a bound only in the justified direction.
- **Sources:** Preskill Sections 10.2.1–10.2.4 and 10.8–10.9.4; [Bridge 2](PRESKILL_READING_MAP.md#2-two-cuts-and-a-matching-construction).

### M08 — Degradable and antidegradable channels

- **Question:** What follows when one output can simulate the other?
- **Understanding target:** Distinguish degradability, antidegradability and entanglement breaking; explain the role of a receiver extension on the zero-capacity side.
- **Dependencies and story role:** M02, M06, M07; supply the structural channel properties.
- **Conceptual connection:** Simulation concerns correlations with arbitrary references, not just one output state.
- **Sources:** Preskill Section 10.7.3 and Exercise 10.18; [theorem](THEOREM.md).

### M09 — Additivity and input optimization

- **Question:** When can a many-use coding problem reduce to one-use inputs?
- **Understanding target:** Explain why degradable-channel additivity and concavity cover correlated endpoint codes and use-varying predetermined measurements.
- **Dependencies and story role:** M06, M08; prepare the exact product benchmark.
- **Conceptual connection:** Individual helper measurements do not mean individual sender or receiver codes.
- **Sources:** Preskill Section 10.7.3; [product-helper reduction](PRODUCT_HELPER_GAP_2026-10-07.md).

### M10 — Freeze an auxiliary operation, then code

- **Question:** How does a helper construction become a transmission protocol?
- **Understanding target:** Explain coding over repeated uses of a fixed flagged channel and the order of helper-block and code-length limits.
- **Dependencies and story role:** M03, M06, M09; supply the achievability framework.
- **Conceptual connection:** A state ensemble alone is not yet a code for unknown quantum messages.
- **Sources:** Preskill Sections 10.8–10.9.4; [helper construction](PRESKILL_READING_MAP.md#the-helper-ensemble-then-ordinary-coding).

### M11 — Bosonic energy and thermal entropy

- **Question:** What changes when a mode has unbounded photon number?
- **Understanding target:** Distinguish mean energy from a peak cutoff and a thermal average coded input from a thermal environment.
- **Dependencies and story role:** M01, M05; introduce the extra optical control of entropy and limits.
- **Conceptual connection:** A finite mean constrains admissible codes without bounding every occupied photon level.
- **Sources:** [Bridge 4](PRESKILL_READING_MAP.md#4-the-optical-energy-limit); [optical dependencies](PROOF_DEPENDENCIES.md#3-optical-identity-and-photon-budget-coding).

### M12 — Assemble the fixed resource model

- **Question:** Which comparisons refer to the same communication task?
- **Understanding target:** Reconstruct the input, three outputs, helper-only-to-receiver record, arbitrary endpoint codes and unconditional rate without importing feedback or shared entanglement.
- **Dependencies and story role:** M02, M04, M10, M11; integrate the background phase.
- **Conceptual connection:** Preskill's preshared entanglement assistance differs from environmental measurement assistance.
- **Sources:** [Model and claims](MODEL_AND_CLAIMS.md); [reading-route resource distinction](PRESKILL_READING_MAP.md#reading-route).

## Narrative and innovation: M13–M30

### M13 — The counted and uncounted qubit branches

- **Question:** How does a detected collected excitation change the receiver state?
- **Understanding target:** Explain the two counting branches, their probabilities and the no-count branch's entropy contribution.
- **Dependencies and story role:** M02, M04, M05, M12; start the proof story with a complete finite example.
- **Conceptual connection:** The count branch can carry zero coherent information while its occurrence still belongs to the unconditional channel.
- **Sources:** [Worked counting example](PRESKILL_READING_MAP.md#a-counting-example).

### M14 — Copy the flag and retain unresolved systems

- **Question:** Why is the inaccessible field alone not the measured channel's complement?
- **Understanding target:** Reconstruct the copied classical record and explain the extra unresolved register after coarse graining.
- **Dependencies and story role:** M04, M05, M08, M13; make the channel entropy calculation sound.
- **Conceptual connection:** The same obligation later includes a discarded optical detector reference.
- **Sources:** [Flag dilation](PRESKILL_READING_MAP.md#copy-the-classical-label-into-the-dilation); [proof audit](PROOF_AUDIT.md).

### M15 — Joint degradation preserves the helper

- **Question:** Why is marginal degradation insufficient for assistance?
- **Understanding target:** Explain the joint $`ED`$ channel identity and why a helper measurement commutes with a map acting only on $`B`$.
- **Dependencies and story role:** M08, M12, M14; establish the hypothesis that makes both cuts work.
- **Conceptual connection:** Preserving helper correlations makes every refined measured channel degradable.
- **Sources:** [Theorem](THEOREM.md); [joint-simulation dependencies](PROOF_DEPENDENCIES.md).

### M16 — Two cuts from established state converses

- **Question:** Why do both $`B`$ and $`BD`$ produce upper bounds?
- **Understanding target:** Explain the two register groupings and identify the inherited degradable-state theorem used for each.
- **Dependencies and story role:** M06, M07, M15; derive the shape of the capacity bound.
- **Conceptual connection:** Enlarging a mathematical task does not grant those registers to the actual helper.
- **Sources:** [Upper bounds](PRESKILL_READING_MAP.md#upper-bounds-with-general-encoders); [proof dependencies](PROOF_DEPENDENCIES.md).

### M17 — General encoders and a common input

- **Question:** Which steps protect the converse against correlated or mixed encodings?
- **Understanding target:** Retain discarded encoder ancillas and explain why both entropy cuts use the same averaged input marginal.
- **Dependencies and story role:** M09, M16; close the operational quantifiers in the upper bound.
- **Conceptual connection:** Maximizing the cuts separately would not give the stated exact objective.
- **Sources:** [Theorem, Section 2](THEOREM.md#2-exact-finite-dimensional-rate); [direct converse](CLAIM_ASSESSMENT_2026-10-07.md).

### M18 — Assistance ensemble followed by ordinary coding

- **Question:** How can a measurement on collected outputs approach the smaller cut?
- **Understanding target:** Explain the inherited assistance ensemble, its mathematical reference grouping, and the fixed flagged-channel coding step.
- **Dependencies and story role:** M10, M14, M15; supply the matching lower bound.
- **Conceptual connection:** No operation on an inaccessible or reference register is borrowed by the construction.
- **Sources:** [Helper ensemble and coding](PRESKILL_READING_MAP.md#the-helper-ensemble-then-ordinary-coding); [theorem](THEOREM.md).

### M19 — The exact unrestricted capacity

- **Question:** Why do the upper and lower arguments meet?
- **Understanding target:** Assemble the minimum of the two entropy differences and identify its assumptions and inherited ingredients.
- **Dependencies and story role:** M16, M17, M18; integrate the first main result.
- **Conceptual connection:** Exact unrestricted capacity supplies a comparison target, not an efficient detector.
- **Sources:** [Capacity theorem](THEOREM.md); [contribution assessment](CONTRIBUTION_ASSESSMENT_2026-10-07.md).

### M20 — Arbitrary qubit inputs and helper rows

- **Question:** How can every individual POVM be represented in the optimization?
- **Understanding target:** Explain how input coherence enters the determinant and how each refined branch reduces to one bounded scalar.
- **Dependencies and story role:** M13, M14, M15; begin the separate all-POVM counting proof.
- **Conceptual connection:** A proof about one diagonal input would not rule out a coherent competing input.
- **Sources:** [Exact product proof, Section 1](EXACT_PRODUCT_CAPACITY_2026-10-07.md#1-reduce-every-branch-to-one-scalar).

### M21 — Convexity of the entropy difference

- **Question:** What justifies replacing every branch by a chord bound?
- **Understanding target:** Distinguish convexity of the required difference from convexity of its individual entropy terms, and use POVM completeness in the average.
- **Dependencies and story role:** M05, M20; supply the decisive measurement inequality.
- **Conceptual connection:** Subtracting convex functions does not automatically preserve convexity.
- **Sources:** [Exact product proof, Section 2](EXACT_PRODUCT_CAPACITY_2026-10-07.md#2-the-entropy-difference-is-convex).

### M22 — Counting saturates after input optimization

- **Question:** Why can no predetermined individual measurement beat optimized counting?
- **Understanding target:** Explain the replacement diagonal input, counting's endpoint saturation and the role of additivity for arbitrary endpoint codes.
- **Dependencies and story role:** M09, M20, M21; complete the central product optimum.
- **Conceptual connection:** The theorem optimizes inputs; it does not assert counting wins at every fixed coherent input.
- **Sources:** [Exact product proof, Section 3](EXACT_PRODUCT_CAPACITY_2026-10-07.md#3-the-chord-is-bounded-by-counting-with-another-diagonal-input).

### M23 — A strict collective advantage throughout the interior

- **Question:** What makes the qubit rate separation universal within its stated region?
- **Understanding target:** Compare both unrestricted cuts with the counting objective at its common optimizing input and explain strict positivity of the difference.
- **Dependencies and story role:** M19, M22; combine the two exact results.
- **Conceptual connection:** The collective benefit raises rate while counting already attains the positive-capacity boundary.
- **Sources:** [Strict-gap corollary](EXACT_PRODUCT_CAPACITY_2026-10-07.md#4-strict-collective-advantage-throughout-the-qubit-interior).

### M24 — What an exact numerical certificate establishes

- **Question:** Which part of the example is certified arithmetically?
- **Understanding target:** Separate rational rate enclosures, finite diagnostic checks and the analytical optimization over all POVMs.
- **Dependencies and story role:** M22, M23; connect the proof to reproducible evidence without confusing their roles.
- **Conceptual connection:** A precise scalar gap illustrates a theorem but does not replace its quantifiers.
- **Sources:** [Certificate](../checks/certify_product_capacity.py); [verification policy](../VERIFICATION.md).

### M25 — The optical converse includes non-Gaussian codes

- **Question:** Why does a thermal entropy expression upper-bound every allowed optical code?
- **Understanding target:** Explain the full Fock-space joint identity and thermal-reference relative-entropy contraction under a mean budget.
- **Dependencies and story role:** M07, M11, M15, M19; extend the unrestricted theorem to optical energy.
- **Conceptual connection:** Thermal references in a proof do not assume Gaussian encodings.
- **Sources:** [Optical proof dependencies](PROOF_DEPENDENCIES.md#3-optical-identity-and-photon-budget-coding).

### M26 — Cutoff, coding limit and optical ceiling

- **Question:** How is the optical upper bound approached without imposing a peak constraint?
- **Understanding target:** Explain the truncated thermal construction, energy slack, order of limits and the fixed-loss capacity ceiling.
- **Dependencies and story role:** M10, M11, M18, M25; complete the optical evaluation.
- **Conceptual connection:** A temporary cutoff in achievability differs from a cutoff defining all competing codes.
- **Sources:** [Bridge 4](PRESKILL_READING_MAP.md#4-the-optical-energy-limit); [theorem](THEOREM.md).

### M27 — The meaning of the fixed resource comparison

- **Question:** Which further conclusions are outside these exact capacities?
- **Understanding target:** Distinguish predetermined product, adaptive local and unrestricted helper measurements, and identify unpriced helper memory, classical records and apparatus resources.
- **Dependencies and story role:** M12, M19, M23, M26; synthesize the main project's physical scope.
- **Conceptual connection:** An exact communication rate does not by itself specify detector cost or finite-block performance.
- **Sources:** [Model and claims](MODEL_AND_CLAIMS.md#scope-and-interpretation); [contribution assessment](CONTRIBUTION_ASSESSMENT_2026-10-07.md).

### M28 — Why the optical sister does not contradict the qubit optimum

- **Question:** Where does optical counting optimality first fail, and which resource matters?
- **Understanding target:** Compare the additional two-photon cutoff example with the mean-only oscillator law; distinguish within-mode number coherence from cross-mode joint processing.
- **Dependencies and story role:** M22, M26, M27; connect the established qubit result to the detector-class question.
- **Conceptual connection:** A first higher photon cutoff and a full-oscillator asymptotic law have different input domains.
- **Sources:** [Sister-project bridge](OPTICAL_DETECTOR_BRIDGE.md#from-one-photon-to-two); its pinned companion proofs.

### M29 — Pricing a local detector reference

- **Question:** What changes when the optical helper's phase reference is no longer free?
- **Understanding target:** Explain the separate-local-invariance model, mean prepared reference stock, and the half-to-full rate profile while retaining arbitrary endpoint codes.
- **Dependencies and story role:** M14, M25, M28; identify a concrete resource extension developed in the sister project.
- **Conceptual connection:** Reference information belongs to the true complement; mean stock differs from work, reset and coherent reuse.
- **Sources:** [Priced-reference bridge](OPTICAL_DETECTOR_BRIDGE.md#when-the-local-reference-is-priced); its pinned companion theorem.

### M30 — Reconstruct the whole comparison

- **Question:** How do the theorem, product optimum, optical law and resource extension fit together?
- **Understanding target:** Trace the common communication task to each exact claim, its proof source, its input and operation domain, and its verification evidence.
- **Dependencies and story role:** M24, M27, M28, M29; integrate the narrative phase and the project as a whole.
- **Conceptual connection:** The same physical split supports different answers when the detector class or priced resources change.
- **Sources:** [Overview](../README.md); [model and claims](MODEL_AND_CLAIMS.md); [sister bridge](OPTICAL_DETECTOR_BRIDGE.md); [verification](../VERIFICATION.md).
