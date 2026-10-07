# Verification policy

The scientific derivations are analytical and author-side. Passing the tests is reproducibility evidence, not an independent proof review or priority certificate.

## Unchanged baseline

Four original scripts and their exact reference reports are copied from the supplied consolidation. There are 23 scientific groups: 6 threshold/counting, 7 qubit-rate, 6 optical-audit and 4 consolidation. Their original assertions and tolerance values are unchanged. The largest matrices in the source record are finite diagnostic models, not full coding simulations.

Seventy imported files/excerpts, including the owner's license, are pinned by byte count and SHA-256 in provenance/IMPORT_MANIFEST.json. The original 110-member input archive was validated before the monitoring-only selection; no claim is made that all 110 members were imported. The eight new infrastructure tests are counted separately from the science.

## Fresh run

`python verify.py --output-dir NEW_DIRECTORY` refuses an existing directory. It records before/after integrity, exact source hashes, the tracked source ZIP, Python/dependency versions, every original log and report, and field-by-field comparisons against the preserved references. The result identifies the actual local commit and staged source tree. The runner never regenerates originals.

An assertion pass, numerical agreement and byte equality are separate report fields. A report may pass while recording nonidentical floating-point bytes. All changed fields, including small diagnostics, remain visible.

For cross-environment comparisons, finite float values use relative tolerance **1e-9** and absolute tolerance **2e-11**. This policy was fixed before the initialization runs. It is additional to, not a replacement for, each original suite's assertions. Types, shapes, dictionary keys, strings, Boolean values and integers must match exactly; nonfinite values are rejected. A discrepancy is not permission to refresh a reference or weaken an original test.

## Local versus hosted

The initial chat could read GitHub but had no write action, and its attempted local clone failed DNS. Local commits and this workflow file do not establish a remote push, PR, CI run or merge. The workspace must perform those actions and inspect their actual outcomes.

The hosted workflow checks out the PR head or push SHA, uses read-only repository permissions, installs the pinned dependencies, and uploads raw verification artifacts even after a failure. Review the artifact's commit, source hashes, protected-file checks, all original assertion outcomes and every report difference. After merging, inspect the actual merged-main run separately.

The workflow uses established major versions rather than claiming to pin immutable action SHAs. Infrastructure references checked during initialization: [checkout](https://github.com/actions/checkout), [setup-python](https://github.com/actions/setup-python), and the [CLI merge head-matching option](https://cli.github.com/manual/gh_pr_merge). This documentation check is not a fresh scientific literature audit.

No forced merge, administration override, automatic reference refresh or private credential is included.
