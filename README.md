# Partial Monitoring Capacity

**Even the best predetermined individual measurements can leave quantum transmission capacity unused.**

A lossy quantum signal reaches a receiver, an inaccessible environment and a collected
field. A helper measures the collected field and sends only a classical record to the
receiver. How much quantum information can that record recover, and when do joint
measurements recover more than the best measurements made one output at a time?

| Read next | Purpose |
|---|---|
| [Physical picture](research/PHYSICAL_PICTURE.md) · [Preskill reading guide](research/PRESKILL_READING_MAP.md) | Start from the physical question and one tutorial, then work through four local bridges |
| [Capacity theorem](research/THEOREM.md) · [Exact product optimum](research/EXACT_PRODUCT_CAPACITY_2026-10-07.md) | Follow both sides of the individual-versus-collective measurement comparison |
| [Model and claims](research/MODEL_AND_CLAIMS.md) · [Proof dependencies](research/PROOF_DEPENDENCIES.md) | Check the resources, supporting claims and corrected attribution |
| [Prior-work comparison](literature/PRIORITY_CHECK_2026-10-07.md) · [Contribution assessment](research/CONTRIBUTION_ASSESSMENT_2026-10-07.md) | Separate established ingredients from the measurement optimization |
| [Verification](#evidence-and-reproduction) · [Status](STATUS.md) · [LLM guide](llms.txt) | Inspect evidence and locate authoritative material by question |

## What the helper can access

A memoryless isometry $`V:A\to B\otimes E\otimes D`$ divides each input into three outputs.

| Output | Who holds it | Available operation |
|---|---|---|
| $`B`$ | Receiver | Arbitrary quantum decoding with the helper's record |
| $`E`$ | Inaccessible environment | No access |
| $`D`$ | Helper | Quantum processing and measurement; a classical message only to the receiver |

The sender and receiver may use arbitrary block codes. The unrestricted helper may
store and jointly measure many collected outputs. The product benchmark permits every
single-use POVM, with choices fixed in advance and allowed to vary between uses.
Outcome-adaptive local measurements and general separable block POVMs are outside that
benchmark.

The rate is asymptotic, unconditional entanglement transmission per original channel
use. No preshared entanglement, sender feedback, coherent helper link or postselection
is supplied.

## Counting is already the best individual measurement

For qubit splitting, let $`a,b,c`$ be the received, inaccessible and collected fractions,
with $`a+b+c=1`$. Throughout $`a>b>0,\ c>0`$, photon counting attains the largest capacity
over all predetermined product helper POVMs and all inputs, including coherent inputs.

At $`(a,b,c)=(0.2,0.08,0.72)`$:

| Helper measurement resource | Capacity, qubits/use |
|---|---:|
| Best predetermined individual measurements, attained by counting | $`0.18621044`$ |
| Unrestricted joint measurements | $`0.30570954`$ |
| Certified difference | $`0.11949910`$ |

Both rows allow arbitrary sender/receiver block codes. A better predetermined
single-use detector cannot close this example's gap. Counting already reaches the
positive-capacity boundary $`a>b`$; the demonstrated collective benefit is a higher rate.
The [exact product proof](research/EXACT_PRODUCT_CAPACITY_2026-10-07.md) supplies the
optimization over all measurements. It establishes counting optimality after input
optimization, rather than for every fixed coherent input.

## Why the capacity is exact

The receiver must be able to simulate the inaccessible output while preserving its
correlations with the helper. The required **joint channel identity** is

```math
\mathcal N_{ED}
=(\mathcal T_{B\to E}\otimes\mathrm{id}_D)\mathcal N_{BD}.
```

It holds for every input, including inputs entangled with a reference. Marginal
degradability alone is insufficient. Under this condition,

```math
\boxed{
Q_{\rm meas}
=\max_{\rho_A}\left[\min\{S(B),S(BD)\}-S(E)\right].
}
```

Both finite-dimensional upper bounds follow from the established one-way distillation
theorem for degradable states after regrouping registers. A known assistance ensemble,
followed by ordinary channel coding, attains their minimum. The
[dependency record](research/PROOF_DEPENDENCIES.md) supplies the reduction and preserves
the correction to the earlier converse attribution. The separate product optimum
still requires its determinant and convexity argument.

## Inaccessible optical loss imposes an energy ceiling

For vacuum optical splitting, an average incident budget of $`N`$ photons per original
mode gives

```math
Q_{\rm optical}(N)=
\begin{cases}
g(aN)-g(bN),&a>b,\\
0,&a\le b,
\end{cases}
\qquad
g(x)=(x+1)\log_2(x+1)-x\log_2x.
```

For $`a>b>0`$, increasing signal energy approaches $`\log_2(a/b)`$ qubits per mode.
At positive energy the positive-rate boundary is $`a>b`$. The budget is an average
signal-energy constraint, not a peak photon-number or apparatus-energy constraint;
the environmental inputs remain vacuum. The [optical proof](research/PROOF_DEPENDENCIES.md)
includes arbitrary correlated, non-Gaussian inputs. The qubit counting-optimality
result does not extend to optical measurements here.

## One tutorial, then these results

The sole external teaching anchor is:

> John Preskill, **Quantum Shannon Theory**, Chapter 10, 2025 revision.
>
> [Versioned text, arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5) ·
> [Author chapter](https://www.preskill.caltech.edu/ph219/chap10_6A_2025.pdf)

The [reading guide](research/PRESKILL_READING_MAP.md) selects the entropy, classical-record,
degradability and coding sections. Four local bridges then explain the extra steps:

| Bridge | What the repository adds |
|---|---|
| Measurement record | A worked counting example, the copied classical flag and the actual complement |
| Exact unrestricted rate | The two cuts, their common input, established state-converse attribution and matching helper construction |
| Optimal individual measurement | Arbitrary input coherence, the convex chord bound and counting saturation |
| Optical energy limit | Thermal entropy, the all-input converse and the order of cutoff and coding limits |

The chapter supplies the common language. Original research papers retain their
attributions; the guide explains their role locally without adding another required
tutorial. The chapter is linked, not redistributed.

## Boundaries and prior work

The helper's quantum memory, circuit complexity, phase references and classical message
length are unrestricted. An efficient collective helper, a finite-block implementation
and a necessity theorem against all adaptive local strategies are not established.
The [model and claim map](research/MODEL_AND_CLAIMS.md) states these boundaries precisely.

Environmental assistance and collective-assistance gains have established predecessors.
The capacity consequence and exact product benchmark are distinguished in the
[contribution assessment](research/CONTRIBUTION_ASSESSMENT_2026-10-07.md).
The results remain author-side research claims; numerical checks do not prove coding
theorems or establish independent review or exhaustive priority.

## Evidence and reproduction

The supplied environment is Python **3.13.5**. Install the pinned dependencies and
use a fresh evidence directory:

```bash
python -m pip install -r requirements.txt
python verify.py --integrity-only
python -m unittest discover -s tests -v
python verify.py --output-dir local-evidence-001
python checks/certify_product_capacity.py --output local-evidence-001/product-capacity-certificate.json
```

Four preserved scientific suites contain **23 monitoring groups**: 6 threshold/counting,
7 exact qubit rate, 6 optical audit and 4 consolidation checks. The eight infrastructure
tests are separate. The rational certificate encloses the example's scalar product rate
and gap; it does not prove the analytical optimization over POVMs.

The runner retains logs, environments, source hashes and every comparison difference
without refreshing reference reports. [Verification policy](VERIFICATION.md) distinguishes
passing assertions, numerical agreement and exact-byte reproduction.
[Provenance](provenance/IMPORT_MANIFEST.json) identifies all 70 protected imports and the
excluded material. The separate spin/strip project remains outside this repository.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [LLM guide](llms.txt) gives relevant questions, search phrases and authoritative reading
links. The [workspace](WORKSPACE.md) and [current work order](work_orders/CURRENT.md) guide
repository maintenance. The owner's [MIT license](LICENSE) is preserved.
