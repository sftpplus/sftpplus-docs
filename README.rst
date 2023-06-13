docs.sftpplus.com
=================

.. image:: https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png
  :target: https://creativecommons.org/licenses/by-nc-sa/4.0/

The documentation for the SFTPPlus product.

There is an `update-docs.sh` script that should be called, while the
`chevah/server` repo is checkout at the release branch.

You should push the changes on the `main` branch.
The main branch will be always updated with the latest release.
You should also create a version dedicated branch with the format `v4-18-0`
and push the changes for that version.

To build the documentation you need a Python3.8 (or newer) environment.::

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    sphinx-build -b html src/doc_source/ deploy

To test the docs for any errors and view in a browser::

    sphinx-build -b html -W --keep-going src/doc_source/ deploy
    python -m http.server -d deploy/
    firefox http://localhost:8000


Sync with product development
-----------------------------

Generate the documentation source and template from the product repository::

    cd chevah-server
    ./brink.sh documentation_website
    cp -r build-server/doc_source ../sftpplus-docs/src/
    cp -r build-server/lib/python2.7/site-packages/sftpplus_website/sphinx ../sftpplus-docs/

Copy any source file documented via API docs to `doc_source/chevah`.

Update doc_source/conf.py to load local theme files::

    templates_path = ['../../sphinx']
    html_static_path = ['_static']
    html_theme_path = ['../../sphinx']
    html_theme = 'integrated'


Generate PDF file
-----------------

Update doc_source/conf.py to load local theme files::

    html_theme = 'sphinx_rtd_theme'

Generate a single HTML page and then from a browser "print" it as PDF.::

    sphinx-build -b singlehtml doc_source/ deploy
