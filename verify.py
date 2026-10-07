#!/usr/bin/env python3
"""Verify protected monitoring inputs and run four unchanged scientific suites.

No file under results/ or archive/ is regenerated. New runs require a new output
path. Assertions, numerical agreement, and identical report bytes are separate.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import zipfile

ROOT = Path(__file__).resolve().parent
POLICY = {"relative_tolerance": 1e-9, "absolute_tolerance": 2e-11,
          "other_fields": "exact type, value, and structure", "nonfinite": "reject"}
SUITES = (
    ("threshold", "source/prior/prior/prior/check_monitoring.py", 6, "test_groups"),
    ("qubit", "source/prior/prior/check_monitoring_followup.py", 7, "test_groups"),
    ("optical", "source/prior/check_audit.py", 6, "groups"),
    ("consolidation", "source/check_consolidation.py", 4, "test_groups"),
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, data: object) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write("\n")


def git(*args: str) -> str | None:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


def source_files(root: Path = ROOT) -> list[str]:
    result = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True)
    if result.returncode == 0 and result.stdout:
        return sorted(result.stdout.decode().rstrip("\0").split("\0"))
    excluded = {".git", ".venv", "__pycache__", "verification-artifacts"}
    return sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()
        and not (set(p.relative_to(root).parts) & excluded)
        and not any(x.startswith("local-evidence") for x in p.relative_to(root).parts))


def safe_relative(name: str) -> bool:
    p = Path(name)
    return bool(name) and not p.is_absolute() and ".." not in p.parts and ".git" not in p.parts


def check_imports(root: Path = ROOT) -> dict:
    record = json.loads((root / "provenance/IMPORT_MANIFEST.json").read_text())
    failures = []
    for name, expected in record["files"].items():
        if not safe_relative(name):
            failures.append({"path": name, "reason": "unsafe path"})
            continue
        p = root / name
        if not p.is_file() or p.is_symlink():
            failures.append({"path": name, "reason": "missing/nonregular"})
            continue
        data = p.read_bytes()
        if len(data) != expected["bytes"] or sha(data) != expected["sha256"]:
            failures.append({"path": name, "reason": "protected bytes differ"})
    return {"status": "PASS" if not failures else "FAIL",
            "protected_files": len(record["files"]), "failures": failures}


def integrity(root: Path = ROOT) -> dict:
    imported = check_imports(root)
    pages = list(root.glob("*.md"))
    for folder in ("research", "literature", "work_orders", "checks"):
        pages.extend((root / folder).glob("*.md"))
    broken, links = [], 0
    for page in pages:
        text = re.sub(r"```.*?```", "", page.read_text(), flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"(?:[a-zA-Z]+:|#)", target):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            links += 1
            path = (page.parent / target).resolve()
            if not path.is_relative_to(root.resolve()) or not path.exists():
                broken.append({"file": page.relative_to(root).as_posix(), "target": target})
    forbidden = [name for name in source_files(root) if Path(name).suffix.lower() in
                 {".pdf", ".ttf", ".otf", ".woff", ".woff2", ".pyc"}]
    separate = [name for name in source_files(root) if
                ("spin" in Path(name).name.lower() or "strip" in Path(name).name.lower())]
    return {"status": "PASS" if imported["status"] == "PASS" and not (broken or forbidden or separate) else "FAIL",
            "imports": imported, "active_links_checked": links, "broken_links": broken,
            "forbidden_files": forbidden, "separate_pilot_files": separate}


def compare(a: object, b: object, path: str = "$") -> list[dict]:
    rows = []
    if type(a) is not type(b):
        return [{"path": path, "kind": "type", "accepted": False,
                 "reference_type": type(a).__name__, "observed_type": type(b).__name__}]
    if isinstance(a, dict):
        for key in sorted(a.keys() | b.keys()):
            if key not in a or key not in b:
                rows.append({"path": path+"."+key, "kind": "key", "accepted": False})
            else:
                rows.extend(compare(a[key], b[key], path+"."+key))
    elif isinstance(a, list):
        if len(a) != len(b):
            rows.append({"path": path, "kind": "length", "accepted": False})
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                rows.extend(compare(x, y, f"{path}[{i}]"))
    elif isinstance(a, float):
        finite = math.isfinite(a) and math.isfinite(b)
        if not finite or a != b:
            rows.append({"path": path, "kind": "float",
                "reference": a if math.isfinite(a) else repr(a),
                "observed": b if math.isfinite(b) else repr(b),
                "absolute_difference": abs(a-b) if finite else None,
                "accepted": finite and math.isclose(a, b,
                    rel_tol=POLICY["relative_tolerance"], abs_tol=POLICY["absolute_tolerance"])})
    elif a != b:
        rows.append({"path": path, "kind": "exact", "reference": a, "observed": b, "accepted": False})
    return rows


def run(output: Path) -> int:
    if output.exists():
        raise FileExistsError(f"Refusing existing evidence directory: {output}")
    names = source_files()
    before_hashes = {n: sha((ROOT/n).read_bytes()) for n in names}
    before = integrity()
    output.mkdir(parents=True)
    write_json(output/"integrity-before.json", before)
    write_json(output/"source-sha256.json", before_hashes)
    write_json(output/"environment.json", {
        "python": sys.version, "platform": sys.platform,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "dependencies": {n: importlib.metadata.version(n) for n in ("numpy", "scipy", "sympy", "mpmath")},
        "blas_threads": 1,
    })
    report = {"repository": "GoGoKo699/Partial-Monitoring-Capacity",
              "commit": git("rev-parse", "HEAD"), "index_tree": git("write-tree"),
              "status": "RUNNING", "comparison_policy": POLICY,
              "before": before, "expected_scientific_groups": 23, "runs": []}
    env = {**os.environ, "OPENBLAS_NUM_THREADS": "1", "OMP_NUM_THREADS": "1",
           "PYTHONDONTWRITEBYTECODE": "1"}
    for name, script, groups, key in SUITES:
        sub = output/name
        sub.mkdir()
        ref = (ROOT/"results/reference"/f"{name}.json").read_bytes()
        (sub/"reference.json").write_bytes(ref)
        start = time.monotonic()
        with (sub/"execution.log").open("x") as log:
            process = subprocess.run([sys.executable, str(ROOT/"checks"/script),
                "--output", str(sub/"observed.json")], cwd=ROOT, env=env,
                stdout=log, stderr=subprocess.STDOUT)
        try:
            raw = (sub/"observed.json").read_bytes()
            observed = json.loads(raw)
            differences = compare(json.loads(ref), observed)
            assertions = process.returncode == 0 and observed.get("status") == "PASS" and observed.get(key) == groups
        except (OSError, ValueError) as error:
            raw, observed, assertions = b"", {}, False
            differences = [{"path": "$", "kind": "report", "accepted": False, "error": str(error)}]
        comparison = {"numerical_agreement": all(r["accepted"] for r in differences),
            "byte_identical": raw == ref, "differences": differences,
            "reference_sha256": sha(ref), "observed_sha256": sha(raw)}
        write_json(sub/"comparison.json", comparison)
        row = {"name": name, "expected_groups": groups, "observed_groups": observed.get(key),
            "exit_code": process.returncode, "assertions_passed": assertions,
            "numerical_agreement": comparison["numerical_agreement"], "byte_identical": raw == ref,
            "difference_count": len(differences), "seconds": time.monotonic()-start}
        report["runs"].append(row)
        print(json.dumps(row), flush=True)
    after = integrity()
    after_hashes = {n: sha((ROOT/n).read_bytes()) for n in names}
    report.update(after=after, source_unchanged=before_hashes == after_hashes,
                  source_files=len(names), all_reports_byte_identical=all(r["byte_identical"] for r in report["runs"]))
    passed = before["status"] == after["status"] == "PASS" and report["source_unchanged"] and all(
        r["assertions_passed"] and r["numerical_agreement"] for r in report["runs"])
    report["status"] = "PASS" if passed else "FAIL"
    write_json(output/"integrity-after.json", after)
    with zipfile.ZipFile(output/"tracked-source.zip", "x", zipfile.ZIP_DEFLATED) as z:
        for n in names:
            z.write(ROOT/n, n)
    write_json(output/"REPORT.json", report)
    print(report["status"], "23 monitoring groups; byte-identical:", report["all_reports_byte_identical"])
    return 0 if passed else 1


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--integrity-only", action="store_true")
    group.add_argument("--output-dir", type=Path)
    args = p.parse_args()
    if args.integrity_only:
        result = integrity()
        print(json.dumps(result, indent=2))
        raise SystemExit(0 if result["status"] == "PASS" else 1)
    try:
        raise SystemExit(run(args.output_dir.resolve()))
    except FileExistsError as error:
        p.error(str(error))


if __name__ == "__main__":
    main()
