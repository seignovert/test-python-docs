CI/CD examples to test and deploy python packages from Github
=============================================================

|Docs| |RTD|

|CI| |Github Pages|

|Codecov| |Coveralls|

|PyPI|  |PyPI Version| |Python Version|

|Conda| |Conda Version| |Conda Platform|

|License| |DOI|

.. |Docs| image:: https://img.shields.io/readthedocs/test-python-docs.svg?logo=read-the-docs&logoColor=white
          :target: https://readthedocs.org/projects/test-python-docs/

.. |RTD| image:: https://img.shields.io/badge/readthedocs.io-test--python--docs-blue.svg?logo=read-the-docs&logoColor=white
          :target: https://test-python-docs.readthedocs.io/

.. |CI| image:: https://img.shields.io/travis/seignovert/test-python-docs.svg?logo=travis-ci&logoColor=white
           :target: https://travis-ci.org/seignovert/test-python-docs

.. |Github Pages| image:: https://img.shields.io/badge/github.io-test--python--docs-blue.svg?logo=github&logoColor=white
          :target: https://seignovert.github.io/test-python-docs/

.. |Codecov| image:: https://img.shields.io/codecov/c/github/seignovert/test-python-docs.svg?label=Codecov&logo=codecov&logoColor=white
              :target: https://codecov.io/gh/seignovert/test-python-docs

.. |Coveralls| image:: https://img.shields.io/coveralls/github/seignovert/test-python-docs.svg?label=Coveralls
              :target: https://coveralls.io/github/seignovert/test-python-docs

.. |PyPI| image:: https://img.shields.io/badge/PyPI%20(test)-foo--autodeploy-blue.svg?logo=python&logoColor=white
        :target: https://test.pypi.org/project/foo-autodeploy/

.. |PyPI Version| image:: https://img.shields.io/github/release/seignovert/test-python-docs.svg?label=Version
          :target: https://test.pypi.org/project/foo-autodeploy/

.. |Python Version| image:: https://img.shields.io/badge/Python-3.6-blue.svg
        :target: https://test.pypi.org/project/foo-autodeploy/

.. |Conda| image:: https://img.shields.io/badge/conda|seignovert-foo--autodeploy-blue.svg?logo=python&logoColor=white
          :target: https://anaconda.org/seignovert/foo-autodeploy

.. |Conda Version| image:: https://img.shields.io/conda/vn/seignovert/foo-autodeploy.svg?label=Version
          :target: https://anaconda.org/seignovert/foo-autodeploy

.. |Conda Platform| image:: https://img.shields.io/conda/pn/seignovert/foo-autodeploy.svg
          :target: https://anaconda.org/seignovert/foo-autodeploy

.. |License| image:: https://img.shields.io/github/license/seignovert/test-python-docs.svg
             :target: https://github.com/seignovert/test-python-docs/

.. |DOI| image:: https://sandbox.zenodo.org/badge/168057818.svg
        :target: https://sandbox.zenodo.org/badge/latestdoi/168057818

Python project to showcase how to hook Github with:

- Read the Docs
- Travis CI
- CodeCov
- Coveralls
- PyPI
- Anaconda
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

See `meta.yaml <meta.yaml>`_ to configure Anaconda recipe.

See `.readthedocs.yml <.readthedocs.yml>`_
to configure `Read the Docs <https://test-python-docs.readthedocs.io/>`_ deployment.

See `.travis.yml <.travis.yml>`_ to configure CI tests and deployments to:

- `Codecov <https://codecov.io/gh/seignovert/test-python-docs>`_
- `Coveralls <https://coveralls.io/github/seignovert/test-python-docs>`_
- `PyPI (test) <https://test.pypi.org/project/foo-autodeploy/>`_
- `Anaconda <https://anaconda.org/seignovert/foo-autodeploy>`_
- `Github Releases <https://github.com/seignovert/test-python-docs/releases>`_
- `Github Pages <https://seignovert.github.io/test-python-docs/>`_

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
