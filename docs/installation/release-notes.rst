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


Version 6.1.2, 2026-10-13
-------------------------

Version 6.1.0 released on 2026-10-09, and 6.1.1 were released on 2026-10-12,
as a release candidate.


Security Fixes
^^^^^^^^^^^^^^

* HTTP/HTTPS services configured to receive forwarded requests via a reverse
  proxy now reject direct OpenID Connect login requests that lack the required
  proxy origin headers, even when a `Referer` header is present.
  To support both direct and proxied access, configure two separate services:
  one with `client_forwarded_header` empty for direct access, and another with
  forwarded headers configured for access through the reverse proxy.
  [server-side][entra-id][okta][https] [#5782]
* Tracebacks are now excluded from event data and default email, log, and
  webhook output to prevent disclosure of sensitive information.
  All event handler templates can explicitly include tracebacks using `{tb}`.
  Event handling also uses less memory by generating JSON data only on demand.
  [server-side][client-side] [#7684]
* Vault items now report an error whenever parsing produces no usable content.
  Previously, trusted certificate and pinned key items created from nonempty
  input without usable PEM content could silently disable TLS server identity
  verification, allowing an untrusted server to be accepted.
  [client-side][ftps][https] [#7698]


New Features
^^^^^^^^^^^^

* The Web Manager now stores a preferred color theme for each administrator
  and applies it automatically after login.
  The preference is available on the administrator's settings page.
  Theme changes are saved automatically after 15 seconds without further
  changes, while preserving other pending configuration edits.
  [manager] [#2174]
* A Helm chart is available as an option for installing SFTPPlus on Kubernetes.
  [server-side][kubernetes] [#3036]
* Administrators can configure the SSH receive window and maximum packet size
  for each SFTP and SCP service to improve uploads over high-latency connections.
  The receive window now defaults to 2 MiB instead of 128 KiB.
  [server-side][sftp][scp] [#4654]
* Cluster nodes now advertise their configured node name, or the local hostname
  when no name is configured, during synchronization with the controller.
  [server-side][cluster] [#5461]
* Standard output and local file event handlers now support Logfmt output.
  [server-side][client-side][logs] [#5786]
*  Missing event data fields no longer interrupt text or CSV logging.
   [logs] [#5786]
* The Web Manager now provides permission selectors and an ordered path rule
  table for configuring account and group file access.
  [manager] [#5790]
* The Web Manager now exports Prometheus metrics for process start time,
  application metadata, resource usage, and reactor delay at `/metrics`.
  [manager][kubernetes] [#6292]
* The Web Manager activity log now shows the estimated country and network
  organization for public IP addresses in newly recorded events.
  [manager] [#6423]
* Application authentication can now continue to another authentication method
  when an account belongs to none of its allowed groups.
  [server-side] [#6487]
* Transfers can be scheduled on the 28th through 31st or on the last or
  second-last day of each month. Days absent from a month are skipped.
  [client-side] [#7019]
* Certificate expiration warnings now cover AS2 private and partner certificates
  configured for accounts, services, and locations, as well as TLS certificates
  used by locations, resources, authentications, and event handlers.
  [manager] [#7585]
* The Web Manager group configuration now provides a list for adding and removing
  home folder structure directories.
  [manager] [#7615]
* The Web Manager provides a virtual folder editor for accounts and groups,
  with separate virtual and local paths and a local filesystem browser.
  [manager] [#7617]
* Account and group permissions are now configured separately using
  `default_permissions` and `path_permissions`.
  [server-side] [#7618]
* Azure BLOB and Azure Files locations, and Exchange Online locations, can now
  authenticate using Azure Workload Identity. Kubernetes deployments can access
  these services without storing a client secret or storage access key.
  [client-side][kubernetes] [#7629]
* Transfer schedules can now be configured in the Web Manager using start and
  stop actions, day selections, and a time picker.
  [manager] [#7679]
* Events now include a severity level and a peer address shortcut.
  New standard output loggers use these fields in their default Logfmt output
  for easier integration with Grafana and Loki.
  [logs][kubernetes] [#7686]
* Cluster nodes can now test their controller connection and configure trusted
  certificates directly during initial setup or from the synchronization
  resource in Web Manager.
  [cluster][server-side] [#7698]
* The Web Manager can export the full public certificate chain without the
  private key, and export or copy all trusted certificates. Pasted PEM content
  with whitespace around each line is accepted.
  [manager] [#7700]


Defect Fixes
^^^^^^^^^^^^

* AS2 uploads no longer fail with `Context was already finalized` when a
  transfer pauses and resumes.
  [client-side][as2] [#5591]
* Web Client browser requests that fail during processing now return to the
  login page instead of displaying a plain error page. JSON requests receive
  an internal server error response in JSON format.
  [server-side][https] [#5782]
* Reduced CPU usage when viewing component status and configuration.
  [manager] [#7547]
* Monitoring large folders is faster when the location does not provide file
  identifiers.
  [client-side] [#7681-1]
* Event handlers use less CPU when formatting timestamps and CSV log entries.
  [logs][event-handlers] [#7681]
* Services now release their listening ports when startup fails, allowing them
  to restart after the configuration is corrected.
  [server-side][ftp][sftp][https] [#7702]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The event handler `servers` filter is replaced by `pool_uuids`. Existing
  configuration values are migrated automatically.
  [event-handlers] [#5461]
* Log messages no longer contain newline characters. Carriage returns and line
  feeds are replaced with spaces, with each CRLF pair replaced by a single space.
  [logs][event-handlers] [#5786]
* The implicit `No` default for account `create_home_folder` has been removed.
  Accounts without this setting now inherit their primary group's value.
  [server-side] [#6487]
* Python API extensions now receive read-only event data in
  `getConfiguration()`. Extensions that change data there must create a copy.
  The worker's `handle()` method still receives a mutable event copy.
  [api][event-handlers] [#7681]
* Account information is no longer included in `data.avatar` or `{data_json}`.
  The `{data.avatar}` and `{data.avatar.ATTRIBUTE}` placeholders are no longer
  available. Use `{account}` and `{account.ATTRIBUTE}` instead, for example
  `{account.name}`. Existing handler INI templates are automatically migrated.
  [event-handlers] [#7684-1]
* Tracebacks are no longer included in event data or `{data_json}`, including
  email templates. Use `{tb}` to explicitly include a traceback.
  Serialized events no longer include the legacy empty `data_json` field.
  The `{data_json}` placeholder remains available in event handler templates.
  [event-handlers] [#7684]


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
