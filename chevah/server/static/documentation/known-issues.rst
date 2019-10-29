Known Issues
============

This is the list of known issues for the current release of SFTPPlus.


* [#1054] No support for non-ASCII characters in the server's installation
  path.

  In order to ensure correct operation of SFTPPlus, please
  avoid using special Unicode characters in the installation folder path.

* [#1245] Events logged in Windows Event Logger are listed without
  a specific Windows description.

  Events logged in Windows Event Logger are listed without a human
  friendly Windows description.
  Nevertheless, the data exported as XML is detailed and complete.

* Copying a Local Manager URL from within an authenticated session
  and pasting it in an unauthenticated session will prompt for the login page.
  After a successful authentication, the new session will redirect to the
  start page, not to the initial requested page.

* Collaborative configuration from multiple separate Local Manager sessions is
  not supported.
  The Local Manager allows opening multiple administration
  sessions, but assumes that only one session will change the configuration.
  Changes in one session will not be automatically reflected in the other
  session.
  You will need to refresh the page in order to see the changes.

* `Internationalized Domain Names <http://en.wikipedia.org/wiki/Internationalized_domain_name>`_
  are not supported.
  The server itself and all systems with which it interacts
  should use ASCII domain names.

* [#1400] When the server fails to start, it will only emit the general log
  event `20002` to signal that the server is stopping, without sending dedicated
  `20078` events for each service that was initially started.
  Service stop events are still emitted when a service is stopped at running
  time from the Local Manager or when the server is stopped in a normal way.

* [#1470] The Local Manager will not warn when adding multiple services,
  accounts, and groups with the same name.
  No error is generated because internally the server uses UUIDs for addressing
  these items.

* [#1547] When creating a new FTP or Implicit FTPS service, the passive
  port range is not updated in the GUI.
  After the new service creation has been applied on the server, the passive
  port range is available for changes.

* [#1588] On service start/stop the audit
  entries for these actions have no field mentioning the administrator
  requesting the action.

* [#1787] HTTP Post Request log handlers accept HTTPS URLs, but do not
  validate the SSL connection.

* [#1935] In the HTTP/HTTPS file service, actions can only be triggered by
  explicitly clicking on buttons.
  Actions cannot be triggered using the 'Enter' keyboard key.

* [#1946] On Windows systems, the installation will not generate an
  install log file when running in silent mode.

* [#2057] SFTP symbolic links on Windows systems only work when using
  absolute paths.

* When the server does not have write permissions to the configuration file and
  an administrator applies changes from the Local Manager, changes are applied,
  but they do not persist in the configuration.
  If you fix the permissions while the server is still running, there is no
  option to force a new save to the configuration file, other than making
  another change and applying it.
  Then, all previous changes will also be saved.

* [#2383] On Windows systems, `execute_before`, `execute_after_success`, and
  `execute_after_failure` cannot be configured with a path containing space
  characters.
  Also, when any `execute_*` action is called for files containing
  non-ASCII characters, the passed file names are corrupted.

* [#2547] When a password is used to import a private key which is not
  password-protected, the Local Manager will still inform you that the key
  is password-protected.

* [#94] FTP session reinitialization command (`REIN`) is not yet implemented.

* [#1160] FTP zlib compression command `MODE Z` is not yet implemented.

* [#1161] FTP cyclic redundancy check using the CRC-32 algorithm `XCRC` is not
  yet implemented.

* [#2357] FTP unique store command (`STOU`) is not yet implemented.

* [#3294] When the file was successfully transferred but failed to be removed
  from the source location, the transfer is considered failed but source file
  is archived as a success.

* [#3371] File dispatcher will not work for upload event for which the client
  is making the initial upload request under a provisional file name which is
  change once the file is successfully uploaded.

* [#3379] `hmac-sha2-512` is not yet available in our SSH implementation due to
  an interoperability issue with the OpenSSH client.

* [#2135] SCP server implementation does not handle errors reported by the
  client side during file get / download operations.

* [#3412] Files which are uploaded to the SFTPPlus using FTP or FTPS and for
  which the data channel is closed before the file was completely uploaded are
  reported as successfully uploaded.
  This is because when the file was successfully uploaded the data channel is
  closed in the same way.

* [#2975] When using Syslog over TCP and the TCP connection is lost, SFTPPlus
  will try to reconnect, but all events emitted while trying to connect are
  discarded.

* [#3478] When certificate revocation lists are configured, they will only
  work when the CA certificates are stored in a single file.
  Storing CA certificates in a single directory is not yet supported.

* [#3461] On Windows, it is not possible to load certificates and CA files
  stored on paths containing non ASCII characters.

* [#3494] When CRL distribution points (CDP) are configured only the first
  advertised HTTP CRL is used.

* [#4382] CRL distribution points (CDP) are not supported yet for client
  side connections when the client does not identify itself with a
  certificate.

* [#2672] Locations for FTP, FTPS and SFTP protocols will perform the
  connections using a fixed timeout of 10 seconds.

* [#3583] Certificate distribution points are not yet supported for the client
  side connections like FTPS locations, when no local certificate is configured.

* [#3602] The rotation time is not automatically changed when the system clock
  is changed (for example with daylight saving time).
  This leasds the roatation beying delayed when the clock is moved backwards.

* [#3594] FTPS CCC command is only supported with Explicit FTPS for both
  client and server side.
  It is not yet supported for Implicit FTPS.

* [#3599] FTPS CCC command is supported by the server-side only in
  active mode, while on the client-side only passive mode is supported.
  Please contact us if you need to communicate with a peer FTPS
  implementation which don't support the above described modes.

* [#3662] When using the components configuration option for an
  Event Handler the UUIDs are not yet verified to exist yet.

* [#3663] The event handler `target` configuration option is not yet
  validated and accepts mixing ignored and allowed event ids.
  When configured using both methods, it will behave as the `allow` method.

* [#3685] Multiline text with blank lines is not correctly parsed from
  the configuration file.
  The blank lines are removed.
  If you need to have a blank line in the configuration, please use `{LF}` in
  the line preceding the needed blank line.

* [#2127] When SCP protocol is used, you can only download a single file
  as part of a SCP session.

* [#4016] The FTP/FTPS client-side operation have no support for timezones.
  For a correct operation the client and server must use the same timezones and
  have the clock synchronized.

* [#4315] When uploading files to SharePoint online via the WebDAV client
  protocol, large files transfers (above 200MB) might fail with SharePoint
  online aborting the transfer and closing the connection by returning a
  404 error code without any reason.

* [#4811] Fully qualified domain names (FQDN) or hostnames resolving only to
  an IPv6 address are not yet supported as the listening address for a file
  transfer service.

* [#4869] When an HTTP file transfer service is closed for not being active,
  there is no explicit logout event.

* [#4945] As of 25th of May 2018, Microsoft CRL used by SharePoint online was
  serving a CRL which expires on the 23rd of May 2018.
  This causes the SharePoint Online CRL validation to fail.

* [#5000] When a transfer is configured in any of the available batch modes,
  SFTPPlus will no longer monitor it once a file is added to the queue.
  If a file is added to the transfer batch queue and the file is removed
  from the source,
  SFTPPlus will still try to transfer it and the transfer will fail as the
  source file is no longer there.

* [#5022] When a transfer has an Azure Files location as destination and is
  configured to rename existing files on destination, the transfer will fail
  as the rename operation is not yet implemented for Azure Files.

* [#5071] For batch transfers, when using `execute_on_destination_before`,
  `execute_on_destination_after_success` and
  `execute_on_destination_after_failure` there is no way to define a command
  to be execute for each file from the batch.
  Only the last processed file is available as a variable.

* [#5251] When the `external-executable` event handler is stopped, the external
  processes which were already started are not cancelled and will continue
  to execute.

* The anonymous authentication method can only be used with accounts defined
  in the main configuration. It does not support accounts from a separate
  local file or accounts from other authentication methods.
