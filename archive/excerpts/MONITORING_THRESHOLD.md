## A. How much quantum information can classical monitoring rescue?

### A1. Operational model

A qubit undergoes zero-temperature amplitude damping during a fixed interval. Let r be the probability that an initially excited qubit decays, and eta the physically collected fraction of its radiation. Define

\[
a=1-r,\qquad b=(1-\eta)r,\qquad c=\eta r,\qquad a+b+c=1.
\]

B denotes the surviving qubit, E the uncollected field and D the collected field. Each field can be represented by its vacuum and one emitted-wavepacket state. The stipulated Stinespring isometry is

\[
|0\rangle\mapsto |000\rangle_{BED},\qquad
|1\rangle\mapsto\sqrt a|100\rangle+\sqrt b|010\rangle+\sqrt c|001\rangle.
\tag{A1}
\]

The sender may encode across independent uses. A helper may make any measurement, including a joint measurement on D from an arbitrarily large block, and send its result classically to the receiver. The receiver may decode conditioned on that result. The helper does not deliver D as a quantum system or interact with the emitter during decay. No sender–receiver pre-entanglement, two-way-assisted entanglement distillation, control feedback during the interval, or free noiseless quantum channel is supplied. Locally prepared measurement ancillas do not change the converse.

Q_mon is the asymptotic quantum transmission rate per input qubit with this measurement-only helper. Positive Q_mon means that a nonzero rate of unknown quantum data can be transmitted with vanishing error using large codes. It does not specify a finite-block fidelity or an efficient practical code.

The collected fraction eta is an access restriction before the otherwise ideal measurement, rather than an outcome-dependent detector efficiency. Different collection geometries that alter the emission law are outside (A1).

### A2. A measurement-independent zero/positive boundary

**Result.** In (A1),

\[
\boxed{Q_{\rm mon}>0\quad\Longleftrightarrow\quad a>b
\quad\Longleftrightarrow\quad r<\frac1{2-\eta}.}
\tag{A2}
\]

This includes optimization over collective measurements of the collected field. It does not determine the value of Q_mon throughout the positive region.

**Converse.** For a<=b, the channel to BD is obtained from the channel to ED by amplitude damping E with survival a/b, leaving D unchanged:

\[
\rho_{BD}=(\mathcal A_{a/b}\otimes\mathrm{id}_D)(\rho_{ED}).
\tag{A3}
\]

Here E is relabeled as B after the map. The identity holds as a channel identity and hence with every reference system and every input, not just diagonal populations. It follows directly by matching the vacuum population, the B–D or E–D single-excitation block, and their coherences. The special a=b=0 endpoint is trivial.

Tensoring (A3) proves the same identity for n uses with D^n intact. Any measurement instrument acting on D^n commutes with the amplitude-damping map on E^n. Conditional on each outcome, the inaccessible E^n state therefore simulates the receiver's B^n state by the same map. The classical outcome can be copied into the complementary output of the induced channel; any residual helper quantum system can be discarded. Every such measured block channel is consequently antidegradable.

An antidegradable channel has zero unassisted quantum capacity by the standard no-cloning/data-processing argument [A2]. This argument applies at every blocklength, so permitting collective helper measurements cannot circumvent it. Feedback or additional assisted communication tasks were not included in the channel definition.

**Achievability.** Photon counting D one use at a time produces the flagged channel below. For a>b it is degradable and has strictly positive coherent information for a sufficiently small excited-state input population. Ordinary channel coding supplies a positive rate. Together the two directions prove (A2).

The prospective physical statement is: the boundary is determined by survival relative to *uncollected* emission, not by improving the downstream measurement basis indefinitely.

### A3. Exact photon-counting capacity

Counted output labels can be represented by the qutrit states |0,no click>, |1,no click>, and |0,click>. The channel is

\[
\mathcal N_{a,b,c}(\rho)=
\begin{pmatrix}
\rho_{00}+b\rho_{11}&\sqrt a\,\rho_{01}&0\\
\sqrt a\,\rho_{10}&a\rho_{11}&0\\
0&0&c\rho_{11}
\end{pmatrix}.
\tag{A4}
\]

One Kraus choice is

\[
K_0=|0\rangle\langle0|+\sqrt a|1\rangle\langle1|,
\quad K_1=\sqrt b|0\rangle\langle1|,
\quad K_2=\sqrt c|2\rangle\langle1|.
\]

Its complementary channel is exactly N_(b,a,c). For a>=b, an additional amplitude damping with survival b/a on the 0–1 block, preserving the flag, degrades N to its complement. For a<=b the converse construction is an antidegrading map. Endpoint cases with zero weights are evaluated by continuity or directly.

Degradability, additivity and concavity of coherent information are established channel results [A2]. Phase covariance permits averaging away input coherences. With h3 denoting Shannon entropy in bits,

\[
Q_{\rm count}=\max_{0\le q\le1}
\bigl[h_3(1-(a+c)q,aq,cq)-h_3(1-(b+c)q,bq,cq)\bigr],\quad a>b.
\tag{A5}
\]

For a<=b the capacity is zero. The small-q leading term is (a-b)q log2(1/q), proving positivity when a>b. The arbitrary-measurement converse in A2 does not use an assumed optimal counting basis.

At r=0.8, selected evaluations are:

| Collected fraction eta | Q_count (qubits/input) |
|---:|---:|
| 0.50 | 0 |
| 0.75 | 0 |
| 0.80 | 0.0544870167364 |
| 0.90 | 0.186210444566 |
| 1.00 | 0.405685231376 |

These interior maxima are scalar numerical evaluations, not rigorous numerical intervals. The threshold and single-letter expression are analytic.

**Counting is not generally optimal above the boundary.** With full environmental access, a known environment-assistance theorem gives max_rho min{S(rho),S(N(rho))} [A3,A4]. For an amplitude-damping qubit of survival a this is h2(a/(1+a)). At a=.2, full collective environmental measurement can attain approximately .650022421648, whereas per-use counting attains .405685231376. This agrees with the distinction already made in the detected-jump paper [A1].

### A4. A sharp difference between a classical record and quantum collection

If the receiver obtains B and D coherently, their one-excitation amplitudes can be combined unitarily. The channel is ordinary amplitude damping with survival a+c=1-b, whose quantum capacity is positive for b<1/2.

At (a,b,c)=(.1,.2,.7), every measurement-only helper strategy has zero rate by (A2). Coherent quantum collection instead gives Q=.506215240927 qubits/input. No claim is made that a device can losslessly implement this collection; it is a control demonstrating that the restriction to a classical record is meaningful.

Nor does zero Q mean the monitored state is separable. The counted channel's Choi partial-transpose negativity is

\[
\mathcal N_{\rm Choi}=\frac{\sqrt{b^2+4a}-b}{4},
\]

positive whenever a>0. It is .115831239518 in the example. Postselected entangled branches, two-way distillation and positive unassisted quantum rate are different claims.

For r=1-exp(-Gamma t) and eta<1, the positive-rate interval ends at

\[
\Gamma t_* =\ln\frac{2-\eta}{1-\eta}.
\tag{A6}
\]

At eta=0 this is ln2; at eta=.9 it is ln11, a factor 3.45943 larger. This is a boundary for independent fixed-duration channels with asymptotic encoding, not a demonstrated fault-tolerant memory lifetime. At eta=1 every finite t has positive rate, but the rate goes to zero as t goes to infinity.

### A5. Prior art and remaining novelty question

The detected-jump channel and perfect photon-count records are established [A1]. Its inspected Eqs.(5)–(8) use a flag for every jump; they do not add an unobserved emission branch. Its paper already distinguishes that fixed-basis capacity from full environment assistance. We must not claim the first monitored communication channel, first degradability calculation, or first distinction between classical and coherent field access.

The full-environment capacity theorem [A3,A4] assumes access to the whole complementary output. The loss of access to E is why it does not directly answer (A2). Recent monitored-dynamics work also studies incomplete monitoring and information persistence in different chaotic/many-body settings [A5]; the existence of a monitoring threshold is not generically new.

The particular item to audit next is the *measurement-independent partial-access boundary* (A2), including collective measurements and the register-preserving identity (A3). It is not enough to search only for our formula or only for “detected jump.” The present comparison supports continued investigation, not first-priority certification or a forecast of publication acceptance. No broad error-correction construction or full mixed-temperature capacity problem is needed to evaluate this specific claim.

