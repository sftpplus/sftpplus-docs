.. container:: tags pull-left

    `server-side`


Using Filezilla Client with SFTPPlus Server
###########################################

SFTPPlus MFT Server is compatible with many client software,
including Filezilla® Client.

In this quick User Guide, we will provide a very brief overview
showing how you can use Filezilla Client with SFTPPlus to perform
basic actions.
We are using Filezilla Client as an example, since it is one of
the more commonly used GUI-based client software used by our
customers.
While we support multiple operating systems, this guide is based
on the Windows platform.


Obtaining SFTPPlus
------------------

New to SFTPPlus? Please contact our Pro:Atria Sales team to obtain
an evaluation copy of SFTPPlus Server.

If you have a copy and this is your first time using SFTPPlus, we
recommend following the Windows installation
`guide <documentation/sftpplus/latest/installation/windows.html>`_
and our `quick steps guide <https://www.sftpplus.com/welcome.html>`_.


Prerequisites for using Filezilla Client with SFTPPlus FTPS Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make sure that you have the following details correct.
These details can be configured and/or checked using the SFTPPlus
Local Manager.
If you are new to SFTPPlus, you can refer to the
`quick steps guide <https://www.sftpplus.com/welcome.html>`_ or see
our documentation for more details.

* You have the Filezilla Client and SFTPPlus installed and running.

* The account is enabled.

* The account username and password are correct.

* The account home folder either exists or a new home folder is created
  if it does not exist.

* Ensure that the service account has the appropriate rights to
  modify/write/read the log and configuration folders (as listed in
  the Windows installation
  `guide <documentation/sftpplus/latest/installation/windows.html>`_)

* The protocol and service (such as SFTP or FTPS) is enabled and
  running.


Logging into the account using Filezilla for the first time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the `host`, `username`, `password` and `port` details.
The values used are::

    host: localhost
    username: test_user
    password: test_password
    port: 10021

These values would also change depending on your own setup.

..  image:: /_static/guides/filezilla-ftps-1.png
    :alt: Initial login of the account from Filezilla.

After logging in for the first time, Filezilla will present details
about the server certificate.
The default certificate being used is a self-signed certificate.
To use your own certificate, please configure the
:doc:`FTPS service </configuration-server/ftp-service>` accordingly.

..  image:: /_static/guides/filezilla-ftps-2.png
    :alt: Filezilla presenting the server certificate.

After successfully logging in, you are presented with the home
folder, files and directories associated with the account.

..  image:: /_static/guides/filezilla-ftps-3.png
    :alt: Filezilla presenting the home folder and files in the FTPS server.

Drag and drop files to upload, use the GUI to rename files/folders
and process other actions.

..  image:: /_static/guides/filezilla-ftps-4.png
    :alt: Filezilla drag and drop of files to be uploaded to the FTPS server.


Using Filezilla Client with SFTPPlus SFTP Server for the first time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similar to using the FTPS server, change the entry to use the SFTP
port and address:

..  image:: /_static/guides/filezilla-ftps-5.png
    :alt: Filezilla change details for SFTP server.

And after connection, you will be presented with the SFTP server
fingerprint.
Since this testing is conducted on a new server key, a warning is
presented.
Please check the server key prior to accepting.
To use your own SSH keys, please configure the
:doc:`SFTP service </configuration-server/ssh-service>` accordingly.

..  image:: /_static/guides/filezilla-ftps-6.png
    :alt: Filezilla drag and drop of files to be uploaded to the SFTP service.


Using Filezilla Client verbose logging
--------------------------------------

For troubleshooting issues, we recommend also turning on verbose
logging and capturing the output to determine if the issue has a
client-side component.

To enable, go to the Debug section in the Settings screen and choose
the level of debugging required.


Need support?
-------------

Please contact the Pro:Atria Support team if you have questions about
using your own client with SFTPPlus or if you also wish to trial our
own SFTPPlus Client software.

This guide is based on SFTPPlus 3.30.0 and Filezilla Client 3.31.0.

Note that FileZilla is a registered trademark of its respective owners.
