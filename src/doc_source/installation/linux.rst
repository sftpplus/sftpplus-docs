Linux Installation
==================

..  contents:: :local:


Overview
--------

For Linux systems, SFTPPlus is distributed as a self-extractable `.sh`
shell script or as a `tar.gz` gzipped TAR archive.
These packages are to be found on the online download page for SFTPPlus.
For example, the link for trial SFTPPlus packages is
https://www.sftpplus.com/documentation/sftpplus/trial/.

Using a dedicated system account to run SFTPPlus is strongly recommended.
By default, a new system user named ``sftpplus`` is created during installation.
This is a special type of OS user also known as a service account.
You can customise the name of this user during installation.
You can also use an already existing user, but make sure it can access
the location of the installed product.

This dedicated OS user should not be used in any other way,
doesn't require a password to be set for it,
and should not be available through SFTPPlus services
even if authenticating operating system users is enabled.

Optionally, on Linux systems you may choose to start SFTPPlus as root,
especially if you want it to authenticate operating system users.
The service account is still required in order to drop privileges
for all other operations.


Self-extractable installer
--------------------------

To install SFTPPlus using the `.sh` self-extractable shell script,
simply launch it in a terminal with superuser privileges. For example::

   sudo /bin/sh ./sftpplus-os-arch-version.sh

The self-extractable installer asks for the destination path.
To set it non-interactively, add the installation directory as an argument::

   sudo /bin/sh ./sftpplus-os-arch-version.sh /opt/sftpplus

Paths with spaces or special characters are not supported by our installers.
To check all available options for the SFTPPlus installation::

   /bin/sh ./sftpplus-os-arch-version.sh -- --help

Some more options are set interactively during installation,
such as the name of the system user to run SFTPPlus and
the name of the default administrative account and its password.

A successful installation also configures SFTPPlus to run at boot.
Use the usual `systemd` commands to manage its service. For example::

    systemctl status sftpplus-mft

See the section on starting and stopping SFTPPlus at the end of this page
for more details on systemd integration.

If your Linux distribution doesn't use systemd, check
the :doc:`advanced Linux installation page</installation/linux-advanced>`.

Only read this page further if you need to
manually tweak the installation process of SFTPPlus
beyond the options available through the self-extractable installer.


Installing using the gzipped TAR archive
----------------------------------------

Installing SFTPPlus using the `tar.gz` gzipped TAR archive consists of
unpacking the archive, initializing the configuration, and generating the
SSH keys and the SSL key / certificate pair to be used by the product.

To have SFTPPlus started at boot, you can use one of the included
unit, init, or service files.
These service initialization files have been tested on supported distributions,
but they should work on other systems as well.

All steps beyond unpacking the archive can be handled by the shell script
found at `bin/install.sh` in the hierarchy of SFTPPlus files.


Unpacking the archive
^^^^^^^^^^^^^^^^^^^^^

After downloading the compressed archive, you can extract its files using
the following command::

    tar xfz sftpplus-os-arch-version.tar.gz

To install SFTPPlus, move (or copy/link) the unpacked directory to your
preferred installation path, for example: ``/opt/sftpplus``.

..  note::
    If `/opt/sftpplus` already exists from a previous cycle of
    installation and uninstallation, make sure you don't put the files
    into `/opt/sftpplus/sftpplus-os-arch-version` when issuing::

        mv sftpplus-os-arch-version /opt/sftpplus

SFTPPlus may be installed in any location on the local file system.
In this documentation page we assume that SFTPPlus is unpacked in the
``/opt/sftpplus`` directory.
Do not use spaces or special characters in the SFTPPlus installation path.


Automated installation from unpacked archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To facilitate installing SFTPPlus, after unpacking it you can use
the shell script found at `bin/install.sh` in the hierarchy of SFTPPlus files.
For example, as root or using `sudo`::

    /opt/sftpplus/bin/install.sh

The `install.sh` script will guide you through all the necessary steps.

A successful installation also configures SFTPPlus to run at boot.
Use the usual `systemd` commands to manage its service. For example::

    systemctl status sftpplus-mft

See the section on starting and stopping SFTPPlus at the end of this page
for more details on systemd integration.
Otherwise, only go further down this page for manual installation.

If your Linux distribution doesn't use systemd, check
the :doc:`advanced Linux installation page</installation/linux-advanced>`.


Manual installation from unpacked archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install SFTPPlus manually, you have to perform step-by-step
all the operations automatically done through the shell script installers,
starting with initializing the configuration.

When installing SFTPPlus on a machine for the first time, you need to
generate the initial configuration file and machine-specific SSH keys.
A self-signed SSL certificate will also be generated to help with the
initial FTPS and HTTPS testing.

To initialize a fresh SFTPPlus installation, execute the following command
(where ``ADMIN`` should be replaced with your favourite administrative username
and ``PASS`` with a password to be used for the SFTPPlus administrative user)::

    cd /opt/sftpplus
    ./bin/admin-commands.sh initialize --init-admin ADMIN --init-password PASS

Default configuration allows external connections to the management web page.
Therefore, use a secure password to protect the management web page.

..  note::
    If you don't want to allow external connections to the `Web Manager`
    web-based console, append the `--local-admin-access` command line argument
    to the initialization command above::

        ./bin/admin-commands.sh initialize \
            --local-admin-access \
            --init-admin ADMIN \
            --init-password PASS

The initialization step is not required when upgrading SFTPPlus.
It will **not** overwrite the configuration file, SSH keys, and SSL
keys and certificates, if existing.
In the case that you want to generate a new configuration,
manually remove the existing files first.

After initializing the configuration, you need to configure
the operating system user and group to be used by SFTPPlus.
For improved security, SFTPPlus is started by default under a regular account.
This requires a dedicated operating system account to be created.

In the following examples, we use the default configuration value of
``sftpplus`` for the name of the user to run SFTPPlus.

To create an ``sftpplus`` group and user::

    groupadd sftpplus
    useradd -g sftpplus -c "SFTPPlus" -s /bin/sh -d /opt/sftpplus -M sftpplus

..  note::
    On Alpine Linux, these tools might be missing, for more instructions check
    the :doc:`advanced Linux installation page</installation/linux-advanced>`.

You need to adjust the ownership of the files to match the newly created
OS user::

    cd /opt && chown -R root:root sftpplus
    cd /opt/sftpplus && chown -R sftpplus:sftpplus configuration log run


After configuring the system user and group for SFTPPlus, you need
to configure the integration with the init system configuration.
On Linux, SFTPPlus' process is managed by the init system bundled with the
distribution: systemd, OpenRC, SysV init, etc.
This page is dedicated to systemd-based distributions such as Red Hat
Enterprise Linux, Ubuntu Server, and Amazon Linux.
Instructions for distributions not using systemd are available in our
:doc:`advanced Linux installation page</installation/linux-advanced>`.

To configure your operating system to automatically start SFTPPlus on boot,
you can use the systemd unit file provided with SFTPPlus.
Customize the `WorkingDirectory`, `ExecStart`, and `PIDFile` paths
in accordance to your SFTPPlus installation.
By default, the ``sftpplus`` user is set for `User` and `Group` in the systemd
unit file, as SFTPPlus runs under a non-root account at all times.
This user must be created as detailed in the previous section. You can also
replace it with another username, as long as it's created appropriately.

Edit this file with your favourite editor, e.g. ``vi``::

    cd /opt/sftpplus
    vi bin/sftpplus-mft.service

When done, copy it to your systemd's `system` sub-directory::

    cd /opt/sftpplus
    cp bin/sftpplus-mft.service /etc/systemd/system/


After configuring the systemd integration, enable launching SFTPPlus on boot::

    systemctl enable sftpplus-mft

Listening on privileged ports also requires a bit of manual configuration.
By default, only the OS root account is allowed to bind ports below 1024.
One generic solution is to set up SFTPPlus to listen on a port above 1024,
then set up port-forwarding in your firewall configuration.

Another method is to grant permissions to listen on privileged ports using
the Linux capabilities system. The relevant capability in this case is
`cap_net_bind_service`, which controls port-listening permissions.
Linux capabilities are associated to a process. A dedicated command-line tool
named `setcap` is required to configure capabilities for the associated binary.

To allow SFTPPlus to listen on ports below 1024, the configuring command should
look similar to the following example (adjust installation path if needed)::

    $ sudo setcap 'cap_net_bind_service=+ep' /opt/sftpplus/bin/python

You can then start SFTPPlus as a non-root user and it will still be capable to
listen on ports below 1024.
For more details, see `man 7 capabilities` on your Linux distribution.

..  note::
    On some Linux distributions, you might need to install an extra package
    to have `setcap` available, such as `libcap` or `libcap2-bin`.


Starting and stopping SFTPPlus
------------------------------

In order to start / stop / restart SFTPPlus, or to check its status,
you may use::

    systemctl start sftpplus-mft
    systemctl stop sftpplus-mft

The generic command is::

    systemctl COMMAND sftpplus-mft

The following COMMANDs are available:

    * `start`
    * `stop`
    * `restart`
    * `try-restart`
    * `status`
    * `is-active`
    * `is-failed`
    * `show`
    * `list-dependencies`

..  include:: first-steps.include
