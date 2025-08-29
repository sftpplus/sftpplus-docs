Release Notes for Version 3
===========================

SFTPPlus version 3 was released in 2015.
It is no longer in active development or supported.


Version 3.55.0, 2020-04-28
--------------------------

This release includes a critical security issue for the
Web Manager's web console GUI introduced with SFTPPlus version 3.24.0.

The vulnerability is a local one if Web Manager only accepts
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
make sure the Web Manager is only available through secured channels
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

* The "Download as CSV" link from the Web Manager no longer allows
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
  can use: `https://acme-v02.api.letsencrypt.org/directory`. If
  you were using the Let's Encrypt V1 server at
  acme-v1.api.letsencrypt.org/directory, it will be automatically
  upgraded to acme-v02.api.letsencrypt.org/directory. [#5351]


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

* Let's Encrypt resource will now highlight in the Web Manager that a restart
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
* When configuring a new account from the Web Manager web console,
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
* You can now create new SFTP services from the Web Manager web interface.
  This issue was introduced in version 3.46.0. [server-side][sftp] [#4124]
* When using the client shell, passwords are now masked by default.
  [security][client-side] [#5213]
* Web Manager's web interface now has an explicit button for disabling a
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
  restart in the Web Manager. [#5137]


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
  by the HTTP file transfer services and the Web Manager.
  This allows running compatible SFTPPlus services behind a load balancer
  without compromising on the default CSRF checks.
  [server-side][http][https] [#5138]


Version 3.40.1, 2018-11-14
--------------------------


Defect Fixes
^^^^^^^^^^^^

* The option to hide the SFTPPlus authentication session from the
  `www-authenticate` headers is now visible in the Web Manager.
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
  Web Manager UI now shows that a restart is required for the event handler.
  [#5079]
* You can now change from the Web Manager the list of SSH ciphers available
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
* A defect was fixed in Web Manager which was causing the Web Manager to
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
* You can now define multiple authentication methods for the Web Manager
  service. [manager] [#5010-2]
* OS authentication method was extended to allow defining a list of
  Operating System account groups which are allowed to act as administrators
  through the Web Manager service. [manager] [#5010]
* You can now use Web Manager to configure the accounts and groups of the
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
* Comma-separated values in Web Manager can now be configured using a simple
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
  can explicitly define an OS authentication method for the Web Manager
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
  authentication mode from the Web Manager. In previous versions saving these
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
  from Web Manager. A password can be read only before being set and applied.
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
* The HTTP/HTTPS file transfer service and the Web Manager service now
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

* The HTTP/HTTPS file transfer service and the Web Manager service now
  advertise a set of HTTP headers to mitigate CSRF and XSS attacks. [security]
  [#4930]
* The low-level JSON-RPC used by the Web Manager service now explicitly
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
* The HTTP file transfer service and the Web Manager service were updated to
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
* When the destination of a transfer is changed, the Web Manager will not
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

* The Past Activity page, accessible from Web Manager,
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
* The Web Manager UI will not show the available locations inside the
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

* The Web Manager now shows the key fingerprint using SHA1 and SHA256,
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
  ("Web Manager") by clicking on any event link. [#3641]
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

* On Web Manager you can now access the configuration page of a component
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
* After applying the configuration changes using the Web Manager, the
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
  Manager is produced after the Web Manager page was closed or refreshed.
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
  which has a `Next Update` field earlier than current time. [security] [#3266]
* The configured certificate revocation list is now validated against the
  configured certificate authority. A failure is raised when the CA doesn't
  match the CRL. [security] [#3270]
* The state of a transfer is now correctly reported as stopped, when the
  transfer was stopped while in the `stalled` state. [client-side] [#3431]
* Properly and conservatively escape paths in the `admin-commands.sh` and
  `client-shell.sh` Unix shell scripts to allow for paths with spaces. Portably
  check for errors in `admin-commands.sh` and `client-shell.sh`. [#3442]
* Values for the `type` configuration options are now case-insensitive. [#3449]
* Web Manager web GUI was updated to instruct web browser to update HTML
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
  generated when starting the SFTPPlus process, as well as in the Web Manager
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
* In the Web Manager the `Enabled` label for the configuration options was
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
* Loading a non-existent page in the Web Manager now produces a single event
  with ID 40001. [local-manager] [#3285]
* Starting the Web Manager or the documentation pages from the Windows Start
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
  auto-started on demand. In the Web Manager, the status for the databases
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

* When a component needs a restart, in the Status page of the Web Manager
  now is displayed the list of configuration options which determine the
  required restart.
* Add a new event handler which can send a copy of the events as email.
* Add configuration for defining an email client component which can be used
  to send email via a remote SMTP server.


Defect Fixes
^^^^^^^^^^^^

* Configuration for `local-file` event handler from the Web Manager GUI
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
* Display a warning when Web Manager UI is accessed in Compatibility View
  mode in Internet Explorer browser.
  [#3020][local-manager]
* Display a warning in the logon page if it's using an unsupported IE version.
  [#3028][local-manager]


Deprecations
^^^^^^^^^^^^

* Removed Startup column in Web Manager Status page for locations as they
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
