"""
Test if the subdirectory is correctly navigated to
"""

import os

import escapism
import pytest

from build2docker.app import Build2Docker

TEST_REPO = "https://github.com/binderhub-ci-repos/build2docker-subdir-support"


def test_subdir(run_build2docker):
    # Build from a subdirectory
    # if subdir support is broken this will fail as the instructions in the
    # root of the test repo are invalid
    cwd = os.getcwd()

    argv = ["--subdir", "a directory", TEST_REPO]
    run_build2docker(argv)

    # check that we restored the current working directory
    assert cwd == os.getcwd(), f"We should be back in {cwd}"


def test_subdir_in_image_name():
    app = Build2Docker(repo=TEST_REPO, subdir="a directory")
    app.initialize()
    app.build()

    escaped_dirname = escapism.escape("a directory", escape_char="-").lower()
    assert escaped_dirname in app.output_image_spec


def test_subdir_invalid():
    # test an error is raised when requesting a non existent subdir
    app = Build2Docker(repo=TEST_REPO, subdir="invalid-sub-dir")
    app.initialize()
    with pytest.raises(FileNotFoundError):
        app.build()  # Just build the image and do not run it.
