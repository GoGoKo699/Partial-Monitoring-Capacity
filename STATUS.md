# Results and verification record

The repository contains an exact partial-environment measurement-assisted capacity
theorem, its qubit and vacuum optical evaluations, and an exact benchmark for
predetermined individual helper measurements.

| Result | Authoritative account |
|---|---|
| Unrestricted helper-assisted capacity under the joint-register identity | [Theorem](research/THEOREM.md) · [proof dependencies](research/PROOF_DEPENDENCIES.md) |
| Photon counting optimizes all predetermined product helper POVMs in the interior qubit family | [Exact product capacity](research/EXACT_PRODUCT_CAPACITY_2026-10-07.md) · [product reduction](research/PRODUCT_HELPER_GAP_2026-10-07.md) |
| Strict individual-versus-collective rate comparison | [Physical picture](research/PHYSICAL_PICTURE.md) · [contribution and predecessors](research/CONTRIBUTION_ASSESSMENT_2026-10-07.md) |
| Vacuum optical energy law and all-input converse | [Optical dependencies](research/PROOF_DEPENDENCIES.md#3-optical-identity-and-photon-budget-coding) · [direct converse](research/CLAIM_ASSESSMENT_2026-10-07.md) |
| Fixed resources and result boundaries | [Model and claims](research/MODEL_AND_CLAIMS.md) |

## Reproducibility evidence

The [verification policy](VERIFICATION.md) defines the four preserved scientific
suites, eight infrastructure tests and separate rational certificate. Numerical
agreement, exact-byte reproduction and analytical proof are distinct findings.

Every maintenance PR records the inspected head revision and a separate actual
merged-main revision, their workflow runs, source-matched artifacts and all report
differences. Use the [merged PR records](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/pulls?q=is%3Apr+is%3Amerged)
for revision-specific receipts and the [Actions runs](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/actions)
for their retained artifacts. A receipt for an earlier revision is not evidence for
a later one.

The [initialization receipt](provenance/TAKEOVER_VERIFICATION_2026-10-07.json) retains
the original source-matched takeover evidence. The
[archived status and handoff](archive/editorial/2026-10-07-pre-release/README.md)
preserve the subsequent chronology and the superseded qualitative product-gap route.
[Import provenance](provenance/IMPORT_MANIFEST.json) pins all 70 protected imports.

## Reading and maintenance

Start with the [README](README.md) and [Preskill reading guide](research/PRESKILL_READING_MAP.md).
[WORKSPACE](WORKSPACE.md) and the [maintenance checklist](work_orders/CURRENT.md)
describe how to preserve and verify this repository. Historical decisions and work
instructions belong to the archive, rather than the current scientific reading route.
