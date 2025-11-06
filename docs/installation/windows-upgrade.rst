Windows update
==============

..  contents:: :local:


General considerations
----------------------

When upgrading on Windows from a previous version,
there are different procedures that you can follow,
depending on the version to be upgraded.

Check if any custom paths or instance names are used for your installation.

You can check the installation path and instance name using the event `20072` from the log file, or the information deployed in the Web Manager Console.

Below are the default values:

* Installation path: `C:\\Program Files\\SFTPPlus\\`
* Instance name: `SFTPPlus`


Using the EXE self-installer
----------------------------

At first, manually stop the SFTPPlus Windows service.
Its default name is `SFTPPlus MFT`.
It might have a different name on custom installs.

Create a backup copy of the `configuration` directory
from the SFTPPlus installation path,
in case you need to revert the upgrade.
The default installation path is `C:\\Program Files\\SFTPPlus\\configuration`.

Execute the installer, selecting the same instance name and installation path
as the existing installation to be updated.

The installation process updates the files and automatically starts the Windows service when done.
There is no need to manually start the Windows SFTPPlus service.


Using the ZIP archive for automated updates
-------------------------------------------

SFTPPlus for Windows is also distributed as a ZIP archive.
This is designed for automated, non-interactive installations and updates.

The update process for the SFTPPlus ZIP archive is as follows:

* Stop the SFTPPlus Windows service.
* Copy the unpacked files over the existing installation.
* Start the SFTPPlus Windows service.


Windows Containers procedure
----------------------------

When using SFTPPlus within a Windows container, updating is as simple as extracting the ZIP archive and combining it with your specific SFTPPlus configuration files.

We assume that you have already defined your configuration file and placed the configuration file, together with any certificates or SSH keys, inside the same directory.

The update process steps would then be:

* Extract the ZIP archive.
* Copy your `configuration` directory to the SFTPPlus installation folder.


Upgrading from 32-bit Windows to 64-bit Windows
-----------------------------------------------

As long as a 32-bit Windows version of SFTPPlus is upgraded to a 64-bit version
using the same installation path, no extra steps are required on top of the
normal upgrade procedure.

Note that the default installation path for 32-bit Windows installations is
`C:\\Program Files (x86)\\SFTPPlus`, while for 64-bit installations it is
`C:\\Program Files\\SFTPPlus`.
When using default paths, these are the exact steps to follow:

1. Backup the current configuration directory from
   `C:\\Program Files (x86)\\SFTPPlus\configuration`.
2. Uninstall the existing 32-bit SFTPPlus application.
3. Install the new 64-bit SFTPPlus application.
4. After 64-bit SFTPPlus is installed, go to Windows services and stop the
   `SFTPPlus MFT` service.
5. Copy the previous configuration from
   `C:\\Program Files (x86)\\SFTPPlus\\configuration` to
   `C:\\Program Files\\SFTPPlus\\configuration`
6. Go to Windows Services and start the `SFTPPlus MFT` service.


Upgrading from SFTPPlus Version 3 Windows service
-------------------------------------------------

SFTPPlus version 2 and version 3 were operating the Windows service using a Windows service controller embedded into the main SFTPPlus process.

In SFTPPlus version 4 and newer, a separate dedicated Windows service process is used.

Starting with version 5, installing SFTPPlus automatically migrates the Windows service.

All SFTPPlus installations initially based on version 4.1.0 or newer
already have the newest controller installed and configured.
No extra changes are required when upgrading.

For SFTPPlus installations initially installed using an older version of SFTPPlus,
a warning message is displayed in the Web Administration Console and in the logs.
In this case, a reinstallation of the SFTPPlus Windows service is required.
Reinstalling the entire SFTPPlus application is **not** required.
Only the Windows Service needs to be reinstalled.

To reinstall the Windows service, follow these steps:

* Stop the current SFTPPlus Windows service.
* From the SFTPPlus installation directory, run as administrator the `service-uninstall.bat` script.
* From the SFTPPlus installation directory, run as administrator the `service-install.bat` script.
* Open the Windows Service administration tool, find the SFTPPlus service and open the `Properties` window.
* From the `Log on` tab, configure the Windows service account and password to be used to run SFTPPlus.
* Restart the SFTPPlus service.
