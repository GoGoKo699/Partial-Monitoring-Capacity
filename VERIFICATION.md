# Verification policy

The scientific derivations are analytical and author-side. Passing the tests is reproducibility evidence, not an independent proof review or priority certificate.

## Unchanged baseline

Four original scripts and their exact reference reports are copied from the supplied consolidation. There are 23 scientific groups: 6 threshold/counting, 7 qubit-rate, 6 optical-audit and 4 consolidation. Their original assertions and tolerance values are unchanged. The largest matrices in the source record are finite diagnostic models, not full coding simulations.

Seventy imported files/excerpts, including the owner's license, are pinned by byte count and SHA-256 in provenance/IMPORT_MANIFEST.json. The original 110-member input archive was validated before the monitoring-only selection; no claim is made that all 110 members were imported. The eight new infrastructure tests are counted separately from the science.

## Fresh run

`python verify.py --output-dir NEW_DIRECTORY` refuses an existing directory. It records before/after integrity, exact source hashes, the tracked source ZIP, Python/dependency versions, every original log and report, and field-by-field comparisons against the preserved references. The result identifies the actual local commit and staged source tree. The runner never regenerates originals.

An assertion pass, numerical agreement and byte equality are separate report fields. A report may pass while recording nonidentical floating-point bytes. All changed fields, including small diagnostics, remain visible.

For cross-environment comparisons, finite float values use relative tolerance **1e-9** and absolute tolerance **2e-11**. This policy was fixed before the initialization runs. It is additional to, not a replacement for, each original suite's assertions. Types, shapes, dictionary keys, strings, Boolean values and integers must match exactly; nonfinite values are rejected. A discrepancy is not permission to refresh a reference or weaken an original test.

## Exact product-capacity certificate

The [counting-optimality proof](research/EXACT_PRODUCT_CAPACITY_2026-10-07.md) has one additional arithmetic certificate, counted separately from the original 23 groups and eight infrastructure tests. After the runner creates its new evidence directory, run:

```bash
python checks/certify_product_capacity.py --output NEW_DIRECTORY/product-capacity-certificate.json
```

The standard-library script uses integer/rational arithmetic only: an exact polynomial derivative-sign bracket, strict concavity, a tangent upper bound and logarithm series with explicit remainder bounds. It encloses the product rate, unrestricted rate and their difference for the fixed example, and records its own source hash. It creates its destination exclusively and neither reads nor changes original reference reports. This certifies the scalar evaluation conditional on the analytical POVM-optimality theorem, not the theorem itself.

The hosted workflow runs this as a dedicated step and includes its JSON in the existing evidence artifact. Inspect that step and the certificate in addition to the unchanged baseline report. Numerical agreement in the four historical suites cannot substitute for this exact-arithmetic certificate.

## Local versus hosted

The initial chat could read GitHub but had no write action, and its attempted local clone failed DNS. The takeover subsequently completed PR #1 and inspected its actual merged-main run; [STATUS](STATUS.md) and the [verification receipt](provenance/TAKEOVER_VERIFICATION_2026-10-07.json) record exact revisions and outcomes. A local commit or workflow file alone never establishes remote verification for a later change.

The hosted workflow checks out the PR head or push SHA, uses read-only repository permissions, installs the pinned dependencies, and uploads raw verification artifacts even after a failure. Review the artifact's commit, source hashes, protected-file checks, all original assertion outcomes and every report difference. After merging, inspect the actual merged-main run separately.

The workflow uses established major versions rather than claiming to pin immutable action SHAs. Infrastructure references checked during initialization: [checkout](https://github.com/actions/checkout), [setup-python](https://github.com/actions/setup-python), and the [CLI merge head-matching option](https://cli.github.com/manual/gh_pr_merge). This documentation check is not a fresh scientific literature audit.

No forced merge, administration override, automatic reference refresh or private credential is included.
