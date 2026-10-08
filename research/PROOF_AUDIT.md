# Complement, encoder ancillas and rate deficits

These arguments explain the true measured-channel complement, arbitrary encoders
and the optical deficit decomposition. The
[dependency record](PROOF_DEPENDENCIES.md) attributes both finite-dimensional
converse cuts to established degradable-state theory. The
[direct coarse-record proof](CLAIM_ASSESSMENT_2026-10-07.md) covers unresolved
helper outputs and continuous records.

## Explicit coding step: arbitrary encoders

For any rank-one refined helper measurement on a block, the true measured-channel output is BX and a true complement is EY, with X and Y copies of the same classical label. The joint-register identity yields a degrading channel BX -> EY. Take any message reference R and discarded encoding ancilla F purifying the input. Then

$$I(RF\rangle BX)-I(R\rangle BX)=S(F|EX).$$

Apply the degrading map to B in the actual output state, producing E'. Conditional on every x, FE and FE' have identical marginals. Weak monotonicity gives

$$S(F|E,x)+S(F|E',x)\ge0\quad\Rightarrow\quad S(F|E,x)\ge0.$$

Averaging establishes the needed inequality for arbitrary encoding channels. The simulator creates a comparison extension; it is not a recovery operation on the real inaccessible field. The same reasoning works for a finite-entropy optical input. Finite mean energy controls the signal entropies; this is not a maximum-photon-number assumption.

This implication of degradability/shareability requires the degrading hypothesis. The finite checks include a nondegradable example for which the inequality fails.

## Explicit complement: refinement cannot be silently undone

The formula S(B|X)-S(E|X) presupposes that the helper effect has been refined to rank one. If all records are discarded, the receiver sees B alone and the complement is ED, not E. At (a,b,c)=(.2,.08,.72), q=.5, the checker gives negative unmonitored coherent information, positive counted coherent information, and an even larger S(B)-S(E). The last number is an upper bound with the requisite joint-degradation property, not the coherent information of a receiver that obtained no record.

This example shows why the unresolved environment must be included when coarsening a classical record. The actual XBE need not be a quantum Markov chain.

## Exact deficit decomposition

For arbitrary block inputs of actual mean bar-N and refined helper measurements, the optical coherent-information deficit at budget N splits into three nonnegative terms:

$$n[Q(N)-Q(\bar N)] +\{D(\rho_B\Vert\tau_{a\bar N}^{\otimes n})-D(\rho_E\Vert\tau_{b\bar N}^{\otimes n})\} +\{I(X;B)-I(X;E)\}.$$

This identity specifies what must vanish per use in a capacity-achieving sequence. It concerns coherent information, rather than finite-code fidelity. The second term is a **contraction deficit**, not a claim that every nonthermal state is strictly suboptimal or that the term measures only non-Gaussianity.

## Scalar qubit evaluation

At a>b, define q_c=1/(1+a-b), s=1-b. The two receiver entropies cross at aq_c+sq_c=1. On [0,q_c] the rate objective is f_1(q)=h2(aq)-h2(bq), with

$$f_1''(q)=\frac{b-a}{\ln2\,q(1-aq)(1-bq)}<0.$$

On the right, f_2(q)=h2(sq)-h2(bq) is concave. At q_c,

$$f_2'(q_c)=s\log_2(a/s)-b\log_2[(1+a-2b)/b]\le0.$$

The inequality follows from s>=a and 1+a-2b>b (as a>b and b<1/2); endpoints use limits. Thus the optimum is q_c when f_1'(q_c)>=0, otherwise the unique left stationary point. The 56 parameter checks compare this rule against independently optimizing both pieces.

## Operational scope

The capacity equality saturates an assistance lower bound under the joint-register condition with receiver-only classical assistance. Its dependencies are the two-cut converse, the flagged-channel coding construction and the finite-energy limiting order.

The rates are asymptotic, with unrestricted helper processing. The result concerns the communication resources in [MODEL_AND_CLAIMS](MODEL_AND_CLAIMS.md), rather than finite-code apparatus performance.

Buscemi–Datta's one-shot assistance work gives the helper the entire purification. Its role and the passages inspected are specified in the [source ledger](../literature/PRIOR_ART.md); no partial-access converse or claim about all cited extensions is inferred from those passages.

## Verification scope

Four consolidation groups check the finite identities using the numerical utilities in `checks/source/prior/check_audit.py`. The largest consolidation density matrix is 144 by 144. The field input in the optical check is supported through four photons only for algebra verification; that is not a restriction on the analytical converse. Separate suites contain 6 optical-audit, 7 monitoring-followup and 6 baseline groups.

The [verification policy](../VERIFICATION.md) describes the checks and numerical comparisons. The [source ledger](../literature/PRIOR_ART.md) distinguishes full-proof, metadata and abstract-only readings.
