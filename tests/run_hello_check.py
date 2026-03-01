#!/usr/bin/env python3

from pathlib import Path
import subprocess
import unittest


class TestHelloScript(unittest.TestCase):
    def test_hello_script_output(self) -> None:
        script_path = Path(__file__).resolve().parent.parent / "scripts" / "hello.sh"

        result = subprocess.run(
            ["bash", str(script_path)],
            capture_output=True,
            text=True,
            check=False,
        )

        expected_stdout = "hello world"
        actual_stdout = result.stdout.strip()

        self.assertEqual(
            result.returncode,
            0,
            f"hello.sh exited with code {result.returncode}. stderr: {result.stderr.strip()}",
        )
        self.assertEqual(actual_stdout, expected_stdout)
        self.assertEqual(result.stderr.strip(), "")

if __name__ == "__main__":
    unittest.main(verbosity=2)
