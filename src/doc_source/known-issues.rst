Known Issues
============

This is the list of known issues for the current release of SFTPPlus.


* [#3787] No support for non-ASCII characters in the server's installation
  path, on the Windows operating system.

  In order to ensure correct operation of SFTPPlus, please
  avoid using special Unicode characters in the installation folder path.

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

* [#1946] On Windows systems, the installation will not generate an
  install log file when running in silent mode.

* [#2057] SFTP symbolic links on Windows systems only work when using
  absolute paths.

* [#2383] On Windows systems, `execute_before`, `execute_after_success`, and
  `execute_after_failure` cannot be configured with a path containing space
  characters.
  Also, when any `execute_*` action is called for files containing
  non-ASCII characters, the passed file names are corrupted.

* [#3412] Files which are uploaded to the SFTPPlus using FTP or FTPS and for
  which the data channel is closed before the file was completely uploaded are
  reported as successfully uploaded.
  This is because when the file was successfully uploaded the data channel is
  closed in the same way.

* [#3602] The rotation time is not automatically changed when the system clock
  is changed (for example with daylight saving time).
  This leads the rotation being delayed when the clock is moved backwards.

* [#2127] When SCP protocol is used, you can only download a single file
  as part of a SCP session.

* [#4016] The FTP/FTPS client-side operation have no support for timezones.
  For a correct operation the client and server must use the same timezones and
  have the clock synchronized.

* [#3577] The FTPS client-side transfer can't upload/push empty files.

* [#4315] When uploading files to SharePoint online via the WebDAV client
  protocol, large files transfers (above 200MB) might fail with SharePoint
  online aborting the transfer and closing the connection by returning a
  404 error code without any reason.

* [#4811] Fully qualified domain names (FQDN) or hostnames resolving only to
  an IPv6 address are not yet supported as the listening address for a file
  transfer service.

* [#4869] When an HTTP file transfer service is closed for not being active,
  there is no explicit logout event.

* [#5071] For batch transfers, when using `execute_on_destination_before`,
  `execute_on_destination_after_success` and
  `execute_on_destination_after_failure` there is no way to define a command
  to be execute for each file from the batch.
  Only the last processed file is available as a variable.

* SFTPPlus only detects daylight saving time changes while starting.
  Timezone changes at runtime are not detected.
  If changing timezone on a system running SFTPPlus you need to restart
  SFTPPlus in order to apply the changes.

* [#5239] When the OS authentication method is configured with `group-name` or
  `group-name-with-default` the allowed source IP configuration and SSH
  public keys configuration are extracted from the default group.

* [#5189] The LDAPS authentication only works with IPv4.
  Only LDAP authentication is supported for IPv6 address literals.

* [#5115] SMB/Windows Shares authenticated via Kerberos Domain method are not
  yet supported. NTLM authentication is supported.
