import subprocess
import sys

from toy_fast_api import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "toy_fast_api", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
