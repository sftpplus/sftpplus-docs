Release Notes for Version 1
===========================

This version is no longer supported.


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
