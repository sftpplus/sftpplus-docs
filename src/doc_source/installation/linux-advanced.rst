Advanced Linux installation
===========================

..  contents:: :local:


Overview
--------

Make sure to follow the instructions from the :doc:`Linux installation page
</installation/linux>` before diving in the following sections.

This page adds specific installation instructions for Linux distributions not
using systemd. Most of the information from the :doc:`Linux installation page
</installation/linux>` is still applicable and required.

This page also documents advanced installation setups for all supported
Linux distributions.


Running the service under Security-Enhanced Linux
-------------------------------------------------

Some distributions such as Red Hat Enterprise Linux come with Security-Enhanced
enabled and enforced by default. SELinux doesn't allow a system service to
run a script from a user's home.

To work around this limitation, use a home directory under ``/var/lib``
for the dedicated SFTPPlus user, for example::

    mkdir /var/lib/sftpplus
    groupadd sftpplus
    useradd -g sftpplus -c "SFTPPlus" s /bin/sh -d /var/lib/sftpplus -M sftpplus


Init system configuration for Linux distributions not using systemd
-------------------------------------------------------------------

For SysV-based distributions (or SysV-compatible ones), such as
Amazon Linux AMI 2018.03, RHEL 5 and 6, SLES 11, Ubuntu Server 14.04,
Debian Linux 7, etc., a sample init script is provided.

Make sure the script is executable, then amend the `INSTALL_ROOT` variable
to the installation path of your SFTPPlus instance.

Copy the modified script to the standard location used by the
initialization system of your distribution::

    cd /opt/sftpplus
    vi bin/sftpplus-mft.sysv.sh
    chmod +x bin/sftpplus-mft.sysv.sh
    cp bin/sftpplus-mft.sysv.sh /etc/init.d/sftpplus-mft

Then you can call the script directly as::

    /etc/init.d/sftpplus-mft COMMAND

On Alpine Linux, you may use the included OpenRC service file,
customizing the `INSTALL_ROOT` variable if needed for your
installation::

    cd /opt/sftpplus
    vi bin/sftpplus-mft.openrc.sh
    chmod +x bin/sftpplus-mft.openrc.sh
    cp bin/sftpplus-mft.openrc.sh /etc/init.d/sftpplus-mft

Then you may use::

    rc-service sftpplus-mft COMMAND

The following COMMANDs are available:

    * `start`
    * `stop`
    * `restart`
    * `status`
    * `debug` (start without detaching from current console)
    * `force-stop` (only for the SysV init script)
    * `zap` (only for the OpenRC service file)
    * `describe` (only for the OpenRC service file)

Starting SFTPPlus automatically on boot can be set through a specific tool.
The following examples (run under the ``root`` account)
show how to do that on supported distributions.

On Amazon Linux AMI 2018.03, RHEL 5 and 6, SLES 11::

    chkconfig --add sftpplus-mft

On Alpine Linux::

    rc-update add sftpplus-mft


Configuring the process user and group on Alpine Linux
------------------------------------------------------

The generic Linux commands should work on Alpine Linux too,
as long as you have the ``shadow`` package installed.

Alternatively, to create an ``sftpplus`` group and user on Alpine Linux
with the default-installed tools, use::

    addgroup sftpplus
    adduser -G sftpplus -g "SFTPPlus" -s /bin/sh -h /opt/sftpplus -H -D sftpplus


SFTPPlus directory hierarchy and permissions
--------------------------------------------

Once unpacked, the SFTPPlus installation should have the following
hierarchical directory structure on disk.

This list also describes the permissions required for the service account.

* `bin/` - `read-only`
  Contains SFTPPlus administration commands and the init-specific files.

* `configuration/` - `read-only`
  Stores all data related to SFTPPlus configuration.

* `configuration/server.ini` - `read-and-write`
  Stores the main configuration.

* `doc/` - `read-only`
  Contains documentation and release notes for SFTPPlus.

* `extension/` - `read-only`
  Contains custom extensions implemented using the SFTPPlus API.

* `include/` - `read-only`
  This directory is for developers interested in extending the
  functionality of SFTPPlus. May be missing in some releases.

* `lib/` - `read-only`
  This directory is for internal use.

* `log/` - `read`, `write`, `create file` and `delete file`
  Stores SFTPPlus log messages.
  SFTPPlus will write log entries into the log files, by default.
  When log rotation is enabled, it will also create new rotated files and
  delete old rotated files.

* `run/` - `read`, `write`, `create file` and `delete file`
  Stores various SFTPPlus runtime information.


Customizing the process of starting SFTPPlus
--------------------------------------------

For your convenience, the SFTPPlus installation comes with files to
be integrated into the startup process of supported distributions,
as discussed in the relevant sections of the Linux installation pages.

All these integrated init and unit files are using common commands for
starting and stopping the SFTPPlus product, as described below.

To start the server, use the following command::

    cd /opt/sftpplus
    ./bin/admin-commands.sh start

By default it will start using the configuration file located at
`configuration/server.ini` and will store the process ID in the
`run/server.pid` file.

To stop the server, send the kill signal to the process ID stored in the
`run/server.pid` file.

To store the process ID in a different file, start the server using
`-p` or `--pid` arguments::

    cd /opt/sftpplus
    ./bin/admin-commands.sh start --pid=/path/to/PID_FILE

If you want to launch the server using a configuration file from a
specific location, use the `-c` or `--config=` argument::

    cd /opt/sftpplus
    ./bin/admin-commands.sh start --config=/path/to/CONFIGURATION_FILE


Running SFTPPlus daemon/service under an unprivileged account
-------------------------------------------------------------

Like any other OS process, the main process of SFTPPlus runs
under an operating-system account.

SFTPPlus can start under the root OS account, and then drop privileges
in order to mainly operate under a regular OS account.

As in most deployments such a regular account is dedicated to running SFTPPlus,
our documentation refers to this regular OS account as the *service account*.

We recommend to always run SFTPPlus under such an unprivileged OS account, even
when the SFTPPlus process is launched as root.

In this regard, the SFTPPlus process has 2 main modes of operation,
each one with its own advantages and disadvantages.


Start as unprivileged account and always operate under it
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the default mode on Linux and macOS.

The included unit, init, service, plist files are configured
to start SFTPPlus as an unprivileged user.

Also make sure the configuration file reads as follows
(account value is empty)::

    [server]
    account =

SFTPPlus will then operate under the same OS account that is used to launch it.

Advantages:

* Operating under the principle of least privilege.
* Even if there are security bugs in SFTPPlus, a successful exploit will
  not have unprivileged access to OS resources.
* On systemd-based Linux distributions and macOS, the unprivileged user
  can be assigned non-valid shell and home values such as
  ``/bin/false`` and ``/var/empty``, respectively.

Disadvantages:

* Using ports below 1024 requires OS-specific configuration.
* OS accounts cannot be used for file transfer services.
* On Alpine Linux and Linux distributions using the SysV init file such as
  Amazon Linux AMI 2018.03, the unprivileged user needs a valid shell and home.


Start as root and mostly operate as unprivileged account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is only needed if you require to authenticate OS accounts in SFTPPlus.

To configure SFTPPlus to start as ``root``, but to run under the dedicated
application account, you have to edit the default-included unit, init, or
service file to use ``root`` instead of ``sftpplus`` for launching SFTPPlus.

Then make sure the following option is present in the
`configuration/server.ini` configuration file::

    [server]
    account = sftpplus

Advantages:

* Binding to ports below 1024 works out of the box.
* OS accounts can be used for file transfer services.
* On Alpine Linux and Linux distributions using the SysV init file,
  for example Amazon Linux AMI 2018.03, the unprivileged user
  can be assigned non-valid shell and home values such as
  ``/bin/false`` and ``/var/empty``, respectively.

Disadvantages:

* Even though most of the time SFTPPlus will operate under the unprivileged
  account, for requests to authenticate an OS account SFTPPlus will briefly
  switch to running as root in order to perform the OS authentication.
  If there is a security bug in SFTPPlus, and that bug is exploited during
  the brief amount of time SFTPPlus runs as root, an attacker can theoretically
  gain privileged access to OS resources.

..  note::
    You can also start SFTPPlus under the privileged root account
    and keep running the SFTPPlus process as root
    using ``account =`` in the server's configuration file.
    For security reasons, we don't recommend this mode of operation.


Running multiple concurrent instances on the same machine / VM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can run multiple independent SFTPPlus instances on the same machine or VM
to achieve one of the following requirements:

* have separate testing and production systems
* better CPU usage and high availability on multi CPU / multi disk systems
* create a pre-production system which is hosted by the same VM as the
  production to allow easy rollback to older version

On systemd (modern Linux) and OpenRC init system this can be achieved
by creating multiple service file with different names
and setting specific configuration files per SFTPPlus instance.

Each instance must be configured with specific paths for log and cache files.
For example, when using a production instance and a testing one,
`log/server-production.log` and `log/server-testing.log`
for the log handler's file paths, and
`configuration/cache-production.db3` and `configuration/cache-testing.db3`
for the embedded database resource paths.

In addition, different instances must use different ports and/or IPs.
For example, 10022 for the first instance's SFTP port and 20022 for the
second one, if using the same IP.

For SysV-based systems, we provide a simplified init script for running
concurrent instances: `bin/sftpplus-mft.sysv.instances.sh`.
Create copies as needed in your `/etc/init.d/` sub-directory,
then edit the `$INSTANCE_ID` variable for each instance.
The init script assumes each instance is configured through a file named
`configuration/server-INSTANCE_ID.ini`, where INSTANCE_ID should match
the value set in the init script.

When running different versions of SFTPPlus concurrently on the same machine,
each instance has a dedicated root directory, therefore the ``INSTALL_ROOT``
variable from the service/init files must be updated accordingly.
