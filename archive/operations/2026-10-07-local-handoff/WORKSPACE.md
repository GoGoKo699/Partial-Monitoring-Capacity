# Workspace handoff

**Target:** `GoGoKo699/Partial-Monitoring-Capacity`.

**Permission:** the owner authorized modifying the repository and merging. Preserve its existing visibility and license. Work in this repository only.

## First finish the pending publication operation

This initialization was prepared locally because the chat exposed no GitHub write action and the container could not resolve github.com. **There is no merged initialization PR yet.** The external handoff package contains an exact Git bundle, a reviewable patch, local verification reports and IMPORT_HANDOFF.md. The bundle is rooted at the verified initial remote commit `9243513e6c8f5dee31977180743e3f6f44a9d613`.

In a write-enabled workspace, read the live remote `main`, branch list and open PRs first. Import the bundle's `initialize/monitoring-workspace` branch. If remote main has moved, inspect those changes and reconcile without forcing or overwriting them. Do not duplicate an initialization already published by another session.

Run the source-integrity, infrastructure and all four scientific suites in fresh output directories. Review the diff, push only the feature branch and open a PR against main. Inspect the actual workflow results and their evidence. Merge through the repository's permitted strategy without bypassing checks. Fetch merged main and validate that revision; record the PR, merge SHA, source tree and outcomes in STATUS.md or a follow-up record.

The prepared `.github/workflows/verify.yml` is read-only with respect to repository contents. It uploads raw reports and their source hash list on success or failure. A workflow file is not evidence that any hosted execution has occurred. Local success does not substitute for remote verification.

## Then enter the scientific work

Read [MODEL_AND_CLAIMS](research/MODEL_AND_CLAIMS.md), [THEOREM](research/THEOREM.md), [PROOF_AUDIT](research/PROOF_AUDIT.md), [PRIOR_ART](literature/PRIOR_ART.md) and [CURRENT](work_orders/CURRENT.md).

This is one consolidated theorem with two solved physical examples, not a request to restart broad scouting. The next pass is a targeted correctness/priority assessment of the equality and its actual resource assumptions. It should not automatically become finite-temperature theory, finite-code design, an experiment or a new helper architecture.

The unchanged archive and monitoring-only excerpts are provenance. Their historical status and earlier loose bounds do not override the active consolidated claim. The spin pilot remains outside this repository. No reviewer has been contacted, and no independent referee report is implied by the local tests.
