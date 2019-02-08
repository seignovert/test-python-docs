CI/CD examples to test and deploy python packages from Github
=============================================================

|Docs| |RTD|

|CI| |Coverage| |Github|

|PyPI| |Release| |DOI|

|License|

.. |Docs| image:: https://img.shields.io/readthedocs/test-python-docs.svg?logo=read-the-docs&logoColor=white
          :target: https://readthedocs.org/projects/test-python-docs/

.. |RTD| image:: https://img.shields.io/badge/readthedocs.io-test--python--docs-blue.svg?logo=read-the-docs&logoColor=white
          :target: https://test-python-docs.readthedocs.io/

.. |CI| image:: https://img.shields.io/travis/seignovert/test-python-docs.svg?logo=travis-ci&logoColor=white
           :target: https://travis-ci.org/seignovert/test-python-docs

.. |Coverage| image:: https://img.shields.io/coveralls/github/seignovert/test-python-docs.svg?logo=travis-ci&logoColor=white
              :target: https://coveralls.io/github/seignovert/test-python-docs

.. |Github| image:: https://img.shields.io/badge/github.io-test--python--docs-blue.svg?logo=github&logoColor=white
          :target: https://seignovert.github.io/test-python-docs/

.. |PyPI| image:: https://img.shields.io/badge/PyPI%20(test)-foo--autodeploy-blue.svg?logo=python&logoColor=white
        :target: https://test.pypi.org/project/foo-autodeploy/

.. |Release| image:: https://img.shields.io/github/release/seignovert/test-python-docs.svg
          :target: https://github.com/seignovert/test-python-docs/releases

.. |DOI| image:: https://sandbox.zenodo.org/badge/168057818.svg
        :target: https://sandbox.zenodo.org/badge/latestdoi/168057818

.. |License| image:: https://img.shields.io/github/license/seignovert/test-python-docs.svg
             :target: https://github.com/seignovert/test-python-docs/

Python project to showcase how to hook Github with:

- Travis CI
- Coveralls.io
- PyPI
- Read the Docs
- Github Pages
- Github Releases
- Zenodo

See `setup.cfg <setup.cfg>`_ to configure:

- package description (name, author, url, files…).
- PyPI deploy settings.
- Pytest options.
- Coverage report settings.
- Linter settings.

See `tox.ini <tox.ini>`_ to configure:

- module tests from ``tests/`` folder (with `pytest`).
- module coverage (from `pytest` output).
- documentation build from ``docs/`` folder (with `sphinx`,
  `autodoc` and `napoleon`).
- documentation tests from ``docs/*.rst`` files and
  docstrings in ``foo`` module.
- linter python files syntax (with `flake8`).

See `.travis.yml <.travis.yml>`_ to configure CI tests and deployments to:

- `Coveralls.io <https://coveralls.io/github/seignovert/test-python-docs>`_
- `PyPI (test) <https://test.pypi.org/project/foo-autodeploy/>`_
- `Github Releases <https://github.com/seignovert/test-python-docs/releases>`_
- `Github Pages <https://seignovert.github.io/test-python-docs/>`_

See `.readthedocs.yml <.readthedocs.yml>`_
to configure `Read the Docs <https://test-python-docs.readthedocs.io/>`_ deployment.

See `.zenodo.json <.zenodo.json>`_ to configure
`Zenodo <https://zenodo.org>`_ deployment, to get a DOI for each
`Github release <https://guides.github.com/activities/citable-code/>`_.

(Note: in this test case, we hook our release with Zenodo
sandbox interface to avoid dummy publications, therefore the DOI badge
is not valid but the record can be found
`here <https://sandbox.zenodo.org/record/257354>`_).


Sphinx autobuild (tip)
----------------------

Install:

.. code:: bash

    $ pip install sphinx-autobuild

Start autobuild (with live reload):

.. code:: bash

    $ cd docs ; make livehtml
