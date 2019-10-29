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
