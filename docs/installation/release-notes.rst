Release Notes
=============

This is the list of all changes for current SFTPPlus version.

..  toctree::
    :maxdepth: 1

    release-notes-v4
    release-notes-v3
    release-notes-v2
    release-notes-v1

.. release-notes-start


Version 5.19.0, 2025-11-10
--------------------------


New Features
^^^^^^^^^^^^

* IBM MQ server support was added as a location that can be used to send and
  receive messages from a queue and transfer them as files. [#7197]
* The `timeout` option was added to the Oracle Database location to configure
  the time to wait for the remote server to return a response.
  If no response is returned in the configured time, SFTPPlus will consider
  the connection lost.
  [client-side][oracle-database] [#7231]


Defect Fixes
^^^^^^^^^^^^

* When the connection to the Oracle Database is lost,
  it now automatically reconnects.
  [client-side][oracle-database] [#7231]
* The Web Manager UI for configuring seconds will no longer automatically
  normalize the measurement unit.
  In previous versions, if you would configure a value to 60 minutes,
  it was automatically converted to 1 hours.
  Now it stays as 60 minutes.
  The unit normalization is now performed only when the page is loaded.
  [manager] [#7234]
* The Oracle Database location now supports transferring empty files.
  [client-side][oracle-database] [#7240]
* The Web Manager UI is now functional for administrators that have
  permissions to only the configuration,
  without any permissions to server operations.
  For a better experience, it is recommended that configuration administrators
  have at least read permissions for the `/operations/` components.
  [manager] [#7243]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `/runnables/` role permissions was renamed to `/operation/`.
  The configuration is automatically migrated.
  The `/runnables/` permissions accidentally documented in version 5.1.0.
  [manager] [#7243]


Version 5.18.0, 2025-10-14
--------------------------


New Features
^^^^^^^^^^^^

* The interactive command line tool now support editing the input line,
  and session command history.
  [cli] [#3941]
* You can now create multiple security policies and associate them to different
  file transfer services.
  [server-side][security] [#4133]
* The Web Manager now has an UI to browse and select a path for locations.
  This can be used to configure the source, destination, or archive paths
  for a transfer.
  [client-side] [#5880]
* You can now test the configuration of a component,
  protocols, locations, resources,
  without having to save the configuration.
  [client-side] [#5893]
* The `client-shell` command line tool can now load location configuration
  from the SFTPPlus configuration file.
  [cli][client-side] [#6250]
* You can now configure SFTPPlus to block the source IPs when the connection is
  made.
  In previous version, there was only the option to block during the
  authentication process.
  [server-side][security] [#6678]
* You can now view the list of blocked source IP for a security policy,
  and delete a particular source IP.
  [manager] [#7053]
* The `client-shell` command line tool will now keep the history of commands
  from previous sessions.
  [client-side][cli] [#7179]
* The `oracle-db` location was added to allow sending and receiving files
  with content stored as rows in Oracle Database tables.
  [client-side][db] [#7194]
* The SMB location can now show the list of all available shares on the server.
  This is not available for Azure Windows Share servers from the Azure File
  service.
  [client-side][azure-file][azure-storage] [#7208]
* The Azure File location can now show the list of all available shares.
  [client-side][azure-file][azure-storage] [#7209]


Defect Fixes
^^^^^^^^^^^^

* The security policy focused on blocking of source IP that triggered
  multiple authentication failures was fixed.
  [server-side][security] [#4133]
* The SFTPPlus server now supports using RSA host keys, signed with SHA256 or
  SHA512, together with the
  `diffie-hellman-group14-sha256`,
  `diffie-hellman-group15-sha512`,
  `diffie-hellman-group16-sha512`,
  `diffie-hellman-group17-sha512`,
  `diffie-hellman-group18-sha512`,
  `diffie-hellman-group-exchange-sha256`
  key exchange algorithms.
  In previous version, for this combination of algorithms,
  SFTPPlus was failing with errors like
  `Disconnecting the SSH connection. bad packet length` or
  `Signature from server's host key is invalid`,
  since SFTPPlus was trying to sign using the SHA1 algorithm.
  [server-side][sftp][scp] [#7225]


Version 5.17.0, 2025-09-11
--------------------------


New Features
^^^^^^^^^^^^

* You can now configure a transfer to archive the files on a remote location.
  [client-side] [#6981]
* You can now use SFTPPlus to transfer files from SharePoint Online directories
  that have more than 1000 files.
  [client-side][sharepoint] [#7179]


Defect Fixes
^^^^^^^^^^^^

* The UI for the documentation embedded with Web Manager was fixed.
  [manager] [#7188]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* When *archive on failure* is enabled for a transfer, it is now supported only
  when the source location is a local filesystem.
  In previous versions, when the source was a remote location an empty file or
  partial file was archived.
  [client-side] [#6981]


Version 5.16.1, 2025-09-05
--------------------------

This is a maintenance bugfix release.


Defect Fixes
^^^^^^^^^^^^

* When the SFTP server authentication fails
  before obtaining a valid password or key,
  the error details will now contain the name of the associated user.
  [server-side][sftp] [#6979]
* An internal error is no longer generated after removing a service that had
  an expired certificate.
  [server-side][manager] [#7177]
* For HTTP uploads, the backend API is now called for any upload method.
  In the previous release it was called only for uploads done using the PUT
  method.
  [server-side][http] [#7181]
* The events emitted when handling SFTP files now contain the `requested_path`
  attribute. This is the path requested by end user, and it might be different
  to the actual file used to store the file.
  For example, when SFTPPlus will automatically add a UUID to the stored filename.
  [server-side][sftp] [#7184]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The following events were removed from the `success` event group and moved
  to the `informational` event group: 10020, 10030, 10033, 10034, 10063, 10065,
  10066, 10081, 10083, 10100, 10101, 30014.
  [server-side][ftp][sftp][event-handler] [#6979]


Version 5.16.0, 2025-08-28
--------------------------


Security Fixes
^^^^^^^^^^^^^^

* The SFTP server can now be configured to enforce the public key algorithms
  defined via the `ssh_cipher_list` service configuration.
  In previous versions it was accepting any public key algorithm.
  To maintain backward compatibility, SFTPPlus will continue to accept any
  public key algorithm, as long as no specific public key algorithm
  is defined in `ssh_cipher_list`.
  If `ssh_cipher_list = secure` it will still restrict the public keys
  algorithms to the list of secure ones.
  [server-side][sftp] [#7153]


New Features
^^^^^^^^^^^^

* The `http` file transfer service can be configured with a blocking HTTP
  event handler for file upload operation.
  When a file is uploaded, SFTPPlus can trigger a separate request to a backend
  HTTP API and will forward the HTTP response headers to the initial HTTP client
  that triggered the initial request.
  [server-side][http][api] [#2606]
* The `content-check` event handler was added to check if a file does or does not
  contain a specific content.
  [event-handler] [#7147]
* You can now define `User-Agent` as a custom header for HTTP event handlers and
  HTTP authentication methods.
  In previous versions, SFTPPlus was always overwriting a predefined value.
  [event-handler][http] [#7148]
* A new location dedicated to SharePoint Online was added.
  This uses the OAuth2 authentication with MS Graph API.
  [client-side][sharepoint] [#7166]


Defect Fixes
^^^^^^^^^^^^

* The Purview extension was updated to automatically retry on error.
  The configuration for the extension was updated to include `sdk_timeout`,
  `retry_count`, and `retry_wait` options.
  When communicating with the Purview API server,
  the default timeout was increased to 10 minutes.
  Previously, the timeout was 1 minute.
  [server-side] [#7136]
* When defining custom `headers` for the HTTP event handler you can now define
  a custom ``Content-Type`` header.
  [event-handler][http] [#7148]
* The SFTP location can now authenticate using RSA SSH keys to SFTP servers that
  don't support the `ssh-rsa` algorithm and only support the
  `rsa-sha2-256` or `rsa-sha2-512`.
  [client-side][sftp] [#7153]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `file-digest` event handler was converted to the `content-check`
  event handler.
  The configuration is automatically migrated.
  [event-handler] [#7147]


Version 5.15.0, 2025-08-11
--------------------------


Security Fixes
^^^^^^^^^^^^^^

* During Let's Encrypt initialization, a unique TLS placeholder certificate
  is now used.
  The TLS placeholder certificate is unique to each SFTPPlus installation and
  each SFTPPlus version.
  Previous versions were using a static placeholder certificate.
  [lets-encrypt] [#7127]


New Features
^^^^^^^^^^^^

* An event is now emitted when a configured certificate is about to expire.
  [security] [#4508]
* The `security-policy` configuration was added to unify the configuration for
  the `deny-username` and `ip-time-ban` authentication method.
  The `security-policy` is now automatically applied to all services.
  [server-side] [#5240]
* You can now use component name and event groups as filters for the
  Activity Log UI.
  [manager] [#5886]
* The `extract-archive` event handler now supports extracting Zip archive encrypted
  using the WinZIP AES.
  [event-handler][zip] [#7120]
* The Web Client GUI now has a button that allows selecting all the files
  from the current directory.
  [server-side][https] [#7134]
* Any configuration component now has a `created` and `changed` value.
  These values contain the date and time when that configuration was
  created or last changed.
  [manager] [#7144]


Defect Fixes
^^^^^^^^^^^^

* The `account_auto_disable_grace_interval` configuration option was added to
  delay auto-disabling an account that was re-enabled but didn't have the
  opportunity to trigger a successful login yet.
  In previous versions, when an account was auto-disabled due to inactivity,
  if an administrator was re-enabling that account, the account was
  automatically disabled right away as the account still did not have a
  recent login time.
  [server-side] [#7141]
* The account created date is kept when the configuration for the account is
  synchronized to nodes.
  In previous version, the account creation date was not included in the
  synchronized data.
  [cluster][manager] [#7144]
* The failure to start the `os` authentication method on Linux was fixed.
  This was a defect introduced in SFTPPlus 5.14.0
  [server-side][os] [#7149]
* The Let's Encrypt resource was fixed.
  This was a regression introduced in SFTPPlus version 5.13.0
  [server-side][https][lets-encrypt] [#7150]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `deny-username` and `ip-time-ban` authentication methods are now deprecated.
  Their functionality was replaced by the `security-policy` configuration.
  The authentication method continue to be supported until the next major version.
  It is recommended to review the configuration for the `security-policy` and then
  delete these deprecated authentication methods.
  [server-side] [#5240]


Version 5.14.0, 2025-06-27
--------------------------


Security Fixes
^^^^^^^^^^^^^^

* **(Breaking Change)** The Entra ID authentication method now requires to be configured using a
  `client secret` via the `password` configuration option.
  [entra-id] [#7057]


New Features
^^^^^^^^^^^^

* You can now configure an HTTP proxy that is used by default for any
  component, via the `[server] proxy` configuration option.
  In previous versions, each component required a separate direct proxy
  configuration.
  [client-side] [#3975-1]
* The Azure BLOB and Azure File location now support connecting via an HTTP
  proxy.
  [client-side][azure-file][azure-blob] [#3975]
* You can now configure the Google and Okta single sign-on authentication
  method to allow access only to members of specific cloud groups.
  [security][google-cloud][okta] [#6098]
* The Okta and Google Identity authentication method now support the
  `remove_username_suffix` and `api_scopes` configuration.
  [server-side] [#7057-1]
* You can now configure the Entra ID authentication method to allow access to
  administrators based on specific cloud groups.
  [server-side][entra-id] [#7057-2]
* The Entra ID authentication method now allows access to both direct group
  members as well as to transitive membership.
  [entra-id][server-side] [#7057]
* You can now configure the `application` authentication method to
  restrict user access only to the filtered groups.
  This is done using the `strict_group_access = yes` configuration option.
  In previous versions users would get access to all their associated
  groups as long as they were a member of at least one of the allowed
  groups for the authentication method.
  [server-side] [#7121]
* When the Web Manager service is configured with an invalid TLS certificate,
  the service will start using a fallback certificate.
  Administrators can then connect to the Web Manager and resolve the issue.
  [manager] [#7126]


Defect Fixes
^^^^^^^^^^^^

* The OS authentication method now generates an error when trying to use it
  on Alpine Linux, since it is not supported.
  [linux] [#7059]


Version 5.13.0, 2025-05-22
--------------------------


New Features
^^^^^^^^^^^^

* The Google Identity and Okta OpenID Connect authentication methods can now
  be used with SFTPPlus running behind an HTTP reverse proxy without
  requiring the proxy to publish the SFTPPlus Web Manager as the root URL.
  [server-side] [#4175]
* Synchronized remote SFTPPlus nodes can now send their logs to the main
  SFTPPlus controller.
  [manager][cluster] [#4879]
* You can now configure the event handlers to trigger based on events that
  are forwarded from remote SFTPPlus instances.
  [events] [#5320]
* Support was added for running client-side transfer on cluster nodes.
  [client-side][cluster] [#5795]
* A transfer can now be configured to skip a source file if the source file
  is removed after it was initially detected by the transfer.
  [client-side] [#7009]
* When updating or rolling back an SFTPPlus installation,
  server logs are no longer backed up alongside SFTPPlus files.
  Make sure you backup your server's logs independently of
  the SFTPPlus backups automatically done during update and rollbacks. [#7037]
* First time when you connect to the SFTPPlus Web Manager you have the
  option to configure the SFTPPlus installation as a node from an SFTPPlus
  cluster.
  [manager][cluster] [#7051]
* The SFTPPlus cluster now has a dedicated `controller` operation mode.
  The `node-sync` resource now needs to be explicitly started and configured
  in `cluster` mode to allow external SFTPPlus instances to access the
  configuration.
  [cluster] [#7052-1]
* The SFTPPlus cluster operating parameters are now configured using the
  `node-sync` resource running on the `controller` node.
  [cluster] [#7052]
* The Exchange Online location now supports remote to remote transfers,
  when the Exchange Online is the source location.
  [client-side][exchange-online] [#7073]
* You can now use the Web Manager to define member of an SFTPPlus cluster.
  This is done using the `node-sync` resource.
  [cluster][manager] [#7088]
* You can now configure a service, transfer, event handler, or resource to
  be active only on specific cluster nodes.
  [cluster] [#7090]
* The nodes in a cluster can now be configured to send the events to the
  central SFTPPlus controller.
  [cluster][manager] [#7095]


Defect Fixes
^^^^^^^^^^^^

* After a SFTPPlus version update, the default components are now automatically
  created at first run.
  This is a regression introduced in version 5.12.0 in which the default
  components were only created on the second run.
  [manager] [#4879]
* When a file to the Azure File service is partially transferred,
  the length of the file is now truncated to the size of the transferred data.
  In previous versions, the file was kept with zero bytes at the end of the file.
  [client-side][azure-file] [#7073]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The `Roles` page was removed from the Web Manager.
  It's content was moved to the `Administrators` page.
  [manager] [#5545]
* The event with ID `10093` was removed.
  It was emitted when the Explicit FTPS server was reconfigured to an unsecure FTP
  service and the server type was automatically updated.
  This change will now require a service restart.
  [server-side][ftp] [#7052]
* The administration roles should no longe be configured with the `sync`
  permission.
  A `cluster-node` should now be created and it automatically has the
  `sync` permission.
  [manager][cluster] [#7088]
* The `node_variables` option was removed from the configuration for an
  administrator.
  The configuration was moved to the `cluster-nodes` configuration.
  The configuration is automatically migrated.
  [manager] [#7089]


Version 5.12.0, 2025-04-11
--------------------------


New Features
^^^^^^^^^^^^

* SFTPPlus Web Client now supports single-sign-on (SSO)
  authentication via Google Cloud,
  and allows users to use the "Sign in with Google" service.
  [server-side][http] [#2610]
* The Okta OpenID Connect authentication method was added.
  This allows using Okta accounts to authenticate in SFTPPlus.
  [server-side] [#2618]
* You can now schedule a transfer based on the day of a month.
  [client-side] [#3232]
* You can now configure the Operating System authentication method to allow
  filesystem access as the SFTPPlus service account to authenticated OS users.
  You can still configure SFTPPlus to restrict filesystem access
  for authenticated OS users as configured at the operating system level.
  [server-side][security] [#5031]
* The `deny-username` authentication method now has a separate option to
  configure the list of denied administrators.
  In previous versions, denying access for both file transfer users
  and administrators was done using the same list.
  The configuration for existing authentication methods is automatically
  migrated.
  [server-side] [#5198]
* Authentication methods configured for a service but stopped are now skipped.
  Credentials can still be validated by remaining configured authentications.
  In previous versions, authenticating a user immediately failed
  when encountering a stopped configured authentication method.
  [server-side] [#5647]
* You can now use SFTPPlus transfer to send files as attachments to emails.
  [client-side][smtp] [#7008]
* When updating or upgrading an existing SFTPPlus installation
  using a self-extractable package, its scripts are used
  instead of those bundled with the installed version. [#7021]
* When a new authentication method is created, it is now automatically
  appended to the ordered list of default active authentications.
  [server-side] [#7047]


Defect Fixes
^^^^^^^^^^^^

* The AS2 server-side URL now support URLs with a trailing slash.
  This is a regression introduced in version 5.6.0.
  [server-side][as2] [#5055]
* When the `authentications` configuration option is left empty
  for the Web Manager service, it no longer falls back to
  the general list of authentication methods configured for SFTPPlus.
  In previous versions, Web Manager would fall back to
  the default SFTPPlus authentication methods.
  [server-side] [#5198]
* An internal server error is no longer generated when a remote SFTP connections
  is requesting setting environment variables.
  The request to set an environment variable is now just ignored.
  [server-side][sftp] [#6703]
* You can now set a CRL in association with a Certification Authority
  certificate defined as PEM content inside the .INI configuration file.
  In previous versions, the CRL was supported only in association with a
  Certification Authority certificate stored as a separate file. [#6977]
* Events with IDs 20021, 20067, 20137, and 20142, emitted by the file transfer
  services
  are now associated with the service and user that triggered these events.
  [server-side][sftp][ftp][http] [#7048]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The Entra ID authentication method now accepts for the `group_association`
  configuration the value `base-and-cloud-groups` instead of
  `base-and-azure-groups`.
  The previous `base-and-azure-groups` continues to be supported.
  Old configurations are automatically migrated.
  [server-side][entra-id] [#2610]
* The Entra ID configuration option `application_id` was removed and replaced
  with the option `client_id`.
  No manual configuration change is required.
  Old configurations are automatically migrated.
  [server-side][entra-id] [#2618]
* The description of an OS account was changed from `os not in config` to `os`
  and from `os` to `os with config`.
  This is a cosmetic change only affecting messages for events with the ID
  `20137`.
  [server-side] [#7061]


Version 5.11.0, 2025-03-18
--------------------------


New Features
^^^^^^^^^^^^

* Emails sent by the event handler can now include information to identify the
  SFTPPlus server and the event handler that generated them.
  [email] [#4532]
* The `node-sync` resource was added to allow a secondary SFTPPlus instance to
  synchronize from a primary SFTPPlus instance by automatically pulling
  the configuration from the main/primary SFTPPlus node.
  [manager] [#4984]
* When loading a PFX/P12 certificate file through Web Manager,
  you can now set it as the certificate
  to be used for a relevant protocol of the SFTPPlus server.
  [https][ftps][manager] [#6773]
* When failing to setup the TLS session over the data channel of a
  FTPS connection, the cause of the error is now logged in more detail.
  [server-side][ftps] [#6970]
* The filtering user interface from the Activity Log page now defaults to
  searching the content of the logged messages.
  [manager] [#6993-1]
* The Activity Log page from SFTPPlus' Web Manager now defaults to showing logs
  from the last 12 hours.
  [manager] [#6993]
* The Let's Encrypt resource can now save the obtained keys and certificates
  as PEM files in a configurable local directory.
  [lets-encrypt][manager] [#7006]
* The SFTP server can now show its clients a banner message
  before asking for user credentials.
  This is configured via the `before_login_message` option.
  [server-side][sftp][scp] [#7028]


Defect Fixes
^^^^^^^^^^^^

* Generated TOTP QR code images are now visible when using SFTPPlus'
  Web Manager behind an HTTP reverse proxy with a custom URL path.
  [manager] [#6997]
* When failing to get a response from the Purview API, two retries are now
  scheduled with a delay period of 15 seconds.
  This reduces the error rate caused by intermittent network issues
  while using the Purview API.
  [purview] [#7024-1]
* Expired Purview sessions are now successfully cleaned from the SFTPPlus cache.
  This is a regression introduced in version 5.10.0.
  The Purview session cache could end in a state that
  triggers the `AlreadyCalled()` error after each login,
  which prevents obtaining a new session.
  [purview] [#7024]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The Let's Encrypt `contact_email` configuration option was removed
  because the Let's Encrypt service no longer sends notification emails.
  [lets-encrypt] [#7006]
* The SFTP and SCP server-side protocol `banner` configuration option was removed.
  This configuration option was not associated with any functionality.
  [server-side][scp] [#7028]


Version 5.10.0, 2025-02-18
--------------------------


New Features
^^^^^^^^^^^^

* Self-extractable installers are now available for Linux and macOS.
  The gzipped TAR archives continue to be available for these operating systems.
  [#6197]
* Self-extractable installers can now be used to update an already existing
  installation of SFTPPlus. [#6973]
* All server-side account passwords stored in legacy plain-text format
  are now automatically converted to a secure hash format when starting SFTPPlus.
  [server-side][security] [#6968]


Defect Fixes
^^^^^^^^^^^^

* When using operating system accounts through SFTPPlus in conjunction with
  the SFTP protocol and filesystems that can block, such as NFS,
  the main SFTPPlus process is no longer kept in the security context
  of an OS account for which the filesystem access was blocked
  by the operating system. [server-side][sftp] [#6816]
* For SFTPPlus installations on filesystems which make use of
  Access Control Lists (ACLs) of files and directories, as set with setfacl(1),
  using the scripts in `bin/` now scrubs the extended permissions
  not only when installing, but also when updating and rolling back. [#6952]
* When a user with an active Purview API session logs out, SFTPPlus
  only ends the Purview API session associated with their web browser.
  In previous version, when an user was logged out or a session expired,
  all Purview API sessions from all connected web browsers were logged out.
  [server-side][purview] [#6983]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The event with ID `20069` was removed.
  This event was emitted at SFTPPlus start time, and was informing that the
  process is not running as root.
  This functionality was replaced with event `20008`, which is now emitted when
  SFTPPlus is running as root. [#6816]


Version 5.9.1, 2025-01-29
-------------------------

This is an update that fixes a few errors found in version 5.9.0.
Version 5.9.0 was available only as a preview.


New Features
^^^^^^^^^^^^

* The AS2 location can now send compressed files to AS2 servers with limited
  support for parsing `smime-type` headers.
  SFTPPlus now sends the value of the `smime-type` parameter from the
  `Content-Type` header without using double quotes.
  Some AS2 servers, like Boomi, were failing to detect the AS2 message type.
  [client-side][as2] [#6910]


Defect Fixes
^^^^^^^^^^^^

* The FTP/FTPS server is now compatible with FTP clients that are sending the
  passive transfer commands before establishing the new passive TCP connections.
  This is implemented via the `passive_wait_connection` configuration option.
  This makes SFTPPlus compatible with the Globalscape FTP/FTPS client.
  [server-side][ftp] [#6953]
* The event handler web GUI now allows searching for specific components.
  This is a regression introduced in SFTPPlus 5.6.0.
  [manager] [#6960]


Version 5.8.0, 2025-01-13
-------------------------


New Features
^^^^^^^^^^^^

* The AS2 server can now receive files encrypted using the RSA AES OAEP
  algorithm.
  [server-side][as2] [#6869]
* Event handlers of type `extension` can now define the `TARGET_EVENTS` instance
  member that configures events for which the handler is triggered.
  [api] [#6873]


Defect Fixes
^^^^^^^^^^^^

* When the AS2 client requests an unsigned MDN for a signed payload,
  the SFTPPlus server returns an MDN that has a `Received-Content-MIC` field
  generated using the same digest algorithm as the signed payload.
  In previous versions, SFTPPlus was using SHA256 for unsigned MDNs.
  [server-side][as2] [#6831]
* The Purview extension now refreshes the API token for file transfer sessions
  that take more than one hour.
  In previous versions, the Purview API access was not refreshed, and it was
  rejected by the Purview server one hour after logging in.
  [server-side][http][purview] [#6873]
* Linux and macOS SFTPPlus setups using mount points for the installation paths
  can now be automatically updated and restored using the scripts in `bin/`. [#6940]


Version 5.7.0, 2024-11-25
-------------------------


Security Fixes
^^^^^^^^^^^^^^

* Our Python-based runtime has been updated to version 3.12.6. [#6820]


New Features
^^^^^^^^^^^^

* The SFTP location now supports setting up authentications
  requiring both password and private SSH key.
  [client-side][sftp] [#5295]
* You can now configure an AS2 location with `debug` enabled.
  This generates log files for all requested and received HTTP headers.
  [client-side][as2] [#5829]
* The shell scripts located in `bin/`, used for installing, updating, rolling
  back, and uninstalling SFTPPlus on Linux and macOS, now support the option
  to use an existing operating system user for the SFTPPlus setup.
  However, it is still highly recommended to use a dedicated OS user
  for running SFTPPlus. This dedicated user can be created automatically
  during the SFTPPlus installation or separately beforehand. [#6275]
* You can now configure transfers to send files to the destination location
  using a relative path.
  [client-side] [#6901]
* The Purview SDK for Windows is now distributed together with the
  SFTPPlus installer.[#6951]


Defect Fixes
^^^^^^^^^^^^

* The Entra ID authentication method now supports users that are members of
  100 groups or more.
  [server-side][entra] [#6806]
* When closing the SSH connection for an SFTP location,
  the code 11 (SSH_DISCONNECT_BY_APPLICATION) is now used to signal
  that closing the connection is expected.
  In previous versions, code 10 (SSH_DISCONNECT_CONNECTION_LOST) was used,
  signalling that the SSH connection was accidentally closed.
  [client-side][sftp] [#6870]
* The `exchange-online` location can now transfer attachments from folders
  that have more than 10 subfolders.
  [client-side][exchange-online] [#6874]
* The `set-on-first-connection` configuration option for TLS connections can now
  be used with URLs with no port explicitly defined.
  [security] [#6876]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* The dedicated `ssh_private_key_password` configuration option was added
  to the SFTP location, superseding the `password` option.
  When both `password` and `ssh_private_key` options are defined,
  the value of the `password` option is migrated to the
  `ssh_private_key_password` one.
  The `password` configuration option is removed as a result of the migration.
  This migration is automated, there is no need for manual changes.
  [client-side][sftp] [#6894]


Version 5.6.0, 2024-10-29
-------------------------


Security Fixes
^^^^^^^^^^^^^^

* The embedded OpenSSL library in SFTPPlus has been updated to version 3.3.2.
  [#6770]


New Features
^^^^^^^^^^^^

* SFTPPlus now supports the symmetric SSH cipher algorithms
  `aes256-gcm@openssh.com` and `aes128-gcm@openssh.com`.
  [client-side][server-side][sftp] [#5468]
* You can now configure an AS2 location to receive asynchronous MDN messages.
  [client-side][as2] [#5400]
* The user interface for the event details view in the Activity log has been
  updated [#6179]
* The AS2 location can now be configured to send compressed files.
  [client-side][as2] [#6756]
* You can now duplicate/clone an existing transfer using the Web Manager GUI.
  [manager] [#6774]
* The AS2 server now supports signatures that are advertised to use the
  `sha256_rsa` algorithm name.
  This is an alternative name for the `rsassa_pkcs1v15` algorithm,
  which implements PKCS#1 v1.5 signatures.
  [server-side][as2] [#6775]
* The AS2 location can now be configured to use the GET method to
  test the availability of the remote AS2 server.
  [client-side][as2] [#6817]
* On the Web Manager login page, you can now configure a short information
  box to provide additional usage or Terms of Service information.
  [manager] [#6833]
* The HTTP REST API used by the SFTPPlus web server is now available as an
  OpenAPI version 3.1 YAML file.
  [server-side][http][https] [#6856]


Defect Fixes
^^^^^^^^^^^^

* The help text for the `Authenticate Peer Certificate` TLS configuration
  from Web Manager has been updated to indicate that the default value is now
  `set-on-first-connection`.
  [manager] [#4099]
* The AS2 server now returns the errors as MDN messages.
  In previous versions, an HTTP 400 Bad request response was used to signal
  an error.
  [server-side][as2] [#5794]
* The Windows Share / SMB location no longer raises the `STATUS_BAD_NETWORK_NAME`
  error when configured with an invalid path, such as when using backslash path
  separators. [client-side][smb] [#6239]
* When using an Exchange Online location, if there is an error retrieving the
  list of attachments for an email that has just been removed, the email is now
  ignored. An error was raised in previous versions under such circumstances.
  [client-side][exchange-online] [#6601-2]
* When an HTTP request fails, the error now includes specific HTTP information.
  In previous versions, an internal server error message was used
  instead of a specific HTTP error.
  [client-side][http] [#6601]
* On Windows, the limit of total concurrent opened files was increased to 2048.
  [windows] [#6770]
* When the SFTPPlus server sends asynchronous MDN messages,
  it now sets the `Content-Type` HTTP header to indicate that the
  content is a MDN message.
  In previous versions, the `Content-Type` header was set to
  `application/octet-stream` instead of `multipart/signed`.
  [server-side][as2] [#6775-1]
* When the SFTPPlus server sends asynchronous MDN messages,
  the message that the AS2 file was successfully received is emitted only after
  the MDN message has been successfully delivered.
  [server-side][as2] [#6775]
* The AS2 service can now receive signed files with the signature stored in
  binary format.
  [server-side][as2] [#6778]
* When uploading files to Azure Files, the paths configured using backslashes
  as separators (Windows path separators) are automatically converted to
  forward slashes (Unix path separators).
  Previously, the Azure Files cloud server accepted backslash-separated paths.
  Following a recent update, only forward-separated slashed are now supported.
  [client-side][azure-files] [#6811]
* When sending AS2 files, the MDN message returned by the remote AS2 server
  no longer needs to contain the "Original-Recipient" or "Final-Recipient"
  headers. [client-side][as2] [#6817-1]
* The AS2 location now includes the AS2-From and AS2-To headers when making the
  HEAD or GET requests to test the availability of the remote AS2 server.
  In previous versions, the request was made without any extra headers.
  [client-side][as2] [#6817]
* The AS2 transfers can now receive AS2 messages from certificates that
  have the serial number as one of the components of the subject field.
  [server-side][client-side][as2] [#6818-1]
* The AS2 transfer can now receive AS2 messages for which the multipart boundary
  option name is defined in uppercase.
  [server-side][client-side][as2] [#6818]
* The macOS `launchd` .plist configuration file is now generated with log
  files inside the SFTPPlus log directory.
  This is a regression introduced in 5.0.0 which will prevent the macOS
  SFTPPlus service to start using `launchd`.
  [macos] [#6864]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Alpine Linux 3.12 is no longer supported. We recommend using an Alpine Linux
  version with upstream support, currently Alpine Linux 3.17 or newer. [#6770]


Version 5.5.0, 2024-07-22
-------------------------


New Features
^^^^^^^^^^^^

* The Purview extension now supports recursively handling all files in
  set directories. [#4759]
* The SFTP server protocol now supports handling blocking filesystems
  such as mounts from NFS servers which occasionally stop responding.
  [server-side][sftp] [#5001]
* The shell script `bin/auto-update.sh` was added for automatically updating
  licensed SFTPPlus installations on Linux and macOS when there's a newer
  version online. [#5664]
* The OpenSSL library embedded with SFTPPlus was updated to version 3.2.2.
  [security] [#6735]


Defect Fixes
^^^^^^^^^^^^

* When processing Exchange Online email subjects containing characters not valid
  on Windows (for example, colons), SFTPPlus now replaces those characters with
  dashes. [client-side][exchange-online] [#5040]
* You can now use long file paths for Windows Share UNC paths. These are paths
  such as `\\\\server.name\\share.name\\path\\file.txt`. [windows] [#6639]
* Web Client's icons are visible again. This was a regression
  introduced in version 5.4.0. [server-side][http] [#6744]


Version 5.4.0, 2024-06-17
-------------------------


Security Fixes
^^^^^^^^^^^^^^

* The Windows service and uninstaller are now invoked using double quotes
  around the executable path. This can prevent a conflict when, for example, you
  have SFTPPlus installed in `C:/Program Files`, but you already have a
  `C:/Program.exe` executable. [windows] [#2609]
* The TLS `secure` list of ciphers was updated to match the latest Mozilla
  recommended configuration for a general-purpose server.
  [server-side][client-side][security] [#6057]
* Support was added for `hmac-sha2-256-etm@openssh.com` and
  `hmac-sha2-256-etm@openssh.com` SSH hash-based message authentication code
  (HMAC) algorithms. [client-side][server-side][sftp] [#6717]
* The HTTP file server protocol now sets the `secure` attribute
  of the session cookie for connections made via an HTTPS reverse proxy. [#6722]


New Features
^^^^^^^^^^^^

* The activity log now contains an audit log entry for files downloaded
  through Web Client as a ZIP archive bundle. [server-side][http] [#2055]
* The HTTP server now emits an event when an authenticated session
  times out. [server-side][http][https] [#4869]
* You can now use an Exchange Online mailbox as the source for a transfer.
  [client-side][email] [#6656]


Defect Fixes
^^^^^^^^^^^^

* Low-level operating system errors are no longer displayed unchanged when
  an unknown OS error is encountered. In previous versions, all details were
  displayed, including the full path to user files. [server-side][http]
  [#2370]
* An internal error is no longer generated when listing empty folders over
  FTPS. When listing an empty folder, some FTPS servers close the data
  connection before confirming its end via the command connection. This was
  causing SFTPPlus to fail validating the server connection. This is a
  regression introduced in SFTPPlus 4.34.0. [client-side][ftps] [#2441]
* The Purview event handler extension now uses the same proxy configured
  for the Entra ID authentication method. [server-side] [#4085]
* Authentication without HTTP cookies works again in Web Client. This is
  a regression introduced in version 5.0.0. [server-side][http] [#4869]
* When a transfer fails to get content from the source directory,
  the transfer no longer fails.
  Instead a new attempt is retried based on the transfer configuration.
  [client-side] [#6674]
* When a transfer fails to get the status of the remote location, the emitted
  event with ID `60005` now contains the number of retries left and the retry
  interval. [client-side] [#6674]
* The event with ID `60074` is no longer emitted when failing to take
  a snapshot of the remote location for a non-recursive transfer. In previous
  versions, the event was emitted reporting an empty directory. For recursive
  transfers, the event with ID `60074` is still emitted because some servers
  raise a generic error instead of a "file not found" error when a recursive
  directory is removed from the remote location. [client-side] [#6674]
* Events with ID 10023, 10032, 10064, 10070, 10079, and 10084 were added to the
  `failure-high` event group. Previously, they were members of the
  `failure` event group exclusively. [ftp][ftps] [#6711]
* When configuring SFTPPlus to start under the `root` account in order to
  authenticate OS users, the server configuration cache file is now owned by
  the dedicated SFTPPlus service account. In previous versions, the
  `server.ini.cache` file was created as the `root` account, raising an error
  from SFTPPlus, which drops privileges after launch. [#6725]


Version 5.3.0, 2024-05-16
-------------------------


New Features
^^^^^^^^^^^^

* Azure Blob is now supported as source and destination of transfers.
  [client-side] [#5003]


Defect Fixes
^^^^^^^^^^^^

* If the `extract-archive` event handler fails to extract a `gzip` file, the
  partially-extracted destination file is now automatically removed. [#5803]
* When starting or stopping a location from Web Manager, the generated
  start/stop events are now associated with the administrator account that
  triggered those actions. In previous versions, the events were associated
  with the client username associated with the location. [manager] [#6647]
* Web Client sessions are no longer timing out during upload requests
  that take longer than the configured inactivity timeout. In previous
  versions, the current session was not updated to an active state while
  a file was uploaded, which could result in Web Client logoffs.
  [server-side][http][https] [#6668]
* When rolling back an SFTPPlus update on Linux, file capabilities such as
  binding privileged ports are now preserved. [#6660-2]
* When providing a custom backup path to rollback from, the `bin/rollback.sh`
  script no longer rolls back from the default SFTPPlus backup. [#6660]


Version 5.2.1, 2024-05-10
-------------------------


Defect Fixes
^^^^^^^^^^^^

* The login page alerts are now displayed only once. In previous versions, any
  alert related to a previous login failure was kept on the login page until
  the next successful attempt. [server-side][http][https] [#6662]
* The SFTP server now disconnects an SFTP client that requests to
  receive data, but doesn't update the channel transfer window using the
  SSH_MSG_CHANNEL_WINDOW_ADJUST SSH command. In previous versions, SFTPPlus
  was buffering the data to send for when the SFTP client was ready to receive
  it. This could cause high memory and CPU usage. [server-side][sftp]
  [#6684]


Version 5.2.0, 2024-04-17
-------------------------


New Features
^^^^^^^^^^^^

* You can now configure the list of accepted SSH host keys algorithms. In
  previous versions, SFPPlus was accepting remote SSH connections using any SSH
  host key algorithm. [client-side][sftp][scp][security] [#6553]
* The shell scripts in the ``bin/`` sub-directory used for installing,
  uninstalling, updating, and rolling back SFTPPlus on Linux and macOS, now
  feature the common switches for showing a help text: ``-h`` and ``--help``.
  [#6654]


Defect Fixes
^^^^^^^^^^^^

* The SFTP server now accepts public key authentication using any supported
  algorithm. In previous versions, it was only accepting authentications from
  the same list of algorithms as the one used for the SSH server host keys.
  [server-side][sftp][scp] [#6553]
* When login footnotes are enabled for SFTPPlus' Web Client, the dialog that
  pops up when clicking on the footnotes link now responsively handles large
  texts. [#6636]
* SFTPPlus works again on Windows Server 2016. This regression was introduced in
  SFPPlus version 5.0.0. [windows] [#6651]


Version 5.1.0, 2024-03-31
-------------------------


Security Fixes
^^^^^^^^^^^^^^

* The `ssl_certificate_authority` configuration option for TLS clients can now
  be configured with pinned public keys. This can be used to implement a
  security policy that requires pinning public certificates/keys.
  [security][https][#6562]


New Features
^^^^^^^^^^^^

* You can now configure an account or a group to limit the size for an uploaded
  file. [server-side][ftps][https][sftp] [#3652]
* The Web Manager console now automatically updates the process state in the
  background when you browse its pages. [manager] [#4843]
* Automatic installation, update, and restore are now supported on ARM64 Linux.
  [linux][arm64] [#6425]
* On Linux systems, when systemd restarts SFTPPlus, advanced systemd options
  are used to improve its default retry strategy. Some of these options are
  only activated with systemd 229 or newer, others require systemd 254 or
  newer. [#6443]
* The Web Manager console now shows the name of the operating system account
  under which SFTPPlus is running. [manager] [#6575]
* You can now configure multiple email addresses per account. [server-side]
  [#6579]
* The LDAP authentication method can now be configured to extract the email
  address associated to the authenticated user. [server-side] [#6590]
* The content for a transfer can now be converted on the fly from UTF-16 to
  UTF-8. [client-side] [#6592]
* You can now define the minimum number of files that are expected to be
  transferred in a time interval. This is done using the
  `minimum_transfer_count` and `minimum_transfer_interval` configuration
  options for a transfer. [client-side] [#6593]
* The filesystem `monitor` resource now emits the event with ID `20065` that
  includes the total number of files and directories detected in the monitored
  path. Event with ID `20065` is emitted only when the monitor is configured to
  check for old files or to auto-delete old files. [#6597]
* When the source directory for a transfer is no longer available, the transfer
  now waits for a time interval configured via `changes_poll_interval`, then
  fails the transfer, and finally stops retrying if the source is still not
  available after `retry_count` retries. An event and a log entry are generated
  for each try. In previous versions, it was only generating an event entry,
  retrying forever. [client-side] [#6600]
* The `home_folder_structure` configuration is now inherited from all groups,
  not only from the primary group. [server-side] [#6608]
* You can now configure the login page of the Web Client with a link to a
  custom text in a message box. You can use it to inform users about privacy
  policy, terms of use, or any other information. [server-side][http] [#6614]
* SSH private keys in Putty version 3 (PuTTY-User-Key-File-3) are now
  supported. [#6615]


Defect Fixes
^^^^^^^^^^^^

* When a SCP file upload operation fails, the server-side file is now closed. In
  previous versions, the file was left open. [server-side][scp] [#3652]
* On Linux and macOS systems, when stopping SFTPPlus without support from the
  init system while another process restarts it repeatedly, the cycle of stop
  retries ends after 20 iterations. [#6454]
* You can now configure an Entra ID authentication with a set of base groups
  that overlap with the associated groups as derived from the Entra ID group
  membership. [server-side][entra-id][azure-ad] [#6545]
* The Web Manager now keeps the session active while using the `Activity log`
  page. In previous versions, the session access time was not updated when
  using only the `Activity log` page. [manager] [#6607]
* Due to a regression introduced in version 5.0.0, SFTPPlus was not properly
  running on Amazon Linux 2 and Ubuntu 18.04 LTS. Only Linux distributions
  based on glibc version 2.26 and 2.27 were affected by this regression.
  [#6612]
* When downloading multiple files or multiple directories using the SFTPPlus
  Web Client, the memory consumption and file transfer speeds are now
  significantly improved. This regression was introduced in SFTPPlus version
  4.30.0. In affected versions, when downloading multiple files or directories,
  the transfer was very slow, and SFTPPlus' memory usage was unusually high
  during the transfer. This was caused by a programming error.
  [server-side][http][https] [#6624]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Event with ID 10090 generated for FTP EPRT command was removed and replaced
  with the event ID 10062. Event with ID 10062 is now emitted for any FTP
  active transfer, for both legacy and extended commands.
  [server-side][ftp][ftps] [#3652]
* The event with ID `10061` emitted at the start of a FTP `PASV` or `EPSV`
  command was removed. The event with ID `10022` presents the same information.
  [server-side][ftp] [#6424]
* The `azure-ad` authentication method was renamed to `entra-id`. This change
  follows Microsoft's renaming of `Azure Active Directory` service to `Microsoft
  Entra ID`. SFTPPlus configuration is automatically updated for the new name.
  [server-side] [#6545]
* The event with ID `60074` no longer has a `count` data attribute. It was
  replaced by the `total_directories` and `total_files` attributes. [#6597]


Version 5.0.0, 2024-02-20
-------------------------


Security Fixes
^^^^^^^^^^^^^^

* SMTP email client resources now require fully-qualified domain names
  when configured.
  This is needed in order to validate the TLS/SSL certificate
  of the remote server.
  If the SMTP server doesn't have a DNS record and a matching certificate,
  you need to explicitly disable TLS identity checks for your SMTP email client
  resource using the following configuration:
  `ssl_certificate_authority = disable-identity-security`
  [smtp][email] [#4374-1]
* WebDAVs locations now require fully-qualified domain names when configured.
  This is needed in order to validate the TLS/SSL certificate
  of the remote server.
  If the remote WebDAV HTTPS server doesn't have
  a DNS record and a matching certificate,
  you need to explicitly disable TLS identity checks for your WebDAVs location
  using the following configuration:
  `ssl_certificate_authority = disable-identity-security`
  [client-side][https] [#4374-2]
* The TLS clients in SFTPPlus
  (HTTPS event handlers, WebDAV locations, HTTPS authentications)
  are now configured by default to only function with remote servers that have
  certificates signed by the Certificate Authority discovered during the
  very first connection.
  The `ssl_certificate_authority = set-on-first-connection` is the default
  configuration for these cases.
  [https] [#4374]
* On Linux and macOS, SFTPPlus no longer starts under the root account when no
  service `account` is configured for running it. This change prevents
  unintentionally running SFTPPlus as root. It is highly recommended to run
  SFTPPlus as a dedicated non-root OS account at all times, but SFTPPlus can
  still be executed as root via the `account = root` configuration option under
  the `[server]` section. If you only need SFTPPlus to run as root for a
  specific purpose such as integrating with OS accounts, start SFTPPlus as root
  with a defined service `account` to have it drop root privileges as soon as
  possible. [linux][macos] [#4578]
* The server-side and client-side FTPS data connections now require TLS session
  reuse to be enabled by default. [server-side][client-side][ftps] [#6421]
* Components using TLS / HTTPS clients can now be configured to automatically
  accept and remember the Certificate Authority chain advertised during the
  first connection. All subsequent connections are then required to use the
  same CA chain. [client-side][https][ftps] [#6479]
* The embedded OpenSSL libraries were updated to version 3.2.1. All SFTPPlus
  packages now come with updated OpenSSL, including the ones supporting Red Hat
  Enterprise Linux 8 and Ubuntu Linux 18.04 or 20.04. [#6480]
* The `hmac-sha1` cipher was removed from the `secure` list of SSH ciphers.
  Note that the way SHA-1 is supported by SFTPPlus when handling SFTP
  connections does not allow for a feasible collision attack in the near
  future. However, as SHA-1 can be used in an unsafe way to sign SSH PKI
  certificates, many security scanners flag the support for SHA-1 as generally
  unsafe for any product supporting the SFTP protocol. If you still require the
  use of the SHA-1 algorithm to support legacy SFTP clients, you can still
  configure it as needed. [server-side][client-side][sftp] [#6484]


New Features
^^^^^^^^^^^^

* The Web Manager console now shows the name of the instance and
  the path to the installation directory. [manager] [#3851]
* SFTPPlus now supports macOS 11 Big Sur and newer on Apple Silicon. [#6064]
* You can now configure a TLS client to trust servers with SSL certificates
  signed by any of the root certificates from Mozilla's CA Certificate Program.
  More on this at https://wiki.mozilla.org/CA/Included_Certificates. To
  configure a TLS client to use this list, specify `${MOZILLA_CA_ROOTS}` for
  the option `ssl_certificate_authority`. [#6227]
* The Activity Log page in the Web Manager console has been redesigned
  to improve the readability of the rows of logging data.
  [#6328]


Defect Fixes
^^^^^^^^^^^^

* The Windows installer now supports administrator names and passwords
  containing spaces. [windows][#6452]
* The FTP/FTPS server now closes any file for which an upload request was
  started, but for which the upload operation failed. In previous versions, if a
  file transfer failed during the data transfer, the uploaded file was kept
  open by the server's operating system. [server-side][ftp] [#6514]
* When using automated updates on Linux, file capabilities such as
  binding privileged ports are now preserved for SFTPPlus installations.
  [#6498]


Deprecations and Removals
^^^^^^^^^^^^^^^^^^^^^^^^^

* Support for Windows 8 and Windows 2012 was removed.
* The `monitor` service was moved to the `resources` category. The
  configuration is automatically migrated after updating. [#3165]
* The events with ID 20001, 20002, and 20181 emitted when SFTPPlus starts or
  stops, now contain the installation `instance_name` instead of the
  `product_name`. [#3851]
* Support was removed for SFTPPlus Windows services created when
  installing SFTPPlus versions up to and including 4.0.0. SFTPPlus
  Windows services installed with SFTPPlus 4.1.0 or newer are still supported.
  [windows] [#5179-1]
* The priority of ECDSA key exchange algorithms for SSH was changed to the
  following order (from highest priority to lowest): ecdh-sha2-nistp256,
  ecdh-sha2-nistp384, ecdh-sha2-nistp521. This was done to achieve parity
  with the OpenSSH implementation. [sftp] [#5179]
* The `shared_secret` RADIUS configuration option was removed. It was replaced
  in a previous version with the `password` configuration option. The UI
  continues to refer to this configuration as `Shared Secret`, since this is how
  it is used in the RADIUS protocol specification. The low-level configuration
  uses `password` to make it easier to perform security audits.
  [server-side][radius] [#5304-1]
* The `address` and `port` WebDAV location configuration options were removed.
  They were replaced in a previous version with the `url` configuration option.
  [client-side][webdav] [#5304-2]
* The `address` configuration option for a transfer was removed. It was
  replaced in a previous version with the `delete_source_on_success` option.
  [client-side] [#5304-3]
* The `rsa_private_key`, `rsa_private_key_password`, `dsa_private_key`, and
  `dsa_private_key_password` configuration options were removed. They were
  deprecated in version 4 by the `ssh_host_private_keys` option. Encrypted
  SSH private keys are no longer supported. [server-side][sftp]
  rsa_private_key_password dsa_private_key rsa_private_key
  dsa_private_key_password [#5304]
* Apple macOS running on Intel hardware is no longer a supported platform.
  Contacts us if you need to run SFTPPlus on Intel Macs running macOS. [#6064]
* The `ftps_force_secured_authentication` configuration option was removed. The
  Explicit and Implicit FTPS server now always require a secure connection.
  [server-side][ftps] [#6509-1]
* The `ftps_force_secured_data_channel` configuration was removed. The security
  of the data channel is now always enforced based on the
  `ftps_force_secured_command_channel` configuration for the command channel.
  [server-side][ftps] [#6509-2]
* The Explicit FTPS server is now enabled by default for the FTP service.
  [server-side][ftps] [#6509-3]
* The support for FTP CCC command was removed on both server-side and
  client-side transfers. Consequently, the `ftps_ccc` configuration option was
  removed. Contact us if you still need to use the FTP CCC command.
  [ftps][server-side][client-side] [#6509]
