# Partial observation, individual detectors and collective measurements

A helper collects part of a lost quantum signal and sends a measurement record
to the receiver. The question is how much quantum transmission that record can
recover, and whether the best individual detector leaves rate available to joint
measurements of many collected outputs.

The [physical picture](physical_picture.md) starts with the three output fields
and a complete qubit example. The [model](model.md) fixes the communication
resources, unconditional transmission task and claim domains. The proofs then
separate two optimizations: the unrestricted helper capacity and the best
predetermined product helper measurement. Both permit arbitrary endpoint block
codes.

## Follow the scientific argument

| Step | Scientific account | What connects it to the next step |
|---|---|---|
| 1 | [Physical picture](physical_picture.md) and [model and claims](model.md) | Collection determines access; the helper supplies only a classical record to the receiver. |
| 2 | [Exact unrestricted capacity](capacity.md) | A joint channel identity preserves the helper's correlations and makes the established assistance lower bound exact. |
| 3 | [Proof dependencies](proof_dependencies.md), [coarse helper records](coarse_records.md), and [complements and deficits](complements_and_deficits.md) | These retain the actual complement, general encoding ancillas, both converse cuts, continuous records and the optical energy limits. |
| 4 | [Product-helper reduction](product_reduction.md) and [exact measurement optimum](product_measurements.md) | Degradability covers arbitrary endpoint codes; the separate determinant and convexity argument optimizes every predetermined single-use helper POVM and every input. |
| 5 | [Strict interior comparison](product_measurements.md#4-strict-collective-advantage-throughout-the-qubit-interior) | Counting is already the best individual qubit measurement, yet the unrestricted helper rate is strictly larger throughout the stated interior region. |
| 6 | [Contribution and prior-work boundary](contribution.md) and [optical sister bridge](optical_detector_bridge.md) | These distinguish the inherited capacity ingredients, the qubit measurement optimization and the optical detector and apparatus questions. |

The qubit comparison concerns rates above the same positive-capacity boundary.
It does not establish necessity of coherent helper memory against adaptive local
strategies. The optical capacity evaluates the same unrestricted principle under
a mean signal-energy constraint; qubit counting optimality does not extend to
optical measurements. The sister bridge identifies which result transfers and
which input and apparatus assumptions change.

## Study and check the account

The [learning route](../learning/README.md) connects the settled 30 milestones
to the sole Preskill Chapter 10 anchor and four worked bridges. The
[source route](../references/README.md) gives the supporting passages and
attribution boundaries. The [verification route](../verification/README.md)
separates analytical proof, finite diagnostics and the exact scalar certificate.

Return to the [repository overview](../README.md).
