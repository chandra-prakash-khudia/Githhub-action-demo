import subprocess
import sys
from pathlib import Path


def test_demo_prints_hello_world():
    demo_path = Path(__file__).with_name("demo.py")
    result = subprocess.run(
        [sys.executable, str(demo_path)],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == "Hello world\n"
