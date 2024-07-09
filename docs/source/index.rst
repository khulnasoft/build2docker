jupyter-build2docker
===================

``jupyter-build2docker`` is a tool to **build, run, and push Docker
images from source code repositories**.

``build2docker`` fetches a repository
(from GitHub, GitLab, Zenodo, Figshare, Dataverse installations, a Git repository or a local directory)
and builds a container image in which the code can be executed.
The image build process is based on the configuration files found in the repository.

``build2docker`` can be
used to explore a repository locally by building and executing the
constructed image of the repository, or as a means of building images that
are pushed to a Docker registry.

``build2docker`` is the tool used by `BinderHub <https://binderhub.readthedocs.io>`_
to build images on demand.

Please report `Bugs <https://github.com/khulnasoft/build2docker/issues>`_,
`ask questions <https://gitter.im/jupyterhub/binder>`_ or
`contribute to the project <https://github.com/khulnasoft/build2docker/blob/HEAD/CONTRIBUTING.md>`_.

.. toctree::
   :maxdepth: 2
   :caption: Getting started with build2docker

   getting-started/index
   howto/index
   configuration/index

.. toctree::
   :maxdepth: 2
   :caption: Contribute to build2docker

   contributing/index

.. toctree::
   :maxdepth: 2
   :caption: Changelog

   changelog
