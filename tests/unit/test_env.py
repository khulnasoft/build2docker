"""
Test that environment variables may be defined
"""

import os
import subprocess
import sys
import tempfile
import time
from getpass import getuser


def test_env(capfd):
    """
    Validate that you can define environment variables

    See https://gist.github.com/hwine/9f5b02c894427324fafcf12f772b27b7
    for how docker handles its -e & --env argument values
    """
    ts = str(time.time())
    # There appear to be some odd combinations of default dir that do
    # not work on macOS Catalina with Docker CE 2.2.0.5, so use
    # the current dir -- it'll be deleted immediately

    with tempfile.TemporaryDirectory(dir=os.path.abspath(os.curdir)) as tmpdir:
        username = getuser()
        os.environ["SPAM"] = "eggs"
        os.environ["SPAM_2"] = "ham"
        result = subprocess.run(
            [
                "build2docker",
                # 'key=value' are exported as is in docker
                "-e",
                f"FOO={ts}",
                "--env",
                "BAR=baz",
                # 'key' is exported with the currently exported value
                "--env",
                "SPAM",
                # 'key' is not exported if it is not exported.
                "-e",
                "NO_SPAM",
                # 'key=' is exported in docker with an empty string as
                # value
                "--env",
                "SPAM_2=",
                tmpdir,
                "--",
                "/bin/bash",
                "-c",
                # Docker exports all passed env variables, so we can
                # just look at exported variables.
                "export",
            ],
        )
    captured = capfd.readouterr()
    print(captured.out, end="")
    print(captured.err, file=sys.stderr, end="")

    assert result.returncode == 0

    # all docker output is returned by build2docker on stderr
    # extract just the declare for better failure message formatting
    # stdout should be empty
    assert not result.stdout

    # stderr should contain lines of output
    declares = [x for x in captured.err.splitlines() if x.startswith("declare")]
    assert f'declare -x FOO="{ts}"' in declares
    assert 'declare -x BAR="baz"' in declares
    assert 'declare -x SPAM="eggs"' in declares
    assert "declare -x NO_SPAM" not in declares
    assert 'declare -x SPAM_2=""' in declares
