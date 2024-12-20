# Overview of tests for the julia buildpack

## Tested configuration files

- [`Project.toml`](https://build2docker.readthedocs.io/en/latest/config_files.html#project-toml-install-a-julia-environment)
- [`REQUIRE`](https://build2docker.readthedocs.io/en/latest/config_files.html#require-install-a-julia-environment-legacy)
- [`requirements.txt`](https://build2docker.readthedocs.io/en/latest/config_files.html#requirements-txt-install-a-python-environment)

## Test folders

### project

- Tests use of a `Project.toml` file for Julia, using the build2docker default
  version of Julia as specified in `julia_project.py`.

### project-1.0.2-binder-dir

- Tests use of a `Project.toml` file for Julia, using a version of Julia
  specified via `julia = "=1.0.2"` in `Project.toml`'s `[compat]` section.

- Test use of a `.binder` directory.

### require

- Tests use of a `REQUIRE` file for Julia, using the build2docker default version
  of Julia as specified in `julia_require.py`. Note that this is default version
  is currently 0.6.4!

- Starting with Julia v0.7 and up, the package manager has changed, so this
  tests that the Julia version below that can be installed correctly as well.

### require-1-requirements-file

- Tests use of a `REQUIRE` file for Julia, using a major version version
  specification. Note that this major version specification is currently
  resolving to a pinned minor and patch version as declared in
  `julia_require.py`.

- Test use of a `requirements.txt` file, where it is expected to be respected
  alongside the `REQUIRE` file.
