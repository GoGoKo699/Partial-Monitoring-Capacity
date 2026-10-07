# Unchanged scientific checkers

The four scripts in source/ retain their exact bytes and original relative imports. Do not flatten or rewrite them merely to improve appearance; the top-level verifier provides a short command route.

| Suite | Source script | Groups | Reference |
|---|---|---:|---|
| Threshold and counting | `source/prior/prior/prior/check_monitoring.py` | 6 | `results/reference/threshold.json` |
| Exact qubit rate | `source/prior/prior/check_monitoring_followup.py` | 7 | `results/reference/qubit.json` |
| Optical capacity audit | `source/prior/check_audit.py` | 6 | `results/reference/optical.json` |
| Consolidated proof identities | `source/check_consolidation.py` | 4 | `results/reference/consolidation.json` |

Paths in the reference column are relative to the repository root. Use `python verify.py --output-dir NEW_DIRECTORY`. Reports use their original group-count keys (`groups` or `test_groups`); the runner handles both without changing them. No spin or Gaussian-field suite is imported or executed.
