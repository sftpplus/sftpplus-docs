docs.sftpplus.com
=================

.. image:: https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png
  :target: https://creativecommons.org/licenses/by-nc-sa/4.0/

The documentation for the SFTPPlus product.

To build the documentation you need a Python environment.
(python3 upgrade soon)::

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    sphinx-build -b html doc_source/ deploy

To test the docs for any errors and view in a browser::

    sphinx-build -b html -W --keep-going doc_source/ deploy
    python -m http.server -d deploy/
    firefox http://localhost:8000


Sync with product development
-----------------------------

Generate the documentation source and template from the product repository::

    cd chevah-server
    ./brink.sh documentation_website
    cp -r build-server/doc_source ../sftpplus-docs/
    cp -r build-server/lib/python2/7/site-packages/sftpplus_website/sphinx ../sftpplus-docs/

Copy any source file documented via API docs to `doc_source/chevah`.

Update doc_source/conf.py to load local theme files::

    templates_path = ['../sphinx']
    html_static_path = ['_static']
    html_theme_path = ['../sphinx']
