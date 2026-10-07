# Status

**7 October 2026 — initialization and bounded claim assessment merged; physical reading guide completed.**

The repository is `GoGoKo699/Partial-Monitoring-Capacity`. [PR #1](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/pull/1) merged the prepared monitoring-only import as `a9d953cd95410fc6add5c047e89133c8b7369ff8`, with source tree `4ca9e3b55b286ebd65fa20fbf7fe180ec776e14c`. Public visibility and the owner's MIT license are unchanged.

The local handoff commit `c7fa61ec1c9157a8f608231399c11254d84f245a` and published feature commit `f8fd17de13160a0ca5c9a81ef3aa51a0a8674bd6` have the same source tree and initial parent. GitHub created a distinct commit because local Git push credentials were unavailable. These identities are not interchangeable. The original dated [local-only status](archive/operations/2026-10-07-local-handoff/STATUS.md), [workspace instructions](archive/operations/2026-10-07-local-handoff/WORKSPACE.md), and [work order](archive/operations/2026-10-07-local-handoff/CURRENT.md) remain historical records.

## Verification actually inspected

| Revision | Hosted run | Outcome |
|---|---|---|
| PR #1 head `f8fd17d` | [37584432025](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/actions/runs/37584432025) | Eight infrastructure tests and all 23 scientific groups passed; all 94 source hashes matched the reviewed tree. |
| Merged main `a9d953c` | [37584672815](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/actions/runs/37584672815) | Separately inspected with the same successful checks and source match. |

The hosted reports agree numerically but are **not byte-identical** to the original references. All 136 changed fields are finite floating-point differences within the existing policy; the largest absolute difference is `3.552713678800501e-15`. The two hosted runs produced identical scientific report bytes to each other. Local runs on the prepared, published and merged revisions reproduced all four reference reports byte for byte. Protected source files, reference reports and tolerances were not changed.

[The verification receipt](provenance/TAKEOVER_VERIFICATION_2026-10-07.json) retains commit/tree identities, source hashes, environments, reports, raw scientific execution logs and every hosted comparison difference. These receipts concern the initialization revisions above; later revisions require their own workflow evidence.

The takeover verified 70 protected imports. The source catalog enumerates 109 files; the initial record reports 110 ZIP members. The original ZIP was not recounted during takeover, so that historical total is not a new verification claim.

## Scientific conclusion

The claim assessment was merged in [PR #2](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/pull/2) as `aa60f70d99831b13e46b71e882f1674c4084604a`, tree `be2db6d2367a41ba4699eeaf3fe09d76a2ccb71c`. Its separate [merged-main run](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/actions/runs/37585678407) passed eight infrastructure tests and all 23 scientific groups. The downloaded evidence matched all 100 source files; all four reports were byte-identical to references in that run. The PR record retains the exact verification receipt. Earlier initialization discrepancies above remain historical observations of different runs.

[The targeted assessment](research/CLAIM_ASSESSMENT_2026-10-07.md) finds no correction to the central equality or its physical evaluations. Its direct converse retains both discarded encoder ancillas and unresolved helper outputs. Finite partitions of a continuous classical record avoid relying on a rank-one refinement theorem in the optical converse. Rank-one refinement remains explicit for the exact coherent-information and deficit identities.

[The priority comparison](literature/PRIORITY_CHECK_2026-10-07.md) identifies close precedents for the entropy method and for partial environmental access. None of the inspected theorem passages directly supplies the same conditional capacity equality. This is a bounded author-side assessment, not exhaustive priority clearance or independent peer review.

## Next work

[The physical picture](research/PHYSICAL_PICTURE.md) completes the requested exposition: observed versus unobserved loss, the energy ceiling at fixed loss fractions, and the collection needed for a target rate. The threshold and rate formulas are unchanged. The guide explicitly distinguishes allowing collective processing from proving it necessary.

[CURRENT](work_orders/CURRENT.md) records a possible bounded follow-up in the same qubit model: determine whether a general individual-use helper measurement can attain the unrestricted optimum. This is an unresolved resource question, not a prerequisite for the established capacity theorem. No new model, manuscript, release or external contact is initiated here.
