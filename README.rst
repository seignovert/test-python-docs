Test Python Docs
=================

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

.. |PyPI| image:: https://img.shields.io/badge/PyPI%20(test)-foo--docs-blue.svg?logo=python&logoColor=white
        :target: https://test.pypi.org/project/foo--docs

.. |Release| image:: https://img.shields.io/github/release/seignovert/test-python-docs.svg
          :target: https://github.com/seignovert/test-python-docs/releases

.. |DOI| image:: https://sandbox.zenodo.org/badge/168057818.svg
        :target: https://sandbox.zenodo.org/badge/latestdoi/168057818

.. |License| image:: https://img.shields.io/github/license/seignovert/test-python-docs.svg
             :target: https://github.com/seignovert/test-python-docs/

See `.readthedocs.yml <.readthedocs.yml>`_
to see how to configure
`Read the Docs <https://test-python-docs.readthedocs.io/>`_ deployment.

See `.travis.yml <.travis.yml>`_
files to see how to tests and build the docs and deploy it to:

- `PyPI <https://test.pypi.org/project/foo-docs/>`_
- `Github Releases <https://github.com/seignovert/test-python-docs/releases>`_
- `Github Pages <https://seignovert.github.io/test-python-docs/>`_
- `Zenodo DOI <https://sandbox.zenodo.org/record/257355>`_

Sphinx autobuild 
----------------

Install:

.. code:: bash

    $ pip install -r docs/requirements.txt

Start autobuild (with live reload):

.. code:: bash

    $ make livehtml


Zenodo DOI
----------

Github releases can be hook with
`Zenodo <https://guides.github.com/activities/citable-code/>`_
to get DOI for each release. See `.zenodo.json <.zenodo.json>`_
will provide automatically your metadata to Zenodo.

(Note: in this test case, we hooks our release with Zenodo
sandbox to avoid dummy publications, therefore the DOI is invalid).
