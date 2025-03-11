Linux or macOS update
=====================

..  contents:: :local:


Introduction
------------

Updating SFTPPlus involves installing latest SFTPPlus application files,
while preserving the installation's configuration file and user data.

This page documents *fully automated* updates, *assisted* updates, and *manual* updates.

When SFTPPlus has egress/outgoing connection to the Internet,
we recommend using the fully automated update process.

Without outgoing Internet access,
we recommend downloading latest SFTPPlus package on another system,
copying it to the server running SFTPPlus,
and then running the assisted update process.

The automated and assisted method automatically create backups of the existing installation,
stopping and restarting the system SFTPPlus service as needed.

The manual method is provided to help you understand how the SFTPPlus process works,
and to allow creating custom update procedures.

..  note::
    Regardless of the chosen updating procedure,
    check if any custom paths are used for the SFTPPlus installation.
    Documentation instructions use default paths and may
    need to be adapted accordingly when using custom paths.


Fully automated
---------------

Since version 5.5.0, the `bin/auto-update.sh` script is provided as the recommended update method.

..  attention::
    The fully automated method needs egress / outgoing access to the Internet.
    Otherwise, procure the latest SFTPPlus package first,
    then follow the assisted update process.

The `bin/auto-update.sh` script automatically downloads latest SFTPPlus package,
backs up the existing application and configuration files,
installs the latest version, and restarts the system SFTPPlus service.

This script is typically called without any arguments::

    $ sudo /opt/sftpplus/bin/auto-update.sh

It is designed to be run automatically without any human input,
making it suitable for fully automated deployments.

If the current SFTPPlus installation is already using latest version,
it doesn't do anything, outputting nothing if running non-interactively.
This allows you to run it as a daily or weekly schedule job,
for example under `cron`.

It uses the `/tmp/` directory to temporarily store downloaded files.

It automatically stops and restarts the system SFTPPlus service.

Backups of the current installation are automatically created.

To try it without updating, use the `-d|--dry` options.
You can use this functionality to alert you when there is an SFTPPlus update available.
For that, make use of its error code, as this script is only successful when finding an update.


Assisted update
---------------

Since version 4.26.0, you can use the included `bin/update.sh` script to assist you with updating SFTPPlus.

It can be used when there is no access to the Internet to automatically download the installation package.

Copy the package on the server running SFTPPlus, then call the script with the path to the package file.
This example assumes you have copied the SFTPPlus installation package to the `/tmp/` directory::

    $ sudo /opt/sftpplus/bin/update.sh /tmp/sftpplus-os-arch-version.tar.gz

The `bin/update.sh` script automatically stops and restarts the system SFTPPlus service as needed.

Backups of the current installation are automatically created.


Update using the self-extractable package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also use the self-extractable SFTPPlus package relevent for your operating system to do an assisted update of an existing installation.
Simply point the downloaded `.sh` package to the install path of SFTPPlus (either through a parameter or interactively)::

    $ sudo /bin/sh ./sftpplus-os-arch-version.sh /opt/sftpplus

After a few starting checks, the `bin/update.sh` script from your existing SFTPPlus installation is used to update your installation using the content of the self-extractable SFTPPlus package, exactly as describe above in the assisted update section.


Update from trial version
-------------------------

To update to a licensed SFTPPlus installation when starting with the trial version,
download the full version of SFTPPlus, then copy it to the system running the SFTPPlus trial version.
Both the gzipped TAR and the self-extractable packages can be used.

You can then follow the same steps as for the assisted update above.

Once updated to the licensed version,
future SFTPPlus updates can be done either using the fully automated method
or through the assisted method.


Assisted rollback
-----------------

The `bin/rollback.sh` script is designed to assist you with reverting the SFTPPlus installation to a previous version.

You can automatically rollback to the last saved backup
by calling the script without any arguments::

    $ sudo /opt/sftpplus/bin/rollback.sh

To rollback to a backup other than the last one automatically saved by the `bin/update.sh` script,
you can provide the path to its directory as a parameter to the `bin/rollback.sh` script::

    $ sudo /opt/sftpplus/bin/rollback.sh /opt/sftpplus_backups/sftpplus-mft_ROLLBACK_20240518-043209

The following directory is used by default for backing up SFTPPlus installations:

* `/opt/sftpplus_backups/`

Assuming that SFTPPlus was installed using the default `sftpplus-mft` service name,
these are the default symbolic links for update and rollback backups:

* `/opt/sftpplus_backups/sftpplus-mft_UPDATE_AUTO_BACKUP` - the SFTPPlus installation prior to the last automated or assisted update
* `/opt/sftpplus_backups/sftpplus-mft_ROLLBACK_AUTO_BACKUP` - the SFTPPlus installation prior to the last rollback

The above symbolic links point to backup sub-directories which, by default, have names such as:

* `/opt/sftpplus_backups/sftpplus-mft_UPDATE_AUTO_BACKUP_20240418-043210`
* `/opt/sftpplus_backups/sftpplus-mft_UPDATE_AUTO_BACKUP_20240511-043209`

The symbolic links are updated during SFTPPlus automatic and assisted updates, and during rollbacks.

SFTPPlus backups are never automatically removed.


Manual update
-------------

Before bringing a SFTPPlus installation to the latest available version,
you must stop the associated system service.

Backup the entire SFTPPlus installation, especially the server configuration file.

Extract the latest SFTPPlus package files over the existing installation sub-directory.

Review the permissions and ownership of the extracted files.

Once all new files are in place and their permissions are reviewed,
you can restart the SFTPPlus service.

To find out more about the latest SFTPPlus version and any relevant changes
between the current version of your installation and the latest release, please consult
the :doc:`Server Release Notes<../release-notes>`.
