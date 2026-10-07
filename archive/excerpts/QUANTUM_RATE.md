## A. Monitored decay: define the communication resource

The memoryless isometry is the same as before, with output order B,E,D:

\[
V|0\rangle=|000\rangle,\qquad
V|1\rangle=\sqrt a|100\rangle+\sqrt b|010\rangle+\sqrt c|001\rangle,
\quad a+b+c=1.
\]

Here B is the surviving qubit, E inaccessible radiation, and D collected radiation. For decay probability r and collection efficiency eta,

\[
a=1-r,\qquad b=(1-\eta)r,\qquad c=\eta r.
\]

An encoder may use many independent inputs. A helper may perform any joint measurement on their D outputs and send its classical result to the receiver, which decodes B. The helper cannot transfer D coherently, receive feedback from the receiver, or intervene in the damping dynamics. No preshared entanglement, uncounted extra channel, free two-way sender–receiver distillation, or discarded unsuccessful trials is allowed. General local quantum operations and phase references are not constrained by energy-conservation rules. Classical message length and the complexity of the collective helper measurement are not bounded.

The capacity is asymptotic entanglement transmission per physical channel use. It is not a single-use restoration probability, an error-corrected-memory lifetime, or a claim of efficient codes or receiver hardware. A rank-one refinement of the helper POVM cannot reduce the receiver's resources, because the receiver can ignore the additional outcome label. Such measurements therefore suffice for both converse and achievability.

## A1. Exact capacity for arbitrary collective measurement of the collected field

Write h2(q)=-q log2 q-(1-q)log2(1-q). The new author-side result is

\[
\boxed{
Q_{\rm mon}(a,b,c)=
\begin{cases}
0,&a\le b,\\[2mm]
\displaystyle\max_{0\le q\le1}
\bigl\{\min[h_2(aq),h_2((1-b)q)]-h_2(bq)\bigr\},&a>b.
\end{cases}}
\tag{A1}
\]

The nonzero condition remains precisely a>b, or r<1/(2-eta). The improvement over the preceding note is that (A1) optimizes the rate over every block measurement on D, not only counting. Its numerical one-variable maximization is not a search over finite POVMs.

The proof uses a general property that is stronger than ordinary marginal degradability. Let N_BD and N_ED be the indicated reductions of V. When a>=b,

\[
\boxed{N_{ED}=(\mathcal A_{b/a}\otimes\mathrm{id}_D)N_{BD},}
\tag{A2}
\]

where A_s is amplitude damping with survival s. The identity preserves D and any reference entangled with the input. When a<=b, the reversed relation with survival a/b holds. The latter was already the preceding threshold converse.

The all-input identities follow on the input operator basis |i><j|, not just for excitation populations. They tensorize and commute with any instrument on D. In particular, conditioning on a rank-one helper result X leaves the environment output E obtainable from B using the *same* damping map, independent of X.

### General statement and two converse bounds

Consider any finite-dimensional isometry A -> B E D satisfying

\[
N_{ED}=(\mathcal T_{B\to E}\otimes\mathrm{id}_D)N_{BD}
\tag{A3}
\]

for a quantum channel T. Under exactly the communication rules above, the capacity is

\[
\boxed{
Q_{D\to B}^{\rm meas}
=\max_{\rho_A}\bigl\{\min[S(B),S(BD)]-S(E)\bigr\}.
}
\tag{A4}
\]

All entropies use base two. The minimum-cut expression is a known assistance lower bound [DH11]; what has to be proved here is its converse and single-letter saturation under (A3). We do not claim a new entanglement-of-assistance protocol.

For an arbitrary input on n uses, purify it with R. After a rank-one helper measurement with classical outcome X, each R B^n E^n branch is pure. The induced channel has coherent information

\[
I_c=S(B^n|X)-S(E^n|X).
\]

By (A3), X--B^n--E^n obeys data processing. Hence

\[
I_c=S(B^n)-S(E^n)
-\{I(X;B^n)-I(X;E^n)\}
\le S(B^n)-S(E^n).
\tag{A5}
\]

Independently, treating the helper measurement as processing of the hypothetical quantum output B^nD^n yields

\[
I_c\le S(B^nD^n)-S(E^n).
\tag{A6}
\]

This second cut is sharper than merely bounding by the input entropy. A preliminary calculation retained the looser input-entropy cut; that true but non-tight result is archived, not relabeled as the final rate.

Both differences D1(rho)=S(B)-S(E) and D2(rho)=S(BD)-S(E) are concave functions of the input. For example, use an isometric dilation B->EF of T to express the first as S(F|E). For the second, the channel BD->E is T after discarding D, so the same conditional-entropy argument applies. Both are subadditive on many-use inputs: total correlations cannot increase under the corresponding product degrading channel. Consequently,

\[
D_j^{(n)}(\rho_{A^n})\le\sum_iD_j(\rho_{A_i})
\le nD_j\left(\frac1n\sum_i\rho_{A_i}\right),\quad j=1,2.
\tag{A7}
\]

Combining (A5)--(A7) bounds arbitrary collective helper channels and encodings by the right side of (A4). Standard regularized coherent-information transmission converses supply the usual vanishing-error coding step. The helper's refined record is part of the output; it is not discarded before applying the converse.

### Achievability does not grant access to the inaccessible field

Fix rho_A, purify with R, and regard the pure R B E D output *mathematically* as a tripartite state with parties B, (RE), and D. The established regularized pure-state assistance theorem [SVW05, Theorem 1] supplies rank-one block measurements on D^n for which

\[
\sum_xp_x S(B^n_x)\ge
n\{\min[S(B),S(RE)]-\epsilon\}
=n\{\min[S(B),S(BD)]-\epsilon\}.
\tag{A8}
\]

This statement is about the ensemble created by a measurement on D. It requires **no physical operation on E or on the combined mathematical party RE**. Concavity separately gives

\[
\sum_xp_xS(E^n_x)\le nS(E).
\]

Thus the actual flagged channel A^n->B^nX has coherent information at least n times the expression in (A4), minus n epsilon. Freeze that helper block measurement and apply ordinary channel coding over repeated such blocks. The classical label goes only to the receiver. This is the flagged-channel step used in [SVW05, Theorem 8], not an import of unrestricted two-way distillation from [DH11].

For the qubit splitter, output phase covariance and concavity allow phase twirling of rho without reducing either D1 or D2. Put rho=diag(1-q,q). The three relevant entropies are

\[
S(B)=h_2(aq),\quad S(E)=h_2(bq),\quad S(BD)=h_2((a+c)q).
\]

This proves (A1) in the a>=b region. For a<=b, the reversed register-preserving degradation makes every helper-induced block channel antidegradable, proving zero capacity as in the baseline. The degenerate endpoints follow directly, with no division by zero.

## A2. Rates, limiting cases and what the collective measurement buys

The previous exact photon-counting rate remains

\[
Q_{\rm count}=\max_q\left\{
H_3[1-(a+c)q,aq,cq]
-H_3[1-(b+c)q,bq,cq]\right\}
\]

in the positive region, and zero otherwise. For r=0.8:

| Collection eta | Counting capacity | Exact monitored capacity | Optimizing population for monitored capacity |
|---:|---:|---:|---:|
| 0.75 | 0 | 0 | — |
| 0.76 | 0.0104567 | 0.0162756 | 0.9920635 |
| 0.80 | 0.0544870 | 0.0868919 | 0.9615385 |
| 0.90 | 0.1862104 | 0.3057095 | 0.8928571 |
| 1.00 | 0.4056852 | 0.6500224 | 0.8333333 |

These are qubits per input, not recovered excitation probabilities. At eta=.9, q*=25/28 and Q=h2(5/28)-h2(1/14). The numerical optimizer agrees with that kink value. The printed decimals are numerical evaluations, not certified intervals or finite-code performance.

At c=0, the two cuts coincide and the formula reduces to the ordinary degradable amplitude-damping capacity. At b=0, it reduces to the known fully environment-assisted expression max min{S(input),S(output)} [SVW05]. With no damping it is one. At a=b it vanishes, despite possible surviving output-reference entanglement. The counting formula reaches the same positive/zero boundary but need not attain the best positive rate.

The expression contains no efficiency bound for the block POVM or code. Joint processing of collected radiation over many uses is a substantial coherent-memory/control resource at the helper. Only its message to B is classical. A finite photon-counter implementation is not claimed to attain the last column.

## A3. Two consequences that sharpen the resource boundary

### Finite-message fidelity on the zero-capacity side

For a<=b, any code followed by any allowed block measurement and decoding has a symmetric extension with equal decoded marginals. For a d-dimensional logical message, the two maximally entangled projectors obey

\[
\|\Phi_{RB}\otimes I_{B'}+\Phi_{RB'}\otimes I_B\|_\infty=1+1/d.
\]

The unconditional entanglement fidelity therefore satisfies

\[
\boxed{F_e\le\frac{d+1}{2d}.}\tag{A9}
\]

For a single logical qubit the bound is 3/4, regardless of how many physical uses encode it. This is a standard cloning/shareability consequence [W98] applied to every helper-induced channel, not a new general cloning bound. We do not claim it is tight for each splitter. It is not an average state-fidelity bound with the same numeric value, and it is not conditioned on a favorable outcome. Free two-way communication, heralded postselection or feedback during decay changes the task.

### The positive/zero boundary also survives a harmonic carrier

Replace the two-level carrier explicitly by an oscillator passing through the same passive vacuum splitter. On number states,

\[
|n\rangle\mapsto\sum_{i+j+k=n}
\sqrt{\frac{n!}{i!j!k!}}a^{i/2}b^{j/2}c^{k/2}|i,j,k\rangle.
\]

Attenuating the larger B or E output still reproduces the smaller while leaving D intact. On coherent-input dyads this follows by multiplying the vacuum-loss overlap factors; normality and totality extend the identity to the whole Fock space. Tests through four input photons verify every input matrix unit, not just number distributions, but the all-Fock statement relies on that analytic argument.

For a<=b all allowed helper channels are antidegradable at every finite input-energy budget. For a>b, a sufficiently small excited population in the {|0>,|1>} subspace gives positive counting coherent information while respecting any strictly positive mean-energy budget. Therefore the same zero/positive boundary holds. **No exact energy-constrained bosonic capacity formula is proved here.** Environment-assisted schemes that prepare nonvacuum states in an incoming reservoir port [V26] use a different resource, not a counterexample.

## A4. What the source audit establishes

[SVW05] supplies the fundamental pure-state assistance and full-environment capacity results. [DH11, Theorem 8] already gives the mixed-state minimum-cut coherent-information lower bound min{I(RD>B),I(R>BD)}. The lower bound is therefore inherited; the proof here identifies a register-preserving degrading condition under which no collective helper measurement or block input can beat it, and evaluates the resulting rate for partial amplitude damping.

The earlier perfect-detection jump-channel construction [G10] does not supply partial detection in its inspected capacity formula. [A03] explicitly studies imperfect error-record labels, unequal decay, correction delay and detector dead time for finite codes with recovery during the evolution. It is a serious imperfect-monitoring predecessor, but not the same no-intervention, helper-measurement channel task. Its correction resources must not be erased when comparing thresholds.

[PDB21]'s inspected classical-conferencing section concerns classical messages; its quantum communication section introduces a quantum link between receivers. [HK05]'s corrected qubit-capacity statement concerns classical information, not a contradiction of zero quantum transmission here. [KFG20] develops flagged-extension capacity bounds, with generalized amplitude damping among its applications; its inspected constructions do not establish the physical partially observed splitter rate. None of these selected passages is an exhaustive literature certificate.

The theorem should now receive a focused proof and exact-prior-art audit, not be downgraded merely because it uses standard assistance or entropy inequalities. Conversely, an original-looking compact formula alone does not establish PRL significance. No independent reviewer report or completed physical-assumption benchmark is claimed. The candidate's central physics is the exact amount of quantum information recoverable from partial environmental measurement without coherent return of the field.

