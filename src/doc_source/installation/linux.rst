Linux Installation
==================

..  contents:: :local:


Overview
--------

For Linux systems, SFTPPlus is distributed as a gzipped TAR archive.
Installing SFTPPlus consists of
unpacking the archive, initializing the configuration, and generating the
SSH keys and the SSL key / certificate pair to be used by the product.

The included default configuration requires the creation of a system
account, named `sftpplus`, under which the SFTPPlus process is executed.

Optionally, you may choose to start SFTPPlus as `root`,
especially if you want it to authenticate operating system users.
The `sftpplus` user is still required in order to drop privileges
for all other operations.

To have SFTPPlus started at boot, you can use one of the included
unit, init, or service files.
These service initialization files have been tested on
all supported distributions,
but they should work on other systems as well.

All steps beyond unpacking the archive can be handled by the shell script
found at ``./bin/install.sh`` in the hierarchy of SFTPPlus files.


Unpacking the archive
---------------------

After downloading the compressed archive, you can extract its files using
the following command::

    tar xfz sftpplus-os-arch-version.tar.gz

To install SFTPPlus, move (or copy/link) the unpacked directory to your
preferred installation path, for example: ``/opt/sftpplus``.

SFTPPlus may be installed in any location on the local file system.
In this documentation page we assume that SFTPPlus is unpacked in the
``/opt/sftpplus`` directory (we discuss INSTALL_ROOT more later).
Avoid using spaces or special characters in the SFTPPlus installation path.


Shell script installer
----------------------

The easiest way to install SFTPPlus is to execute the shell script
found at ``./bin/install.sh`` in the hierarchy of SFTPPlus files,
for example::

    /opt/sftpplus/bin/install.sh

The ``./bin/install.sh`` script will guide you through all the necessary steps.
Only go further down this page for manual installation or debugging.


Initializing the configuration
------------------------------

When installing SFTPPlus on a machine for the first time, you need to
generate the initial configuration file and machine-specific SSH keys.
A self-signed SSL certificate will also be generated to help with the
initial FTPS and HTTPS testing.

To initialize a fresh SFTPPlus installation, execute the following command
(where `ADMIN` should be replaced with your favourite administrative username
and `PASS` with a password to be used for the SFTPPlus ADMIN user)::

    cd /opt/sftpplus
    ./bin/admin-commands.sh initialize --init-admin ADMIN --init-password PASS

Default configuration allows external connections to the management web page.
Therefore, use a secure password to protect the management web page.

..  note::
    If you don't want to allow external connections to the `Local Manager`
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


Configuring the SFTPPlus process user and group
-----------------------------------------------

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


Init system configuration with systemd
--------------------------------------

On Linux, SFTPPlus' process is managed by the init system bundled with the
distribution: systemd, OpenRC, SysV init, etc.

This page is dedicated to systemd-based distributions such as Red Hat
Enterprise Linux version 7 or later, Ubuntu Server 16.04 LTS or later,
Amazon Linux version 2 or later, etc.

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

Edit this file with your favourite editor, e.g. `vi`::

    cd /opt/sftpplus
    vi bin/sftpplus-mft.service

When done, copy it to your systemd's `system` sub-directory::

    cd /opt/sftpplus
    cp bin/sftpplus-mft.service /etc/systemd/system/


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


Running SFTPPlus on boot
------------------------

To enable launching SFTPPlus on startup::

    systemctl enable sftpplus-mft


Listening on privileged ports
-----------------------------

By default, only the OS ``root`` account is allowed to bind ports below 1024.

One generic solution is to set up SFTPPlus to listen on a port above 1024,
then set up port-forwarding in your firewall configuration.

Another method is to grant permissions to listen on privileged ports using
the Linux `capabilities` system. The relevant capability in this case is
`cap_net_bind_service`, which controls port-listening permissions.

Linux capabilities are associated to a process. A dedicated command-line tool
named `setcap` is required to configure capabilities for the associated binary.

To allow the SFTPPlus process to listen on ports below 1024, the command
will look similar to the following example::

    $ sudo setcap 'cap_net_bind_service=+ep' SFTPPLUS_INSTALL_PATH/bin/python

You can then start SFTPPlus as a non-root user and listen on ports below 1024.

For more details, see `man 7 capabilities` on your Linux distribution.

..  note::
    On some Linux distributions, you might need to install an extra package
    to have `setcap` available, such as `libcap` or `libcap2-bin`.

..  include:: first-steps.include
