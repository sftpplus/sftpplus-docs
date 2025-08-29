Updates and upgrades
====================

..  toctree::
    :maxdepth: 1
    :hidden:

    upgrade-to-v4
    upgrade-to-v3
    upgrade-to-v2


Introduction
------------

There are 2 classes of software version changes for SFTPPlus:

* updates, where the same first digit in the version number is kept, and
* upgrades, where the first digit in the version number is incremented.

**Updates** add new functionality, fix defects, and improve security.

**Upgrades** include all of the above,
but also remove functionalities and introduce backward-incompatible changes.

The backward-incompatible changes introduced in upgrades are typically due to increased security standards.
However, for most such changes, there are backward-compatible options that can be manually enabled.

Upgrades are also used to remove support for obsolete protocols, outdated security mechanisms, and end-of-life versions of supported operating systems.

Before proceeding with an update or an upgrade, ensure that SFTPPlus
and all its file transfer services are stopped.

Then, make sure to backup the SFTPPlus configuration
located inside the "configuration" directory of the installation path.

The previous configuration is automatically updated to the newer version as needed.
Reinitializing the configuration or the service account and groups is not required.

Consult the :doc:`Server Release Notes<./release-notes>`,
as they contain detailed information on the steps required for updating between specific versions.


Updating to latest version
--------------------------

SFTPPlus version 5 was released in 2024.
Version 5 is under active development and support.


To update from on older version 5 to the latest version 5 release,
follow the general update procedure for your operating system.

It is important that you check the latest version and changes,
as well as recommended update procedures in the
:doc:`Server Release Notes<./release-notes>`.


Updating from trial version
---------------------------

Once you have obtained the full version of the software,
follow the regular updating instructions using the full version software.

The configuration defined during the trial period is kept and automatically migrated to the fully-featured version.


Upgrade from version 4
----------------------

You first need to update to the last version 4, SFTPPlus version 4.35.0.

Once your SFTPPlus 4 installation is up-to-date,
you can upgrade to latest SFTPPlus version 5
over the existing installation following the update steps for Windows, Linux, or macOS.

The configuration file is automatically updated.

In comparison with version 4, SFTPPlus version 5 is introducing a higher default security level.

SFTPPlus 4 installations using weaker security algorithms or cryptographic keys need to be either updated to use more secure keys and cryptographic algorithms,
or configured to allow exceptions for weaker security options.

Security changes are described in the next section.

.. grid:: 1 1 2 1
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`move-to-top` Upgrade to version 4
        :link-type: doc
        :link: ./upgrade-to-v4

        Reference documentation for upgrading to version 4, released in 2020.
        Version 4 is no longer in active development.
        Version 4 is still supported until 2027.


Functional changes from version 4
---------------------------------

Below is a summary of all the major changes since version 4.0.0.
Note that some of these changes were introduced during the development of SFTPPlus version 4.

The server-side user account passwords stored in plain text are no longer supported.
The plain text passwords are automatically converted to hashed passwords at start time.

The following operating systems are no longer supported:

* 32-bit Windows installations
* Red Hat Enterprise Linux version 5, 6, and 7
* macOS on Intel Macs
* AIX.

Note that support for 64-bit Windows installations is unchanged.
We can also reinstate support for one or more of these platforms if there is significant request.

The following operating systems are newly-supported in SFTPPlus 5:

* macOS on Apple Silicon
* glibc-based Linux distributions on ARM64 / Apple Silicon.

TLS certificates with RSA keys of size 1024 or signed using SHA-1 are
no longer accepted as part of the default security level.
If you still need to use weak RSA keys or TLS certificates,
you can configure SFTPPlus ciphers list as::

    ssl_cipher_list = secure@seclevel=0

The following ciphers were removed from our `secure` list of SSH ciphers:

* diffie-hellman-group-exchange-sha1
* diffie-hellman-group14-sha1
* hmac-sha1
* aes256-cbc
* aes192-cbc
* aes128-cbc

The following SSH ciphers are no longer supported:
* cast128-ctr
* blowfish-ctr
* 3des-ctr

OS accounts are no longer supported on Apple macOS. [server-side] [#3135]

The OS authentication method now requires explicit configuration for the
allowed list of operating system groups. In previous versions, when the
"allowed_groups" was not defined, the OS authentication was allowing users
from any OS group. [security] [#4972]

The `monitor` service was migrated to a resource.

The `manager_authentications` configuration of the `server` section was removed.
The Web Manager console now uses the authentication defined directly
in the manager service configuration.
The old configuration is automatically migrated, no manual configuration changes are required. [manager] [#5879]

The default authentication method for RADIUS is now MS-CHAP-V2, improving the default security.
In previous versions the default method was PAP. [server-side] [#5701]

The `rsa_private_key` and `dsa_private_key` configuration options were
replaced with the `ssh_host_private_keys` configuration
option.

The Python API event handler extension no longer allows emitting events directly via the `parent.emitEvent` method. The extension should now return a list of event data to be emitted by the event handler. [api] [#5961]

When the name of the user is used to dynamically define the `home_folder_path` or `ssh_authorized_keys_path` from the group configuration, the following characters are now replaced with the dot (.) character: `\ / : * ? " < > |`.
This change prevents creating invalid path names. [#5959]

The `session_username` cookie is no longer used by the Web Manager interface. [manager] [#5900]

The `group_association` configuration option for the OS authentication method
no longer accepts a group UUID. The group UUID configuration was moved to the
new `base_groups` option. In this way, you can configure the OS accounts to
be associated with multiple SFTPPlus groups.
The existing configurations are automatically migrated, manual changes are not required. [server-side] [#3494]

The `shared_secret` configuration option for the RADIUS authentication method
was renamed as `password`. The change is automatically migrated, manual
changes are not required. [server-side][radius] [#5865]

The account or administrator `source_ip_filter` configuration option no longer supports the `inherit` value. Inheriting is now always enabled.

The `source_ip_filter` configuration option now requires
comma-separated values instead of a space-separated one spanning multiple lines. This
makes it possible to explicitly list both allowed and denied IP addresses.
The previous configuration format only supported allowed IP addresses. The
`source_ip_filter` configuration is automatically converted to allow the
selected IPs while denying all other IPs. [server-side] [#5751]

The legacy WebAdmin authentication method is no longer supported. If you are
still using the SFTPPlus PHP Webadmin authentication, you can use the generic
HTTP authentication method together with PHP WebAdmin version 1.11.0 or
newer. [server-side] [#425]

New SFTPPlus installations no longer automatically generate SSH DSA/DSS host keys.
SSH DSA is considered a less secure legacy cryptographic algorithm.
Customers may still manually enable SSH DSA/DSS host keys, they are still
supported. [server-side] [#5800-1]

The `disabled` value is no longer supported for the transfer's `source_uuid`
and `destination_uuid` configuration options. Previously, the `disabled`
values were accidentally supported instead of the default local filesystem.
[client] [#5629]

The `configuration.identity` section from the server configuration JSON-RPC
API was removed. The accounts, groups, roles, and administrator configuration
are now accessible via `configuration.acccounts`, `configuration.groups`,
`configuration.roles`, and `configuration.administrators` options
respectively. [manager][api] [#5651]

The role permission targets for accounts, roles, groups, and administrators
were updated to deprecate the `identity` part. Access to accounts, roles,
groups, and administrators can now be granted and restricted based on the
`configuration/accounts`, `configuration/groups`, `configuration/roles`, and
`configuration/administrators` targets respectively. The old target
`configuration/identity/accounts` still works via the programmatic API.
For access to accounts, roles, groups, and administrators via the Local
Manager UI, you need to update the configuration to use the new paths.
The old path is planned to be removed in future version 5 of SFTPPlus.
[manager][security] [#5651-1]

The `--ssl-allowed-methods` configuration option of the client shell now
requires a comma-separated list of TLS methods. In previous versions, it was
a space-separated list, requiring extra escaping when invoked from a shell.
[cli] [#4453-1]

The `ssl_allowed_methods` configuration option was updated from being a
space-separated value to a comma-separated value. The conversion is done
automatically, no manual changes required. [#4453]

The authentication for an administrator fails if any of the roles associated
with the admin is disabled. This is a change from the previous version 4.16.0,
where the authentication was denied only for the first (primary)
associated role of an administrator. [manager] [#5573]

The `role` configuration option for an administrator was renamed as `roles`.
The change is automatically migrated by SFTPPlus. [manager] [#3398]

The `address` and `port` configuration options for the WebDAV client were
removed, being replaced with the `url` option. Old configuration options
are automatically migrated to use `url`. [client-side][webdav] [#5602]

The CRL digital signature extension no longer supports validating the configured certificate against a certificate revocation list. [#5961-1]

The `disable` value is no longer a valid value for the following configuration options:

* To disable executing external commands for a transfer, you should now set the
  `execute_before`, `execute_after_success`, `execute_after_failure`,
  `execute_on_destination_before`, `execute_on_destination_after_success`, or
  `execute_on_destination_after_failure` configuration options to empty
  values.
  Using `disable` is supported until the next major release. [#2090-10]
* To disable filtering the source files for a transfer, you should now set the
  `source_filter` configuration option to an empty value.
  Using `disabled` is supported until the next major release. [#2090-11]
* To disable the process service account on Linux or macOS, you should now set
  the `account` configuration option to an empty value.
  Using `disabled` is supported until the next major release. [#2090-12]
* To disable log file rotation based on time, you should now set the `rotate_on`
  configuration option to an empty value.
  Using `disabled` is supported until the next major release. [#2090-13]
* To disable the usage of PAM for Linux OS authentication, you should now set
  the `pam_usage` option to an empty value.
  Using `disabled` is supported until the next major release. [#2090-1]
* To disable the SSH public key loading for a file, you should now set the
  `ssh_authorized_keys_path` option to an empty value.
  Using `disabled` is supported until the next major release. [#2090-2]
* To disable archiving the files for a transfer, you should now set the
  `archive_success_path` or `archive_failure_path` configuration options to
  empty values.
  Using `disabled` is supported until the next major release. [#2090-3]
* To disable CCC FTPS for a transfer, you should now set the `ftps_ccc`
  configuration option to an empty value.
  Using `disabled` is supported until the next major release. [#2090-4]
* To disable the usage of an explicit FTPS passive address for an FTP or FTPS
  server, set `passive_address` configuration option to an empty value.
  Using `disabled` is supported until the next major release. [#2090-5]
* To disable uploading files with modified names for users, set
  `amend_write_name` configuration option to an empty value.
  Using `disabled` is supported until the next major release. [#2090-6]
* To disable attaching associated files to an email, you should now set the
  `email_associated_files` to an empty value.
  Using `disabled` is supported until the next major release. [#2090-7]
* To disable the creation of a destination folder for a file dispatcher, you
  should now set the `create_destination_folder` to an empty value.
  Using `disabled` is supported until the next major release. [#2090-8]
* To disable authenticating an SFTP location with SSH keys, you should now set
  the `ssh_private_key` to an empty value.
  Using `disabled` is supported until the next major release. [#2090-9]
* To disable the usage of a SSL certificate, CA, or CRL for a connection, you
  should now set the `ssl_certificate`, `ssl_certificate_authority`, or
  `ssl_certificate_revocation_list` to empty values.
  Using `disabled` is supported until the next major release. [ssl] [#2090]


Upgrade from version 3
----------------------

For upgrading from version 3,
you need to first upgrade to the :doc:`last version 4 release </installation/upgrade-to-v4>`.

Once your SFTPPlus 4 installation is up-to-date, you can follow the upgrade process described at the start of this page.

.. grid:: 1 1 2 1
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`move-to-top` Upgrade to version 3
        :link-type: doc
        :link: ./upgrade-to-v3

        SFTPPlus version 3 was released in 2015.
        It is no longer in active development or support.
        The information on this page is provided for legacy deployments.


Upgrade from version 2
----------------------

If you are still using SFTPPlus version 2 or older,
and you plan to upgrade, get in touch with our support team.
They can help you upgrade to the latest supported version.


.. grid:: 1 1 2 1
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`move-to-top` Upgrade to version 2
        :link-type: doc
        :link: ./upgrade-to-v2

        SFTPPlus version 2 was released in 2013.
        It is no longer in active development or support.
        The information on this page is provided for legacy deployments.
