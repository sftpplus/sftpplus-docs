Release Notes
=============

This is the list of all changes for SFTPPlus releases, ordered by release
number (not by release date).

.. release-notes-start


Version 4.25.0, 2022-11-04
--------------------------

Version 4.25.0rc1 was released on 2022-11-03 as the first release candidate,
and other than changes to the text of the release note itself,
there are no other changes.


New Features
^^^^^^^^^^^^

* The Azure AD authentication method now supports configuring extra API access
  scopes to be requested by SFTPPlus during authentication. They can be used to
  implement custom extensions that integrate with Azure AD and Azure API.
  [server-side] [#2196]
* You can now configure the `email-sender` event handler to send emails
  using data attached to an event. [#5906-1]
* The email address associated with an account is now available in the event
  handlers. [#5906]
* You can now configure the email event handler to send emails to an account or
  all accounts in a group (if they have a configured email address).
  [server-side] [#5917]
* A new event handler was added that can detect the accounts associated with a
  file that was created, modified, or removed. [server-side] [#5954]


Defect Fixes
^^^^^^^^^^^^

* When executing external scripts or commands on Linux and macOS, SFTPPlus now
  automatically sets the `PWD` and `PATH` environment variables. In previous
  versions, for security considerations, external commands were executed in
  a restricted environment with no default variables. [linux][macos]
  [#5923-1]
* When executing external scripts or commands on Windows, SFTPPlus now
  automatically sets the `SystemDrive` and `SystemRoot` environment variables.
  In previous versions, for security considerations, external commands were
  executed in a restricted environment with no default variables. [windows]
  [#5923]
* FTP and FTPS locations no longer fail to perform a password-less TLS
  certificate-based authentication for servers returning FTP code 232. Previous
  versions had support for password-less authentication only for servers
  returning FTP code 230. [client-side][ftp][ftps] [#5950]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* When the name of the user is used to dynamically define the
  `home_folder_path` or `ssh_authorized_keys_path` from the group
  configuration, the following characters are now replaced with the dot (.)
  character: `\ / : * ? " < > |`. This change was made to prevent creating
  invalid path names. [#5959]


Version 4.24.0, 2022-10-12
--------------------------

The final release contains a bugfix for the "Reports" page of the web console.
This bug was introduced in 4.24.0rc1.

The final release also contains a bugfix for the pagination of the
"Activity Log" page of the web console.
This bug was introduced in 4.23.0.


Version 4.24.0rc2 was released on 2022-10-11
and adds more bug fixes on top of the first release candidate.

Version 4.24.0rc1 was released on 2022-09-30 as the first release candidate.


New Features
^^^^^^^^^^^^

* The event with ID `20192` is now emitted at the start of each day with a
  summary of the transfer activity for the last day. [#3459]
* You can now configure a transfer with a fallback destination path using the
  `destination_fallback_path` configuration option. This is used when the main
  configured destination path doesn't exist. It can be used together with
  dynamically-defined destination paths. For now, this configuration is
  only designed to work with non-recursive transfers. Support for fallback in
  recursive transfers will be added in a future release. Get in touch with us
  if you need the fallback functionality for recursive transfers. [client-side]
  [#3478]
* AIX version 7.1 and newer is again a supported platform. Service Pack
  7100-05-09 is required on AIX 7.1 [#5931]


Defect Fixes
^^^^^^^^^^^^

* When installing with Security-Enhanced Linux enabled, the dedicated
  SFTPPlus operating system user is assigned a sub-directory under
  ``/var/lib/`` to allow the SFTPPlus system service to run scripts
  from the installation directory. [#5771]
* The FTP `ALLO` command is now handled as an operation that is not required,
  returning code `202`, which is associated with a successful event. There was a
  regression introduced in version 4, which returned code `502`,
  associated with an error event. [server-side][ftp] [#5909]
* The web management console now keeps the session active as long as the
  web page is active in the web browser. In version 4.23.0, a regression was
  introduced, letting the session expire 5 minutes after login.
  [manager] [#5926]
* The web manager UI was fixed for `source_ip_filter` configuration. This is a
  regression introduced in version 4.23.0. [manager] [#5929]
* The retry for a failed file no longer blocks the whole transfer processing
  queue. This is a regression introduced in version 4.20.0. [client-side]
  [#5938]
* The pagination now works for the "Activity Log" page of the web console.
  This was a bug introduced in version 4.23.0. [manager][#5947]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `session_username` cookie is no longer used by the Local Manager web
  interface. [manager] [#5900]
* The OAuth2 redirection URL for Azure AD was changed from
  `https://SITE-ADDRESS/__chsps__/login?redirect-AUTH-UUID` to
  `https://SITE-ADDRESS/?redirect-AUTH-UUID`. You need to manually update the
  Azure AD Application Registration Redirect URIs. [server-side][http] [#5903]


Version 4.23.0, 2022-09-23
--------------------------

Version 4.23.0rc2 was released on 2022-09-21 as a release candidate,
with security updates.
Version 4.23.0rc2 was released on 2022-09-14 as a release candidate,
and includes more defect fixes.
Version 4.23.0rc1 was released on 2022-08-23 as a release candidate,
as the first release candidate.


Security Fixes
^^^^^^^^^^^^^^

* The cross-site scripting (XSS) protection was improved for the web console's
  `Activity Log` page. Any HTML markup produced by a malicious person
  via the log system is now sanitized. In previous versions, if a malicious
  person attempted to log in using a username formatted as an HTML link, the
  link was displayed on the page. More so, JavaScript and CSS code could be
  inserted. However, no JavaScript code would have been executed,
  as Content Security Policy (CSP) was already enabled in previous versions.
  The same sanitization was done for the review page difference view.
  For the review page, the risk was even lower, as only administrators
  could produce malicious changes. [manager] [#5872]
* The Python runtime has been patched to address CVE-2022-0391 for urlparse.
  [#5890]


New Features
^^^^^^^^^^^^

* You can now configure the Azure AD authentication method to remove the domain
  name from usernames. In this way, SFTPPlus handles Azure AD users
  using shorter names. [#2375]
* The OS authentication method now supports associating OS users with multiple
  SFTPPlus groups. [server-side] [#3494]
* You can now override options from the main `server.ini` configuration file
  with configuration variables stored in `server.override.ini`. This is
  designed to help sharing the `server.ini` configuration between testing and
  production instances, or between nodes in a load balancer or a cluster.
  [#4964]
* You can now install and uninstall SFTPPlus on Linux and macOS using the
  provided shell scripts ``install.sh`` and ``uninstall.sh`` found in the
  ``bin/`` sub-directory of your SFTPPlus installation path. [#5757]
* The new `HTTP pull` location was added to allow transferring files from
  arbitrary HTTP URLs. [client-side][http] [#5808]
* The web console now shows the name of the current SFTPPlus instance at
  the top of every page. [#5823]
* The `http-pull` location can now trigger the downloading of a remote file
  based on the payload extracted from a local file. Once a local file is
  detected in the source directory, it is used as the payload for the request,
  and the response is stored in the destination file. [#5835]
* The `http-pull` location can now request to download a file using a `POST` or
  `PUT` method with a specific request body and a set of request headers.
  [client-side][http] [#5836]
* The Azure AD authentication method can now connect to the Internet via an
  HTTP proxy. [server-side] [#5883]
* The `ssh_delete_delay` configuration option for groups was added to instruct
  the SFTP server to delay performing a delete operation requested by a client.
  The client is informed that deletion was successful, but the operation is not
  done right away. This was implemented to work around an issue with the Azure
  Data Factory SFTP connector, that requested the file to be deleted before
  sending the file close operation. [server-side][sftp] [#5895]
* RSA keys generated by SFTPPlus now have a default size of 3072-bit. [#3292]
* Alpine Linux 3.12 and newer on x86_64 are now supported through a generic
  musl-based package. Other x86_64 Linux distributions using musl should work,
  provided musl 1.1.24 or newer is available. [#5890]
* Red Hat Enterprise Linux 9 is now supported on x86_64. Its clones such as
  Oracle Linux, Rocky Linux, AlmaLinux are also supported. [#5890-2]


Defect Fixes
^^^^^^^^^^^^

* The event with ID `10093` is no longer emitted multiple times for
  an FTP service that was restarted repeatedly. [server-side][ftp] [#5173]
* Deletion of accounts and groups stored in external configuration files was
  fixed. This defect was introduced in SFTPPlus version 4.22.0. [manager]
  [#5824]
* The OS authentication method no longer fails when multi-group support
  is enabled via `group_association = base-and-os-groups` if the user is
  already a member of the base group. This is a regression only affecting the
  4.23.0rc1 version. [#5871]
* The Azure AD integration now works when SFTPPlus runs behind an HTTP proxy. In
  previous versions, when SFTPPlus was behind a proxy, the Azure AD redirection
  link would be the internal SFTPPlus URL instead of the public URL.
  [server-side] [#5883]
* The `group -> home_folder_structure` configuration options can now be
  modified using the web console. This is a regression introduced in version
  4.22.0. [manager] [#5862]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Support for AIX was removed due to lack of demand.
  If you are an existing customer looking for an update on AIX 7.1 or newer,
  please get in touch with our support team.
* The `sync_pull` permission for roles was renamed as `sync`. If you already
  have one or more roles using the `sync_pull` permissions, you have to
  manually update them to use the `sync` permission. [manager] [#1907]
* The `group_association` configuration option for the OS authentication method
  no longer accepts a group UUID. The group UUID configuration was moved to the
  new `base_groups` option. In this way, you can configure the OS accounts to
  be associated with multiple SFTPPlus groups. The existing configurations are
  automatically migrated, manual changes are not required. [server-side]
  [#3494]
* The `shared_secret` configuration option for the RADIUS authentication method
  was renamed as `password`. The change is automatically migrated, manual
  changes are not required. [server-side][radius] [#5865]


Version 4.22.0, 2022-07-11
--------------------------

The 4.22.0 final version was preceded by a series of release candidates.
In addition to the release candidates, the final version contains an updated
user interface for configuring accounts.

Version 4.22.0rc5 was released on 2022-07-08 as a release candidate. It added
support for defining virtual folders containing a `${USER}` placeholder.

Version 4.22.0rc4 was released on 2022-06-14 as a release candidate.
Version 4.22.0rc3 was released on 2022-06-08 as a release candidate.
Version 4.22.0rc2 was released on 2022-06-07 as a release candidate.
Version 4.22.0rc1 was released on 2022-06-06 as a release candidate.


Security Fixes
^^^^^^^^^^^^^^

This release includes a security related backward-incompatible change.
This change is designed to improve the security of SFTPPlus and to discourage
insecure or ambiguous configurations.

When the account or administrator `source_ip_filter` configuration is empty,
it now uses the access rules defined in the associated groups or roles.

In previous versions, the rules from the associated groups or roles were
ignored.
With an empty `source_ip_filter` configuration at the account or admin level,
the authentication was always successful,
even when the source IP was not allowed by associated groups or roles.


New Features
^^^^^^^^^^^^

* You can now configure groups with dynamic virtual folders using permissions
  based on the authenticated username. [server-side] [#2786]
* SFTPPlus Web File Browser can authenticate users via Azure Active Directory.
  [server-side][http] [#3250]
* Virtual folders defined for a group that contains the `${USER}`
  placeholder are considered user home paths. They are automatically created
  when the `create_home_folder` configuration option is enabled. [server-side]
  [#4600]
* The `source_ip_filter` configuration option now supports defining both
  allowed and denied IP addresses for an account. [server-side] [#5751]
* You can now configure a transfer to wait for multiple files before
  transferring the files as a batch. [client-side] [#5772]


Defect Fixes
^^^^^^^^^^^^

* An internal error is no longer triggered when a message encrypted for an
  unknown partner/certificate is received over AS2. The event with ID 40044 is
  now emitted with an informative error message. The remote AS2 partner is
  informed that the transfer failed. [server-side][as2] [#5704]
* The JQuery library used by SFTPPlus Local Manager web console and the legacy
  web pages was updated to use the latest version. [server-http] [#5799]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The account or administrator `source_ip_filter` configuration option no longer
  supports the `inherit` value. Inheriting is now always set.
  [#5751-1]
* The `source_ip_filter` configuration options were changed from a
  comma-separated value to a space-separated one spanning multiple lines. This
  makes it possible to explicitly list both allowed and denied IP addresses.
  The previous configuration format only supported allowed IP addresses. The
  `source_ip_filter` configuration is automatically converted to allow the
  selected IPs while denying all other IPs. [server-side] [#5751]
* New SFTPPlus installations no longer automatically generate SSH DSA/DSS host
  keys. SSH DSA is considered a less secure legacy cryptographic algorithm.
  Customers may still manually enable SSH DSA/DSS host keys, they are still
  supported. [server-side] [#5800-1]
* The following ciphers were removed from our `secure` list of SSH ciphers:
  diffie-hellman-group-exchange-sha1, diffie-hellman-group14-sha1, hmac-sha1.
  SHA1 is no longer considered a secure algorithm. [#5800]


Version 4.21.0, 2022-05-31
--------------------------

In this release, we continue to redesign the user interface and to improve
user interaction for the web management console.


New Features
^^^^^^^^^^^^

* You can now configure the Local Manager web console to only show server-side
  configuration options, client-side configuration options, or both. [manager]
  [#2795]
* The rules for defining virtual folders were relaxed to allow defining virtual
  folder names without using absolute paths. [server-side] [#5680]


Defect Fixes
^^^^^^^^^^^^

* The main process no longer fails to start when configured with invalid
  values for numeric configuration options. The process now automatically
  recovers from such an error by using default values for the affected
  configuration options. The event with ID 20190 is emitted to inform about this
  error. [#1926]
* On Windows, operating system accounts with unlocked / full access to all the
  local drives are working again. This is a regression introduced in version
  3.17.0. [windows][server-side] [#5680-1]
* When SFTPPlus runs on Windows, you can now set the home folder path using an
  UNC path to a directory inside a Windows Share. [server-side] [#5680]
* When the configuration is changed for a Python API event handler, the handler
  is now highlighted as requiring restart. [#5722]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The event with ID 20020, emitted when an invalid value is configured for the
  `port` number, was removed. It was replaced by the generic event with ID
  `20190`, emitted when any configuration option has invalid values. [#1926]


Version 4.20.0, 2022-05-10
--------------------------


New Features
^^^^^^^^^^^^

* The configuration documentation pages were reorganized with separate
  sections for server-side, client-side, and managed file transfer options.
  [#1925]
* SFTPPlus can now call up to 3 concurrent external processes. In previous
  versions, the old limit was 2. The new limit of 3 is designed to reduce
  the general operating system memory and process handlers usage. [#5308]
* To allow the transfer of a source file to a dynamic destination path, the
  `transform` option was added to `destination_path_actions`. The
  destination can be defined based on current date and time, or based on parts
  of the source file path. [client-side] [#5409]
* You can now associate LDAP and RADIUS users with one or multiple SFTPPlus
  groups UUIDs using the `group_mapping` configuration option.
  [server-side][ldap][radius] [#5482]
* Windows Server 2022 is now a supported platform. [#5653]
* Amazon Linux 2022 is now supported on x86_64. [#5653-2]
* Ubuntu Server 22.04 LTS is now supported on x86_64. [#5694]


Defect Fixes
^^^^^^^^^^^^

* You can now configure the `external-executable` event handler and the
  `execution` action of the `file-dispatcher` event handler with timeouts
  greater than 30 seconds. In previous versions, there was a hard limit of
  30 seconds. [events] [#5308]
* A transfer now continues processing source files when restarted after a
  failure. This is a regression introduced in version 4.3.0, for which a
  complete product restart is required to recover from a failed transfer.
  [client-side] [#5615]
* When no explicit source or destination location UUIDs are defined for a
  transfer, the DEFAULT-LOCAL-FILESYSTEM UUID is now explicitly used. In
  previous versions, the value was left empty, which implicitly triggered the
  usage of the default local filesystem. [client-side] [#5629]
* Included zlib libraries were updated to version 1.2.12 to fix CVE-2018-25032
  on all platforms except Windows. [#5653-2]
* The OpenSSL 1.1.1 libraries used for Python's cryptography on Windows,
  generic Linux, and macOS were updated to version 1.1.1n to fix CVE-2022-0778.
  On generic Linux and macOS, this fix is also applied to Python's stdlib ssl.
  The OpenSSL 1.0.2 libraries used on AIX for Python's cryptography and the
  stdlib ssl module were patched for CVE-2022-0778. [#5653]
* The documentation search was fixed to prevent stalling. [#5661]
* The documentation for the events was updated to show double quotes characters
  instead of HTML codes. [doc] [#5670]
* The `admin-shell` command was fixed. The error was introduced in version
  4.19.0. [cli] [#5681]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `disabled` value is no longer supported for the transfer's `source_uuid`
  and `destination_uuid` configuration options. Previously, the `disabled`
  values were accidentally supported instead of the default local filesystem.
  [client] [#5629]
* The event with ID 20034 emitted when a service is configured with an unknown
  protocol was removed and replaced by the event with ID 20091. The event with
  ID 20091 is now emitted for any component configured with an unknown type.
  [server-side] [#5648]
* The role permission targets for accounts, roles, groups, and administrators
  were updated to deprecate the `identity` part. Access to accounts, roles,
  groups, and administrators can now be granted and restricted based on the
  `configuration/accounts`, `configuration/groups`, `configuration/roles`, and
  `configuration/administrators` targets respectively. The old target
  `configuration/identity/accounts` still works via the programmatic API.
  For access to accounts, roles, groups, and administrators via the Local
  Manager UI, you need to update the configuration to use the new paths.
  The old path is planned to be removed in future version 5 of SFTPPlus.
  [manager][security] [#5651-1]
* The `configuration.identity` section from the server configuration JSON-RPC
  API was removed. The accounts, groups, roles, and administrator configuration
  are now accessible via `configuration.acccounts`, `configuration.groups`,
  `configuration.roles`, and `configuration.administrators` options
  respectively. [manager][api] [#5651]


Version 4.19.0, 2022-04-18
--------------------------

You can now associate an account with multiple groups.
This simplifies managing shared virtual folders across
multiple users and groups.

Version 4.19.0rc1 was released on 2022-04-07 as a release candidate.
No changes were made to the final release since the release candidate.


New Features
^^^^^^^^^^^^

* You can now configure an account to be associated with multiple groups. In
  this way, an account has access to the virtual directories and inherited
  permissions defined in all of the associated groups. [server-side] [#2184]
* The Local Manager's user interface for configuring the list of SSL/TLS
  ciphers to be used by HTTPS and FTPS services has been improved to allow
  selecting from a list of available ciphers. [ssl] [#5600]
* The Python API extension `handle` method can now return a string to
  be emitted in an event and logged.
  [api] [#5626-1]
* The Python API extension `handle` method can now return a sequence of
  Python dict instances containing the `message` attribute.
  This sequence is used to emit events with specified messages.
  A dict instance can contain other attributes to be made available to the
  event handling mechanism of SFTPPlus.
  [api] [#5626-2]
* For the Python API Extension event handler,
  the `getConfiguration` method can now return a scheduled
  result to be used for delaying execution or for waiting for an
  additional external condition before executing the event. [api] [#5626]


Version 4.18.0, 2022-04-04
--------------------------

The look and feel of Local Manager's login page was refreshed.
This is the first step into updating the Local Manager web console interface
over the coming releases.

Version 4.18.0rc1 was released on 2022-04-01 as a release candidate.
No changes were made to the final release since the release candidate.


New Features
^^^^^^^^^^^^

* The `ssl_allowed_methods` configuration option now supports the `secure` and
  `all` values, which can be used to configure a set of methods via a single
  configuration value. [#4453]
* The `as2_no_mdn_success_text` configuration option was added to allow
  returning a custom text message on success when no MDN was requested. In
  previous versions, the response was a fixed empty text. [server-side][as2]
  [#5581]


Defect Fixes
^^^^^^^^^^^^

* When serving a file via FTP fails before its entire data is sent,
  the event with ID 10070 is emitted to signal the failure.
  The event with ID 10069 is no longer emitted, this event is reserved
  for successful operations.
  [server-side][ftp] [#5588]
* You can now enable DHE ciphers for server-side services. Previously, only
  ECDHE-based ciphers were available. [server-side][ssl] [#5597]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `--ssl-allowed-methods` configuration option of the client shell now
  requires a comma-separated list of TLS methods. In previous versions, it was
  a space-separated list, requiring extra escaping when invoked from a shell.
  [cli] [#4453-1]
* The `ssl_allowed_methods` configuration option was updated from being a
  space-separated value to a comma-separated value. The conversion is done
  automatically, no manual changes required. [#4453]


Version 4.17.0, 2022-03-18
--------------------------

Version 4.17.0rc1 was released on 2022-02-28 as a release candidate.
No changes were made to the final release since the release candidate.


New Features
^^^^^^^^^^^^

* The Local Manager UI for selecting multiple component identifiers was updated
  to allow selecting from a list of names. Copy-pasting identifiers is
  no longer needed. [manager] [#5559]
* The file browser for HTTP(s) clients has an updated UI which is enabled by
  default for all new installations. Existing installations continue to use
  the old UI, but you can manually update them to show the new UI by changing
  the `ui_version = ui-gen-2` configuration option. [server-side][http] [#5563]
* The LDAP authentication method now supports Security Account Manager (SAM)
  usernames when connecting to an Active Directory LDAP server. This is done
  using the sAMAccountName username attribute. [server-side][ldap][ad] [#5575]


Defect Fixes
^^^^^^^^^^^^

* The AS2 server can now receive encrypted files. In previous versions, the AS2
  server was only able to receive non-encrypted AS2 files. [server-side][as2]
  [#5499-1]
* The user interface for configuring the AS2 MDN receipt for a location was
  fixed to describe the methods as "Synchronous". In previous versions, the
  description was "Asynchronous", but the configuration was always set as
  synchronous. [manager][as2] [#5499]
* An administrator now fails to be authenticated when
  configured with a missing role. [manager] [#5573]
* When sending files over AS2, SFTPPlus now encodes their names using
  MIME encoding.
  In previous versions, filenames were encoded using only UTF-8.
  [client-side][as2] [#5499]
* SFTPPlus can now receive AS2 files with Unicode names encoded using the
  RFC 2047 or RFC 2231 standards.
  [server-side][as2] [#5499]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The authentication for an administrator fails if any of the roles associated
  with the admin is disabled. This is a change from the previous version 4.16.0,
  where the authentication was denied only for the first (primary)
  associated role of an administrator. [manager] [#5573]


Version 4.16.0, 2022-02-10
--------------------------

This release includes a security fix for a denial of service of
moderate severity affecting the SFTP and the SCP server-side protocols.


New Features
^^^^^^^^^^^^

* You can now configure a role to restrict read access to parts of
  the configuration for associated administrators. [manager][security] [#1164]
* The LDAP authentication method provides a Python-based API for augmenting the
  configuration for an account, after the account was successfully
  authenticated. [server-side] [#1886]
* You can now configure roles for restricting associated administrators, making
  it possible to only allow certain operations. [manager][security] [#3397]
* You can now associate an administrator with more than one role. [management]
  [#3398]
* You can now configure LDAP authentications to search in multiple base DNs.
  [server-side][authentication] [#3631]
* You can now configure a timeout for the requests made by the HTTP event
  handler. [server-side][http] [#3779]
* You can now configure a Windows Share / SMB server to not require encryption.
  This allows SFTPPlus to connect to legacy servers such as Windows Server 2008
  and older versions. [client-side][smb] [#4497]
* The event with ID `20174`, emitted when failing to handle an event, now
  contains the path of the associated file. [management] [#4800-1]
* The HTTP POST / webhook API for event handles now emits the event with ID
  `20189` after a successful operation. [management][api] [#4800]
* The HTTPS AS2 server now accepts requests made using the HTTP PUT method.
  [server-side][http] [#5509]
* The `file-dispatcher` event handler now supports the `ignore` action, which
  does nothing. It was added to make it possible to ignore files that might be
  matched by more generic rules. [mft][events] [#5510]
* The HTTP web file manager has a new login UI. For backward compatibility,
  existing installations still use the old UI after upgrading. You can switch
  to using the new UI via the `ui_version` configuration option.
  [server-side][https] [#5514]
* Each emitted event now has a unique identifier, formatted as an UUID
  version 4 value. [#5516]
* The `source_filter` configuration option for a transfer, when used with
  globbing expressions, can now be used to match files based on their full path.
  To do so, make sure the matching expression contains path separators.
  [client-side] [#5548]


Defect Fixes
^^^^^^^^^^^^

* You can now set the `password_lifetime` configuration option for a group
  using the Local Manager web interface. Due to a defect, in previous versions
  it was only possible to set it manually via the configuration file. [manager]
  [#5500]
* The HTTPS AS2 server can now receive multiple AS2 messages (files) over the
  same connection. In previous versions, a single file was accepted per
  connection. To accept another file, the previous connection had to be closed,
  and a new one opened. [server-side][as2] [#5509]
* A remote denial of service for SFTPPlus' SFTP / SCP servers and clients
  was fixed. During SSH handshakes, SFTPPlus could have been forced to use all
  available  memory. To mitigate this until upgrading, you should reject public
  access to SFTP / SCP servers, only allowing connections from trusted sources.
  [security][server-side][client-side][sftp][scp] [#5525]
* The automatic archive clean-up now works with recursive transfers. This issue
  was introduced in version 4.0.0. Older versions are not affected. [#5527]
* When trying to generate a PGP RSA or DSA key using an unsupported key size,
  the error message now lists the available sizes. In previous versions, an
  internal server error was generated. [pgp] [#5533]
* It is now possible to disable `delete_source_parent_delay` on a transfer,
  by setting it to value 0 from Local Manager.
  Due to a defect in previous GUI versions,
  you could only set it to a minimum value of 1,
  making it impossible to disable it from the GUI.
  For previous versions, as a workaround, you can still disable it by manually
  editing the configuration file. [#5493]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `multi_factor_authentication_attribute` configuration option from the
  LDAP authentication method was removed. It was replaced with the
  `python:chevah.server.extension.ldap_mfa.AugmentedTOTP` extension.
  [server-side] [#1886]
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
* The `group_name` data attribute of event `20137` was updated to include a
  comma-separated list of all the groups or roles associated to an account or
  administrator. [server-side] [#3398-1]
* The `role` configuration option for an administrator was renamed as `roles`.
  The change is automatically migrated by SFTPPlus. [manager] [#3398]
* The event with ID 30050 used for server-side SFTP timeout events was updated.
  It is now used for generic SSH connection close events. [#5525]


Version 4.15.0, 2021-10-29
--------------------------

This release contains 3 major defect fixes:

* A fix for the SFTP service to close a file for which an open/upload request
  failed. On Windows, this no longer generates files locked by SFTPPlus, which
  would require a service restart to be unlocked.
* A fix for the HTTP service to prevent not receiving the initial part of a
  transferred file for requests missing the `Expect: 100-continue` header.
* A fix for the HTTP service to correctly detect the client source IP
  as the original client when multiple chained proxies are used.

The following release candidates were created for this release:

* 4.15.0rc1, released 2021-10-19
* 4.15.0rc2, released 2021-10-20


New Features
^^^^^^^^^^^^

* You can now configure the `file-dispatcher` event handler to perform an
  action on a file using an external executable or script. [mft] [#14]
* The events with ID 10069 and 10078, emitted when downloading or uploading a
  file over FTP, now contain information about the transfer size, speed, and
  duration. [server-side][ftp] [#2870]
* You can now configure the HTTP file upload API (REST / AS2 / multi-part
  POST) to accept a set of key/value metadata attached to the events
  associated with a file upload request. This metadata is propagated to the
  audit and event handling systems. [server-side][http][rest][api] [#376]


Defect Fixes
^^^^^^^^^^^^

* The full file content is now received over HTTP PUT, multipart form, and AS2
  method when no `Expect` header is provided in the request. In previous
  versions, if part of the content was sent in the same data chunk as the HTTP
  headers, that file data was ignored. Requests made using `Expect:
  100-continue` are not affected by this issue. [server-side][http] [#1471]
* You can now edit OS accounts in the Local Manager.
  This was a regression introduced in version 3.46.0. [server-side] [#2873]
* SFTPPlus now uses the first IP address from `X-Forwarded-For` or
  `Forwarded` headers as the original source IP address. In previous
  versions, it was assuming that the last IP address from the header is the
  client original source IP. [server-side][http] [#31-1]
* SFTPPlus now extracts the port value from the `X-Forwarded-For` header.
  In version 4.14.0, it was assuming that the value of the header doesn't
  contain a port number. This concerns Azure's HTTP Load Balancer and Internet
  Information Services (IIS) servers, which are including the port
  in the forwarded header. [server-side][http] [#31]
* The Local Manager web interface no longer shows the WebDAV location as
  requiring a restart due to updated address or port. This was a defect
  introduced in 4.11.0 while updating the WebDAV location configuration
  from address and port to URL. [manager] [#3671]
* The SFTP service no longer keeps a file locked when failing to write it with
  the set of attributes requested by the SFTP client. In previous versions,
  if an SFTP client requested to create a file with a set of attributes, and
  those attributes were not accepted by the operating system, the operation
  failed, but the file was accidentally left open. [server-side][sftp] [#5142]


Version 4.14.0, 2021-10-15
--------------------------


Security Fixes
^^^^^^^^^^^^^^

* SFTPPlus now blocks client TLS renegotiation requests over TLS 1.1/1.2.
  This issue does not affect TLS 1.3 connections, as key exchange parameters
  are no longer negotiated between client and server. [server-side][security]
  [#3267]
* The OpenSSL 1.0.2 libraries used on AIX for Python's cryptography and the
  stdlib ssl module were patched for CVE-2021-3712. OpenSSL version 1.0.2 is
  not affected by CVE-2021-3711. [#5728-2]
* The OpenSSL 1.1.1 libraries used for Python's cryptography on Windows,
  generic Linux, and macOS were updated to version 1.1.1l to fix CVE-2021-3711
  and CVE-2021-3712. On generic Linux and macOS, the same CVEs were fixed for
  Python's stdlib ssl module. [#5728]


New Features
^^^^^^^^^^^^

* When SFTPPlus operates behind an HTTP reverse proxy, it can be configured via
  the `client_forwarded_header` option to extract the source address of a
  connection by parsing a header such as `X-Forwarded-For`, `Forwarded`, etc.
  [server-side][http][https] [#1555]
* You can now configure a list of allowed source IP addresses for
  authenticating an administrator. [manager] [#2908]
* You can now configure the default filename used for AS2 file transfers.
  In previous versions, a fixed filename was used if an AS2 request
  didn't include one. [server-side][http][as2] [#5717]
* The events emitted for a transfer are now associated with the source
  location. [client-side] [#5721]


Defect Fixes
^^^^^^^^^^^^

* When a location fails while a transfer is using that location as the source,
  the event with ID 60040 is emitted to inform that the transfer is no longer
  monitoring the source. In previous versions, the event 60040 was delayed
  until the source location was reconnected. [client-side] [#3960-1]
* If the source location of a transfer is manually stopped, the Local Manager
  web interface now highlights that the transfer is suspended. In previous
  versions, the transfer status was reported as "started". [client-side]
  [#3960-2]
* File changes at the source location are now observed even if the connection
  is disconnected between checks. In previous versions, the list of changes
  was reset on disconnect, and no files were being transferred. [client-side]
  [#3960]
* The utility used by SFTPPlus to manage its Windows service was updated to
  prevent antivirus false-positives. [windows] [#4644]
* For SMTP client configuration, the authentication password is now ignored
  when no username is defined. In previous versions, an internal server error
  was generated. As workarounds for previous versions, you can either
  explicitly disable the password or you can define the username as
  two double quotes: `""`. [smtp][email] [#4977]
* The AS2 file transfer service can now receive data for UTF-8 encoded
  filenames. [server-side][as2] [#5717]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* 32-bit Windows is no longer supported. If you still use an x86 version of
  SFTPPlus, it is recommended to upgrade to the x64 version. [windows] [#5713]


Version 4.13.0, 2021-08-30
--------------------------

Below are the changes since the 4.13.0rc3 release candidate.


Defect Fixes
^^^^^^^^^^^^

* The SharePoint Online authentication was updated to work with latest
  Microsoft server changes. [client-side][webdav] [#5710]


Version 4.13.0rc3, 2021-08-21
-----------------------------

Below are the changes since the 4.13.0rc2 release candidate.


New Features
^^^^^^^^^^^^

* You can now use Azure Files as a source location for a transfer.
  [client-side][http] [#5016]

* You can now configure a SMB (Windows Share, Azure Files, Samba) location as
  the source and destination for a transfer. [client-side][smb] [#4701][#5685]


Version 4.13.0rc2, 2021-08-12
-----------------------------

Below are the changes since the 4.13.0rc1 release candidate.


New Features
^^^^^^^^^^^^

* Azure Storage API was updated to use API version 2020-04-08. [#3010-1]
* Azure Files locations can now list directories and get the attributes of
  items. [client-side][http] [#3010]
* You can now configure a timeout for the HTTP authentication method. In the
  previous version, the HTTP authentication connection was closed after a fixed
  120 seconds if the server didn't return a response. [server-side] [#5696]
* The RADIUS authentication method now supports CHAP, MS-CHAP-V1 and
  MS-CHAP-V2. [server-side] [#5701]
* The RADIUS authentication method can be configured with a custom `NAS-Port`
  number and now has a debug option. [server-side] [#5702]
* The `group_mapping` configuration now does case insensitive matching for the
  attribute names. [server-side][ldap][radius] [#5706-1]
* You can now configure the RADIUS authentication to continue validating the
  credentials even when the RADIUS server returned a successful response. This
  can be used to implement multi-factor authentication for legacy operating
  system accounts, by sending first the requests to a MFA aware RADIUS server.
  [server-side] [#5706]


Defect Fixes
^^^^^^^^^^^^

* HTTP and HTTPS file downloads now work with cURL. This was a regression
  introduced in version 4.12.0. [server-side][http][https] [#5693-1]
* HTTP and HTTPS file transfer services now support resuming downloads.
  [server-side][http][https] [#5693]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The default authentication method for RADIUS is now MS-CHAP-V2. In previous
  versions the default method was PAP. [server-side] [#5701]


Version 4.13.0rc1, 2021-08-02
-----------------------------


Security Fixes
^^^^^^^^^^^^^^

* Python libraries were updated to fix CVE-2021-23336, addressing a web cache
  poisoning issue reported in urllib.parse.parse_qsl(). SFTPPlus is not using
  urllib.parse.parse_qsl() and was never vulnerable to this security issue. If
  you are explicitly calling urllib.parse.parse_qsl() as part of a custom
  SFTPPlus Python extension, update to this version to fix CVE-2021-23336.
  [#5682]


New Features
^^^^^^^^^^^^

* You can now configure a transfer using a temporary file name to an Azure
  Files location destination. [#5022]
* AIX 7.1 and newer for IBM Power Systems is now a supported platform. AIX
  packages embed OpenSSL 1.0.2 libraries patched with latest security fixes, up
  to and including CVE-2020-1971, CVE-2021-23840, CVE-2021-23841. [#5581]
* Alpine Linux 3.14 on x86_64 is now supported. [#5682]
* When failing to initialize the data connection the error message now
  indicates whether a passive or active connection was attempted. In previous
  versions both passive and active connections had the same error message.
  [server-side][ftp] [#5681]
* The data associated with an event will now contain the file extension and the
  file base name without the extension. [#5686]
* You can now configure the duration for which SFTPPlus will wait for the
  RADIUS server to provide a response. In previous versions, a fixed timeout of
  10 seconds was used. [server-side][radius] [#5694]


Defect Fixes
^^^^^^^^^^^^

* The links and commands to start the Local Manager and documentation pages
  will now start much faster. [local-manager] [#5677]
* An extra event with ID 20024 is no longer emitted when failing to initialize
  the FTP client passive connection. [client-side][ftp][ftps] [#5681-1]
* An FTP transfer and location no longer fails when the remote directory can't
  be listed. The error is emitted and the directory listing is retried.
  [client-side][ftp][ftps] [#5681-2]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Alpine Linux 3.12 is no longer supported. We recommend using Alpine Linux
  3.14 on x86_64 for your containerized SFTPPlus deployments. [#5682]


Version 4.12.0, 2021-07-06
--------------------------


New Features
^^^^^^^^^^^^

* The `source_ip_filter` configuration option now allows defining a range of
  allowed IP addresses using the Classless Inter-Domain Routing (CIDR)
  notation. [#1044]
* When a new component is created using the Local Manager interface, the
  component is automatically started if "Launch at startup" is enabled.
  [local-manager] [#1917]
* WebDAVS locations now support HTTP Basic Authentication.
  [client-side][webdavs][https] [#3913]
* SFTPPlus can now be launched with a read-only configuration file and cache.
  [server-side] [#5591]
* Azure Files Locations now support automatic directory creation.
  [client-side][http] [#5593]
* The account configuration now contains the account creation time
  in ISO format. [server-side] [#5635]
* TOTP multi-factor authentication for LDAP users is now possible even with
  standard LDAP servers not providing native TOTP support. [#5663]
* The SFTPPlus download page now has specific entries for Amazon Linux and
  older Red Hat Enterprise Linux versions. These entries link to the generic
  Linux SFTPPlus package, which works with any glibc-based Linux distribution.
  [#5664]


Defect Fixes
^^^^^^^^^^^^

* The "Enabled at startup" configuration option was renamed as "Launch at
  startup". [local-manager] [#1917]
* The last login report now only shows the IP address, the port number is
  no longer shown. This makes it easier to search based on IP only.
  [#5637]
* Event with ID 60070 emitted when the destination location is connecting and
  not yet ready for a transfer, was updated from the `failure` group to the
  `informational` one. [#5643]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* SUSE Linux Enterprise Server (SLES) 11 and 12 on X86_64 are no longer
  supported. Use the generic Linux package on SLES and contact us if you need
  specific support for SFTPPlus on any version of SUSE Linux Enterprise Server,
  including using OS-provided OpenSSL libraries instead of our generic ones.
  [#5664]


Version 4.11.0, 2021-05-06
--------------------------

This is the final release of version 4.11.0.
Below are the changes since the 4.11.0rc1 release candidate.


Defect Fixes
^^^^^^^^^^^^

* The LDAP authentication method now supports IPv4 LDAP.
  This was a regression introduced in 4.11.0rc1.
  [server-side] [#2227]

* The FTP `idle_data_connection_timeout` option now uses the default value when
  set to zero or a negative number, as documented. In previous versions, the
  timeout was disabled when the value was zero. [server-side][ftp] [#5610]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Default value for `connection_retry_interval` was increased from 60
  seconds to 300 seconds (5 minutes). Default value for
  `connection_retry_count` was increased from 2 to 12. This results in
  connections for remote SFTP or FTP locations being retried for 1 hour before
  stopping the transfers. [client-side] [#5610]


Version 4.11.0rc1, 2021-04-27
-----------------------------


Security Fixes
^^^^^^^^^^^^^^

* Python has been patched with latest security patches from ActiveState. Fixes
  CVE-2020-27619, CVE-2020-26116, CVE-2019-20907, CVE-2020-8492. On Linux and
  macOS, CVE-2021-3177 has also been fixed. [#5600-2]
* The OpenSSL libraries used for Python's cryptography on Windows, generic
  Linux, and macOS were updated to version 1.1.1k. Fixes CVE-2020-1971,
  CVE-2021-23840, CVE-2021-23841, CVE-2021-3449, and CVE-2021-3450. On generic
  Linux and macOS, same CVEs were fixed for Python's stdlib ssl module. [#5600]


New Features
^^^^^^^^^^^^

* The LDAP authentication method now supports IPv4 LDAP over TLS/SSL, also
  referred to as LDAPS. [server-side] [#2227]
* It is now possible to configure the timeout delay for external commands
  called during a transfer. In previous versions, this was fixed to 15 seconds.
  [client-side] [#5549]
* You can now configure the OS authentication method to associate
  authenticated OS accounts to an SFTPPlus group with the same name or with
  a specific group name. In previous versions, authenticated OS accounts
  were associated with the default SFTPPlus group. [server-side] [#5559]
* Client-side WebDAV location is now configurable using an URL. This allows
  configuring connections to WebDAV pages that are not located in the
  HTTP server's root path. [client-side][webdav] [#5602]
* The `file-dispatcher` event handler now supports explicit globbing matching
  expressions to define a full destination path. In previous versions, when
  a globbing expression was used, the destination path only defined the
  base directory, therefore the filename was always appended to it. [#5604-1]
* You can now explicitly define a globbing matching expression using the
  `g/EXPRESSION/` format. [#5604]
* Events with ID 60012 and 60017 emitted on a successful client-side transfer
  now contain the destination file path as part of the attached data.
  [client-side] [#5597]


Defect Fixes
^^^^^^^^^^^^

* In Local Manager, in the list of accounts for a local file authentication
  method, you will now see the name of the associated group. In previous
  versions, the group was listed as UNKNOWN. [#2368]
* The authentication page of the Local Manager web console was fixed to work
  with Internet Explorer. This was a defect introduced in version 4.10.0.
  [#5547]
* Defining configuration options in Local Manager using text values
  containing newline characters other than the default Unix or Windows
  characters no longer generates an invalid configuration file. [manager]
  [#5553]
* The OS authentication manager now shows an error at startup when no group
  is configured for allowed users or administrators. In previous versions,
  the OS authentication would start with no errors, then deny all
  authentication requests. [#5559]
* On Linux and macOS, the OpenPGP event handler now works when the main
  SFTPPlus process is started as root. [#5592]
* For file transfers configured to not transfer duplicated files via the
  `transfer_memory_duration` and `ignore_duplicate_paths` options, the entire
  file transfer is now retried as a transfer restart when the rename operation
  fails. In previous versions, the file was not re-transferred after the
  failed rename operation. [client-side] [#5597]
* Documentation for the `file-dispatcher` event handler now includes
  details on variables available when defining the destination path. [#5604]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* For transfers executed using a temporary file name, the `destination_path`
  attribute of the events with ID 60012 now contains the temporary path. This
  is because the file is not yet renamed to the final destination path when
  the event is emitted. In previous versions, the attribute contained the final
  destination path. [client-side] [#5597]
* Specific support for Amazon Linux 2 and Red Hat Enterprise Linux 7.x
  (including derivatives such as CentOS and Oracle Linux) has been removed due
  to OpenSSL 1.0.2 no longer being supported by the upstream cryptography
  project. Use the supported generic x64 Linux package instead. [#5600]
* The `address` and `port` configuration options for the WebDAV client were
  removed, being replaced with the `url` option. Old configuration options
  are automatically migrated to use `url`. [client-side][webdav] [#5602]


Version 4.10.0, 2021-03-17
--------------------------


New Features
^^^^^^^^^^^^

* You can now configure a recursive transfer to automatically delete the source
  parent directory of a successfully transferred file. [client-side] [#2594]
* You can now configure a password history policy in SFTPPlus. [#5406]
* A new event handler was added to allow publishing audit events to a
  RabbitMQ AMQP 0-9-1 server. [#5554]
* SFTPPlus can now authenticate users using an external RADIUS server over
  the UDP protocol. [#5562]
* You can now configure the authentication for an account to require both a
  valid password and a valid SSH key. [server-side][sftp][scp] [#5573]


Defect Fixes
^^^^^^^^^^^^

* Paths containing single quotes are now correctly handled.
  In previous versions, single quote characters were replaced with
  path separators, invalidating path requests. [#5585]
* On Linux and macOS, the GPG external utility required by the OpenPGP event
  handler is now distributed together with SFTPPlus. [linux][macos] [#5584]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The Microsoft certificate revocation lists were removed from
  `${MICROSOFT_IT_CRL}` placeholder as they are no longer updated. [#5554]


Version 4.9.0, 2021-02-03
-------------------------


New Features
^^^^^^^^^^^^

* The SSL Certificate Authority configuration now supports validating partial
  CA chains. This allows for authenticating remote HTTPS connections through
  self-signed and self-issued certificates. Using a pinned non-CA certificate
  is also allowed. [#2198-1]
* The AS2 server can now respond to asynchronous AS2 MDNs. [server-side][as2]
  [#2198]
* You can now configure an account to receive files over AS2 without requiring
  a password. Files received over AS2 still need to be validated for
  signature and encryption. [server-side][as2] [#5490]
* HTTP connection requests to HTTPS services such as the Local Manager web
  administration interface or the HTTPS file transfer service are now
  automatically redirected to HTTPS. [server-side] [#5512]
* You can now configure a client-side transfer to operate on files using a
  temporary prefix. Previous versions only supported a temporary suffix.
  [client-side] [#5514]
* The SSH (SFTP/SCP) list of secure ciphers no longer contains CBC mode
  ciphers. They are no longer enabled by default, although still supported.
  You can still explicitly enable Cipher Block Chaining modes for
  aes256-cbc, aes192-cbc, and aes128-cbc using the
  `ssh_cipher_list` configuration. [sftp][scp] [#5529-1]
* The SFTP/SCP file transfer services and locations now support ECDSA SSH keys.
  Supported SSH key types are ecdsa-sha2-nistp256,
  ecdsa-sha2-nistp384, and ecdsa-sha2-nistp521.
  [sftp][server-side][client-side] [#5529]
* The SFTP/SCP file transfer services and locations now support
  Ed25519 SSH keys for system using OpenSSL version 1.1.1 or above.
  Supported SSH key type is ssh-ed25519.
  [sftp][server-side][client-side] [#5529]
* SSH host keys for SFTP/SCP server-side services are now configured using a
  single configuration option named `ssh_host_keys`. [server-side][sftp]
  [#5533]
* The Let's Encrypt root certificate authority certificates were updated to
  the list published by Let's Encrypt as of Jan 20, 2021.
  [#5542][lets-encrypt][security]


Defect Fixes
^^^^^^^^^^^^

* When transferring concurrent files through multiple transfers, the
  transfer queue is no longer stalled after the destination location is
  reconnected. [client-side] [#5519]
* Components listed on the Local Manager general status page are now sorted
  in alphabetical order. [manager] [#5537]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Following SSH ciphers are no longer supported: cast128-ctr, blowfish-ctr,
  and 3des-ctr. The CBC mode for these ciphers are still supported. [sftp]
  [#5529]
* The `rsa_private_key` and `dsa_private_key` configuration options were
  removed, being replaced by a single `ssh_host_keys` configuration option. For
  backward compatibility, the old configuration options are still supported.
  [server-side][sftp] [#5533]
* The SSH (SFTP/SCP) list of secure ciphers no longer contains CBC mode
  ciphers. Cipher Block Chaining modes aes256-cbc, aes192-cbc, and aes128-cbc
  were removed for potential security vulnerabilities. [sftp][scp] [#5529-1]


Version 4.8.0, 2020-11-19
-------------------------


New Features
^^^^^^^^^^^^

* The embedded OpenSSL libraries used on Windows, macOS, and generic Linux were
  updated to version 1.1.1h. [#5496]
* You can now configure an `overwrite` rule for the file dispatcher event
  handler. [#5510-1]
* You can now configure the file dispatcher event handler to copy a file
  using a temporary name and then rename it to the original name at the end
  of the transfer. [#5510]


Defect Fixes
^^^^^^^^^^^^

* The states for authentication methods are now correctly displayed in the Local
  Manager GUI. This regression was introduced in version 3.51.0. Since then,
  their states were always shown as disabled. [#5458]
* When a transfer is configured with a `stable_interval` value lower than the
  value of `changes_poll_interval`, the `stable_interval` value is ignored. The
  number of seconds used is 1 more than what is set for `changes_poll_interval`.
  [client-side][#5496]


Version 4.7.0, 2020-11-05
-------------------------


New Features
^^^^^^^^^^^^

* You can now configure the PGP and archive extraction event handlers
  using an event that has a list of files attached. [#5502]
* The PGP and extract archive event handlers can now be configured
  to overwrite an existing destination. [#5503]
* A new event handler was added to allow creating ZIP archives. [#5504]


Defect Fixes
^^^^^^^^^^^^

* A typo was fixed in the name of the configuration for `{day.of_year_padded}`.
  In previous versions it was defined as `day.of_year_paddedd`. [#5504]
* The SFTPPlus Windows Service manager was updated to no longer depend
  on the .NET framework.


Version 4.6.0, 2020-10-02
-------------------------


New Features
^^^^^^^^^^^^

* You can now configure a `file-dispatcher` event handler to retry the
  processing of a file. [#5302]
* The generic Linux package has been re-based on glibc version 2.5 to cover
  older distributions, including (but not limited to) Red Hat Enterprise Linux
  5.11. [#5453]
* You can now start the SysV init script and the OpenRC service file in debug
  mode using the "debug" option. [#5474]
* Running multiple concurrent SFTPPlus instances from the same installation
  path is now documented for all Linux init systems. A simplified SysV init
  script for running multiple concurrent instances from the same installation
  path has been added and documented. [#5477]
* You can now convert SSL files from PFX / P12 files to PEM format using the
  web management GUI. [#5489]


Defect Fixes
^^^^^^^^^^^^

* An internal error is no longer generated when the FTP command channels times
  out before the command channel. [server-side][ftp] [#5467-1]
* The ProxyProtocol v2 support now works with FTPS explicit and implicit
  protocols. In the previous version, the Proxy Protocol was only supported for
  FTP. [server-side][ftp] [#5467-2]
* A transfer no longer fails when the source detects a path with multiple
  operations on the same node id. [#5468-1]
* An internal error is no longer generated when starting an FTP service without
  allowing any authentication credential type. [ftp][ftps][server-side]
  [#5476-1]
* An internal error is no longer generated when starting an FTP service without
  a password-based authentication type. [ftp][server-side] [#5476-2]
* When failing to allocate a new passive port, the error message now contains
  the error details provided by the operating system. [ftp][ftps][server-side]
  [#5476]
* When failing to read the configuration file at startup, an error is now
  visible. [#5479]
* A security issue was fixed where SFTPPlus was not checking if the remote peer
  has a copy of the private key when using the HTTP authentication method
  together with SSH key authentication. This security issue only affects SSH key
  authentication when using the external HTTP authentication method. This does
  not affect the SSH key authentication when using the embedded SFTPPlus
  credentials validation. [server-side][sftp][scp][security] [#5480]
* Local Manager's user interface for the OS authentication method was updated
  to inform that all OS accounts are denied access when no OS group is
  configured. [server-side] [#5483]
* An internal error is no longer raised when trying to directly access the HTTP
  service login URL while already authenticated. [server-side][http][https]
  [#5487]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with ID 50012 emitted by the Local Manager web interface was removed.
  It was replaced by the generic event with ID 50003, which is raised when
  failing to apply a configuration change request. [local-manager] [#5476-1]
* Event with ID 20041 was removed as it is now redundant and never emitted.
  [server-side] [#5476-2]
* The events with ID 10017 and 10018, emitted by the FTP service for an invalid
  configuration, were removed and replaced by the generic event ID 20158,
  emitted when a service fails to start. [ftp][ftps][server-side] [#5476]
* Events with ID 30069 and 30070 were removed and replaced with the event ID
  30007, which is emitted for any error occurred during the SSH authentication
  protocol. [server-side][sftp][scp] [#5480]
* Event with ID 50024 was removed and replaced by ID 50023, which is emitted
  when an administrator request fails via the web-based GUI. [#5489]


Version 4.5.0, 2020-09-04
-------------------------


New Features
^^^^^^^^^^^^

* The HTTP/HTTPS file transfer services can now receive files using the
  Applicability Statement 2 (AS2) protocol.
  [server-side][http][https]. [#4568][#1059][#1308]
* You can now configure a transfer to send files to a remote AS2 location.
  [client-side][http][https][as2] [#221]
* You can now configure virtual folders directly into the account
  configuration. In previous versions, virtual folders could only be configured
  at the group level for SFTPPlus embedded accounts. [server-side] [#5460]
* You can now configure whether an HTTP authentication method will validate or
  not its URL configuration at startup. [server-side] [#5466]
* The file transfer service can now handle new connections made using the Proxy
  Protocol version 2. This is done automatically without any extra
  configuration. [server-side][ftp][ftps][sftp][scp] [#5467]
* The data for the emitted events now contains the filename and directory name
  as separate members for the associated file. [#5469]
* When creating a matching expression based on globbing rules,
  you can now use the exclamation mark to reverse the meaning of the
  expression. This can be used to define exclusion rules.
  [#5473]


Defect Fixes
^^^^^^^^^^^^

* An internal error is no longer raised when the FTP server is in debug mode
  and receives commands with non-ASCII values. [server-side][ftp] [#5467]
* A transfer no longer fails when the source detects 2 paths created at the
  same time for the same node id. [#5468]


Version 4.4.0, 2020-08-07
-------------------------


New Features
^^^^^^^^^^^^

* You can now define filtering expressions based on current date and time.
  [#5450]
* You can now configure extra HTTP headers to be sent with the requests made by
  the HTTP Authentication method. [server-side] [#5456]


Defect Fixes
^^^^^^^^^^^^

* If, during a file transfer, the source or destination locations are no longer
  available, the transfer is now paused and only resumed (automatically) once
  the locations are available again. [client-side] [#5443]
* When the destination location for a transfer is not available, the files
  found in the source are queued to be transferred as soon as the
  location is available again. In previous versions, a manual restart of the
  transfer was required to transfer the queued files. [client-side] [#5444]
* You can now use virtual directories together with the SFTP protocol. Due to a
  defect, in previous versions the virtual directories were only available via
  the FTP/FTPS and HTTP/HTTPS protocols. [server-side][sftp] [#5457]


Version 4.3.0, 2020-07-21
-------------------------


New Features
^^^^^^^^^^^^

* You can now generate a self-signed certificate using the `admin-command`
  command line tool. [#239]
* You can now configure the URL suffix used for the HTTP/HTTPS public access.
  [server-side][http][https] [#2586]
* SFTPPlus can now use unencrypted OpenSSH RSA or DSA private keys stored as
  the openssh-key-v1 format. [sftp][scp] [#5435-1]
* Alpine Linux 3.12 on x86_64 is now a supported platform. [#5435] [#5435]
* The event with ID 50005 emitted when a configuration change is requested from
  the Local Manager now includes the UUID of the newly created component.
  [local-manager] [#5439]
* Red Hat Enterprise Linux 5 was added as a platform with limited support.
  RHEL 5's Extended Life Cycle Support (ELS) ends on November 30, 2020.
  Contact us if you need to run SFTPPlus on RHEL 5 in production. [#5448]


Defect Fixes
^^^^^^^^^^^^

* You can now use SFTPPlus on localized Windows versions. In previous
  versions, SFTPPlus was only working with English as main language.
  [windows] [#1446]
* You can now run SFTPPlus on Linux from an installation path containing
  Unicode characters outside of the ASCII range. [linux] [#2074]
* Redirecting to directory paths containing non-ASCII characters no longer
  generates an internal server error. [server-side][http][https] [#2586]
* When a file scheduled to be transferred is removed from source, transfer
  attempts will no longer occur for it. [client-side] [#3796-1]
* When a file scheduled to be transferred is modified while waiting in the
  queue, transfer attempts will no longer occur for it. [client-side] [#3796]
* When a transfer is manually stopped, pending retry attempts are canceled.
  In previous versions, the transfer of the latest file was still retried.
  [client-side] [#5390]
* To reduce temporary memory allocations for running external processes, they
  are now executed by a dedicated process. [#5407]
* Waiting for a file to be retried will not block the other files queued for
  the transfer. [client-side] [#5436]
* A transfer is no longer retried and fails right away if the source file no
  longer exists on the source location. [client-side] [#5438]
* Microsoft Certificate Authority root certificates were updated to include
  the new `DigiCert SHA2 Secure Server CA` used for Microsoft's login page.
  [client-side][sharepoint]. [#855]
* The SysV init script properly manages the SFTPPlus daemon process again.
  This regression was introduced in version 4.2.0. [linux][#5446]
* Self-signed certificates automatically created when initializing
  configuration are no longer created with `Version 3`.
  This fixes an error raised by latest Chrome-based browsers which resulted
  in rejecting HTTPS connections using these certificates. [https][#5446]


Version 4.2.0, 2020-06-17
-------------------------


New Features
^^^^^^^^^^^^

* The HTTP Post event handler can now be configured to send a set of custom
  headers. [#3778-1]
* The event emitted when a file is closed for an FTP/FTPS server-side connection
  now contains the overall transfer speed of that file.
  [server-side][ftp][ftps] [#3778-2]
* You can now send HTTP POST events using a custom format. [#3778]
* You can now configure a delay for the execution of the dispatch-file event
  handler and the execution is ignored if the targeted file no longer exists
  after the delay. [#814]


Defect Fixes
^^^^^^^^^^^^

* When copying local files using the file-dispatcher event handler,
  the copies are now created without keeping the source file's attributes. This
  prevents creating extra file versions on a versioned filesystem. [#2042]


Version 4.1.0, 2020-06-11
-------------------------


New Features
^^^^^^^^^^^^

* The LDAP authentication method now provides the option to construct the home
  folder path based on an LDAP attribute and a template. [server-side]
  [#1863-1]
* You can now configure a default domain for LDAP users when used together with
  an Active Directory server. [server-side] [#1863]
* The HTTP Request event handler can now send an event as an XML SOAP message or
  as a generic XML document. [#1973]
* The SFTPPlus instance name is now visible in the Local Manager web-based
  administration console. [#5296]
* You can now test the configuration of the email sender resource. [#5405-1]
* You can now define a default list of email recipients used for sending email
  when there is no explicit configuration. [#5405-2]
* You can now configure the SSL/TLS details for the email resource.
  [smtp][email] [#5405]
* Destination path for a file dispatcher can now be defined based on
  extra event attributes other than the source path. [#55]
* You can now configure multiple remote SSH/SFTP server identities for an SFTP
  location. This can be used for connecting to a disaster recovery server which
  uses a separate SSH identity. [client-side][sftp] [#135]


Defect Fixes
^^^^^^^^^^^^

* Firefox auto-completion no longer applies to the `ssl_domain` field for
  various services and the `username` and `password` values for email
  resources. [#1792]
* The link for changing passwords is no longer visible for accounts
  authenticated using X.509 TLS/SSL certificates. [server-side][https] [#2828]
* The email client resource now works with email servers over TLS 1.2. In
  previous versions, it was only working over older TLS versions. [#5404]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* OS accounts are no longer supported on Apple macOS. [server-side] [#3135]
* The `install-service` option was removed from the `admin-command.bat` command
  line tool. There is now a dedicated command named `sftpplus-service.exe`
  for managing the SFTPPlus Windows service. [windows] [#3878]
* The legacy WebAdmin authentication method is no longer supported. If you are
  still using the SFTPPlus PHP Webadmin authentication, you can use the generic
  HTTP authentication method together with PHP WebAdmin version 1.11.0 or
  newer. [server-side] [#425]
* The OS authentication method now requires explicit configuration for the
  allowed list of operating system groups. In previous versions, when the
  "allowed_groups" was not defined, the OS authentication was allowing users
  from any OS group. [security] [#4972]


Version 4.0.0, 2020-05-19
-------------------------


New Features
^^^^^^^^^^^^

* There is now an admin-shell command line interface that can be used to manage
  and configure the SFTPPlus process from the command line. It is the CLI
  equivalent of the Local Manager web-based GUI console. [#1158]
* The `openpgp` event handler was added for encrypting and decrypting files
  using OpenPGP. [#1177]
* You can now use SSL/TLS certificates to authenticate users against the HTTPS
  file transfer service. [server-side] [#143]
* You can now send credentials for an account via email. [#1468]
* You can now create PGP keys from the Local Manager web interface or the
  command line administrative tool. [#1591]
* SFTPPlus administration accounts now support multi-factor authentication
  based on the TOTP standard. [#2000]
* Two-factor authentication can be enabled for user accounts defined inside the
  SFTPPlus configuration. [#2401]
* Logged date and time can now be formatted using ISO-8601 UTC, ISO 6501 UTC
  with fractional seconds, or ISO-8601 with local time. [#2919]
* The OpenPGP event handler can now encrypt/decrypt files using asymmetric PGP
  keys. [#3797]
* It is now possible to create a new Certificate Signing Request (CSR) using an
  existing private key. [local-manager] [#3806]
* The Python extension event handlers can now be set up with a custom
  JSON-based configuration string. [#3921]
* You can now disable the overwriting rule for a transfer destination. In this
  way, the file is uploaded right away, without doing any extra requests on the
  server. [client-side] [#4054-1]
* Details of files transferred in the past (name, size, modified timestamp) can
  now be recorded to prevent transferring the exact same file more than once.
  [client-side] [#4369]
* The `extract-archive` event handler now also supports extracting TAR, TAR.GZ,
  and TAR.BZ2 archives. [#495]
* You can now configure the application authentication method to only accept
  members of selected groups. [server-side] [#4963]
* Recursive transfers can now automatically create destination folders.
  [client-side] [#5004]
* The SFTPPlus initialization command now also asks for initializing a custom
  administration password. With this change, Local Manager is now accessible by
  default for any IP source. [#5193]
* Product version is no longer advertised during protocol handshake for FTP,
  SSH and HTTP. [#5222]
* There is now a dedicated documentation page for macOS installations. [#5297]
* SFTPPlus now uses by default the SHA-512 function for hashing passwords. The
  hash function is now configurable, following options are available: SHA-256,
  SHA-512, PBKDF2 SHA-256, PBKDF2 SHA-512. In previous versions, only SHA-256
  was used. [server-side] [#5322]
* Accounts names, administrator names, and passwords longer than 150 characters
  are no longer allowed. Passwords longer than 128 characters are no longer
  generated. [server-side] [#5333]
* The `extract-archive` event handler now supports extracting ZIP files.
  [#5346]
* For the `monitor` service, you can now configure the type of file operations
  for which to emit events. [#5347-1]
* The local filesystem monitor service now has a new configuration option named
  `file_age_notification`. This was introduced to replace the
  `warn_non_modified_files_interval` configuration. [#5347-2]
* The `monitor` service can now automatically delete old files. [#5347]
* A new option, `delete_source_on_success`. is available for a transfer to
  configure if the file should be removed from the source directory after a
  successful transfer. [client-side] [#5393]
* You can now archive files using a recursive folder structure. [client-side]
  [#5394]
* The `process-monitor` resource was renamed as the `analytics` resource. It
  now monitors date, time, and source IP of successful authentications. [#64]
* SFTPPlus now provides an embedded self-signed certificate which can be used
  as a starting point for configuring TLS-based services such as FTPS and
  HTTPS. This self-signed certificate is automatically used for these services
  if the `ssl_certificate` configuration option is empty. [server-side] [#723]
* An account can now be configured to read authorized public SSH keys from any
  file found in a specified directory path. [server-side][scp][sftp] [#972]


Defect Fixes
^^^^^^^^^^^^

* On non-Windows systems, the `extract-archive` event handler can now handle
  paths with uppercase characters. In previous versions, it was always using
  lowercase characters for the destination's filename. [#1177]
* The Windows start menu shortcut to the Local Manager page now works even when
  the Local Manager is configured for the `0.0.0.0` IP address. [#3030]
* The PID file created when SFTPPlus starts in service/daemon mode is no longer
  readable by other system users. [linux][security] [#4402]
* The SysV and OpenRC init scripts now work when SFTPPlus is started as `root`.
  This was a defect introduced in 3.42.0. [#4686]
* The event with id 60005, emitted when failing to monitor the source path of a
  transfer, now contains the exact path which triggered the failure. In previous
  versions, it was only containing the base source path of the transfer.
  [client-side] [#5004]
* A dedicated event is emitted when a service has no authenticated method.
  [server-side] [#5053]
* The SFTP file transfer service now has improved performance for directory
  listing when a large number of files are present. [server-side][sftp] [#57]
* You will now receive an error at service start if the configured SSH
  RSA or DSA keys are of an invalid type. [server-side][scp][sftp] [#723]
* There is now a limit of 100kB for the file containing authorized public SSH
  keys for an account. [security][sftp][scp][server-side] [#972]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with ID 20078, used to signal that a service was stopped, was removed
  and replaced by event with ID 20157, used when any component is stopped.
  [#1158-1]
* Event with ID 20045, used to signal that a service failed to stop, was removed
  and replaced by events with IDs 20159 and 20185, used when any
  component fails to stop. [#1158-2]
* Event with ID 20077, used to signal that a service failed to start, was
  removed and replaced by event with ID 20158, used when any component fails to
  start. [#1158-3]
* Event with ID 20076, used to signal that a service was successfully started,
  was removed and replaced by event with ID 20156, used when any
  component is successfully started. [#1158]
* The 'Account activity' event handler now only works with the embedded
  standard SQLite database. Support for MySQL databases and custom SQLite
  databases was removed. [#1376]
* Event with ID `20101`, emitted when the configured password is invalid, was
  removed. It was replaced with event with ID `20142`, emitted when
  authentication fails. [server-side] [#2000]
* `./bin/admin-command.sh --start` is no longer supported. Use
  ``./bin/admin-command.sh start`` instead. [linux][macos] [#2783]
* The `address`, `port`, and `path` configuration options were removed from the
  Syslog event handler. They are replaced by the single `url` configuration
  option. [#2914]
* Default format used to store log entries was changed to show date and time
  first. Upgrading existing installations will not automatically switch to the
  new logging format. [#2919]
* Event with ID 20089, raised when trying to delete the default group, was
  removed and replaced with the generic event 20108, raised when trying to
  delete a component which is already in use. [#316-1]
* Only one email client resource is now supported. This is the resource with
  UUID `DEFAULT-EMAIL-CLIENT`. Any other email client resource is ignored.
  [#316-2]
* The `email_client_resource` configuration option was removed from the
  `email-sender` event handler. Emails are now sent using the default email
  client. [#316-3]
* Event with ID 20063, raised when the default group is missing, was removed as
  SFTPPlus will automatically create the default group if missing. [#316-4]
* Event with ID 50020, raised when SFTPPlus Local Manager failed to start a
  database, was removed and replaced by ID 20112. [#316-5]
* The `Past Activity` page in the Local Manager web console was renamed to
  `Activity log`. [#316-6]
* Event with ID 20163, emitted by SFTPPlus when failing to record the date and
  time when an account was successfully authenticated, was removed and replaced
  with the generic ID 20174. [#316-7]
* Event with ID 20116, raised when failing to create a DB table database, was
  removed and replaced by ID 20112. [#316-8]
* The database event handlers no longer use a separate database configuration.
  Each database event handler has now its own database file. [#3168-1]
* SFTPPlus no longer supports MySQL databases. If you need to send events to a
  MySQL database, please get in touch with our support. [#3168-2]
* Events with IDs 20161, 20162, 20164 were removed and replaced by
  ID 20112, used for all database errors. [#3168-3]
* Events with ID 20112 and 20117, emitted when a DB operation fails, were
  removed. They were replaced with specific event ID errors for
  each SFTPPlus component using the DB. [#3168-4]
* Events with IDs 50019, 50021, 50022, 50025, emitted when a Local Manager DB
  operation fails, were removed. They were replaced with specific event ID
  errors for each Local Manager operation using the DB. [#3168-5]
* Support for the MySQL database event handler was removed. [#3168]
* Event with ID 20160 was removed and replaced with the generic event 20165
  raised when a component fails. [db] [#316]
* The `%(event_id)s` variable for the `email_subject` configuration was
  removed, after being deprecated in 3.16.0. It should be replaced by the
  `{id}` variable. [#3655]
* The `amend-content` event handler was removed and replaced by the
  `python:chevah.server.extension.amend_content.RemoveLastLine` extension event
  handler. [#3921]
* The `digital-signature-validation` event handler was removed and replaced by
  the `python:chevah.server.extension.digital_signature.ValidateCSV_RSASSA_PSS`
  extension event handler. [#3956]
* The `rotate_each` configuration option from the `local-file` event handler
  was removed and replaced with `rotate_on`. Existing `rotate_each`
  configuration are interpreted as `rotate_on: 00:00 time-of-day`. [#4351]
* TEST_DELAY_EXECUTION is no longer supported. [server-side][sftp] [#4976]
* Passwords stored in plain text are no longer supported. [security] [#5154]
* Events with IDs 10029, 10058, 10060, 10067, emitted by the FTP server, were
  removed. They were replaced with generic events. [server-side][ftp][ftps]
  [#5155]
* The `configuration/ssh-service.moduli` file is no longer used by the SFTP and
  SCP services. SFTPPlus now has an embedded list of SSH moduli, refreshed
  every release. [server-side][sftp][scp] [#5222]
* Red Hat Enterprise Linux 6 (RHEL 6) is no longer supported in SFTPPlus
  version 4.0.0. You can continue to use latest SFTPPlus 3.x.x version with
  RHEL 6. [#5261-1]
* Ubuntu Server 16.04 is no longer supported in SFTPPlus version 4.0.0.
  You can continue to use latest SFTPPlus version 3.x.x with this version of
  Ubuntu Server. [#5261-2]
* Apple OS X 10.8 and newer Mac OS X versions up to and including macOS 10.12
  are no longer supported in SFTPPlus version 4.0.0. You can continue to use
  latest SFTPPlus version 3.x.x for these systems. Only macOS 10.13 and
  newer versions are supported in SFTPPlus version 4.0.0. [#5261-4]
* The following Unix operating systems are no longer supported starting with
  SFTPPlus version 4.0.0: AIX, HP-UX, Solaris. You can continue to use SFTPPlus
  version 3.x.x on these operating systems. [#5261]
* The `permission` configuration option for an account will now have `inherit`
  as the default value. In previous versions, it was set to
  `allow-full-control`. The default configuration for a group is still
  `allow-full-control`. [server-side][security] [#5339]
* `warn_non_modified_files_interval` configuration option of the monitor
  service was removed and replaced with a new configuration option named
  `file_age_notification`. For backward compatibility, SFTPPlus can still read
  the configuration stored in `warn_non_modified_files_interval`, but it
  rewrites it as `file_age_notification`. [#5347]
* The `type` configuration option for transfers was removed. It was replaced
  by the `delete_source_on_success` option. [#5393]
* The `execute_at_startup` configuration option and functionality was removed.
  You can use the `external-executable` event handler to execute external
  scripts. Event with ID `20181` is emitted each time the SFTPPlus process
  starts. [#5413]
* The `account-activity` event handler was removed. It was replaced by the
  `process-monitor` resource. [#64]
* Event with ID 20182, emitted when an account is authenticated, was removed.
  Only the event with ID 20137 is now emitted on successful authentication.
  [#888-1]
* Event with ID 20023, emitted when failing to read the file containing the
  authorized SSH keys for an account, was removed. It was replaced by the
  generic event with ID 20142. [#888-2]
* Event with ID 50007, emitted when an administrator was successfully
  authenticated, was removed. It is replaced by the generic event with ID 20137.
  [#888]


Version 3.55.0, 2020-04-28
--------------------------

This release includes a critical security issue for the
Local Manager's web console GUI introduced with SFTPPlus version 3.24.0.

The vulnerability is a local one if Local Manager only accepts
local connections, as configured by default.

Your SFTPPlus setup is not affected if you are not using
the default-enabled "Store in database" event handler.

In order to audit for potential security breaches, parse the log files for
events with ID 50026 and check them for any unauthorized access.
Unfortunately, you can only identify unauthorized access by its timestamp.

No user data or passwords can be compromised this way.
The usernames and file names are found in the logs and can be exposed to
unauthorized parties.

To fix this security issue, you need to upgrade SFTPPlus to version 3.55.0.

If you can't upgrade right away, you should harden the configuration
by deleting the "Store in database" event handlers.
If you would rather keep using this feature without updating,
make sure the Local Manager is only available through secured channels
such as a VPN tunnel.


New Features
^^^^^^^^^^^^

* Ubuntu 20.04 on x86_64 is now a supported platform. [#1512]
* The "Download as CSV" functionality from the Activity Log will now download
  only the entries selected by the active filters. [#4233]
* The embedded OpenSSL libraries on Windows, generic Linux, and macOS were
  updated to version 1.1.1g. [#5400]
* Red Hat Entreprise Linux 8 on X86_64 is now a supported platform. [#5324]
* The bundled OpenSSL libraries on Windows, SLES 11,
  and generic Linux distributions were updated to version 1.1.1g. [#5357]


Defect Fixes
^^^^^^^^^^^^

* The "Download as CSV" link from the Local Manager no longer allows
  unauthenticated requests. [security][web-manager] [#4233]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The macOS package no longer depends on the system-included LibreSSL
  libraries. On macOS, SFTPPlus now uses embedded OpenSSL libraries. [#5400]
* On SLES 11, RHEL 6, and other unsupported Linux distributions,
  SFTPPlus uses a generic glibc-based Linux runtime which includes
  OpenSSL 1.1.1 libraries. [#5312]


Version 3.54.0, 2020-04-21
--------------------------


New Features
^^^^^^^^^^^^

* You can now define custom triggers for the HTTP / HTTPS service. These
  triggers are available as buttons in the web client GUI and as custom actions
  in the HTTP API. [server-side][http][https] [#3832]
* You can now configure the SFTPPlus Let's Encrypt resource with email
  addresses as contact information to be submitted to the ACME server.
  [#5351-1]
* SFTPPlus now supports the Let's Encrypt ACME v2 protocol. [#5351]
* 64bit packages for Windows x64 were added. [#5376]


Defect Fixes
^^^^^^^^^^^^

* You can now define the password when creating a new account. This was a
  defect introduced in a previous version. [#5379]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Let's Encrypt ACME v1 protocol is no longer supported. You will need to
  manually update your configuration to use an ACME v2 server. For example, you
  can use: https://acme-v02.api.letsencrypt.org/directory. If
  you were using the Let's Encrypt V1 server at
  https://acme-v1.api.letsencrypt.org/directory, it will be automatically
  upgraded to https://acme-v02.api.letsencrypt.org/directory. [#5351]


Version 3.53.0, 2020-01-17
--------------------------


New Features
^^^^^^^^^^^^

* A new option was defined for the `overwrite_rule` configuration to allow the
  file to be skipped and not transferred when destination already has a file
  with the same name. [client-side][sync] [#4709]
* The bundled OpenSSL libraries in Windows, Generic Linux, and OS X,
  were updated to version 1.1.1d. [#5348]


Defect Fixes
^^^^^^^^^^^^

* SFTPPlus can now successfully push large files over SFTP even if the remote
  SFTP server is not accepting large file chunks. This affected large file
  transfers to servers such as Microsoft's OpenSSH For Windows Server.
  [sftp][client-side] [#5367]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Support for Debian Linux 9 on X86_64 was removed. Please use the generic
  Linux package on any Debian Linux version. [#5373]


Version 3.52.0, 2019-12-17
--------------------------


New Features
^^^^^^^^^^^^

* A new HTTP redirect service is available to help redirect HTTP requests to
  an HTTPS file transfer service. [server-side][http] [#5352]
* You can now configure a redirection URL for any requests made to the Let's
  Encrypt resource HTTP service that do not match ACME validation requests.
  This can be used to combine the functionality of the HTTP to HTTPS
  redirection service with that of the Let's Encrypt client validator.
  [#5352-1]
* The FTP/FTPS client will ignore the IP address returned by the server's PASV
  command, always using the same IP address for both the control and data
  channels. [client-side][ftp][ftps] [#5362]


Defect Fixes
^^^^^^^^^^^^

* Let's Encrypt resource will now highlight in the Local Manager that a restart
  is required after changing the address and port configuration. [server-side]
  [#5352]
* When upgrading, the existing Windows service is no longer reset and the
  configured Windows service account is kept between installations. This defect
  was introduced in SFTPPlus 3.50.0. [windows] [#5358]


Version 3.51.0, 2019-11-05
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to configure HTTP POST event handlers and HTTP
  authentication methods with multiple URLs which will act as a fallback.
  [#1788]
* You can now configure file transfers to ignore source files older than a
  certain time. [client-side] [#5081]
* SFTP and SCP protocols now support the hmac-sha2-512 MAC algorithm.
  [sftp][scp] [#5313-1]
* SFTP and SCP protocols now support diffie-hellman-group14-sha256,
  diffie-hellman-group15-sha512, diffie-hellman-group16-sha512,
  diffie-hellman-group18-sha512, and diffie-hellman-group18-sha512 key exchange
  algorithms as required by RFC-8268. [sftp][scp] [#5313]
* You can now configure a retention period for the archived files of a
  transfer. Older files from the archive folder will be automatically removed
  by SFTPPlus. [client-side] [#5314]
* The SFTPPlus globbing expressions now support defining multiple patterns in a
  logical disjunction expression `OR` using the vertical bar character `|`.
  [#5316]
* Remote SSH server's fingerprint can now also be defined as SHA1, SHA256,
  an SSH public key, or an X.509 SSL/TLS certificate. MD5 fingerprints are
  still supported. [client-side][sftp] [#5327-1]
* When configuring a new account from the Local Manager web console,
  `permission` and other configuration options are set by default to inherit
  from group configuration. [server-side] [#5340]
* Alpine Linux 3.10 on X86_64 is now a supported platform. [#5282]
* On macOS 10.13 and newer, the OpenSSL 1.0.2 libraries from Homebrew
  are no longer required. [#5243]
* For old Linux distributions with unsupported system OpenSSL versions,
  SFTPPlus is statically-linked against OpenSSL 1.1.1 libraries.
  This version of SFTPPlus is distributed as the "Generic Linux" version.
  The Generic Linux version also runs on unsupported Linux distributions,
  provided they are based on glibc/eglibc version 2.11 or newer. [#5312]
* The bundled OpenSSL libraries in Windows, Generic Linux, and OS X,
  were updated to version 1.1.1c. [#5286]


Defect Fixes
^^^^^^^^^^^^

* The `ignore_create_permissions` configuration option will now also ignore
  setting attributes when a file is created. In previous versions,
  attributes were ignored only for folders. [server-side][sftp] [#1741]
* The HTTP CONNECT proxy now works with HTTP endpoints. In previous
  versions, it was only working with HTTPS endpoints. [#1788]
* Transfers with a WebDAV location as source no longer fail when the WebDAV
  server returns a "302 FOUND" response. The response is now ignored and
  considered a transient error. [client-side][webdav][sharepoint]
  [#5300], [#5309]
* File dispatcher event handler can now handle events with more than 2
  associated paths. In previous versions, only the first and the last paths for
  an event were handled. [#5317-1]
* The value for the `paths` attribute from the event with ID `60017` is now a
  plain text value. The new `success_list` attribute was added to access the
  raw list value. The values for `failed_paths` and `success_paths` for ID
  60016 are now plain text values. `failed_list` and `success_list` attributes
  were added to access raw list values. In previous versions, these attributes
  were used in an internal list which was not available for pattern matching.
  [client-side] [#5317]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `ssh_server_fingerprint` configuration option was replaced by a new
  `ssh_server_identity` option in new configurations.
  The `ssh_server_fingerprint` option is still accepted for backward
  compatibility with older configurations. [client-side][sftp] [#5327]
* Support for Alpine Linux 3.7 on X86_64 was removed. [#5282]
* Support for Ubuntu Linux 14.04 LTS on X86_64 was removed. Please try the
  generic Linux package if you still use this version of Ubuntu Linux. [#5312]


Version 3.50.0, 2019-07-24
--------------------------


New Features
^^^^^^^^^^^^

* The embedded Let's Encrypt client now has the option to debug the HTTP ACME
  protocol. [#5287]
* It is now possible to install multiple SFTPPlus instances on the same Windows
  system, all operating and active at the same time. [#5291]


Defect Fixes
^^^^^^^^^^^^

* The embedded Let's Encrypt client can now successfully request certificates.
  Version 3.48.0 introduced a defect which prevented requesting new
  certificates. [lets-encrypt] [#5287]


Version 3.49.0, 2019-06-24
--------------------------


New Features
^^^^^^^^^^^^

* You can now use PXF / PKCS#12 certificates in SFTPPlus without converting
  them to the PEM format first. [#2596]
* The HTTP file transfer server web UI now has dedicated ID for each UI element
  making it easier to implement themes. [web-server][http][https] [#3224]


Defect Fixes
^^^^^^^^^^^^

* Documentation for the group's `ssh_authorized_keys_path` configuration
  option was updated to specify that reading multiple SSH keys from a single
  file is not supported. This implementation change was done in version 2.6.0,
  but the documentation was not updated until now. [server-side] [#1296]
* FTP client transfers no longer create empty files on transfer failures.
  [client-side][ftp][ftps] [#3006]
* You can now create new SFTP services from the Local Manager web interface.
  This issue was introduced in version 3.46.0. [server-side][sftp] [#4124]
* When using the client shell, passwords are now masked by default.
  [security][client-side] [#5213]
* Local Manager's web interface now has an explicit button for disabling a
  password. In previous versions it was required to type `disabled` to disable
  the usage of a password. [manager] [#5236]


Version 3.48.0, 2019-05-27
--------------------------


New Features
^^^^^^^^^^^^

* HTTP POST event handler can now be configured
  to automatically retry on network and HTTP errors. [server-side][http-api]
  [#2619]
* It is now possible to configure a file transfer service to emit debugging
  events for the low-level protocol used.
  [http][ftp][ftps][sftp][scp][server-side] [#2697]
* The Python Extension event handler now handles events on multiple CPUs.
  In previous versions all events were handled by a single CPU. [#5262]
* A new destination path action named `single-file` was added to transfer
  multiple source files as a single destination file. [client-side] [#4054]
* You can now disable the overwriting rule for a transfer destination.
  In this way, the file is uploaded right away, without doing any extra
  requests on the server. [client-side] [#4054]
* Debian 9 is now a supported platform. [#3353]


Defect Fixes
^^^^^^^^^^^^

* When changing the current folder in FTP, the SFTPPlus server now only checks
  that the path is a folder and that path traversal is allowed. It no longer
  tries to see if the operating system allows listing content. Asking the
  operating system to list content for every target directory could have
  caused performance issues. [server-side][ftp][ftps] [#2111]
* You can now use a local directory with a large number of files
  (more than 10.000), as the source for a transfer.
  [client-side] [#1319]
* The local filesystem source location no longer stops to monitor the source
  on I/O errors. It will log an error and retry to get the content again after
  `changes_poll_interval` seconds. [client-side] [#3350]
* The SysV and OpenRC init scripts now work when executed as `root` user.
  This was a defect introduced in 3.42.0. [#3353]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The Python Extension event handler no longer takes a parent argument. The
  events are no longer handled in separate threads. Instead, they are added to a
  queue to be executed on a dedicate CPU. [#5262]
* Support for Ubuntu 16.04 on ARM64 was removed. [#3353]
* Support for Debian 8 was removed. [#3353]


Version 3.47.0, 2019-04-11
--------------------------


New Features
^^^^^^^^^^^^

* You can now configure multiple domains for a free Let's Encrypt certificate
  using the subjectAlternativeName field. [server-side][ftps][https] [#5108]
* A new event handler of type `external-executable` was added to execute
  external scripts or programs. [#5234]
* Windows Server 2019 is now a supported platform. [#5241-1]
* The bundled OpenSSL libraries in Windows, SLES 11, and OS X were updated to
  versions 1.1.1b, adding support for TLS 1.3. [#5241]


Defect Fixes
^^^^^^^^^^^^

* The WebDAV location now ignores HTTP proxy errors when they occur while
  monitoring a remote SharePoint Online site. [client-side][https] [#5114-1]
* The WebDAV location now works with multiple parallel transfers from the same
  SharePoint Online source. [client-side][https] [#5114]
* The SFTP and SCP file transfer services will no longer block the whole
  SFTPPlus process during the SSH handshake. [server-side][sftp][scp] [#5202]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with ID 20057, emitted when `execute_at_startup` times out, was removed
  and replaced by event with ID 20056. [#5234]


Version 3.46.0, 2019-03-11
--------------------------


New Features
^^^^^^^^^^^^

* The HTTP/HTTPS file transfer service now supports downloading multiple files
  at once as a Zip file. [server-side][web-api][http][https] [#5093]
* It is now possible to set up password expiration for accounts and groups.
  [server-side][security] [#5146]
* It is now possible to configure the preferred size of the group in the SSH
  Diffie-Hellman group key exchange method. [server-side][sftp][scp] [#5205]
* The file dispatcher event handler now supports the `copy` action. This will
  copy the source file to one or more destinations without removing the
  source file. [server-side][client-side] [#5210]
* The file dispatcher event handler now supports the `rename` action. This will
  rename the source file (with an atomic move operation) without overwriting
  an existing file. [server-side][client-side] [#5220]


Defect Fixes
^^^^^^^^^^^^

* An event is now emitted when a file is closed after it was open for reading
  through the HTTP file transfer service. [server-side][http][https] [#5093]
* The HTTP/HTTPS file transfer service now responds with `401 Unauthorized` for
  requests made with `100 Continue` when no credentials are provided in the
  request. [server-side][http][https] [#5223]


Version 3.45.0, 2019-02-13
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible for SFTP/SCP clients to change their own password using
  the SSH command execution service. [server-side][sftp][scp] [#5129]
* It is now possible to transfer files using temporary names, renaming to their
  initial names once successfully transferred. [client-side] [#5156]
* Events emitted when a file is closed after a server-side SFTP or SCP transfer
  now include transferred size, duration, and average speed.
  [server-side][scp][sftp] [#5196]
* You can now configure an account to allow authentication only from a specific
  list of source IP addresses. [server-side][security] [#5201]


Defect Fixes
^^^^^^^^^^^^

* The SFTP/SCP file transfer service no longer generates an internal server
  error when the SCP protocol is requested as an SSH subsystem.
  [server-side][scp] [#5129]
* For move transfers, the removal of the source file is now retried when the
  operation fails. In previous versions, once the file was transferred, the
  source removal was attempted only once. [client-side] [#5156-1]
* The transfer of a file is now retried when the operation to check the
  existence of the remote file fails. [client-side] [#5156]
* For the SCP protocol, the event with ID 30042 is no longer emitted when the
  client is sending the whole file without an end of file marker. In previous
  versions, if the SCP client uploaded all the file data, but did not send the
  explicit confirmation for the end of file or stream, SFTPPlus was emitting
  the event 30042 to inform that the transfer was not complete.
  [server-side][scp] [#5196]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The events emitted for rename operations now have the destination path as the
  default `path` attribute. In previous versions the source path was used. The
  `from` attribute will contain the source path. The following event IDs are
  affected: 60043, 60044, 30025, 30026, 30027 [server-side][client-side]
  [#5156]
* Support for FreeBSD 10.x on X86_64 was removed. [#5170]


Version 3.44.0, 2019-01-25
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to configure the name associated to the sender email
  address in the email client resource. [#3069]
* It is now possible for file transfer users to change the password associated
  with their accounts via the HTTP / HTTPS protocols.
  [server-side][http][https] [#5128]
* It is now possible to configure an email sender event handler with CC and BCC
  fields. [#5158]
* It is now possible to monitor OS resources used by SFTPPlus, and trigger an
  event when their usage hits certain configurable limits. These features
  are not available on HP-UX, Windows XP, Windows Server 2003, and AIX. [#5175]
* Alpine Linux 3.7 on X86_64 is now a supported platform. [#5179]
* It is now possible to schedule a transfer based on week days.
  [client-side][#5184]


Defect Fixes
^^^^^^^^^^^^

* The HTTP/HTTPS file transfer service login page is now accessible in HTML
  format for Internet Explorer in compatibility mode. [http][https][server-side]
  [#5188]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The URL of the login page used by the HTTP/HTTPS file transfer service was
  moved from /login to /__chsps__/login. [server-side][http][https] [#5128]
* Support for Alpine Linux 3.6 on X86_64 was removed. [#5179]
* Event with ID 60019 emitted when a transfer has invalid schedule
  configuration was removed and replaced with the generic event ID. [#5184]
* The HTTP/HTTPS file transfer API now requires an explicit `Accept:
  application/json` header in order to use the JSON variant of the API.
  Otherwise, it will default to the HTML/WebDAV variant.
  [http][https][api][server-side] [#5188]


Version 3.43.1, 2019-01-07
--------------------------


Defect Fixes
^^^^^^^^^^^^

* SFTP client now waits for a maximum of 60 seconds for the server to
  respond. In previous versions it was waiting forever, causing transfers to
  stall if the server never responded to the request.
  This could happen if the server drops the connection during a transfer.
  [client-side][sftp] [#5172]


Version 3.43.0, 2018-12-19
--------------------------


New Features
^^^^^^^^^^^^

* When defining a new password for an account, it is now possible to define a
  minimum level of complexity and strength. [#4700]
* You can now set an email as part of the user's account details. [#5125]
* You can now allow FTP/FTPS users to change their passwords.
  [server-side][ftp][ftps] [#5127]
* The bundled OpenSSL library was updated to OpenSSL 1.1.0j on Windows, SLES
  11, and OS X. [#5148]
* A new event handler was added for extracting GZIP compressed files to a
  destination folder. [#5150]
* Debian 8 (Jessie) on X86_64 is now a supported operating system. [#5152]


Defect Fixes
^^^^^^^^^^^^

* SFTP and SCP file transfer services no long fail when the client is sending a
  "keep alive" global request. [server-side][sftp][scp] [#5149]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Debian 7 is no longer supported as it was replaced by Debian 8. [#5152-1]
* Solaris 11 on SPARC and X86 is no longer receiving new SFTPPlus updates due
  to weak demand for Solaris 11 and increasing costs in keeping Solaris 11
  infrastructure up to date. [#5152]


Version 3.42.0, 2018-11-27
--------------------------


New Features
^^^^^^^^^^^^

* You can now define a custom CSS file for HTTP/HTTPS file transfer
  services. [server-side][http][https] [#5101]
* You can now automatically get SSL/X.509 certificates signed by Let's
  Encrypt's certificate authority. [ftps][https] [#5117]
* The sample init scripts were updated to allow starting SFTPPlus directly
  under an unprivileged service account. [#5132]
* It is now possible to set a database event handler which will automatically
  delete older events. In this way you can limit the size of the database.
  [#5137]
* Amazon Linux 2 on X86_64 is now a supported platform. [#5139]


Defect Fixes
^^^^^^^^^^^^

* The MySQL database resource is no longer erroneously marked as requiring a
  restart in the Local Manager. [#5137]


Version 3.41.1, 2018-11-21
--------------------------


Defect Fixes
^^^^^^^^^^^^

* In marker-based batch transfer, the marker file is now always transferred
  last. [client-side] [#5143]


Version 3.41.0, 2018-11-15
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to define a list of HTTP Host header origins accepted
  by the HTTP file transfer services and the Local Manager.
  This allows running compatible SFTPPlus services behind a load balancer
  without compromising on the default CSRF checks.
  [server-side][http][https] [#5138]


Version 3.40.1, 2018-11-14
--------------------------


Defect Fixes
^^^^^^^^^^^^

* The option to hide the SFTPPlus authentication session from the
  `www-authenticate` headers is now visible in the Local Manager.
  [server-side][http][https] [#5134]


Version 3.40.0, 2018-11-13
--------------------------


New Features
^^^^^^^^^^^^

* SuSE Enterprise Linux without the Security Module and OS X are now
  distributed with OpenSSL 1.1.0h, making it possible to use TLS 1.2 and SHA2.
  [#5030]
* It is now possible to use variable placeholders when defining the path for
  the local file event handler. [#5095]
* You can now define the SSH keys used by the SFTP/SCP file transfer service
  and by the SFTP location as text values inside the configuration file.
  Storing SSH keys in external files is still supported. [sftp][scp] [#5096]
* You can now define the SSL certificate and key pairs used by HTTPS/FTPS and
  the local manager services as text values inside the configuration file.
  [ftps][https] [#5097]
* You can now hide the SFTPPlus session authentication method from the
  `www-authenticate` header. This can be used as a workaround for an
  authentication issue when using SFTPPlus with older HTTP clients, which don't
  recognize multiple `www-authenticate` headers. [server-side][http][https]
  [#5099]
* It is now possible to make the files of an account available over HTTP as a
  public file transfer site. No username or password is required to access and
  manage those files. [server-side][http][https] [#5100]
* It is now possible to filter event handlers based on the source IP address.
  [#5120]


Defect Fixes
^^^^^^^^^^^^

* When an SFTP transfer (upload or download) is interrupted, a dedicated event
  is emitted.
  In previous versions, no event was emitted to signal the transfer failure.
  [server-side][sftp] [#5027-1]
* When an SCP transfer (upload or download) is interrupted, the emitted events
  now clearly signal the transfer failure. In previous versions, the same
  events as for a successful transfer were emitted. [server-side][scp] [#5027]
* SFTPPlus no longer uses the MIME type database provided by the operating
  system. In older operating systems like SuSE 11, the MIME type for JavaScript
  files was defined as `text/x-js`, which caused failures in modern versions of
  Chrome and Firefox. SFTPPlus now defines the MIME type as
  `application/javascript` on any operating system. [local-manager] [#5075]
* The speed for listing the folder content using the FTP/FTPS or HTTP/HTTPS
  file transfer services was improved. The improvement is observed especially
  on Windows, and when listing folders hosted by a remote Windows or NFS share.
  [server-side][ftp][http] [#5083]
* The SCP server will now use the correct name to write a file when the client
  is requesting an upload without providing the base path.
  In previous versions, a file named '-t' was created instead.
  [server-side][scp] [#5094]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with ID 20107 was removed and replaced with the event with ID 20158.
  [#5095]
* Events with ID 30013, 30048, 30052 were removed and replaced with the generic
  event ID 20077. Event with ID 30075 was removed and replaced with the generic
  event with ID 20158. [server-side][sftp][scp] [#5096]
* Loading of SSL/X.509 certificates and keys from .DER files was removed. You
  should convert your certificates and keys to PEM format. PEM format is the
  only format supported by SFTPPlus. DER support was removed, as not all of its
  features were supported. For example, loading the certificate chain or using
  multiple certificate authorities was only supported for the PEM format.
  [ftps][https] [#5097-1]
* Loading the certificate authority configuration from a directory containing
  multiple files is no longer supported. You can still use multiple certificate
  authorities for the same configuration by storing all the CA certificates in
  the same file. [https][ftps] [#5097]


Version 3.39.0, 2018-10-05
--------------------------

**Customers using the SCP protocol are urged to upgrade to this version.
Any previous version contains a security issue when overwriting
files over SCP.**


New Features
^^^^^^^^^^^^

* In the event handler configuration, it is now possible to filter the events
  based on their groups. [#2483]
* When the remote FTP/FTPS server supports the MLST command, SFTPPlus will use
  it to determine the existence of remote paths. [client-side][ftp][ftps]
  [#3885]
* The events emitted at the start or at the end of a client-side file transfer
  now contain the size of the file, duration and transfer speed. [client-side]
  [#5067]


Defect Fixes
^^^^^^^^^^^^

* When using `execute_on_destination_before` in a transfer for which the
  destination location is stopped, the transfer will automatically start the
  location. In previous versions the transfer would failed as the location was
  stopped, requiring a manual start of the location. [client-side] [#3511]
* When checking the existence of a remote FTP file, the operation now fails
  when the server returns an error other than 'Path not found'. In previous
  versions, the error was ignored and the path was considered as non-existing.
  [client-side][ftp][ftps] [#3576]
* FTP/FTPS client operation can now successfully detect the absence of a file
  on a remote server. [client-side][ftp][ftps] [#3885]
* You can now disable the timeout for the FTP data connection by setting its
  value to 0. In previous versions, when set to 0, the connection was
  disconnected right away due to the timeout. [server-side][ftp][ftps] [#5049]
* When changing the `extra_data` configuration for the HTTP event handler, the
  Local Manager UI now shows that a restart is required for the event handler.
  [#5079]
* You can now change from the Local Manager the list of SSH ciphers available
  to the SFTP and SCP file transfer services. This was a regression introduced
  in 3.37.0. [server-side][sftp][scp] [#5085]
* When overwriting files using the SCP file transfer, the content of the
  existing file is completely erased. In previous versions, when overwriting an
  existing file with a new file which was smaller in size, the resulting file
  would still have the file size of the previous file, with the extra data kept
  from the previous file. [security][server-side][scp] [#5087]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* When a FTP server-side operation fails due to a permission error, the error
  code is now 553. In previous versions, it was 550, which was the same error
  code for `Path not found` or the generic error code for other error cases.
  [server-side][ftp] [#3576]


Version 3.38.0, 2018-09-21
--------------------------


New Features
^^^^^^^^^^^^

* When the remote FTP/FTPS server supports the MLST command, SFTPPlus will use
  it to determine the existence of remote paths. [client-side][ftp][ftps]
  [#3885]
* For a transfer, it is now possible to execute on destination commands which
  will include the source and destination path and file name. [client-side]
  [#4522]
* New permissions `allow-create-folder`, `allow-delete-folder`,
  `allow-delete-file`, and `allow-set-attributes` were added to help defining a
  stricter configuration. [server-side] [#4955-1]
* A new permission, `deny-full-control` was added to deny any action to the
  configured path. [server-side] [#4955]
* You can now add custom values to the JSON payload sent by the HTTP event
  handler.
  This allows sending SFTPPlus HTTP events to existing webhooks like Slack or
  Splunk. [api] [#5068]


Defect Fixes
^^^^^^^^^^^^

* FTP/FTPS client operation can now successfully detect the absence of a file
  on a remote server. [client-side][ftp][ftps] [#3885]


Version 3.37.1, 2018-09-13
--------------------------


Defect Fixes
^^^^^^^^^^^^

* The HTTP API authentication for an account now fails when the account is
  accepted by the remote HTTP API but the associated group is disabled.
  [server-side][security] [#5058]
* A defect was fixed in Local Manager which was causing the Local Manager to
  fail on Internet Explorer 11. [#5061]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with ID 20060 was removed and replaced by event with ID 20136.
  [server-side] [#5058]


Version 3.37.0, 2018-09-06
--------------------------


New Features
^^^^^^^^^^^^

* HTTP and HTTPS file transfer API now supports session-based authentication.
  Basic Auth login is still supported. [server-side][http][https] [#5009-1]
* HTTP and HTTPS file transfer services now have a session-based login
  page. Basic Auth login is still supported for web clients which don't
  support cookies. [server-side][http][https] [#5009]
* LDAP authentication method was extended to allow defining a LDAP filter
  for LDAP users which are allowed to act as administrators through the Local
  Manager service. [manager] [#5010-1]
* You can now define multiple authentication methods for the Local Manager
  service. [manager] [#5010-2]
* OS authentication method was extended to allow defining a list of
  Operating System account groups which are allowed to act as administrators
  through the Local Manager service. [manager] [#5010]
* You can now use Local Manager to configure the accounts and groups of the
  `local-file` authentication method. [#5041]
* It is now possible to configure an event handler filter based on excluded
  usernames or components by using the `!` (exclamation mark) to mark a value
  which needs to be excluded. [server-side][client-side] [#5043]
* The MDTM FTP command now shows microseconds when displaying time.
  [server-side][ftp][ftps] [#93-1]
* FTP/FTPS server now supports MLST and MLSD commands (Listings for
  Machine Processing) as specified in RFC 3659. [server-side][ftp][ftps] [#93]


Defect Fixes
^^^^^^^^^^^^

* The authentication process now fails when an authentication is configured but
  not running. In previous versions, the stopped authentication method was
  skipped, and the authentication process continued with the next configured
  method. [security] [#5010]
* When sending files to an FTP or FTPS destination location, transfers will
  no longer saturate the network, instead they will follow the TCP congestion
  signaling. In previous versions this issue was causing excessive memory
  usage and transfer failures over low bandwidth networks.
  [client-side][ftp][ftps] [#5033]
* Comma-separated values in Local Manager can now be configured using a simple
  free-text input box. This allows editing existing values and makes it easier
  to reorder them. [management] [#5043]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* HTTP file transfer service API now uses cookie-based authentication by
  default. In previous versions the default authentication method was
  HTTP Basic authentication, which remains an available method.
  [server-side][http][https] [#5009-1]
* HTTP file transfer service API now uses JSON as default content type
  for responses. In previous versions you would have to explicitly ask for
  JSON. Now you need to explicitly ask for HTML. [server-side][http][https]
  [#5009]
* Events with ID 20005 and 50008 were removed and replaced with event 20136.
  Events with ID 20135 and 20138 were removed and replaced with event 20142.
  [#5010-1]
* Event with ID 50009 was removed, as OS administrators now use the OS
  authentication method. [#5010-2]
* With the introduction of multiple authentication methods for the Local
  Manager service, you will now need to explicitly define the `[server]
  manager_authentications` configuration option. If `manager_authentications`
  is not defined (or left empty), SFTPPlus will fall back to the first
  defined Application authentication method. [#5010-3]
* The `include_os_group` configuration options for roles was removed. Now you
  can explicitly define an OS authentication method for the Local Manager
  server. `include_os_group` was replaced by the `manager_allowed_groups`
  configuration option for the OS authentication method. [server-side] [#5010]


Version 3.36.0, 2018-08-02
--------------------------


New Features
^^^^^^^^^^^^

* The Azure File Service of the Azure Storage Account
  is now available as a location for client-side transfers. [client-side][http]
  [#4988]
* It is now possible to define a client-side file transfer that will wait for a
  signaling filename before it starts transferring the files. [client-side]
  [#4989]
* It is now possible to configure transfers which will monitor the source
  recursively and will then transfer to the same non-recursive destination.
  [client-side] [#4998]
* It is now possible to configure a transfer rule which will use a destination
  file name that is different to the source name. [client-side] [#5007]


Defect Fixes
^^^^^^^^^^^^

* The Windows installer is now signed. [#4794]
* It is now possible to clear the data attributes and structured fields
  configuration for an event handler and the allowed groups for an OS
  authentication mode from the Local Manager. In previous versions saving these
  configuration changes was generating an error. [#5018]
* When local file event handler is rotating the files based on time, it now
  preserves the file extension. In previous versions the timestamp was used as
  the file extension. [#5036]


Version 3.35.0, 2018-07-03
--------------------------


New Features
^^^^^^^^^^^^

* The OpenSSL library used by SFTPPlus on Windows was updated to OpenSSL
  1.1.0h. [#4579]
* It is now possible to define virtual folders that are available to all
  accounts from a group. These virtual folders can point to directories outside
  an account's locked home folder. [server-side] [#4928]
* It is now possible to allow authentication of operating-system accounts only
  for those belonging to a configured group. [server-side] [#4962]
* Python version on all supported platforms except HP-UX was updated to 2.7.15.
  Consequently, the Expat libraries bundled with Python were updated to 2.2.4
  on these platforms. [#4579]


Defect Fixes
^^^^^^^^^^^^

* An internal error is no longer raised when a SSH client sends a message
  for a method which is not supported by the SSH transport. Instead, the client
  receives a standard SSH not-implemented error. [server-side][sftp] [#4579]
* The speed of the SSH handshake for the SFTP service has been improved.
  Previously, there was a noticeable difference for certain customers during
  the SSH handshake authentication process. [server-side][sftp][#4579]
* pyOpenSSL was updated on AIX and Solaris to fix CVE-2013-4314. The
  X509Extension in pyOpenSSL before 0.13.1 does not properly handle a '\0'
  character in a domain name in the Subject Alternative Name field of an X.509
  certificate, which allows man-in-the-middle attackers to spoof arbitrary SSL
  servers via a crafted cert issued by a legitimate Certification Authority.
  The experimental packages for HP-UX are still vulnerable to this and
  will to be fixed in a future release.[server-side][#4579]
* Once set, passwords for locations or email resources are no longer readable
  from Local Manager. A password can be read only before being set and applied.
  Afterwards, its value cannot be read, only updated. [security] [#4938]
* Comma-separated configuration values may now contain comma characters,
  as long as they are enclosed in double quotation marks. [#4951]
* The event generated when a peer's certificate validation fails during a
  TLS/SSL handshake now shows the detailed error message, not just the error
  code. [#4979]


Version 3.34.1, 2018-06-07
--------------------------


Defect Fixes
^^^^^^^^^^^^

* The files downloaded using the HTTP file transfer service now have explicit
  headers to disable caching. [security][http][https] [#4953]
* The HTTP service no longer returns user input as part of the error messages.
  [security][http][https][server-side] [#4954]


Version 3.34.0, 2018-05-28
--------------------------


New Features
^^^^^^^^^^^^

* You can now set up an UNC path or a symbolic link to Windows Shares as home
  folder for an account. [#4635]
* The HTTP/HTTPS file transfer service and the Local Manager service now
  provide the option to configure a set of headers which are sent for all
  responses. You can use this to set the Strict-Transport-Security header or
  the use a custom `Server` header in an attempt to conceal the identity of the
  server. [security] [#4784]
* The LDAP authentication method can now connect to LDAP servers using IPv6
  address literals. [server-side] [#4824-1]
* It is now possible to dynamically associate LDAP accounts to SFTPPlus groups
  based on arbitrary LDAP entry attributes. This is designed to augment the
  LDAP configuration without requiring any updates to the LDAP database.
  [server-side] [#4824]
* We now provide limited support for running SFTPPlus on legacy Windows 2003
  Servers. For more details, check the known issues section in our
  documentation. [#4896]
* Ubuntu 18.04 LTS on X86_64 is now a supported platform. [#4912]
* A new permission, `allow-traverse`, was added to allow viewing only the
  folder structure without any files. In this way, accounts can traverse the
  folder hierarchy without seeing what files are already there. [#4931]
* A new permission `allow-list` was added to allow configuration of only the
  folder/directory listing operations. This has no effect for the SCP protocol,
  as the protocol itself does not support the folder listing operation. [#4932]
* A new permission `allow-rename` was added to allow configuration of only the
  rename operations available in the SFTP and FTP/FTPS file transfer servers.
  [#4933]
* The `Ban IP for a time interval` authentication method is now enabled by
  default in new installations. [#4934]


Defect Fixes
^^^^^^^^^^^^

* The HTTP/HTTPS file transfer service and the Local Manager service now
  advertise a set of HTTP headers to mitigate CSRF and XSS attacks. [security]
  [#4930]
* The low-level JSON-RPC used by the Local Manager service now explicitly
  informs the web browser not to cache its POST responses. In the previous
  version, only GET requests were instructing the web browser not to cache the
  response. [security] [#4937]
* The LDAP authentication method no longer accepts credentials with empty
  passwords. [server-side][security] [#4939-1]
* When receiving a request which is authenticated via SSH key or SSL/X.509
  certificates, the LDAP authentication method now emits a message informing
  that only password credentials are supported. [server-side] [#4939]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `allow-read` permission will no longer allow listing the content of a
  folder. If you want to allow folder listing, you will need to update the
  configuration and add the new explicit `allow-list` permission. [#4932-1]
* The error message returned when denying a folder listing operation was
  changed to include `allow-list` instead of the previous `allow-read` details.
  [#4932]
* The error message returned when denying a rename operation was changed to
  include `allow-rename` instead of the previous `allow-full-control` details.
  [#4933]


Version 3.33.0, 2018-04-23
--------------------------


New Features
^^^^^^^^^^^^

* A new authentication method was added which allows the server to read
  application accounts from a separate file. [server-side] [#1056]
* It is now possible to configure the supported ciphers for an SFTP location
  using the `ssh_cipher_list` configuration option. [#4619]
* The FTP and FTPS file transfer services now support IPv6 as specified in RFC
  2428. [server-side][ftp][ftps] [#4823-1]
* The HTTP and HTTPS file transfer services now support IPv6.
  [server-side][http][https] [#4823]
* The event with ID 30011 now contains details about the encryption used by the
  SFTP and SCP connections. [server-side][sftp][scp] [#4850]


Defect Fixes
^^^^^^^^^^^^

* A defect was fixed in the SFTP service for the `chmod` operation. In
  previous versions, the `chmod` was ignored and always returned a success
  result. [server-side][sftp] [#4338]
* The HTTP PUT method of the file transfer service now returns a correct code
  when the HTTP request contains `Expect: 100-continue` and the request
  fails to be authenticated. [server-side][http][https] [#4856]
* When uploading files into an empty folder using a web browser which has
  Javascript enabled, you will now see the uploaded file in the folder listing.
  This issue was introduced in 3.31.0. This was not an issue for web browsers
  with Javascript disabled. [server-side][http][https] [#4865]
* The HTTP file transfer service will now force any file to be downloaded by
  the browser. Previously, it was displaying HTML or images inside the browser
  without forcing a download. [server-side][http][https][security] [#4877-1]
* The HTTP file transfer service and the Local Manager service were updated to
  prevent cross-site request forgery (CSRF / XSRF) attacks by validating the
  `Origin` and `Referer` headers against the `Host` header.
  [server-side][http][https][security] [#4877]
* The HTTP file transfer service will now set the session cookie using the
  `httpOnly` and 'sameSite' options. [server-side][http][https][security]
  [#4881]
* The error messages in the HTTP service were updated to prevent cross site
  scripting attacks (XSS). [server-side][http][https] [#4884]


Version 3.32.0, 2018-04-03
--------------------------


New Features
^^^^^^^^^^^^

* SFTP and SCP file transfer services can now listen on IPv6 addresses and
  accept connections from IPv6 clients. [server-side][sftp][scp] [#1924]
* The HTTP and HTTPS service now accepts creating new folders with the HTTP PUT
  and WebDAV MKCOL methods. [server-side][http][https] [#4828-1]
* The HTTP and HTTPS service now accepts deleting folders and files with the
  HTTP DELETE method. [server-side][http][https] [#4828-2]
* The HTTP and HTTPS service now accepts file uploads using the HTTP PUT
  method. [server-side][http][https] [#4828]


Defect Fixes
^^^^^^^^^^^^

* FTP and FTPS client side transfer can now transfer files larger than a few
  bytes from a remote FTP/FTPS server and to the local filesystem. This issue
  was introduced in SFTPPlus version 3.20.0. This defect was not affecting
  uploading / pushing files to a remote FTP/FTPS server.
  [client-side][ftp][ftps] [#4754]
* The Developer Documentation for the HTTP authentication method was updated to
  make it clear the expected repose codes for the authentication server.
  [server-side] [#4758]
* The JavaScript UI for the HTTP and HTTPS file transfer services no longer
  limit the file size to 256MB. This defect was introduced in 3.31.0.
  [server-side][http][https] [#4815]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The default `secure` `ssl_cipher_list` configuration was updated to
  `HIGH:!PSK:!RSP:!eNULL:!aNULL:!RC4:!MD5:!DES:!3DES:!aDH:!kDH:!DSS`. The
  previous value was `ALL:!RC4:!DES:!3DES:!MD5:!EXP`. In this way, when
  updating the OpenSSL library you will automatically get an update in the list
  of secure ciphers, without the need to update SFTPPlus.
  [security][ftps][https][client-side][server-side] [#4748]
* The event (ID 40025) that was emitted when an unknown error was generated by
  the HTTP service during a JSON API request was removed. It has been replaced
  with event ID 40003. [server-side][http][https] [#4828]


Version 3.31.0, 2018-02-20
--------------------------


New Features
^^^^^^^^^^^^

* The option to enforce unique names for uploaded files is now available for
  the HTTP and HTTPS file transfer services. [server-side] [#4465]
* A SOCKS version 5 (SOCKS5) proxy without authentication can now be used to
  connect to remote SFTP and SCP servers. [client-side][sftp][scp] [#4546]
* A new event handler option is added in order to send filtered events to
  standard output. This can be used when running SFTPPlus in Docker or with
  other process supervisors. [#4645]
* The option to enforce unique names for uploaded files is now available for
  the FTP, Implicit FTPS and Explicit FTPS protocols. [server-side] [#4650]
* The `file-dispatcher` event handler can now be configured to automatically
  create destination folders. [#4652]
* The close event description for SFTP and SCP client-side and server-side
  connection now contains the encryption used to protect connection.
  [client-side][server-side][sftp][scp] [#4668]
* The HTTP and HTTPS file transfer services now allow uploading multiple files
  and adding files via drag and drop. [server-side][http][https] [#4673]
* Support for Red Hat Enterprise Linux versions 7.0 to 7.3 with OpenSSL 1.0.1
  was readded alongside support for RHEL 7.4 and newer using OpenSSL 1.0.2.
  [#4691]
* A new `secure` configuration value is available for the `ssl_cipher_list` and
  `ssh_cipher_list` as part of the FTPS, SFTP, SCP, and HTTPS file transfer
  services. [security][client-side][server-side] [#4727]


Defect fixes
^^^^^^^^^^^^

* The transfer for SFTP and SCP locations is no longer interrupted when the
  remote server is requesting a SSH re-key exchange. This was affecting
  client-side transfers of files bigger than 1GB, as this is the point
  where some servers are re-keying. This is when either side forces the other
  to run the key-exchange phase which changes the encryption and integrity keys
  for the session. [client-side] [#4302]
* It is now possible to stop the client shell at any time by pressing the
  Ctrl+C key combination. In previous versions this was not available while an
  operation was in progress. [#4626]
* The AIX 7.1 build of SFTPPlus was updated to work with older OpenSSL versions.
  Previous versions of SFTPPlus (from 3.27.0 to 3.30.0) on AIX 7.1
  required OpenSSL 1.0.2k or newer. [#4696]
* SFTP and SCP client and server side can now handle key exchange process even
  for peers which advertise their SSH version string with trailing spaces. This
  can happen for Bitvise SSHD Server when configured to omit its version.
  [client-side][server-side][sftp][scp] [#4718]
* The documentation for expression matching was updated to explain that regular
  expression matching is done as a search operation. For an exact match, use
  the start and end regex anchors. [#4724]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Events with ID 40015 and 40016 were replaced by already existing event with
  ID 40022. Event 40022 is now the only one emitted when there are errors
  during an upload operation. [server-side][http] [#4465]
* The default configuration for SFTP, SCP, FTPS, and HTTPS connections was
  updated to exclude the 3DES cipher in order to prevent SWEET32 attacks. To
  not break backward compatibility for existing installations, this change
  affects only new installations. Existing installations will need to be
  manually updated to exclude the 3DES-based ciphers. [#4727]


Version 3.30.0, 2018-01-23
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to dynamically dispatch files to different destinations
  based on the name of the file which was dispatched. [#4555]
* The HTTP authentication method can now send requests which are authenticated
  using the HTTP Basic authentication (BA) method. [#4589-1]
* The HTTP event handler can now send requests which are authenticated using
  the HTTP Basic authentication (BA) method. [#4589]
* The `file-dispatcher` event handler now has the capability to delete files.
  [client-side] [#4624]
* You can now configure an account to amend the requested file for an upload by
  prefixing it with a universally unique identifier (UUID4). This option is
  available for the SFTP and SCP protocols. [server-side][sftp][scp] [#4643]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `${SHAREPOINT_CA}` and `${SHAREPOINT_CRL}` placeholders were replaced by
  the more inclusive `${MICROSOFT_IT_CA}` and `${MICROSOFT_IT_CRL}`. The
  `${SHAREPOINT_CA}` and `${SHAREPOINT_CRL}` placeholders will continue to be
  available as an alias for Microsoft IT CA. [#4625]


Version 3.29.0, 2018-01-09
--------------------------


New Features
^^^^^^^^^^^^

* An event with ID 30079 is now emitted when an SFTP location sends a banner
  message during authentication. [#4293]
* The HTTP file transfer service now supports the HEAD method for folders which
  return OK when the folder exists. [#4493]
* The HTTP event handler now sends the local timestamp for the generated event.
  Previously, the event was sent without a timestamp and the event timestamp
  was supposed to be created by the PHP WebAdmin. To take advantage of this
  change, you will need PHP WebAdmin version 1.9.0 or newer. [#4577]


Defect Fixes
^^^^^^^^^^^^

* An error is no longer produced when the source location for a SFTP transfer
  is a Bitvise SSH server. [#4297]
* An internal server error is no longer produced by the HTTP file transfer
  service when a file or a folder is accessed with an unsupported method.
  [server-side][http] [#4493]
* The HTTP event handler now sends the IP and PORT of the remote peer
  associated with the event. Previously, this detail was omitted and PHP
  WebAdmin was using the address of the SFTPPlus server instead of the client
  connected to the server. [#4577]
* The limit of pending files to be transferred for a single transfer was raised
  from 5 000 files to 100 000 files. [client-side] [#4586]


Version 3.28.0, 2017-11-29
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to set permissions for file management operations for
  accounts authenticated with the FTP/FTPS service. [ftp][ftps][server-side]
  [#3399]
* You can now implement custom event handlers using our Python-based API.
  [#4192]
* SFTPPlus is now distributed with the CA chains for SharePoint Online and
  Let's Encrypt. [#4365]
* The FTPS client-side connections now show the SSL/TLS method used together
  with the cipher protecting the communication. [client-side][ftps] [#4370]
* FTPS server-side events emitted when the command connection is closed now
  contains the cipher used to secure the connection. [ftps][server-side] [#4458]
* It is now possible to define the permissions of file management operations
  set by accounts that are authenticated with the SCP and SFTP services.
  [scp][sftp][server-side] [#4461]
* It is now possible to define the permissions of file management operations
  set by accounts that are authenticated with the HTTP/HTTPS services.
  [http][https][server-side] [#4462]
* A rename-prepend-unixtime method was added to the file dispatcher event
  handler. It will allow the event handler to conduct an instant, atomic rename
  of the source file. [#4466]
* You can now use additional SSL/TLS configuration options to protect HTTPS URL
  set for the HTTP authentication method. [server-side] [#4482]
* HTTPS client connections now support the Server Name Indication (SNI) TLS
  extension. [#4490]
* You can now use HTTPS url for the HTTP Post event handler. [#4512]


Defect Fixes
^^^^^^^^^^^^

* The WebDAV location can now be configured with SSL/TLS details in order to
  set up the parameter for the SSL/TLS connection.
  [security][client-side][webdavs][https] [#3912]
* The events emitted by the file dispatcher event handler will now contain the
  full path to the destination file. In previous versions, the events
  contained the destination paths. [#4501]
* An internal server error is no longer raised when the SMTP client connects
  to the server and the server drops the connection. [#4509]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The event with ID 40002 is now associated with a server-side error when
  obtaining the attributes of a path. In previous versions, it was only used
  when the path was not found. [server-side][http][https] [#4462]
* Support was removed for the s390x IBM Systems z mainframe and the Hercules
  mainframe emulator, for both Red Hat Enterprise Linux 6 and generic Linux.
  If you are still using this platform, please get in touch with us. [#4503-1]
* Support was removed for Ubuntu 14.04 LTS on POWER8 (little endian). Ubuntu
  14.04 LTS is still supported on Intel X86_64. If you are still using this
  platform, please get in touch with us. [#4503-2]
* Support was removed for Red Hat Enterprise Linux 6 on POWER8 (big endian).
  Red Hat Enterprise Linux 6 is still supported on Intel X86_64. If you are
  still using Red Hat Enterprise Linux 6 on POWER8, please get in touch with
  us. [#4503-3]
* Support was removed for Solaris 10 11/06 U3 on SPARC and X64. Latest Solaris
  10 on both SPARC and X64 are still supported. If you are still using these
  platforms, please get in touch with us. [#4503]


Version 3.27.0, 2017-11-06
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to define the expiration date and time when configuring an
  account of type application or OS. [server-side] [#1152]
* An audit event is now emitted when the HTTP connection is made and when it is
  closed. [client-side][http][https] [#3925]


Defect Fixes
^^^^^^^^^^^^

* When the user is authenticated based on the SSL certificate, the FTPS server
  now responds with code 230 instead of 232. [ftps][server-side] [#3563]
* FTPS client connections will now verify the identity of the remote FTPS
  server when configured to check against a certificate authority.
  [ftps][client-side][security] [#3566]
* When a WebDAV location fails to re-authenticate, it will enter the fail state
  and no other operations are performed. [client-side][http][https] [#4339-1]
* When a WebDAV client session has its session credentials rejected and
  multiple WebDAV client requests are made at the same time, only a single
  re-authentication request is made. [client-side][http][https] [#4339]
* Use a PID file in $INSTALL_ROOT in the init/unit files too, as used by the
  bin/admin-commands.sh script by default. This avoids mismatches when the
  daemon is started with this script and the status is checked with an init
  script. [#4388]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Support for AIX 5.3 was removed. AIX 7.1 is still supported. If you are still
  using this platform, please get in touch with us. [#4361-1]
* Support for Raspbian Linux was removed. If you would like to use SFTPPlus on
  this platform, please get in touch with us. [#4361]
* Support for SUSE Enterprise Linux 10 was removed. If you are still using this
  platform, please get in touch with us. [#4397]


Version 3.26.0, 2017-10-03
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible for the LDAP authentication to accept a direct username.
  In this way, you can leverage the Active Directory implementation and
  authentication using the User Principal Name (UPN). [server-side] [#4352]


Defect Fixes
^^^^^^^^^^^^

* An internal server error is no longer emitted for long uploads taking more
  than 15 minutes to complete over HTTP/HTTPS. [server-side][http][https]
  [#2533]
* Stopping the SFTPPlus during a transfer which is pending a reconnection, the
  stop procedure is no longer delayed until all reconnection retries are
  exhausted. [client-side] [#2656]
* The WebDAV location will detect changes into folders, when the letter cases
  in the configured path does not match the cases on the server.
  [client-side][http][https] [#3945-1]
* The WebDAV location can now get members and attributes for paths containing
  the `+` (plus) character, as well as detecting changes into folders with such
  names. [client-side][http][https] [#3945]
* When the destination of a transfer is changed, the Local Manager will not
  mark the transfer as requiring a restart. Unless the transfer is restarted,
  the files are transferred using the destination defined at start time.
  [client-side] [#4245]
* The event with ID 10079 was updated to show the reason of the failure.
  [ftp][ftps][server-side] [#4326]
* The references to recursive transfers were removed, as recursive transfers
  are not yet supported. Recursive transfers were never supported, and we have
  accidentally referenced them in the documentation and the administration UI.
  [client-side] [#4367]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Support for Windows XP, Windows Vista, and Windows Server 2003 was removed.
  If you are still using these operating systems, please get in touch with us.
  [#3415]
* Events with IDs 30009, 30010 and 30066 were replaced by the generic event
  with ID 30008. [server-side][sftp] [#4326]


Version 3.25.1, 2017-09-14
--------------------------


Defect Fixes
^^^^^^^^^^^^

* When using the client-shell with a FTP/FTPS location, the path attributes
  will show the modified time assuming that the server is in the same timezone
  as the client. [ftp][ftps][client-side] [#3038]
* When using OS and application accounts containing `@` in their names, the
  home folder is no longer automatically translating the `@` character to the
  dot (`.`) character. [server-side] [#4257]


Version 3.25.0, 2017-09-07
--------------------------


New Features
^^^^^^^^^^^^

* Ubuntu Server 16.04 on ARM64 (ARMv8-A/AArch64) is now a supported platform.
  [#4321]


Defect Fixes
^^^^^^^^^^^^

* When downloading files over WebDAV, the file content is now correctly
  transferred.
  In the previous version, small files (below 10kB) might have be transferred
  without content and larger files (over 10kB) may have the last few bytes
  missing.
  [client-side][http][webdav] [#4329]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Support for Ubuntu Server 14.04 on ARM64 (ARMv8-A/AArch64) was removed.
  Please contact us if you still need to deploy on this Ubuntu version. [#4321]


Version 3.24.1, 2017-08-29
--------------------------


Defect Fixes
^^^^^^^^^^^^

* When a failure occurs rotating a Local File Handler event handler, the error
  is now logged properly and the event handler will stop after a specified
  number of failures. [#4176]
* Timeouts for HTTP and WebDAV requests were increased from 15 to 30 seconds
  for downloads requests and from 20 to 120 second for file upload requests.
  [#4306]
* An internal server error is no longer generated when uploading large files to
  a WebDAV server. [client-side][http][https] [#4306]


Version 3.24.0, 2017-08-09
--------------------------


New Features
^^^^^^^^^^^^

* The Past Activity page, accessible from Local Manager,
  now has an option to download all events in CSV format.

* The WebDAV location now supports the `get_attributes` client shell command.
  [http][https][webdav][client-side]

* The Solaris 10 and 11 packages for SPARC are now only available in 32bit in
  order to keep Python's memory usage low.

* SUSE Enterprise Linux 11 with Security Module is now a supported platform,
  providing stronger cryptography than base SLES 11, with support for
  TLS 1.2 and SHA2.

* The OpenSSL version distributed in our Windows version was updated to OpenSSL
  1.1.0f.
  [ftps][https]

* Transient errors generated while watching a location will now emit an
  event.
  [client-side]


Defect Fixes
^^^^^^^^^^^^

* You can now run file uploads taking longer than 20 seconds.
  A timeout is no longer raised after 20 seconds when performing a long
  upload over HTTP, as long as chunks are transferred with a delay smaller than
  20 seconds.
  [http][https][client-side] [#4227]

* A defect was fixed which previously allowed bad configurations for the
  `structured_fields` Local File Event Handler configuration option. [#4207]

* An internal error is not triggered when a local file event handler
  with time-based rotation has a bad configuration. [#4208]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The following events where renamed as part of event ID reorganization.
  Event with ID 32001 was renamed to 30004, 70001 to 30071,
  70002 to 30072, 70003 to 30073, 70005 to 30075, 70006 to 30076,
  70007 to 30077, 70008 to 30078,
  80002 to 10102, 80003 to 10103, 80004 to 10104, 80005 to 10105,
  80006 to 10106.

* Standard support for Red Hat Enterprise Linux 5 was removed.
  RHEL 5 has reached the end of production phase.
  Please contact us if you need extended life-cycle support.

* The Windows renamed installation file is no longer provided as part of the
  standard download files.
  Please contact us if you are not able to download the standard Windows
  installation kit.


Version 3.23.0, 2017-07-04
--------------------------


New Features
^^^^^^^^^^^^

* The Local File Event Handler now includes a header when log entries are
  stored using the CSV format.


Defect Fixes
^^^^^^^^^^^^

* FTP client-side transfer now works with FTP servers which don't support the
  FEAT command. [ftp][ftps][client-side] [#4180]
* For WebDAV client-side operation, the authentication token is automatically
  refreshed once it is no longer valid. [http][https][client-side] [#4194]


Version 3.22.0, 2017-06-15
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to configure the Local File Event Handler to rotate files
  on a certain time every day using the option `rotate_on`.
* It is now possible to configure the certificate chain advertised by the
  SFTPPlus services which act as SSL/TLS servers. [ftps][https]
* It is now possible to define an event handler which will remove the last line
  from a copy of the file attached the the event.
* It is now possible to define the filter for an event handler based on the
  structured data associated to the event.


Defect Fixes
^^^^^^^^^^^^

* The time-based log rotation now occurs exact at the configured time, not only
  when a new event is emitted. [#3604]
* HTTP/HTTPS client-side connections which take more than 15 seconds to be
  initialized, more than 20 seconds to send the headers once connection is
  established, more than 15 seconds to send a fragment of the body content, are
  now considered stalled and are closed with a timeout error.
  [client-side][webdav] [#4117]


Version 3.21.0 (2017-05-30)
---------------------------

This release fixes a security issue initially introduced in
SFTPPlus version 3.17.0.

**Users that are on SFTPPlus version 3.17.0, 3.18.0, 3.19.0 and 3.20.0,
using FTP with OS accounts,
should upgrade to version 3.21.0 or newer.**


New Features
^^^^^^^^^^^^

* New configuration option `structured_fields` is now available for local file
  event handler, making it possible to store events in a CSV file.
* FreeBSD 10 on X86_64 was introduced as a new supported platform.


Defect Fixes
^^^^^^^^^^^^

* When executing the FTP LIST command for an OS account, it will no longer put
  on hold the whole SFTPPlus process running under that OS account while the
  LIST command is executed. This affects environments in which both OS and
  application accounts are used.
  This issue was introduced in 3.17.0.
  This issue does not affect SFTP operation, FTP operations when using only
  application accounts, nor FTP operations when using only OS
  accounts. [security][os-accounts][ftp][ftps][server-side] [#3692]
* A transfer with a WebDAV source location will no longer fail at runtime if
  the WebDAV server is temporary unavailable. [#4062]
* When failing to close the source or destination file for a transfer, the
  failure is no longer ignored and the transfer failure is observed. [client-
  side] [#4094]
* The audit message, emitted after an account is successfully authenticated,
  now includes the correct information about the local path used by that account
  and whether it is locked. [server-side] [#4103]
* When using the FTP LIST command with an explicit path, the member's name in
  the resulting listing will no longer include the parent path.
  [ftp][ftps][server-side] [#3692]
* A transfer with a WebDAV source location will no longer fail at runtime if
  the proxy server is temporary unavailable. [#4062]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The event with ID 30063 was removed and replaced by the event with ID 30011.
  [scp][server-side] [#4103]


Version 3.20.1, 2017-04-12
--------------------------


Defect Fixes
^^^^^^^^^^^^

* SFTP connection will not hang on QUIT command. [#3994]


Version 3.20.0, 2017-04-08
--------------------------


New Features
^^^^^^^^^^^^

* The HTTP authentication method can now use an HTTP 1.1 proxy via the CONNECT
  command to connect to the final destination.
* Solaris 10 11/06 U3 on SPARC and X64 are now supported platforms. A new
  distributable / installation kit is available for Solaris 10 U3. It can be
  used for any Solaris 10 releases up to U7.
* It is now possible to configure the SSH service using only the
  rsa_private_key or the dsa_private_key configuration options.
* The SysV init script for Unix and Linux now shows the PID of the SFTPPlus
  process when invoked with the `status` parameter.
* SharePoint Online from Office365 Online suite is now available as a location
  using the WebDAV over HTTPS protocol.
* The file dispatcher event handler can now be used together with the events
  emitted by the client-side transfer for a successful or a failed event.
* The file dispatcher event handler can now be configured to use a specific
  event attribute as the path of the file which will be dispatched.
* The LDAP authentication method can now filter the accepted LDAP entries based
  on an LDAP search filter. In this way you can restrict the access to the file
  transfer services.
* It is now possible to authenticate LDAP entries which are located inside the
  LDAP tree in multiple branches. For example, you can authenticate users from
  multiple organizations where each organization has its own subtree.
* It is now possible to configure a group in such a way so that all users which
  are configured to inherit their home folder path from the group can share the
  same path. In previous versions this configuration was not possible as the
  system was designed to prevent accidental configuration of multiple users
  with the same home folder.


Defect Fixes
^^^^^^^^^^^^

* An internal server error is no longer generated when the admin-commands CLI
  tool fails to execute the requested task. [#2338]
* The SSL/TLS shutdown operation was updated to abort the connection when the
  remote peer is no longer actively undergoing the shutdown. The connection is
  aborted if the shutdown sequence needs more than 2 seconds to complete.
  [ftps][https] [#3388]
* When the SCP server-side service successfully received an uploaded file, it
  will exit with exit code 0. [#3507]
* When execute on success or execute on failure are used for a transfer with a
  destination of type local filesystem, the path which is passed as the first
  argument is now a full path to a local file. [#3781]
* The output produced by using the command line tools can now handle non ASCII
  characters with terminal supporting UTF-8 encoding. [#3833]
* The Local File event handler will now detect failures occurred during
  operation and will stop the handler. [#3848]
* An internal server error is no longer produced when a SFTP client will try to
  authenticate using a non ASCII password which contains an invalid UTF-8
  encoding. [server-side][sftp][scp] [#3864]
* For FTPS server-side connection the data channel is now closed even if an
  internal error was encountered on the server-side. [FTPS][server-side]
  [#3904]
* HTTPS connections will no longer produce an internal server error at closing.
  [#3904-1]
* Entities with configuration referring to its own UUID can now be deleted.
  [#3924]
* HTTP authentication method and HTTP event log handler will now accept HTTPS
  URLs. The server is not yet validated. [#3929]
* The Local Manager UI will not show the available locations inside the
  `Locations` page, even when no resources are defined. [#3981]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The configuration options `rsa_public_key` and `dsa_public_key` are now
  deprecated and kept for compatibility purposes. The public key is now read
  from the file configured by the correspondent `_private_key` option. [#3800]
* The event with ID 60017 was updated to signal that the `path` argument
  contains multiple paths. The event with ID 60016 was updated to have separate
  attributes for the failed and success files. For both of the above elements
  the `path` attribute was removed. [#3959]


Version 3.19.0, 2017-02-21
--------------------------


New Features
^^^^^^^^^^^^

* The Local Manager now shows the key fingerprint using SHA1 and SHA256,
  together with the MD5 format, when generating or importing a key.
* MacOS Sierra 10.12 with OpenSSL 1.0.2 provided by the Homebrew community is
  now a supported platform.


Defect Fixes
^^^^^^^^^^^^

* It is now possible to stop a component while it is being started or when it
  is connecting. Previously, a component that was starting or already connected
  was not considered as being active, and there was only the option to start
  and not stop the component. [#3439]
* When a resource is disconnected it will now be in the `Disconnected` state
  instead of the previous `Stalled` state. When the source or destination for a
  transfer are not available the state will be `Source has failed` or
  `Destination has failed` instead of the previous `Stalled` state.
  [client-side] [#3439-1]
* A transfer no longer fails to stop when it is started with an unknown source
  UUID. [client-side] [#3496]
* An internal server error is no longer produced when a transfer fails to
  start. [client-side] [#3496-2]
* A transfer with scheduled resume/stop action will no longer have the actions
  active after the transfer was stopped. [client-side] [#3496-3]
* Fix the issue when event data is not displayed in the "Attached data" section
  on event details page. The page is available from "Past activity" page
  ("Local Manager") by clicking on any event link. [#3641]
* An internal server error is no longer produced when the SSH server is sending
  a global request. [sftp][client-side] [#3735]
* Installing on Linux with partitions mounted with noexec or with SELinux
  restriction will no longer trigger a MemoryError. [#3777]
* The Legacy WebAdmin authentication method now has a visual hint that it
  requires restart after changing the URL configuration. [#3786]
* Format strings such as the entry_content configuration for event handlers are
  now better protected, preventing misuse when configuring them. [#3788]
* A location and any resource component can't any longer be accidentally
  triggered to started multiple times in parallel. In previous versions this
  was triggered by clicking multiple times, in a short period of time, on the
  `Start` button of a location or a resource. [client-side] [#3795]
* The restart required label is no longer displayed for components which are in
  the process of being started, but only for those which are already started
  and operational. [#3795-1]
* The configuration file for the SFTP service which is created by default as
  part of the installation process was fixed to point to the right DSS/DSA
  private key. It was wrongly pointing to the RSA key. The configuration file
  should be `dsa_private_key = configuration/ssh_host_dsa_key` instead of the
  wrong `dsa_private_key = configuration/ssh_host_rsa_key`. [sftp][server-side]
  [#3799]
* A location or a resource will not attempt to reconnect on failure after it is
  stopped. [client-side] [#3826]
* An internal error is no longer raised when calling the admin-commands command
  line tool with unknown parameters. [#3837]
* Globbing/wildcard operation are now available for the FTP NLST command. This
  regression was introduced in 3.17.0. [ftp][ftps][server-side] [#3842]
* The stop operation for a SFTP location will no longer hang when stopping from
  the `stalled` or `disconnected` state. [client-side][sftp] [#3846]
* Monitoring a SFTP location for changes will no longer hang for a SFTP
  transfer when the folder listing operation is done in the same time as the
  remote server is closing the connection. [sftp][client-side] [#3847]
* A warning is displayed when cookies are not allowed for the HTTP service,
  informing the user that some features might not be available. [http] [#3852]
* An internal server error is no longer produced when the command channel is
  closed while the data connection is waiting to connect.
  [ftp][ftps][server-side] [#3853]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The event with ID 10099 was removed and replaced with the event ID 10048.
  [ftp][ftps][server-side] [#3842]


Version 3.18.0, 2016-12-14
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible for event handlers to filter an event based on the UUID of
  the component which has generated the event.
* It is now possible to configure `email-sender` event handler to send an email
  with the associated file as an attachment.
* It is now possible to configure a template for generating the body of the
  email sent by the `email-sender` event handler.
* A group can now be configured to create a set of directories and
  subdirectories after an account is successfully authenticated.
* The audit message for loading a CRL was updated to include the date and time
  at which the CRL will be reloaded together with information about the date
  and time advertised by the CRL for the next publish and next update.
* The HTTP and Legacy WebAdmin authentication method were updated to support
  the new `home_folder_structure` configuration option.
* It is now possible to listen on Linux and Unix on ports below 1024 using a
  non-root user as long as the user or the SFTPPlus application was configured
  with the required capabilities / permissions. [server-side]


Defect Fixes
^^^^^^^^^^^^

* When a file is created and then moved immediately a single event is now
  emitted informing of the creation at the moved path. [#2311]
* When a file in a monitored location is modified and then moved/renamed now
  both the rename and modify events are observed. [#2311-1]
* Email event handler now ignores events emitted by the email client it's using
  to prevent vicious circle of loops. [#3620]
* On Linux and Unix systems, when the SFTP server-side creates new files, their
  permissions are filtered against the configured umask. This was a regression
  introduced in version 2.8.0, in which the umask value was not used for the
  newly created files. [sftp][security][linux][unix] [#3698]
* When the FTP server-side implementation fails to execute the requested NLST
  command an error is now created in the audit trail. [ftp][server-side]
  [#3717]
* Monitoring/watching a location is no longer stopped when a file is quickly
  moved then removed, moved then create another file with the same name or
  moved and then modify the moved file. [#3719]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The Port configuration option is no longer validated when saving, only when
  the value is used. Consequently the event with id 20011 is no longer used.
  [#3210]
* Default value for `email_subject` configuration option has changed. For now
  its default value equals to `[{id}] [{component.name}] New event from
  SFTPPlus`. [#3675]
* Event with ID 20028 is no longer used as the group configuration is no longer
  validated when it is defined, but only when it is used. [#3706]
* Events with ID 20054 and 20064 were removed and replaced with the event
  20031. The Event with ID 20031 was converted into a generic event emitted
  when the home folder or the home folder structure could not be created.
  [#3711]


Version 3.17.0, 2016-11-15
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to configure event handlers to ignore certain event IDs.
* The audit messages for initiating the FTP authentication and closing the data
  channel now contain the negotiated SSL/TLS protocol version and cipher name
  used to protect the connections. [ftps][server-side]
* It is now possible to configure the LDAP attribute used to associate the
  username when creating the full DN used for the BIND (authentication)
  operation. In previous version the BIND DN was always constructed using the
  `cn` attribute.


Defect Fixes
^^^^^^^^^^^^

* When a FTP command fails to be processed due to an internal server error, the
  error message will now display the root cause of the error.
  [ftp][ftps][server-side] [#3630]
* The FTP server-side protocol no longer blocks the whole SFTPPlus process when
  listing the content of a directory with many members. [ftp][server-side]
  [#3690]
* The server-side FTP command channel is now successfully closed after the FTP
  client is requesting the QUIT command. In the previous version (3.16.0) we
  have introduced a regression causing the command channel to close in a
  incorrect way and it was closed only after the timeout period. [#3691]


Version 3.16.0, 2016-10-26
--------------------------


New Features
^^^^^^^^^^^^

* For the FTP/FTPS services you can now use the MDTM, MFMT and SITE UTIME
  commands to set the modify time of a file. [ftp][server-side]
* It is now possible to configure `email_subject` configuration option using
  variable interpolation.
* The FTP/FTPS service now support the REST command for the REST, STOR and APPE
  commands. [ftp][server-side]


Defect Fixes
^^^^^^^^^^^^

* The javascript error "old_text is null" doesn't appear anymore on Local
  Manager when a user reviews a change with the empty old value. [#3625]
* Monitoring/watching a location is no longer stopped when a file is quickly
  moved to overwrite an existing file. [#3653]
* The processes executed by a transfer before and after a file is transferred
  are now executed as the SFTPPlus service account. In previous versions they
  were executed as the `root` account leading to possible security issues.
  [client-side][security] [#3668]
* An internal error is no longer generated for STOR and APPE FTP commands when
  failing to open the requested file due to a generic error. [ftp][server-side]
  [#91]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Variable notation `%(event_id)s` for `email_subject` configuration option
  (event handler of type `email-sender`) has been deprecated. It is preserved
  for backward compatibility. Use context variables instead for customization
  of the subject. See documentation for `email_subject` for more details.
  [#3647]


Version 3.15.0, 2016-10-24
--------------------------


New Features
^^^^^^^^^^^^

* On Local Manager you can now access the configuration page of a component
  directly from the "Require restart" section of the "Review changes" page.
* The FTP/FTPS service can now be configured to not show the product name and
  version as part of the FTP banner / welcome message.


Defect Fixes
^^^^^^^^^^^^

* The FTP command channel timeout is no longer ignored after a RETR command.
  [ftp][server-side]. [#2078]
* WinSCP FTPS client functionality no longer times out when connecting to the
  FTPS (implicit or explicit) server side implementation of SFTPPlus. [#3243]


Version 3.14.0, 2016-10-19
--------------------------


New Features
^^^^^^^^^^^^

* The CRL can now be reloaded based on the CRL Next Publish extension, when the
  CRL has this extension defined.


Defect Fixes
^^^^^^^^^^^^

* Fix the typo in the message of the event with ID 20178, where `CRL` was
  referred as `CRP`. [#3623]


Version 3.13.1, 2016-10-31
--------------------------


Defect Fixes
^^^^^^^^^^^^

* The processes executed by a transfer before and after a file is transferred
  are now executed as the SFTPPlus service account. In previous versions they
  were executed as the root account leading to possible security issues.
  [client-side][security] [#3668]


Version 3.13.0, 2016-09-13
--------------------------


New Features
^^^^^^^^^^^^

* Add support for authenticating SFTPPlus application accounts based on a
  remote LDAP server.
* Explicit FTPS is now a supported protocol for the location used in client
  side transfers.
* When a service using SSL/TLS is configured to not enforce client from a
  certain certificate authority, certificates received from the clients are
  completely ignored.
* It is now possible to configure a custom format string for the Log File event
  handler using the option `entry_content`.
* It is now possible to configure a local file event handler to rotate the file
  each month on a specific day.
* Implicit FTPS is now a supported protocol for the location used in client
  side transfers.
* After applying the configuration changes using the Local Manager, the
  components requiring restart after the changes are now also listed on the
  "Review changes" page and you can restart them from this same page.
* An audit entry is created when a CRL is loaded, informing the date and time
  of the next update for this CRL.
* The digital signature validation event handler can now check if the
  configured certificate is not part of a CRL.


Defect Fixes
^^^^^^^^^^^^

* Database event handler and account activity report now check database and
  table permissions for INSERT/UPDATE and DELETE on start. If permissions are
  not properly configured they will fail to start and report the cause. [#3219]
* The user account is now correctly registered in the Account Activity Report.
  [#3585]
* On Solaris 10 is it now possible to authenticate FTPS clients using an
  SSL/X.509 certificate generated by latest CAs and using UTF8STRING. In
  previous releases, Solaris 10 was expecting that UTF-8 values are stored in
  BMPSTRING fields. [#3610]
* The digital signature validation event handlers can now work with X.509
  certificates version 1 which have an implicit version field. Newly generated
  certificates are at least at version 3 and have an explicit version field, so
  this defect had a very low impact. [#3614]


Version 3.12.0, 2016-08-01
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to load the certificate revocation list based on the CRL
  distribution points extension advertised by the peer's certificate.
* It is now possible to use the `fips` configuration value in the
  `ssh_cipher_list` configuration option to allow using only FIPS 140-2
  compliant ciphers and algorithms for the SSH-based services.
* Event handlers of type local-file are now emitting an event after each
  rotation.
* The local file event handler now supports in place rotation. This will reset
  the file content without keeping any rotated copy.
* Accounts authenticated using the HTTP authentication method can now be
  configured to be associated with any group defined in SFTPPlus. In previous
  implementation they were always associated with the default group.
* You can now authenticate legacy SFTPPlus WebAdmin accounts as operating
  system accounts using the "User Alias" configuration option defined by the
  WebAdmin.


Defect Fixes
^^^^^^^^^^^^

* An internal server error is no longer emitted when a response from the Local
  Manager is produced after the Local Manager page was closed or refreshed.
  [#1890]
* Certificates signed by unknown certificate authorities are now rejected right
  away, without being first checked for revocation. [#2466]
* Transfers will no longer fail shortly after being started or resumed when the
  source locations fails. The transfers enter the `suspended` stated and will
  automatically resume once the source is available. [client-side] [#3441]
* When a transfer is active after being stalled due to a failure occurred at
  the source location, it will re-check that source path exists. In previous
  version, the source path was only checked when the transfer was started or
  resumed. [client-side] [#3441]
* An internal server error is no longer produced on Linux and Unix when the
  product is started with a configured service account which doesn't exist.
  [#3473]
* An internal server error is no longer generated for a transfer when failing
  to close the source file after failing to open the destination file.
  [client-side] [#3512]
* Rotating files base on size will now keep all rotated files when
  `rotate_count` is set to `0`. [#3531]
* The HTTP/HTTPS service will now request the web browser to download files
  with unknown mime types (extensions) rather than trying to display them as
  HTML files. [server-side][http] [#3533]
* Home folder path configuration can no longer be defined with empty values.
  This prevents accidental configuration in which the account is given access
  to the application's installation folder. [security] [#3537]
* Home folder path configuration is now enforced to absolute paths. This
  prevents accidental configuration in which the account is given access to the
  application's installation folder. [security] [#3537]
* An internal server error is no longer generated when an invalid path is
  configured as a home folder for users when running on Windows operating
  systems. [#3529]
* An internal server error is no longer generated when home folder creation
  fails due to an invalid home folder path configured. [#3529]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with id 20053 was removed and replaced with event 20031. [#3529]


Version 3.11.2, 2016-11-16
--------------------------


Defect Fixes
^^^^^^^^^^^^

* Monitoring/watching a location is no longer stopped when a file is quickly
  moved to overwrite an existing file. [#3653]
* On Linux and Unix systems, when the SFTP server-side is creates new files,
  their permissions are filtered against the configured umask. This was a
  regression introduced in version 2.8.0, in which the umask value was not used
  for the newly created files. [sftp][security][linux][unix] [#3698]


Version 3.11.1, 2016-10-26
--------------------------


Defect Fixes
^^^^^^^^^^^^

* The processes executed by a transfer before and after a file is transferred
  are now executed as the SFTPPlus service account. In previous versions they
  were executed as the `root` account leading to possible security issues.
  [client-side][security] [#3668]


Version 3.11.0, 2016-06-09
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to configure a list of ciphers used by the SSH-based
  services. You can now configure the accepted symmetric encryption, key
  exchange and MAC algorithms. [sftp][scp]
* The certificate revocation lists can now be refreshed based on the value
  advertised in the `Next Update` field.
* It is now possible to load CRLs from local filesystem in both PEM and DER
  format. Previously only the PEM format was supported.
* When the destination location of a transfer is not available, the file
  changes detected on source are observed but not processed. [client-side]
* Now it is possible to use the `all` option when configuring
  `ssh_cipher_list`.
* Add support for certificate revocation lists (CRL) when configured with
  Certificate Authority (CA) certificates.
* Support was added for SUSE Enterprise Linux 10 SP3 on X86_64.
* Certificate revocation list can now be loaded over HTTP.
* It is now possible to configure a service with a list of certificate
  revocation lists (CRL).


Defect Fixes
^^^^^^^^^^^^

* Database event handlers will now resume once the associated database becomes
  available again. [event-handlers] [#3258]
* Services using TLS/SSL will now fail to start when configured with a CRL
  which has a `Next Update` field earlier than current time. [ssl][tls] [#3266]
* The configured certificate revocation list is now validated against the
  configured certificate authority. A failure is raised when the CA doesn't
  match the CRL. [security] [#3270]
* The state of a transfer is now correctly reported as stopped, when the
  transfer was stopped while in the `stalled` state. [client-side] [#3431]
* Properly and conservatively escape paths in the `admin-commands.sh` and
  `client-shell.sh` Unix shell scripts to allow for paths with spaces. Portably
  check for errors in `admin-commands.sh` and `client-shell.sh`. [#3442]
* Values for the `type` configuration options are now case-insensitive. [#3449]
* Local Manager web GUI was updated to instruct web browser to update HTML
  pages cached from previous versions. [#3486]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The default value for `ssl_certificate_revocation_list_refresh` is now `0` to
  allow refreshing of CRLs based on the advertised `Next Update` field. [#3266]


Version 3.10.1, 2016-05-11
--------------------------


Defect Fixes
^^^^^^^^^^^^

* Account activity monitor table uses indexed columns for improved performance.
  [event-handlers] [#3281]
* An internal server error, which was observed when stopping a location or a
  transfer, was fixed [client-side] [#3440]
* Files that are open for writing and kept open by other processes are skipped
  when transferring until they are closed by all other processes. [#3452]


Version 3.10.0, 2016-05-10
--------------------------


New Features
^^^^^^^^^^^^

* It is now possible to configure the default data type used by the FTP
  service, in transfers for which the client is not explicitly requesting a
  transfer type. [ftp][ftps][server-side]


Defect Fixes
^^^^^^^^^^^^

* The `admin-commands.sh` script was updated to work in environment which don't
  export the `PATH` variable. Such environments are rare but can be
  encountered for example when using `cron`. [#1403]


Version 3.9.0, 2016-04-29
-------------------------


New Features
^^^^^^^^^^^^

* Event with ID 20181 is now emitted when all server components have started.
* Add configuration option to filter an event based on account names.
  [event-handlers]
* It is now possible to configure the FTP and FTPS services to pretend that
  ASCII data type is supported, while the actual data is transferred in IMAGE
  mode. [ftp][ftps]
* Allow configuring rules for re-trying failed connection to a location. This
  can produce a fault-tolerant location. [client-side]


Defect Fixes
^^^^^^^^^^^^

* Log entries stored in databases are indexed for improved performance.
  [event-handlers] [#3280]
* Now adding a Syslog Event Handler using the target configuration option will
  save the values. [#3402]
* Transfers for which the source location has failed are now entering the
  `Stalled` state and will be automatically resumed once the location is
  available. [#3425]
* Locations and transfers are now successfully auto-stopped when their
  configuration is removed. [#3429]
* It is no longer possible to delete a location if it is configured as source
  or destination for a transfer. [#3429]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with ID 20108 is now use to signal any configuration delete request
  which was blocked as the configuration is already used by another component.
  ID 20108 was previously used only for database configurations. [#3429]
* Events with IDs 20088, 20175, 20176, and 20178 were converted into 20108.
  [#3429]


Version 3.8.0, 2016-04-21
-------------------------


New Features
^^^^^^^^^^^^

* Event with ID 10042 is now emitted for all FTP command channels which are not
  closed in a clean way. [ftp][ftps]
* A sample systemd unit file was added, together with documentation for setting
  up SFTPPlus as a systemd service.
* Change the human readable text message for the FTP 226 response from
  "Transfer Complete." to "Transfer complete." to work around some FTP clients
  which are also validating the human readable text. [ftp][ftps]
* Add support for Syslog over TCP as documented in RFC 6587. [syslog]
* Add support for Ubuntu 16.04 LTS on X86_64
* Add support for running SFTPPlus on hardened Linux system in which the
  OpenSSL library is compiled only with TLS support and in which SSL
  (v2 and v3) are not available.


Defect Fixes
^^^^^^^^^^^^

* The digital signature event handler will now reject reading and validating
  files with lines longer than 16,000 character. This was done to prevent
  handling accidental binary files. [event-handlers] [#3201]
* The digital signature file handler was updated to support a simple format in
  which the whole file content is validated and in which the signature is
  appended to the end of the file using a comma delimiter. [#3365]
* Improve error handling when loading incomplete SSH keys. [#2545] [#3408]
* SSH key import now fails when a password is specified for an unencrypted
  private key. [#2547] [#3408]
* Transfers that process multiple files in distinct batches are working now.
  [client-side] [#3409]
* Syslog messages are now formatted according to RFC 3164 also known as
  syslog-bsd. [#3410]
* Fix new line delimiter conversion for server-side FTP downloads in ASCII
  mode. [ftp][ftps] [#3413]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `address`, `port` and `path` configuration options of the SysLog event
  handler are now deprecated and replaced by the `url` configuration. They
  continue to work in the current major release, but will be removed in the
  next major release. [syslog] [#3395]


Version 3.7.0, 2016-03-28
-------------------------


New Features
^^^^^^^^^^^^

* The OpenSSL version distributed in our Windows version was updated to OpenSSL
  1.0.2g. [ftps][https]
* Update the generic error handling to include more messages when running as
  normal server. Previously, these log messages were available only in the
  debugging mode.
* SFTP and SCP server-side file close operations now emit dedicated event ids.
  In this way you can filter file upload or download operations based on a
  specific event ID. The previous event with ID 30017 is now used only when the
  file was not opened in read-only or write-only mode. [SFTP][SCP]
* Allow simple negation of the regular expression used in source filter. In
  this way you don't need to use look-around zero-length assertion regex rules
  to exclude a certain pattern.
* The SSH protocol was updated to support hmac-sha2-256,
  diffie-hellman-group14-sha1, and diffie-hellman-group-exchange-sha256.
  [sftp][scp]


Defect Fixes
^^^^^^^^^^^^

* The SCP server-side implementation now sends a response for successful SCP
  initialization, before starting to process the SCP transfer requests. This
  fixes a bug in which the Cisco SCP client (SSH-1.99-Cisco-1.25
  implementation) hangs when SCP is initialized. For example when running `copy
  start scp://10.0.2.1/some-file`. [scp] [#3356]
* Allow using the file dispatcher with any event from the `file-operation`
  group. Previously only the FTP upload events were supported. [#3366]
* Documentation for matching expressions was fixed to include examples with
  valid regular expressions. [monitor][transfers] [#3373]
* An internal server error was fixed caused by invalid regular expressions
  defined for the `source_filter` configuration option of a transfer.
  [client-side] [#3374]
* Fix parsing the SCP arguments for client sending command line arguments with
  leading spaces. This affect the integration with the SCP client available on
  Cisco ASA and ASAv systems. [scp] [#3376]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `path` data attribute for events with ID `10074` was change from `from`
  to `to` so that the `path` and `real_path` attributes point to an existing
  path. [ftp][ftps] [#3366]


Version 3.6.0, 2016-03-17
-------------------------


New Features
^^^^^^^^^^^^

* Service monitor now emits dedicated events for files and folders which
  already exists when service is started.
* The OpenSSL version used by SFTPPlus is advertised as part of the events
  generated when starting the SFTPPlus process, as well as in the Local Manager
  status page.
* Now you can configure the source port used by the FTP and FTPS services to
  initiate active data connections. [ftp][ftps]
* Allow generating certificate signing requests using exceptionally reserved
  country codes like UK, UN, EU and others.
* When HTTPS connection fails due to SSL/TLS errors a dedicated event is
  emitted.
* The matching rules for file dispatching are now applied to the full path, not
  only to the file name.


Defect Fixes
^^^^^^^^^^^^

* Fix an internal server error produced when removing the account configuration
  for an account which has still active connections. [#3060]
* When a transfer requires multiple files to be transferred, they are now
  queued so that the files are transferred sequentially, one at a time. [#3131]
* When a location fails to start, it is no longer auto-started by a transfer.
  Now it needs to be manually started after the failure was investigated. All
  components/transfer trying to use a location which failed, will also have
  their operation failed. [#3176]
* Locations are now auto-started in the correct state, emitting an event and
  not leaving them in a 'restart-required' state. [#3176]
* When no type specified for new account it will be created as an application
  account. [#3213]
* The file transfer services secured by TLS/SSL and using a CRL will
  automatically stop/fail if the CRL can not be updated at runtime. In previous
  versions a warning was raised but the file transfer service continued to
  operate with a version of CRL which was previously loaded, resulting in an
  insecure operation. [security] [#3216]
* The files already present on the source location for a transfer are now
  filtered based on the transfer configuration and processed only after they
  are stable. [#3223]
* In the Local Manager the `Enabled` label for the configuration options was
  renamed to `Enable at startup` to provide a better description of its effect.
  [#3256]
* The file dispatcher event handler now no longer enters an infinite loop by
  handling its own events. [#3261]
* The dedicated event with ID 20077 is emitted when failing to start a file
  transfer service due to errors in SSL/TLS setup. In previous versions only
  the event with ID 20032 was emitted to signal the SSL/TLS setup error,
  without emitting event 20077 to signal that the service failed to start.
  [ftps][https] [#3271]
* No internal server error is now produced when failing to remove the remote
  file after the file was successfully transferred on the local machine.
  [client] [#3283]
* Loading a non-existent page in the Local Manager now produces a single event
  with ID 40001. [local-manager] [#3285]
* Starting the Local Manager or the documentation pages from the Windows Start
  menu or using the command line using the `admin-commands manager` command,
  now successfully opens the default browser. [local-manager] [#3295]
* Locations and resources now completely ignore the `enable` configuration
  option as they are auto-started when a component needs them. They are no
  longer automatically started at process launch if another component doesn't
  need them. [#3305]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with ID 20037 and 20141 were replaced by the event with ID 20036. Event
  with ID 20039 was replaced by the event with ID 20040. [#3216]
* Events with ID 20033, 20035, 20092, 20093, 20094, 20095, 20096 and 20140 were
  replaced with the generic event dedicated to start failures 20077. [#3216]
* Event with ID 20040 was converted into a generic event emitted for any client
  certificate validation error. [#3216]
* Databases no longer have the `enable` configuration option as they are
  auto-started on demand. In the Local Manager, the status for the databases
  and the locations was merged into the resources status. [#3256]
* Events with ID 20044 and 20098 were replaced by the generic ID 20010. [#3305]


Version 3.5.1, 2016-02-05
-------------------------


Defect Fixes
^^^^^^^^^^^^

* Event with ID 20024 is now emitted for internal errors caused by unhandled
  runtime errors. [#3242]
* Include the sample `Library_LaunchDaemons_sftpplus.plist` file in the
  distributable archive. Documentation was updated to document the filesystem
  permissions required for the service account. [osx] [#3238]
* Fix SCP protocol interoperability with the OpenSSH scp command. [scp] [#3240]


Version 3.5.0, 2016-01-25
-------------------------


New Features
^^^^^^^^^^^^

* Add an event handler which can validate the trailing, comma separated,
  digital signature.
* Add an event handler which can dispatch a file in one or multiple destination
  directories based on a set of matching rules.
* The monitor service can now emit events for files which were not modified in
  a configured number of seconds.
* Upgraded bundled OpenSSL to version 1.0.2d for Windows distributions.
  [windows][https][ftps]


Defect Fixes
^^^^^^^^^^^^

* Authentications that are being used by other components are no longer
  removed. A dedicated failure event will be emitted. [#3211]


Version 3.4.0, 2015-12-22
-------------------------


New Features
^^^^^^^^^^^^

* When a component needs a restart, in the Status page of the Local Manager
  now is displayed the list of configuration options which determine the
  required restart.
* Add a new event handler which can send a copy of the events as email.
* Add configuration for defining an email client component which can be used
  to send email via a remote SMTP server.


Defect Fixes
^^^^^^^^^^^^

* Configuration for `local-file` event handler from the Local Manager GUI
  is now fixed.
  [#3152]
* Fix client transfers for destination locations which were not been previously
  started.
  [#3175]
* Events emitted during SFTPPlus' startup before any event handler is started
  are now buffered and sent to the first event handler which is started.
  [#2989]


Deprecations
^^^^^^^^^^^^

* Events with ID 20122, 20131, 20132 were removed as they were never used
  directly. The already event with ID 20044 will contain the error details.
  [#3147]
* Events with ID 20147 and 20148 were removed and replaced with the existing
  event ID 20010.
  [#3147]


Version 3.3.0, 2015-12-09
-------------------------


New Features
^^^^^^^^^^^^

* Event with ID 20136 now also includes the type of the credentials which were
  rejected by the authentication method.
* Add support for the FTP CLNT command. The command was implemented to prevent
  generating an error when a FTP client is sending this command, and the
  received client name is ignored.
* Extend the OS authentication method to provide explicit configuration for the
  PAM authentication used on Linux, OSX, and AIX.
  You can now configure a custom PAM service name. In previous versions the
  PAM service name was hardcoded as `login`.


Defect Fixes
^^^^^^^^^^^^

* `admin-commands debug` output now correctly shows audit/log messages
  containing non US-ASCII characters.
  [#3117]
* The `pam_unix` PAM module is no longer ignored by the `os` authentication
  module as the PAM authentication can now be configured as the preferred
  method.
  In previous versions if the `pam_unix` PAM module was configured in the
  `login` PAM service, SFTPPlus was ignoring the PAM configuration as it was
  doing direct checks for the /etc/passwd and the /etc/shadow files.
  [#3054][linux][unix]
* Fix parsing of the FTP command `TYPE A N`.
  [#3149][ftp]
* Remove trailing carriage return characters from the path used in the FTP RETR
  command. This should fix transfer failures in the AIX's FTP client when mget
  is used in binary mode.
  [#3149][ftp]


Deprecations
^^^^^^^^^^^^

* Event with ID 20008 was removed and replaced with the generic authentication
  failure event with ID 20136.
  [#3054][sftp]


Version 3.2.1.aixpam1, 2015-11-24
---------------------------------

* On AIX, disable OS account authentication from /etc/passwd and only use PAM
  authentication.[aix]


Version 3.2.1, 2015-11-17
-------------------------


Defect Fixes
^^^^^^^^^^^^

* When database event handler is unable to process events at the speed they
  are produced and the internal queue is full it will emit a failure event.
  [#3084]
* Improve product responsiveness while monitoring big recursive directory
  structures.
  [#3085]
* Fix PAM authentication on AIX.
  [#3097][aix][os-accounts]
* Add a dedicated SFTPPlus package for AIX 7.1. The SFTPPlus AIX 5.3 package is
  working on AIX 7.1 only if OpenSSL 0.9.8 is also installed on AIX 7.1.
  [#3097][aix]


Version 3.2.0, 2015-10-30
-------------------------


New Features
^^^^^^^^^^^^

* Add support for blocking source IP address if they generate consecutive
  failure attempts. This is implemented using a dedicated authentication
  method.
* Add support for anonymous accounts using the
  `Anonymous Authentication Method` as specified in RFC 1635.
* Allow defining specific authentication methods per service. You can still
  use the global authentication methods.
* Add support for the FTP LANG command as described in RFC 2640. For now
  only English is supported. The command will accept any language
  request while preserving English for server greetings and the textual part of
  the command responses.


Defect Fixes
^^^^^^^^^^^^

* SFTP client events with ID 70001, 70002, 70003, 70006 and 70007 now include
  the name of the associated SFTP location.
  [#2552][sftp]
* The multi-line response of the FEAT command now uses FTP new lines
  ``\r\n`` rather than Unix new lines ``\n``.
  [#3074][ftp][ftps]
* When the client is requesting an unsupported option using the OPTS command
  the server now replies with error code 501 (option not implemented),
  rather than the generic 502 (command not implemented).
  [#3074][ftp][ftps]
* Support for the EPSV and EPRT commands from RFC 2428 is now advertised in
  the response of the FEAT command.
  [#3063][ftp][ftps]
* When a service monitor is configured with an unknown source path, it now
  fails to start.
  [#2676]
* Fix an internal server error triggered by a rare condition in which both
  the FTP command and data channel generate a timeout in the same time.
  [#3079][ftp][ftps]


Deprecations
^^^^^^^^^^^^

* Event with ID 70004 was replaced by 70008 as it was a duplicate.
  [#3033][sftp]


Version 3.1.0, 2015-10-09
-------------------------


New Features
^^^^^^^^^^^^

* Added support for recursive monitor services.
* Event with ID 20137 now includes the accepted credentials type in the
  human readable message. Credentials type were already part of the
  event's data.
* A dedicated event with ID 30005 is now used when an unknown SSH message
  id is requested.
  [#3026][sftp][scp]
* A dedicated event with ID 30006 is now used for internal server error
  while processing the SSH requests.
  [#3026][sftp][scp]


Defect Fixes
^^^^^^^^^^^^

* The SFTP service can now be identified using DSA (ssh-dss) SSH host keys.
  It no longer ignores the configured DSA keys.
  [#3021][sftp]
* On Linux, when failing to get a file descriptor for /dev/urandom the
  SSH layer no longer generates an internal server error but will fall
  back to a simpler random generator.
  [#3025][sftp][scp][linux]
* When the SFTP service receives an authentication request for an unknown
  SSH authentication method it now emits a dedicated event, rather than
  an internal server error event.
  [#3026][sftp][scp]
* On Linux and Unix, when running under a dedicated service account,
  you can now use port below 1024 for the file transfer service.
  [#2987][unix][linux]
* Events with ID 20060, 20094, 20095, 20096, 70004, 70008 now have a valid
  text representation.
  [#3027]
* Stopped event handlers no longer emit error information for events which
  failed to be processed. [#2991][event-handlers]
* Allow PROT command to be issued by a FTPS client before the USER command.
  [#3016][ftps]
* Fix an internal server error when the FTP specific AUTH command is issued
  by a client for a FTP service for which the FTPS extensions were not
  enabled.
  [#3016][ftps]
* Display a warning when Local Manager UI is accessed in Compatibility View
  mode in Internet Explorer browser.
  [#3020][local-manager]
* Display a warning in the logon page if it's using an unsupported IE version.
  [#3028][local-manager]


Deprecations
^^^^^^^^^^^^

* Removed Startup column in Local Manager Status page for locations as they
  are started on demand.


Version 3.0.0, 2015-09-18
-------------------------


Major Changes
^^^^^^^^^^^^^

* The product was renamed from SFTPPlus Server to just SFTPPlus. In some
  places, to avoid confusing it with the previous SFTPPlus Client, the new
  SFTPPlus product is referred to as SFTPPlus MFT.
* All log handlers were converted to event handlers. This allows an unified
  method for interacting the the audit events produced by SFTPPlus.
* All authentication methods are now explicitly defined and ordered.
  You can now choose the order in which different authentication methods are
  used.
* Client-side file transfers were introduced using `locations` and `transfers`.
  Locations represent the endpoint servers used by the file transfers.
  Transfers represent the rules for exchanging files between locations.
* On Linux and Unix, when running the process using a dedicated service
  account, all event handlers and the log files are handled by the dedicated
  service account.
  In the previous version they were handled as the `root` account.

Please consult the documentation for upgrade instructions.


New Features
^^^^^^^^^^^^

* Added support for SUSE Linux Enterprise Server 12 on Intel x86_64.
* Added support for Red Hat Enterprise Linux 6 and Generic Linux on
  IBM System z s390x mainframe and the Hercules mainframe emulator.
* Added support for Red Hat Enterprise Linux 6 on POWER8 (big endian).
* Added support for Ubuntu 14.04 LTS on POWER8 (little endian).
* Added support for Generic Linux on IBM Systems z s390x mainframes and the
  Hercules mainframe emulator.
* Added support for Generic Linux on IBM Power Systems POWER8 in big and little
  endian versions.
* Added support for Solaris 11 on SPARC.
* Now, each time the `401 Unauthorized` response is sent by the HTTP service,
  the event with id `40000` is emitted with details about the reason why
  that response was given.
* Added support for configuring the number of consecutive errors after which
  the event handler and log handlers will automatically stop.
* Added an event handler which stores the received event in a local file.
  This is used to implement the log file functionality.
* Added an Account Activity event handler that keeps a record of the
  successful authentications of regular accounts and administrators.
  The records are stored in a database.
* Added Syslog event handler. It replaces the Syslog log handler.
* Added a new authentication method which allows denying users based on a
  pre-configured list of users.
* Added a dedicated authentication method for authenticating global accounts
  provided by the legacy SFTPPlus WebAdmin.
* Added a dedicated authentication method for authenticating application
  accounts defined in the configuration file.
* Added a dedicated authentication method for authenticating accounts provided
  by the operating system.
* Added event handler which sends events to the Legacy SFTPPlus WebAdmin.
* Events sent to the event handlers now also contains the full text as in the
  previous log system.
* Added `create-folder-if-missing` command to the HTTP JSON API of the HTTP
  service. It will allow creating new folders without raising an error when
  the folders already exists.
* Removed legacy SQLite/MySQL loggers. They were replaced by a generic database
  logger.
* Removed database log handler and replaced with a dedicated event handler.


Defect Fixes
^^^^^^^^^^^^

* Fix an internal server error generated while stopping the SFTPPlus process
  before it has finalized its start phase. [#2961]
* Read /etc/passwd files as the service account to get account information.
  In previous version the file was read as the root account.
  [#2845][linux][unix][os-account]
* Database connection will no longer stop after 10 consecutive
  failures, but rather the internal components using the database will stop.
  [#2818][database]
* Fix an internal server error occurring in the HTTP service when credentials
  were validly encoded to BASE64, but the payload was not validly encoded to
  UTF-8. [#2967][http]


Deprecations
^^^^^^^^^^^^

* Events with id 20109 and 20111 are no longer emitted. They are replaced
  by events 20156 and 20157. [#2818][database]
* Event with id 20051 is no longer emitted; it has been replaced by event 20158.
* The cipher suites based on RC4, DES (not 3DES), MD5 and weak export ciphers
  are disabled by default for SSL and TLS.
* Support for SUSE Linux Enterprise Server 11 has been updated from SP1 to SP3.
  SLES 11 SP1 and SP2 are no longer supported. We recommend upgrading to SP3
  or the forthcoming SP4. If you still need support for SP1, please contact us.
* Support for Ubuntu 10.04 LTS has been discontinued.
  If you still need support for 10.04, please contact us.
* Support for Ubuntu 12.04 LTS has been discontinued.
  If you still need support for 12.04, please contact us or try the Generic
  Linux versions.
* The server reports have been removed. They were replaced by the
  Account Activity event handler.
* Global accounts from the legacy SFTPPlus WebAdmin are no longer authenticated
  using a generic server configuration. They now have a dedicated
  authentication method, and you can choose the order in which global SFTPPlus
  accounts are authenticated, in respect with other account types. The
  following event IDs are no longer used: 20006, 20012, 20015, 20018, 20025,
  20026, 20027, 20029, 20030, 20048.
* Events with id 20009, 20061 and 20068 are no longer emitted.
* File log handler was removed and replaced with an event handler.
* WebAdmin HTTP Post Request log handler was removed and replaced with an
  HTTP event handler which uses the `legacy-webadmin` format.
* Legacy SQLite/MySQL log handlers were removed.
* The Syslog log handler was removed and replaced by a dedicated event handler.
* Database log handler was removed and replaced with a database event handler.
* Events 20133, 20134 and 20050 are no longer emitted. They are replaced by
  20161, 20162 and 20160 respectively.
* The process can now be started even if no services are configured to start
  at startup. Event with ID 20003 is no longer emitted.


Version 2.12.1, 28/09/2015
--------------------------


Defect fixes
^^^^^^^^^^^^

* Allow PROT command to be issued by a FTPS client before the USER command.
  [#3017][ftps]
* Fix an internal server error when the FTP specific AUTH command is issued
  by a client for a FTP service for which the FTPS extensions were not
  enabled.
  [#3017][ftps]


SFTPPlus Server 2.12.0, 26/04/2015
----------------------------------


New features
^^^^^^^^^^^^

* Added support for Solaris 10 on SPARC.
* `server-commands` command line tool was reorganized into sub-commands to
  improve readability of available options for each command.
* `server-commands start` options was added to help start the SFTPPlus
  Server on Unix and Linux as a daemon.
* Server SSH configuration is now initialized with an RSA key of size 2048.
* Added a version for generic x86_64 64bit Linux. This version is provided
  for testing purposes only. It is not supported for production use, where
  we advise you to deploy the version specifically built for your Linux
  distribution. Please contact us in case we don't have a release for your
  distribution yet.
* Add command line option to generate an SSL key and the associated certificate
  signing request / CSR.
* Add Local Manager option to generate an SSL key and the associated
  certificate signing request / CSR.
* Emit audit events when setting the representational type for FTP data.


Defect fixes
^^^^^^^^^^^^

* Fix an internal server error generated by the HTTP and HTTPS service
  when displaying the failure message for removing files or folders with
  Unicode names. [#2777][http]
* Fix generating of passwords from command line on Windows. [#2782][windows]
* Database connection and database log handlers now stop after 10 consecutive
  failures. [#2738][database]


Deprecations
^^^^^^^^^^^^

* `--start` option of `server-commands` command line tool was replaced by the
  `start` sub-command. It is still available to provide backward compatibility
  with previous init scripts, but will be removed in the next major release.
* `server-commands` command line tool was reorganized into sub-commands and
  the following commands were renamed:

  * `--generate-uuid` into `generate-uuid`
  * `--validate` into `validate`
  * `--debug` into `debug`
  * `--manager` into `manager`
  * `--documentation` into `documentation`
  * `--generate-key` into `generate-ssh-key`
  * `--generate-password` into `generate-password`
  * `--generate-uuid` into `generate-uuid`
  * `--start-in-foreground` into `start-in-foreground`
  * `--initialize` into `initialize`
  * `--migrate` into `migrate`


Deprecations
^^^^^^^^^^^^

* Remove support for RHEL 4. Please contact us if you still need to deploy
  on this RHEL version.


SFTPPlus Server 2.11.0, 27/03/2015
----------------------------------


New features
^^^^^^^^^^^^

* Support Solaris 11 for x86.
* Initial update for HP-UX 11iv3 support.
* Add support for ARM64 architecture on any Linux distribution providing the
  OpenSSL 1.0.X library.
* Update HTTP GET API for a folder to return content in JSON format.
* Update HTTP POST API for a folder to accept commands in JSON format.
* HTTP events with ID 40010, 40011, 40012 and 40013 were updated so that now
  `path` data will contain the actual file/folder which was removed/created
  and not the parent path.
* HTTP events with ID 40012 and 40013 are now emitted for each **file**
  which was removed and no longer aggregated into a single event.
* HTTP events with ID 40026 and 40027 are now emitted for each **folder**
  which was removed and no longer aggregated into a single event.


Defect fixes
^^^^^^^^^^^^

* Fix an internal server error generated by the HTTP and HTTPS service
  for invalid requests originating from accounts authenticated using the
  external HTTP authentication method. [#2758][http]


SFTPPlus Server 2.10.0, 13/03/2015
----------------------------------


New features
^^^^^^^^^^^^

* Allow filtering source files for monitored folders based on glob or regular
  expressions.
* When a file is closed in SFTP or SCP include in the emitted event the mode
  in which the file was opened.
* Add experimental modular authentication method over HTTP. This allows
  authenticating external accounts over HTTP as well as implementing
  a high-availability / resilient authentication.
* Add a `failure-critical` group for events which should not occur during
  normal server operation.
* Add experimental HTTP POST hooks for events.
* Add a version for generic x86 Linux. This is only for testing and
  evaluation and is not supported for production use, where we advise you
  to deploy the version specifically built for your Linux distribution.
* Monitoring local folders is now an officially supported feature, provided
  as part of server side services.
* Add support of ARM64 (ARMv8-A/AArch64) CPU architecture on Ubuntu 14.04.
  Please contact us if want to use SFTPPlus Server on ARM64 with a different
  operating system.


Defect fixes
^^^^^^^^^^^^

* Fix an internal server error generated by the FTP and FTPS service when
  a client issues a command which fails but then disconnects before receiving
  the command's response. [#2628][ftp][ftps]
* Allow EPSV command after EPSV ALL request. In previous versions all
  data connection command were denied, including EPSV. [#2566][ftp][ftps]
* Fix --validate server command option. [#2622]
* Convert transfer specific start/stop events into generic events for
  components. Changed events are:
  20135 -> 20156, 20136 -> 20157, 20137 -> 20158, 20138 -> 20159 [#2639]
* Fix internal server error when receiving an invalid or not supported public
  SSH key from the client. [#2623][sftp][scp]
* Improve error logging when launching the server in debug mode. [#2615]
* Experimental event ID 60007, 60008, 60009 were change to generic external
  command execution.
* Fix Windows EventLog handler to record the IDs for events. In previous
  releases it was always using id `1`. [#2676][windows]
* Fix an internal server error when removing from Local Manager a
  component which was already running. Introduced in 2.6.0. [#2684]
* Fix database logger memory usage footprint. In previous versions the database
  loggers consumed significant amounts of memory when a lot of events were
  logged. [#2413]
* Fix resetting the maximum failures count after restarting a database
  component. [#2736]


Deprecations
^^^^^^^^^^^^

* `protocol` configuration option for a service was replaced with `type`
  configuration option. This should help create an uniform configuration
  process, in which each configurable object has a standard `type` option.
  For backward compatibility, `protocol` option still works but it will be
  removed in the next major release. [#2563]
* Experimental event ID 60011, 60019, 60020, 60021, 60022, 60023, 60024 were
  removed.
* We no longer provide support for Ubuntu Server on x86. For testing you can
  now use our generic Linux x86 version. If you still need Ubuntu Server x86
  for production, please contact us and we will make it available to you.


SFTPPlus Server 2.9.0, 09/12/2014
---------------------------------


New features
^^^^^^^^^^^^

* Allow configuring SSH key authentication by directly associating
  public SSH keys with an account. Authorized public SSH keys can now
  be stored in configuration file, rather than on a separate file.
* Event monitors will automatically restart on configuration changes.
* Log an error when an account is configured with invalid public SSH keys
  [#998][sftp][scp]
* To prevent creating huge log files, the default configuration creates a log
  file which is automatically rotated at the end of the day.
* Allow importing/exporting public and private SSH keys
  (including encrypted private keys) to and from the following formats:

  * OpenSSH
  * SSH.com (Tectia SSH and other commercial implementations)
  * PuTTY

* Show public SSH key MD5 fingerprint when importing a public SSH key from
  Local Manager. [sftp][scp]
* Generate SSH keys from Local Manager. [sftp][scp]
* Allow configuring a static IP address to be advertised in the PASV
  response for the case when server is accessed from behind a NAT. [ftp][ftps]


Defect fixes
^^^^^^^^^^^^

* Fix monitoring local files. [#2472]
* Use valid default values when creating a new SSH (SFTP/SCP) service from
  local manager. [#2485][sftp][scp][local-manager]
* Fix deleting `read only` files on Windows, or folders containing `read only`
  files. In previous versions, files were prevented to be removed with an
  access denied error. [#2467][windows]
* Fix keeping Local Manager session alive while web browser page is open.
  [#2532][local-manager]


SFTPPlus Server 2.8.0, 24/10/2014
---------------------------------


New features
^^^^^^^^^^^^

* Add support for Red Hat Enterprise Linux 7 x86_64 and CentOS 7.
* Add support for Apple OS X 10.8 Mountain Lion.
* Add configuration option to disable TLS version 1.1 and 1.2.
  In previous version TLS versions 1.1 and 1.2 were always enabled and
  there was no configuration option to disable them.
  There is no known vulnerability in TLS version 1.1 and 1.2 and
  for now, there is no reason to disable them. This option was added as a
  proactive measure in case a vulnerability is discovered in these versions.
* Allow refreshing the CRL stored as local file using the
  `ssl_certificate_revocation_list_refresh` configuration option.


Defect fixes
^^^^^^^^^^^^

* Fix loading of CRL files from disk. [#2465][ftps][https][local-manager]


Deprecations
^^^^^^^^^^^^

* Support for SSLv3 in FTPS and HTTPS services is discouraged due to the
  SSLv3 POODLE vulnerability.
  It is still possible to use SSLv3, but the server will emit a warning
  informing that SSLv3 is no longer secure and will be removed in future
  versions. When SSLv3 is still required, it is highly recommended to use a
  non-CBC cipher, for example RC4-SHA.


SFTPPlus Server 2.7.0, 18/09/2014
---------------------------------


New features
^^^^^^^^^^^^

* Add support for Ubuntu 14.04 LTS x86_64.
* Add support for FTP SITE CHMOD command on Unix and Linux.
* Add support for obsolete FTP commands XCUP, XCWD, XMKD, XPWD, XRMD as
  described in RFC 775.
* Add support for executing external command on files from monitored folders.
* Add an option to configure the amount of time after which a file is
  considered stable, if no changes are made to it.


Defect fixes
^^^^^^^^^^^^

* FTP data channel stops accepting new connection as soon as FTP client
  connects to the data channel. In previous version the data channel stops
  accepting new connections only when the FTP client requested the close
  of data channel. This case should reduce the time a data channel port
  is used and allow it to be reused faster in another session. [#2354]
* For FTP transfer, fix a data channel error which was returned when a new
  data channel was requested after the previous requested data channel timed
  out. [#2354]
* Fix an internal server error when FTP client drops the connection during a
  transfer [#2355][ftp].
* Fix FTP text/ASCII transfer to Unix and Linux server [#1024][ftp].


SFTPPlus Server 2.6.0, 07/08/2014
---------------------------------


New features
^^^^^^^^^^^^

* Update support for Solaris x86_64. Solaris support was temporarily
  discontinued after version 2.0.0 was launched.
* Add new "force-stop" command for the Unix init script to be used when PID
  file would be missing or kill -9 is required to stop the server.
* Add dedicated configuration for databases used by the server to allow using
  the same database for both log handlers and activity reporting.
* Log handlers attached to a database are now configured using the shared
  databases configurations. The old method of directly configuring a SQLite
  or MySQL connection is obsolete.
* Last account login information is collected and available as a report from
  the Local Manager UI. Data is stored in a user definable database.
* Experimental feature to monitor local filesystem paths and audit changes
  to files and folders. See documentation for more info. In the next release, we
  plan to allow the execution of an external command based on observed changes.
* On Linux and Unix, add support for FTP SITE CHMOD command.


Defect fixes
^^^^^^^^^^^^

* When upgrading the server on Windows, the existing configuration file is no
  longer overwritten.
* Fix ssh_authorized_keys_path expansion of username when placeholder
  has not been defined for group path. In the previous version, when a path for
  a group did not contain a placeholder, it was used as such, without appending
  the username. [#2199][sftp]
* Improve error reporting when failing to save configuration file, due to
  permissions errors. [#2193][local-manager]


Deprecations
^^^^^^^^^^^^

* It is no longer possible to configure a log handler directly attached to a
  database. Due to this a log handler with `type`: `sqlite` or `mysql` is
  no longer supported. Those options are replaced by `type: database`.
  Users now have the option to configure a log handler with a shared
  database configuration.


SFTPPlus Server 2.5.0, 03/06/2014
---------------------------------


New features
^^^^^^^^^^^^

* Add support for downloading and uploading a single file using SCP.
  For now, SCP protocol is very limited and available as a preview.
* Add new configuration option to independently enable SCP or SFTP support
  inside the SSH service.


Defect fixes
^^^^^^^^^^^^

* Fix an internal server error when SSH client requests to execute a command,
  a shell or a pseudo-terminal. [#2116][sftp]


Removals
^^^^^^^^

* Event with ID 30049 emitted when trying to open a folder as a file was
  removed and replaced with the generic file open error ID 30044. [#2130][sftp]


Deprecation
^^^^^^^^^^^

* `protocol: sftp` for service configuration was replaced with `protocol: ssh`
  to permit configuring SCP protocol on same service/port as SFTP service.
  `sftp` still works and is an alias for `ssh` but it will be removed in the
  next major release.


SFTPPlus Server 2.4.0, 14/04/2014
---------------------------------


New features
^^^^^^^^^^^^

* Add support for uploading files with unlimited size over HTTP and HTTPS.
  This puts HTTP/HTTPS service capabilities in line with SFTP and FTP/FTPS
  services.
* Add support for application accounts for creating and reading symbolic links
  on Windows using SFTP protocol. On Unix/Linux symbolic link support was
  already available.
* Add connection limits for HTTP/HTTPS file transfer services and
  Local Manager service.
* Allow disabling account passwords from Local Manager.
* Add more details to audit trail when reporting failures for SFTP service.
* Add more details to audit trail when reporting failures for FTP/FTPS service.
* Add details for FTP active and passive data connection failures.
* Add `development mode` for Local Manager service to help audit Local
  manager code and actions.
* Fix a JavaScript error logged in browser console while applying changes
  for services.


Defect fixes
^^^^^^^^^^^^

* Fix page not found error generated while configuring a Windows EventLog from
  Local Manager.
* Fix FTP/FTPS service for listing folders with names similar to FTP globbing
  expressions.
* Fix configuring idle_connection_timeout to a disable value from both
  configuration file and Local Manager.
* Fix disabling of maximum connection limit from Local Manager for all services.
* Fix FTP/FTPS service for listing folders with names similar to FTP globbing
  expressions.
* Fix an error in FTPS service reconfiguration where FTPS service failed
  after Explicit FTPS was enabled.
* Fix accessing files over HTTP/HTTPS service for operating system accounts
  which are not locked inside home folder.
* Add account name to SFTP disconnect event (id 30015) for connection which are
  authenticated.
* Fix a condition in which SFTP subsystem closed event (id 30012) was emitted
  twice.
* In Unix and Linux fix listing of symbolic links to folder using the same
  visual identifier as normal folders.


SFTPPlus Server 2.3.0, 17/02/2014
---------------------------------


New features
^^^^^^^^^^^^

* Add initial public version of HTTP and HTTPS file transfer service.
  See documentation for more details.
* Windows installer generates an install log file called `install.log`. The
  file is saved in the installation folder.


Defect fixes
^^^^^^^^^^^^

* Improve Unix init script together with improving documentation installation
  procedure on Unix.


SFTPPlus Server 2.2.0, 24/12/2013
---------------------------------


New features
^^^^^^^^^^^^

* Add support for AIX 5.3 (L6 and above) operating system.

* Add support for authentication legacy SFTPPlus WebAdmin accounts based on
  ssh keys. This requires a version of SFTPPlus WebAdmin greater than 1.7.0.


Defect fixes
^^^^^^^^^^^^

* Fix intermittent errors when displaying audit log from a MySQL database.

* Use CR/LF as line terminator for all file-based loggers on Windows systems.

* Mask clear passwords in audit entries.


SFTPPlus Server 2.1.0, released 26/11/2013
------------------------------------------


New features
^^^^^^^^^^^^

* Add a graphical user interface for managing SFTPPlus.

* Add support for FTP APPE command. For more details consult the IETF RFC 959.

* Implement globbing for FTP NLST and LIST commands. Globbing support is
  limited to Unix Shell wildchars ``* , ? , [ and ]``.

* Add ``–-generate-uuid``  command line options to generate UUIDs.

* Add ``--validate`` command line options to server-commands to validate server
  configuration.

* Add ``–key-comment`` command line options to server-commands to allow
  specifying a comment for the generated SSH public key.

* [windows] Allow automatically creating missing home folders for OS accounts
  with a custom owner and group.

* [windows] Added links to local manager and documentation in start menu on
  Windows at installation.

* Allow sending log entries to remote HTTP server using HTTP Post requests.

* Use a generic HTTP POST request for sending logs to legacy SFTPPlus
  WebAdmin.

* Add support for storing server logs inside a database. MySQL and SQLite are
  supported.

* Allow configuring an arbitrary number of log handlers, including multiple
  log handlers of the same type.


Defect fixes
^^^^^^^^^^^^

* SFTP errors are reported with specific event IDs and details instead of
  internal server errors.

* When requesting a file open operation on SFTP the action will emit a single
  signal (log entry) containing information about both action result and
  result file open mode. In previous versions 2 signals were emitted at file
  open.

* When starting the server in debug mode, the configured loggers are no longer
  disabled. A logger to standard output is added on top of configured loggers.

* When the server fails to launch a service at startup, it will log an error
  and continue to try loading the other services. In previous version, the
  startup was aborted as soon as a service was failing to start. The server
  will still abort the startup if no service was started.

* [unix] Fix launching the server as an Unix daemon.

* Fix reporting of timeout errors for passive connections.

* Fix reporting of errors for PORT command with address in bad format.

* Internal error report for FTP service error now shows full command which
  triggered the error condition.

* With the introduction of Local Manager GUI and managing services
  without restarting the server, the `enable` configuration option for a
  service was updated to configure if the service should be automatically
  started at server startup.

* [windows] The SFTPPlus service is stopped gracefully, both on
  system shut down and when stop command is received via the Services
  Management Console.

* Allow sending log entries to remote HTTP server using HTTP Post requests.


Upgrade information
^^^^^^^^^^^^^^^^^^^

With the move to dynamic log handlers, all configuration option from
``[log]`` section are ignored and new log handlers are required to be
configured.

The upgrade procedure will depend on the current version installed:

* If you have installed Server 2.0.X, you only need the upgrade steps
  specific for version 2.1.0.

* If you have installed Server 1.8.X or 1.7.X then you need to uninstall the
  previous version, install the new version and follow all upgrade steps
  since your version up to version 2.0.1

The upgrade steps involve only updating the configuration files and for most
customers will be straightforward. We will guide you as necessary.


SFTPPlus Server 2.0.1, released 22/04/2013
------------------------------------------

* [security][sftp] Fix checking public key signature when authenticating SFTP
  sessions using public key authentication method.


SFTPPlus Server 2.0.0, released 08/04/2013
------------------------------------------

* Fix message for event with ID "20009". The appropriate account type
  is displayed in the message, instead of always having "application account".
* Licenses for 3rd party libraries are now published in doc/legal folder.
* On Windows system, server can be configured to send logs to Windows
  Events Logger.
* Improve logging of internal server errors.
* Fix authentication of domain accounts on Windows server. For domain
  accounts, the automatic home folder name for account ``user@domain`` is
  generated as ``user.DOMAIN``.


Upgrade information
^^^^^^^^^^^^^^^^^^^

Due to the configuration changes that were merged in this version, the upgrade
from any previous version of SFTPPlus Server to version 2.0.0 can only be done
by uninstalling the product and installing the new version.

..  note::
    In order to be able to reconfigure the server after upgrade, do not delete
    the configuration files.

The following manual changes are required for the 'configuration/server.config'
file:

* ``configuration/server.config`` has been renamed to
  ``configuration/server.ini``. Having .ini extension, the configuration
  file should be automatically associated with a text editor.
  The rename is optional on Unix/Linux since the Unix init script
  can work with any filename.

* ``[services]``, renamed to ``[server]``

* Removed  ``services_`` prefix from all configuration options.

* The new ``[server]`` section has new attributes `uuid`, `name`,
  `description`. For more details see documentation.
* Renamed ``APPLICATION_GROUP`` to ``DEFAULT_GROUP``.
* ``DEFAULT_GROUP`` is automatically associated to all accounts for which
  a group was not explicitly defined. These are operating system accounts
  not defined in the configuration file or legacy SFTPPlus WebAdmin
  accounts.
* ``OS_GROUP`` is now a normal group and accounts are not automatically
  associated to this group. We recommend renaming it to 'os_group' to
  hint that it is just a normal.
* ``${DEFAULT_GROUP}`` placeholder was renamed to ``${DEFAULT_OS_GROUP}``.
  The new name should make it clear that it is referring to a group name
  as defined in the operating system.
* ``${DEFAULT_USER}`` placeholder has been renamed ``${DEFAULT_OS_USER}``.
  The new name should make it clear that it is referring to an account name
  as defined in the operating system.

* Services configuration are now defined using a new section marker. Each
  service has now an universally unique identifier (UUID) and a human
  readable short name. This allows rename operations and operating multiple
  services in a cluster environment. For more details see documentation.

  For example to update the service configuration for a service named
  ``ftp-partners`` having the following configuration::

      [ftp-partners]
      service_enabled = yes

  update it as::

      [services/550e8400-e29b-41d4-a716-446655440000]
      name = ftp-partners
      enabled = yes

* Service configuration options have been moved from dedicated files into the
  main configuration file. All configuration options for the ``[service]``
  section of each service configuration file need to be copied inside
  the dedicate section for each service.

  Here is an example of service section definition for an FTP protocol::

      [services/550e8400-e29b-41d4-a716-446655440000]
      name = ftp-partners
      enabled = yes

      ; Protocol options copied from configuration-server/ftp-service.config file.
      banner = Welcome to the FTP/FTPS Service.
      passive_port_range = 9000 - 9200

* Groups and accounts configuration have been moved from dedicated file into the
  main configuration file. All accounts and groups should now have an
  associated UUID. For more information please check the dedicated
  documentation.

* Configuration sections for groups are now in the format
  ``[groups/550e8400-e29b-41d4-a716-446655440001]``, and group name has been
  as a configuration option. `550e8400-e29b-41d4-a716-446655440001`
  is the group unique ID.

* Configuration sections for accounts are now in the format
  ``[accounts/550e8400-e29b-41d4-a716-446655440000]`` and account name has been
  moved as a configuration option. `550e8400-e29b-41d4-a716-446655440000`
  is the account unique ID. This allows renaming for accounts.

  Here is an example of new account definition::

      [accounts/550e8400-e29b-41d4-a716-446655440000]
      name = john
      type = application


SFTPPlus Server 1.8.10, released 25/04/2014
-------------------------------------------

* Update Unix initialization scripts.
* Add support for FTP APPE command. For more details consult
  the IETF RFC 959.
* Implement globbing for FTP NLST and LIST commands. Globbing support is
  limited to Unix Shell wildchars * , ? , [ and ].
* Add more details to audit trail when reporting failures for SFTP service.
* Add more details to audit trail when reporting failures for FTP/FTPS service.
* Add details for FTP active and passive data connection failures.


Defect fixes
^^^^^^^^^^^^

* Fix reporting of timeout errors for passive connections.
* Fix reporting of errors for PORT command with address in bad format.
* Internal error report for FTP service error now shows full command which
  triggered the error condition.
* SFTP errors are reported with specific event IDs and details instead of
  internal server errors.
* When requesting a file open operation on SFTP the action will emit a single
  signal (log entry) containing information about both action result and result
  file open mode. In previous versions 2 signals were emitted at file open.
* Fix a condition in which SFTP subsystem closed event (id 30012) was
  emitted twice.
* Fix FTP/FTPS service for listing folders with names similar to
  FTP globbing expressions.
* Fix an internal server error when SSH client requests to execute a command,
  a shell or a pseudo-terminal.


SFTPPlus Server 1.8.9, released 17/12/2013
------------------------------------------

* Add support for authentication legacy SFTPPlus WebAdmin accounts based on
  SSH keys. This requires SFTPPlus WebAdmin version 1.7.0 or
  higher.


SFTPPlus Server 1.8.8, released 16/10/2013
------------------------------------------

* Use persistent HTTP connections when sending logs to legacy
  SFTPPlus WebAdmin.


SFTPPlus Server 1.8.7, released 01/05/2013
------------------------------------------

* Fix initialization of SFTPPlus server configuration using
  server-commands --initialize.


SFTPPlus Server 1.8.6, released 22/04/2013
------------------------------------------

* [security][sftp] Fix checking public key signature when authenticating SFTP
  sessions using public key authentication method.


SFTPPlus Server 1.8.5, released 28/01/2013
------------------------------------------

* Allow application account to work together with SFTPPlus WebAdmin.
  In SFTPPlus Webadmin, "application" and "os" account are configured
  as "Local users".


SFTPPlus Server 1.8.4, released 23/01/2013
------------------------------------------

* When the FTP/FTPS data channel connection is closed abruptly
  (connection lost), the server will ignore these kinds of errors.


Upgrade information
^^^^^^^^^^^^^^^^^^^

The following manual changes are required for the
'configuration-server/ftp-service.config' file:

 * ``service_dtp_timeout``, renamed to
   ``service_idle_data_connection_timeout``


SFTPPlus Server 1.8.3, released 21/01/2013
------------------------------------------

* Display more details about a failed SSH authentication, instead of an
  internal server error.
* [security] When writing into existing files, truncate file size to the
  new uploaded file. Previously, when uploading a file smaller than the
  existing one, the file content was overwritten only with the new
  data, leaving the remaining data unchanged.
* Close FTPS control channel when the remote client does not close the
  connection in a clear way.
* Close idle FTP/FTPS data connections. For more details,
  check documentation for FTP/FTPS service configuration.
* Send an error to the client when failing to start an FTP/FTPS session
  due to an internal server error.
* Log an error when FTP/FTPS data connection has not been closed correctly.
* Log the amount of data received and sent over FTP/FTPS data channel.


SFTPPlus Server 1.8.2, released 20/12/2012
------------------------------------------

* Add support for user groups.
* [win] Add limited support for OS accounts on Windows XP and 2003.
  Accounts are locked inside their home folders and an explicit home
  folder is required to be defined for each user or the group associated
  with these accounts.


Upgrade information
^^^^^^^^^^^^^^^^^^^

The following manual changes are required for the
'configuration/users.config' file:

* For ``[APPLICATION_GROUP]`` and ``[OS_GROUP]`` add the new settings
  ``type: group``.

Instead of::

   [APPLICATION_GROUP]
   enabled: yes
   ...

   [OS_GROUP]
   enabled: yes
   ...

You should have::

   [APPLICATION_GROUP]
   type: group
   enabled: yes
   ...

   [OS_GROUP]
   type: group
   enabled: yes
   ...


SFTPPlus Server 1.8.1, released 29/11/2012
------------------------------------------

* Add support for Implicit FTPS service. Protocol type "ftpsi" is used
  for configuring Implicit FTPS services.
* Allow external / 3rd party mechanism for authentication and
  retrieving account configuration.
* Document event's data properties.
* Add a command for generating encrypted passwords.
* Add support for using encrypted password for application accounts.
  Passwords are salt-based SHA-256 hash values.
* Add 'allow_certificate_authentication' option to user's configuration.
  This allows per user enable / disable the authentication based on
  SSL certificates.
* Fix data channel connections closing in passive mode.
  The connection is cleared as soon as it is closed.


Upgrade information
^^^^^^^^^^^^^^^^^^^

The following manual changes are required for the
'configuration/users.config' file:

* ``account_name``, renamed to ``description``


SFTPPlus Server 1.8.0, released 03/10/2012
------------------------------------------

* Service configuration was changed to allow starting an arbitrary number of
  services for each supported protocol. Each service has its own
  configuration file.
* [technology preview] Add initial support for transferring files over HTTP
  and HTTPS services. Full support and documentation will be available
  in the next updates.
* Add support for enabling / disabling logs using log groups.
* Log file is initialized as services_account (if defined), rather than
  the account launching the server.


Upgrade information
^^^^^^^^^^^^^^^^^^^

When upgrading to version 1.8.0, the 'configuration/server.config' file
should be changed according to the following notes:

* all ftp_* options renamed to service_*
* all sftp_* options renamed to service_*
* in the '[ftp]' section you should add 'service_protocol: ftp'
* in the '[sftp]' section you should add 'service_protocol: sftp'

With these changes you can start multiple FTP and SFTP services from
a single configuration file.

The following options from 'configuration/service-ftp.config' file should be
renamed according to this notes:

* service_ftps_ssl_certificate -> service_ssl_certificate
* service_ftps_ssl_key -> service_ssl_key
* service_ftps_cipher_list -> service_ssl_cipher_list
* service_ftps_allowed_methods -> service_ssl_allowed_methods
* service_ftps_certificate_authority -> service_ssl_certificate_authority
* service_ftps_certificate_revocation_list ->
  service_ssl_certificate_revocation_list

These changes have been made to create unified configuration options for all
services working with SSL/TLS connections. Explicit FTPS will use the
same configuration files as the planned Implicit FTPS and HTTPS services
which will be added in future updates.


SFTPPlus Server 1.7.21, released 22/04/2013
-------------------------------------------

* [security][sftp] Fix checking public key signature when authenticating SFTP
  sessions using public key authentication method.


SFTPPlus Server 1.7.20, release 03/09/2012
------------------------------------------

* Fix installation errors introduced by 1.7.19.


SFTPPlus Server 1.7.19, released 14/08/2012
-------------------------------------------

* Add idle connection timeout configuration for FTP/FTPS service. This is
  configured by the ``service_idle_connection_timeout`` directive from
  service configuration file.
* Add idle connection timeout configuration for SFTP service. This is
  configured by the ``service_idle_connection_timeout`` directive from
  service configuration file.
* Add maximum number of concurrent connections for FTP/FTPS service. This is
  configured by the ``service_maximum_concurrent_connections`` directive from
  service configuration file.
* Add maximum number of concurrent connections for SFTP service. This is
  configured by the ``service_maximum_concurrent_connections`` directive from
  service configuration file.
* Allow loading encrypted SSL certificate's key. This is configured by the
  ``service_ftps_ssl_key_password`` from the FTP/FTPS service configuration
  file.
* Allow loading encrypted SSH private keys. This is configured by the
  ``service_rsa_private_key_password`` and
  ``service_dsa_private_key_password`` from the SFTP service configuration
  file.


SFTPPlus Server 1.7.18, released 27/06/2012
-------------------------------------------

* Log unknown or unimplemented FTP commands.
* Add support for Extending Passive (EPSV) and Extended Port (EPRT)
  commands.
* Add support for FTPS Clear Command Channel (CCC).


SFTPPlus Server 1.7.17, released 30/05/2012
-------------------------------------------

* When the server starts, list privileges for the account under which server
  was started. This should help troubleshoot permission related configuration
  errors.
* [Windows] Create home folders for newly created accounts. For this action,
  the account under which the server is executed will require
  "SeBackupPrivilege" and "SeRestorePrivilege".


SFTPPlus Server 1.7.16, released 23/05/2012
-------------------------------------------

* [Unix] Add support for running the server as a simple account. In this case
  only application accounts will be authenticated by the server.
* Refactor the way local user is queried. This should fix some errors on
  the Windows systems.
* Prepare local web administrator to support a dedicated administration
  username and password.


SFTPPlus Server 1.7.15, released 05/04/2012
-------------------------------------------

* Add support for internal and external log file rotation.
* Fix SFTP service automatically generated config file.


SFTPPlus Server 1.7.14, released 21/03/2012
-------------------------------------------

* Improve user configuration file to allow configuring local account and
  add more flexibility to the way accounts are configured.
* Create dedicated groups for specifying general behaviour for all
  application accounts and for all operating systems accounts.
* Add a server command for initial configuration that will generate new
  ssh key files and a self-signed certificate.


Upgrade information
^^^^^^^^^^^^^^^^^^^

When upgrading to SFTPPlus Server 1.7.14, the 'configuration/users.config' file
should be changed according to the following rules:

* ALL_APPLICATIONS_USERS section renamed to APPLICATION_GROUP
* ALL_OS_USERS section renamed to OS_GROUP


SFTPPlus Server 1.7.13, released 25/01/2012
-------------------------------------------

* Add `service_ignore_create_permissions` to SFTP service configuration for
  ignoring SFTP clients to set file and folder permissions at creation time.
* Add a log when a file transfer was done in SFTP.
* Add IP and port number for SFTP logs after an account was successfully
  authenticated.


SFTPPlus Server 1.7.12, released 20/01/2012
-------------------------------------------

* Fix server initialization.
* Allow server to execute under the same account used for starting the
  main server process.


SFTPPlus Server 1.7.11, released 19/01/2012
-------------------------------------------

* Add support for authenticating Centrify accounts.


SFTPPlus Server 1.7.10, released 18/01/2012
-------------------------------------------

* [security][sftp] Don't allow application account to authenticate with SSH
  keys when SSH keys are disabled.
* Allow using SFTPPlus Webadmin only for authentication, only for storing
  audit entries, or for both.


SFTPPlus Server 1.7.9, released 13/01/2012
------------------------------------------

* [security][sftp] Don't allow application account to authenticate with SFTP
  without specifying either a non-empty password or an SSH key.


SFTPPlus Server 1.7.8, released 26/12/2011
------------------------------------------

* Fix access to files from supplementary groups.
* Add logs for disabled accounts.


SFTPPlus Server 1.7.7 (0.2.7), released 16/11/2011
--------------------------------------------------

* Fix closing connection when transferring an empty file over FTPS.


SFTPPlus Server 1.7.6 (0.2.6), released 15/11/2011
--------------------------------------------------

* Update OpenSSL library on Windows.
* Improve handling SSL connections close procedures before the SSH handshake
  was finalized.


SFTPPlus Server 1.7.5 (0.2.5), released 02/11/2011
--------------------------------------------------

* Improve Unicode handling on POSIX-based locale.
* Add support for Solaris 10 on Intel x86.


SFTPPlus Server 1.7.4 (0.2.4), released 14/10/2011
--------------------------------------------------

* Add option to specify FTPS SSL/TLS cipher list.
* Add option to specify FTPS methods.
* Allow FTP FEAT command to be called at any time during an FTP session.
* Allow FTP authentication based on SSL certificate and no longer require a
  password. Certificate's Common Name must match user name.


SFTPPlus Server 1.7.3 (0.2.3), released 30/09/2011
--------------------------------------------------

* Fix FTPS Active connections.
* Raise an error if a download request is made on FTP for a folder.
* [security][unix] Fix user impersonation under Unix.
* Update installation documentation.


SFTPPlus Server 1.7.2 (0.2.2), released 24/08/2011
--------------------------------------------------

* Add startup execution command.


SFTPPlus Server 1.7.1 (0.2.1), released 23/08/2011
--------------------------------------------------

* Fix ssh key generation.
* Fix SFTP operations for application users.


SFTPPlus Server 1.7.0 (0.2.0), released 01/08/2011
--------------------------------------------------

* GUI installer on Windows.
* Add utility for generating RSA/DSA keys.
* Check for OpenSSL support.
* Add support for application users.
* Add server name and version into FTP welcome message and
  SSH protocol string.
* [0.1.11] Add support for ignoring SFTP file/folder mode on creation.
* [0.1.10] Add support for username and password PAM authentication.
* [0.1.8] Add umask option for uploaded files.
* [0.1.7] Fix SFTP set attribute command.
* [0.1.5] Add an option for creating home folders for SFTPPlus users.
* [0.1.5] Improve unicode support for authentication errors.
* [0.1.4] Fix setting initial working folder for SFTPPlus users.
* [0.1.4] Add support for Red Hat Enterprise Linux 4 and 5.
* [0.1.4] Log an error if service account is not available.
* [0.1.4] Log an error if RSA/DSA keys could not be found.
* [0.1.3] Add FTP passive port range.


SFTPPlus Server 1.6.11.a (0.1.11), released 27/06/2011
------------------------------------------------------

* Add support for ignoring SFTP requested mode on file and folder creation.

  * Ignore mode on creation is enabled by default.
  * Ignore mode can be changed from constants.py via IGNORE_CREATE_PERMISSIONS


SFTPPlus Server 1.6.10 (0.1.10), released 24/06/2011
----------------------------------------------------

* Add support for username and password PAM authentication.


SFTPPlus Server 1.6.9 (0.1.9), released 23/06/2011
--------------------------------------------------

* Use 0666 as default mode for files and 0777 for folders.


SFTPPlus Server 1.6.8 (0.1.8), released 21/06/2011
--------------------------------------------------

* Add umask option for uploded files.


SFTPPlus Server 1.6.7 (0.1.7), released 16/06/2011
--------------------------------------------------

* Fix file transfers using WinSCP.


SFTPPlus Server 1.6.6 (0.1.6), released 16/06/2011
--------------------------------------------------

* Allow SFTPPlus WebAdmin users to authenticate based on RSA/DSA keys.


SFTPPlus Server 1.6.5 (0.1.5), released 07/06/2011
--------------------------------------------------

* Add an option for creating home folders for SFTPPlus users.
* Improve unicode support for authentication errors.


SFTPPlus Server 1.6.4 (0.1.4), released 03/06/2011
--------------------------------------------------

* Fix setting initial working directory for SFTPPlus users.
* Add support for Red Hat Enterprise Linux 4 and 5.
* Log an error if service account is not available.
* Log an error if RSA/DSA keys could not be found.


SFTPPlus Server 1.6.3 (0.1.3), released 22/05/2011
--------------------------------------------------

* Add FTP passive port range.


SFTPPlus Server 1.6.2 (0.1.2), released 19/04/2011
--------------------------------------------------

* Use default port numbers for services.
* [Windows] Fix Windows service install for SFTP service.
* [Windows] Fix Windows service uninstall for services.
* [Windows] Log service startup errors in Windows Event logger.
* [Windows] Use Windows end of line for log file on Windows.
* [Windows] Add error number when failing to get user home folder on Windows


SFTPPlus Server 1.6.1 (0.1.1), released 11/03/2011
--------------------------------------------------

* Add more FTP and SFTP logs.
* Send logs to SFTPPlus Webadmin


SFTPPlus Server 1.6.0 (0.1.0), released 01/03/2011
--------------------------------------------------

* [Unix] SFTPPlus users will always run under a single local account defined
  by 'service_account' configuration key.
* [Windows] SFTPPlus users will run under the account configured for the
  specific windows service.
* Operating system users can use the default OS home folders, or a custom
  home folder specified by 'os_users_custom_home_folder_path' configuration
  key.
* SFTPPlus users are always locked into their home folder
