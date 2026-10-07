> Imported 7 October 2026 from the supplied 6 October consolidation. Editorial links only; scientific claims and qualifications are unchanged. See [import provenance](../provenance/IMPORT_MANIFEST.json).

# What the consolidation added, and what it did not

**Current attribution correction:** [PROOF_DEPENDENCIES](PROOF_DEPENDENCIES.md) derives both finite-dimensional cuts directly from the established degradable-state distillation theorem. The historical descriptions of a candidate converse below do not claim an independent new inequality. The preserved calculations and capacity formulas are unchanged.

**7 October follow-up:** [CLAIM_ASSESSMENT](CLAIM_ASSESSMENT_2026-10-07.md) extends the converse presentation to unresolved helper outputs directly, including continuous records through finite partitions. It changes no capacity formula. This dated consolidation record remains below.

**6 October 2026. Internal/author-side review, not an independent referee report.**

## Preserved central result

The finite-dimensional theorem, qubit rate, positive-rate threshold, optical energy law, asymptotic ceiling and finite-message bound are the existing supplied results. Their values and domains are unchanged. The previous historical papers and test reports remain intact under [archive/](../archive/README.md). No proof from the spin-strip pilot is used, and its numerical or analytical status is not advanced.

`THEOREM.md` is now a single short route through the model, joint-register identity, two cuts, matching achievability and the two physical evaluations. It is not a claim that a practical collective receiver has been built. Source methods and the candidate converse are explicitly separated.

## Explicit coding step: arbitrary encoders

The earlier audit invoked the standard energy-constrained coding equivalence. Here the relevant monotonicity is written out rather than assumed.

For any rank-one refined helper measurement on a block, the true measured-channel output is BX and a true complement is EY, with X and Y copies of the same classical label. The joint-register identity yields a degrading channel BX -> EY. Take any message reference R and discarded encoding ancilla F purifying the input. Then

$$I(RF\rangle BX)-I(R\rangle BX)=S(F|EX).$$

Apply the degrading map to B in the actual output state, producing E'. Conditional on every x, FE and FE' have identical marginals. Weak monotonicity gives

$$S(F|E,x)+S(F|E',x)\ge0\quad\Rightarrow\quad S(F|E,x)\ge0.$$

Averaging establishes the needed inequality for arbitrary encoding channels. The simulator creates a comparison extension; it is not a recovery operation on the real inaccessible field. The same reasoning works for a finite-entropy optical input. Finite mean energy controls the signal entropies; this is not a maximum-photon-number assumption.

This is a standard implication of degradability/shareability used in the specific proof, not another independent communication theorem. The finite checks include a nondegradable example showing the inequality cannot be used without the hypothesis.

## Explicit complement: refinement cannot be silently undone

The formula S(B|X)-S(E|X) presupposes that the helper effect has been refined to rank one. If all records are discarded, the receiver sees B alone and the complement is ED, not E. At (a,b,c)=(.2,.08,.72), q=.5, the checker gives negative unmonitored coherent information, positive counted coherent information, and an even larger S(B)-S(E). The last number is an upper bound with the requisite joint-degradation property, not the coherent information of a receiver that obtained no record.

This makes a hidden-environment error explicit and avoids the false inference that coarsening a classical record helps. It does not correct or change a formula in the preceding note, which already stipulated refinement. Likewise, the actual XBE need not be a quantum Markov chain.

## Exact deficit decomposition

For arbitrary block inputs of actual mean bar-N and refined helper measurements, the optical coherent-information deficit at budget N splits into three nonnegative terms:

$$n[Q(N)-Q(\bar N)] +\{D(\rho_B\Vert\tau_{a\bar N}^{\otimes n})-D(\rho_E\Vert\tau_{b\bar N}^{\otimes n})\} +\{I(X;B)-I(X;E)\}.$$

This is an exact consolidation of equalities already used in the proof. It is not a new rate law or a finite-code fidelity statement. It shows precisely what must vanish per use in a capacity-achieving sequence. The second term is a **contraction deficit**, not a claim that every nonthermal state is strictly suboptimal or that the term measures only non-Gaussianity.

## Scalar qubit evaluation

At a>b, define q_c=1/(1+a-b), s=1-b. The two receiver entropies cross at aq_c+sq_c=1. On [0,q_c] the rate objective is f_1(q)=h2(aq)-h2(bq), with

$$f_1''(q)=\frac{b-a}{\ln2\,q(1-aq)(1-bq)}<0.$$

On the right, f_2(q)=h2(sq)-h2(bq) is concave. At q_c,

$$f_2'(q_c)=s\log_2(a/s)-b\log_2[(1+a-2b)/b]\le0.$$

The inequality follows from s>=a and 1+a-2b>b (as a>b and b<1/2); endpoints use limits. Thus the optimum is q_c when f_1'(q_c)>=0, otherwise the unique left stationary point. The 56 parameter checks compare this rule against independently optimizing both pieces. This does not enlarge the noise model or optimize a finite helper apparatus.

## What still deserves scrutiny

The actual author-side result to test is the saturation of an assistance lower bound under the joint-register condition, with the specified receiver-only resources. A reader can attack that condition, the two-cut converse, the flagged-channel coding construction, or the finite-energy limiting order without first reconstructing the exploration history.

No broad stronger claim is quietly attached: there is no efficient helper implementation, strong-converse exponent, finite-block coding construction, robustness theorem, nonvacuum-environment capacity, bounded-message tradeoff, or general two-way entanglement-distillation equality. Such work might be useful later, but it is not required to define the current theorem.

The prior-art comparison is targeted, not exhaustive. In particular, Buscemi–Datta's one-shot assistance work is added to the active ledger at its actual full-purification scope. It does not establish a partial-access converse merely by having a general title. No statement about all of its cited extensions is inferred from the inspected passages.

## Verification scope

Four new finite identity checks pass twice. They reuse explicitly imported, byte-preserved numerical utilities from `prior/check_audit.py`. The largest new density matrix is 144 by 144. The field input in the optical check is supported through four photons only for algebra verification; that is not a restriction on the analytical converse. The previous 6 optical-audit, 7 monitoring-followup and 6 baseline groups are rerun separately with unchanged output references. Spin suites are not rerun.

No numerical assertion or tolerance was changed after the first complete run. Bibliographic names in the working draft were checked against primary metadata before finalization; no unverified citation is left in the active theorem note. The source ledger states exactly which proofs were reread and which records were metadata/abstract checks.
