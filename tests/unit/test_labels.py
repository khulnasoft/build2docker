"""
Test if labels are supplied correctly to the container
"""

from unittest.mock import Mock

import pytest

from build2docker import __version__
from build2docker.app import Build2Docker
from build2docker.buildpacks import BuildPack

URL = "https://github.com/binderhub-ci-repos/build2docker-ci-clone-depth"


def test_buildpack_labels_rendered(base_image):
    bp = BuildPack(base_image)
    assert "LABEL" not in bp.render()
    bp.labels["first_label"] = "firstlabel"
    assert 'LABEL first_label="firstlabel"\n' in bp.render()
    bp.labels["second_label"] = "anotherlabel"
    assert 'LABEL second_label="anotherlabel"\n' in bp.render()


@pytest.mark.parametrize(
    "ref, repo, expected_repo_label",
    [(None, URL, URL), ("some-ref", None, "local"), (None, None, "local")],
)
def test_Build2Docker_labels(ref, repo, expected_repo_label, tmpdir):
    app = Build2Docker(dry_run=True)
    # Add mock BuildPack to app
    mock_buildpack = Mock()
    mock_buildpack.return_value.labels = {}
    app.buildpacks = [mock_buildpack]

    if repo is None:
        repo = str(tmpdir)
    app.repo = repo
    if ref is not None:
        app.ref = ref

    app.initialize()
    app.start()
    expected_labels = {
        "build2docker.ref": ref,
        "build2docker.repo": expected_repo_label,
        "build2docker.version": __version__,
    }

    assert mock_buildpack().labels == expected_labels
