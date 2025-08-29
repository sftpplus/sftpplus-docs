Release Notes for Version 4
===========================

Version 4 is no longer in active development.
Version 4 is still supported until 2027.


Version 4.36.0, 2024-12-11
--------------------------


Security Fixes
^^^^^^^^^^^^^^

* The Python runtime has been patched with security fixes from ActiveState to
  account for CVE-2017-18207, CVE-2021-4189, CVE-2022-45061, CVE-2022-48565,
  and CVE-2024-7592. On Linux and macOS, the following security issues were
  also fixed: CVE-2022-48560, CVE-2022-48566, CVE-2023-40217, and
  CVE-2024-0397. [#6781-2]
* The OpenSSL 1.1.1 libraries used for Python's `cryptography` on Windows,
  generic Linux, Alpine Linux, and macOS were patched to fix CVE-2023-5678,
  CVE-2024-0727, CVE-2024-2511, CVE-2024-4741, and CVE-2024-5535. [#6781]


New Features
^^^^^^^^^^^^

* You can now configure a transfer to send the file to the destination location
  using a relative path. [client-side] [#6901]


Defect Fixes
^^^^^^^^^^^^

* When using automated updates on Linux, file capabilities such as binding
  privileged ports are now preserved for SFTPPlus installations. [#6498]


Version 4.35.1, 2024-07-17
--------------------------


Defect Fixes
^^^^^^^^^^^^

* An internal error is no longer generated when listing empty folders over
  FTPS. When listing an empty folders, some FTPS server close the data
  connection before confirming the end via the command connection. This was
  causing SFTPPlus to fail to validate the server connection. This is a
  regression introduced in SFTPPlus 4.34.0. [client-side][ftps] [#4346]
* The FTP/FTPS server now closes any file for which an upload request was
  started, but for which the upload operation failed. On previous version, if a
  file transfer failed during the data transfer, the uploaded file was kept
  opened on the server operating system. [server-side][ftp] [#6514]


Version 4.35.0, 2024-01-12
--------------------------


Security Fixes
^^^^^^^^^^^^^^

A critical security issue was fixed for the FTPS server.

SFTPPlus can now be
configured to enforce the use of the same TLS session for both command
and data connections.

For backward compatibility, the TLS session reuse is not automatically enabled
for existing configuration.
You will need to manually update the SFTPPlus configuration.

For TLS session reuse you might also need to update your FTPS client.
For example you will need WinSCP version 6, or configure WinSCP version 5
to only use TLS 1.2.
WinSCP version 5 with TLS 1.3 does not work with TLS session reuse.

In previous versions, reusing the TLS session was not enforced.

This could allow a malicious third party to hijack the data
connection without any authentication, by only guessing the passive port
number.
As a result of such an attack, data can be leaked or corrupted.
SFTP and HTTPS protocols are not affected. The security issue is mitigated
when the FTPS server is configured to validate client connections against a
certificate authority (CA).

In such a case, the malicious third party
would also need a valid matching certificate signed by the configured
Certificate Authority to successfully hijack the data connection.
This issue affects all previous versions of SFTPPlus. [#6379]


New Features
^^^^^^^^^^^^

* You can now configure role permissions to allow referencing the currently
  authenticated administrator using the `own` prefix. This allows defining
  administrator accounts able to create, delete, and update users and groups
  without having permissions for configuring other administrator accounts.
  [manager] [#6470]


Defect Fixes
^^^^^^^^^^^^

* The HTTP(S) server now closes the downloaded file if there was an error
  during download. In previous versions, the affected file was left open.
  [server-side][http] [#6469]


Version 4.34.1, 2023-11-22
--------------------------

This is a re-release of 4.34.0, previously released on 2023-11-22,
that fixes our container images published on Dockerhub.


Security Fixes
^^^^^^^^^^^^^^

* When connecting to remote FTPS servers, SFTPPlus makes sure the same TLS
  certificate is used for both data and command connections.
  This prevents man-in-the-middle attacks where a malicious third party
  pretends to handle the data connection. [client-side][ftps][security]
  [#6382-1]
* When connecting to remote FTPS servers, SFTPPlus now makes sure the TLS
  session used for the data connection has the same session ID as the command
  connection. This prevents man-in-the-middle attacks in which a malicious
  third party pretends to handle the data connection. This can also improve
  performance when transferring many small files. Some FTPS servers might not
  know how to handle a TLS session reuse. In SFTPPlus v4 the default
  `ftps_reuse_session = no` configuration is set to avoid reusing the TLS
  session. This default option will be changed to `ftps_reuse_session = yes`
  in the future release of SFTPPlus 5.0. [client-side][ftps][security] [#6382]
* The passive data ports are now used by SFTPPlus in random order. In
  previous versions, they were allocated based on the lowest available port
  number. [ftp][server-side] [#6430]


Defect Fixes
^^^^^^^^^^^^

* The FTP location now automatically disconnects if the FTP server
  connection is opened, but the server doesn't send any response.
  [client-side][ftp] [#6401]
* Multiple re-connections are no longer triggered when a location is
  disconnected for being idle, but then it needs to reconnect to perform
  multiple transfers. [client-side] [#6402]
* When updating through the included ``bin/update.sh`` script, the saved
  service name from ``configuration/INSTALL_INFO`` is checked before trying to
  stop a running SFTPPlus instance. This prevents systemd restarting the
  SFTPPlus service in the background under a different service name. [#6407]
* The FTP/FTPS location now sends the PBSZ and PROT commands right after the
  AUTH command for Implicit FTPS following a successful TLS handshake. In
  previous versions, it was sending the PBSZ/PROT commands after the USER
  command and, by doing so, it was getting rejected connections from some
  FTPS servers. [client-side][ftp] [#6429]
* The FTP/FTPS location can now transfer files to and from servers that don't
  support the `PWD` command. For servers with no `PWD` support, SFTPPlus
  assumes that the server uses Unix path separators.
  [client-side][ftp][ftps] [#6435]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The event with ID `10020` was removed and replaced by the existing event with
  ID `10061`. There is now a single event ID to inform that a passive transfer
  was requested, for both PASV and EPSV (extended PASV) transfers.
  [server-side][ftp] [#6395]


Version 4.33.0, 2023-10-10
--------------------------


Security Fixes
^^^^^^^^^^^^^^

* The OpenSSL 1.1.1 libraries used for Python's `cryptography` on Windows,
  generic Linux, Alpine Linux, and macOS were updated to version 1.1.1w to fix
  CVE-2023-4807, CVE-2023-3817, CVE-2023-3446, CVE-2023-2975, CVE-2023-2975,
  CVE-2023-2975, CVE-2023-1255, CVE-2023-0466, and CVE-2023-0464. [#6399]


New Features
^^^^^^^^^^^^

* Theme support was added for HTTP `ui-gen-2`. [server-side][http] [#6265]


Defect Fixes
^^^^^^^^^^^^

* The configuration options that are measured in seconds are now set to the
  default value, when a new component is created. In previous versions, the
  options were set to 1 second. This is a defect introduced in 4.31.0.
  [manager] [#6388]


Version 4.32.1, 2023-09-18
--------------------------

This release is dedicated to fixing a bug introduced by the 4.32.0 version.

The defect was causing the analytics resource to fail when an
account was configured to be auto-disabled on inactivity
while not having a creation date and any previous successful authentications.

The download links for Red Hat Enterprise Linux version 9, 7, 6 and 5
were fixed. The download link for RHEL version 8 was already working properly.


Version 4.32.0, 2023-09-15
--------------------------


New Features
^^^^^^^^^^^^

* You can now configure the `external-executable` event handler to accept
  output in JSON format from a command. [#6359]
* You can now configure an SFTPPlus account to be disabled if not active for a
  number of days. [server-side][security] [#6363]


Defect Fixes
^^^^^^^^^^^^

* A transfer no longer fails when its source location cannot connect to the
  remote server. The transfer now waits for the source location to be
  available. It automatically restarts once the source location is
  available. [client-side][ftps][sftp] [#5537]
* Monitoring an FTP source location no longer stalls when the source location
  is disconnected due to an idle connection while the source
  directory is checked. In previous versions, the source location was
  disconnected due to being idle, and, if the source check operation was
  scheduled for the exact same time, the source check operation was failing,
  without rescheduling a retry or scheduling a reconnection of the source
  location. [client-side][ftp] [#6333]
* The web management console no longer has the public URL name disabled for the
  HTTPS service. In previous versions, the configuration UI for the public URL
  name was always disabled in the web interface. The only option for configuring
  that value was to edit the .INI configuration file. [manager] [#6334]
* A pull transfer from FTP/FTPS locations is no longer stalled when the server
  initially responds that the pull transfer can start, but then doesn't send
  any data. In previous versions, the whole transfer was blocked, requiring a
  manual restart of the transfer. In the latest version, the current file
  transfer fails, but a retry is scheduled for the current file and any other
  files for which a transfer was attempted. [client-side][ftp] [#6346]
* Automated content conversion for a transfer initially failed and then retried
  is now properly working. [client-side] [#6351]
* The summary text search for the `Activity Log` page was fixed. This was a
  defect introduced in 4.31.0. [manager] [#6353]
* A push transfer from an FTP/FTPS/SFTP locations no longer ignores a file
  upload when the server is disconnecting at the same time that a file upload
  operation is requested. In previous versions, the transfer was still active,
  but the file was not retried, even though new files would have been uploaded.
  [client-side][ftp][sftp] [#6356]
* The pending operation for a transfer no longer generates a retry when the
  transfer is stopped. In previous versions, for some transfer operations, a
  `CancelledError()` was generated when the transfer was stopped. This was
  considered a failure, therefore the transfer was retried, preventing the
  stopping of the transfer. [client-side] [#6375]


Version 4.31.0, 2023-08-07
--------------------------


New Features
^^^^^^^^^^^^

* You can now configure a transfer to do automatic content conversion from
  UTF-16 to ASCII. [client-side] [#5943]
* You can now manage components from the admin-shell command line tool using
  component name as a reference. [manager][cli] [#6291]
* A new event handler was added to compute the digest of files. [#6302]
* The HTTP Post event handler can now trigger requests using the GET or PUT HTTP
  methods. [#6309]


Defect Fixes
^^^^^^^^^^^^

* The `usernames` configuration option of the `deny-username` authentication
  method now handles the configured values as case-insensitive, regardless
  of the actual case of the configured values. In previous versions, the
  configured value was required to be defined in lowercase. [security] [#6293]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* In order to speed up loading past activity logs, the total
  number of logs is no longer displayed. [manager] [#2707]
* A warning is generated in the logs and the web administration console when
  the SFTPPlus Windows service is still started using the legacy utility that
  was used in version 2 and 3 of SFTPPlus. The legacy utility still works with
  version 4, but will no longer work with future major SFTPPlus versions.
  This issue only affects SFTPPlus installations that were first installed
  using a version prior to 4.1.0. [windows] [#5550]
* The main page of the Web Administration Console no longer contains the list
  of resources and locations. These lists can now be found in the dedicated
  pages for resources and locations. [manager] [#6236]
* In the web administration console, the local filesystem monitor service was
  moved to the `Resources` section. From the resources section you can add,
  delete, or modify existing resource monitors. No configuration changes are
  required. In the .INI configuration file, the file system monitor continues
  to be configured from the services section. [manager] [#6279]


Version 4.30.1, 2023-06-13
--------------------------

Version 4.30.0 was released on 2023-06-09 as a release candidate.


New Features
^^^^^^^^^^^^

* When updating or rolling back SFTPPlus using the dedicated scripts in `bin/`,
  it's now possible to have multiple automatic backups in
  `/srv/sftpplus_backups`. [#6012]
* The Dashboard section of the Web Administration Console now lists all failed
  components (services, transfers, event handlers, etc). [manager] [#6080]
* The Web Administration Console now supports access via a reverse proxy with
  URL rewrites. [manager] [#6242]


Defect Fixes
^^^^^^^^^^^^

* SFTPPlus can now receive over the AS2 protocol files sent using multi-line
  headers. In previous versions, a `boundary` error was raised in such
  instances, for example when the multi-part header was defined on multiple
  lines. [server-side][as2] [#5795]
* An informational error message is now raised when the `--ssh-server-identity
  set-on-first-connection` command line option is used for the `client-shell`
  CLI. The `set-on-first-connection` value is not supported for the CLI. In
  previous versions, an internal error was raised. [client-side][sftp] [#6190]
* The page listing the accounts now only shows TOTP as enabled for accounts
  that have it enabled. In previous versions, due to a defect, all accounts
  were listed as having TOTP enabled. [manager] [#6234]
* Support was added for paths longer than 255 characters on Windows. A single
  filename is still limited to 255 characters at most. However, the combined
  path for the filename and its parents can now be longer than 255 characters.
  [#6245]
* A transfer no longer skips pulling a file from a remote location when the
  connection is lost just before starting to transfer the file. The failed file
  transfer is now retried even when failing in this way. In previous versions,
  a transfer failing in these particular conditions was skipped.
  [client-side] [#6247]
* When receiving AS2 files via the SFTPPlus AS2 server, besides having the
  temporary files stored into a separate temporary folder, the files being
  transferred now also have temporary file extensions.
  [server-side][as2][security] [#6252]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `size` data attribute associated with the `20175` event emitted when
  a file is rotated is now always a text value. In previous versions,
  it was either a number or a text value. [#6121]


Version 4.29.0, 2023-04-06
--------------------------


New Features
^^^^^^^^^^^^

* You can now configure the event handler `data_filter` option using multiple
  filtering rules. The configured rules are applied in conjunction (all of
  them have to match). [#6152]


Defect Fixes
^^^^^^^^^^^^

* When the `ssl_certificate_authority` is configured with an expired
  certificate, the component using the configured CA now fails to start and an
  explicit error message is returned. [security] [#6102-1]
* The expired root CA certificates from the SFTPPlus predefined list of CA
  certificates like `${MICROSOFT_IT_CA}`, `${LETS_ENCRYPT_X3_CA}`, or
  `${GO_DADDY_G2_G1}` are now ignored. This allows you to continue using the
  predefined list, even if one of the root certificates is now expired.
  [security] [#6102]
* The events emitted by the local filesystem monitor service are now associated
  with the service that triggered them. In previous versions, the events
  weren't associated to any SFTPPlus component. [#6126-1]
* The account interaction event handler no longer emits events for accounts
  that are disabled. [server-side] [#6126]
* The FTP/FTPS location/client can now handle multi-line authentication
  responses. This was a regression introduced in version 4.28.0.
  [client-side][ftp][ftps] [#6156]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* AIX support was removed. For existing AIX customers, older versions of
  SFTPPlus 4 are still supported on AIX 7.1 and newer. [#6089]


Version 4.28.0, 2023-03-08
--------------------------


New Features
^^^^^^^^^^^^

* The FTP/FTPS server now accepts the `STRU F` and `MODE S` FTP commands.
  [server-side][ftp][ftps] [#6067-1]
* The web file browser now preserves the directory structure when uploading
  a hierarchy of files using drag and drop. In previous versions, all files from
  the hierarchy of a source directory were uploaded into the target directory,
  ignoring the structure of sub-directories in the source directory.
  [https][server-side] [#6067]
* When transferring files using the `batch_interval`, the files from the same
  batch are now transferred in alphabetical order. [client-side] [#6069]
* When receiving AS2 files for which the filename is set by the remote AS2
  partner to either `smime.s7m` or `smime.p7z`, SFTPPlus now handles the AS2
  transfer as if the filename is not set, using the configured default
  filename instead. [server-side][as2] [#6071]
* The FTP/FTPS locations now support sending the `ACCT` command after
  a successful login. [client-side][ftp][ftps] [#6074]


Defect Fixes
^^^^^^^^^^^^

* SFTPPlus now stores the AS2 files that have not yet been validated
  in a separate pending folder.
  This avoids having invalid files in the final destination path at any point.
  [server-side][as2][security] [#6011]
* When receiving AS2 files, the algorithm names for the payload and MDN are now
  normalized. For example, `sha-256` will have the same meaning as `sha256`.
  [server-side][as2] [#6071]
* The Python runtime has been patched with the latest security patches from
  ActiveState to fix CVE-2015-20107. On Linux, AIX, and macOS, CVE-2020-10735
  was also patched. [#6062-2]
* The OpenSSL 1.1.1 libraries used for Python's cryptography on Windows,
  generic Linux, Alpine Linux, and macOS were updated to version 1.1.1t to fix
  CVE-2023-0286, CVE-2023-0215, CVE-2022-4450, and CVE-2022-4450. [#6062]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `markers` data attribute from event with ID `60006` was removed. It was
  replaced by the generic `details` attribute containg the details for the
  delay of a transfer. [client-side] [#6067]


Version 4.27.0, 2023-02-14
--------------------------


New Features
^^^^^^^^^^^^

* The Web Administration Console now allows authentication using the Azure AD
  method. [manager] [#4155]
* The `permissions` configuration options for roles now allow defining a
  read-only permission for SFTPPlus components such as services, transfers, and
  locations. The `update` permission can be used to allow
  starting/stopping/restarting a component. [manager] [#5465]
* The management UI for the event handlers filter was updated to allow
  configuring event groups, usernames, and components by selecting
  from a list of available items. [#5726]
* The HTTP authentication API now supports the `public_error` key in the
  response to allow displaying authentication errors when logging into
  the HTTP service via the web browser GUI or through the programmatic
  HTTP file transfer API. [http][https][server-side] [#6035-1]
* The HTTP authentication API now supports the `public_response` key in the
  response to allow displaying a structured JSON for the JSON API when the
  authentication is rejected. [authentication][api][server-side] [#6035-2]
* You can now associate operating system groups to SFTPPlus roles for the
  authenticated administrators. [manager] [#6036]
* The FTP and FTPS client locations can now be configured to use the IP address
  returned by the PASV command using the `ignore_passive_address` configuration
  option.
  In previous versions, the IP address for the
  data channel was ignored. Instead, the address configured for the command
  channel was used.
  This was a regression introduced in version 3.52.0.
  [ftp][ftps][client-side] [#6042]
* The SFTP/SCP server-side and client-side transfers now support the
  `rsa-sha2-256` and `rsa-sha2-512` algorithms.
  [sftp][server-side][client-side] [#6044]


Defect Fixes
^^^^^^^^^^^^

* The HTTP and HTTPS connections are now disconnected by the SFTPPlus server
  with a timeout when no data is requested by the client after
  `idle_connection_timeout`. [http][https][server-side] [#2630]
* The font features used for the SFTPPlus web-based user interfaces were
  updated for increased legibility. For example, lowercase l and capital I
  should now be easily distinguishable. [#6009]
* The configuration of the Operating System authentication method is now
  successfully migrated from version 4.22.0 or older. In previous versions, the
  OS authentication method failed to start because the new `base_roles` and
  `role_association` values were not correctly migrated. [manager] [#6036]
* The web management console can now be used to manage accounts and groups with
  access only to the external local file authentication method. In previous
  versions, managing the external local file authentication required access to
  at least one account or group from the main configuration file. [manager]
  [#6047]
* The web management console now enforces unique names for accounts,
  groups, administrators, and roles. [server-side] [#6048]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `idle_connection_timeout` service configuration option no longer accepts
  the `Disable` value. Using `Disable` results in setting it back to the default
  value. By disabling this timeout, the server is vulnerable to denial of
  service attacks. [server-side] [#2630-1]
* Events with ID `40009` and `40029`, emitted when an HTTPS connection is closed
  due to a TLS error, were replaced by the general event with ID `40054`,
  emitted when closing HTTP or HTTPS connections. [server-side][https] [#2630]
* The role permissions for component targets now have to be prefixed by
  "operation/". The existing non-prefixed targets are automatically migrated.
  [manager] [#5465]
* The `home_folder_structure` value, returned by the remote HTTP authentication
  server as part of the SFTPPlus HTTP authentication method, was changed from
  being a `list of lists` to a `list of strings/paths`. This is a regression
  introduced in SFTPPlus version 4.23.0. The current version of SFTPPlus has
  support for both value types, but you are encouraged to update your HTTP API
  response format. [server-side][api] [#6035]


Version 4.26.2, 2022-12-19
--------------------------

Version 4.26.0 was released on 2022-12-12 as the first release candidate.
Version 4.26.1 was released on 2022-12-14 as the second release candidate,
in which further work was done to fix defect #5982.
Version 4.26.2 was released on 2022-12-19 as the third release candidate,
in which the fix for defect #6017 was added.


New Features
^^^^^^^^^^^^

* The configuration for general authentication methods was moved from the
  `General Configuration` page to the `Authentications` page. [manager] [#5879]
* The shell scripts ``bin/update.sh`` and ``bin/rollback.sh`` were added to help
  with updating SFTPPlus on Linux, macOS, and AIX. The update script backs up
  the current installation before proceeding. Rolling back to this backup is
  also possible in an automated way. [#5899]
* When configuring the Azure AD authentication method with extra API scopes,
  the OAuth2 token is available as part of the user avatar exposed to the
  Python API extensions. [api] [#5961]
* When defining a negative filter for the event handler, you can now have a
  space between the exclamation mark and the negated value. [#5986]
* The `${MICROSOFT_IT_CA}` root CA certificates were updated to include the
  `Microsoft RSA TLS CA 01` and `Microsoft RSA TLS CA 02`
  certificate authorities. [security] [#6002]
* You can now configure SFTPPlus to receive AS2 files in a sub-path of the
  server's root.
  In previous versions, SFTPPlus was only able to receive AS2 files in a path
  that is a direct child of the server's root. [server-side][as2] [#6004]
* Is is now possible to automatically install multiple instances of SFTPPlus
  on the same Linux system through the included ``bin/install.sh`` script
  by providing a custom service name as an argument. [#5995]


Defect Fixes
^^^^^^^^^^^^

* When sending files to HTTPS-based locations (SharePoint, WebDAV, Azure Files,
  AS2) the transfer now waits for TLS renegotiation before sending more
  data. In previous versions, the transfer failed because SFTPPlus
  sent more data, but the TLS connection was not yet ready.
  [client-side][https][as2] [#5279-1]
* When sending files over AS2 encrypted using 3DES, the encryption is now
  using 192-bit keys. In previous versions, it used 128-bit keys.
  [client-side][as2] [#5279-2]
* When sending AS2 files, the algorithm names from MDNs are normalized.
  For example, `sha-256` is the same as `sha256`. [client-side][as2]
  [#5279]
* It is now possible to configure the operating system authentication method to
  allow all users from all OS groups. You can associate them to a fixed
  set of SFTPPlus groups. [server-side] [#5955]
* When SFTPPlus has an ongoing file download operation on Windows, it no
  longer blocks the file from being deleted.
  [server-side][windows][sftp][ftps][https] [#5982]
* The HTTP(s) server session now expires based on the
  `idle_connection_timeout` configuration defined for each service. In previous
  versions, the session expiration was ignoring the configuration. A fixed
  value of 15 minutes was used instead. [server-side][http][manager] [#5983]
* The standard output and the error output generated when calling external
  commands using the `external-executable` event handler are no longer
  truncated at 100 characters. [#5991]
* You can now use TLS/SSL certificates with subjects or subject alternative
  names using Unicode characters outside of the ASCII range.
  In previous versions, an internal error was raised when SFTPPlus
  was configured with such a certificate, or when connecting to
  remote servers that were using such a certificate. [ftps][https][#6017]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `manager_authentications` configuration of the `server` section was
  removed. The manager web console now uses the authentication defined directly
  in the manager service configuration. The old configuration is automatically
  migrated, no manual configuration changes are required. [manager] [#5879]
* The CRL digital signature extension no longer supports validating the
  configured certificate against a certificate revocation list. [#5961-1]
* The Python API event handler extension no longer allows emitting events
  directly via the `parent.emitEvent` method. The extension should now return a
  list of event data to be emitted by the event handler. [api] [#5961]


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

* The Azure AD SFTPPlus application permissions were changed from
  `Directory.Read.All` to `GroupMember.Read.All`.
  You will need to manually change the SFTPPlus permissions inside the
  Azure Portal and grant admin consent.
  [server-side] [#2196]
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

* The `session_username` cookie is no longer used by the Web Manager web
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
* The JQuery library used by SFTPPlus Web Manager web console and the legacy
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

* You can now configure the Web Manager web console to only show server-side
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
* The Web Manager's user interface for configuring the list of SSL/TLS
  ciphers to be used by HTTPS and FTPS services has been improved to allow
  selecting from a list of available ciphers. [security] [#5600]
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

The look and feel of Web Manager's login page was refreshed.
This is the first step into updating the Web Manager web console interface
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
  ECDHE-based ciphers were available. [server-side][security] [#5597]


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

* The Web Manager UI for selecting multiple component identifiers was updated
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
  using the Web Manager web interface. Due to a defect, in previous versions
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
  by setting it to value 0 from Web Manager.
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
  Using `disabled` is supported until the next major release. [security] [#2090]
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
* You can now edit OS accounts in the Web Manager.
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
* The Web Manager web interface no longer shows the WebDAV location as
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
* If the source location of a transfer is manually stopped, the Web Manager
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

* The links and commands to start the Web Manager and documentation pages
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
* When a new component is created using the Web Manager interface, the
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

* In Web Manager, in the list of accounts for a local file authentication
  method, you will now see the name of the associated group. In previous
  versions, the group was listed as UNKNOWN. [#2368]
* The authentication page of the Web Manager web console was fixed to work
  with Internet Explorer. This was a defect introduced in version 4.10.0.
  [#5547]
* Defining configuration options in Web Manager using text values
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
  signature and encryption. [server-side][as2] [#5370]
* HTTP connection requests to HTTPS services such as the Web Manager web
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
* Components listed on the Web Manager general status page are now sorted
  in alphabetical order. [manager] [#5537]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Following SSH ciphers are no longer supported: cast128-ctr, blowfish-ctr,
  and 3des-ctr. The CBC mode for these ciphers are still supported. [sftp]
  [#5529]
* The `rsa_private_key` and `dsa_private_key` configuration options were
  removed, being replaced by a single `ssh_host_private_keys` configuration
  option.
  For backward compatibility, the old configuration options are still supported.
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
* Web Manager's user interface for the OS authentication method was updated
  to inform that all OS accounts are denied access when no OS group is
  configured. [server-side] [#5483]
* An internal error is no longer raised when trying to directly access the HTTP
  service login URL while already authenticated. [server-side][http][https]
  [#5487]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with ID 50012 emitted by the Web Manager web interface was removed.
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
  [#5397]


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
  the Web Manager now includes the UUID of the newly created component.
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
* The SFTPPlus instance name is now visible in the Web Manager web-based
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
  equivalent of the Web Manager web-based GUI console. [#1158]
* The `openpgp` event handler was added for encrypting and decrypting files
  using OpenPGP. [#1177]
* You can now use SSL/TLS certificates to authenticate users against the HTTPS
  file transfer service. [server-side] [#143]
* You can now send credentials for an account via email. [#1468]
* You can now create PGP keys from the Web Manager web interface or the
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
  administration password. With this change, Web Manager is now accessible by
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
* The Windows start menu shortcut to the Web Manager page now works even when
  the Web Manager is configured for the `0.0.0.0` IP address. [#3030]
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
* Event with ID 50020, raised when SFTPPlus Web Manager failed to start a
  database, was removed and replaced by ID 20112. [#316-5]
* The `Past Activity` page in the Web Manager web console was renamed to
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
* Events with IDs 50019, 50021, 50022, 50025, emitted when a Web Manager DB
  operation fails, were removed. They were replaced with specific event ID
  errors for each Web Manager operation using the DB. [#3168-5]
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
