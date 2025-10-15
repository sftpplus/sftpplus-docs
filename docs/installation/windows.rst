Windows Installation
====================

..  contents:: :local:


Overview
--------

For Microsoft Windows systems,
SFTPPlus is available as an self-extract executable or as a .ZIP archive.

The installation files are available on our download page.

Once SFTPPlus is installed,
use the `Web Manager`` administrative interface to configure and operate SFTPPlus.
It can be accessed by default at `https://localhost:10020`.

The SFTPPlus application files must be installed on a local drive.
Installation on a Windows Share or a network mapped drive is not supported.

The configuration file or log file can be stored on a network Windows Share.
You can find more details on this page.

The default installation will create a Windows Service that will start SFTPPlus using the `Local System` account.
It is recommended to create a dedicated service account for SFTPPlus
and then reconfigure the Windows service.
More details about setting a dedicated service account can be found on this page.

The automatic installation process will generate a new configuration file,
together with the associated SSH keys and the SSL self-signed certificate.


Self-extract executable
-----------------------

In order to install SFTPPlus follow the steps:

1. Locate and launch the installer executable.
   It will automatically switch to run as an administrator and start the installation process.

2. Review the License Agreement and click the `Agree` button.

3. If you plan to run multiple SFTPPlus services on the same operating system,
   use a custom name for each instance.
   Otherwise use the default instance name.

4. Optionally, you can select a custom installation path.

5. The installer will ask to define the credentials used to access the Web Manager. You will use this username and password to connect to the management interface,
   once the installation was completed.

6. As the final step, click `Install`. This will install SFTPPlus and will automatically start the Windows Service.

7. When the installation completes, click `Close`.


ZIP archive installer
---------------------

The .ZIP archive can be used for Server Core without the Desktop Experience
or with automated deployment and provisioning tools.

To install follow these steps:

1. Unpack the ZIP file and copy the server folder to your preferred install location, e.g. ``C:\\Program Files\\SFTPPlus\``.

2. Initialize the environment using the default values by running the following command in a command line as Administrator::

    CMD> admin-commands.bat initialize --init-password PLAIN-TEXT-PASSWORD

where, --init-password defines the password used by the default administrator `admin`.
It will be used to connect to the Web Manager once the installation is completed.

Some customization can be made at this stage using the following arguments:

* --init-admin defines the username of the administrator used to connect to the management interface (default is `admin`);
* --local-admin-access forces the access to the management only from localhost (by default will allow access from any host);
* --key-size generates a RSA or DSA key of size SIZE (default size is 3072).

Here is an example for a customized initialization::

    CMD> admin-commands.bat initialize --init-admin sftpplus-admin --init-password wX67%7B8AtvI --local-admin-access --key-size 4096

In the install folder a new configuration file is created along with the scripts required to run the application server as a Windows service.

3. Once the SFTPPlus configuration is successfully initialized, the `service-install.bat` can be executed in order to finalize the installation::

    CMD> service-install.bat

After the service is installed, regular Windows Services management tools
can be used for starting, stopping, restarting, or removing it.


Configure a dedicated Windows service account
---------------------------------------------

For security reasons, creating a dedicated service account is recommended.
Use the newly created service account to run the SFTPPlus service after completing the installation.

The following is a list of steps to configure the service.

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


Multi-instance/parallel SFTPPlus installations
----------------------------------------------

Multiple SFTPPlus instances can be installed and operated in parallel on the
same machine or VM.

For example, you can use one instance for the testing/staging environment
and another one for the production environment.

During the installation process, you will need to choose for each installation
a unique `instance name` and a unique installation path.

When running on the same system, parallel SFTPPlus instances
can't use the same port numbers.

To manage parallel SFTPPlus instances, after installing the first SFTPPlus
instance, connect to the Web Manager web-based console and change the
management port from the default value of ``10020`` to a different one.
For example, you can use the following port convention
for their management ports:

* `10031` - for the first instance
* `10032` - for the second instance
* `10033` - for the third instance


Load the configuration file from a network Windows Share
--------------------------------------------------------

While the SFTPPlus application files should be stored on a local drive,
you can configure the SFTPPlus Windows service to load the configuration file from a network Windows Share.

The SFTPPlus Windows service account should have read and write permissions to the remote network location.

It is highly recommended to use a dedicated service account for SFTPPlus.

If using a domain service account, make sure that the domain account has permissions on that share.

If using the default `Local System` account, make sure the domain machine has permissions.
This creates a less secure configuration, as any other application from the machine that runs SFTPPlus will have access to the SFTPPlus configuration file.

The default SFTPPlus installation will configure the Windows service to load the configuration file from the local drive.

We need to reconfigure the SFTPPlus Windows service.
One option is to uninstall the existing Windows service for SFTPPlus,
and reinstall it with the updated configuration path.

We only need to reinstall the Windows service, not the whole SFPPlus installation.

Start by removing the existing Windows service::

    CMD> service-uninstall.bat

Open the `service-install.bat` file with a text editor.

Check for a line ending with ``start-in-foreground --config configuration\server.ini``.
This is the line that installs the SFTPPlus Windows service and configured the path from where the configuration file is loaded.

Replace the ``--config configuration\server.ini`` with the path to your network locations.
For example ``--config \\central-uk.acme.org\infra\sftpplus\server.ini``.

Install the new Windows service::

    CMD> service-install.bat

The service will be installed using the default `Local System` account.
use the `Windows Services` tool to reconfigure the `SFTPPlus MFT` service to start using the dedicated service account.

You can now start the SFTPPlus Windows service and it will load and save the configuration changes from a network location.


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


* `.\\lib` - `read-only` -
  This folder is for internal server use.

* `.\\log` - `read`, `write`, `create file` and `delete file` -
  Stores all SFTPPlus log messages.
  SFTPPlus will write log entries into the log files.
  When log rotation is enabled, it will also create new rotated files and
  delete old rotated files.

* `.\\run` - `read`, `write`, `create file` and `delete file`
  Stores various SFTPPlus runtime information.
