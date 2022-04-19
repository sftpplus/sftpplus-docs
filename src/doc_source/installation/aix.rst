AIX Installation
================

..  contents:: :local:


Overview
--------

For AIX systems, SFTPPlus is distributed as a gzipped TAR archive.
Installing SFTPPlus consists of
unpacking the archive, initializing the configuration, and generating the
SSH keys and the SSL key and certificate to be used by the product.

The included default configuration requires the creation of a system
account, named `sftpplus`, under which the SFTPPlus process is executed.

Optionally, you may choose to start SFTPPlus as `root`,
but the `sftpplus` user is still required in order to drop privileges
after starting up.

To have SFTPPlus launched at boot, you may use the included SysV init script.


Unpacking the archive
---------------------

After downloading the compressed archive, you can extract its files using
the following command::

    gunzip -cd xfz sftpplus-os-arch-version.tar.gz | tar -xf -

To install SFTPPlus, move (or copy/link) the unpacked directory to your
preferred installation path, for example: ``/opt/sftpplus``.

SFTPPlus may be installed in any location on the local file system.
In this documentation page we assume that SFTPPlus is unpacked in the
``/opt/sftpplus`` directory (we discuss INSTALL_ROOT more later).


Initializing the configuration
------------------------------

When installing SFTPPlus on a machine for the first time, you need to
generate the initial configuration file and machine-specific SSH keys.
A self-signed SSL certificate will also be generated to help with the
initial FTPS and HTTPS testing.

To initialize a fresh SFTPPlus installation, execute the following command
(where $ADMIN should be replaced with your favourite administrative username
and $PASS with a password to be used for the SFTPPlus $ADMIN user)::

    cd /opt/sftpplus
    ./bin/admin-commands.sh initialize --init-admin $ADMIN --init-password $PASS

Default configuration allows external connections to the management web page.
Therefore, use a secure password to protect the management web page.

..  note::
    If you don't want to allow external connections to the `Local Manager`
    web-based console, append the `--local-admin-access` command line argument
    to the initialization command above::

        ./bin/admin-commands.sh initialize \
            --local-admin-access \
            --init-admin $ADMIN \
            --init-password $PASS

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

To create an ``sftpplus`` group and user on AIX::

    mkgroup sftpplus
    mkuser sftpplus
    usermod -g sftpplus -d /opt/sftpplus -s /bin/sh -c "SFTPPlus" sftpplus

You need to adjust the ownership of the files to match the newly created
OS user::

    cd /opt && chown -R root:adm sftpplus
    cd /opt/sftpplus && chown -R sftpplus:sftpplus configuration log run

At the very least, SFTPPlus needs read access to all the files under
`/opt/sftpplus`, but in a typical installation it also requires write
permission to the `log/` subdirectory (for logging) and the `configuration/`
subdirectory (for saving changes to the running configuration).
If running at all times under an unprivileged account, write permissions
to the `run/` sub-directory holding the PID file are needed as well.


Init system configuration for AIX
---------------------------------

For SysV-compatible operating systems such as AIX,
a sample init script is provided.

Make sure the script is executable, then amend the `INSTALL_ROOT` variable
to the installation path of your SFTPPlus instance.

Copy the modified script to the standard location used by the
initialization system of your distribution::

    cd /opt/sftpplus
    vi bin/sftpplus-mft.sysv.sh
    chmod +x bin/sftpplus-mft.sysv.sh
    cp bin/sftpplus-mft.sysv.sh /etc/rc.d/init.d/sftpplus-mft

Then you can call the script directly as::

    /etc/rc.d/init.d/sftpplus-mft COMMAND

The following COMMANDs are available:

    * `start`
    * `stop`
    * `restart`
    * `status`
    * `debug` (start without detaching from current console)
    * `force-stop`

To start SFTPPlus automatically on boot::

    ln -s /etc/rc.d/init.d/sftpplus-mft /etc/rc.d/rc2.d/S99sftpplus-mft


Listening on privileged ports
-----------------------------

When running SFTPPlus as a regular user, it's not possible to bind
privileged ports in the range 0-1024.

One generic method which works on any Unix-like system is to set up
SFTPPlus to listen only on ports above 1024, then set up port-forwarding
in your firewall configuration.

..  include:: first-steps.include
