"""Repository checks; not additional scientific evidence."""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("verification", ROOT/"verify.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class RepositoryChecks(unittest.TestCase):
    def test_protected_inputs(self):
        result = v.check_imports()
        self.assertEqual(result["status"], "PASS", result)
        self.assertEqual(result["protected_files"], 70)

    def test_mutation_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); (root/"provenance").mkdir()
            (root/"file").write_bytes(b"changed")
            record = {"files": {"file": {"bytes": 8, "sha256": v.sha(b"original")}}}
            (root/"provenance/IMPORT_MANIFEST.json").write_text(json.dumps(record))
            self.assertEqual(v.check_imports(root)["status"], "FAIL")

    def test_numeric_policy_records_small_differences(self):
        self.assertEqual(v.compare({"x": 1.0}, {"x": 1.0}), [])
        self.assertTrue(v.compare(1.0, 1.0+1e-12)[0]["accepted"])
        self.assertFalse(v.compare(1.0, 1.001)[0]["accepted"])

    def test_structural_and_nonfinite_errors(self):
        for a,b in [(1,2),(True,1),(1,1.0),([1],[1,2]),({"x":1},{}),(float("nan"),float("nan")),(float("inf"),float("inf"))]:
            self.assertTrue(any(not r["accepted"] for r in v.compare(a,b)))

    def test_output_refusal(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); (root/"marker").write_bytes(b"keep")
            result = subprocess.run([sys.executable,str(ROOT/"verify.py"),"--output-dir",temp],cwd=ROOT,capture_output=True,text=True)
            self.assertEqual(result.returncode,2)
            self.assertEqual((root/"marker").read_bytes(),b"keep")
            self.assertEqual(len(list(root.iterdir())),1)

    def test_paths_and_separation(self):
        self.assertTrue(v.safe_relative("checks/a.py"))
        for path in ("../file","/tmp/file",".git/config",""):
            self.assertFalse(v.safe_relative(path))
        result = v.integrity()
        self.assertEqual(result["status"],"PASS",result)
        self.assertGreater(result["active_links_checked"],20)

    def test_original_reference_counts(self):
        self.assertEqual(sum(r[2] for r in v.SUITES),23)
        for name,_,count,key in v.SUITES:
            record=json.loads((ROOT/"results/reference"/f"{name}.json").read_text())
            self.assertEqual(record["status"],"PASS")
            self.assertEqual(record[key],count)

    def test_contact_and_owner_license(self):
        notice="This repository serves as a record of the work and a guide for the author’s self-directed learning."
        for name in ("README.md","llms.txt"):
            text=(ROOT/name).read_text()
            self.assertIn(notice,text)
            self.assertIn("mailto:gogoko699@gmail.com",text)
        data=(ROOT/"LICENSE").read_bytes()
        self.assertEqual(hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest(),"e17a781bf47c4aadf18b68fc593846a1193b86c1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
