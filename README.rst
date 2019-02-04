Test Python Docs
=================

|Docs| |RTD| |Build| |Coverage| |Github| |License| |Tag|

.. |Docs| image:: 	https://img.shields.io/readthedocs/test-python-docs.svg?logo=read-the-docs&logoColor=white
          :target: https://readthedocs.org/projects/test-python-docs/

.. |RTD| image:: https://img.shields.io/badge/readthedocs.io-test--python--docs-blue.svg?logo=read-the-docs&logoColor=white
          :target: https://test-python-docs.readthedocs.io/

.. |Build| image:: 	https://img.shields.io/travis/seignovert/test-python-docs.svg?logo=travis-ci&logoColor=white
           :target: https://travis-ci.org/seignovert/test-python-docs

.. |Coverage| image:: https://img.shields.io/coveralls/github/seignovert/test-python-docs.svg?logo=travis-ci&logoColor=white
              :target: https://coveralls.io/github/seignovert/test-python-docs

.. |Github| image:: https://img.shields.io/badge/github.io-test--python--docs-blue.svg?logo=github&logoColor=white
          :target: https://seignovert.github.io/test-python-docs/

.. |License| image:: https://img.shields.io/github/license/seignovert/test-python-docs.svg
             :target: https://github.com/seignovert/test-python-docs/

.. |Tag| image:: https://img.shields.io/github/tag/seignovert/test-python-docs.svg
          :target: https://github.com/seignovert/test-python-docs/releases

See `.readthedocs.yml <.readthedocs.yml>`_
to see how to deploy to
`Read the Docs <https://test-python-docs.readthedocs.io/>`_

See `.travis-ci.yml <.travis-ci.yml>`_
files to see how to tests and build the docs and deploy it to
`Github Pages <https://seignovert.github.io/test-python-docs/>`_.

Sphinx autobuild
----------------

Install:

.. code:: bash

    $ pip install -r docs/requirements.txt

Start autobuild:

.. code:: bash

    $ make livehtml
