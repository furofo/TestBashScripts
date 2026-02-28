#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys


def main() -> int:
    script_path = Path(__file__).resolve().parent.parent / "scripts" / "hello.sh"

    result = subprocess.run(
        ["bash", str(script_path)],
        capture_output=True,
        text=True,
        check=False,
    )

    expected_stdout = "hello world"
    actual_stdout = result.stdout.strip()

    if result.returncode != 0:
        print(f"FAIL: hello.sh exited with code {result.returncode}")
        if result.stderr:
            print("stderr:")
            print(result.stderr.strip())
        return 1

    if actual_stdout != expected_stdout:
        print("FAIL: stdout did not match expected output")
        print(f"Expected: {expected_stdout!r}")
        print(f"Actual:   {actual_stdout!r}")
        return 1

    if result.stderr.strip():
        print("FAIL: expected no stderr, but got:")
        print(result.stderr.strip())
        return 1

    print("PASS: hello.sh ran successfully with expected output")
    return 0


if __name__ == "__main__":
    sys.exit(main())
