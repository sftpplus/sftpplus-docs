Updates and upgrades
====================

..  toctree::
    :maxdepth: 1
    :hidden:

    upgrade-to-v5
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

SFTPPlus version 6 was released in 2026.
Version 6 is under active development and support.

To update from an older version 6 to the latest version 6 release,
follow the general update procedure for your operating system.

It is important that you check the latest version and changes,
as well as recommended update procedures in the
:doc:`Server Release Notes<./release-notes>`.


Updating from trial version
---------------------------

Once you have obtained the full version of the software,
follow the regular updating instructions using the full version software.

The configuration defined during the trial period is kept and automatically migrated to the fully-featured version.


Upgrading from version 5
------------------------

Review the compatibility and connector changes below before upgrading an existing SFTPPlus 5 installation to version 6.
Complete any required connector installation and startup configuration before restarting SFTPPlus.


Deny usernames and ban IP authentication methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `deny-username` and `ip-time-ban` authentication methods have been deprecated. They were replaced with the security policies.
The configuration is automatically migrated.


LDAP Python API extension
^^^^^^^^^^^^^^^^^^^^^^^^^

The LDAP Python API extension authentication support has been removed.
There is no direct replacement for this extension in version 6.
Contact us if you require assistance with migrating from the LDAP Python API extension.
The configuration is automatically migrated.


Service configuration API
^^^^^^^^^^^^^^^^^^^^^^^^^

The Web Manager JSON-RPC API now returns common and protocol options in the same service configuration object.
For example, `port` and `idle_connection_timeout` are both direct properties of a service.
The nested `configuration` object has been removed.

Update integrations that create services to send protocol options directly in the service object.
For updates, use paths such as `services/UUID/idle_connection_timeout` instead of `services/UUID/configuration/idle_connection_timeout`.
Read protocol options from the same flat structure in configuration responses and service startup snapshots.
Update administrator role permission paths that target protocol options to use these flat paths.
Python extensions that access a service manager must use `service.configuration.OPTION` instead of `service.configuration.configuration.OPTION`.


HTTP authentication and event handlers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HTTP authentication methods and HTTP event handlers no longer support fallback URLs.
Existing comma-separated URL lists are automatically migrated to their first value; all remaining values are discarded.
HTTP event handlers continue to support retrying the configured URL using `retry_count` and `retry_increase`.

The obsolete `legacy-webadmin` HTTP event format has been removed.
Event handlers configured with this format fail to start with an unknown format error.
Update these handlers to use a supported format and ensure that the receiving endpoint accepts it.
See the :doc:`HTTP event handler configuration </configuration-events/http>` for supported formats.


HTTP authentication permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HTTP authentication responses now support separate `default_permissions` and `path_permissions` members.
The legacy `permissions` member is still accepted for compatibility.
Its first list supplies default permissions, and subsequent lists supply path rules.
If the first list is `["inherit"]`, default permissions are inherited and the account path rules are empty.
Explicit `default_permissions` and `path_permissions` members take precedence over legacy values.
See the :doc:`HTTP authentication API</developer/http-api-authentication>` for the current response format.


Event handler group filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The event handler `groups` configuration option has been renamed to `event_groups` to distinguish it from account group filters.
Existing configuration files are automatically migrated, preserving the event group filters.
If both options are configured, the `event_groups` value takes precedence, including an empty value.
Update any custom configuration templates or scripts that use the old option name to use `event_groups`.


Runtime and browser compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SFTPPlus 6 uses Python 3.14 and OpenSSL 4.
Internet Explorer 11 is no longer supported.
Use a supported modern browser to access Web Manager and Web Client.


IBM MQ and Microsoft Purview on Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On Linux, the IBM MQ C client and Microsoft Purview SDK libraries are now available as :doc:`extra connectors<./extra-connectors>`.
Install the separate archive when upgrading if you use either connector.
The extra-connectors guide describes how to extract the archive and set ownership of the connector directories.

For IBM MQ, update your installed systemd unit or other startup script to include the new library paths in `LD_LIBRARY_PATH`::

    /opt/sftpplus/ibm-mq/lib64:/opt/sftpplus/ibm-mq/gskit9/lib64

Replace the old `/opt/sftpplus/lib/ibm-mq` paths and adapt `/opt/sftpplus` to your installation directory.
Retain any other required directories already present in `LD_LIBRARY_PATH`.
Follow the :doc:`extra-connectors startup configuration<./extra-connectors>` instructions to apply the changes before restarting SFTPPlus.

Windows packages continue to include these libraries.


Migrating from node-based to pool-based cluster configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In SFTPPlus version 6, the cluster configuration has changed from a nodes-based approach to a pool-based approach.

When migrating a cluster to v6 you will need to follow the following steps:

* Upgrade the controller instance first
* Upgrade each node instance

The pool configuration replaces the individual node configuration from earlier versions.
Existing `cluster-nodes/UUID` sections are automatically migrated to `cluster-pools/UUID`, preserving their UUIDs and configuration options.
An existing deployment can continue to use one pool per node.


Upgrading from version 4 or earlier
-----------------------------------

If you are using SFTPPlus version 4 or earlier, you will first need to upgrade to SFTPPlus version 5.
Once your SFTPPlus installation is on version 5,
you can upgrade to latest SFTPPlus.

.. grid:: 1 1 2 1
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`move-to-top` Upgrade to version 5
        :link-type: doc
        :link: ./upgrade-to-v5

        Reference documentation for upgrading to version 5.
        Version 5 is no longer in active development.
        Version 5 is still supported until 2029.
