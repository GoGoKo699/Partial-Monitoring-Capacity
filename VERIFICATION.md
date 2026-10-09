# Verification policy

The scientific derivations are analytical. The checks reproduce finite identities
and scalar evaluations; they do not replace the capacity proofs.

## Scientific suites and protected sources

Four scientific scripts and their reference reports contain 23 groups: 6
threshold/counting, 7 qubit-rate, 6 optical-audit and 4 consolidation checks.
Their assertions and tolerance values are fixed. These are finite diagnostic
models, not full coding simulations.

Seventy source files and excerpts, including the license, are pinned by byte count
and SHA-256 in [the import manifest](provenance/IMPORT_MANIFEST.json). The eight
infrastructure tests are counted separately from the scientific groups.

Three additional [strict-gap regression tests](tests/test_strict_gap.py) use
120-decimal-digit arithmetic to compare direct entropy differences with the mixed
differences and their lower bounds, including cancellation-sensitive inputs near
the boundaries. They also check the second derivative, the common product-optimal
input and endpoint consistency. These finite safeguards do not prove universal
strictness; the [analytical corollary](research/EXACT_PRODUCT_CAPACITY_2026-10-07.md#4-strict-collective-advantage-throughout-the-qubit-interior)
does. Run all eleven tests with `python -m unittest discover -s tests -v`.

## Fresh run

`python verify.py --output-dir NEW_DIRECTORY` refuses an existing directory. It records before/after integrity, exact source hashes, the tracked source ZIP, Python/dependency versions, every original log and report, and field-by-field comparisons against the preserved references. The result identifies the actual local commit and staged source tree. The runner never regenerates originals.

An assertion pass, numerical agreement and byte equality are separate report fields. A report may pass while recording nonidentical floating-point bytes. All changed fields, including small diagnostics, remain visible.

For cross-environment comparisons, finite float values use relative tolerance **1e-9** and absolute tolerance **2e-11**. This comparison is additional to each suite's assertions. Types, shapes, dictionary keys, strings, Boolean values and integers must match exactly; nonfinite values are rejected. A discrepancy is not permission to refresh a reference or weaken a test.

## Exact product-capacity certificate

The [counting-optimality proof](research/EXACT_PRODUCT_CAPACITY_2026-10-07.md) has one additional arithmetic certificate, counted separately from the original 23 groups, eight infrastructure tests and three strict-gap regression tests. After the runner creates its new evidence directory, run:

```bash
python checks/certify_product_capacity.py --output NEW_DIRECTORY/product-capacity-certificate.json
```

The standard-library script uses integer/rational arithmetic only: an exact polynomial derivative-sign bracket, strict concavity, a tangent upper bound and logarithm series with explicit remainder bounds. It encloses the product rate, unrestricted rate and their difference for the fixed example, and records its own source hash. It creates its destination exclusively and neither reads nor changes original reference reports. This certifies the scalar evaluation conditional on the analytical POVM-optimality theorem, not the theorem itself.

The hosted workflow runs this as a dedicated step and includes its JSON in the
evidence artifact. Inspect the certificate alongside the four suite reports.
Numerical agreement in those suites cannot substitute for this exact-arithmetic
certificate.

## Local versus hosted

Local and hosted evidence identify their actual revisions separately. The
[Actions runs](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/actions)
retain workflow evidence; [merged PR records](https://github.com/GoGoKo699/Partial-Monitoring-Capacity/pulls?q=is%3Apr+is%3Amerged)
record exact head and merged-main commits, run and artifact identities, source
matches and report differences. Evidence applies to its recorded revision.

The hosted workflow checks out the PR head or push SHA, uses read-only repository permissions, installs the pinned dependencies, and uploads raw verification artifacts even after a failure. Review the artifact's commit, source hashes, protected-file checks, all original assertion outcomes and every report difference. After merging, inspect the actual merged-main run separately.

The workflow uses major-version references for [checkout](https://github.com/actions/checkout)
and [setup-python](https://github.com/actions/setup-python), rather than immutable
action SHAs. Contributor procedures are in [repository maintenance](.github/MAINTENANCE.md).

No forced merge, administration override, automatic reference refresh or private credential is included.
