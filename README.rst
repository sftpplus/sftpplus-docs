docs.sftpplus.com
=================

.. image:: https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png
  :target: https://creativecommons.org/licenses/by-nc-sa/4.0/

The documentation for the SFTPPlus product.

To build the documentation you need a Python3 environment::

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    sphinx-build -b html doc_source/ deploy
