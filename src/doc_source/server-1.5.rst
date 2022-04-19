SFTPPlus Server 1.5 (obsolete)
==============================

SFTPPlus Server version 1.5, together with the 1.5.1 release series,
have reached the end of support.

Our recommendation is to upgrade to the latest version of SFTPPlus.
For more information about the current SFTPPlus release and the changes
in the new versions, please consult
:doc:`SFTPPlus Release Notes<release-notes>`.

SFTPPlus Server 1.5 is based on `OpenSSH <http://www.openssh.com/>`_ for
providing support for SFTP transfers and on
`VSFTPD <https://security.appspot.com/vsftpd.html>`_ for FTP/FTPS transfers.

The documentation for SFTPPlus Server version 1.5 (together with 1.5.1) is
available in PDF format from the following addresses:

    * `Installation guide for Linux and UNIX
      <http://proatria.com/downloads/SFTPPlus/SFTPPlus1.5.1/
      SFTPPlus%20Server1.5.1InstallationGuideforLinuxandUnix(PHP).pdf>`_

    * `Installation guide for Windows
      <http://proatria.com/downloads/SFTPPlus/SFTPPlus1.5.1/
      SFTPPlusServer1.5.1InstallationGuideforWindowsServer2003.pdf>`_

Additional documentation for configuring the SFTP and FTP/FTPS servers can
be found by consulting the documentation for OpenSSH and VSFTP
configuration files.

For FTP/FTPS, please consult the documentation for the `vsftpd.conf` file
available online at the following URL.
The same options are available inside the SFTPPlus Server
``/opt/SFTPPlus-server/etc/vsftpd.conf`` configuration file.

    * https://security.appspot.com/vsftpd/vsftpd_conf.html

For SFTP, please consult the documentation for the `sshd_config` file available
online at the following URL.
The same options are available inside the SFTPPlus Server
``/opt/SFTPPlus-server/ssh/sshd_config`` configuration file.

    * http://www.openbsd.org/cgi-bin/man.cgi?query=sshd_config&sektion=5
