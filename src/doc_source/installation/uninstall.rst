Uninstalling SFTPPlus on Windows
================================

Uninstalling SFTPPlus is a straightforward process, and it can
be initiated using any of the following methods:

* Using the `Uninstall SFTPPlus` link from the Windows Programs Menu.
* Using the *Programs and Features* Windows feature in *Control Panel*.
* From a command line, by running the uninstaller available in the SFTPPlus
  installation folder.

Regardless of the uninstallation method used, the following sub-directories in
the installation directory will have to be manually removed once the process
is completed:

* `configuration`
* `log`


Silently uninstalling SFTPPlus
------------------------------

In order to silently uninstall SFTPPlus,
open a command line with full administrator access rights
(Run As Administrator).

Then go to the installation path of SFTPPlus and run the uninstaller
with the following parameters::

    SFTPPlus-windows-x86-VERSION-uninstall.exe /S _?=Installation\Path

Where:

* `VERSION` - is the version of SFTPPlus running in your environment

* ``/S`` - makes the uninstallation process silent

* ``_?`` - defines the installation directory.


Uninstalling SFTPPlus on Linux and macOS
========================================

To uninstall SFTPPlus on Linux and macOS systems, first make sure it is stopped.
Then save its configuration and logs, if relevant.

You may use the ``bin/uninstall.sh`` script in the hierarchy of SFTPPlus files.
Following examples assume paths typical for a default SFTPPlus installation.

On Linux::

    /opt/sftpplus/bin/uninstall.sh

On macOS::

    /Library/sftpplus/bin/uninstall.sh

If you prefer to uninstall SFTPPlus manually, after stopping the SFTPPlus server
(and optionally saving its configuration and logs), follow the sections below.


Removing unit, init, service files
----------------------------------

The init-related SFTPPlus files are specific to the local operating system.
Use the following exemplified commands as a guide.
They assume your init-related SFTPPlus files are using
the generic names suggested in the installation documentation.

On systemd-based Linux systems::

    systemctl disable sftpplus-mft.service
    rm /etc/systemd/system/sftpplus-mft.service

On SysV-based Linux systems such as RHEL 5/6, SLES 11,
Amazon Linux AMI 2018.03::

    chkconfig --del sftpplus-mft
    rm /etc/init/sftpplus-mft

On Alpine Linux::

    rc-update del sftpplus-mft
    rm /etc/init.d/sftpplus-mft

On macOS::

    launchctl unload /Library/LaunchDaemons/sftpplus.plist
    rm /Library/LaunchDaemons/sftpplus.plist


Removing SFTPPlus files
-----------------------

First of all, make sure you have backed up any SFTPPlus configuration and log
files that might be useful later.

The following commands remove all remaining SFTPPlus-related files
from a typical installation path.

On Linux::

    rm -rf /opt/sftpplus

On macOS::

    rm -rf /Library/sftpplus


Removing SFTPPlus user and group
--------------------------------

Assuming the ``sftpplus`` user and group were added for running SFTPPlus,
the following commands remove them.

On Linux::

    userdel sftpplus

..  note::
    On Alpine Linux, the shadow package might not be installed.
    In that case, use::

        deluser sftpplus

On macOS::

   dscl . delete /Users/sftpplus
   dscl . delete /Groups/sftpplus
