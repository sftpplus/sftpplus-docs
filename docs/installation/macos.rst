macOS Installation
==================

..  contents:: :local:


Overview
--------

For macOS systems, SFTPPlus is distributed as a self-extractable `.sh`
shell script or as a `tar.gz` gzipped TAR archive.
These packages are to be found on the online download page for SFTPPlus.
For example, the link for trial SFTPPlus packages is
https://www.sftpplus.com/documentation/sftpplus/trial/.

Using a dedicated system account to run SFTPPlus is strongly recommended.
By default, a new system user named ``sftpplus`` is created during installation.
This is a special type of OS user also known as a service account.
You can customise the name and unique ID of this user during installation.
You can also use an already existing user, but make sure it can access
the location of the installed product.

This dedicated OS user should not be used in any other way,
doesn't require a password to be set for it,
and should not be available through SFTPPlus services.


Self-extractable installer
--------------------------

To install SFTPPlus using the `.sh` self-extractable shell script,
simply launch it in Terminal with superuser privileges::

   sudo /bin/sh ./sftpplus-macos-arm64-VERSION.sh

The self-extractable installer asks for the destination path.
To set it non-interactively, add the installation directory as an argument::

   sudo /bin/sh ./sftpplus-macos-arm64-VERSION.sh /Library/sftpplus

To check all available options for the SFTPPlus installation::

   /bin/sh ./sftpplus-macos-arm64-VERSION.sh -- --help

Some more options are set interactively during installation,
such as the name of the system user to run SFTPPlus and
the name of the default administrative account and its password.

Only read this page further if you need to manually tweak the installation
process of SFTPPlus beyond the options available through the installer.


Installing using the gzipped TAR archive
----------------------------------------

Installing SFTPPlus using the `.tar.gz` gzipped TAR archive consists of
unpacking the archive, initializing the configuration, and generating the
SSH keys and the SSL key and certificate to be used by the product.
To have SFTPPlus launched at boot, you may use the included `plist`
(property list) file.

All steps beyond unpacking the archive can be handled by the shell script
found at `bin/install.sh` in the hierarchy of SFTPPlus files.


Unpacking the archive
^^^^^^^^^^^^^^^^^^^^^

After downloading the compressed archive, you can extract its files using
the following command::

    tar xfz sftpplus-macos-arm64-VERSION.tar.gz

To install SFTPPlus, move (or copy/link) the unpacked directory to your
preferred installation path, for example: ``/Library/sftpplus``::

    sudo mv sftpplus-macos-arm64-VERSION /Library/sftpplus

SFTPPlus may be installed in any location on the local file system.
In this documentation page we assume that SFTPPlus is unpacked in the
``/Library/sftpplus`` directory.
Avoid using spaces or special characters in the SFTPPlus installation path.


Automated installation from unpacked archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest way to install SFTPPlus is to execute the shell script
found at `bin/install.sh` in the hierarchy of SFTPPlus files.
For example::

    sudo /Library/sftpplus/bin/install.sh

The `install.sh` script will guide you through all the necessary steps.

Once the installation is complemented,
the install script will automatically start the SFTPPlus process.
You can check the status of the SFTPPlus process using::

    launchctl list | grep SFTPPlus

After a successful installation using the shell script, jump to
`Listening on privileged ports`_
to learn how to enable SFTPPlus to listen on privileged ports.

Otherwise, only go further down this page for manual installation or debugging.


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

    cd /Library/sftpplus
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
On macOS systems, SFTPPlus always runs under a regular account, thus requiring
a dedicated operating system account, such as ``sftpplus``, to be created.
Creating a dedicated new group and a new user for running SFTPPlus
is therefore strongly recommended.

In the following examples we use the default configuration value of
``sftpplus`` for the name of the user to run SFTPPlus.
To create an ``sftpplus`` group and a corresponding user,
use the commands exemplified below.
You can replace the value of ``299`` from the following commands with
a unique ID for your system.
On macOS, you can use `dscacheutil -q user` or `dscacheutil -q group` to
identify the used IDs and pick a unique ID.
The commands below are included into an easy-to-use script available on
`GitHub Gist <https://gist.github.com/adiroiban/80c8acc00b8957869f68>`_::

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
``/Library/sftpplus``, but in a typical installation it also requires write
permission to the `log/` subdirectory (for logging) and the `configuration/`
subdirectory (for saving changes to the running configuration).
Since SFTPPlus on macOS runs under an unprivileged OS account at all times,
write permissions for the `run/` sub-directory are needed for saving its PID.

The next step is to configure your operating system to automatically
start SFTPPlus on boot.
On macOS, SFTPPlus is designed to be started via the `launchd` system tool
as a daemon that runs continuously.
You can use the example `launchd` job definition provided
with SFTPPlus.
The job definition file is formatted as XML, and it is called a property list
file or a `plist` file.
Edit this file with your favourite editor, e.g. ``vi``::

    vi bin/sftpplus-mft.plist

Depending on where the job definition is copied onto your system,
it will be treated as a service or an agent.
In order to have SFTPPlus act as a global service,
launching each time the macOS system starts,
you need to copy it in the appropriate place::

    sudo cp bin/sftpplus-mft.plist /Library/LaunchDaemons/sftpplus-mft.plist

After the file is copied, you need to instruct `launchd` to load/read the new
job definition file using the command::

    sudo launchctl load /Library/LaunchDaemons/sftpplus-mft.plist

..  note::
    During startup, the `launchd` process will scan and automatically load job
    definitions found in the `/Library/LaunchDaemons` directory.

To stop SFTPPlus, use the following command::

    sudo launchctl unload /Library/LaunchDaemons/sftpplus-mft.plist

In the case that there are problems starting the server, you can check the log files at
`SFTPPLUS-INSTALL-DIR/log/launchd-stdout.log` and
`SFTPPLUS-INSTALL-DIR/log/launchd-stderr.log`.
You can read more about `launchd` on the `official documentation page
<https://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html>`_.


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

..  include:: first-steps.include
