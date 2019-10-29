Linux and macOS Installation
============================

..  contents:: :local:


Overview
--------

For Unix-like OS'es such as Linux and macOS,
SFTPPlus is distributed as a gzipped TAR archive.
Installing SFTPPlus on these operating systems consists of
unpacking the archive, initializing the configuration and generating the
SSH keys and the SSL certificate which will be used by the product.

The included default configuration requires the creation of a system
account, named `sftpplus`, under which the SFTPPlus process is executed.
Optionally, you may choose to run SFTPPlus as `root`,
especially if you want it to authenticate operating system users.

In order to have SFTPPlus started at boot time, you may use one of the included
init, unit, service or plist files.
The service initialization script has been tested on
all supported operating systems, but it should work on other systems as well.


Unpacking the archive
---------------------

After downloading the compressed archive, you can extract the files using
the following command::

    gunzip -dc sftpplus-os-arch-version.tar.gz | tar -xf -

..  note::
    The tar archive has been created using `pax`, and should be extractable
    by the GNU `tar` command or its alternatives.

To install SFTPPlus, move (or copy/link) the unpacked directory to your
preferred installation path, for example: ``/opt/sftpplus`` or,
if you are using macOS, ``/Library/sftpplus``.

..  note::
    SFTPPlus may be installed in any location on the local file system.
    For this documentation, we will assume that on Linux systems
    SFTPPlus is unpacked in the ``/opt/sftpplus`` directory
    (we will discuss the INSTALL_ROOT more later).

..  note::
    For macOS systems we will assume that SFTPPlus is unpacked in the
    ``/Library/sftpplus`` directory.
    In the following examples please
    replace ``/opt/sftpplus/`` with ``/Library/sftpplus``.


Initializing the configuration
------------------------------

When installing SFTPPlus on a machine for the first time, you need to
generate the initial configuration file and a machine-specific SSH key.
A self-signed SSL certificate will also be generated to help with the
initial FTPS and HTTPS testing.

To initialize SFTPPlus, execute the following commands::

    cd /opt/sftpplus
    ./bin/admin-commands.sh initialize \
        --init-admin ftadmin \
        --init-password YOUR-ADMIN-PASSWORD

Default configuration allows external connections to the management web page.
Therefore, use a secure password to protect the management web page.
If you don't want to allow external connections to the `Local Manager`
web-based console, use the `--local-admin-access` command line argument::

    cd /opt/sftpplus
    ./bin/admin-commands.sh initialize \
        --init-admin ftadmin \
        --init-password YOUR-ADMIN-PASSWORD
        --local-admin-access

..  warning::
    The initialization step is not required when upgrading SFTPPlus.
    It will **not** overwrite the configuration file, SSH keys, and SSL
    certificate, if existing.
    In the case that you want to generate a new configuration,
    manually remove the existing files first.


Working with the SFTPPlus process account and group
---------------------------------------------------

On Unix-like systems, SFTPPlus' process runs as a single, self-managed daemon.
It does not depend on inetd (the Internet daemon).

On Linux, SFTPPlus is designed to run as a foreground process executed
under the root account and will drop privileges after it is launched.

On macOS, SFTPPlus' process is managed by `launchd`.

The following are details for configuring the SFTPPlus account and group
for Unix-like systems.


Configuring the process user and group on Linux and macOS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On Unix-like systems, SFTPPlus is able to drop privileges to a regular account.
The default configuration takes advantage of this feature,
thus requiring a dedicated `sftpplus` operating system account to be created.
Creating a dedicated new group and a new user for running SFTPPlus' process
is therefore recommended.

In the following example we will use the default configuration value of
`sftpplus` for the name of the user to run SFTPPlus.

To create an `sftpplus` group and user in Linux
(with the exception of Alpine Linux)::

    groupadd sftpplus
    useradd -g sftpplus -c "SFTPPlus" -s /bin/false -d /dev/null sftpplus

To create an ``sftpplus`` group and user in Alpine Linux::

    addgroup sftpplus
    adduser -G sftpplus -g "SFTPPlus" -s /bin/false -h /dev/null -H -D sftpplus

..  note::
    To run SFTPPlus in Alpine Linux under an unprivileged account at all times
    through the included OpenRC init script,
    avoid creating the user with "/bin/false" as shell and "/dev/null" as home,
    eg.: `adduser -G sftpplus -g "SFTPPlus" -h /opt/sftpplus -H -D sftpplus`

..  note::
    The generic Linux commands should work in Alpine Linux too,
    as long as you have the ``shadow`` package installed.


Configuring the process user and group on macOS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create an `sftpplus` group and a corresponding user on macOS, replace the
value of ``240`` from the following example with a unique ID for your system::

    # Create the group dedicated to the service account.
    dscl . create /Groups/sftpplus
    # Assign an unique ID to the group.
    dscl . create /Groups/sftpplus PrimaryGroupID 240
    # Disable group password.
    dscl . create /Groups/sftpplus Password '*'
    # Create a user for the service account.
    dscl . create /Users/sftpplus
    # Assign a unique ID to the new user.
    dscl . create /Users/sftpplus UniqueID 240
    # Assign this account to the dedicated group.
    dscl . create /Users/sftpplus PrimaryGroupID 240
    # Disable shell access.
    dscl . create /Users/sftpplus UserShell /usr/bin/false
    # Make sure it has a default empty home folder.
    dscl . create /Users/sftpplus NFSHomeDirectory /var/empty
    # Disable password to block any authentication request.
    dscl . create /Users/sftpplus Password '*'
    # Initialize blank password and authentication rules.
    dscl . delete /Users/sftpplus PasswordPolicyOption
    dscl . delete /Users/sftpplus AuthenticationAuthority

..  note::
    On macOS, you can use `dscacheutil -q user` or `dscacheutil -q group` to
    identify the used IDs and pick a unique ID for the system.

..  note::
    The above commands are included into an easy to use script which is
    available as
    `osx_useradd.sh <https://gist.github.com/adiroiban/80c8acc00b8957869f68>`_


Finalizing the .ini configuration file for OS account configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is not required on Windows.

This is only needed if you require to authenticate OS accounts on Linux or
macOS.

To configure SFTPPlus to start as `root`, but to run under the dedicated
application account,
make sure the following option is present in the
`configuration/server.ini` configuration file::

    [server]
    account = sftpplus

..  note::
    Don't forget to adjust the ownership of the files, otherwise some of the
    functionality (logging and saving configuration changes) may not work.
    At the very least, SFTPPlus needs read access to all the files under
    /opt/sftpplus, but in a typical installation it would also require write
    permission to the log/ subdirectory (for logging) and the configuration/
    subdirectory (for saving changes to the running configuration).
    If running at all times under an unprivileged account, write permissions
    to the run/ sub-directory holding the PID file are needed as well.

    A quick and easy way to achieve the above would be:
    `cd /opt/sftpplus && chown -R sftpplus configuration/ log/ run/`


Running SFTPPlus daemon/service under an unprivileged account
-------------------------------------------------------------

Like any other process on a Unix-like OS, the main process of SFTPPlus runs
under an operating-system account.

SFTPPlus can start under the root OS account, and then drop privileges
in order to mainly operate under a regular OS account.

As in most deployments such a regular account is dedicated to running SFTPPlus,
our documentation refers to this regular OS account as the *service account*.

We recommend to always run SFTPPlus under such an unprivileged OS account, even
when the SFTPPlus process is launched as root.

In this regard, the SFTPPlus process has 2 main modes of operation,
each one with its own advantages and disadvantages.


1. Start as root and mostly operate as unprivileged account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the default mode, in which the init script or unit file is configured
to start SFTPPlus as root, while the configuration file defines an unprivileged
OS account (by default, ``sftpplus``) for the process' operation.

If you want the SFTPPlus process launched as root, but operating under the
``sftpplus`` account, make sure the configuration file reads as follows::

    [server]
    account = sftpplus

Advantages:

* Binding to ports below 1024 works out of the box.
* The OS accounts can be used for file transfer services.

Disadvantages:

* Even though most of the time SFTPPlus will operate under the unprivileged
  account, for requests to authenticate an OS account SFTPPlus will briefly
  switch to running as root in order to perform the OS authentication.
  If there is a security bug in SFTPPlus, and that bug is exploited during
  the brief amount of time SFTPPlus runs as root, an attacker can theoretically
  gain privileged access to OS resources.


2. Start as unprivileged account and always operate under it
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want the SFTPPlus process launched and always operating as an
unprivileged user, you have to edit the init script or unit file to start
SFTPPlus under that user, and then make sure the configuration file reads
as follows::

    [server]
    account = Disabled

SFTPPlus will then operate under the same OS account that is used to launch it.

Advantages:

* Operating under the principle of least privilege.
* Even if there are security bugs in SFTPPlus, a successful exploit will
  not have unprivileged access to OS resources.

Disadvantages:

* Binding to ports below 1024 requires extra configuration steps. If at all
  possible, as on some Unix-like systems you can only bind those ports as root.
  You can still configure the file transfer services to listen on any ports
  above 1024.
* The OS accounts cannot be used for file transfer services.

..  note::
    You can also start SFTPPlus under the privileged root account in
    the init script or unit file, and keep running the SFTPPlus process as root
    using ``account = Disabled`` in the server's configuration file.
    For security reasons, we don't recommend this mode of operation.


Starting and stopping the server
--------------------------------

For your convenience, the SFTPPlus installation comes with a script which can
be integrated into the boot or startup process of your operating system,
as discussed in the next section.

All the scripts for every operating system are using a common command for
starting and stopping the SFTPPlus product, as described here.

To start the server, use the following command::

    ./bin/admin-commands.sh start

By default it will start using the configuration file located at
`configuration/server.ini` and will store the process ID inside the
`run/server.pid` file.

To stop the server, send the kill signal to the process ID stored inside the
`run/server.pid` file.

To store the process ID in a different file, start the server using
`-p` or `--pid` arguments::

    ./bin/admin-commands.sh start --pid=/path/to/PID_FILE

If you want to launch the server using a configuration file from a
specific location, use the `-c` or `--config=` argument::

    ./bin/admin-commands.sh start --config=/path/to/CONFIGURATION_FILE


Init system configuration for Linux
-----------------------------------

For Unix-like systems, the following script is provided as a starting
point for creating custom initialization scripts for various service managers
(SysVinit, Upstart, OpenRC, systemd with SysV compatibility, etc.)::

    ./bin/sftpplus-mft.sysv.sh

You should copy the sample script to the standard location used by the
initialization system of your operating system, for example::

    /etc/init.d/sftpplus-mft

Make sure the script is executable, and amend the `INSTALL_ROOT` variable found
inside the script to the installation path of your SFTPPlus instance.
In the case that SFTPPlus is installed at `/opt/sftpplus`, the
script's relevant section should look as follows::

    Replace INSTALL_ROOT with your installation path.
    INSTALL_ROOT="/opt/sftpplus"

On systemd-based distributions (especially on those without the SysV
compatibility bits, such as Arch Linux) you can use the following unit file::

    ./bin/sftpplus-mft.service

..  note::
    You should copy it to `/etc/systemd/system/`, customizing the
    `WorkingDirectory`, `ExecStart` and `PIDFile` paths
    based on your SFTPPlus installation.
    You can run SFTPPlus under a non-root account through systemd by
    changing `User` and `Group` in the systemd unit file.

On Alpine Linux, you may use the included OpenRC service file::

   ./bin/sftpplus-mft.openrc.sh

..  note::
    You should copy it to `/etc/init.d/sftpplus-mft`, customizing the
    `INSTALL_ROOT` variable, if necessary for your SFTPPlus installation.

Depending on your operating system, you will have to either manually create
symbolic links to the initialization script from the `rcN.d` directories (where
`N` is the runlevel) or run a specific tool that will automatically do that.

Examples (run under the ``root`` account):

RHEL, Amazon Linux, and SUSE::

    chkconfig --add sftpplus-mft

Debian and Ubuntu::

    update-rc.d sftpplus-mft defaults

Linux systems with systemd (including RHEL 7, Ubuntu 18.04, Debian 9,
Amazon Linux 2, and SLES 12)::

    systemctl enable sftpplus-mft

Alpine Linux::

    rc-update add sftpplus-mft


Starting and stopping SFTPPlus on Linux
---------------------------------------

On Linux systems, in order to start / stop / restart SFTPPlus, or
to check its status, you can either call the script directly as::

    /etc/init.d/sftpplus-mft COMMAND

Or through the relevant service management tool provided by the
operating system::

    service sftpplus-mft COMMAND

For Linux systems with systemd you may use::

    systemctl COMMAND sftpplus-mft

For Alpine Linux you may use::

    rc-service sftpplus-mft COMMAND

The following COMMANDs are available:

    * `start`
    * `stop`
    * `restart`
    * `status`
    * `force-reload` (only for the SysV init script)
    * `force-stop` (only for the SysV init script)
    * `zap` (only for the OpenRC service file)
    * `describe` (only for the OpenRC service file)

..  note::
    The `force-reload` action is an alias for `restart`, in order to comply
    with the Linux Standard Base.

..  note::
    When running the legacy SFTPPlus WebAdmin on the same machine,
    SFTPPlus should be started after Apache, as it will check the
    availability of the configured legacy SFTPPlus WebAdmin.


Init system configuration for Apple macOS
-----------------------------------------

For macOS systems, the following `launchd` job definition is provided
with the SFTPPlus distribution.
The job definition file is formatted as XML, and it is called a property list
file or 'plist'::

    bin/Library_LaunchDaemons_sftpplus.plist

The sample job definition file assumes that SFTPPlus is installed in
the `/Library/sftpplus` directory.
Depending on where the job definition is stored, it will be treated as a
daemon or an agent.
In order to have SFTPPlus act as a global daemon, launching it each
time the macOS system starts, you need to copy the plist file into the following
location: `/Library/LaunchDaemons/sftpplus.plist`

After the file is copied, you need to instruct `launchd` to load/read the new
job definition file using the command::

    launchctl load /Library/LaunchDaemons/sftpplus.plist

..  note::
    At boot time, the `launchd` process will scan and automatically load job
    definitions found in the ``/Library/LaunchDaemons`` directory.

To stop SFTPPlus, use the following command::

    launchctl unload /Library/LaunchDaemons/sftpplus.plist

..  note::
    In the case that there are problems starting the server, you can check
    the log files at ``/var/log/system.log`` and
    ``/var/log/sftpplus-launchd.log``.

You can also launch SFTPPlus in debug mode using::

    ./bin/admin-commands.sh debug

..  note::
    You can read more about `launchd` on the `official documentation page
    <https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html>`_


SFTPPlus directory hierarchy and permissions
--------------------------------------------

Once unpacked, the SFTPPlus installation should have the following
hierarchical directory structure on disk.

This list also describes the permissions required for the service account.

* `bin/` - `read-only`
  Contains SFTPPlus administration commands and the init script.
  Only available on Unix-like systems.

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

.. include:: first-steps.include
