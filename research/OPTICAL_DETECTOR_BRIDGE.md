# From the qubit optimum to optical detector resources

[Overview](../README.md) · [Preskill bridge](PRESKILL_READING_MAP.md) · [Milestones M28–M30](LEARNING_MILESTONES.md)

Partial Monitoring establishes the exact unrestricted helper capacity and, for
the vacuum/one-photon qubit family, the optimal predetermined individual
measurement. The sister Optical Detector Capacity project uses the optical
capacity as its benchmark and asks which detector operations and apparatus
resources approach it. This page connects the results; their proofs remain in
their respective authoritative homes.

All companion links below are pinned to
[Optical Detector Capacity revision c3582795](https://github.com/GoGoKo699/Optical-Detector-Capacity/tree/c3582795f208bfa287d53db2458ca710cefeb6f7).
Both projects use **Preskill, Quantum Shannon Theory, Chapter 10, arXiv v5** as
the sole educational anchor. The [four local bridges](PRESKILL_READING_MAP.md)
provide the channel, complement, converse and coding language needed here.

## Keep the common task and translate notation

Both projects use a vacuum splitter with fractions $`a,b,c`$ sent respectively to
the receiver, an inaccessible field and a helper. The helper sends a classical
record only to the receiver. Endpoint block codes are unrestricted and the
transmission rate is unconditional per original channel use.

| Object | Partial Monitoring | Optical Detector Capacity |
|---|---|---|
| Receiver and helper outputs | $`B,D`$ | $`B,D`$ |
| Inaccessible output | $`E`$ | $`Z`$ |
| Mean incident signal photons | $`N`$ | $`E`$ |
| Useful signal scale | $`L=\min\{N,1/b\}`$ | $`L=\min\{E,1/b\}`$ |
| Mean initial reference photons per use | Unrestricted apparatus resource | $`M`$ in the priced local-reference model |

The companion's signal-energy variable $`E`$ is not this project's inaccessible
quantum register. In both conventions $`1/0=\infty`$.

## From one photon to two

On the vacuum/one-photon input space, this project's
[all-input product theorem](EXACT_PRODUCT_CAPACITY_2026-10-07.md) proves that
counting is optimal over every predetermined individual helper POVM. Throughout
$`a>b>0,c>0`$, collective helper measurements nevertheless give a strictly
higher capacity. Both sides permit arbitrary endpoint codes.

The companion's [two-photon example](https://github.com/GoGoKo699/Optical-Detector-Capacity/blob/c3582795f208bfa287d53db2458ca710cefeb6f7/science/qubit_optical_bridge.md)
changes the allowed input support to vacuum through two photons. At
$`(a,b,c)=(1/5,2/25,18/25)`$, it certifies

```math
Q_{\rm cnt}^{[2]}<0.318,\qquad R_{\pm}^{[2]}>0.329
```

in qubits per original use. The detector resolves $`|1\rangle`$ and the two
superpositions $`(|0\rangle\pm|2\rangle)/\sqrt2`$. Its average coded input
is the equal mixture of $`|1\rangle`$ and $`|2\rangle`$. Thus the first higher
photon cutoff already permits an individual detector to beat every counting code
under that same cutoff.

This is a photon-cutoff statement, not a minimum input-subspace-dimension
theorem: the displayed input itself uses two number states. Nor is its counting
upper bound an upper bound for the full oscillator under only a mean budget.

## The full oscillator separates number coherence from collective processing

With no peak cutoff and only the mean incident budget, the inherited collective
capacity is $`g(aN)-g(bN)`$ when $`a>b`$. The companion's
[uniform optical laws](https://github.com/GoGoKo699/Optical-Detector-Capacity/blob/c3582795f208bfa287d53db2458ca710cefeb6f7/science/uniform_laws.md)
give, at fixed $`0\lt a\lt 1`$, $`N\ge1`$ and
$`0\le b\le\tfrac12\min\{a,1-a\}`$,

```math
Q_{\rm cnt}(N)=\tfrac12\log_2L+O_a(1),\qquad
Q_1(N)=Q_{\rm coll}(N)+O(1)=\log_2L+O_a(1).
```

Here $`Q_1`$ permits predetermined arbitrary POVMs on individual collected
modes. Across all finite energies, the difference between the best such
individual measurements and the collective benchmark is at most $`\log_2e`$
qubits per mode. Counting can lose an unbounded amount as $`L`$ grows.

The [structured detector proof](https://github.com/GoGoKo699/Optical-Detector-Capacity/blob/c3582795f208bfa287d53db2458ca710cefeb6f7/science/coherent_measurements.md)
uses coherence between photon numbers within one mode. Its selected Fourier
measurement is fixed before transmission and needs no coherent memory across
collected modes. This explains why counting's qubit optimum does not extend to
the oscillator. It does not contradict the qubit collective advantage or show
that every number-coherent detector is good.

## When the local reference is priced

The unrestricted optical detector class supplies a phase reference and coherent
control without charging their initial energy. The companion's
[mean-reference theorem](https://github.com/GoGoKo699/Optical-Detector-Capacity/blob/c3582795f208bfa287d53db2458ca710cefeb6f7/science/reference_mean_bounds.md)
instead includes a prepared reference $`W_i`$ at each collected mode. Effective
helper effects commute with **each** local total
$`N_{D_i}+N_{W_i}`$. The references are initially independent of the encoded
signal and its logical reference; their mean initial photons are bounded by
$`M`$ per use on average. No support or variance constraint is imposed.

Using this page's signal variable $`N`$, its energy-driven profile is

```math
Q_{\rm loc}^{\rm mean}(N,M)
=\min\!\left\{\log_2N,
\max\!\left\{\tfrac12\log_2N,\log_2(M+1)\right\}\right\}+O_a(1).
```

The domain is $`N\ge1`$, fixed $`0\lt a\lt 1`$,
$`0\le b\le\tfrac12\min\{a,1-a\}`$ and $`bN\le1`$, so $`L=N`$.
Retaining the full logarithmic rate within a fixed additive gap requires and
admits initial mean reference stock of order $`N`$. The converse retains the
actual logical reference and arbitrary correlated endpoint codes. The
[direct construction](https://github.com/GoGoKo699/Optical-Detector-Capacity/blob/c3582795f208bfa287d53db2458ca710cefeb6f7/science/direct_reference.md)
uses fresh finite sine references and keeps the discarded reference in the true
complement, just as the copied record must be kept in the qubit calculation.

The local conservation condition is substantive. Commuting only with the sum
over all modes permits a larger class, and a reference reused after becoming
signal-correlated is outside the stated contract. Prepared stock is different
from preparation work, net energy consumption and reset cost. Classical records
are unrestricted in this profile; it does not optimize a simultaneous record
and reference budget or assert the same necessity when $`N\gg L`$.

## Follow the proof appropriate to the question

| Question | Authoritative route |
|---|---|
| Why are joint helper measurements strictly better in the qubit interior? | This project's [capacity theorem](THEOREM.md) and [exact product optimum](EXACT_PRODUCT_CAPACITY_2026-10-07.md). |
| Why does optical counting cease to be the best individual detector? | Companion [cutoff example](https://github.com/GoGoKo699/Optical-Detector-Capacity/blob/c3582795f208bfa287d53db2458ca710cefeb6f7/science/qubit_optical_bridge.md) and [uniform laws](https://github.com/GoGoKo699/Optical-Detector-Capacity/blob/c3582795f208bfa287d53db2458ca710cefeb6f7/science/uniform_laws.md), with their distinct input domains. |
| How much local prepared reference energy is needed? | Companion [mean-reference bound and construction](https://github.com/GoGoKo699/Optical-Detector-Capacity/blob/c3582795f208bfa287d53db2458ca710cefeb6f7/science/reference_mean_bounds.md), under separate local invariance. |
| What does the evidence certify? | The [Partial Monitoring verification policy](../VERIFICATION.md) and [companion verification account](https://github.com/GoGoKo699/Optical-Detector-Capacity/blob/c3582795f208bfa287d53db2458ca710cefeb6f7/verification/README.md); finite checks and analytical proofs have different roles. |

The sister results add detector and apparatus comparisons. They leave this
project's authoritative capacity theorem, product benchmark and operational
assumptions intact.
