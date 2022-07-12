Getting Started with SFTPPlus on Linux
======================================

..  contents:: :local:


Download and installation steps
-------------------------------

Open your terminal and change the directory to where you downloaded the
SFTPPlus package.

..  code-block:: bash

    $ ls
    sftpplus-lnx-x64-trial.tar.gz
    $ tar -xf sftpplus-lnx-x64-trial.tar.gz

To complete the installation, SFTPPlus will generate an initial
configuration file.
This initialization only needs to be done once and is not required for
future upgrades.
Choose a secure administrator password.

..  code-block:: bash

    $ cd sftpplus-lnx-x64-trial
    $ ./bin/admin-commands.sh initialize --init-password «ADMIN_PASSWORD»


.. include:: /quick-start/admin-credentials.include.rst


Adjust the default configuration file and start the service
-----------------------------------------------------------

In order to explore the SFTPPlus features, we will use the default
configuration file in which we enable a test account named
``test_user`` with the password ``test_password``.
The files for this account are stored in ``/tmp/test_user-files``.
SFTPPlus comes with extensive documentation for all of the sections:

* :doc:`accounts </configuration-identity/accounts>` and
  :doc:`groups </configuration-identity/groups>`

* :doc:`authentication methods </configuration-auth/index>`

* :doc:`services </configuration-server/index>`


You can fully configure the SFTPPlus server using the configuration file
available at ``configuration/server.ini``.

You also have the option of configuring SFTPPlus from a web based management
console.
The web console is available by default on ``https://127.0.0.1:10020``.

To help with testing and quick troubleshooting we will start the service in
debugging mode.
On start SFTPPlus will provide detailed information about the services,
connections and errors if there will be any.

..  code-block:: bash

    $ ./bin/admin-commands.sh debug


Enable the test account
-----------------------

The SFTPPlus Local Manager is the web console available over HTTPS on
port 10020.
It comes with a default administration account. The username is ``admin`` and
the password is the one chosen for ``«ADMIN_PASSWORD»`` during initialization.
Use the credentials to log in before proceeding with the next step.

If you get the **This site is not secure** message, click on the **Details** and
then **Go on to the webpage**. This message is due to your self-signed SSL
certificate, which SFTPPlus generates as part of the installation process.

The default configuration also provides a test account test_user with
the password test_password. For security reasons, this account is disabled by
default.
To enable this account, find the Accounts section and click on the test_user.

Next we will enable the account. Change the home folder.
And finally enable SFTPPlus to create the missing new home folder.
You can find all the options we need to change below:

* Enabled: **Yes**
* File access -> Path: ``/tmp/test_user-files/``
* Advanced account configurations -> Create missing home folder: **Yes**

..  figure:: /_static/guides/2_account.png
    :alt: SFTPPlus Account Configuration
    :class: "mb-1 pt-2 bg-gray rounded-sm border-img grayscale"

..  figure:: /_static/guides/2_account_home.png
    :alt: SFTPPlus Account Home Folder Configuration
    :class: "mb-1 pt-2 bg-gray rounded-sm border-img grayscale"

..  figure:: /_static/guides/2_account_create_home.png
    :alt: SFTPPlus Account Home Folder Creation
    :class: "mb-1 pt-2 bg-gray rounded-sm border-img grayscale"

In order to apply the changes, scroll down to the bottom of the page and
click **Review and apply**. SFTPPlus will show all the changed configurations
to be applied and show which components require a restart.
To proceed, click **Apply all changes**.

..  figure:: /_static/guides/2_review.png
    :alt: SFTPPlus Review Configuration Changes
    :class: "mb-1 pt-2 bg-gray rounded-sm border-img grayscale"


Connect to the server and upload a file
---------------------------------------

You can use any SFTP client to connect and upload or download the files from
the SFTPPlus server. We will be using FileZilla to upload a test file.
Open FileZilla and fill in the following values:

* Host: ``sftp://127.0.0.1``
* Username: ``test_user``
* Password: ``test_password``
* Port: ``10022``

Next click **Quickconnect**. Please accept the SSH key fingerprint warning
that FileZilla will show. The SSH fingerprint is derived from the SSH keys
generated as part of the SFTPPlus installation. Use the **Local site** panel in
FileZilla to point to a location with a file for upload.
In the screenshot, we created and uploaded an empty text file from the Desktop
folder.

..  figure:: /_static/guides/3_upload.png
    :alt: SFTPPlus FileZilla Upload
    :class: "mb-1 pt-2 bg-gray rounded-sm border-img grayscale"

Upon completion, this file should be available in the earlier defined home
folder location.

You can use a graphical SFTP client or the command line ``sftp(1)`` remote file
copy program provided by most of the modern Linux distributions to upload and
download the files. In the example below, the transferred file will be stored at
``/tmp/test_user-files/README-sftp-test``, to run it,
open a new console window::

    $ sftp -P 10022 test_user@127.0.0.1
    test_user@127.0.0.1's password:
    Connected to 127.0.0.1.
    sftp> put doc/README README-sftp-test
    sftp> quit
    $ ls -l /tmp/test_user-files/


.. include:: /quick-start/configuration-items.include.rst

.. include:: /quick-start/log-files.include.rst
