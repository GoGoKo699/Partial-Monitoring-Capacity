# Partial Monitoring Capacity

**Quantum transmission limits when only part of the environment can be observed.**

A lossy quantum signal is divided among a receiver, an inaccessible environment, and a collected field. A helper may process the collected field coherently and measure it, but sends only a classical record to the receiver. This project determines the resulting asymptotic quantum transmission rate for a class of channels and evaluates it for qubit decay and vacuum optical loss.

The central distinction is **received information versus permanently unobserved loss**. At fixed nonzero unobserved loss, increasing signal energy cannot remove the optical rate ceiling. Collecting more of the lost field can raise that ceiling. Collective quantum processing at the helper is an allowed resource; a practical receiver attaining the limit is not supplied.

Start with [the physical picture](research/PHYSICAL_PICTURE.md): why the receiver can obtain only 20% of the signal and still transmit quantum information, and how the exact rate translates into a collection requirement.

## The result under study

Let $V:A\to B\otimes E\otimes D$ be a memoryless isometry. The receiver has $B$, the inaccessible environment is $E$, and the helper holds $D$. The hypothesis is the **joint channel identity**

```math
\mathcal N_{ED}=(\mathcal T_{B\to E}\otimes\mathrm{id}_D)\mathcal N_{BD}.
```

It must preserve the correlations with $D$ for every input, including reference-entangled inputs. Marginal degradability alone is insufficient. Under this condition, the supplied author-side theorem is

```math
Q_{\rm meas}=\max_{\rho_A}\left[\min\{S(B),S(BD)\}-S(E)\right].
```

The achievable assistance bound and coding tools are inherited. The proposed contribution is their exact saturation under the joint-register condition. [The theorem and proof](research/THEOREM.md) separates those attributions and states the resources precisely.

For vacuum optical splitting, let $a,b,c$ be the received, unobserved-loss and collected fractions, with $a+b+c=1$. With mean incident signal energy $N$ photons per original mode,

```math
Q_{\rm optical}(N)=
\begin{cases}
g(aN)-g(bN),&a>b,\\
0,&a\le b,
\end{cases}
\qquad g(x)=(x+1)\log_2(x+1)-x\log_2x.
```

The positive-rate boundary is $a>b$. For $a>b>0$, increasing signal energy approaches the ceiling $\log_2(a/b)$. The input constraint is an average photon budget, not a maximum photon number per codeword or total apparatus-energy budget. The qubit example has its own single-variable entropy optimization; photon counting reaches its positivity boundary but need not attain its optimal rate.

For the qubit model with $a>b>0$ and $c>0$, [photon counting is optimal among all predetermined product helper POVMs](research/EXACT_PRODUCT_CAPACITY_2026-10-07.md), even with arbitrary input coherence and sender/receiver block codes. At $(a,b,c)=(0.2,0.08,0.72)$, that capacity is about $0.18621044$ qubits/use, while unrestricted helper measurements attain about $0.30570954$. The gap is certified at about $0.11949910$ qubits/use. Outcome-adaptive local strategies remain outside this comparison.

## Reading route

| File | Purpose |
|---|---|
| [Physical picture](research/PHYSICAL_PICTURE.md) | The physical question, one example, collection requirements, and contribution boundary. |
| [Contribution assessment](research/CONTRIBUTION_ASSESSMENT_2026-10-07.md) | Continue/stop judgment, the two missing prior-work implications, and the limits of the physical claim. |
| [Model and claims](research/MODEL_AND_CLAIMS.md) | Resource definition, result hierarchy, proof dependencies, and limitations. |
| [Theorem](research/THEOREM.md) | Consolidated finite-dimensional proof and both physical examples. |
| [Proof audit](research/PROOF_AUDIT.md) | Refined measurement complement, general encoders, and deficit identity. |
| [Current claim assessment](research/CLAIM_ASSESSMENT_2026-10-07.md) | Direct converse for unresolved helper outputs and continuous records; unchanged rates. |
| [Product helper gap](research/PRODUCT_HELPER_GAP_2026-10-07.md) | All-input product capacity reduction and analytical strict separation in the qubit example. |
| [Exact product capacity](research/EXACT_PRODUCT_CAPACITY_2026-10-07.md) | Optimality of photon counting over all predetermined product POVMs, with an exact-arithmetic rate and gap certificate. |
| [Optical audit](research/OPTICAL_AUDIT.md) | Preserved optical derivation, including the finite-support entropy bounds. |
| [Prior art](literature/PRIOR_ART.md) and [targeted comparison](literature/PRIORITY_CHECK_2026-10-07.md) | Closest constructions, inherited ingredients, and actual reading depth. |
| [Status](STATUS.md) and [workspace](WORKSPACE.md) | Current evidence, unresolved tasks, and handoff. |

The theorem is an **author-side research claim**, not an independently reviewed result. Finite matrix tests check identities and evaluations; they do not prove coding theorems or establish global priority. No manuscript, release, or implemented code is included.

## Reproduce

The supplied environment is Python **3.13.5**. Install the pinned dependencies, then use a fresh evidence directory:

```bash
python -m pip install -r requirements.txt
python verify.py --integrity-only
python -m unittest discover -s tests -v
python verify.py --output-dir local-evidence-001
python checks/certify_product_capacity.py --output local-evidence-001/product-capacity-certificate.json
```

There are **23 monitoring check groups** in four unchanged suites: 6 threshold/counting, 7 exact qubit rate, 6 optical audit, and 4 consolidation checks. The separate product-capacity certificate uses exact rational arithmetic to enclose the scalar optimum and gap. The runner stores raw logs, numerical comparisons, environment details and source hashes. It never refreshes the original reports. [Verification policy](VERIFICATION.md) distinguishes assertions, numerical agreement, and exact-byte reproduction.

The source import is monitoring-only. Shared pilot notes are included only as explicitly identified monitoring excerpts; the spin/strip code and data remain outside this repository. No unrelated publication PDF is included. [Provenance](provenance/IMPORT_MANIFEST.json) records every protected copy and the exclusions from the supplied archive.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The owner's existing [MIT license](LICENSE) is preserved.
