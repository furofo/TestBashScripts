#!/usr/bin/env python3

from pathlib import Path
import os
import subprocess
import tempfile
import unittest


class TestHelloScript(unittest.TestCase):
    def test_hello_script_writes_file_with_testscript_env(self) -> None:
        script_path = Path(__file__).resolve().parent.parent / "scripts" / "hello.sh"
        test_name = "alice"
        expected_file_name = f"hello_{test_name}.txt"

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            env = os.environ.copy()
            env["TestScript"] = "True"

            result = subprocess.run(
                ["bash", str(script_path), test_name],
                capture_output=True,
                text=True,
                check=False,
                cwd=temp_dir,
                env=env,
            )

            generated_file = temp_path / expected_file_name

            self.assertTrue(generated_file.exists(), f"Expected file not found: {generated_file}")
            self.assertEqual(generated_file.read_text().strip(), "hello world alice")

            self.assertEqual(
                result.returncode,
                0,
                f"hello.sh exited with code {result.returncode}. stderr: {result.stderr.strip()}",
            )
            self.assertIn("Test mode: Skipping upload to S3.", result.stdout)
            self.assertIn(expected_file_name, result.stdout)
            self.assertEqual(result.stderr.strip(), "")

if __name__ == "__main__":
    unittest.main(verbosity=2)
