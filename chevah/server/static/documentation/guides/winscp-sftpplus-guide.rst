.. container:: tags pull-left

    `server-side`


Using WinSCP Client and SFTPPlus Server
#######################################

..  contents:: :local:


SFTPPlus MFT Server is compatible with any client software,
including WinSCP®.

In this quick guide, we will provide a very brief
overview showing how you can use WinSCP with SFTPPlus MFT
Server for Windows to perform basic actions.


Obtaining SFTPPlus
------------------

New to SFTPPlus? Please contact our Pro:Atria Sales team to
obtain an evaluation copy of SFTPPlus Server.

If you have a copy and this is your first time using SFTPPlus,
we recommend following the Windows installation
`guide <documentation/sftpplus/latest/installation/windows.html>`_
followed by our `quick steps guide <https://www.sftpplus.com/welcome.html>`_.


Prerequisites for using WinSCP with SFTPPlus Server
---------------------------------------------------

Make sure that you have the following details correct.
These details can be configured and/or checked using the SFTPPlus
Local Manager.
If you are new to SFTPPlus, you can follow the
`quick steps guide <https://www.sftpplus.com/welcome.html>`_ or see
our documentation for more details.

* You have WinSCP and SFTPPlus installed and running.

* The account is enabled.

* The account username and password are correct.

* The account home folder either exists or a new home folder is
  created if it does not exist.

* Ensure that the service account has the appropriate rights to
  modify/write/read the log and configuration folders (listed in the
  Windows installation
  `guide <documentation/sftpplus/latest/installation/windows.html>`_)

* A file transfer service using the targeted protocol (such as SCP,
  SFTP or FTPS Implicit) is running.


Using WinSCP for SFTP
---------------------

Add the `file protocol`, `host name`, `port number` and `username`
details.
The values used are part of our default configuration for the SFTP
service::

    host: localhost
    username: test_user
    password: test_password
    port: 10022

..  image:: /_static/guides/winscp-sftpplus-1.png
    :alt: Initial account details for the SFTP service.
    :width: 500px

And after connection, you will be presented with the SFTP server
fingerprint.
Since this testing is conducted on a new server key, a warning is
presented.
Please check the server key prior to accepting.
To use your own SSH keys, please configure the
`SFTP service </documentation/sftpplus/latest/configuration/ssh-service.html>`_
accordingly.

..  image:: /_static/guides/winscp-sftpplus-2.png
    :alt: Self-signed certificate for the SFTP service.
    :width: 500px

After logging in, you will now see the directory and start conducting file
transfer operations on the SFTP server.


Using WinSCP for FTPS
---------------------

Add the `file protocol`, `host name`, `port number` and `username`
details.
The values used are part of our default configuration for the FTPES
service::

    host: localhost
    username: test_user
    password: test_password
    port: 10021

..  image:: /_static/guides/winscp-sftpplus-4.png
    :alt: Initial account details for the SFTP service.
    :width: 500px

After logging in for the first time, Filezilla will present details
about the server certificate.
The certificate being used in the default SFTPPlus installation is a
self-signed.
To use your own certificate, please configure the
`FTPS service </documentation/sftpplus/latest/configuration/ftp-service.html>`_
accordingly.
For production, we highly recommend using your own certificate.

..  image:: /_static/guides/winscp-sftpplus-5.png
    :alt: Verify the self-signed certificate.
    :width: 500px

After logging in, you will now see the directory and start conducting file
transfer operations on the FTPS server.


Using WinSCP for SCP
--------------------

With the SCP service, you can only do file uploads and downloads,
as the SCP protocol is quite limited.
What you get from the Unix `cp` command, you also get from SCP, except
`scp` does not support folder listing, folder creation, folder removal,
and file removal.

WinSCP cannot be used together with SFTPPlus server to do SCP based
transfers.
This is because the SCP server implementation on SFTPPlus Server
only allows the standard `scp` command.
Since the `scp` commands does not support folder listing, WinSCP uses
a non-SCP command to list the directory and this non-standard
command is denied by SFTPPlus server as it it outside of the SCP scope.
From SFTPPlus Local Manager, you will see this message, which is
expected.

..  image:: /_static/guides/winscp-sftpplus-8.png
    :alt: SCP listing folder not available
    :width: 600px

This is also indicated in the logs for WinSCP which shows that
`ls -la` command being set to list directories:

    | 2018-03-22 17:55:37.966 LS: ls -la, Ign LS warn: Yes, Scp1 Comp: No
    | 2018-03-22 17:55:37.966 Local directory: default, Remote
      directory: home, Update: Yes, Cache: Yes
    | 2018-03-22 17:55:37.966 Cache directory changes: Yes,
      Permanent: Yes
    | 2018-03-22 17:55:37.966 Recycle bin: Delete to: No,
      Overwritten to: No, Bin path:

Followed by the expected message even after access is granted:

    | 2018-03-22 17:56:42.968 Access granted
    | 2018-03-22 17:56:42.968 Opening session as main channel
    | 2018-03-22 17:56:42.968 Opened main channel
    | 2018-03-22 17:56:42.970 Server refused to start a
      shell/command
    | 2018-03-22 17:56:42.982 (EFatal) Server refused to start
      a shell/commands
    | 2018-03-22 17:56:42.982 Authentication log (see session
      log for details):
    | 2018-03-22 17:56:42.982 Using username "test_user".
    | 2018-03-22 17:56:42.982 Authentication failed.

For more robust file transfer support involving SSH, we recommend
using the SFTP protocol which is also delivered over SSH version 2.
SFTP supports a rich set of file transport operations, not only
upload and download, like in the case of SCP.


Need support?
-------------

Please contact the Pro:Atria Support team if you have questions about
using your own client with SFTPPlus or if you also wish to trial our
own SFTPPlus Client software.

This guide is based on SFTPPlus 3.30.0 and WinSCP 5.13.

Note that WinSCP is a registered trademark of its respective owners.
