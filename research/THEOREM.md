# Quantum transmission with partial environmental observation

The joint-register identity makes an established assistance lower bound exact.
Both finite-dimensional converse cuts follow from Leditzky–Datta–Smith [LDS17]
through the [register reduction](PROOF_DEPENDENCIES.md). The
[direct coarse-record converse](CLAIM_ASSESSMENT_2026-10-07.md) and
[optical dependencies](PROOF_DEPENDENCIES.md#3-optical-identity-and-photon-budget-coding)
supply the finite-energy extension. The separate
[exact product optimum](EXACT_PRODUCT_CAPACITY_2026-10-07.md) establishes counting
optimality and the qubit individual-versus-collective rate comparison. Adaptive
local strategies remain outside the product benchmark.

## 1. Physical question and communication model

A quantum signal is divided among a receiver, a collected field, and an inaccessible environment. How much quantum information can be recovered when the collected field can be measured but not transmitted coherently?

Let a memoryless finite-dimensional channel be specified by an isometry

$$V:A\longrightarrow B\otimes E\otimes D.$$

The receiver obtains B; E is inaccessible; a helper controls D. For n uses the helper may implement an arbitrary joint POVM on D^n and send its outcome X only to the receiver. The sender uses a predetermined encoder; the receiver decodes B^nX. There is no preshared entanglement, quantum helper link, intervention during the channel, feedback, or sender–receiver distillation side channel. Every trial and outcome, including declared failure outcomes, contributes to the unconditional transmission error.

The helper may use coherent quantum storage, arbitrary non-Gaussian operations where appropriate, and phase references. Classical message length, helper circuit size, and storage duration are not constrained. The capacity Q_meas is the asymptotic entanglement-transmission rate per original channel use. It is not a finite-code recovery probability or an implemented quantum-memory lifetime.

The required hypothesis is the **joint channel identity**

$$\mathcal N_{ED}=(\mathcal T_{B\to E}\otimes\mathrm{id}_D)\mathcal N_{BD},\tag{1}$$

for a trace-preserving completely positive map T. This is equality on all input operators, hence with arbitrary references, not just equality on a selected ensemble. In particular, T preserves the correlations with D. Ordinary marginal degradation N_E=T N_B is insufficient.

## 2. Exact finite-dimensional rate

**Theorem.** Under (1),

$$\boxed{Q_{\mathrm{meas}}=\max_{\rho_A}\left[\min\{S(B),S(BD)\}-S(E)\right].}\tag{2}$$

Entropies are in bits and evaluated on V rho V^dagger. The minimum-cut assistance lower bound is inherited from assistance theory [SVW05, DH11]. The matching finite-dimensional upper bounds follow from the degradable-state theorem [LDS17] with register groupings RFD:B and RF:BD; common-input single-letterization gives (2). See [the explicit reduction](PROOF_DEPENDENCIES.md).

### Proof: measured channel and its actual complement

A helper POVM can be refined into rank-one effects without reducing achievable transmission: the receiver can ignore the extra classical label. Write its rows as m_x, with sum_x m_x^dagger m_x=I, and put W_x=(I_BE tensor m_x)V^tensor n. A dilation of the resulting flagged channel is

$$J=\sum_x W_x\otimes|x\rangle_X|x\rangle_Y.$$

The receiver has B^nX. A complementary output is E^nY. Tracing either copy of the classical label eliminates cross terms, so both are classical–quantum block states. Equation (1) gives, for every input and outcome,

$$\mathcal N_M^c=(\mathcal T^{\otimes n}\otimes\mathrm{id}_{X\to Y})\mathcal N_M.$$

Thus **every refined measured block channel is degradable**, not only the photon-counting channel. With a purifying reference R, its coherent information is exactly

$$I_c(\rho,\mathcal N_M)=S(B^n|X)-S(E^n|X).\tag{3}$$

For a coarse measurement this formula cannot generally subtract E alone: an unrefined part of the helper/environment must also be included in the complement. Refinement is a proof reduction, not permission to erase that information without consequence.

### Two upper bounds

The same degrading map relates the conditional E and B states. Data processing gives I(X;E^n)<=I(X;B^n), and therefore

$$I_c\le S(B^n)-S(E^n).\tag{4}$$

Sending BD coherently would be a stronger receiver resource. Processing that output into B^nX cannot increase coherent information, so also

$$I_c\le S(B^nD^n)-S(E^n).\tag{5}$$

For j=1,2 define D_1(rho)=S(B)-S(E) and D_2(rho)=S(BD)-S(E). Each is concave: dilate the relevant degrading map isometrically to E F and write the difference as S(F|E). Each is subadditive across uses because total correlations decrease under the product degrading map. Consequently, for rho_i the input marginals and bar-rho their average,

$$D_j^{(n)}(\rho_{A^n})\le\sum_iD_j(\rho_i)\le nD_j(\bar\rho),\qquad j=1,2.$$

Taking the minimum of (4) and (5) yields n times the right side of (2), including arbitrarily correlated input states and collective helper measurements.

There is no hidden restriction to isometric encoders. Dilate a general encoder using a discarded ancilla F, so the pre-channel RFA state is pure. For a refined helper outcome, the difference between purified-input coherent information and the actual message coherent information is S(F|E^nX). The complementary channel is antidegradable; it has a symmetric extension with two identical E^nX marginals. Weak monotonicity of conditional entropy therefore gives S(F|E^nX)>=0. Discarding F cannot evade the upper bound. The usual coherent-information transmission converse then applies [DS05, WQ18]. This paragraph makes explicit a coding step previously delegated to the standard theorem.

### Achievability with a receiver-only classical message

Fix rho_A and purify it by R. Apply the pure-state assistance ensemble theorem to the mathematical grouping B | (RE) | D. For any epsilon>0, a sufficiently large block admits a rank-one measurement on D^n such that

$$\sum_xp_xS(B_x^n)\ge n\bigl[\min\{S(B),S(BD)\}-\epsilon\bigr].$$

This asserts the existence of a measurement ensemble; it requires no physical operation on RE. Independently, entropy concavity gives sum_x p_x S(E_x^n)<=n S(E). The actual flagged channel therefore has coherent information at least n times (2)'s objective minus n epsilon.

Freeze that finite block measurement. Standard quantum coding over repeated uses of the resulting flagged channel achieves its coherent information. The unknown message is never supplied to the helper, and its outcome goes only to the decoder. This is the flagged-channel construction of [SVW05, Theorem 8], with the partial-environment subtraction explicitly retained. It is not a substitution of the broader two-recipient LOCC task of [DH11]. Maximizing over rho proves (2). Pure inputs give an objective of zero, so the maximum is nonnegative. No capacity strong-converse exponent is asserted. Continuous classical outcomes are interpreted through conditional cq entropies (or measurable limits), not subtraction of divergent differential entropies; the constructive finite-cutoff measurements can be chosen with finite classical alphabets.

## 3. Qubit decay: exact rate and irreversible boundary

For

$$|0\rangle\mapsto|000\rangle_{BED},\qquad
|1\rangle\mapsto\sqrt a|100\rangle+\sqrt b|010\rangle+\sqrt c|001\rangle,$$

let a be survival, b inaccessible decay, and c collected decay; a+b+c=1. When a>=b, amplitude damping B with survival b/a gives (1). When a<=b, the reverse identity makes every helper-induced channel antidegradable. Thus

$$\boxed{Q_{\mathrm{qubit}}=\begin{cases}
\displaystyle\max_{0\le q\le1}\{\min[h_2(aq),h_2((1-b)q)]-h_2(bq)\},&a>b,\\
0,&a\le b.
\end{cases}}\tag{6}$$

Phase covariance and concavity justify the diagonal input diag(1-q,q). Positivity is equivalent to a>b. For exponential damping, a=1-r, b=(1-eta)r, so the threshold is r<1/(2-eta). This compares surviving and permanently lost excitation, not merely detector quality after collection.

Counting the collected photon gives the previously established flagged channel with output populations 1-(a+c)q, aq, cq and complementary populations 1-(b+c)q, bq, cq. Its capacity is the maximum difference of their ternary entropies when a>b. Counting reaches the positivity boundary but not the full optimal rate. At (a,b,c)=(.2,.08,.72), Q_count=.18621044 while (6) gives .30570954 qubits/use. Full collection b=0 recovers the established environment-assisted endpoint [SVW05, DJ10].

Equation (6) needs only one scalar root or the entropy-crossover point. Set q_c=1/(1+a-b). For q<=q_c the active expression is h2(aq)-h2(bq); above q_c it is h2((1-b)q)-h2(bq). The right piece is nonincreasing from q_c onward. If

$$a\log_2\frac{1-aq_c}{aq_c}-b\log_2\frac{1-bq_c}{bq_c}\ge0,$$

the optimum is q_c. Otherwise the unique zero of that derivative on (0,q_c) is the optimum. Terms multiplied by b=0 are interpreted by their limit. This is an evaluation corollary, not another capacity theorem. At the example above q_c=25/28.

On the zero-capacity side, antidegradability also supplies an unconditional finite-message ceiling F_e<=(d+1)/(2d) for a d-dimensional logical message. In particular, F_e<=3/4 for one logical qubit at every blocklength. This is the standard shareability/no-cloning argument, not a tight error formula for every parameter or a postselection statement. The prior proof is preserved in the [monitoring-rate excerpt](../archive/excerpts/QUANTUM_RATE.md), Section A3.

## 4. Vacuum optical loss: exact energy-constrained rate

For a passive optical splitter with vacuum at every unused input,

$$\hat A^\dagger\mapsto\sqrt a\,\hat B^\dagger+\sqrt b\,\hat E^\dagger+\sqrt c\,\hat D^\dagger,$$

and mean incident photon budget N per original mode, the result is

$$\boxed{Q_{\mathrm{optical}}(N)=\begin{cases}
g(aN)-g(bN),&a>b,\\
0,&a\le b,
\end{cases}\quad
g(x)=(x+1)\log_2(x+1)-x\log_2x.}\tag{7}$$

The energy constraint is on the encoded signal averaged over the message state and channel uses, not a maximum photon number per codeword or a total apparatus-energy budget. Thermal optimality describes the **average coded input**, not an uncoded thermal signal or a nonvacuum bath.

The passive network gives the joint identity (1) over the complete Fock space using additional loss b/a on B. It is not only a Gaussian covariance identity. For an arbitrary n-mode encoded input of actual mean bar-N<=N,

$$S(B^n)-S(E^n)
=n[g(a\bar N)-g(b\bar N)]-\Delta_{\mathrm{th}},$$

$$\Delta_{\mathrm{th}}=
D(\rho_{B^n}\Vert\tau_{a\bar N}^{\otimes n})-
D(\rho_{E^n}\Vert\tau_{b\bar N}^{\otimes n})\ge0.$$

The thermal-reference logarithm and mean output energies give the equality; relative-entropy contraction under additional loss gives the inequality. This is the established thermal-reference extremality method [WQ18], now applied after the helper-compatible converse. It includes non-Gaussian input states and entanglement across modes.

For achievability, truncate the thermal average input, not competing codes, at photon number K. With r=N/(1+N), the retained normalized distribution has mean

$$N_K=N-\frac{(K+1)r^{K+1}}{1-r^{K+1}}<N.$$

For fixed K, vacuum loss leaves finite output support; apply the finite-dimensional assistance construction and then energy-constrained channel coding [WQ18, Theorem 2] to the fixed flagged block channel with its summed photon-number Hamiltonian and strict energy slack. Only afterward let K grow. The discarded thermal tail has probability epsilon_K=r^(K+1) and conditional mean K+1+N. Entropy-of-mixture bounds enclose the output entropies and prove convergence to (7), rather than assuming entropy continuity from trace-distance convergence. The full coding application and finite-cutoff minimum are explicit in [PROOF_DEPENDENCIES](PROOF_DEPENDENCIES.md); the original entropy bounds and numerical checks remain in [archived optical audit](../archive/original/prior/AUDIT.md), Section 4.3. The converse is never cutoff-restricted. Cases b=0, N=0 and vanishing port weights follow directly.

For a=.2,b=.08,N=1, the capacity is .3686045934 qubits/mode. At N=10 it is .9709505945. For b>0 and a>b,

$$Q(N)\nearrow\log_2(a/b),\qquad
Q''(N)=\frac{b-a}{\ln2\,N(1+aN)(1+bN)}<0.$$

The .2/.08 example has a large-energy ceiling log2(2.5)=1.321928095. Additional power cannot remove an uncollected-loss ceiling or move the a=b threshold. With b=0 the rate g(aN) is not bounded as N grows. Coherent delivery of D instead gives ordinary pure-loss capacity with survival 1-b; it is a different resource, not an alternative measurement in this theorem.

## 5. A proof identity clarifies what remains unrecovered

For any fixed refined measurement on n optical outputs, define

$$\Delta_{\mathrm{meas}}=I(X;B^n)-I(X;E^n)\ge0.$$

For a>b>0 and finite budget N,

$$\boxed{
nQ(N)-I_c
=\underbrace{n[Q(N)-Q(\bar N)]}_{\text{unused signal energy}}
+\underbrace{\Delta_{\mathrm{th}}}_{\text{entropy-difference deficit}}
+\underbrace{\Delta_{\mathrm{meas}}}_{\text{measurement deficit}}.
}\tag{8}$$

All terms are nonnegative. This is a rearrangement of the already used equalities, not a new independent capacity law. It separates deficient average inputs from deficient helper measurements. In particular, for an exact thermal product input at budget N, the finite-block coherent-information gap is exactly Delta_meas. The capacity-achieving sequence makes this gap sublinear in n. Simply collecting a more detailed photon record is not a proof that the best rate is reached.

Equation (8) is not a finite-code fidelity formula and does not say that discarding parts of a classical record improves performance. Once the outcome is coarsened, an additional unresolved helper system appears in the complement, and (3)'s E-only subtraction need not apply. For a=.2,b=.08,c=.72,q=.5, ignoring the helper gives negative coherent information, although the incorrect E-only subtraction would be positive. The separate check makes this distinction explicit.

Likewise, replacing (1) by marginal degradability is invalid: the standard random-phase example with a key in D is perfectly correctable by reading the key although the inaccessible marginal is a fixed state. Its joint ED correlations cannot be obtained by acting on B with D untouched [GW03]. Neither example contradicts the theorem.

## 6. Attribution and scope

The main claim is **exact saturation of a known assistance lower bound under a register-preserving degradation condition**, with computable qubit and photon-budget examples. Its finite-dimensional converse is a resource-specific application of established degradable-state theory [LDS17]. Environment-assisted communication, the assistance minimum cut, coherent-information coding, thermal-reference extremality and the no-cloning bound are inherited.

The [dependency correction](PROOF_DEPENDENCIES.md) supersedes the earlier assessment that the matching converse required an additional new inequality. The separate [exact product-capacity proof](EXACT_PRODUCT_CAPACITY_2026-10-07.md) still requires optimization over every predetermined single-use helper measurement and every input. The inspected state-decomposition minima do not supply that maximum. This bounded comparison is **not exhaustive priority clearance**.

The theorem specifies asymptotic entanglement transmission with unrestricted helper processing, a receiver-only classical record and vacuum environmental inputs in the optical model. Its operational scope is given in [MODEL_AND_CLAIMS](MODEL_AND_CLAIMS.md); its evidence policy is in [VERIFICATION](../VERIFICATION.md).

### Sources

[LDS17] F. Leditzky, N. Datta and G. Smith, *Useful states and entanglement distillation*. https://arxiv.org/abs/1701.03081v4 — Definition 2.2 and Proposition 2.4, including the optimized single-copy one-way statement; supplies both finite-dimensional converse cuts through the register reduction above.

[SVW05] J. A. Smolin, F. Verstraete and A. Winter, *Entanglement of assistance and multipartite state distillation*, PRA 72, 052317 (2005). https://arxiv.org/abs/quant-ph/0505038 — Theorems 1 and 8 and the ensemble/flagged-channel proofs.

[DH11] N. Dutil and P. Hayden, *Assisted Entanglement Distillation*. https://arxiv.org/abs/1011.1972 — Theorem 8 and the two-recipient LOCC model. Its lower bound is credited, not imported with extra communication permissions.

[WQ18] M. M. Wilde and H. Qi, *Energy-constrained private and quantum capacities of quantum channels*, IEEE TIT 64, 7802–7827 (2018). https://arxiv.org/abs/1609.01997 — energy-constrained converse/coding and thermal-reference extremality, especially Theorems 2, 5 and 6.

[DS05] I. Devetak and P. W. Shor, *The capacity of a quantum channel for simultaneous transmission of classical and quantum information*, CMP 256, 287–303 (2005). https://arxiv.org/abs/quant-ph/0311131 — degradable-channel coherent information. The explicit encoder-ancilla argument above is also derived directly.

[DJ10] M. Grassl, Z. Ji, Z. Wei and B. Zeng, *Quantum Capacity Approaching Codes for the Detected-Jump Channel*, PRA 82, 062324 (2010). https://arxiv.org/abs/1008.3350 — perfect detected-jump records and associated codes; active bibliography checked against the primary record.

[GW03] M. Gregoratti and R. F. Werner, *Quantum Lost and Found*, J. Mod. Opt. 50 (2003). https://arxiv.org/abs/quant-ph/0209025 — random-unitary correction scope control.

[BD13] F. Buscemi and N. Datta, *General theory of environment-assisted entanglement distillation*, IEEE TIT 59, 1940–1954 (2013). https://arxiv.org/abs/1009.4464 — the helper holds the entire purification; no claim of an imperfect-access converse imported.

[OMW21] S. Khabbazi Oskouei, S. Mancini and A. Winter, *Capacities of Gaussian Quantum Channels with Passive Environment Assistance*. https://arxiv.org/abs/2101.00602 — primary abstract only: helper controls the incoming environment state, not this output measurement.
