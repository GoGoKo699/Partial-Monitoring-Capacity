# Contribution assessment: exact limits and the detector benchmark

**7 October 2026. Decision: retain and advance the completed contribution; stop scientific expansion for now.** The exact product optimum strengthens the result materially. The contribution is a precise capacity theorem and resource comparison in a restricted, physically motivated channel class. It is not the discovery that environmental observation or collective assistance can help.

This is an author-side assessment of the results through [the exact product-capacity proof](EXACT_PRODUCT_CAPACITY_2026-10-07.md). Parallel assistant critiques informed it; they are not independent scientific review. The focused source checks below do not establish global priority.

## The physical lesson

A signal is split between the receiver, permanently inaccessible loss, and a collected field. The helper measures the collected field and sends only a classical record to the receiver. For the stated vacuum-loss models, transmission becomes possible when the received fraction exceeds the inaccessible fraction. In the qubit model, photon counting already reaches that positive-capacity boundary.

Above that boundary, the question becomes how much rate an individual detector can recover. For the qubit family with $a>b>0$ and $c>0$, optimizing every predetermined single-use helper POVM cannot beat photon counting, even with coherent inputs and arbitrary sender/receiver block codes. In the example below, the larger unrestricted capacity therefore cannot be obtained merely by selecting a better independent-use detector basis.

| Qubit example: $(a,b,c)=(0.2,0.08,0.72)$ | Capacity, qubits/use |
|---|---:|
| Best predetermined product helper measurements, attained by counting | $0.18621044$ |
| Unrestricted collective helper measurements | $0.30570954$ |
| Difference | $0.11949910$ |

The approximately 64% increase illustrates the exact comparison; its size is not the novelty argument. These are asymptotic rates, not single-photon recovery probabilities. Collective processing improves the rate in this example, not the positive-capacity boundary. Adaptive local measurements and general separable block POVMs remain outside the product benchmark, so necessity of coherent helper memory has not been established.

The optical evaluation adds a complementary lesson: at fixed splitting fractions $a>b>0$, more signal energy approaches the ceiling $\log_2(a/b)$; reducing that loss can raise the ceiling. This is an exact consequence of the capacity theorem for vacuum splitting, not an independent discovery about all monitored noise. The qubit product-optimality theorem has not been proved for the optical model.

## The two substantive implications

**Exact partial-access converse.** Under the joint channel identity

```math
\mathcal N_{ED}=(\mathcal T_{B\to E}\otimes\mathrm{id}_D)\mathcal N_{BD},
\qquad
Q_{\rm meas}=\max_\rho[\min\{S(B),S(BD)\}-S(E)].
```

The identity preserves the helper register and correlations with references. It permits an upper bound matching the inherited assistance lower bound while retaining inaccessible $E$, collective helper measurements and correlated encodings. Marginal simulation alone does not suffice. [The theorem](THEOREM.md) and [direct converse assessment](CLAIM_ASSESSMENT_2026-10-07.md) supply the channel and general-encoder arguments.

**Exact product optimum.** For the interior qubit family,

```math
\sup_{\rho,M} I_c(\rho,\mathcal N_M)
=Q_{\rm prod}=\max_{0\le q\le1}(1-cq)
\left[h_2\!\left(\frac{aq}{1-cq}\right)-h_2\!\left(\frac{bq}{1-cq}\right)\right].
```

Here $M$ ranges over all single-use helper POVMs; predetermined choices may vary across uses. Degradable-channel additivity connects this optimization to the full product-helper capacity with arbitrary endpoint codes. The nontrivial measurement comparison uses common branch determinants, convexity of $e(\alpha r)-e(\beta r)$, and a chord bound. For a coherent input it gives $I_c\le(q/\widetilde q)F(\widetilde q)\le\max_s F(s)$. Counting attains the final maximum. This is global optimality after input optimization, not a claim of counting optimality for every fixed coherent input.

## What the predecessors do and do not supply

The earlier [priority comparison](../literature/PRIORITY_CHECK_2026-10-07.md) retains the central resource comparison and reading limits. The following targeted checks address the completed package.

| Primary result and inspected passage | Inherited content and missing implication |
|---|---|
| [Smolin–Verstraete–Winter, quant-ph/0505038](https://arxiv.org/pdf/quant-ph/0505038), Theorems 1 and 8; Section III, Example 4 | Assistance regularization, measurement followed by ordinary channel coding, receiver-only signaling, and collective gains are established. Full-environment assistance does not itself retain an inaccessible output in the present matching converse. |
| [Dutil–Hayden, 1011.1972](https://arxiv.org/pdf/1011.1972), operational task, Propositions 5–6 and Theorem 8 | The mixed-state assistance min-cut lower bound is inherited. Its recipient-LOCC task permits two-way distillation. The inspected results do not supply this receiver-only channel equality; one must not identify two-way distillable entanglement with coherent information merely from degradability. |
| [Grassl–Ji–Wei–Zeng, 1008.3350](https://arxiv.org/pdf/1008.3350), Eqs. (5)–(8), (16), and concluding paragraph | Perfect-detection counting has a degradable flagged capacity; its rate below full environment assistance is explicitly recognized. This does not optimize every product POVM with residual inaccessible loss. Persistence of some counting gap for small positive residual loss is unsurprising by continuity; the exact partial-access and all-POVM optima are the additions. |
| [Kianvash–Fanizza–Giovannetti, 2008.02461](https://arxiv.org/pdf/2008.02461), Proposition 3.1, Sections 6–7 | Chosen flagged degradable extensions upper-bound an unassisted channel. This is not an ordering of all physical helper measurements; the paper leaves optimal Kraus choice unresolved. |
| [Uhlmann, quant-ph/0605103](https://arxiv.org/pdf/quant-ph/0605103), Section 5, Eqs. (51)–(54), Theorem 3 | A rank-two entropy infimum convex roof does not maximize a shared entropy difference generated by one helper measurement. The inherited entropy–concurrence tools and the required difference-convexity step are separated in the exact-product proof. |
| [Ouyang, 1106.2337](https://arxiv.org/pdf/1106.2337), Theorem IV.1 and Corollary IV.3 | Covariance permits symmetry-averaged inputs for a fixed degradable covariant channel. It does not justify diagonalizing the joint input/POVM optimization when an arbitrary chosen measurement breaks covariance. |
| [Pollock–Wang–Chitambar, 2010.11431](https://arxiv.org/pdf/2010.11431), Section II.B and Theorem III.4 | Single-copy entropy assistance and its failure to saturate asymptotic cuts further establish the qualitative collective/local distinction. The assisted outputs there are pure bipartite states, not the present states retaining inaccessible $E$ and objective $S(B_x)-S(E_x)$. |
| [Pereg, 2411.16263v2](https://arxiv.org/pdf/2411.16263v2), introduction, Definition 3, Theorems 3–5 | The Hadamard equality and measure-/assist-forward bounds concern classical messages, with an active relay input. They do not give this entanglement-transmission capacity. Definitions and results were inspected, not the full appendix proofs. |

These checks used primary parsed text at the specified passages. No covering implication was found there. Different titles, failed searches and numerical tests are not evidence of novelty.

## Strongest objection and decision

The serious objection is that the result combines familiar assistance and degradability in a clean splitting model. That objection has force: the lower bound and coding method are inherited; the central equality is a concise resource-specific synthesis, not a new coding mechanism. The joint-register hypothesis is restrictive. It nevertheless follows from ordinary attenuation over the vacuum-splitter region $a\ge b$, rather than from a new assistance resource.

The exact product theorem answers a further question that this synthesis alone leaves open. It closes the explanation that counting was simply a poor detector choice, throughout the stated interior qubit family. Together, the two exact optimizations separate inaccessible-loss limitations from the limitations of predetermined independent-use readout. That is sufficient to retain and advance this bounded theoretical contribution. It does not establish broad significance by itself, an efficient collective receiver, or an experimental advantage at finite code length.

**Stop additional numerical refinement, model extensions and broad scouting.** No extra digits or larger measurement class are needed to make this judgment. The one next task is the author's review of this brief alongside the two proofs, deciding which physical claim deserves emphasis. The scientific scope stays frozen during that review; this assessment initiates no manuscript, external contact or release.
