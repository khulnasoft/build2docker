# <a href="https://github.com/khulnasoft/build2docker"><img src="https://raw.githubusercontent.com/khulnasoft/build2docker/8731ecf0967cc5fde028c456f2b92be651ebbc18/docs/source/_static/images/build2docker.png" height="48px" /> build2docker</a>

[![Build Status](https://github.com/khulnasoft/build2docker/workflows/Test/badge.svg)](https://github.com/khulnasoft/build2docker/actions)
[![Documentation Status](https://readthedocs.org/projects/build2docker/badge/?version=latest)](http://build2docker.readthedocs.io/en/latest/?badge=latest)
[![Contribute](https://img.shields.io/badge/I_want_to_contribute!-grey?logo=jupyter)](https://build2docker.readthedocs.io/en/latest/contributing/contributing.html)
[![Docker Repository on Quay](https://img.shields.io/badge/quay.io-container-green "Docker Repository on Quay")](https://quay.io/repository/khulnasoft/build2docker?tab=tags)

`build2docker` fetches a git repository and builds a container image based on
the configuration files found in the repository.

See the [build2docker documentation](http://build2docker.readthedocs.io)
for more information on using build2docker.

For support questions please search or post to https://discourse.jupyter.org/c/binder.

See the [contributing guide](CONTRIBUTING.md) for information on contributing to
build2docker.

---

Please note that this repository is participating in a study into sustainability
of open source projects. Data will be gathered about this repository for
approximately the next 12 months, starting from 2021-06-11.

Data collected will include number of contributors, number of PRs, time taken to
close/merge these PRs, and issues closed.

For more information, please visit
[our informational page](https://sustainable-open-science-and-software.github.io/) or download our [participant information sheet](https://sustainable-open-science-and-software.github.io/assets/PIS_sustainable_software.pdf).

---

## Using build2docker

### Prerequisites

1. Docker to build & run the repositories. The [community edition](https://store.docker.com/search?type=edition&offering=community)
   is recommended.
2. Python 3.6+.

Supported on Linux and macOS. [See documentation note about Windows support.](http://build2docker.readthedocs.io/en/latest/install.html#note-about-windows-support)

### Installation

This a quick guide to installing `build2docker`, see our documentation for [a full guide](https://build2docker.readthedocs.io/en/latest/install.html).

To install from PyPI:

```bash
pip install jupyter-build2docker
```

To install from source:

```bash
git clone https://github.com/khulnasoft/build2docker.git
cd build2docker
pip install -e .
```

### Usage

The core feature of build2docker is to fetch a git repository (from GitHub or locally),
build a container image based on the specifications found in the repository &
optionally launch the container that you can use to explore the repository.

**Note that Docker needs to be running on your machine for this to work.**

Example:

```bash
jupyter-build2docker https://github.com/norvig/pytudes
```

After building (it might take a while!), it should output in your terminal
something like:

```bash
    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://0.0.0.0:36511/?token=f94f8fabb92e22f5bfab116c382b4707fc2cade56ad1ace0
```

If you copy paste that URL into your browser you will see a Jupyter Notebook
with the contents of the repository you had just built!

For more information on how to use `build2docker`, see the
[usage guide](http://build2docker.readthedocs.io/en/latest/usage.html).

## Repository specifications

Build2Docker looks for configuration files in the source repository to
determine how the Docker image should be built. For a list of the configuration
files that `build2docker` can use, see the
[complete list of configuration files](https://build2docker.readthedocs.io/en/latest/config_files.html).

The philosophy of build2docker is inspired by
[Heroku Build Packs](https://devcenter.heroku.com/articles/buildpacks).

## Docker Image

Build2Docker can be run inside a Docker container if access to the Docker Daemon is provided, for example see [BinderHub](https://github.com/jupyterhub/binderhub). Docker images are [published to quay.io](https://quay.io/repository/khulnasoft/build2docker?tab=tags). The old [Docker Hub image](https://hub.docker.com/r/khulnasoft/build2docker) is no longer supported.
