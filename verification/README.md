# Verification route

The [verification policy](../VERIFICATION.md) defines the evidence and its
limits. The analytical proofs establish the capacity and measurement optima.
Finite diagnostics check identities and evaluations; the rational certificate
encloses the fixed example's scalar optimum and gap.

Run from the repository root with the pinned [requirements](../requirements.txt)
and a fresh evidence directory:

```bash
python -m pip install -r requirements.txt
python verify.py --integrity-only
python -m unittest discover -s tests -v
python verify.py --output-dir local-evidence-001
python checks/certify_product_capacity.py --output local-evidence-001/product-capacity-certificate.json
```

| Evidence | What it checks |
|---|---|
| [Import manifest](../provenance/IMPORT_MANIFEST.json) | Exact bytes of all 70 protected source files and excerpts. |
| [Four scientific suites](../checks/README.md) | 23 diagnostic groups, with retained original assertions, tolerances and reference reports. |
| [Repository tests](../tests/test_repository.py) and [strict-gap regressions](../tests/test_strict_gap.py) | Eight infrastructure checks and three high-precision finite safeguards. |
| [Exact-arithmetic certificate](../checks/certify_product_capacity.py) | Rational brackets for the example, conditional on the analytical product-measurement theorem. |
| [Hosted mathematical review](../VERIFICATION.md#hosted-mathematical-display) | Source inventory and actual GitHub rendering at the inspected revision, followed by a separate visual review. |

Assertion success, numerical agreement and byte equality remain separate findings.
Use evidence for its recorded revision. The [scientific route](../science/README.md)
and [learning route](../learning/README.md) point to the claims being checked.
