"""
Test that build time memory limits are enforced
"""

import os
from unittest.mock import MagicMock

import pytest

import docker
from build2docker.buildpacks import BaseImage, DockerBuildPack

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_memory_limit_enforced(tmpdir, base_image):
    fake_cache_from = ["image-1:latest"]
    fake_log_value = {"stream": "fake"}
    fake_client = MagicMock(spec=docker.APIClient)
    fake_client.build.return_value = iter([fake_log_value])
    fake_extra_build_kwargs = {"somekey": "somevalue"}

    # some memory limit value, the important bit is that this value is
    # later passed to the `build` method of the Docker API client
    memory_limit = 128 * 1024

    # Test that the buildpack passes the right arguments to the docker
    # client in order to enforce the memory limit
    tmpdir.chdir()
    for line in BaseImage(base_image).build(
        fake_client,
        "image-2",
        memory_limit,
        {},
        fake_cache_from,
        fake_extra_build_kwargs,
    ):
        pass

    # check that we pass arguments asking for memory limiting
    # to the Docker API client
    args, kwargs = fake_client.build.call_args
    assert "container_limits" in kwargs
    assert kwargs["container_limits"] == {
        "memory": memory_limit,
        "memswap": memory_limit,
    }


@pytest.mark.parametrize("BuildPack", [BaseImage, DockerBuildPack])
def test_memlimit_argument_type(BuildPack, base_image):
    # check that an exception is raised when the memory limit isn't an int
    fake_log_value = {"stream": "fake"}
    fake_client = MagicMock(spec=docker.APIClient)
    fake_client.build.return_value = iter([fake_log_value])

    with pytest.raises(ValueError) as exc_info:
        for line in BuildPack(base_image).build(
            fake_client, "image-2", "10Gi", {}, [], {}
        ):
            pass

        assert "The memory limit has to be specified as an" in str(exc_info.value)