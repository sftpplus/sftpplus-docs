Windows Installation
====================

..  contents:: :local:


Overview
--------

For Microsoft Windows systems, SFTPPlus is distributed as an
installation package.

To install SFTPPlus, you will have to launch the server installer as a
Windows Administrator.

An installation log file will be generated and stored inside the installation
folder.
The name of the file is `install.log`.

On Windows systems, the server runs as a single service and by
default it will run under the SYSTEM account.

When launched, the server will log the privileges enabled for the account
used for running SFTPPlus.
This can be used for debugging privilege-related issues.

The automatic installation process will generate a new configuration
file, together with the associated SSH keys and the SSL self-signed
certificate.

..  note::
    The server must be installed on a local drive.
    Installing the server on a network mapped drive is not supported.
    However, SFTPPlus can serve files stored on network mapped drivers to its
    clients.


Manual installation of SFTPPlus
-------------------------------

A ZIP archive of the server installation package can be provided on request.

To install the server, copy the server folder to your preferred install
location, e.g. `C:\\Program Files`.

For Windows systems, the following BAT files are provided to install and
uninstall the service.
These must be executed as an administrator::

    CMD> service-install.bat
    CMD> service-start.bat
    CMD> service-uninstall.bat

After the service is installed, regular Windows Services management tools
can be used for starting, stopping, restarting, or removing it.


Multi-instance/parallel SFTPPlus installations
----------------------------------------------

Multiple SFTPPlus instances can be installed and operated in parallel on the
same machine or VM.

For example, you can use one instance for the testing/staging environment
and another one for the production environment.

During the installation process, you will need to choose for each installation
a unique `instance name` and a unique installation paths.

When running on the same system, parallel SFTPPlus instances
can't use the same port numbers.

To manage parallel SFTPPlus instances, after installing the first SFTPPlus
instance, connect to the Local Manager web-based console and change the
management port from the default value of ``10020`` to a different one.
For example, you can use the following port convention
for their management ports:

* `10031` - for the first instance
* `10032` - for the second instance
* `10033` - for the third instance


Silent installation of SFTPPlus
-------------------------------

In order to perform a silent installation of SFTPPlus,
open a command line with full administrator access rights
(Run As Administrator).

Then go to the SFTPPlus' distributable location and run the following
command::

    CMD> sftpplus-windows-x86-VERSION.exe /S [/D=c:\path\to\install folder]

Note that:

* ``VERSION`` is the SFTPPlus distributable version.

* ``/S`` makes the installation process silent.

* ``/D`` defines the installation directory.
  If no value is defined for it, it will install the server in the default
  location such as `C:\\Program Files (x86)\\SFTPPlus` for x64 environments or
  `C:\\Program Files\\SFTPPlus` for x86 environments.

* If a custom ``/D`` installation path is desired, the parameter
  ``/D=Custom\\installation\\path`` can be used.
  It must be the last parameter used in the command line and must not
  contain any quotes, even if the path contains spaces.
  Only absolute paths are supported.

..  note::
    When installing in silent mode, the installation log file will not be
    generated.


Post-installation considerations
--------------------------------

For security reasons, creating a dedicated service account is recommended.
Use the newly created service account
to run the SFTPPlus service after completing the installation.

The following is a list of explicit steps to configure the service
successfully.

* Create a new standard Windows user account via *Control Panel*.
  Go to *User Accounts* then *Manage Account* and select the *Create new
  Standard account* option.

* Alternatively, use the *Computer Management* administrative tool.
  Go to *Local Users and Groups*, then *Users* and select *New User*.

* Open *Windows Services*, select the SFTPPlus service and stop it.
  In its *Properties* window, select the *Logon* tab and set the *Log on as*
  to be the newly created OS account.

* Open the *Registry Editor* and navigate to:

  | HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\services\\eventlog\\
    Application\\sftpplus-service

* Access the *Permission* windows for the ``sftpplus-service`` registry key
  and grant full control for the dedicated OS account.

* Ensure that the service account has the appropriate rights to
  modify/write/read the ``log`` and ``configuration`` folders.

* To allow the server to create missing home folders under a Windows system,
  the account used for running SFTPPlus will require backup and
  restore privileges. In the *Local Security Policy* administrative tool, go to
  *Local Policies*, then *User Rights Assignment*, and add the account
  to *Back up files and directories* and *Restore files and directories*
  policy settings.

* Alternatively, you can use the *Computer Management* administrative tool.
  Go to *Local Users and Groups*, *Groups* and add the user to the
  *Backup operators* group.

* Start the SFTPPlus service.


Server folders hierarchy and permissions
----------------------------------------

Once installed, SFTPPlus should have the following hierarchical
folder structure on disk.

The following also describes the permissions required for the service account.

* `.\\` - `read-only` -
  Contains server administration commands and the init script.

* `.\\configuration` - `read-only`
  Stores all data related to SFTPPlus configuration.

* `.\\configuration\\server.ini` - `read-and-write`
  Stores the main configuration.

* `.\\doc` - `read-only` -
  Contains server documentation and release notes.

* `.\\extension` - `read-only`
  Contains custom extensions implemented using the SFTPPlus API.

* `.\\include` - `read-only` -
  This folder is for developers interested in extending the
  functionality of the server.
  May be missing on some releases.

* `.\\lib` - `read-only` -
  This folder is for internal server use.

* `.\\log` - `read`, `write`, `create file` and `delete file` -
  Stores all SFTPPlus log messages.
  SFTPPlus will write log entries into the log files.
  When log rotation is enabled, it will also create new rotated files and
  delete old rotated files.

.. include:: first-steps.include
