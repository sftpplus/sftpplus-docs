Release Notes
=============

This page lists the changes for SFTPPlus version 6.

For compatibility changes and upgrade instructions, see :doc:`Upgrading to SFTPPlus 6<./upgrade>`.

Release notes for earlier major versions are available below.

..  toctree::
    :maxdepth: 1

    release-notes-v5
    release-notes-v4
    release-notes-v3
    release-notes-v2
    release-notes-v1

.. release-notes-start


Version 6.0.0, 2026-09-18
-------------------------


Security Fixes
^^^^^^^^^^^^^^

* The embedded Python version used by SFTPPlus was updated to version 3.14.7. [#7471]
* The OpenSSL library was updated to version 4.0.1. [#7504]


New Features
^^^^^^^^^^^^

* The Web Manager now provides light and dark theme controls.
  The browser remembers the selected theme across sessions.
  [manager] [#5602]
* The Web Manager and management API now show the signature algorithm,
  certificate SHA-256 fingerprint, and public-key SHA-256 fingerprint for
  certificates.
  [manager] [#7526]
* The Web Manager now warns Internet Explorer 11 users that their browser is no
  longer supported and directs them to SFTPPlus version 5 when IE11 is required. [#7565]
* Cluster nodes are now configured in pools that share a name, password, and
  configuration. Web Manager uses pool names when configuring cluster access.
  Existing `cluster-nodes` sections are automatically migrated to
  `cluster-pools`, and the node synchronization `username` option is migrated
  to `pool_name`.
  An optional `node_name` setting is available and defaults to empty. [#7577]


Defect Fixes
^^^^^^^^^^^^

* The Web Manager API now checks vault-item read permissions when including
  an existing vault item's content in a pinned-key import. [#7597]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Service configuration returned by the Web Manager JSON-RPC API is now flat.
  Integrations must read and update protocol options directly on the service,
  without the nested `configuration` object or `configuration/` path segment.
  Existing INI configuration files are unchanged. [#2599]
* The event handler `groups` configuration option was renamed to `event_groups`
  to distinguish it from account groups.
  Existing configurations are automatically migrated without changing event
  filtering behavior. If both options are configured, `event_groups` is used. [#6521]
* On Linux, the IBM MQ C client and Microsoft Purview SDK libraries are now
  available in a separate extra-connectors archive.
  IBM MQ locations and Microsoft Purview event handlers report a clear
  installation error when their extra-connectors files are missing.
  Windows packages continue to include both connectors.
  See the version 6 upgrade guide for connector installation and startup
  configuration instructions. [#7165]
* SSL v3 is no longer supported. [#7471-1]
* You can no longer generate Certificate Signing Requests
  or self-signed certificates using the SHA-1 algorithm. [#7471]
* The Web Manager service no longer supports Internet Explorer 11.
  Use Firefox, Chrome, Edge or other modern web browsers.
  Microsoft ended support for Internet Explorer 11 in 2022.
  [manager] [#7565]
* The Python API for extending LDAP authentication has been removed,
  including the `extension_entry_point` and `extension_configuration` options.
  Custom LDAP extensions and the bundled extension for validating TOTP codes
  using secrets stored in LDAP are no longer supported.
  Before upgrading, replace any authentication checks provided by these
  extensions and remove the obsolete configuration options.
  LDAP servers that validate TOTP codes themselves remain supported. [#7575]
* The obsolete `legacy-webadmin` HTTP event format has been removed.
  Event handlers configured with this format fail to start with an unknown
  format error. [#7590-1]
* HTTP authentication methods and HTTP event handlers now accept a single URL.
  Support for fallback URLs has been removed. Existing comma-separated URL
  lists are automatically migrated to their first value; all remaining values
  are discarded. HTTP event handlers continue to support retrying that endpoint
  using `retry_count` and `retry_increase`. [#7590]
* The `deny-username` and `ip-time-ban` authentication methods are no longer
  supported. Their settings are migrated to the default security policy,
  preserving values already configured in that policy. The default legacy
  sections and their authentication references are removed. Other legacy
  sections remain as disabled placeholders. Services using a custom security
  policy must have the corresponding restrictions configured in that policy. [#7591]
* The `anonymous` authentication method is no longer supported. Existing
  anonymous authentication configurations remain as disabled placeholders.
  Use an application account with a password for file transfer access. [#7596]
