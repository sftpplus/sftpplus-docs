macOS Installation
==================

..  contents:: :local:


Overview
--------

For macOS systems, SFTPPlus is distributed as a gzipped TAR archive.
Installing SFTPPlus consists of
unpacking the archive, initializing the configuration, and generating the
SSH keys and the SSL key and certificate to be used by the product.

The included default configuration requires the creation of a system account,
usually named `sftpplus`, under which the SFTPPlus process is executed.
This is a special type of OS user also known as a service account.

Optionally, you may choose to start SFTPPlus as `root`,
but the service account is still required in order to drop privileges
after starting up.

This dedicated OS user should not be used in any other way,
doesn't require a password to be set for it,
and should not be available through SFTPPlus services
even if authenticating operating system users is enabled.

To have SFTPPlus launched at boot, you may use the included plist file.

All steps beyond unpacking the archive can be handled by the shell script
found at ``./bin/install.sh`` in the hierarchy of SFTPPlus files.


Unpacking the archive
---------------------

After downloading the compressed archive, you can extract its files using
the following command::

    tar xfz sftpplus-os-arch-version.tar.gz

To install SFTPPlus, move (or copy/link) the unpacked directory to your
preferred installation path, for example: ``/Library/sftpplus``.

SFTPPlus may be installed in any location on the local file system.
In this documentation page we assume that SFTPPlus is unpacked in the
``/Library/sftpplus`` directory (we discuss INSTALL_ROOT more later).
Avoid using spaces or special characters in the SFTPPlus installation path.


Shell script installer
----------------------

The easiest way to install SFTPPlus is to execute the shell script
found at ``./bin/install.sh`` in the hierarchy of SFTPPlus files,
for example::

    sudo /Library/sftpplus/bin/install.sh

The ``install.sh`` script will guide you through all the necessary steps.

After a successful installation using the shell script, jump to
`Listening on privileged ports`_
to learn how to enable SFTPPlus to listen on privileged ports.
This would be needed if SFTPPlus is not started with superuser privileges,
which would mean it cannot bind ports below 1024.


Initializing the configuration
------------------------------

When installing SFTPPlus on a machine for the first time, you need to
generate the initial configuration file and machine-specific SSH keys.
A self-signed SSL certificate will also be generated to help with the
initial FTPS and HTTPS testing.

To initialize a fresh SFTPPlus installation, execute the following command
(where $ADMIN should be replaced with your favourite administrative username
and $PASS with a password to be used for the SFTPPlus $ADMIN user)::

    cd /Library/sftpplus
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

On macOS, SFTPPlus' process is managed by `launchd`.

The following are details for configuring the SFTPPlus account and group
for macOS systems.


Configuring the process user and group on macOS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On macOS systems, SFTPPlus is able to drop privileges to a regular account
even when launched as root.
The default configuration takes this a step further,
always running under a regular account,
thus requiring a dedicated `sftpplus` operating system account to be created.
Creating a dedicated new group and a new user for running SFTPPlus' process
is therefore strongly recommended.

In the following examples we will use the default configuration value of
`sftpplus` for the name of the user to run SFTPPlus.


Configuring the process user and group on macOS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create an `sftpplus` group and a corresponding user on macOS,
use the following commands.

You can replace the value of ``299`` from the below example commands with
a unique ID for your system.
On macOS, you can use `dscacheutil -q user` or `dscacheutil -q group` to
identify the used IDs and pick a unique ID.

The below commands are included into an easy to use script which is
available as
`osx_useradd.sh <https://gist.github.com/adiroiban/80c8acc00b8957869f68>`_::

    # Create the group dedicated to the service account.
    sudo dscl . create /Groups/sftpplus
    # Assign an unique ID to the group.
    sudo dscl . create /Groups/sftpplus PrimaryGroupID 299
    # Disable group password.
    sudo dscl . create /Groups/sftpplus Password '*'
    # Create a user for the service account.
    sudo dscl . create /Users/sftpplus
    # Assign a unique ID to the new user.
    sudo dscl . create /Users/sftpplus UniqueID 299
    # Assign this account to the dedicated group.
    sudo dscl . create /Users/sftpplus PrimaryGroupID 299
    # Disable shell access.
    sudo dscl . create /Users/sftpplus UserShell /usr/bin/false
    # Make sure it has a default empty home folder.
    sudo dscl . create /Users/sftpplus NFSHomeDirectory /var/empty
    # Disable password to block any authentication request.
    sudo dscl . create /Users/sftpplus Password '*'
    # Initialize blank password and authentication rules.
    sudo dscl . delete /Users/sftpplus PasswordPolicyOption
    sudo dscl . delete /Users/sftpplus AuthenticationAuthority

You need to adjust the ownership of the files, otherwise some of the
functionality (logging and saving configuration changes) will not work::

    cd /Library && chown -R root:admin sftpplus
    cd /Library/sftpplus && chown -R sftpplus configuration/ log/ run/

At the very least, SFTPPlus needs read access to all the files under
`/Library/sftpplus`, but in a typical installation it also requires write
permission to the `log/` subdirectory (for logging) and the `configuration/`
subdirectory (for saving changes to the running configuration).
If running at all times under an unprivileged account, write permissions
to the `run/` sub-directory holding the PID file are needed as well.


Init system configuration for macOS
-----------------------------------

The next step is to configure your operating system to automatically
start SFTPPlus on boot.

For macOS systems, you can use the example `launchd` job definition provided
with SFTPPlus.
The job definition file is formatted as XML, and it is called a property list
file or 'plist'.
Edit this file with your favourite editor, e.g. `vi`::

    vi bin/sftpplus-mft.plist

The sample job definition file assumes that SFTPPlus is installed in
the `/Library/sftpplus` directory.
Depending on where the job definition is stored, it will be treated as a
service or an agent.
In order to have SFTPPlus act as a global service, launching each
time the macOS system starts, you need to copy it in the appropriate place::

    sudo cp bin/sftpplus-mft.plist /Library/LaunchDaemons/sftpplus.plist

After the file is copied, you need to instruct `launchd` to load/read the new
job definition file using the command::

    sudo launchctl load /Library/LaunchDaemons/sftpplus.plist

..  note::
    During startup, the `launchd` process will scan and automatically load job
    definitions found in the ``/Library/LaunchDaemons`` directory.

To stop SFTPPlus, use the following command::

    sudo pkill -x sftpplus-service-supervisor

In the case that there are problems starting the server, you can check
the log files at ``/var/log/system.log`` and
``/var/log/sftpplus-launchd.log``.

    You can read more about `launchd` on the `official documentation page
    <https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html>`_


Listening on privileged ports
-----------------------------

When running SFTPPlus as a regular user, it's not possible to bind
privileged ports in the range 0-1024.

One generic method which works on any Unix-like system is to set up
SFTPPlus to listen on a port above 1024, then set up port-forwarding
in your firewall configuration.

For example, to set up port-forwarding using `pf`,
we can use the loopback interface to keep things simple.
However, you should adapt and extend the exemplified firewall rules
to account for your own local configuration:
different network interfaces, IPs, and other network traffic rules.

Step-by-step instructions on how to forward port 122 to 10022::

    Create a pf anchor file for sftpplus in /etc/pf.anchors/sftpplus
    with the following contents:
        rdr pass on lo0 inet proto tcp from any to 127.0.0.1
        port = 122 -> 127.0.0.1 port 10022
        (note the above 2 lines go into only one line, it has been
        split here for better readability)

    Reference anchor in /etc/pf.conf, add:
        rdr-anchor "sftpplus"
        load anchor "sftpplus" from "/etc/pf.anchors/sftpplus"

    Enable and reload pf manually:
        $ sudo pfctl -ef /etc/pf.conf

    Note: Updates to the OS may override the pf.conf file, make sure to
    make a backup of it.

..  note::

    In the case in which you know how to configure macOS to allow
    binding privileged ports without firewall redirection,
    please let us know and we will improve this documentation.

..  include:: first-steps.include
