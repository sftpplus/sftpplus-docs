


Generic and server-side common functionality
============================================












































































































































































































































































































































































































































































































































































































































20000
^^^^^


:Message: DEBUG: %(details)s
:Groups: authenticated, informational
:From version: 3.48.0
:To version: None
:Description: Event emitted when debug is enabled. This is a debug event only. This event should not be used for managed file transfer purposes.









20001
^^^^^


:Message: Starting %(product_name)s - %(product_version)s.
:Groups: process, informational, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :product_name: Name of the product


  :product_version: Current version of the product.











20002
^^^^^


:Message: Shutting down %(product_name)s - %(product_version)s.
:Groups: process, informational, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :product_name: Name of the product


  :product_version: Current version of the product.











20003
^^^^^


:Message: No service was started.
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: The server could not start any of the enabled services.









20004
^^^^^


:Message: Startup process failed. %(details)s %(traceback)s
:Groups: process, failure, failure-critical, operational
:From version: 3.6.0
:To version: None
:Description: The process failed while starting a component.









20005
^^^^^


:Message: Account &#34;%(account_name)s&#34; authenticated for &#34;%(username)s&#34; is disabled. Authenticated by %(method_name)s.
:Groups: failure, session, failure-specific, operational
:From version: 1.6.0
:To version: 3.37.0
:Description: None
:Data:
  :account_name: Name of the authenticated account.


  :method_name: Name of the authentication method which has authenticated this account.


  :username: Username under which the account was authenticated.











20006
^^^^^


:Message: Could not get protocol type for credentials.
:Groups: failure, session, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None









20007
^^^^^


:Message: Failed to start the service as current account. Could not drop process privileges to user &#34;%(account)s&#34;. Make sure you are starting the process as &#34;root&#34; account and that user &#34;%(account)s&#34; exists. It is defined by the [services] account configuration options from the server configuration file. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :account: Name of the account under which the server was trying to start.


  :details: Details about the failure reason.











20008
^^^^^


:Message: Failed to switch user context to %(username)s. Make sure the server is started as an root or administration account.
:Groups: failure, session, failure-high, operational
:From version: 1.6.0
:To version: 3.3.0
:Description: None









20009
^^^^^


:Message: User authenticated as %(account_kind)s account using %(credentials_kind)s credentials.
:Groups: authenticated, success, operational
:From version: 1.8.1
:To version: 3.0.0
:Description: None
:Data:
  :account_kind: Type of account authenticated on the server.


  :credentials_kind: Type of credentials used for authentication.











20010
^^^^^


:Message: Failed to configure the process. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 3.1.0
:To version: None
:Description: None









20011
^^^^^


:Message: Please configure &#34;%(section)s&#34; to listen on a port number in the range %(range_start)s - %(range_end)s. Current value %(port)s.
:Groups: process, failure, operational
:From version: 1.6.0
:To version: 3.18.0
:Description: The port was specified outside of allowed range.
:Data:
  :port: Value of current configuration.


  :range_end: The maximum value allowed for port.


  :range_start: The minimum value allowed for port.


  :section: Name of the configuration section with the bad configuration.











20012
^^^^^


:Message: SFTPPlus Webadmin URL has an invalid value. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None
:Data:
  :details: Details about the error.











20013
^^^^^


:Message: Could not check the remote SFTPPlus WebAdmin at &#34;%(url)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: Details about the error.


  :url: URL configured for SFTPPlus WebAdmin.











20014
^^^^^


:Message: There is no SFTPPlus Webadmin installed at %(url)s
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 1.6.0
:To version: None
:Description: None









20015
^^^^^


:Message: SFTPPlus home folder for user %(username)s is empty.
:Groups: failure, session, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None
:Data:
  :username: Name of the authenticated account.











20016
^^^^^


:Message: New Let&#39;s Encrypt certificate for &#34;%(domains)s&#34; used for service &#34;%(service)s&#34;.
:Groups: process, informational, operational
:From version: 3.40.0
:To version: None
:Description: None
:Data:
  :domains: Comma-separated list of domains with new certificates.


  :service: Name of the service on which the new certificate is used.











20017
^^^^^


:Message: Failed to get a new Let&#39;s Encrypt certificate for &#34;%(domains)s&#34;. %(details)s.
:Groups: process, failure, failure-critical, operational
:From version: 3.40.0
:To version: None
:Description: None
:Data:
  :domain: Comma-separated list of domains with new certificates.


  :service: Name of the service on which the new certificate is used.











20018
^^^^^


:Message: SFTPPlus details for user %(username)s does not contain any home folder.
:Groups: process, failure, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None









20019
^^^^^


:Message: User home folder &#34;%(path)s&#34; is not withing the root folder &#34;%(root)s&#34;.
:Groups: failure, failure-specific, operational
:From version: 1.6.0
:To version: None
:Description: This is a compat error.









20020
^^^^^


:Message: Port value must be an integer.
:Groups: process, failure, failure-specific, operational
:From version: 1.6.0
:To version: None
:Description: None









20021
^^^^^


:Message: Failed to authenticate user &#34;%(username)s&#34; with &#34;%(credentials_type)s&#34; credentials. Possible typo in username. No authentication method was able to handle the credentials.
:Groups: failure, session, failure-specific, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :credentials_type: Type of the credentials which were not authenticated.











20022
^^^^^


:Message: Property &#34;%(property_name)s&#34; for group &#34;%(group_name)s&#34; can not be inherited.
:Groups: process, failure, failure-specific, operational
:From version: 1.8.2
:To version: None
:Description: None
:Data:
  :group_name: Name of the group.


  :property_name: Name of the property that cannot be inherited.











20023
^^^^^


:Message: Failed to read authorized SSH keys file &#34;%(path)s&#34;. %(details)s
:Groups: failure, failure-high, authenticated, operational
:From version: 1.6.0
:To version: 4.0.0
:Description: None
:Data:
  :details: Details about the error.











20024
^^^^^


:Message: Internal error. Unhandled error. %(details)s
:Groups: process, failure, failure-critical, operational
:From version: 3.6.0
:To version: None
:Description: None









20025
^^^^^


:Message: SFTPPlus global user &#34;%(username)s&#34; not allowed on this server.
:Groups: failure, session, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None
:Data:
  :username: Denied username.











20026
^^^^^


:Message: SFTPPlus global user &#34;%(username)s&#34; allowed on this server.
:Groups: session, success, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None









20027
^^^^^


:Message: Could not authenticate against the remote SFTPPlus Webadmin at %(url)s
:Groups: failure, session, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None









20028
^^^^^


:Message: Property &#34;%(property_name)s&#34; for group &#34;%(group_name)s&#34; can not be set as inherited.
:Groups: process, failure, operational
:From version: 1.8.2
:To version: 3.18.0
:Description: None
:Data:
  :group_name: Name of the group.


  :property_name: Name of the property that cannot be inherited.











20029
^^^^^


:Message: Got an unknown response from SFTPPlus Webadmin. %(details)s
:Groups: failure, session, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None
:Data:
  :details: Details with actual server response.











20030
^^^^^


:Message: Could not get user configuration from the remote SFTPPlus Webadmin at %(url)s. %(details)s
:Groups: failure, session, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None
:Data:
  :url: URL form which user details were retrieved.











20031
^^^^^


:Message: Invalid account configuration for &#34;%(username)s&#34;. %(details)s
:Groups: failure, session, failure-high, operational
:From version: 1.6.0
:To version: None
:Description: None









20032
^^^^^


:Message: Failed to initialize the SSL/TLS context. Using cert:%(cert)s key:%(key)s ca:%(ca)s crl:%(crl)s. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :ca: Path to the certificate of the CA used by this SSL/TLS context.


  :cert: Path to X509 certificates.


  :crl: CRL used by this SSL/TLS context


  :key: Path to the key associated to the certificate.











20033
^^^^^


:Message: Internal error. Unhandled logged error. %(reason)s %(details)s
:Groups: process, failure, failure-critical, operational
:From version: 3.7.0
:To version: None
:Description: None









20034
^^^^^


:Message: Unknown protocol &#34;%(protocol)s&#34; for service &#34;%(service_uuid)s&#34;.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :protocol: Name of the unknown protocol.


  :service_uuid: Name of the service for which an unknown protocol was defined.











20035
^^^^^


:Message: Connection failed. Retrying %(retries_left)s more times after %(delay)s seconds. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 3.9.0
:To version: None
:Description: None
:Data:
  :delay: Number of seconds after which the connection is retried.


  :retries_left: Number of retries left.











20036
^^^^^


:Message: Failed to read the certificate revocation list located at &#34;%(uri)s&#34;. %(details)s
:Groups: failure, failure-high, authenticated, operational
:From version: 1.6.0
:To version: None
:Description: None









20037
^^^^^


:Message: Certificate revocation list located at &#34;%(uri)s&#34; and issued by &#34;%(issuer)s&#34; was successfully updated and has now %(count)s entries. Next publish advertised as %(next_publish)s. Next update advertised as %(next_update)s. Next update scheduled in %(update_seconds)s seconds for UTC %(update_datetime)s.
:Groups: informational, authenticated, operational
:From version: 3.13.0
:To version: None
:Description: None
:Data:
  :count: Number of loaded revoked certificates in the CRL


  :issuer: The subject field of the CRL&#39;s issuer.


  :next_publish: UTC date and time at which the CRL advertised its next publish


  :next_update: UTC date and time at which the CRL advertised its next update


  :update_datetime: UTC date and time at which the CRL will be loaded again


  :update_seconds: Number in seconds after which the CRL will be loaded again.


  :uri: Path or url from where the CRL was loaded











20038
^^^^^


:Message: Reloading failed for certificate revocation list located at &#34;%(uri)s&#34;. Next update scheduled in %(next_load)s seconds. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 3.14.0
:To version: None
:Description: None
:Data:
  :next_load: Number in seconds after which the CRL will be loaded again.


  :uri: Path or url from where the CRL was loaded











20039
^^^^^


:Message: The operational audit report was successfully generated at %(path)s.
:Groups: process, file-operation, success, operational
:From version: 3.23.0
:To version: None
:Description: None









20040
^^^^^


:Message: Invalid certificate &#34;%(subject)s&#34;. %(details)s
:Groups: failure, authenticated, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :subject: Certificate subject.











20041
^^^^^


:Message: Failed to create configuration for service &#34;%(service_name)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.8.0
:To version: None
:Description: None









20042
^^^^^


:Message: Created missing folder in home &#34;%(path)s&#34; with owner &#34;%(owner)s&#34; and group &#34;%(group)s&#34;.
:Groups: authenticated, success, operational
:From version: 1.8.3
:To version: None
:Description: A note that the account had a missing home folder, and it was created by the server.
:Data:
  :group: Name of the group for the new folder


  :owner: Name of the owner for new folder


  :path: Path to the created folder.











20043
^^^^^


:Message: Failed to retrieve group. %(details)s
:Groups: failure-critical, failure, authenticated, operational
:From version: 2.0.0
:To version: None
:Description: Error occurred while retrieving the group for new home folder.
:Data:
  :details: Details about the error.











20044
^^^^^


:Message: Failed to load the main configuration file for %(path)s. See previous error.
:Groups: process, failure, failure-high, operational
:From version: 2.0.0
:To version: 3.6.0
:Description: Error occurred while loading the main configuration file.
:Data:
  :path: Path from where configuration file was loaded











20045
^^^^^


:Message: Service &#34;%(service_name)s&#34; stopped with a failure. %(details)s
:Groups: failure, failure-high, authenticated, operational
:From version: 2.1.0
:To version: None
:Description: Service was stopped with a failure.
:Data:
  :details: Details about failure during stop.


  :service_name: Name of the service.











20046
^^^^^


:Message: Configuration changes stored in the local files.
:Groups: authenticated, success, operational
:From version: 1.6.0
:To version: None
:Description: None









20047
^^^^^


:Message: Bad value for passive port range. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the error.











20048
^^^^^


:Message: SFTPPlus global user &#34;%(username)s&#34; provided an invalid SSH key.
:Groups: failure, session, operational
:From version: 2.2.0
:To version: 3.0.0
:Description: None
:Data:
  :username: Denied username.











20049
^^^^^


:Message: Failed to save configuration changes to the local files. Changes will be discarded after server restart. %(details)s
:Groups: failure, failure-high, authenticated, operational
:From version: 2.6.0
:To version: None
:Description: None









20051
^^^^^


:Message: Successfully performing %(operation)s to &#34;%(path)s&#34; from &#34;%(source_path)s&#34;.
:Groups: process, success, operational
:From version: 3.43.0
:To version: None
:Description: None
:Data:
  :path: Path to the destination file which was encrypted/decrypted.


  :source_path: Path to the source file which was encrypted/decrypted.











20052
^^^^^


:Message: Failed to perform %(operation)s on &#34;%(real_path)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 3.43.0
:To version: None
:Description: None
:Data:
  :path: Path to the source file which was extracted.











20053
^^^^^


:Message: Successfully executed &#34;%(command)s&#34;. Exit code &#34;%(exit_code)s&#34;. Output &#34;%(output)s&#34;. Error &#34;%(error)s&#34;.
:Groups: process, success, operational
:From version: 3.47.0
:To version: None
:Description: None
:Data:
  :command: Executed command.


  :error: First part of the standard error produced by the command.


  :exit_code: Exit code of the executed command.


  :ouput: First part of the standard output produced by the command.











20054
^^^^^


:Message: Failed to execute &#34;%(command)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 3.47.0
:To version: None
:Description: None
:Data:
  :command: Executed command.











20055
^^^^^


:Message: Startup command executed with output &#34;%(output)s&#34; and error &#34;%(error)s&#34; and exit code &#34;%(exit_code)s&#34;.
:Groups: process, success, operational
:From version: 1.6.0
:To version: None
:Description: Called after executing the server startup command.
:Data:
  :error: Standard error data generated by the command.


  :exit_code: Exit code of the command.


  :output: Standard output data generated by the command.











20056
^^^^^


:Message: Failed to execute startup command &#34;%(command)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: None
:Description: Called when failing to execute the startup command.
:Data:
  :command: Name of the command.


  :details: Details about the failure reason.











20057
^^^^^


:Message: Startup command &#34;%(command)s&#34; took more than &#34;%(timeout)s&#34; seconds to execute.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 1.6.0
:To version: 3.47.0
:Description: Called when startup command took to long to execute
:Data:
  :command: Command that was launched.


  :timeout: Number of seconds after which the command execution was aborted.











20058
^^^^^


:Message: Internal error. Failed to get avatar for &#34;%(username)s&#34;. %(details)s
:Groups: failure-critical, failure, session, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: Details about the failure.


  :username: Name for the account for which the authentication failed











20059
^^^^^


:Message: Internal error. Failed to authenticate &#34;%(name)s&#34;. %(details)s
:Groups: failure-critical, failure, session, operational
:From version: 1.6.0
:To version: None
:Description: None









20060
^^^^^


:Message: Failed user configuration retrieval. Group &#34;%(group_uuid)s&#34; does not exists for account &#34;%(account_name)s&#34;
:Groups: failure, session, failure-high, failure-specific, operational
:From version: 1.8.2
:To version: 3.38.0
:Description: None









20061
^^^^^


:Message: Failed authentication. Group &#34;%(group_uuid)s&#34; does not exists for account &#34;%(account_name)s&#34;
:Groups: failure, session, failure-high, operational
:From version: 1.8.2
:To version: 3.0.0
:Description: None









20062
^^^^^


:Message: Failed to delete older database events: %(details)s
:Groups: process, failure, failure-high
:From version: 3.42.0
:To version: None
:Description: None









20063
^^^^^


:Message: Missing special group with name &#34;%(name)s&#34;. Please add it to your configuration. See documentation for more details about special groups.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 1.8.2
:To version: 4.0.0
:Description: None









20064
^^^^^


:Message: Failed to set new password. %(details)s
:Groups: failure, authenticated, operational
:From version: 3.42.0
:To version: None
:Description: None









20065
^^^^^


:Message: Failed to send log for %(logger_name)s. Error: %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None
:Data:
  :details: Details about the reason of the error.


  :logger_name: Name of the handler with failure.











20066
^^^^^


:Message: Stopping %(family)s &#34;%(name)s&#34; of type %(type)s due to too many failures.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.











20067
^^^^^


:Message: Failed to get home folder for account. %(details)s
:Groups: failure, failure-high, authenticated, operational
:From version: 1.6.0
:To version: None
:Description: None









20068
^^^^^


:Message: Failed to retrieve account details for &#34;%(username)s&#34;.
:Groups: failure, session, failure-high, operational
:From version: 1.6.0
:To version: 3.0.0
:Description: None
:Data:
  :username: Name of the account which failed.











20069
^^^^^


:Message: Server running under the same account under which it was started. If started as root or as an user with sudo access without passwords, it is highly recommended to configure the server to run under a dedicated account.
:Groups: process, informational, operational
:From version: 1.6.0
:To version: None
:Description: None









20070
^^^^^


:Message: Missing user impersonation capabilities. Server can not authenticate operating system accounts.
:Groups: process, informational, operational
:From version: 1.6.0
:To version: None
:Description: None









20071
^^^^^


:Message: Switching server process to &#34;%(account_name)s&#34; account.
:Groups: process, success, operational
:From version: 1.6.0
:To version: None
:Description: None









20072
^^^^^


:Message: Cryptography: %(cryptography_library_version)s. Privileges: %(process_privileges)s
:Groups: process, informational, operational
:From version: 1.6.0
:To version: None
:Description: Information about privileges of the process under which server is running.
:Data:
  :cryptography_library_version: Library used for cryptography and SSL/TLS protocols.


  :process_privileges: Details about the privileges available to the current process.











20073
^^^^^


:Message: Missing capabilities for creating missing local home folders.
:Groups: process, informational, operational
:From version: 1.6.0
:To version: None
:Description: None









20074
^^^^^


:Message: Missing capabilities for retrieving local home folder paths.
:Groups: process, informational, operational
:From version: 1.8.2
:To version: None
:Description: None









20075
^^^^^


:Message: Critical security error. The home folder &#34;%(home_folder_path)s&#34; might be in an inconsistent state. %(details)s
:Groups: failure-critical, failure, authenticated, operational
:From version: 2.0.0
:To version: None
:Description: None
:Data:
  :home_folder_path: Path to home folder.











20076
^^^^^


:Message: Service &#34;%(service_name)s&#34; started on &#34;%(address)s:%(port)s&#34; using &#34;%(protocol)s&#34; protocol.
:Groups: authenticated, success, operational
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :address: Address of the interfaces on which service is listening.


  :port: Port on which the service is listening


  :protocol: Protocol used by the service.


  :service_name: Name of the service that was started











20077
^^^^^


:Message: Failed to start the &#34;%(service_name)s&#34; service. %(details)s
:Groups: failure, failure-high, authenticated, operational
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :details: Details about the failure reason.


  :service_name: Name of the service which failed to start.











20078
^^^^^


:Message: Service &#34;%(service_name)s&#34; stopped.
:Groups: authenticated, success, operational
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :service_name: Name of the service.











20079
^^^^^


:Message: Current resource usage: cpu=%(cpu_percent)s%% mem-res=%(memory_resident)s mem-virt=%(memory_virtual)s conn=%(connection_count)s file=%(file_count)s thread=%(thread_count)s.
:Groups: process, informational, operational
:From version: 3.44.0
:To version: None
:Description: None
:Data:
  :connection_count: Total number of connections in use.


  :cpu_percent: Percentage of total CPU currently in use.


  :file_count: Total number of files (with connections and pipes) in use.


  :memory_resident: Total persistent/physical memory in bytes in use.


  :memory_virtual: Total memory in bytes (with swap) in use.


  :thread_count: Total number of threads in use.











20080
^^^^^


:Message: Resource usage trigger: %(details)s.
:Groups: process, failure, operational
:From version: 3.44.0
:To version: None
:Description: None
:Data:
  :details: Comma separated value of resources which have triggered this event.


  :triggers: Triggers as list of (name, value) tuple.











20081
^^^^^


:Message: No configured authentication for &#34;%(username)s&#34; of type &#34;%(credentials_type)s&#34;.
:Groups: failure, session, failure-high, failure-specific, operational
:From version: 4.0.0
:To version: None
:Description: None
:Data:
  :credentials_type: Type of the authentication request.


  :username: Name for which the authentication was requested.











20085
^^^^^


:Message: User successfully updated own password.
:Groups: authenticated, success, operational
:From version: 3.43.0
:To version: None
:Description: None









20086
^^^^^


:Message: User failed to update own password. %(details)s
:Groups: failure, authenticated, operational
:From version: 3.43.0
:To version: None
:Description: None









20087
^^^^^


:Message: File &#34;%(source_path)s&#34; was successfully amended to %(path)s.
:Groups: process, file-operation, informational
:From version: 3.22.0
:To version: None
:Description: None
:Data:
  :source_path: Path of the source file which was modified.











20088
^^^^^


:Message: Failed to amend file &#34;%(path)s&#34; from %(source_path)s. %(details)s
:Groups: process, file-operation, failure-high, failure
:From version: 3.22.0
:To version: None
:Description: None
:Data:
  :source_path: Path of the source file which was modified.











20089
^^^^^


:Message: Can not delete default group &#34;%(group_uuid)s&#34;.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 2.1.0
:To version: 4.0.0
:Description: None
:Data:
  :group_uuid: The uuid of the group for which delete action was requested.











20090
^^^^^


:Message: Unknown account type &#34;%(account_type)s&#34; for &#34;%(account_uuid)s&#34;.
:Groups: failure, failure-high, failure-specific, operational
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :account_type: The type defined for the account


  :account_uuid: The uuid of the account with unknown type.











20091
^^^^^


:Message: Unknown type &#34;%(type)s&#34; for section &#34;%(uuid)s&#34;.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :type: The type defined for the section.


  :uuid: The uuid of the section with unknown type.











20097
^^^^^


:Message: Failed to get home folder for account. %(details)s
:Groups: failure, session, failure-high
:From version: 2.0.0
:To version: None
:Description: None
:Data:
  :details: Details about the error.











20098
^^^^^


:Message: Invalid umask value &#34;%(umask)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 2.0.1
:To version: 3.6.0
:Description: None
:Data:
  :details: Details about the error.


  :umask: The umask value in used.











20099
^^^^^


:Message: Logger &#34;%(logger_name)s&#34; of type &#34;%(type)s&#34; was created.
:Groups: process, success, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logger that was created.











20100
^^^^^


:Message: Logger &#34;%(logger_name)s&#34; was removed.
:Groups: process, success, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logger that was removed.











20101
^^^^^


:Message: Stored hashed password for &#34;%(username)s&#34; is not valid. %(details)s
:Groups: failure, session, failure-high, operational
:From version: 2.2.0
:To version: 4.0.0
:Description: None
:Data:
  :details: More details about the error.


  :username: Username with a bad hashed password.











20102
^^^^^


:Message: Internal error. Failed to start the logger &#34;%(logger_name)s&#34;. %(details)s
:Groups: process, failure, failure-critical, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logging handler that reported the error.











20103
^^^^^


:Message: Internal error. Failed to stop the logger &#34;%(logger_name)s&#34;. %(details)s
:Groups: process, failure, failure-critical, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logging handler that reported the error.











20104
^^^^^


:Message: Failed to start the logger &#34;%(logger_name)s&#34;.
:Groups: process, failure, failure-high, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logging handler that reported the error.











20105
^^^^^


:Message: Failed to stop the logger &#34;%(logger_name)s&#34;.
:Groups: process, failure, failure-high, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logging handler that reported the error.











20106
^^^^^


:Message: Internal error. Failed at the logger &#34;%(logger_name)s&#34;. %(details)s
:Groups: process, failure, failure-critical, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logging handler that reported the error.











20107
^^^^^


:Message: Event handler &#34;%(name)s&#34; can not be started without a configured path.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 2.1.0
:To version: 3.40.0
:Description: None
:Data:
  :name: Name of the event handler that reported the error.











20108
^^^^^


:Message: Can not delete configuration &#34;%(uuid)s&#34; as it is still used by: %(usage)s.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :usage: List of components still configured to use this configuration.


  :uuid: The uuid of the configuration for which delete action was requested.











20109
^^^^^


:Message: File &#34;%(path)s&#34; was successfully fallback dispatched to %(destinations)s.
:Groups: process, file-operation, informational
:From version: 3.5.0
:To version: None
:Description: None
:Data:
  :destination_paths: List of destination where source path was dispatched.


  :destinations: Comma separated list of destinations where source path was dispatched.











20110
^^^^^


:Message: Failed to fallback dispatch file &#34;%(path)s&#34; to %(destinations)s. %(details)s
:Groups: process, file-operation, failure-high, failure
:From version: 3.5.0
:To version: None
:Description: None
:Data:
  :destinations: Comma separated list of destinations where source path was tried to be dispatched.











20111
^^^^^


:Message: Starting %(family)s &#34;%(name)s&#34; of type %(type)s.
:Groups: process, informational, operational
:From version: 3.9.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.











20112
^^^^^


:Message: Failed to perform %(action)s in db &#34;%(database_name)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: prototype
:To version: None
:Description: None
:Data:
  :action: Description of the action.


  :database_name: Database connection name.


  :details: Database error details.











20113
^^^^^


:Message: Invalid data for database entry. Columns %(columns)s. %(errors)s
:Groups: process, failure, failure-high, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: Database entry is invalid.
:Data:
  :columns: List of columns with invalid data.


  :errors: Data validation errors.











20114
^^^^^


:Message: Stop sending logs to logging database due to too many failures.
:Groups: failure, failure-high, failure-specific, operational
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :logger_name: Name of the logging handler.











20115
^^^^^


:Message: File %(path)s was not modified in the last %(age)s seconds.
:Groups: process, file-operation, informational
:From version: 3.5.0
:To version: None
:Description: None
:Data:
  :age: Number of seconds since the file was not modified.











20116
^^^^^


:Message: Invalid schema for table &#34;%(table_name)s&#34; in %(database_name)s. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 2.1.0
:To version: 4.0.0
:Description: Invalid table schema.
:Data:
  :database_name: Database connection name


  :details: Information about the error.


  :table_name: Name of table with invalid schema.











20117
^^^^^


:Message: %(name)s unable to fetch entries from &#34;%(database_name)s&#34;. Filter criteria: &#39;%(filter)s&#39;. Sort order &#39;%(sort_order)s&#39;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 2.1.0
:To version: None
:Description: None.
:Data:
  :database_name: Database connection name.


  :details: Information about the error.


  :filter: Filter criteria.


  :name: Name of the database source that failed.


  :sort_order: Sort order for the entries











20118
^^^^^


:Message: Fail to add log handler %(uuid)s. Configuration not found.
:Groups: process, failure, failure-high, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None.
:Data:
  :uuid: UUID for the log handler for which add operation was requested.











20119
^^^^^


:Message: Invalid public SSH keys for &#34;%(username)s&#34;. %(details)s
:Groups: failure, session, failure-high, operational
:From version: 2.9.0
:To version: 4.0.0
:Description: None
:Data:
  :username: Username to which the SSH public keys are associated.











20120
^^^^^


:Message: Wrong %(type)s value for option &#34;%(option)s&#34; in section &#34;%(section)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the error.


  :option: Name of the option that was set.


  :section: Name of the section in which option was set.


  :type: Type of value that was requested to be set.











20121
^^^^^


:Message: Cannot set %(type)s value %(value)s for option %(option)s in %(section)s. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :details: More details about the error.


  :option: Name of the option that was set.


  :section: Name of the section in which option was set.


  :type: Type of value that was requested to be set.


  :value: Value that was requested to be set.











20122
^^^^^


:Message: Could not parse the configuration file. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: 3.4.0
:Description: None









20125
^^^^^


:Message: Failed to &#34;%(mode)s&#34; file &#34;%(path)s&#34; to %(destinations)s. %(details)s
:Groups: process, file-operation, failure-high, failure
:From version: 3.5.0
:To version: None
:Description: None
:Data:
  :destinations: Comma separated list of destinations where source path was dispatched.











20126
^^^^^


:Message: Failed to start the Windows Event logger. %(details)s
:Groups: failure, failure-high, operational
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the error











20127
^^^^^


:Message: Logger &#34;%(logger_name)s&#34; started.
:Groups: administration, success, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logger.











20128
^^^^^


:Message: Logger &#34;%(logger_name)s&#34; stopped.
:Groups: authenticated, success, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logger.











20129
^^^^^


:Message: Logger &#34;%(logger_name)s&#34; is already stopped.
:Groups: informational, authenticated, operational
:From version: 2.1.0
:To version: 3.0.0
:Description: None
:Data:
  :logger_name: Name of the logger.











20130
^^^^^


:Message: File &#34;%(path)s&#34; was successfully &#34;%(mode)s&#34; to %(destinations)s.
:Groups: process, file-operation, informational
:From version: 3.5.0
:To version: None
:Description: None
:Data:
  :destination_paths: List of destination where source path was dispatched.


  :destinations: Comma separated list of destinations where source path was copied.











20131
^^^^^


:Message: Configuration file &#34;%(path)s&#34; does not exists.
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: 3.4.0
:Description: None









20132
^^^^^


:Message: Server process could not read the configuration file at %(path)s.
:Groups: process, failure, failure-high, operational
:From version: 1.6.0
:To version: 3.4.0
:Description: None









20135
^^^^^


:Message: Failed to authenticate &#34;%(username)s&#34;. No authentication method with UUID %(method_uuid)s.
:Groups: failure, session, failure-high, failure-specific, operational
:From version: 2.10.0
:To version: 3.37.0
:Description: None
:Data:
  :method_uuid: UUID of the unknown method.


  :username: Name of the account which requested to authenticate.











20136
^^^^^


:Message: Account &#34;%(username)s&#34; forbidden by %(method_type)s authentication &#34;%(method_name)s&#34; using &#34;%(credentials_type)s&#34; credentials. %(details)s
:Groups: failure, session, operational
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :credentials_type: Type of the credentials used during authentication.


  :method_name: Name of the method used for authentication.


  :method_type: Type of the method used for authentication.


  :username: Name of the account which requested to authenticate.











20137
^^^^^


:Message: Account &#34;%(account_name)s&#34; of type &#34;%(account_type)s&#34; from &#34;%(group_name)s&#34;, authenticated as &#34;%(username)s&#34; by &#34;%(method_name)s&#34; of type &#34;%(method_type)s&#34; using %(credentials_type)s.
:Groups: session, informational, operational
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :account_name: Name of the authenticated account.


  :account_type: Type of the authenticated account.


  :account_uuid: UUID of the authenticated account.


  :credentials_type: Type of the accepted credentials.


  :group_name: Name of the group/role associated to this account. (Since 3.38.0)


  :method_name: Name of the method used for authentication.


  :method_type: Type of the method used for authentication.


  :username: User name under which the authentication was requested.











20138
^^^^^


:Message: Ignoring %(method_type)s authentication &#34;%(method_name)s&#34; for &#34;%(username)s&#34; since it is not active.
:Groups: session, informational, operational
:From version: 2.10.0
:To version: 3.37.0
:Description: None
:Data:
  :method_name: Name of the method used for authentication.


  :method_type: Type of the method used for authentication.


  :username: Name of the account which requested to authenticate.











20139
^^^^^


:Message: SSLv3 detected for configuration &#34;%(configuration)s&#34;. SSLv3 method is no longer secure due to POODLE vulnerability. If SSLv3 is still required please make sure you use it together with the non-CBC cipher RC4-SHA.
:Groups: failure, failure-specific, authenticated, operational
:From version: 2.8.0
:To version: None
:Description: None
:Data:
  :configuration: Full configuration value in which SSLv3 is used.











20140
^^^^^


:Message: Connecting resource &#34;%(name)s&#34;.
:Groups: informational, authenticated, client-side
:From version: 3.9.0
:To version: None
:Description: None
:Data:
  :name: Name of the location associated with this event.











20141
^^^^^


:Message: Resource &#34;%(name)s&#34; successfully connected.
:Groups: authenticated, success, operational
:From version: 3.9.0
:To version: None
:Description: None









20142
^^^^^


:Message: Failed to get a valid response from the &#34;%(method_name)s&#34; authentication for the account &#34;%(username)s&#34;. %(details)s
:Groups: failure, session, failure-high, operational
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :method_name: Name of the authentication method which failed.


  :username: Name of the account for which the failure occurred.











20143
^^^^^


:Message: Failed to configure log rotation. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.7.17
:To version: None
:Description: None
:Data:
  :details: More details about the error.











20144
^^^^^


:Message: EventNotFound: Unknown event with id &#34;%(id)s&#34;. %(details)s
:Groups: process, failure, failure-critical, operational
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :details: Details error showing the source of this error.


  :id: ID of the original event.











20145
^^^^^


:Message: Failed to resolve text for event id &#34;%(id)s&#34; with data &#34;%(bad_data)s&#34;. %(details)s
:Groups: process, failure, failure-critical, operational
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :bad_data: Data of the original event


  :id: ID of the event with error.











20146
^^^^^


:Message: Failed to initialize logger as account &#34;%(username)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.8.0
:To version: 3.0.0
:Description: Error raised when the logger could not be initialized under the configured account.
:Data:
  :username: Name of the account under which the log file was trying to be initialized.











20147
^^^^^


:Message: Failed to load JSON file &#34;%(path)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.8.1
:To version: 3.4.0
:Description: Error raised when the JSON file could not be loaded.
:Data:
  :details: Details about failure reason.


  :path: Path to the JSON file.











20148
^^^^^


:Message: Bad format for JSON file &#34;%(path)s&#34;. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 1.8.1
:To version: 3.4.0
:Description: Error raised when the JSON file is not well formatted.
:Data:
  :details: Details about failure reason.


  :path: Path to the JSON file.











20149
^^^^^


:Message: Unknown keys for account configuration. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :details: List with keys which were not accepted.











20151
^^^^^


:Message: No EventGroupDefinition with name %(name)s.
:Groups: process, failure, failure-specific, failure-critical, operational
:From version: 1.6.0
:To version: None
:Description: The event group could not be found in the database. This is emitted before the event db is loaded









20152
^^^^^


:Message: No such property %(name)s.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 2.1.0
:To version: None
:Description: The property could not be found.
:Data:
  :name: Name of the requested property.











20153
^^^^^


:Message: No such section %(name)s.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 2.1.0
:To version: None
:Description: The section could not be found.
:Data:
  :name: Name of the requested section.











20154
^^^^^


:Message: Create not supported for %(name)s.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 2.1.0
:To version: None
:Description: Create operation is not supported.
:Data:
  :name: Name of the requested property.











20155
^^^^^


:Message: Delete not supported for %(name)s.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 2.1.0
:To version: None
:Description: Delete operation is not supported.
:Data:
  :name: Name of the requested property.











20156
^^^^^


:Message: Successfully started %(family)s &#34;%(name)s&#34; of type %(type)s.
:Groups: authenticated, success, operational
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.











20157
^^^^^


:Message: Stopped %(family)s &#34;%(name)s&#34; of type %(type)s. %(reason)s
:Groups: authenticated, success, operational
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :reason: Reason for which the component was stopped. It can be either due to a failure or normal stop request for shutdown or administrative actions.


  :type: Type of the component associated with this event.











20158
^^^^^


:Message: Failed to start %(family)s &#34;%(name)s&#34; of type %(type)s. %(details)s
:Groups: failure, authenticated, operational
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component which failed to start


  :name: Name of the component which failed to start.


  :type: Type of the component which failed to start.











20159
^^^^^


:Message: Failed to stop %(family)s &#34;%(name)s&#34; of type %(type)s. %(details)s
:Groups: failure, authenticated, operational
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.











20160
^^^^^


:Message: Unknown database &#34;%(database_uuid)s&#34; for %(family)s &#34;%(name)s&#34; of type %(type)s.
:Groups: process, failure, failure-high, failure-specific, operational
:From version: 2.6.0
:To version: 4.0.0
:Description: None
:Data:
  :database_uuid: UUID of configured database for event monitor.


  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.











20161
^^^^^


:Message: Disconnected %(family)s &#34;%(name)s&#34; of type %(type)s as database is not available.
:Groups: process, informational, operational
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.











20162
^^^^^


:Message: Resumed %(family)s &#34;%(name)s&#34; of type %(type)s as database became available.
:Groups: process, informational, operational
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.











20163
^^^^^


:Message: Internal error. Failure for account activity event handler &#34;%(name)s&#34;. %(details)s
:Groups: process, failure, failure-critical, operational
:From version: 2.6.0
:To version: 4.0.0
:Description: None
:Data:
  :name: Name of the event handler.











20164
^^^^^


:Message: Unable to migrate database &#34;%(database_uuid)s&#34; table for %(family)s &#34;%(name)s&#34; of %(type)s . %(details)s
:Groups: process, failure, failure-high, operational
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :database_uuid: UUID of configured database for event monitor.


  :details: Details about the migration error.


  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.











20165
^^^^^


:Message: Failure while running %(family)s &#34;%(name)s&#34; of type %(type)s. %(details)s
:Groups: failure, failure-high, authenticated, operational
:From version: 2.10.0
:To version: None
:Description: Used when the the component failed without an explicit error id.
:Data:
  :family: Family name of the component which failed to start


  :name: Name of the component which failed to start.


  :type: Type of the component which failed to start.











20166
^^^^^


:Message: File &#34;%(path)s&#34; was modified in monitor %(name)s.
:Groups: file-operation, process, informational, monitor
:From version: 2.10.0
:To version: None
:Description: None.
:Data:
  :name: Name of the monitor.











20167
^^^^^


:Message: File &#34;%(from_path)s&#34; was renamed in monitor %(name)s to &#34;%(to_path)s&#34;.
:Groups: file-operation, process, informational, monitor
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :from_path: Initial path.


  :to_path: Final path.











20168
^^^^^


:Message: Folder &#34;%(from_path)s&#34; was renamed in monitor %(name)s to &#34;%(to_path)s&#34;.
:Groups: file-operation, process, informational, monitor
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :from_path: Initial path.


  :name: Name of the monitor.


  :to_path: Final path.











20169
^^^^^


:Message: File &#34;%(path)s&#34; was created in monitor %(name)s.
:Groups: file-operation, process, informational, monitor
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :name: Name of the monitor.











20170
^^^^^


:Message: Folder &#34;%(path)s&#34; was created in monitor %(name)s.
:Groups: file-operation, process, informational, monitor
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :name: Name of the monitor.











20171
^^^^^


:Message: File &#34;%(path)s&#34; was deleted in monitor %(name)s.
:Groups: file-operation, process, informational, monitor
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :name: Name of the monitor.











20172
^^^^^


:Message: Folder &#34;%(path)s&#34; was deleted in monitor %(name)s.
:Groups: file-operation, process, informational, monitor
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :name: Name of the monitor.











20173
^^^^^


:Message: File &#34;%(path)s&#34; has a valid digital signature.
:Groups: file-operation, process, informational
:From version: 3.5.0
:To version: None
:Description: None









20174
^^^^^


:Message: Failed to handle event %(id)s by &#34;%(name)s&#34;. %(details)s
:Groups: process, failure, failure-high
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :family: Family of the event handler that failed.


  :id: ID of the event which failed to be sent.


  :name: Name of the event handler that failed.











20175
^^^^^


:Message: File &#34;%(previous_path)s&#34; was successfully rotated as &#34;%(path)s&#34; with a size of %(size)s bytes.
:Groups: process, file-operation, success, operational
:From version: 3.12.0
:To version: None
:Description: None
:Data:
  :path: New (current) path of the rotated file.


  :previous_path: Previous path where the rotated file was located.











20176
^^^^^


:Message: File &#34;%(path)s&#34; was successfully rotated without keeping any copy of the previous content.
:Groups: process, file-operation, success, operational
:From version: 3.12.0
:To version: None
:Description: None
:Data:
  :path: Path of the rotated file.











20177
^^^^^


:Message: File &#34;%(path)s&#34; has failed digital signature validation. %(details)s
:Groups: file-operation, process, failure
:From version: 3.5.0
:To version: None
:Description: None
:Data:
  :details: Reason of the failure.


  :path: Path to the file with valid signature.











20178
^^^^^


:Message: Failed to load CRL from the CDP of &#34;%(peer_subject)s&#34;. %(details)s
:Groups: process, failure, operational
:From version: 3.12.0
:To version: None
:Description: None
:Data:
  :details: Reason of the failure.


  :path: Subject of the peer certificate for which CDP/CRL loading failed.











20179
^^^^^


:Message: File &#34;%(path)s&#34; exists in the monitor %(name)s.
:Groups: file-operation, process, informational, monitor
:From version: 3.6.0
:To version: None
:Description: None
:Data:
  :name: Name of the monitor.











20180
^^^^^


:Message: Folder &#34;%(path)s&#34; exists in the monitor %(name)s.
:Groups: file-operation, process, informational, monitor
:From version: 3.6.0
:To version: None
:Description: None
:Data:
  :name: Name of the monitor.











20181
^^^^^


:Message: Started %(product_name)s - %(product_version)s.
:Groups: process, informational, operational
:From version: 3.9.0
:To version: None
:Description: None
:Data:
  :product_name: Name of the product


  :product_version: Current version of the product.











20182
^^^^^


:Message: Account &#34;%(account_name)s&#34; logged in with permissions %(permissions)s. Files will be uploaded as: %(upload_names)s
:Groups: informational, authenticated, operational
:From version: 3.13.0
:To version: 4.0.0
:Description: None
:Data:
  :account_name: Name of the account which logged in.


  :permissions: Permissions configured for account.


  :upload_names: Format of the files as they are uploaded.











20183
^^^^^


:Message: Unexpected error occurred during log rotation. %(details)s.
:Groups: process, failure, failure-high, file-operation, operational
:From version: 3.14.0
:To version: None
:Description: None
:Data:
  :details: Reason of the failure.











20184
^^^^^


:Message: Internal Error. Failed to start %(family)s &#34;%(name)s&#34; of type &#34;%(type)s&#34;. %(details)s
:Groups: failure-critical, failure, authenticated, operational
:From version: 3.24.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component which failed to start


  :name: Name of the component which failed to start.


  :type: Type of the component which failed to start.











20185
^^^^^


:Message: Internal Error. Failed to stop %(family)s &#34;%(name)s&#34; of type %(type)s. %(details)s
:Groups: failure-critical, failure, authenticated, operational
:From version: 3.24.0
:To version: None
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.











20186
^^^^^


:Message: You are using the evaluation version. Email us at sales@proatria.com or visit https://www.sftpplus.com/pricing/ to get the full licence. %(details)s
:Groups: process, informational, operational
:From version: 3.29.0
:To version: None
:Description: Upgrading is straight-forward. Once upgraded, you can continue to use the same configuration files or start with a new setup. For technical support and other questions about the demo, please email our team at support@proatria.com.
:Data:
  :details: Additional information about the demo version status.









































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































FTP protocol
============






















































































10012
^^^^^


:Message: Successfully open file &#34;%(path)s&#34; for writing at offset %(offset)s. Path requested as &#34;%(requested_path)s.
:Groups: file-operation, ftp, authenticated, success
:From version: 2.4.0
:To version: None
:Description: None
:Data:
  :offset: Position inside the file where the read will begin.


  :path: Path as processed by the server.


  :requested_path: The path as it was requested by the client.











10013
^^^^^


:Message: Failed to open file &#34;%(path)s&#34; for writing  at offset %(offset)s. Path requested as &#34;%(requested_path)s. %(details)s
:Groups: file-operation, failure, authenticated, ftp
:From version: 2.4.0
:To version: None
:Description: None
:Data:
  :path: Path as processed by the server.


  :requested_path: The path as it was requested by the client.











10014
^^^^^


:Message: Clients are required to send a valid certificate. Maybe the client did not send a certificate or the client certificate is not valid. %(details)s
:Groups: failure, session, ftp
:From version: 1.6.0
:To version: None
:Description: None









10015
^^^^^


:Message: Ran out of passive ports from range %(port_range)s.
:Groups: ftp, failure-specific, authenticated, operational, failure, failure-high
:From version: 1.8.1
:To version: None
:Description: None
:Data:
  :port_range: Range from which passive ports are allocated.











10016
^^^^^


:Message: Internal error. Failed to process the FTP command &#34;%(line)s&#34;. %(details)s
:Groups: failure-critical, ftp, authenticated, operational, failure, failure-specific
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :line: Full line of FTP command that generated the error.











10017
^^^^^


:Message: No authentication method enabled. Users will not be able to authenticate against the FTP/FTPS service. Please enable one of the supported authentication methods.
:Groups: failure, session, failure-high, failure-specific, ftp
:From version: 1.7.4
:To version: None
:Description: None









10018
^^^^^


:Message: Password based authentication must be enabled when FTPS is not enabled.
:Groups: ftp, failure-specific, operational, failure, session, failure-high
:From version: 1.7.4
:To version: None
:Description: None









10019
^^^^^


:Message: FTP command &#34;%(command)s&#34; not implemented by the service.
:Groups: failure, failure-specific, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :command: FTP command received.











10020
^^^^^


:Message: Extended Passive transfer requested.
:Groups: ftp, authenticated, operational
:From version: 1.8.1
:To version: None
:Description: None









10021
^^^^^


:Message: Connection was closed before finalization of SSL handshake.
:Groups: failure, session, failure-specific, ftp
:From version: 1.6.0
:To version: None
:Description: None









10022
^^^^^


:Message: Listening on port %(port)s for the next passive request.
:Groups: ftp, authenticated, success
:From version: 1.8.1
:To version: None
:Description: This event is raised by both normal and extended passive requests.
:Data:
  :port: Port number on which passive connection was established.











10023
^^^^^


:Message: Passive data connection time out while waiting for client initialization. %(details)s
:Groups: failure, authenticated, ftp
:From version: 2.1.0
:To version: None
:Description: None









10024
^^^^^


:Message: Initializing secure command channel.
:Groups: ftp, session, informational
:From version: 1.6.0
:To version: None
:Description: None









10025
^^^^^


:Message: Processing APPE command for file &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: FTP APPE command request was received from the client.









10026
^^^^^


:Message: Invalid address &#34;%(address)s&#34; for PORT command.
:Groups: failure, failure-specific, authenticated, ftp
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :address: The requested raw address, in FTP format.











10027
^^^^^


:Message: No authentication method was enabled for this service.
:Groups: failure, session, failure-high, failure-specific, ftp
:From version: 1.7.4
:To version: None
:Description: None









10028
^^^^^


:Message: User &#34;%(username)s&#34; is required to authenticate using a SSL certificate.
:Groups: failure, session, failure-specific, ftp
:From version: 1.7.4
:To version: None
:Description: None









10029
^^^^^


:Message: Failed to authenticate as user &#34;%(username)s&#34; with X.509 certificate credentials.
:Groups: failure, session, failure-specific, ftp
:From version: 1.7.4
:To version: 4.0.0
:Description: None
:Data:
  :username: Username requesting authentication.











10030
^^^^^


:Message: Data connection closed. Protected using %(encryption)s. Received: %(received)s. Sent %(sent)s. Duration %(duration)s. %(host_address)s:%(host_port)s - %(peer_address)s:%(peer_port)s . Client certificate: %(certificate)s
:Groups: ftp, authenticated, success
:From version: 1.8.1
:To version: None
:Description: None
:Data:
  :certificate: The certificate of the remote client.


  :duration: Time in seconds for which the connection was open.


  :host_address: IP address for the local data connection.


  :host_port: Port number for the local data connection peer.


  :peer_address: IP address of the remote data connection peer.


  :peer_port: Port number of the remote data connection peer.


  :received: Size of data read from the data connection.


  :sent: Size of data wrote on the data connection.











10031
^^^^^


:Message: Data connection closed in a non clean way. Protected using %(encryption)s. Received %(received)s. Sent %(sent)s. Duration %(duration)s. %(host_address)s:%(host_port)s - %(peer_address)s:%(peer_port)s. Client certificate: %(certificate)s %(details)s
:Groups: failure, authenticated, ftp
:From version: 1.8.1
:To version: None
:Description: None
:Data:
  :certificate: The certificate of the remote client.


  :details: More details about the connection error.


  :duration: Time in seconds for which the connection was open.


  :host_address: IP address for the local data connection.


  :host_port: Port number for the local data connection peer.


  :peer_address: IP address of the remote data connection peer.


  :peer_port: Port number of the remote data connection peer.


  :received: Size of data read from the data connection.


  :sent: Size of data wrote on the data connection.











10032
^^^^^


:Message: Data connection time out after initialization. %(host_address)s:%(host_port)s - %(peer_address)s:%(peer_port)s.
:Groups: failure, session, failure-specific, ftp
:From version: 1.8.3
:To version: None
:Description: None
:Data:
  :host_address: IP address for the local data connection.


  :host_port: Port number for the local data connection peer.


  :peer_address: IP address of the remote data connection peer.


  :peer_port: Port number of the remote data connection peer.











10033
^^^^^


:Message: New FTP/FTPS client connection made.
:Groups: ftp, session, success
:From version: 1.6.0
:To version: None
:Description: None









10034
^^^^^


:Message: Command connection closed. Protected using %(encryption)s. Client connected with certificate: %(certificate)s
:Groups: ftp, authenticated, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :certificate: The certificate of the remote client.











10035
^^^^^


:Message: SSL/TLS required on the command channel.
:Groups: failure, session, failure-specific, ftp
:From version: 1.6.0
:To version: None
:Description: None









10036
^^^^^


:Message: SSL/TLS required on the data channel.
:Groups: failure, session, failure-specific, ftp
:From version: 1.6.0
:To version: None
:Description: None









10037
^^^^^


:Message: Request to change current folder to &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None









10038
^^^^^


:Message: Current folder successfully changed to &#34;%(path)s&#34;.
:Groups: file-operation, ftp, authenticated, success
:From version: 1.6.0
:To version: None
:Description: None









10039
^^^^^


:Message: Failed to change to folder &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: Details about the failure.











10040
^^^^^


:Message: Successfully open file &#34;%(path)s&#34; for appending.
:Groups: file-operation, operation-append, authenticated, success, ftp
:From version: 2.4.0
:To version: None
:Description: None









10041
^^^^^


:Message: Failed to open file &#34;%(path)s&#34; for appending. %(details)s
:Groups: file-operation, failure, authenticated, operation-append, ftp
:From version: 2.4.0
:To version: None
:Description: None









10042
^^^^^


:Message: Command connection closed due to an error. Protected using %(encryption)s. Client certificate: %(certificate)s %(details)s
:Groups: failure, failure-high, authenticated, ftp
:From version: 2.8.0
:To version: None
:Description: None
:Data:
  :certificate: The certificate of the remote client.











10043
^^^^^


:Message: Request to delete &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None









10044
^^^^^


:Message: Successfully deleted &#34;%(path)s&#34;.
:Groups: file-operation, ftp, authenticated, operation-delete, success
:From version: 1.6.0
:To version: None
:Description: None









10045
^^^^^


:Message: Failed to delete &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, operation-delete, ftp
:From version: 1.6.0
:To version: None
:Description: None









10046
^^^^^


:Message: Listing path &#34;%(path)s&#34; with wildcard &#34;%(glob)s&#34; for %(operation)s.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :operation: Type of the requested listing.











10047
^^^^^


:Message: Path &#34;%(path)s&#34; successfully listed with wildcard &#34;%(glob)s&#34; for %(operation)s.
:Groups: file-operation, ftp, authenticated, success
:From version: 1.6.0
:To version: None
:Description: None









10048
^^^^^


:Message: Failed to list path &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None









10049
^^^^^


:Message: Getting attributes for &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :attributes: List of requested attributes.











10050
^^^^^


:Message: Successfully got attributes for &#34;%(path)s&#34;.
:Groups: file-operation, ftp, authenticated, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :attributes: List of requested attributes.











10051
^^^^^


:Message: Failed to get attributes for &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :attributes: List of requested attributes.











10052
^^^^^


:Message: Creating folder &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None









10053
^^^^^


:Message: Successfully created folder &#34;%(path)s&#34;.
:Groups: file-operation, ftp, authenticated, operation-create-folder, success
:From version: 1.6.0
:To version: None
:Description: None









10054
^^^^^


:Message: Failed to create folder &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, operation-create-folder, ftp
:From version: 1.6.0
:To version: None
:Description: None









10055
^^^^^


:Message: Data connection opened. %(host_address)s:%(host_port)s - %(peer_address)s:%(peer_port)s
:Groups: ftp, authenticated, success
:From version: 3.14.0
:To version: None
:Description: None
:Data:
  :host_address: IP address for the local data connection.


  :host_port: Port number for the local data connection peer.


  :peer_address: IP address of the remote data connection peer.


  :peer_port: Port number of the remote data connection peer.











10058
^^^^^


:Message: Validating password for user &#34;%(username)s&#34;.
:Groups: ftp, session, informational
:From version: 1.6.0
:To version: 4.0.0
:Description: None
:Data:
  :username: Username requesting authentication.











10059
^^^^^


:Message: User successfully logged on &#34;%(real_path)s&#34; as &#34;%(virtual_path)s&#34;. Command protected using %(encryption)s. Client certificate: %(certificate)s
:Groups: ftp, authenticated, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :certificate: Certificate sent by the client over the command channel.


  :encryption: The cipher suite used to protect the command channel.


  :home_folder: User&#39;s home folder.


  :real_path: User&#39;s home folder system path.











10060
^^^^^


:Message: Failed to authenticate as user &#34;%(username)s&#34; with password credentials.
:Groups: failure, session, failure-specific, ftp
:From version: 1.6.0
:To version: 4.0.0
:Description: None
:Data:
  :username: Username requesting authentication.











10061
^^^^^


:Message: Passive transfer requested.
:Groups: informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None









10062
^^^^^


:Message: Active transfer requested to &#34;%(address)s:%(port)s&#34;.
:Groups: informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :address: Address on the client where server should connect for active transfer.


  :port: Port where server should connect.











10063
^^^^^


:Message: Successfully initiated active connection to destination %(address)s:%(port)s using source %(source_address)s:%(source_port)s.
:Groups: ftp, authenticated, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :address: IP address of the remote data connection peer.


  :port: Port number of the remote data connection peer.


  :source_address: Source IP address use for data connection.


  :source_port: Source TCP port used for data connection.











10064
^^^^^


:Message: Failed to initiate active connection to destination %(address)s:%(port)s using source %(source_address)s:%(source_port)s. %(details)s
:Groups: failure, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :address: IP address of the remote data connection peer.


  :port: Port number of the remote data connection peer.


  :source_address: Source IP address use for data connection.


  :source_port: Source TCP port used for data connection.











10065
^^^^^


:Message: Requesting current folder.
:Groups: ftp, authenticated, success
:From version: 1.6.0
:To version: None
:Description: None









10066
^^^^^


:Message: Closing current FTP session.
:Groups: ftp, session, success
:From version: 1.6.0
:To version: None
:Description: None









10067
^^^^^


:Message: Client initiating authentication as &#34;%(username)s&#34;. Command protected using %(encryption)s. Client certificate: %(certificate)s
:Groups: ftp, session, success
:From version: 1.6.0
:To version: 4.0.0
:Description: None
:Data:
  :certificate: Certificate sent by the client over the command channel.


  :encryption: The cipher suite used to protect the command channel.


  :username: Username requesting authentication.











10068
^^^^^


:Message: Opening file &#34;%(path)s&#34; for reading.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None









10069
^^^^^


:Message: Successfully retrieved file &#34;%(path)s&#34;.
:Groups: file-operation, ftp, authenticated, operation-read, success
:From version: 1.6.0
:To version: None
:Description: None









10070
^^^^^


:Message: Failed to retrieve file &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, operation-read, ftp
:From version: 1.6.0
:To version: None
:Description: None









10071
^^^^^


:Message: Deleting folder &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None









10072
^^^^^


:Message: Successfully deleted folder &#34;%(path)s&#34;.
:Groups: file-operation, ftp, authenticated, operation-delete, success
:From version: 1.6.0
:To version: None
:Description: None









10073
^^^^^


:Message: Failed to delete folder &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, operation-delete, ftp
:From version: 1.6.0
:To version: None
:Description: None









10074
^^^^^


:Message: Renaming &#34;%(from)s&#34; to &#34;%(to)s&#34;.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :from: Current name of the file.


  :path: Current name of the file.


  :to: The future name of the file.











10075
^^^^^


:Message: Successfully renamed &#34;%(from)s&#34; to &#34;%(to)s&#34;.
:Groups: file-operation, ftp, operation-rename, authenticated, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :from: Old name of the file.


  :path: Old name of the file.


  :to: The new name of the file.











10076
^^^^^


:Message: Failed to rename &#34;%(from)s&#34; to &#34;%(to)s&#34;. %(details)s
:Groups: file-operation, failure, operation-rename, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :from: Current name of the file.


  :path: Current name of the file.


  :to: The future name of the file.











10077
^^^^^


:Message: Processing STOR command for file &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ftp
:From version: 1.6.0
:To version: None
:Description: FTP STOR command request was received from the client.
:Data:
  :path: The path as it will be processed by the command.











10078
^^^^^


:Message: Successfully stored file &#34;%(path)s&#34;.
:Groups: file-operation, ftp, authenticated, operation-write, success
:From version: 1.6.0
:To version: None
:Description: None









10079
^^^^^


:Message: Failed to store file &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, operation-write, ftp
:From version: 1.6.0
:To version: None
:Description: None









10080
^^^^^


:Message: Unknown FTP representation type &#34;%(type)s&#34;.
:Groups: failure, failure-specific, authenticated, ftp
:From version: 2.12.0
:To version: None
:Description: None
:Data:
  :type: The value requested for the type.











10081
^^^^^


:Message: FTP representation type set to &#34;%(type)s&#34;.
:Groups: ftp, authenticated, success
:From version: 2.12.0
:To version: None
:Description: None
:Data:
  :type: The value requested for the type.











10082
^^^^^


:Message: Ignoring FTP representation type for &#34;%(type)s&#34;.
:Groups: informational, authenticated, ftp
:From version: 3.9.0
:To version: None
:Description: None
:Data:
  :type: The value requested for the type.











10083
^^^^^


:Message: Listening on port %(port)s for the next passive request.
:Groups: ftp, session, authenticated, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :port: Port number on which passive connection was established.











10084
^^^^^


:Message: Client FTP/FTPS connection time out.
:Groups: failure, session, failure-specific, ftp
:From version: 1.6.0
:To version: None
:Description: None









10085
^^^^^


:Message: Successfully cleared the command channel.
:Groups: ftp, authenticated, success
:From version: 1.7.18
:To version: None
:Description: None









10086
^^^^^


:Message: Command channel is already cleared.
:Groups: failure, failure-specific, authenticated, ftp
:From version: 1.7.18
:To version: None
:Description: None









10087
^^^^^


:Message: Server does not allow to clear the command channel.
:Groups: failure, failure-specific, authenticated, ftp
:From version: 1.7.18
:To version: None
:Description: None









10088
^^^^^


:Message: Failed to secure the command channel with the explicit AUTH. %(details)s
:Groups: failure, session, ftp
:From version: 3.47.0
:To version: None
:Description: None









10090
^^^^^


:Message: Extended address active transfer requested to protocol &#34;%(protocol)s&#34; on address &#34;%(ip)s:%(port)s&#34;.
:Groups: informational, authenticated, ftp
:From version: 1.7.18
:To version: None
:Description: None
:Data:
  :ip: Destination IP address.


  :port: Destination port.


  :protocol: Protocol name.











10091
^^^^^


:Message: New client connection denied. Too many concurrent FTP/FTPS connections.
:Groups: failure, session, failure-specific, ftp
:From version: 1.8.0
:To version: None
:Description: None









10092
^^^^^


:Message: Internal error. Failed to start FTP protocol handler. %(details)s
:Groups: failure-critical, failure, session, ftp
:From version: 1.8.3
:To version: None
:Description: An internal server error occurred while creating FTP protocol handler for new client.









10093
^^^^^


:Message: Explicit FTPS for %(service)s changed to %(state)s.
:Groups: informational, ftp, administration, operational
:From version: 2.4.0
:To version: None
:Description: Inform about changes in SSL layer for FTP protocol.
:Data:
  :service: Name of the service.


  :state: New state.











10094
^^^^^


:Message: Successfully open file &#34;%(path)s&#34; for reading at offset %(offset)s.
:Groups: file-operation, ftp, authenticated, operation-read, success
:From version: 2.4.0
:To version: None
:Description: None
:Data:
  :offset: Position inside the file where the read will begin.











10095
^^^^^


:Message: Failed to open file &#34;%(path)s&#34; for reading at offset %(offset)s. %(details)s
:Groups: file-operation, failure, authenticated, operation-read, ftp
:From version: 2.4.0
:To version: None
:Description: None









10096
^^^^^


:Message: Setting attributes for &#34;%(path)s&#34; to &#34;%(attributes)s&#34;.
:Groups: file-operation, informational, authenticated, ftp
:From version: 2.6.0
:To version: None
:Description: None









10097
^^^^^


:Message: Successfully set attributes for &#34;%(path)s&#34; to &#34;%(attributes)s&#34;.
:Groups: file-operation, ftp, authenticated, success
:From version: 2.6.0
:To version: None
:Description: None









10098
^^^^^


:Message: Failed to set attributes for &#34;%(path)s&#34; to &#34;%(attributes)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ftp
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











10102
^^^^^


:Message: Connected to the FTP/FTPS server.
:Groups: ftp, session, informational, client-side
:From version: 3.2.0
:To version: None
:Description: None









10103
^^^^^


:Message: Connection to FTP/FTPS server was lost. Protected using: %(encryption)s. Server certificate: %(certificate)s. Reason: %(reason)s
:Groups: ftp, session, informational, client-side
:From version: 3.2.0
:To version: None
:Description: None
:Data:
  :certificate: Certificate sent by the server over the command channel.


  :encryption: The cipher suite used to protect the command channel.











10104
^^^^^


:Message: Failed authentication. Credentials not accepted for &#34;%(name)s&#34;. %(details)s
:Groups: ftp, session, client-side, failure, operational
:From version: 3.2.0
:To version: None
:Description: None
:Data:
  :name: Name of the location which failed at the authentication process.











10105
^^^^^


:Message: Security for the command channel cleared in &#34;%(mode)s&#34; mode.
:Groups: informational, authenticated, client-side, ftp
:From version: 3.13.0
:To version: None
:Description: None









10106
^^^^^


:Message: Connection to FTP/FTPS was authenticated. Protected using %(encryption)s. Server certificate: %(certificate)s.
:Groups: informational, authenticated, client-side, ftp
:From version: 3.2.0
:To version: None
:Description: None
:Data:
  :certificate: Certificate sent by the server over the command channel.


  :encryption: The cipher suite used to protect the command channel.























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































SSH protocol
============


























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































30004
^^^^^


:Message: Global request &#34;%(request_type)s&#34; declined.
:Groups: informational, authenticated, ssh
:From version: 3.18.0
:To version: None
:Description: None
:Data:
  :request_type: Request type that was rejected.











30005
^^^^^


:Message: SSH command %(message_id)s is not supported. %(payload)s
:Groups: failure, failure-specific, authenticated, ssh, operational
:From version: 3.1.0
:To version: None
:Description: None
:Data:
  :message_id: ID of the command as specified by the SSH Standard.


  :payload: The data received together with the SSH command.











30006
^^^^^


:Message: Internal error. Failed to process the SSH command %(message_id)s - %(payload)s. %(details)s
:Groups: failure-critical, failure, session, ssh, operational
:From version: 3.1.0
:To version: None
:Description: None
:Data:
  :message_id: ID of the command as specified by the SSH Standard.


  :payload: The data received together with the SSH command.











30007
^^^^^


:Message: Authentication method &#34;%(method)s&#34; is not supported.
:Groups: failure, session, failure-specific, ssh
:From version: 3.1.0
:To version: None
:Description: None
:Data:
  :method: Name of the requested SSH authentication method.











30008
^^^^^


:Message: SSH request rejected. %(details)s
:Groups: failure, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None









30009
^^^^^


:Message: Start processing &#39;%(command)s&#39; command.
:Groups: informational, authenticated, ssh, operational
:From version: 3.45.0
:To version: None
:Description: None
:Data:
  :command: Name of the requested command.











30010
^^^^^


:Message: End processing &#39;%(command)s&#39; command.
:Groups: informational, authenticated, ssh, operational
:From version: 3.45.0
:To version: None
:Description: None
:Data:
  :command: Name of the requested command.











30011
^^^^^


:Message: Subsystem %(service_name)s successfully started in &#34;%(real_path)s&#34; as &#34;%(virtual_path)s&#34;. Protected using host-key:%(host_key)s key-exchange:%(key_exchange)s in-hmac:%(in_hmac)s in-cipher:%(in_cipher)s out-hmac:%(out_hmac)s out-cipher:%(out_cipher)s in-compression:%(in_compression)s out-compression:%(out_compression)s
:Groups: authenticated, ssh, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :in-compression: Compression used to receive data.


  :in_cipher: Cipher used for received data.


  :in_hmac: Hash-based message authentication code for received data.


  :out-compression: Compression used to send data.


  :out_cipher: Cipher used for sent data.


  :out_hmac: Hash-based message authentication code for sent data.


  :real_path: Path on the server&#39;s filesystem where SFTP session was initiated.


  :service_name: Name of the SSH subsystem used. Ex SFTP or SCP.


  :virtual_path: Path of the folder in the virtual filesystem where sessions was initiated.











30012
^^^^^


:Message: SFTP subsystem closed. Using SFTP version %(client_version)s.
:Groups: authenticated, ssh, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :client_version: SFTP version used for the connection.











30013
^^^^^


:Message: Could not load prime numbers database from &#34;%(path)s&#34;. %(details)s
:Groups: process, failure, failure-high, ssh, operational
:From version: 1.6.0
:To version: 3.40.0
:Description: None









30014
^^^^^


:Message: New SSH connection made.
:Groups: session, ssh, success
:From version: 1.6.0
:To version: None
:Description: None









30015
^^^^^


:Message: SSH connection lost from &#34;%(client_version)s&#34;. Protected using host-key:%(host_key)s key-exchange:%(key_exchange)s in-hmac:%(in_hmac)s in-cipher:%(in_cipher)s out-hmac:%(out_hmac)s out-cipher:%(out_cipher)s in-compression:%(in_compression)s out-compression:%(out_compression)s
:Groups: informational, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :client_version: SSH version advertised by the client.


  :host_key: Host key algorithm in used to identify the server-side.


  :in-compression: Compression used to receive data.


  :in_cipher: Cipher used for received data.


  :in_hmac: Hash-based message authentication code for received data.


  :key_exchange: Key exchange algorithm used by the connection.


  :out-compression: Compression used to send data.


  :out_cipher: Cipher used for sent data.


  :out_hmac: Hash-based message authentication code for sent data.











30016
^^^^^


:Message: Internal error. Failed to process the SFTP command. %(details)s
:Groups: failure-critical, failure, authenticated, ssh, operational
:From version: 1.6.0
:To version: None
:Description: None









30017
^^^^^


:Message: File &#34;%(path)s&#34; successfully closed after opening for %(mode)s. Read %(total_read)s bytes at %(read_speed)s bytes/second and wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: file-operation, authenticated, ssh, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :mode: Mode in which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











30018
^^^^^


:Message: Internal error. Failure in the SSH userauth service for &#34;%(username)s&#34;. %(details)s
:Groups: failure-critical, failure, session, ssh
:From version: 1.8.1
:To version: None
:Description: None
:Data:
  :username: Name of the account.











30019
^^^^^


:Message: Listing folder &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None









30020
^^^^^


:Message: Successfully listed folder &#34;%(path)s&#34;.
:Groups: file-operation, authenticated, ssh, success
:From version: 1.6.0
:To version: None
:Description: None









30021
^^^^^


:Message: Failed to list folder &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30022
^^^^^


:Message: Deleting &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None









30023
^^^^^


:Message: Successfully deleted &#34;%(path)s&#34;.
:Groups: file-operation, authenticated, operation-delete, success, ssh
:From version: 1.6.0
:To version: None
:Description: None









30024
^^^^^


:Message: Failed to delete &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, operation-delete, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30025
^^^^^


:Message: Renaming &#34;%(from)s&#34; to &#34;%(to)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :from: Current file/folder path.


  :path: Future file/folder path.


  :to: Future file/folder path.











30026
^^^^^


:Message: Successfully rename &#34;%(from)s&#34; to &#34;%(to)s&#34;.
:Groups: file-operation, operation-rename, authenticated, ssh, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :from: Old file/folder path.


  :path: New file/folder path.


  :to: New file/folder path.











30027
^^^^^


:Message: Failed to rename &#34;%(from)s&#34; to &#34;%(to)s&#34;. %(details)s
:Groups: file-operation, failure, operation-rename, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.


  :from: Current file/folder path.


  :path: New file/folder path.


  :to: Future file/folder path.











30028
^^^^^


:Message: Creating folder &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None









30029
^^^^^


:Message: Successfully created folder &#34;%(path)s&#34;.
:Groups: file-operation, authenticated, operation-create-folder, success, ssh
:From version: 1.6.0
:To version: None
:Description: None









30030
^^^^^


:Message: Failed to create folder &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh, operation-create-folder
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30031
^^^^^


:Message: Deleting folder &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None









30032
^^^^^


:Message: Successfully delete folder &#34;%(path)s&#34;.
:Groups: file-operation, authenticated, operation-delete, success, ssh
:From version: 1.6.0
:To version: None
:Description: None









30033
^^^^^


:Message: Failed to delete folder &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, operation-delete, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30034
^^^^^


:Message: Getting attributes for &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None









30035
^^^^^


:Message: Successfully got attributes for &#34;%(path)s&#34;.
:Groups: file-operation, authenticated, ssh, success
:From version: 1.6.0
:To version: None
:Description: None









30036
^^^^^


:Message: Failed to get attributes for &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30037
^^^^^


:Message: Setting attributes for &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None









30038
^^^^^


:Message: Successfully set attributes for &#34;%(path)s&#34;.
:Groups: file-operation, authenticated, ssh, success
:From version: 1.6.0
:To version: None
:Description: None









30039
^^^^^


:Message: Failed to set attributes for &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30040
^^^^^


:Message: Transfer failure. File &#34;%(path)s&#34; was closed after opening for %(mode)s. Read %(total_read)s bytes at %(read_speed)s bytes/second and wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: file-operation, failure, failure-specific, authenticated, ssh
:From version: 3.40.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :mode: Mode in which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











30041
^^^^^


:Message: File &#34;%(path)s&#34; failed to be fully read. Read %(total_read)s bytes at %(read_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, operation-read, failure, ssh, file-operation, failure-specific
:From version: 3.40.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,











30042
^^^^^


:Message: File &#34;%(path)s&#34; failed to be fully written. Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, operation-write, failure, ssh, file-operation, failure-specific
:From version: 3.40.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











30043
^^^^^


:Message: Successfully opened &#34;%(path)s&#34; in &#34;%(mode)s&#34; mode, requested as &#34;%(requested_path)s&#34;.
:Groups: file-operation, authenticated, ssh, success
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :mode: Open mode requested for the file


  :path: Virtual path of the opened file.


  :requested_path: The path as it was requested by the client.











30044
^^^^^


:Message: Failed to open &#34;%(path)s&#34; in &#34;%(mode)s&#34; mode, requested as &#34;%(requested_path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :mode: Open mode requested for the file


  :requested_path: The path as it was requested by the client.











30045
^^^^^


:Message: Failed to read from file &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30046
^^^^^


:Message: Failed to write to file &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30047
^^^^^


:Message: Failed to close file &#34;%(path)s&#34; after opening for %(mode)s. Read %(total_read)s at %(read_speed)s and wrote %(total_write)s at %(write_speed)s in %(duration)s seconds. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 1.6.0
:To version: None
:Description: None
:Data:
  :mode: Mode in which the file was opened.











30048
^^^^^


:Message: Could not read DSA/RSA key at &#34;%(path)s&#34;. %(details)s
:Groups: process, failure, failure-high, ssh, operational
:From version: 1.6.0
:To version: 3.40.0
:Description: None









30049
^^^^^


:Message: Could not read SSH key received from client. %(details)s
:Groups: failure, session, ssh, operational
:From version: 2.10.0
:To version: None
:Description: None









30050
^^^^^


:Message: Client SSH connection time out.
:Groups: failure, failure-specific, authenticated, ssh
:From version: 1.8.0
:To version: None
:Description: None









30051
^^^^^


:Message: New client connection denied. Too many concurrent SSH connections.
:Groups: failure, session, failure-specific, ssh
:From version: 1.8.0
:To version: None
:Description: None









30052
^^^^^


:Message: Failed to load SSH key from &#34;%(path)s&#34;. %(details)s
:Groups: process, failure, failure-high, ssh, operational
:From version: 1.8.0
:To version: 3.40.0
:Description: None









30053
^^^^^


:Message: Reading link for &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 2.4.0
:To version: None
:Description: None









30054
^^^^^


:Message: Successfully read link for &#34;%(path)s&#34;.
:Groups: file-operation, authenticated, ssh, success
:From version: 2.4.0
:To version: None
:Description: None









30055
^^^^^


:Message: Failed to read link for &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 2.4.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30056
^^^^^


:Message: Making link for &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 2.4.0
:To version: None
:Description: None









30057
^^^^^


:Message: Successfully made link for &#34;%(path)s&#34;.
:Groups: file-operation, authenticated, ssh, success
:From version: 2.4.0
:To version: None
:Description: None









30058
^^^^^


:Message: Failed to make link for &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 2.4.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30059
^^^^^


:Message: Extended requests are not supported by the SFTP protocol.
:Groups: failure, failure-specific, authenticated, ssh
:From version: 2.4.0
:To version: None
:Description: None









30060
^^^^^


:Message: Canonical file name requested for &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 2.4.0
:To version: None
:Description: None









30061
^^^^^


:Message: Failed to get attributes for opened file &#34;%(path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, ssh
:From version: 2.4.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.











30062
^^^^^


:Message: Setting attributes on opened files not implemented for &#34;%(path)s&#34;.
:Groups: file-operation, failure, failure-specific, authenticated, ssh
:From version: 2.4.0
:To version: None
:Description: None









30063
^^^^^


:Message: SCP process successfully started in &#34;%(real_path)s&#34; as &#34;%(virtual_path)s&#34;.
:Groups: informational, authenticated, ssh
:From version: 2.5.0
:To version: 3.21.0
:Description: None
:Data:
  :real_path: Path on the server&#39;s filesystem where SCP process was initiated.


  :virtual_path: Path of the folder in the virtual filesystem where sessions was initiated.











30064
^^^^^


:Message: SCP session closed.
:Groups: informational, authenticated, ssh
:From version: 2.5.0
:To version: None
:Description: None









30065
^^^^^


:Message: Internal error. Failed to process the SCP request. %(details)s
:Groups: failure-critical, failure, authenticated, ssh, operational
:From version: 2.5.0
:To version: None
:Description: None









30066
^^^^^


:Message: Failed to process &#39;%(command)s&#39; command request. %(details)s
:Groups: failure-critical, failure, authenticated, ssh, operational
:From version: 3.45.0
:To version: None
:Description: None
:Data:
  :command: Name of the requested command.











30067
^^^^^


:Message: File &#34;%(path)s&#34; successfully read. Read %(total_read)s bytes at %(read_speed)s bytes/second in %(duration)s seconds.
:Groups: file-operation, authenticated, operation-read, success, ssh
:From version: 3.7.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :mode: Mode in which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,











30068
^^^^^


:Message: File &#34;%(path)s&#34; successfully written. Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: file-operation, authenticated, operation-write, success, ssh
:From version: 3.7.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :mode: Mode in which the file was opened.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











30069
^^^^^


:Message: Authentication requested for username with invalid encoding &#34;%(username)s&#34;.
:Groups: failure, session, ssh, failure-specific
:From version: 3.20.0
:To version: None
:Description: None
:Data:
  :username: Raw value of the requested username.











30070
^^^^^


:Message: Authentication requested with a password with invalid encoding.
:Groups: failure, session, failure-specific, ssh
:From version: 3.20.0
:To version: None
:Description: None









30071
^^^^^


:Message: Invalid remote SSH server identity for location %(name)s. Configured &#34;%(expected_fingerprint)s&#34;, remote sent &#34;%(actual_fingerprint)s&#34;. 
:Groups: failure-critical, client-side, failure, session, ssh, failure-specific
:From version: 2.9.0
:To version: None
:Description: None
:Data:
  :actual_fingerprint: Fingerprint received from the remote server.


  :expected_fingerprint: Configured fingerprint.


  :name: Name of the location associated with this event











30072
^^^^^


:Message: Location %(name)s connected to the SSH server.
:Groups: client-side, session, informational, ssh
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the location associated with this event











30073
^^^^^


:Message: Connection to SSH server was lost for location %(name)s. Protected using host-key:%(host_key)s key-exchange:%(key_exchange)s in-hmac:%(in_hmac)s in-cipher:%(in_cipher)s out-hmac:%(out_hmac)s out-cipher:%(out_cipher)s
:Groups: client-side, session, informational, ssh
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :host_key: Host key algorithm in used to identify the server-side.


  :in_cipher: Cipher used for received data.


  :in_hmac: Hash-based message authentication code for received data.


  :key_exchange: Key exchange algorithm used by the connection.


  :name: Name of the location associated with this event


  :out_cipher: Cipher used for sent data.


  :out_hmac: Hash-based message authentication code for sent data.











30074
^^^^^


:Message: Ignoring setting attributes for opened file &#34;%(path)s&#34;.
:Groups: file-operation, failure, failure-specific, authenticated, ssh
:From version: 3.51.0
:To version: None
:Description: None









30075
^^^^^


:Message: Failed to read private SSH key &#34;%(name)s&#34; from %(path)s. %(details)s
:Groups: process, failure, client-side, ssh, operational
:From version: 3.0.0
:To version: 3.40.0
:Description: None
:Data:
  :name: Name of the location which failed.


  :path: Path to SSH private key which failed to load.











30076
^^^^^


:Message: Client SFTP subsystem initialized for location %(name)s.
:Groups: informational, authenticated, ssh, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the location associated with this event











30077
^^^^^


:Message: Client SFTP subsystem closed for location %(name)s.
:Groups: informational, authenticated, ssh, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the location associated with this event











30078
^^^^^


:Message: Failure while authenticating the SFTP client for &#34;%(name)s&#34; using methods: %(methods)s. %(details)s
:Groups: client-side, operational, failure, session, ssh, failure-high
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :methods: List with all methods tried to authenticate.


  :name: Name of the location which failed at the authentication process.











30079
^^^^^


:Message: SSH Banner received: %(message)s
:Groups: client-side, session, informational, ssh
:From version: 3.29.0
:To version: None
:Description: None
:Data:
  :message: The message sent by the server.











30080
^^^^^


:Message: SSH rekey successfully completed.
:Groups: client-side, session, informational, ssh
:From version: 3.31.0
:To version: None
:Description: None









30081
^^^^^


:Message: Successfully got attributes for opened file &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, ssh
:From version: 3.51.0
:To version: None
:Description: None



















































































































































































































































































































































































































































































































































































































































































































































































































































































































HTTP/HTTPS protocol
===================














































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































40000
^^^^^


:Message: Unauthorized request for &#34;%(uri)s&#34;. %(details)s
:Groups: failure, session, http
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :uri: URI for which the request was made.











40001
^^^^^


:Message: Static web resource could not be found: %(uri)s
:Groups: failure, session, http, failure-specific
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :uri: URI associated with this request.











40002
^^^^^


:Message: Failed to get attributes for &#34;%(path)s&#34;. Details: %(details)s
:Groups: file-operation, failure, authenticated, http
:From version: 2.3.0
:To version: None
:Description: None









40003
^^^^^


:Message: Internal error. Failed to retrieve &#34;%(uri)s&#34;. %(title)s. %(details)s
:Groups: failure-critical, failure, session, http
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :title: Name of the error.


  :uri: URI associated with this request.











40004
^^^^^


:Message: Opened file for reading at &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, http
:From version: 1.8.0
:To version: None
:Description: None









40005
^^^^^


:Message: HEAD request done for file at &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, http
:From version: 1.8.0
:To version: None
:Description: None









40006
^^^^^


:Message: Listing folder at &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, http
:From version: 1.8.0
:To version: None
:Description: None









40007
^^^^^


:Message: HTTP/HTTPS file access successfully started in &#34;%(real_path)s&#34; as &#34;%(virtual_path)s&#34;.
:Groups: informational, authenticated, http
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :real_path: Path on the server&#39;s filesystem where session was initiated.


  :virtual_path: Path of the folder in the virtual filesystem where sessions was initiated.











40008
^^^^^


:Message: Redirecting from &#34;%(uri)s&#34; to &#34;%(redirect_uri)s&#34;.
:Groups: informational, authenticated, http
:From version: 1.8.0
:To version: None
:Description: None
:Data:
  :redirect_uri: New URI where request will redirect.


  :uri: Initial URI request.











40009
^^^^^


:Message: Client HTTPS did not sent a valid certificate. &#34;%(details)s&#34;.
:Groups: failure, session, http
:From version: 1.8.0
:To version: None
:Description: None









40010
^^^^^


:Message: New folder created at &#34;%(path)s&#34;.
:Groups: file-operation, http, authenticated, success
:From version: 2.3.0
:To version: None
:Description: None









40011
^^^^^


:Message: Failed to create new folder &#34;%(path)s&#34;. Details: %(details)s
:Groups: file-operation, failure, authenticated, http
:From version: 2.3.0
:To version: None
:Description: None









40012
^^^^^


:Message: Successfully removed file at &#34;%(path)s&#34;.
:Groups: file-operation, http, authenticated, success
:From version: 2.3.0
:To version: None
:Description: None









40013
^^^^^


:Message: Failed to remove file at &#34;%(path)s&#34;. &#34;%(details)s&#34;
:Groups: file-operation, failure, authenticated, http
:From version: 2.3.0
:To version: None
:Description: None









40014
^^^^^


:Message: Failed to list folder content at &#34;%(path)s&#34;. Details: %(details)s
:Groups: file-operation, failure, authenticated, http
:From version: 2.3.0
:To version: None
:Description: None
:Data:
  :details: More details about the error.











40015
^^^^^


:Message: Failed to open file for writing at &#34;%(path)s&#34;. Details: %(details)s
:Groups: file-operation, failure, authenticated, http
:From version: 2.3.0
:To version: 3.31.0
:Description: None
:Data:
  :details: More details about the error.











40016
^^^^^


:Message: Failed while storing uploaded file at &#34;%(path)s&#34;. Details: %(details)s
:Groups: file-operation, failure, authenticated, http
:From version: 2.3.0
:To version: 3.31.0
:Description: None
:Data:
  :details: More details about the error.











40017
^^^^^


:Message: Successfully uploaded file at &#34;%(path)s&#34;. Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: file-operation, http, authenticated, success
:From version: 2.3.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











40018
^^^^^


:Message: Forcing client disconnection at &#34;%(uri)s&#34; after receiving %(size)s bytes in body. Response: %(code)s %(details)s
:Groups: failure, session, http, failure-high
:From version: 2.3.0
:To version: None
:Description: None
:Data:
  :code: HTTP disconnection response code.


  :message: HTTP response message.


  :size: Received bytes for body content


  :uri: URI for which client was disconnected.











40019
^^^^^


:Message: Bad request for &#34;%(path)s&#34;. Requested as &#34;%(uri)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, http
:From version: 2.3.0
:To version: None
:Description: None
:Data:
  :details: More details about the failure.


  :uri: Full URI of the bad request.











40020
^^^^^


:Message: Internal error. Failed initializing request handler. %(details)s
:Groups: failure-critical, failure, session, http
:From version: 2.4.0
:To version: None
:Description: None
:Data:
  :details: Details about the error.











40021
^^^^^


:Message: File opened for writing at &#34;%(path)s&#34;. Path requested as &#34;%(requested_path)s.
:Groups: file-operation, informational, authenticated, http
:From version: 2.4.0
:To version: None
:Description: None









40022
^^^^^


:Message: Failed to upload file at &#34;%(path)s&#34;. Path requested as &#34;%(requested_path)s. Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds. %(details)s
:Groups: file-operation, failure, authenticated, http
:From version: 2.4.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











40023
^^^^^


:Message: Internal error. Failed processing the request for &#34;%(uri)s&#34;. %(details)s
:Groups: failure-critical, failure, session, http
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :uri: URI associated with this request.











40024
^^^^^


:Message: Internal error. Failed processing the headers for &#34;%(uri)s&#34;. %(details)s
:Groups: failure-critical, failure, session, http
:From version: 2.11.0
:To version: None
:Description: None
:Data:
  :uri: URI associated with this request.











40025
^^^^^


:Message: Internal error. Failed executing JSON API &#34;%(uri)s&#34;. %(details)s
:Groups: failure-critical, failure, session, http
:From version: 2.11.0
:To version: 3.32.0
:Description: Replaced by event ID 40003.
:Data:
  :uri: URI associated with this request.











40026
^^^^^


:Message: Successfully removed folder at &#34;%(path)s&#34;.
:Groups: file-operation, http, authenticated, success
:From version: 2.11.0
:To version: None
:Description: None









40027
^^^^^


:Message: Failed to remove folder at &#34;%(path)s&#34;. &#34;%(details)s&#34;
:Groups: file-operation, failure, authenticated, http
:From version: 2.11.0
:To version: None
:Description: None









40028
^^^^^


:Message: Failed to decode name for file &#34;%(name)s&#34; in &#34;%(operation)s&#34; operation. The request for this file was ignored.
:Groups: failure, failure-specific, authenticated, http
:From version: 2.12.0
:To version: None
:Description: None
:Data:
  :name: Name of the file which failed


  :operation: Name of the file transfer operation











40029
^^^^^


:Message: HTTP/HTTPS connection closed on the server-side due to a failure. &#34;%(details)s&#34;
:Groups: failure, session, http
:From version: 3.6.0
:To version: None
:Description: None









40030
^^^^^


:Message: Folder at &#34;%(path)s&#34; already exist for create request.
:Groups: file-operation, informational, authenticated, http
:From version: 3.0.0
:To version: None
:Description: None









40031
^^^^^


:Message: Client session was re-authenticated since previous credentials were no longer accepted by the server.
:Groups: informational, authenticated, http, client-side
:From version: 3.27.0
:To version: None
:Description: None









40032
^^^^^


:Message: HTTP/HTTPS connection closed on the client-side to %(hostname)s. Session fully established: %(session_established)s
:Groups: http, session, informational, client-side
:From version: 3.27.0
:To version: None
:Description: None
:Data:
  :hostname: Name use to initiate the connection. This can be IP address or FQDN


  :session_established: Whether the connection was established, or the connection was lost during setup.











40033
^^^^^


:Message: HTTP/HTTPS connection created on the client-side as %(hostname)s. Server certificate: %(certificate)s. Used encryption: %(encryption)s.
:Groups: http, session, informational, client-side
:From version: 3.27.0
:To version: None
:Description: None
:Data:
  :certificate: Details for the server&#39;s certificate.


  :encryption: Method and cipher used by this connection.


  :hostname: Name use to initiate the connection. This can be IP address or FQDN.











40034
^^^^^


:Message: Successfully listed folder at &#34;%(path)s&#34;.
:Groups: file-operation, http, authenticated, success
:From version: 3.28.0
:To version: None
:Description: None









40035
^^^^^


:Message: Failed to open file for reading at &#34;%(path)s&#34;. Details: %(details)s
:Groups: file-operation, failure, authenticated, http
:From version: 3.28.0
:To version: None
:Description: None









40036
^^^^^


:Message: HEAD requested for folder at &#34;%(path)s&#34;.
:Groups: file-operation, informational, authenticated, http
:From version: 3.29.0
:To version: None
:Description: None









40037
^^^^^


:Message: Closing current HTTP session.
:Groups: process, http, success
:From version: 3.37.0
:To version: None
:Description: None









40038
^^^^^


:Message: Public access is forbidden. %(details)s
:Groups: failure, session, http
:From version: 3.40.0
:To version: None
:Description: None









40039
^^^^^


:Message: Successfully downloaded file from &#34;%(path)s&#34;. Read %(total_read)s bytes at %(read_speed)s bytes/second in %(duration)s seconds.
:Groups: file-operation, informational, authenticated, http
:From version: 3.46.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,











40040
^^^^^


:Message: Failed to download file from &#34;%(path)s&#34;. Read %(total_read)s bytes at %(read_speed)s bytes/second in %(duration)s seconds. %(details)s
:Groups: file-operation, failure, authenticated, http
:From version: 3.46.0
:To version: None
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,











40041
^^^^^


:Message: Failed to download multiple files as ZIP archive. %(details)s
:Groups: failure, authenticated, http
:From version: 3.46.0
:To version: None
:Description: None









40042
^^^^^


:Message: HTTP request failed for %(url)s as part of a redundant request. Will retry after %(retry_interval)s seconds. %(details)s
:Groups: process, failure, failure-high, operational
:From version: 3.51.0
:To version: None
:Description: None
:Data:
  :url: URL which failed.



















































































































































































































































































































































































































































































































































































































































Management and Local Manager Events
===================================
















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































50000
^^^^^


:Message: Request does not contains an session id.
:Groups: failure, session, failure-specific, local-manager
:From version: 2.1.0
:To version: None
:Description: None









50001
^^^^^


:Message: Authentication failed.
:Groups: failure, session, failure-specific, local-manager
:From version: 2.1.0
:To version: None
:Description: None









50002
^^^^^


:Message: Configuration read from local manager.
:Groups: administration, local-manager, success
:From version: 2.1.0
:To version: None
:Description: None









50003
^^^^^


:Message: Unrecognized change requested from local manager: &#34;%(details)s&#34;.
:Groups: failure, failure-high, administration, local-manager
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :details: Details about the error.











50004
^^^^^


:Message: Internal JSON-RPC error: %(details)s
:Groups: failure-critical, failure, administration, local-manager, operational
:From version: 2.1.0
:To version: None
:Description: None









50005
^^^^^


:Message: All requested changes successfully applied. Changes: %(changes)s. Results: %(results)s.
:Groups: administration, local-manager, success, operational
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :changes: List of changes applied.


  :results: List of results after applying changes.











50006
^^^^^


:Message: Not all requested changes successfully applied. Changes: %(changes)s. Results: %(results)s.
:Groups: failure, failure-specific, administration, local-manager, operational
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :changes: List of changes applied.


  :results: List of results after applying changes.











50007
^^^^^


:Message: %(kind)s administrator &#34;%(name)s&#34; logged in local manager as role &#34;%(role)s&#34;.
:Groups: administration, local-manager, success
:From version: 2.1.0
:To version: 4.0.0
:Description: None
:Data:
  :kind: The type of the authenticated administrator.


  :name: Name of administrator that was authenticated.


  :role: Name of the role associated with this administrator.











50008
^^^^^


:Message: Local manager authentication failed for &#34;%(username)s&#34;.
:Groups: failure, failure-specific, administration, local-manager
:From version: 2.1.0
:To version: 3.37.0
:Description: None
:Data:
  :username: Name of administrator for which authentication failed.











50009
^^^^^


:Message: Local manager authentication failed for &#34;%(name)s&#34;. Administrator is not a member of one of the enabled administrations groups.
:Groups: failure, failure-specific, administration, local-manager
:From version: 2.1.0
:To version: 3.37.0
:Description: None
:Data:
  :name: Name of administrator for which authentication failed.











50010
^^^^^


:Message: Administrator logged out from local manager.
:Groups: informational, administration, local-manager
:From version: 2.1.0
:To version: None
:Description: None









50011
^^^^^


:Message: Bad format for requested changes: %(changes)s. %(details)s
:Groups: failure, failure-high, administration, local-manager
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :changes: Changes are requested by local-manager.











50012
^^^^^


:Message: Failed to apply requested change: &#34;%(details)s&#34;.
:Groups: failure, administration, local-manager
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :details: Details about the error.











50013
^^^^^


:Message: Failed to process action for runnable with UUID %(uuid)s: %(details)s
:Groups: failure, session, local-manager
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :details: More details about the error.


  :uuid: UUID of the requested runnable.











50015
^^^^^


:Message: Internal error. Failed processing the action for runnable with UUID: %(uuid)s. %(details)s
:Groups: failure-critical, failure, session, local-manager
:From version: 2.1.0
:To version: None
:Description: None
:Data:
  :uuid: UUID of the requested runnable.











50019
^^^^^


:Message: Failed to get configuration for database &#34;%(database_uuid)s&#34;. Source: %(source)s. %(details)s
:Groups: failure, failure-high, authenticated, local-manager, operational
:From version: 2.6.0
:To version: None
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :details: Error details.


  :source: Data source name











50020
^^^^^


:Message: Failed to get %(source)s data since database &#34;%(database_uuid)s&#34; is not started.
:Groups: informational, authenticated, local-manager, operational
:From version: 2.6.0
:To version: 4.0.0
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :source: Data source name











50021
^^^^^


:Message: Failed to get data. Unknown source: &#34;%(source)s&#34;.
:Groups: informational, authenticated, local-manager, operational
:From version: 2.6.0
:To version: None
:Description: None.
:Data:
  :source: Data source name.











50022
^^^^^


:Message: Failed to get %(source)s database configuration for: &#34;%(database_uuid)s&#34;.
:Groups: informational, authenticated, local-manager, operational
:From version: 2.6.0
:To version: None
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :source: Data source name











50023
^^^^^


:Message: Failed to process uploaded SSH key. %(details)s
:Groups: failure, failure-high, authenticated, local-manager, operational
:From version: 2.9.0
:To version: None
:Description: None









50024
^^^^^


:Message: Failed to generate SSH key or SSL key/csr. %(details)s
:Groups: failure, failure-high, authenticated, local-manager, operational
:From version: 2.12.0
:To version: None
:Description: None









50025
^^^^^


:Message: Internal error. Failed processing database entries. %(details)s
:Groups: failure, authenticated, local-manager, operational
:From version: 3.0.0
:To version: None
:Description: None









50026
^^^^^


:Message: Successfully generated CSV logs from %(database_uuid)s.
:Groups: authenticated, local-manager, success, operational
:From version: 3.1.0
:To version: None
:Description: None
:Data:
  :database_uuid: UUID of the database.











50027
^^^^^


:Message: Error occurred while generating CSV logs from %(database_uuid)s. %(details)s
:Groups: failure, authenticated, local-manager, operational
:From version: 3.1.0
:To version: None
:Description: None
:Data:
  :database_uuid: UUID of the database.



































































































































































































































































































































































































































































































Transfer and client-side functionality
======================================
































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































60000
^^^^^


:Message: File &#34;%(path)s&#34; was modified in monitored path.
:Groups: process, client-side, location-operation, informational
:From version: 2.6.0
:To version: None
:Description: None.









60001
^^^^^


:Message: File &#34;%(from_path)s&#34; was renamed in monitored path to &#34;%(to_path)s&#34;.
:Groups: process, client-side, location-operation, informational
:From version: 2.6.0
:To version: None
:Description: None
:Data:
  :from_path: Initial path.


  :to_path: Final path.











60002
^^^^^


:Message: Command failed: %(details)s
:Groups: failure-critical, failure, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None









60003
^^^^^


:Message: File &#34;%(path)s&#34; was created in monitored path.
:Groups: process, client-side, location-operation, informational
:From version: 2.6.0
:To version: None
:Description: None









60004
^^^^^


:Message: File &#34;%(path)s&#34; exists in the monitored path and will be transferred.
:Groups: process, client-side, location-operation, informational
:From version: 3.6.0
:To version: None
:Description: None









60005
^^^^^


:Message: Error occurred while taking a snapshot for &#34;%(path)s&#34;. %(details)s
:Groups: session, failure, location-operation, client-side
:From version: 3.19.0
:To version: None
:Description: None









60006
^^^^^


:Message: Transfer delayed for &#34;%(path)s&#34;. Will be transfered together with marker &#34;%(marker)s&#34;.
:Groups: process, client-side, location-operation, informational
:From version: 3.36.0
:To version: None
:Description: None
:Data:
  :marker: Expression used to detect the file marker.


  :path: Path to the file for which a transfer was delayed.











60007
^^^^^


:Message: Executing command &#34;%(name)s&#34; for &#34;%(path)s&#34;.
:Groups: transfer, location-operation, informational, client-side
:From version: 2.7.0
:To version: None
:Description: None
:Data:
  :destination_path: Path to destination file.


  :source_path: Path to source file.











60008
^^^^^


:Message: Command &#34;%(name)s&#34; was successful for &#34;%(path)s&#34;. Output &#34;%(output)s&#34;. Error &#34;%(error)s&#34;. Exit code &#34;%(exit_code)s&#34;.
:Groups: transfer, location-operation, client-side, success
:From version: 2.7.0
:To version: None
:Description: None
:Data:
  :destination_path: Path to destination file.


  :error: Error text produced by the command.


  :exit_code: Exit code of the command


  :output: Output text produced by the command.


  :source_path: Path to source file.











60009
^^^^^


:Message: Command &#34;%(name)s&#34; failed for &#34;%(path)s&#34;. Output &#34;%(output)s&#34;. Error &#34;%(error)s&#34;. Exit code &#34;%(exit_code)s&#34;. %(details)s
:Groups: transfer, location-operation, client-side, failure
:From version: 2.7.0
:To version: None
:Description: None
:Data:
  :destination_path: Path to destination file.


  :error: Error text produced by the command.


  :exit_code: Exit code of the command


  :output: Output text produced by the command.


  :source_path: Path to source file.











60010
^^^^^


:Message: Source and destination ready. Start %(transfer_type)s for &#34;%(path)s&#34; of %(size)s bytes.
:Groups: informational, location-operation, authenticated, client-side
:From version: 2.9.0
:To version: None
:Description: None
:Data:
  :size: Size of the source file in bytes.


  :transfer_type: Describe if this is a upload/push, download/pull or local-to-local transfer.











60011
^^^^^


:Message: Failed to transfer &#34;%(path)s&#34;. Will retry %(count)s more. Next try after %(wait)s seconds. %(details)s
:Groups: process, failure, location-operation, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :count: Number of times the transfer will be retried from now on.


  :wait: Number of seconds to wait before retrying.











60012
^^^^^


:Message: Successful %(transfer_type)s for file &#34;%(path)s&#34; as &#34;%(destination_path)s&#34; of %(size)s bytes of which %(transferred_size)s bytes were transferred in %(duration)s seconds at %(speed)s bytes/second.
:Groups: client-side, location-operation, authenticated, success
:From version: 2.9.0
:To version: None
:Description: None
:Data:
  :destination_path: Path on the destination location.











60013
^^^^^


:Message: Error occurred while %(transfer_type)s for file &#34;%(path)s&#34; of %(size)s bytes of which %(transferred_size)s bytes were transferred in %(duration)s seconds at %(speed)s bytes/second. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 2.9.0
:To version: None
:Description: None









60014
^^^^^


:Message: Failed to open source file &#34;%(path)s&#34; for reading. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 2.9.0
:To version: None
:Description: None









60015
^^^^^


:Message: Failed to open destination file &#34;%(path)s&#34; for writing. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 2.9.0
:To version: None
:Description: None









60016
^^^^^


:Message: Transfer failed at %(step_name)s after all retries. The following files failed %(failed_paths)s. The following files succeeded %(success_paths)s.
:Groups: failure, location-operation, authenticated, failure-specific, client-side
:From version: 2.9.0
:To version: None
:Description: None
:Data:
  :failed_list: List of paths which failed.


  :failed_paths: Comma separated paths which failed.


  :step_name: Name of the step at which transfer failed.


  :success_list: List of path which were successfully transferred to the destination.


  :success_paths: Comma separated paths which were successfully transferred to the destination.











60017
^^^^^


:Message: Transfer succeeded for %(paths)s.
:Groups: client-side, location-operation, authenticated, success
:From version: 2.9.0
:To version: None
:Description: None
:Data:
  :paths: Comma separated paths which were transferred to the destination.


  :success_list: List of paths which were transferred to the destination.











60018
^^^^^


:Message: Internal error. Failed executing transfer for &#34;%(path)s&#34;. %(details)s
:Groups: failure-critical, failure, location-operation, authenticated, client-side
:From version: 2.9.0
:To version: None
:Description: None









60019
^^^^^


:Message: Invalid schedule value for transfer &#34;%(name)s&#34;. %(details)s
:Groups: process, failure, client-side
:From version: 3.0.0
:To version: 3.44.0
:Description: None
:Data:
  :name: Name of the transfer with invalid configuration.











60020
^^^^^


:Message: Transfer &#34;%(name)s&#34; has scheduled action &#34;%(action)s&#34; in &#34;%(seconds)s&#34; seconds for &#34;%(date)s&#34;.
:Groups: process, client-side, location-operation, informational
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :action: Name of the scheduled action.


  :date: Date and time at which the action was scheduled.


  :name: Name of the transfer for which the action was scheduled.











60021
^^^^^


:Message: Transfer &#34;%(name)s&#34; started in &#34;%(state)s&#34; state.
:Groups: process, client-side, location-operation, informational
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the started transfer.


  :state: The name of the state in which the transfer was started.











60022
^^^^^


:Message: Transfer &#34;%(name)s&#34; is now executing the scheduled action &#34;%(action)s&#34;.
:Groups: process, client-side, location-operation, informational
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :action: Name of the scheduled action.


  :name: Name of the transfer for which the action was scheduled.











60023
^^^^^


:Message: Transfer &#34;%(name)s&#34; has detected a &#34;%(action)s&#34; action scheduled for &#34;%(expected_date)s&#34;, but its execution time has already passed. It was re-scheduled for now.
:Groups: process, failure, location-operation, client-side, failure-specific
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :action: Name of the scheduled action.


  :expected_date: Date and time at which the action was scheduled in ISO format.


  :name: Name of the transfer for which the action was scheduled.











60024
^^^^^


:Message: Keep alive call failed for location &#34;%(name)s&#34; . %(details)s
:Groups: failure, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the location for which the keep alive was called.











60025
^^^^^


:Message: Failed to archive &#34;%(path)s&#34; as &#34;%(archive_path)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :archive_path: Destination path of the archive.











60026
^^^^^


:Message: File &#34;%(path)s&#34; was successfully archived as &#34;%(archive_path)s&#34;.
:Groups: transfer, location-operation, client-side, success
:From version: 2.10.0
:To version: None
:Description: None
:Data:
  :archive_path: Destination path of the archive.











60027
^^^^^


:Message: Invalid overwrite rule configuration &#34;%(details)s&#34; for transfer &#34;%(name)s&#34;.
:Groups: failure, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the transfer with invalid configuration.











60028
^^^^^


:Message: Fail to transfer file &#34;%(path)s&#34; for &#34;%(name)s&#34;. File already exists on the destination and transfer is not configured to overwrite it.
:Groups: location-operation, failure, failure-specific, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the transfer associated with this event.











60029
^^^^^


:Message: Remote file &#34;%(path)s&#34; is going to be overwritten for transfer &#34;%(name)s&#34;.
:Groups: informational, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the transfer associated with this event.











60030
^^^^^


:Message: Remote file &#34;%(existing_path)s&#34; was renamed to &#34;%(path)s&#34; to prevent overwriting it for &#34;%(name)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :existing_path: Previous path of the existing file on the destination.


  :name: Name of the transfer associated with this event.


  :path: New path of the existing file, after rename operation.











60031
^^^^^


:Message: File &#34;%(path)s&#34; is going to be transfered as &#34;%(destination_path)s&#34; for &#34;%(name)s&#34; as a file with same name already exists on the destination.
:Groups: informational, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :destination_path: Path on the destination where file will be transferred.


  :name: Name of the transfer associated with this event.











60032
^^^^^


:Message: Start collecting files for batch transfer &#34;%(name)s&#34; with an interval of %(seconds)s seconds.
:Groups: process, client-side, informational
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the transfer.


  :seconds: Number of seconds used for batch interval.











60033
^^^^^


:Message: Added to the execute queue the %(type)s transfer for &#34;%(name)s&#34; with %(count)s files: %(files)s.
:Groups: process, client-side, informational
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :count: Number of files in the batch.


  :files: List of the scheduled files


  :name: Name of the transfer.


  :type: The type of this transfer











60034
^^^^^


:Message: Cancelled execution of batch transfer for &#34;%(name)s&#34; with %(count)s files.
:Groups: process, client-side, informational
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :count: Number of files in the batch.


  :name: Name of the transfer.











60035
^^^^^


:Message: Closed with success &#34;%(path)s&#34; on &#34;%(location)s&#34; after opening for %(mode)s.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.











60036
^^^^^


:Message: Closed with failure &#34;%(path)s&#34; on &#34;%(location)s&#34; after opening for %(mode)s. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.











60037
^^^^^


:Message: Failed to read &#34;%(path)s&#34; on &#34;%(location)s&#34; after opening for %(mode)s. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.











60038
^^^^^


:Message: Failed to write &#34;%(path)s&#34; on &#34;%(location)s&#34; after opening for %(mode)s. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.











60039
^^^^^


:Message: Started monitoring &#34;%(path)s&#34; on &#34;%(location)s&#34; (recursive %(recursive)s).
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :recursive: Flag to signal if monitoring is recursive.











60040
^^^^^


:Message: Stopped monitoring &#34;%(path)s&#34; on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60041
^^^^^


:Message: Operation to check the existence of &#34;%(path)s&#34; was successful on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60042
^^^^^


:Message: Failed to check that &#34;%(path)s&#34; exists on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60043
^^^^^


:Message: Successfully renamed &#34;%(from)s&#34; to &#34;%(to)s&#34; on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :path: The new name of the file.


  :to: The new name of the file.











60044
^^^^^


:Message: Failed to rename &#34;%(from)s&#34; to &#34;%(to)s&#34; on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :path: The new name of the file.


  :to: The new name of the file.











60045
^^^^^


:Message: Successfully delete file &#34;%(path)s&#34; on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60046
^^^^^


:Message: Failed to delete file &#34;%(path)s&#34; on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60047
^^^^^


:Message: Successfully delete directory (recursive %(recursive)s) &#34;%(path)s&#34; on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :recursive: `True` when a recursive request was made











60048
^^^^^


:Message: Failed to delete directory (recursive %(recursive)s) &#34;%(path)s&#34; on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :recursive: `True` when a recursive request was made











60049
^^^^^


:Message: Successfully created directory &#34;%(path)s&#34; on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60050
^^^^^


:Message: Failed to create directory &#34;%(path)s&#34; on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60051
^^^^^


:Message: Successfully listed directory &#34;%(path)s&#34; on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60052
^^^^^


:Message: Failed to list directory &#34;%(path)s&#34; on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60053
^^^^^


:Message: Successfully opened &#34;%(path)s&#34; for reading on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60054
^^^^^


:Message: Failed to open file &#34;%(path)s&#34; for reading on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60055
^^^^^


:Message: Successfully opened &#34;%(path)s&#34; for writing on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60056
^^^^^


:Message: Failed to open file &#34;%(path)s&#34; for writing on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60057
^^^^^


:Message: Successfully opened &#34;%(path)s&#34; for appending on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60058
^^^^^


:Message: Failed to open file &#34;%(path)s&#34; for appending on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60059
^^^^^


:Message: Successfully touched &#34;%(path)s&#34; on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60060
^^^^^


:Message: Failed to touch &#34;%(path)s&#34; on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60061
^^^^^


:Message: Successfully copied local &#34;%(path)s&#34; to local &#34;%(to)s&#34; (overwrite %(overwrite)s) on &#34;%(location)s&#34;.
:Groups: file-operation, client-side, location-operation, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :overwrite: True if copy operation was done with overwrite enabled.


  :path: Old name of the file.


  :to: The new name of the file.











60062
^^^^^


:Message: Failed to copy local &#34;%(path)s&#34; to local &#34;%(to)s&#34; on &#34;%(location)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :overwrite: True if copy operation was done with overwrite enabled.


  :path: Old name of the file.


  :to: The new name of the file.











60063
^^^^^


:Message: Sending keep alive call for location &#34;%(name)s&#34;.
:Groups: informational, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the location for which the keep alive was called.











60064
^^^^^


:Message: Executing &#34;%(condition)s&#34; commands on destination for &#34;%(name)s&#34;.
:Groups: informational, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :condition: Condition for which the commands are executed.


  :name: Name of the transfer for which the commands are executed.











60065
^^^^^


:Message: Successfully executed &#34;%(condition)s&#34; commands on destination for &#34;%(name)s&#34;.
:Groups: client-side, authenticated, success
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :condition: Condition for which the commands are executed.


  :name: Name of the transfer for which the commands are executed.











60066
^^^^^


:Message: Failed to execute &#34;%(condition)s&#34; commands on destination for &#34;%(name)s&#34;. %(details)s
:Groups: failure, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :condition: Condition for which the commands are executed.


  :name: Name of the transfer for which the commands are executed.











60067
^^^^^


:Message: Disconnecting as location &#34;%(name)s&#34; was idle for %(seconds)s seconds.
:Groups: informational, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the location associated with this event.


  :seconds: Number of seconds after which location is configured to disconnect on idle.











60068
^^^^^


:Message: Reconnecting as location &#34;%(name)s&#34; is configured to always keep the connection alive.
:Groups: informational, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :name: Name of the location associated with this event.











60069
^^^^^


:Message: Failed to close source &#34;%(path)s&#34; after failing to open destination &#34;%(destination_path)s&#34;. %(details)s
:Groups: file-operation, failure, authenticated, client-side
:From version: 3.12.0
:To version: None
:Description: None
:Data:
  :destination_path: Path of the destination file which failed to be opened.


  :source_path: Path of the source file which failed to be closed.











60070
^^^^^


:Message: Destination location is not available for transferring the source files from &#34;%(paths)s&#34;.
:Groups: failure, failure-specific, authenticated, client-side
:From version: 3.10.0
:To version: None
:Description: None
:Data:
  :paths: Comma separated list of files which were attempted to be transferred.











60071
^^^^^


:Message: Successfully got attributes for &#34;%(path)s&#34; on &#34;%(location)s&#34;.
:Groups: client-side, location-operation, authenticated, success
:From version: 3.20.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60072
^^^^^


:Message: Failed to get attributes for &#34;%(path)s&#34; on &#34;%(location)s&#34;. %(details)s
:Groups: failure, location-operation, authenticated, client-side
:From version: 3.20.0
:To version: None
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60073
^^^^^


:Message: Start executing transfer for &#34;%(name)s&#34; with %(count)s files: %(files)s.
:Groups: informational, authenticated, client-side
:From version: 3.0.0
:To version: None
:Description: None
:Data:
  :count: Number of files in the batch.


  :files: List of the scheduled files


  :name: Name of the transfer.


  :type: The type of this transfer











60074
^^^^^


:Message: Got a full snapshot for &#34;%(path)s&#34; with %(count)s directories.
:Groups: informational, authenticated, client-side
:From version: 3.48.0
:To version: None
:Description: None
:Data:
  :count: Number of directories which were monitored.


  :path: Path which was listed











60075
^^^^^


:Message: Not transferring file &#34;%(path)s&#34; in the monitored path. %(reason)s
:Groups: process, client-side, location-operation, informational
:From version: 4.0.0
:To version: None
:Description: None
:Data:
  :reason: Event which triggered the attempt to transfer this file.











60076
^^^^^


:Message: Skipping source file &#34;%(path)s&#34; as it already exist on destination.
:Groups: informational, location-operation, authenticated, client-side
:From version: 4.0.0
:To version: None
:Description: None









60077
^^^^^


:Message: Successfully removed archived file &#34;%(path)s&#34; older than %(days)s days.
:Groups: informational, location-operation, authenticated, client-side
:From version: 3.51.0
:To version: None
:Description: None










