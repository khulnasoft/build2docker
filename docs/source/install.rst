.. _install:

Installing ``build2docker``
==========================

build2docker requires Python 3.6 or above on Linux and macOS. See
:ref:`below <windows>` for more information about Windows support.

Prerequisite: Docker
--------------------

Install `Docker <https://www.docker.com>`_ as it is required
to build Docker images. The
`Community Edition <https://docs.docker.com/install/>`_,
is available for free.

Recent versions of Docker are recommended.
The latest version of Docker, ``18.03``, successfully builds repositories from
`binder-examples <https://github.com/binder-examples>`_.
The `BinderHub <https://binderhub.readthedocs.io/>`_ helm chart uses version
``17.11.0-ce-dind``.  See the
`helm chart <https://github.com/jupyterhub/binderhub/blob/HEAD/helm-chart/binderhub/values.yaml#L167>`_
for more details.

Optional: Mercurial
-------------------

For `Mercurial <https://www.mercurial-scm.org>`_ repositories, Mercurial and
`hg-evolve <https://www.mercurial-scm.org/doc/evolution/>`_ need to be
installed. For example, on Debian based distributions, one can do::

  sudo apt install mercurial
  $(hg debuginstall --template "{pythonexe}") -m pip install hg-evolve --user

To install Mercurial on other systems, see `here
<https://www.mercurial-scm.org/download>`_.

Note that for old Mercurial versions, you may need to specify a version for
hg-evolve. For example, ``hg-evolve==9.2`` for hg 4.5 (which is installed with
`apt` on Ubuntu 18.4).

Installing with ``pip``
-----------------------

We recommend installing ``build2docker`` with the ``pip`` tool::

    python3 -m pip install jupyter-build2docker

for the latest release. To install the most recent code from the upstream repository, run::

    python3 -m pip install https://github.com/khulnasoft/build2docker/archive/main.zip

For information on using ``build2docker``, see :ref:`usage`.

Installing from source code
---------------------------

Alternatively, you can install build2docker from a local source tree,
e.g. in case you are contributing back to this project::

  git clone https://github.com/khulnasoft/build2docker.git
  cd build2docker
  python3 -m pip install -e .

That's it! For information on using ``build2docker``, see
:ref:`usage`.

.. _windows:

Windows support
---------------

Windows support for ``build2docker`` is still in the experimental stage.

An article about `using Windows and the WSL`_ (Windows Subsytem for Linux or
Bash on Windows) provides additional information about Windows and docker.


.. _using Windows and the WSL: https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly
