.. container:: tags pull-left

    `server-side`
    `client-side`
    `security`
    `configuration`


Hardening SFTPPlus Deployments
==============================

..  contents:: :local:


Introduction
------------

The default SFTPPlus configuration provides a balance between a secure
deployment, ease of troubleshooting and compatibility with external systems.

This page documents a few steps which can be followed to increase the security
of SFTPPlus deployments.


Running as a non-privileged account
-----------------------------------

SFTPPlus can operate under a non-privileged account on any operating system.
You don't need `root` or an administrator account to start the SFTPPlus process.

Keep in mind that on Unix-like systems this will not allow SFTPPlus to
authenticate accounts from the operating system, you will be limited to
only authenticating application-level accounts.

The operating system account used to run the SFTPPlus process only needs
the following rights to access SFTPPlus files:
* read permissions for the configuration file,
* write permissions for the log files,
* read/write permissions for the actual files managed by SFTPPlus.


Review file permissions
-----------------------

All the files belonging to an SFTPPlus installation should be set so that they
only have read permissions for the account under which SFTPPlus runs.
They should not have read permissions (or any other permission) for
other accounts.

When logs are stored in a local file and log rotation is enabled, SFTPPlus
will need write permissions to the log file as well as to the folder containing
this file.

If you only send the logs to a syslog server or a remote HTTP server, you will
not need write permissions for a local log file.

When using Local Manager, SFTPPlus will need read and write access to its
configuration file and to the folder containing this configuration file.
This is because SFTPPlus will create a temporary file before updating the
main configuration file.

If you don't use Local Manager, you can set SFTPPlus with read-only access
to the configuration files.


Lock accounts inside their home folder
--------------------------------------

All SFTPPlus application accounts are locked by default inside their home
folder, and there is no configuration option to allow full access.

Accounts belonging to the operating system can be configured in SFTPPlus to
have access to all the files found on the machine running SFTPPlus.
This includes files from other users, but also files used by
the operating system or by other applications.

To reduce the risk of unwanted access to sensitive files, you should always
configure an account to be locked inside its home folder.

When you want multiple accounts to access each other's data, design the
directory structure so that all files are in a dedicated root folder, and set
the home folders for these accounts to this dedicated root folder.
By locking the accounts in their home folders, they will still have access to
the shared files, but will not have access to the OS files or other files
outside of the dedicated common root folder.


Hiding the product name and version
-----------------------------------

By default, SFTPPlus will advertise the product name and version to clients
using its file transfer services.

You may conceal the identity of the SFTPPlus file transfer services by
configuring a different name or configuring just the name without a
version number.

You can do this for the FTP/FTPS service by setting a value for the `banner`
configuration option which starts with the `>` character.

For the HTTP/HTTPS file transfer service and for the Local Manager service
you can use the `headers` configuration option to set a different value for
the standard `Server` header.

Note that a targeted attacker could still detect the product or even
a specific version by observing idiosyncrasies in server operations
(for example responses to invalid requests).


Enforce HTTPS usage
-------------------

For the Local Manager and the HTTPS file transfer services you may configure
the service to enable `HTTP Strict Transport Security
<https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security>`_.

This can be done using the `headers` configuration option.

Note that this will deny the usage of the self-signed certificate generated
by default in SFTPPlus.


Mitigate exposure to scan attacks
---------------------------------

The easiest way to avoid scan attacks is to use non-standard ports for
file transfer services.

When this is not an option, you can configure SFTPPlus to immediately
block known usernames widely used by scanners, without forwarding the
authentication requests to specialized methods.

You can also configure SFTPPlus to ban an IP once a configured number of
failed authentication requests were generated from that source IP in a
configured period of time.
