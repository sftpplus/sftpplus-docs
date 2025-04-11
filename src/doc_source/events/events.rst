Generic and server-side common functionality
============================================

20000
^^^^^

:Message: DEBUG: %(message)s
:Groups: informational, authenticated
:From version: 3.48.0
:Description: Event emitted when "debug" is enabled. This is a debug event only. This event should not be used for managed file transfer purposes.



20001
^^^^^

:Message: Starting %(instance_name)s - %(product_version)s.
:Groups: operational, process, informational
:From version: 1.6.0
:Description: None
:Data:
  :instance_name: Name of this installation instance


  :product_version: Current version of the product.





20002
^^^^^

:Message: Shutting down %(instance_name)s - %(product_version)s.
:Groups: operational, process, informational
:From version: 1.6.0
:Description: None
:Data:
  :instance_name: Name of this installation instance


  :product_version: Current version of the product.





20003
^^^^^

:Message: Proxy connection received. Updating remote peer from %(host)s:%(port)s.
:Groups: operational, session, informational
:From version: 4.5.0
:Description: None



20004
^^^^^

:Message: Startup process failed. %(details)s %(traceback)s
:Groups: operational, process, failure, failure-critical
:From version: 3.6.0
:Description: The process failed while starting a component.



20007
^^^^^

:Message: Failed to start the service as current account. Could not drop process privileges to user "%(account)s". Make sure you are starting the process as "root" account and that user "%(account)s" exists. It is defined by the [services] account configuration options from the server configuration file. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 1.6.0
:Description: None
:Data:
  :account: Name of the account under which the server was trying to start.


  :details: Details about the failure reason.





20008
^^^^^

:Message: Failed to start the service as root. You need to explicitly configure a service account.
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 5.0.0
:Description: None



20009
^^^^^

:Message: Failed to store new Let's Encrypt certificates for "%(domains)s" at %(path)s. %(details)s
:Groups: operational, process, failure, failure-critical
:From version: 5.11.0
:Description: None
:Data:
  :domains: Comma-separated domain names for the new certificate.


  :path: Path to the directory where the key and the certificates were to be saved.





20010
^^^^^

:Message: Failed to configure the process. %(details)s %(tb)s
:Groups: operational, process, failure, failure-critical
:From version: 3.1.0
:Description: None



20013
^^^^^

:Message: Could not check the remote SFTPPlus WebAdmin at "%(url)s". %(details)s
:Groups: operational, process, failure, failure-high
:From version: 1.6.0
:Description: None
:Data:
  :details: Details about the error.


  :url: URL configured for SFTPPlus WebAdmin.





20014
^^^^^

:Message: There is no SFTPPlus Webadmin installed at %(url)s
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 1.6.0
:Description: None



20015
^^^^^

:Message: Let's Encrypt certificate for "%(domains)s" generated at"%(path)s".
:Groups: operational, process, informational
:From version: 5.11.0
:Description: None
:Data:
  :domains: Comma-separated domain names for the new certificate.


  :path: Path to the directory where the key and the certificates were saved.





20016
^^^^^

:Message: New Let's Encrypt certificate for "%(domains)s" used for service "%(service)s".
:Groups: operational, process, informational
:From version: 3.40.0
:Description: None
:Data:
  :domains: Comma-separated domain names for the new certificate.


  :service: Name of the service on which the new certificate is used.





20017
^^^^^

:Message: Failed to get a new Let's Encrypt certificate for "%(domains)s". %(details)s.
:Groups: operational, process, failure, failure-critical
:From version: 3.40.0
:Description: None
:Data:
  :domain: Comma-separated list of domains with new certificates.


  :service: Name of the service on which the new certificate is used.





20019
^^^^^

:Message: User home folder "%(path)s" is not within the root folder "%(root)s".
:Groups: operational, failure, failure-specific
:From version: 1.6.0
:Description: This is a compat error.



20020
^^^^^

:Message: Port value must be an integer.
:Groups: operational, process, failure, failure-specific
:From version: 1.6.0
:Description: None



20021
^^^^^

:Message: Failed to authenticate user "%(username)s" with "%(credentials_type)s" credentials. Possible typo in username. No authentication method was able to handle the credentials.
:Groups: operational, session, failure, failure-specific
:From version: 1.6.0
:Description: None
:Data:
  :credentials_type: Type of the credentials which were not authenticated.





20022
^^^^^

:Message: Property "%(property_name)s" for group "%(group_name)s" can not be inherited.
:Groups: operational, process, failure, failure-specific
:From version: 1.8.2
:Description: None
:Data:
  :group_name: Name of the group.


  :property_name: Name of the property that cannot be inherited.





20023
^^^^^

:Message: Failed to read authorized SSH keys file "%(path)s". %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 1.6.0
:Description: None
:Data:
  :details: Details about the error.





20024
^^^^^

:Message: Internal error. Unhandled error. %(details)s
:Groups: operational, process, failure, failure-critical
:From version: 3.6.0
:Description: None



20031
^^^^^

:Message: Invalid account configuration for "%(username)s". %(details)s
:Groups: operational, session, failure, failure-high
:From version: 1.6.0
:Description: None



20032
^^^^^

:Message: Failed to initialize the SSL/TLS context. Using cert:%(cert)s key:%(key)s ca:%(ca)s crl:%(crl)s. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 1.6.0
:Description: None
:Data:
  :ca: Path to the certificate of the CA used by this SSL/TLS context.


  :cert: Path to X509 certificates.


  :crl: CRL used by this SSL/TLS context


  :key: Path to the key associated to the certificate.





20033
^^^^^

:Message: Internal error. Unhandled logged error. %(reason)s %(details)s
:Groups: operational, process, failure, failure-critical
:From version: 3.7.0
:Description: None



20034
^^^^^

:Message: Unknown protocol "%(protocol)s" for service "%(service_uuid)s".
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 1.6.0
:Description: None
:Data:
  :protocol: Name of the unknown protocol.


  :service_uuid: Name of the service for which an unknown protocol was defined.





20035
^^^^^

:Message: Connection failed for %(name)s. Retrying %(retries_left)s more times after %(delay)s seconds. %(details)s
:Groups: operational, session, failure
:From version: 3.9.0
:Description: None
:Data:
  :delay: Number of seconds after which the connection is retried.


  :retries_left: Number of retries left.





20036
^^^^^

:Message: Failed to read the certificate revocation list located at "%(uri)s". %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 1.6.0
:Description: None



20037
^^^^^

:Message: Certificate revocation list located at "%(uri)s" and issued by "%(issuer)s" was successfully updated and has now %(count)s entries. Next update advertised as %(next_update)s. Next update scheduled in %(update_seconds)s seconds for UTC %(update_datetime)s.
:Groups: operational, authenticated, informational
:From version: 3.13.0
:Description: None
:Data:
  :count: Number of loaded revoked certificates in the CRL


  :issuer: The subject field of the CRL's issuer.


  :next_publish: UTC date and time at which the CRL advertised its next publish


  :next_update: UTC date and time at which the CRL advertised its next update


  :update_datetime: UTC date and time at which the CRL will be loaded again


  :update_seconds: Number in seconds after which the CRL will be loaded again.


  :uri: Path or url from where the CRL was loaded





20038
^^^^^

:Message: Reloading failed for certificate revocation list located at "%(uri)s". Next update scheduled in %(next_load)s seconds. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 3.14.0
:Description: None
:Data:
  :next_load: Number in seconds after which the CRL will be loaded again.


  :uri: Path or url from where the CRL was loaded





20039
^^^^^

:Message: The operational audit report was successfully generated at %(path)s.
:Groups: process, operational, success, file-operation
:From version: 3.23.0
:Description: None



20040
^^^^^

:Message: Invalid certificate %(serial_number)s "%(subject)s". %(details)s
:Groups: operational, authenticated, failure
:From version: 1.6.0
:Description: None
:Data:
  :subject: Certificate subject.





20041
^^^^^

:Message: Failed to create configuration for service "%(service_name)s". %(details)s
:Groups: operational, process, failure, failure-high
:From version: 1.8.0
:Description: None



20042
^^^^^

:Message: Created missing account folder "%(path)s" with owner "%(owner)s" and group "%(group)s".
:Groups: operational, authenticated, success
:From version: 1.8.3
:Description: A note that the account had a missing required folder, and it was automatically created after a successful authentication.
:Data:
  :group: Name of the group for the new folder


  :owner: Name of the owner for new folder


  :path: Path to the created folder.





20043
^^^^^

:Message: Failed to retrieve group. %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 2.0.0
:Description: Error occurred while retrieving the group for new home folder.
:Data:
  :details: Details about the error.





20045
^^^^^

:Message: Service "%(service_name)s" stopped with a failure. %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 2.1.0
:Description: Service was stopped with a failure.
:Data:
  :details: Details about failure during stop.


  :service_name: Name of the service.





20046
^^^^^

:Message: Configuration changes stored in the local files.
:Groups: operational, authenticated, success
:From version: 1.6.0
:Description: None



20047
^^^^^

:Message: Bad value for passive port range. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the error.





20049
^^^^^

:Message: Failed to save configuration changes to the local files. Changes will be discarded after server restart. %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 2.6.0
:Description: None



20051
^^^^^

:Message: Successfully performing %(operation)s to "%(path)s" from "%(source_path)s".
:Groups: operational, authenticated, success
:From version: 3.43.0
:Description: None
:Data:
  :path: Path to the destination file which was handled.


  :source_path: Path to the source file which was handled.





20052
^^^^^

:Message: Failed to perform %(operation)s on "%(real_path)s". %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 3.43.0
:Description: None
:Data:
  :path: Path to the source file which was handled.





20053
^^^^^

:Message: Successfully executed "%(command)s". Exit code "%(exit_code)s". Output "%(output_log)s". Error "%(error_log)s".
:Groups: operational, process, success
:From version: 3.47.0
:Description: None
:Data:
  :command: Executed command.


  :error: The full the standard error produced by the command.


  :error_log: First part of the standard error produced by the command, with newlines replaced by spaces.


  :exit_code: Exit code of the executed command.


  :ouput: The full standard output produced by the command.


  :ouput_log: First part of the standard output produced by the command, with newlines replaced by spaces.





20054
^^^^^

:Message: Failed to execute "%(command)s". %(details)s
:Groups: operational, process, failure, failure-high
:From version: 3.47.0
:Description: None
:Data:
  :command: Executed command.





20055
^^^^^

:Message: Startup command executed with output "%(output)s" and error "%(error)s" and exit code "%(exit_code)s".
:Groups: operational, process, success
:From version: 1.6.0
:Description: Called after executing the server startup command.
:Data:
  :error: Standard error data generated by the command.


  :exit_code: Exit code of the command.


  :output: Standard output data generated by the command.





20056
^^^^^

:Message: Failed to execute startup command "%(command)s". %(details)s
:Groups: operational, process, failure, failure-high
:From version: 1.6.0
:Description: Called when failing to execute the startup command.
:Data:
  :command: Name of the command.


  :details: Details about the failure reason.





20058
^^^^^

:Message: Internal error. Failed to get avatar for "%(username)s". %(details)s
:Groups: operational, session, failure, failure-critical
:From version: 1.6.0
:Description: None
:Data:
  :details: Details about the failure.


  :username: Name for the account for which the authentication failed





20059
^^^^^

:Message: Internal error. Failed to authenticate "%(name)s". %(details)s
:Groups: operational, session, failure, failure-critical
:From version: 1.6.0
:Description: None



20062
^^^^^

:Message: Failed to delete older database events: %(details)s
:Groups: process, failure, failure-high
:From version: 3.42.0
:Description: None



20063
^^^^^

:Message: Missing special group with name "%(name)s". Please add it to your configuration. See documentation for more details about special groups.
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 1.8.2
:Description: None



20064
^^^^^

:Message: Failed to set new password. %(details)s
:Groups: operational, authenticated, failure
:From version: 3.42.0
:Description: None



20065
^^^^^

:Message: Snapshot with %(total_files)s files and %(total_directories)s directories for "%(path)s".
:Groups: operational, informational, authenticated
:From version: 5.1.0
:Description: None
:Data:
  :path: Path which was monitored.


  :total_directories: Number of directories which were detected.


  :total_files: Number of files which were detected and matching the filter.





20066
^^^^^

:Message: Stopping %(family)s "%(name)s"%(kind)s due to too many failures.
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 1.6.0
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :kind: Human readable description of the type of this component


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.





20067
^^^^^

:Message: Failed to get home/root folder for account. %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 1.6.0
:Description: None



20069
^^^^^

:Message: Server running under the same account under which it was started. If started as root or as an user with sudo access without passwords, it is highly recommended to configure the server to run under a dedicated account.
:Groups: operational, process, informational
:From version: 1.6.0
:Description: None



20070
^^^^^

:Message: Operating system accounts authentication unavailable. Missing user impersonation capabilities.
:Groups: operational, process, informational
:From version: 1.6.0
:Description: None



20071
^^^^^

:Message: Switching server process to "%(account_name)s" account.
:Groups: operational, process, success
:From version: 1.6.0
:Description: None



20072
^^^^^

:Message: %(windows_legacy_service)sOS user: "%(os_user)s" Cryptography: %(cryptography_library_version)s. Working dir: "%(cwd)s". Privileges: %(process_privileges)s
:Groups: operational, process, informational
:From version: 1.6.0
:Description: Information on the main SFTPPlus process.
:Data:
  :cryptography_library_version: Library used for cryptography and SSL/TLS protocols.


  :cwd: The current working dirtory, used when relative paths are configured.


  :process_privileges: Details about the privileges available to the current process.


  :python_version: The current Python version used by the process.





20073
^^^^^

:Message: Creating root home folders for OS accounts is unavailable due to missing process permissions.
:Groups: operational, process, informational
:From version: 1.6.0
:Description: None



20074
^^^^^

:Message: Retrieving home folder paths for OS accounts is unavailable due to missing process permissions.
:Groups: operational, process, informational
:From version: 1.8.2
:Description: None



20075
^^^^^

:Message: Critical security error. The home folder "%(home_folder_path)s" might be in an inconsistent state. %(details)s
:Groups: operational, authenticated, failure, failure-critical
:From version: 2.0.0
:Description: None
:Data:
  :home_folder_path: Path to home folder.





20076
^^^^^

:Message: Service "%(service_name)s" started on "%(address)s:%(port)s" using "%(protocol)s" protocol.
:Groups: operational, authenticated, success
:From version: 1.8.0
:Description: None
:Data:
  :address: Address of the interfaces on which service is listening.


  :port: Port on which the service is listening


  :protocol: Protocol used by the service.


  :service_name: Name of the service that was started





20077
^^^^^

:Message: Failed to start the "%(service_name)s" service. %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 1.8.0
:Description: None
:Data:
  :details: Details about the failure reason.


  :service_name: Name of the service which failed to start.





20078
^^^^^

:Message: Service "%(service_name)s" stopped.
:Groups: operational, authenticated, success
:From version: 1.8.0
:Description: None
:Data:
  :service_name: Name of the service.





20079
^^^^^

:Message: Current resource usage: cpu=%(cpu_percent)s%% mem-res=%(memory_resident)s mem-virt=%(memory_virtual)s conn=%(connection_count)s file=%(file_count)s thread=%(thread_count)s cpus=%(global_cpus)s mem-available=%(global_memory_available)s.
:Groups: operational, process, informational
:From version: 3.44.0
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
:Groups: operational, process, failure
:From version: 3.44.0
:Description: None
:Data:
  :details: Comma separated value of resources which have triggered this event.


  :triggers: Triggers as list of (name, value) tuple.





20081
^^^^^

:Message: No configured authentication for "%(username)s" of type "%(credentials_type)s".
:Groups: operational, session, failure, failure-high, failure-specific
:From version: 4.0.0
:Description: None
:Data:
  :credentials_type: Type of the authentication request.


  :username: Name for which the authentication was requested.





20082
^^^^^

:Message: File %(path)s was successfully removed as it was older than %(age)s seconds.
:Groups: monitor, success, file-operation
:From version: 3.52.0
:Description: None
:Data:
  :age: Number of seconds since the file was not modified.





20083
^^^^^

:Message: Failed to remove %(path)s, which was older than %(age)s seconds. %(details)s
:Groups: monitor, failure, failure-high, file-operation
:From version: 3.52.0
:Description: None
:Data:
  :age: Number of seconds since the file was not modified.





20084
^^^^^

:Message: Failed to record analytics event. %(details)s
:Groups: process, operational, failure
:From version: 4.0.0
:Description: None



20085
^^^^^

:Message: User successfully updated own password.
:Groups: operational, authenticated, success
:From version: 3.43.0
:Description: None



20086
^^^^^

:Message: User failed to update own password. %(details)s
:Groups: operational, authenticated, failure
:From version: 3.43.0
:Description: None



20087
^^^^^

:Message: File "%(source_path)s" was successfully amended to %(path)s.
:Groups: process, informational, file-operation
:From version: 3.22.0
:Description: None
:Data:
  :source_path: Path of the source file which was modified.





20088
^^^^^

:Message: Failed to amend file "%(path)s" from %(source_path)s. %(details)s
:Groups: process, file-operation, failure, failure-high
:From version: 3.22.0
:Description: None
:Data:
  :source_path: Path of the source file which was modified.





20089
^^^^^

:Message: Can not delete default group "%(group_uuid)s".
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 2.1.0
:Description: None
:Data:
  :group_uuid: The uuid of the group for which delete action was requested.





20090
^^^^^

:Message: Unknown account type "%(account_type)s" for "%(account_uuid)s".
:Groups: operational, failure, failure-high, failure-specific
:From version: 2.1.0
:Description: None
:Data:
  :account_type: The type defined for the account


  :account_uuid: The uuid of the account with unknown type.





20091
^^^^^

:Message: Unknown type "%(type)s" for section "%(uuid)s".
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 2.1.0
:Description: None
:Data:
  :type: The type defined for the section.


  :uuid: The uuid of the section with unknown type.





20101
^^^^^

:Message: Stored hashed password for "%(username)s" is not valid. %(details)s
:Groups: operational, session, failure, failure-high
:From version: 2.2.0
:Description: None
:Data:
  :details: More details about the error.


  :username: Username with a bad hashed password.





20108
^^^^^

:Message: Can not delete configuration "%(uuid)s" as it is still used by: %(usage)s.
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 2.6.0
:Description: None
:Data:
  :usage: List of components still configured to use this configuration.


  :uuid: The uuid of the configuration for which delete action was requested.





20109
^^^^^

:Message: File "%(path)s" was successfully fallback "%(mode)s" to %(destinations)s.
:Groups: authenticated, informational, file-operation
:From version: 3.5.0
:Description: None
:Data:
  :destination_paths: List of destination where source path was dispatched.


  :destinations: Comma separated list of destinations where source path was dispatched.





20110
^^^^^

:Message: Failed to fallback "%(mode)s" file "%(path)s" to %(destinations)s. %(details)s
:Groups: authenticated, file-operation, failure, failure-high
:From version: 3.5.0
:Description: None
:Data:
  :destinations: Comma separated list of destinations where source path was tried to be dispatched.





20111
^^^^^

:Message: Skip auth "%(method_name)s" of type "%(method_type)s" because it is currently stopped. Consider starting the method or remove it from the list of authentication methods configured for this service.
:Groups: session, informational
:From version: 5.12.0
:Description: Emitted when an authentication method is configured as active for a service, but it is stopped.
:Data:
  :method_name: Name of the authentication method that was skipped.


  :method_type: Type of the authentication method that was skipped.





20112
^^^^^

:Message: Failed to perform %(action)s in db "%(database_name)s". %(details)s
:Groups: operational, process, failure, failure-high
:From version: 3.0.0
:Description: None
:Data:
  :action: Description of the action.


  :database_name: Database connection name.


  :details: Database error details.





20115
^^^^^

:Message: File %(path)s was not modified in the last %(age)s seconds.
:Groups: monitor, informational, file-operation
:From version: 3.5.0
:Description: None
:Data:
  :age: Number of seconds since the file was not modified.





20116
^^^^^

:Message: Invalid schema for table "%(table_name)s" in %(database_name)s. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 2.1.0
:Description: Invalid table schema.
:Data:
  :database_name: Database connection name


  :details: Information about the error.


  :table_name: Name of table with invalid schema.





20117
^^^^^

:Message: %(name)s unable to fetch entries from "%(database_name)s". Filter criteria: '%(filter)s'. Sort order '%(sort_order)s'. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 2.1.0
:Description: None.
:Data:
  :database_name: Database connection name.


  :details: Information about the error.


  :filter: Filter criteria.


  :name: Name of the database source that failed.


  :sort_order: Sort order for the entries





20119
^^^^^

:Message: Invalid public SSH keys for "%(username)s". %(details)s
:Groups: operational, session, failure, failure-high
:From version: 2.9.0
:Description: None
:Data:
  :username: Username to which the SSH public keys are associated.





20120
^^^^^

:Message: Wrong %(type)s value for option "%(option)s" in section "%(section)s". %(details)s
:Groups: operational, process, failure, failure-high
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the error.


  :option: Name of the option that was set.


  :section: Name of the section in which option was set.


  :type: Type of value that was requested to be set.





20121
^^^^^

:Message: Cannot set %(type)s value %(value)s for option %(option)s in %(section)s. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 2.1.0
:Description: None
:Data:
  :details: More details about the error.


  :option: Name of the option that was set.


  :section: Name of the section in which option was set.


  :type: Type of value that was requested to be set.


  :value: Value that was requested to be set.





20122
^^^^^

:Message: Failed to %(operation)s for "%(path)s" . %(details)s
:Groups: operational, process, failure, failure-high
:From version: 2.1.0
:Description: None
:Data:
  :details: More details about the error.


  :operation: Action that failed.


  :path: Path associated with the failure.





20123
^^^^^

:Message: Skipping %(operation)s on "%(real_path)s" as destination "%(destination_path)s" exists.
:Groups: operational, process, informational
:From version: 4.7.0
:Description: None
:Data:
  :destination_path: Path to the destination path that already exists.


  :real_path: Path to the source file which was handled.





20124
^^^^^

:Message: Dispatch ignored for "%(path)s" as file no longer exists.
:Groups: authenticated, informational
:From version: 4.2.0
:Description: None



20125
^^^^^

:Message: Failed to "%(mode)s" file "%(path)s" to %(destinations)s. %(details)s
:Groups: authenticated, file-operation, failure, failure-high
:From version: 3.5.0
:Description: None
:Data:
  :destinations: Comma separated list of destinations where source path was dispatched.





20126
^^^^^

:Message: More credentials needed for account "%(username)s" accepted by %(method_type)s authentication "%(method_name)s" using "%(credentials_type)s" credentials. Still required: %(required_credentials)s
:Groups: operational, session, informational
:From version: 4.10.0
:Description: None
:Data:
  :credentials_type: Type of the credentials used during authentication.


  :method_name: Name of the method used for authentication.


  :method_type: Type of the method used for authentication.


  :required_credentials: List of credentials that are still required to authenticate the account.


  :username: Name of the account which requested to authenticate.





20130
^^^^^

:Message: File "%(path)s" was successfully "%(mode)s" to "%(destinations)s".
:Groups: authenticated, informational, file-operation
:From version: 3.5.0
:Description: None
:Data:
  :destination_paths: List of destination where source path was dispatched.


  :destinations: Comma separated list of destinations where source path was copied.





20136
^^^^^

:Message: Account "%(username)s" forbidden by %(method_type)s authentication "%(method_name)s" using "%(credentials_type)s" credentials. %(details)s
:Groups: operational, session, failure
:From version: 2.10.0
:Description: None
:Data:
  :credentials_type: Type of the credentials used during authentication.


  :method_name: Name of the method used for authentication.


  :method_type: Type of the method used for authentication.


  :response: More details from the authentication rejection response.


  :username: Name of the account which requested to authenticate.





20137
^^^^^

:Message: Account "%(account_name)s" of type "%(account_type)s" from groups/roles "%(group_name)s", authenticated by "%(method_name)s" of type "%(method_type)s" using %(credentials_type)s credentials as "%(username)s". %(ignored_groups)s
:Groups: operational, authenticated, informational
:From version: 2.10.0
:Description: None
:Data:
  :account_name: Name of the authenticated account.


  :account_type: Type of the authenticated account.


  :account_uuid: UUID of the authenticated account.


  :credentials_type: Type of the accepted credentials.


  :group_name: Comma separated text with name of the group/role associated to this account. (Since 3.38.0)


  :group_names: List with name of the group/role associated to this account. (Since 4.16.0)


  :ignored_groups: Human readable description of the groups or roles not associated with the account due to source IP. (Since 4.22.0)


  :method_name: Name of the method used for authentication.


  :method_type: Type of the method used for authentication.


  :username: User name under which the authentication was requested.





20138
^^^^^

:Message: Failed to synchronize "%(component_family)s/%(component_uuid)s". Will retry in %(interval)ss. %(details)s
:Groups: operational, session, failure
:From version: 5.11.0
:Description: None



20139
^^^^^

:Message: SSLv3 detected for configuration "%(configuration)s". SSLv3 method is no longer secure due to POODLE vulnerability. If SSLv3 is still required please make sure you use it together with the non-CBC cipher RC4-SHA.
:Groups: operational, authenticated, failure, failure-specific
:From version: 2.8.0
:Description: None
:Data:
  :configuration: Full configuration value in which SSLv3 is used.





20140
^^^^^

:Message: Connecting resource "%(name)s".
:Groups: authenticated, informational, client-side
:From version: 3.9.0
:Description: None
:Data:
  :name: Name of the location associated with this event.





20141
^^^^^

:Message: Resource "%(name)s" successfully connected.
:Groups: operational, authenticated, success
:From version: 3.9.0
:Description: None



20142
^^^^^

:Message: Failed to get a valid response from the "%(method_name)s" authentication for the account "%(username)s" using %(credentials_type)s. %(details)s
:Groups: operational, session, failure, failure-high
:From version: 2.10.0
:Description: None
:Data:
  :credentials_type: Type of credentials provided by the client.


  :method_name: Name of the authentication method which failed.


  :username: Name of the account for which the failure occurred.





20143
^^^^^

:Message: Failed to configure log rotation. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 1.7.17
:Description: None
:Data:
  :details: More details about the error.





20144
^^^^^

:Message: EventNotFound: Unknown event with id "%(id)s". %(details)s
:Groups: operational, process, failure, failure-critical
:From version: 1.8.0
:Description: None
:Data:
  :details: Details error showing the source of this error.


  :id: ID of the original event.





20145
^^^^^

:Message: Failed to resolve text for event id "%(id)s" with data "%(bad_data)s". %(details)s
:Groups: operational, process, failure, failure-critical
:From version: 1.8.0
:Description: None
:Data:
  :bad_data: Data of the original event


  :id: ID of the event with error.





20146
^^^^^

:Message: Failed dispatch %(mode)s for "%(path)s". Will retry %(count)s more. Next try after %(wait)s seconds. %(details)s
:Groups: process, failure, file-operation
:From version: 4.5.0
:Description: None
:Data:
  :count: Number of times the dispatch will be retried from now on.


  :wait: Number of seconds to wait before retrying.





20149
^^^^^

:Message: Unknown keys for account configuration. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 2.10.0
:Description: None
:Data:
  :details: List with keys which were not accepted.





20151
^^^^^

:Message: No EventGroupDefinition with name %(name)s.
:Groups: operational, process, failure, failure-critical, failure-specific
:From version: 1.6.0
:Description: The event group could not be found in the database. This is emitted before the event db is loaded



20152
^^^^^

:Message: No such property: "%(name)s".
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 2.1.0
:Description: The property could not be found.
:Data:
  :name: Name of the requested property.





20153
^^^^^

:Message: No such section %(section_name)s.
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 2.1.0
:Description: The section could not be found.
:Data:
  :section_name: Name of the requested section.





20154
^^^^^

:Message: Create not supported for %(section_name)s.
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 2.1.0
:Description: Create operation is not supported.
:Data:
  :section_name: Name of the requested property.





20155
^^^^^

:Message: Delete not supported for %(name)s.
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 2.1.0
:Description: Delete operation is not supported.
:Data:
  :name: Name of the requested property.





20156
^^^^^

:Message: Successfully started %(family)s "%(name)s"%(kind)s. %(description)s
:Groups: operational, authenticated, success
:From version: 2.6.0
:Description: None
:Data:
  :description: A short human readable description of this component.


  :family: Family name of the component associated with this event.


  :kind: Human readable description of the type of this component


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.





20157
^^^^^

:Message: Stopped %(family)s "%(name)s"%(kind)s. %(reason)s
:Groups: operational, authenticated, success
:From version: 2.6.0
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :kind: Human readable description of the type of this component


  :name: Name of the component associated with this event.


  :reason: Reason for which the component was stopped. It can be either due to a failure or normal stop request for shutdown or administrative actions.


  :type: Type of the component associated with this event.





20158
^^^^^

:Message: Failed to start %(family)s "%(name)s"%(kind)s. %(details)s
:Groups: operational, authenticated, failure
:From version: 2.6.0
:Description: None
:Data:
  :family: Family name of the component which failed to start


  :kind: Human readable description of the type of this component


  :name: Name of the component which failed to start.


  :type: Type of the component which failed to start.





20159
^^^^^

:Message: Failed to stop %(family)s "%(name)s"%(kind)s. %(details)s
:Groups: operational, authenticated, failure
:From version: 2.6.0
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :kind: Human readable description of the type of this component


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.





20160
^^^^^

:Message: Unknown database "%(database_uuid)s" for %(family)s "%(name)s" of type %(type)s.
:Groups: operational, process, failure, failure-high, failure-specific
:From version: 2.6.0
:Description: None
:Data:
  :database_uuid: UUID of configured database for event monitor.


  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.





20161
^^^^^

:Message: Disconnected %(family)s "%(name)s" of type %(type)s as database is not available.
:Groups: operational, process, informational
:From version: 2.6.0
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.





20162
^^^^^

:Message: Resumed %(family)s "%(name)s" of type %(type)s as database became available.
:Groups: operational, process, informational
:From version: 2.6.0
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.





20163
^^^^^

:Message: Internal error. Failure for account activity event handler "%(name)s". %(details)s
:Groups: operational, process, failure, failure-critical
:From version: 2.6.0
:Description: None
:Data:
  :name: Name of the event handler.





20164
^^^^^

:Message: Unable to migrate database "%(database_uuid)s" table for %(family)s "%(name)s" of %(type)s . %(details)s
:Groups: operational, process, failure, failure-high
:From version: 2.6.0
:Description: None
:Data:
  :database_uuid: UUID of configured database for event monitor.


  :details: Details about the migration error.


  :family: Family name of the component associated with this event.


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.





20165
^^^^^

:Message: Failure while running %(family)s "%(name)s"%(kind)s. %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 2.10.0
:Description: Used when the the component failed without an explicit error id.
:Data:
  :family: Family name of the component which failed to start


  :kind: Human readable description of the type of this component


  :name: Name of the component which failed to start.


  :type: Type of the component which failed to start.





20166
^^^^^

:Message: File "%(path)s" was modified in monitor %(name)s.
:Groups: file-operation, informational, monitor
:From version: 2.10.0
:Description: None.
:Data:
  :name: Name of the monitor.





20167
^^^^^

:Message: File "%(from_path)s" was renamed in monitor %(name)s to "%(to_path)s".
:Groups: file-operation, informational, monitor
:From version: 2.10.0
:Description: None
:Data:
  :from_path: Initial path.


  :to_path: Final path.





20168
^^^^^

:Message: Folder "%(from_path)s" was renamed in monitor %(name)s to "%(to_path)s".
:Groups: file-operation, informational, monitor
:From version: 2.10.0
:Description: None
:Data:
  :from_path: Initial path.


  :name: Name of the monitor.


  :to_path: Final path.





20169
^^^^^

:Message: File "%(path)s" was created in monitor %(name)s.
:Groups: file-operation, informational, monitor
:From version: 2.10.0
:Description: None
:Data:
  :name: Name of the monitor.





20170
^^^^^

:Message: Folder "%(path)s" was created in monitor %(name)s.
:Groups: file-operation, informational, monitor
:From version: 2.10.0
:Description: None
:Data:
  :name: Name of the monitor.





20171
^^^^^

:Message: File "%(path)s" was deleted in monitor %(name)s.
:Groups: file-operation, informational, monitor
:From version: 2.10.0
:Description: None
:Data:
  :name: Name of the monitor.





20172
^^^^^

:Message: Folder "%(path)s" was deleted in monitor %(name)s.
:Groups: file-operation, informational, monitor
:From version: 2.10.0
:Description: None
:Data:
  :name: Name of the monitor.





20173
^^^^^

:Message: File "%(path)s" has a valid digital signature.
:Groups: file-operation, process, informational
:From version: 3.5.0
:Description: None



20174
^^^^^

:Message: Failed to handle event %(id)s by "%(name)s" for "%(target_path)s". %(details)s
:Groups: authenticated, failure, failure-high
:From version: 2.10.0
:Description: None
:Data:
  :%(traceback)s: Details to troubleshoot this failure.


  :family: Family of the event handler that failed.


  :id: ID of the event which failed to be sent.


  :name: Name of the event handler that failed.


  :target_path: Path to a file associated with the failed event handling.





20175
^^^^^

:Message: File "%(source_path)s" was successfully rotated as "%(path)s" with a size of %(size)s bytes.
:Groups: operational, process, success, file-operation
:From version: 3.12.0
:Description: None
:Data:
  :path: New (current) path of the rotated file.


  :source_path: Previous path where the rotated file was located.





20176
^^^^^

:Message: File "%(path)s" was successfully rotated without keeping any copy of the previous content.
:Groups: operational, process, success, file-operation
:From version: 3.12.0
:Description: None
:Data:
  :path: Path of the rotated file.





20177
^^^^^

:Message: File "%(path)s" has failed digital signature validation. %(details)s
:Groups: file-operation, process, failure, failure-high
:From version: 3.5.0
:Description: None
:Data:
  :details: Reason of the failure.


  :path: Path to the file with valid signature.





20178
^^^^^

:Message: Failed to load CRL from the CDP of "%(peer_subject)s". %(details)s
:Groups: operational, process, failure
:From version: 3.12.0
:Description: None
:Data:
  :details: Reason of the failure.


  :path: Subject of the peer certificate for which CDP/CRL loading failed.





20179
^^^^^

:Message: File "%(path)s" exists in the monitor %(name)s.
:Groups: file-operation, informational, monitor
:From version: 3.6.0
:Description: None
:Data:
  :name: Name of the monitor.





20180
^^^^^

:Message: Folder "%(path)s" exists in the monitor %(name)s.
:Groups: file-operation, informational, monitor
:From version: 3.6.0
:Description: None
:Data:
  :name: Name of the monitor.





20181
^^^^^

:Message: Started %(instance_name)s - %(product_version)s.
:Groups: operational, process, informational
:From version: 3.9.0
:Description: None
:Data:
  :instance_name: Name of this installation instance


  :product_version: Current version of the product.





20182
^^^^^

:Message: Account "%(account_name)s" logged in with permissions %(permissions)s. Files will be uploaded as: %(upload_names)s
:Groups: operational, authenticated, informational
:From version: 3.13.0
:Description: None
:Data:
  :account_name: Name of the account which logged in.


  :permissions: Permissions configured for account.


  :upload_names: Format of the files as they are uploaded.





20183
^^^^^

:Message: Unexpected error occurred during log rotation. %(details)s.
:Groups: operational, process, failure, failure-high, file-operation
:From version: 3.14.0
:Description: None
:Data:
  :details: Reason of the failure.





20184
^^^^^

:Message: Internal Error. Failed to start %(family)s "%(name)s"%(kind)s. %(details)s %(tb)s.
:Groups: operational, authenticated, failure, failure-critical
:From version: 3.24.0
:Description: None
:Data:
  :family: Family name of the component which failed to start


  :kind: Human readable description of the type of this component


  :name: Name of the component which failed to start.


  :type: Type of the component which failed to start.





20185
^^^^^

:Message: Internal Error. Failed to stop %(family)s "%(name)s"%(kind)s. %(details)s
:Groups: operational, authenticated, failure, failure-critical
:From version: 3.24.0
:Description: None
:Data:
  :family: Family name of the component associated with this event.


  :kind: Human readable description of the type of this component


  :name: Name of the component associated with this event.


  :type: Type of the component associated with this event.





20186
^^^^^

:Message: You are using the evaluation version. Email us at sales@proatria.com or visit https://www.sftpplus.com/pricing/ to get the full licence. %(details)s
:Groups: process, operational, informational
:From version: 3.29.0
:Description: Upgrading is straight-forward. Once upgraded, you can continue to use the same configuration files or start with a new setup. For technical support and other questions about the demo, please email our team at support@proatria.com.
:Data:
  :details: Additional information about the demo version status.





20187
^^^^^

:Message: Successfully performing %(operation)s to member "%(path)s" from "%(source_path)s".
:Groups: operational, process, success
:From version: 3.52.0
:Description: None
:Data:
  :path: Path to the destination file which was extracted.


  :source_path: Path to the source file which was extracted.





20188
^^^^^

:Message: Overwriting destination "%(destination_path)s" while performing %(operation)s on "%(real_path)s".
:Groups: operational, process, informational
:From version: 4.7.0
:Description: None
:Data:
  :destination_path: Path to the destination path that already exists.


  :real_path: Path to the source file which was handled.





20189
^^^^^

:Message: HTTP POST notification for event %(event_id)s successful for "%(target_path)s".
:Groups: operational, authenticated, informational
:From version: 4.16.0
:Description: None
:Data:
  :event_id: The original event ID for which this was requested.


  :target_path: Path to a file associated with the HTTP post.





20190
^^^^^

:Message: Invalid value "%(invalid_value)s" defined for "%(option)s" in "%(section)s". Using "%(default)s" value. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 4.21.0
:Description: None
:Data:
  :default: Value used instead of the invalid configuration.


  :invalid_value: The value found in the configuration.


  :option: The name of the configuration option.


  :section: The section/component for which this option is defined.





20191
^^^^^

:Message: Failure on %(operation)s operation for file transfer analytics. %(details)s
:Groups: failure, process
:From version: 4.24.0
:Description: Emitted when failed to perform a transfer analytics operation.



20192
^^^^^

:Message: Last day client-side transfer statistics. Successful files %(success_files)s, retried files %(retried_files)s, success jobs %(success_jobs)s, failed jobs %(failure_jobs)s, total size %(total_size)s bytes, total duration %(total_duration)s seconds.
:Groups: informational, process, client-side
:From version: 4.24.0
:Description: Emitted to inform the statistic for transferred files.
:Data:
  :failure_jobs: Number of transfer jobs that failed after all retries.


  :retried_files: Number of files that were retried


  :success_files: Number of files that were successfully transferred, include those that succeed after a retry.


  :success_jobs: Number of transfer jobs that success for all files.


  :total_duration: Total duration, in seconds, of the files that were successfully transferred


  :total_size: Total size in bytes of the files that were successfully transferred.





20193
^^^^^

:Message: File %(operation)s for %(account_name)s at "%(account_path)s".
:Groups: informational, authenticated
:From version: 4.25.0
:Description: Emitted when one account performs a file transfer operation on a file accessible to another account.
:Data:
  :account_name: The name of the other account that also has access to this file.


  :account_path: Path to the file as available ot the other account.


  :account_uuid: The UUID of the other account that also has access to this file.


  :operation: The file operation that was performed





20194
^^^^^

:Message: Digest message is "%(output)s" for %(path)s.
:Groups: operational, authenticated, success
:From version: 4.31.0
:Description: Result of the file digest event handler



20195
^^^^^

:Message: Account "%(account_name)s" was auto disabled as it was inactive in the last %(day_count)s days. Last login: %(last_login)s.
:Groups: operational, process, success
:From version: 4.32.0
:Description: Account auto-disabled for inactivity
:Data:
  :account_name: Name of the account


  :account_uuid: UUID of the account


  :day_count: Number of days for which this account is configured for auto-disable.


  :last_login: Date and time of the last login





20196
^^^^^

:Message: Fail to check auto-disable for "%(account_name)s". %(details)s
:Groups: operational, process, failure, failure-specific
:From version: 4.32.0
:Description: Account with invalid auto-disabled configuration
:Data:
  :account_name: Name of the account


  :account_uuid: UUID of the account





20197
^^^^^

:Message: Legacy text password automatically converted for account "%(account_name)s".
:Groups: operational, process, informational
:From version: 5.9.0
:Description: The legacy password for an account was automatically migrated.
:Data:
  :account_name: Name of the account





20200
^^^^^

:Message: %(message)s
:Groups: informational, authenticated
:From version: 4.19.0
:Description: Event designed to be emitted by Python API extension as informational.



20201
^^^^^

:Message: %(message)s
:Groups: success, authenticated
:From version: 5.1.0
:Description: Event designed to be emitted by Python API extension on success.



20202
^^^^^

:Message: %(message)s %(details)s
:Groups: failure, authenticated
:From version: 5.1.0
:Description: Event designed to be emitted by Python API extension on errors.
:Data:
  :details: Details for this error.


  :message: The high level description of the error.






FTP protocol
============






















































































10012
^^^^^


:Message: Successfully opened file "%(path)s" for writing at offset %(offset)s. Path requested as "%(requested_path)s.
:Groups: authenticated, success, file-operation, ftp
:From version: 2.4.0
:Description: None
:Data:
  :offset: Position inside the file where the write will begin.


  :path: Path as processed by the server.


  :requested_path: The path as it was requested by the client.











10013
^^^^^


:Message: Failed to open file "%(path)s" for writing  at offset %(offset)s. Path requested as "%(requested_path)s. %(details)s
:Groups: authenticated, failure, file-operation, ftp
:From version: 2.4.0
:Description: None
:Data:
  :path: Path as processed by the server.


  :requested_path: The path as it was requested by the client.











10014
^^^^^


:Message: Clients are required to send a valid certificate. Maybe the client did not send a certificate or the client certificate is not valid. %(details)s
:Groups: session, failure, ftp
:From version: 1.6.0
:Description: None









10015
^^^^^


:Message: Failed to get a new %(mode)s passive port. %(details)s
:Groups: authenticated, operational, failure, failure-high, ftp
:From version: 1.8.1
:Description: None
:Data:
  :mode: PASV or EPSV values.


  :port_range: Range from which passive ports are allocated.











10016
^^^^^


:Message: Internal error. Failed to process the FTP command "%(line)s". %(details)s
:Groups: operational, authenticated, failure, failure-critical, ftp, failure-specific
:From version: 1.6.0
:Description: None
:Data:
  :line: Full line of FTP command that generated the error.











10019
^^^^^


:Message: FTP command "%(command)s" not implemented by the service.
:Groups: authenticated, failure, ftp, failure-specific
:From version: 1.6.0
:Description: None
:Data:
  :command: FTP command received.











10020
^^^^^


:Message: Extended Passive transfer requested.
:Groups: operational, authenticated, ftp
:From version: 1.8.1
:Description: None









10021
^^^^^


:Message: Connection was closed before finalization of SSL handshake.
:Groups: session, failure, failure-specific, ftp
:From version: 1.6.0
:Description: None









10022
^^^^^


:Message: Expecting client connection on %(address)s:%(port)s for the next %(mode)s passive request.
:Groups: authenticated, informational, ftp
:From version: 1.8.1
:Description: This event is raised by both normal and extended passive requests.
:Data:
  :address: The network interface on which the passive connection is expected


  :mode: PASV or EPSV values.


  :port: Port number on which passive connection was established.











10023
^^^^^


:Message: No FTP client connection to %(mode)s passive data %(address)s:%(port)s. %(details)s
:Groups: authenticated, failure, failure-high, ftp
:From version: 2.1.0
:Description: None









10024
^^^^^


:Message: Initializing secure command channel.
:Groups: session, informational, ftp
:From version: 1.6.0
:Description: None









10025
^^^^^


:Message: Processing APPE command for file "%(path)s".
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: FTP APPE command request was received from the client.









10026
^^^^^


:Message: Invalid address "%(address)s" for %(kind)s data command.
:Groups: authenticated, failure, failure-specific, ftp
:From version: 2.1.0
:Description: None
:Data:
  :address: The requested raw address, in FTP format.


  :kind: Whether the error is for a passive or active transfer.











10027
^^^^^


:Message: No authentication method was enabled for this service.
:Groups: session, failure, failure-high, failure-specific, ftp
:From version: 1.7.4
:Description: None









10028
^^^^^


:Message: User "%(username)s" is required to authenticate using a SSL certificate.
:Groups: session, failure, ftp, failure-specific
:From version: 1.7.4
:Description: None









10029
^^^^^


:Message: Failed to authenticate as user "%(username)s" with X.509 certificate credentials.
:Groups: session, failure, failure-specific, ftp
:From version: 1.7.4
:Description: None
:Data:
  :username: Username requesting authentication.











10030
^^^^^


:Message: Data connection closed. Protected using %(encryption)s. Received: %(received)s. Sent %(sent)s. Speed %(speed)s bytes/second. Duration %(duration)s. %(host_address)s:%(host_port)s - %(peer_address)s:%(peer_port)s . Client certificate: %(certificate)s
:Groups: authenticated, success, ftp
:From version: 1.8.1
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


  :speed: The transfer speed in bytes per second.











10031
^^^^^


:Message: Data connection closed in a non clean way. Protected using %(encryption)s. Received %(received)s. Speed %(speed)s bytes/second. Sent %(sent)s. Duration %(duration)s. %(host_address)s:%(host_port)s - %(peer_address)s:%(peer_port)s. Client certificate: %(certificate)s %(details)s
:Groups: authenticated, failure, ftp
:From version: 1.8.1
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


  :speed: The transfer speed in bytes per second.











10032
^^^^^


:Message: Data connection time out after initialization. %(host_address)s:%(host_port)s - %(peer_address)s:%(peer_port)s.
:Groups: session, failure, failure-high, failure-specific, ftp
:From version: 1.8.3
:Description: None
:Data:
  :host_address: IP address for the local data connection.


  :host_port: Port number for the local data connection peer.


  :peer_address: IP address of the remote data connection peer.


  :peer_port: Port number of the remote data connection peer.











10033
^^^^^


:Message: New FTP/FTPS client connection made.
:Groups: session, success, ftp
:From version: 1.6.0
:Description: None









10034
^^^^^


:Message: Command connection closed. Protected using %(encryption)s. Client connected with certificate: %(certificate)s
:Groups: authenticated, success, ftp
:From version: 1.6.0
:Description: None
:Data:
  :certificate: The certificate of the remote client.











10035
^^^^^


:Message: SSL/TLS required on the command channel.
:Groups: session, failure, failure-specific, ftp
:From version: 1.6.0
:Description: None









10036
^^^^^


:Message: SSL/TLS required on the data channel.
:Groups: session, failure, failure-specific, ftp
:From version: 1.6.0
:Description: None









10037
^^^^^


:Message: Request to change current folder to "%(path)s".
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: None









10038
^^^^^


:Message: Current folder successfully changed to "%(path)s".
:Groups: authenticated, success, file-operation, ftp
:From version: 1.6.0
:Description: None









10039
^^^^^


:Message: Failed to change to folder "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ftp
:From version: 1.6.0
:Description: None
:Data:
  :details: Details about the failure.











10040
^^^^^


:Message: Successfully open file "%(path)s" for appending.
:Groups: authenticated, success, file-operation, operation-append, ftp
:From version: 2.4.0
:Description: None









10041
^^^^^


:Message: Failed to open file "%(path)s" for appending. %(details)s
:Groups: authenticated, failure, file-operation, operation-append, ftp
:From version: 2.4.0
:Description: None









10042
^^^^^


:Message: Command connection closed due to an error. Protected using %(encryption)s. Client certificate: %(certificate)s %(details)s
:Groups: authenticated, failure, ftp, failure-high
:From version: 2.8.0
:Description: None
:Data:
  :certificate: The certificate of the remote client.











10043
^^^^^


:Message: Request to delete "%(path)s".
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: None









10044
^^^^^


:Message: Successfully deleted "%(path)s".
:Groups: authenticated, success, file-operation, operation-delete, ftp
:From version: 1.6.0
:Description: None









10045
^^^^^


:Message: Failed to delete "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, operation-delete, ftp
:From version: 1.6.0
:Description: None









10046
^^^^^


:Message: Listing path "%(path)s" with wildcard "%(glob)s" for %(operation)s.
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: None
:Data:
  :operation: Type of the requested listing.











10047
^^^^^


:Message: Path "%(path)s" successfully listed with wildcard "%(glob)s" for %(operation)s.
:Groups: authenticated, success, file-operation, ftp
:From version: 1.6.0
:Description: None









10048
^^^^^


:Message: Failed to list path "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ftp
:From version: 1.6.0
:Description: None









10049
^^^^^


:Message: Getting attributes for "%(path)s".
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: None
:Data:
  :attributes: List of requested attributes.











10050
^^^^^


:Message: Successfully got attributes for "%(path)s".
:Groups: authenticated, success, file-operation, ftp
:From version: 1.6.0
:Description: None
:Data:
  :attributes: List of requested attributes.











10051
^^^^^


:Message: Failed to get attributes for "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ftp
:From version: 1.6.0
:Description: None
:Data:
  :attributes: List of requested attributes.











10052
^^^^^


:Message: Creating folder "%(path)s".
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: None









10053
^^^^^


:Message: Successfully created folder "%(path)s".
:Groups: authenticated, success, file-operation, operation-create-folder, ftp
:From version: 1.6.0
:Description: None









10054
^^^^^


:Message: Failed to create folder "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, operation-create-folder, ftp
:From version: 1.6.0
:Description: None









10055
^^^^^


:Message: Data connection opened. %(host_address)s:%(host_port)s - %(peer_address)s:%(peer_port)s
:Groups: authenticated, success, ftp
:From version: 3.14.0
:Description: None
:Data:
  :host_address: IP address for the local data connection.


  :host_port: Port number for the local data connection peer.


  :peer_address: IP address of the remote data connection peer.


  :peer_port: Port number of the remote data connection peer.











10059
^^^^^


:Message: User successfully logged on "%(real_path)s" as "%(virtual_path)s".
:Groups: authenticated, success, ftp
:From version: 1.6.0
:Description: None
:Data:
  :home_folder: User's home folder.


  :real_path: User's home folder system path.











10061
^^^^^


:Message: Passive transfer requested in %(mode)s mode.
:Groups: authenticated, informational, ftp
:From version: 1.6.0
:Description: None
:Data:
  :mode: PASV or EPSV values.











10062
^^^^^


:Message: Active transfer requested in %(mode)s mode to "%(address)s:%(port)s".
:Groups: authenticated, informational, ftp
:From version: 1.6.0
:Description: None
:Data:
  :address: Address on the client where server should connect for active transfer.


  :mode: PORT or EPRT values.


  :port: Port where server should connect.











10063
^^^^^


:Message: Successfully initiated active connection to destination %(address)s:%(port)s using source %(source_address)s:%(source_port)s.
:Groups: authenticated, success, ftp
:From version: 1.6.0
:Description: None
:Data:
  :address: IP address of the remote data connection peer.


  :port: Port number of the remote data connection peer.


  :source_address: Source IP address use for data connection.


  :source_port: Source TCP port used for data connection.











10064
^^^^^


:Message: Failed to initiate active connection to destination %(address)s:%(port)s using source %(source_address)s:%(source_port)s. %(details)s
:Groups: authenticated, failure, failure-high, ftp
:From version: 1.6.0
:Description: None
:Data:
  :address: IP address of the remote data connection peer.


  :port: Port number of the remote data connection peer.


  :source_address: Source IP address use for data connection.


  :source_port: Source TCP port used for data connection.











10065
^^^^^


:Message: Requesting current folder.
:Groups: authenticated, success, ftp
:From version: 1.6.0
:Description: None









10066
^^^^^


:Message: Closing current FTP session.
:Groups: session, success, ftp
:From version: 1.6.0
:Description: None









10068
^^^^^


:Message: Opening file "%(path)s" for reading.
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: None









10069
^^^^^


:Message: Close successfully delivered file "%(path)s". Read %(total)s bytes at %(speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, success, file-operation, operation-read, ftp
:From version: 1.6.0
:Description: None









10070
^^^^^


:Message: Close failed delivered file "%(path)s". Read %(total)s bytes at %(speed)s bytes/second in %(duration)s seconds. %(details)s
:Groups: authenticated, failure, failure-high, file-operation, operation-read, ftp
:From version: 1.6.0
:Description: None









10071
^^^^^


:Message: Deleting folder "%(path)s".
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: None









10072
^^^^^


:Message: Successfully deleted folder "%(path)s".
:Groups: authenticated, success, file-operation, operation-delete, ftp
:From version: 1.6.0
:Description: None









10073
^^^^^


:Message: Failed to delete folder "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, operation-delete, ftp
:From version: 1.6.0
:Description: None









10074
^^^^^


:Message: Renaming "%(from)s" to "%(to)s".
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: None
:Data:
  :from: Current name of the file.


  :path: Current name of the file.


  :to: The future name of the file.











10075
^^^^^


:Message: Successfully renamed "%(from)s" to "%(to)s".
:Groups: authenticated, success, file-operation, operation-rename, ftp
:From version: 1.6.0
:Description: None
:Data:
  :from: Old name of the file.


  :path: Old name of the file.


  :to: The new name of the file.











10076
^^^^^


:Message: Failed to rename "%(from)s" to "%(to)s". %(details)s
:Groups: authenticated, failure, file-operation, operation-rename, ftp
:From version: 1.6.0
:Description: None
:Data:
  :from: Current name of the file.


  :path: Current name of the file.


  :to: The future name of the file.











10077
^^^^^


:Message: Processing STOR command for file "%(path)s".
:Groups: authenticated, file-operation, informational, ftp
:From version: 1.6.0
:Description: FTP STOR command request was received from the client.
:Data:
  :path: The path as it will be processed by the command.











10078
^^^^^


:Message: Close successfully received file "%(path)s". Wrote %(total)s bytes at %(speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, success, file-operation, operation-write, ftp
:From version: 1.6.0
:Description: None









10079
^^^^^


:Message: Close for failed receive file "%(path)s". Wrote %(total)s bytes at %(speed)s bytes/second in %(duration)s seconds. %(details)s
:Groups: authenticated, failure, failure-high, file-operation, operation-write, ftp
:From version: 1.6.0
:Description: None









10080
^^^^^


:Message: Unknown FTP representation type "%(type)s".
:Groups: authenticated, failure, ftp, failure-specific
:From version: 2.12.0
:Description: None
:Data:
  :type: The value requested for the type.











10081
^^^^^


:Message: FTP representation type set to "%(type)s".
:Groups: authenticated, success, ftp
:From version: 2.12.0
:Description: None
:Data:
  :type: The value requested for the type.











10082
^^^^^


:Message: Ignoring FTP representation type for "%(type)s".
:Groups: authenticated, informational, ftp
:From version: 3.9.0
:Description: None
:Data:
  :type: The value requested for the type.











10083
^^^^^


:Message: Listening on port %(port)s for the next passive request.
:Groups: authenticated, success, session, ftp
:From version: 1.6.0
:Description: None
:Data:
  :port: Port number on which passive connection was established.











10084
^^^^^


:Message: Client FTP/FTPS connection time out.
:Groups: session, failure, failure-high, ftp, failure-specific
:From version: 1.6.0
:Description: None









10085
^^^^^


:Message: Successfully cleared the command channel.
:Groups: authenticated, success, ftp
:From version: 1.7.18
:Description: None









10086
^^^^^


:Message: Command channel is already cleared.
:Groups: authenticated, failure, ftp, failure-specific
:From version: 1.7.18
:Description: None









10087
^^^^^


:Message: Server does not allow to clear the command channel.
:Groups: authenticated, failure, ftp, failure-specific
:From version: 1.7.18
:Description: None









10088
^^^^^


:Message: Failed to secure the %(channel_type)s channel. %(details)s
:Groups: authenticated, failure, failure-high, ftp
:From version: 3.47.0
:Description: FTP TLS handshake failed (server-side).









10089
^^^^^


:Message: Failed to initiate FTP session. %(details)s
:Groups: authenticated, failure, ftp
:From version: 4.16.0
:Description: None









10090
^^^^^


:Message: Extended address active transfer requested to protocol "%(protocol)s" on address "%(ip)s:%(port)s".
:Groups: authenticated, informational, ftp
:From version: 1.7.18
:Description: None
:Data:
  :ip: Destination IP address.


  :port: Destination port.


  :protocol: Protocol name.











10091
^^^^^


:Message: New client connection denied. Too many concurrent FTP/FTPS connections.
:Groups: session, failure, failure-specific, ftp
:From version: 1.8.0
:Description: None









10092
^^^^^


:Message: Internal error. Failed to start FTP protocol handler. %(details)s
:Groups: session, failure, failure-critical, ftp
:From version: 1.8.3
:Description: An internal server error occurred while creating FTP protocol handler for new client.









10093
^^^^^


:Message: Explicit FTPS for %(service)s changed to %(state)s.
:Groups: operational, administration, informational, ftp
:From version: 2.4.0
:Description: Inform about changes in SSL layer for FTP protocol.
:Data:
  :service: Name of the service.


  :state: New state.











10094
^^^^^


:Message: Successfully open file "%(path)s" for reading at offset %(offset)s.
:Groups: authenticated, success, file-operation, operation-read, ftp
:From version: 2.4.0
:Description: None
:Data:
  :offset: Position inside the file where the read will begin.











10095
^^^^^


:Message: Failed to open file "%(path)s" for reading at offset %(offset)s. %(details)s
:Groups: authenticated, failure, file-operation, operation-read, ftp
:From version: 2.4.0
:Description: None









10096
^^^^^


:Message: Setting attributes for "%(path)s" to "%(attributes)s".
:Groups: authenticated, informational, file-operation, ftp
:From version: 2.6.0
:Description: None









10097
^^^^^


:Message: Successfully set attributes for "%(path)s" to "%(attributes)s".
:Groups: authenticated, success, file-operation, ftp
:From version: 2.6.0
:Description: None









10098
^^^^^


:Message: Failed to set attributes for "%(path)s" to "%(attributes)s". %(details)s
:Groups: authenticated, failure, file-operation, ftp
:From version: 2.6.0
:Description: None
:Data:
  :details: More details about the failure.











10099
^^^^^


:Message: Connected to passive data port %(host)s:%(port)s for "%(command)s". Server address: %(fqdn)s
:Groups: session, informational, ftp, client-side
:From version: 4.27.0
:Description: None
:Data:
  :host: The address of the remote FTP server used to connect to the passive port.


  :port: The remote server port number used for the FTP passive connection.











10100
^^^^^


:Message: Secure %(channel_type)s channel successfully initialized. Protected using: %(encryption)s. Client certificate: %(certificate)s
:Groups: authenticated, success, ftp
:From version: 4.33.0
:Description: FTP TLS handshake done (server-side).
:Data:
  :certificate: Certificate sent by the client over the command channel.


  :encryption: The cipher suite used to protect the command channel.











10101
^^^^^


:Message: Secure %(channel_type)s channel successfully initialized. Protected using: %(encryption)s. Server certificate: %(certificate)s
:Groups: authenticated, success, ftp, client-side
:From version: 4.33.0
:Description: FTP TLS handshake done (client-side).
:Data:
  :certificate: Certificate sent by the server over the command channel.


  :encryption: The cipher suite used to protect the command channel.











10102
^^^^^


:Message: Connected to the FTP/FTPS server.
:Groups: session, informational, ftp, client-side
:From version: 3.2.0
:Description: None









10103
^^^^^


:Message: Connection to FTP/FTPS server was lost. Protected using: %(encryption)s. Server certificate: %(certificate)s. Reason: %(reason)s
:Groups: session, informational, ftp, client-side
:From version: 3.2.0
:Description: None
:Data:
  :certificate: Certificate sent by the server over the command channel.


  :encryption: The cipher suite used to protect the command channel.











10104
^^^^^


:Message: Failed authentication. Credentials not accepted for "%(name)s". %(details)s
:Groups: operational, session, ftp, failure, client-side
:From version: 3.2.0
:Description: None
:Data:
  :name: Name of the location which failed at the authentication process.











10105
^^^^^


:Message: Security for the command channel cleared in "%(mode)s" mode.
:Groups: authenticated, informational, ftp, client-side
:From version: 3.13.0
:Description: None









10106
^^^^^


:Message: Connection to FTP/FTPS was authenticated.
:Groups: authenticated, informational, ftp, client-side
:From version: 3.2.0
:Description: FTP client auth accepted.









10107
^^^^^


:Message: Failed to secure the %(channel_type)s channel. %(details)s
:Groups: session, failure, failure-high, ftp, client-side
:From version: 4.33.0
:Description: FTP TLS handshake failed (client-side).









10108
^^^^^


:Message: Failed to setup TLS session on data connection for "%(command)s". %(details)s
:Groups: authenticated, failure, failure-high, ftp
:From version: 4.35.0
:Description: FTP TLS handshake failed (client-side).









































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































SSH protocol
============














































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































30004
^^^^^


:Message: Global request "%(request_type)s" declined.
:Groups: authenticated, informational, ssh
:From version: 3.18.0
:Description: None
:Data:
  :request_type: Request type that was rejected.











30005
^^^^^


:Message: SSH command %(message_id)s is not supported. %(payload)s
:Groups: operational, authenticated, failure, failure-specific, ssh
:From version: 3.1.0
:Description: None
:Data:
  :message_id: ID of the command as specified by the SSH Standard.


  :payload: The data received together with the SSH command.











30006
^^^^^


:Message: Internal error. Failed to process the SSH command %(message_id)s - %(payload)s. %(details)s
:Groups: operational, session, failure, failure-critical, ssh
:From version: 3.1.0
:Description: None
:Data:
  :message_id: ID of the command as specified by the SSH Standard.


  :payload: The data received together with the SSH command.











30007
^^^^^


:Message: SSH protocol failure at userauth service. %(details)s
:Groups: session, failure, failure-high, ssh
:From version: 3.1.0
:Description: None
:Data:
  :method: Name of the requested SSH authentication method.











30008
^^^^^


:Message: SSH request rejected. %(details)s
:Groups: authenticated, failure, ssh
:From version: 1.6.0
:Description: None









30009
^^^^^


:Message: Start processing '%(command)s' command.
:Groups: operational, authenticated, informational, ssh
:From version: 3.45.0
:Description: None
:Data:
  :command: Name of the requested command.











30010
^^^^^


:Message: End processing '%(command)s' command.
:Groups: operational, authenticated, informational, ssh
:From version: 3.45.0
:Description: None
:Data:
  :command: Name of the requested command.











30011
^^^^^


:Message: Subsystem %(service_name)s successfully started in "%(real_path)s" as "%(virtual_path)s". Protected using %(host_key)s %(key_exchange)s %(in_hmac)s %(in_cipher)s compression:%(in_compression)s.
:Groups: authenticated, success, ssh
:From version: 1.6.0
:Description: None
:Data:
  :in-compression: Compression used to receive data.


  :in_cipher: Cipher used for received data.


  :in_hmac: Hash-based message authentication code for received data.


  :max_packet_local: The maximum packet size we can receive.


  :max_packet_remote: The maximum packet size we can send.


  :out-compression: Compression used to send data.


  :out_cipher: Cipher used for sent data.


  :out_hmac: Hash-based message authentication code for sent data.


  :real_path: Path on the server's filesystem where SFTP session was initiated.


  :service_name: Name of the SSH subsystem used. Ex SFTP or SCP.


  :virtual_path: Path of the folder in the virtual filesystem where sessions was initiated.


  :window_local: How much more data can be received before the server will ask to extend the receive buffer.


  :window_remote: How much more data can be send before the server will wait for the client to to extend the send buffer.











30012
^^^^^


:Message: SFTP subsystem closed. Using SFTP version %(client_version)s.
:Groups: authenticated, success, ssh
:From version: 1.6.0
:Description: None
:Data:
  :client_version: SFTP version used for the connection.











30013
^^^^^


:Message: SSH algorithms negotiation failed at %(type)s. Client: "%(client_algorithms)s". Server: "%(server_algorithms)s".
:Groups: session, failure, failure-high, failure-specific, ssh
:From version: 5.1.0
:Description: Emitted when we don't have a match for the client and server algorithms.
:Data:
  :client_algorithms: List of algorithm supported by client.


  :server_algorithms: List of algorithm supported by server.


  :type: The type of algorithm for which no common value was found.











30014
^^^^^


:Message: New SSH connection made.
:Groups: session, success, ssh
:From version: 1.6.0
:Description: None









30015
^^^^^


:Message: SSH connection closed from "%(client_version)s". Protected using host-key:%(host_key)s key-exchange:%(key_exchange)s in-hmac:%(in_hmac)s in-cipher:%(in_cipher)s out-hmac:%(out_hmac)s out-cipher:%(out_cipher)s in-compression:%(in_compression)s out-compression:%(out_compression)s
:Groups: authenticated, informational, ssh
:From version: 1.6.0
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


:Message: Failed to process the SFTP command. %(details)s
:Groups: operational, authenticated, failure, failure-high, ssh
:From version: 1.6.0
:Description: None









30017
^^^^^


:Message: Close file "%(path)s" after successful %(mode)s. Read %(total_read)s bytes at %(read_speed)s bytes/second and wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, success, file-operation, ssh
:From version: 1.6.0
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


:Message: Internal error. Failure in the SSH userauth service for "%(username)s". %(details)s
:Groups: session, failure, failure-critical, ssh
:From version: 1.8.1
:Description: None
:Data:
  :username: Name of the account.











30019
^^^^^


:Message: Listing folder "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 1.6.0
:Description: None









30020
^^^^^


:Message: Successfully listed folder "%(path)s".
:Groups: authenticated, success, file-operation, ssh
:From version: 1.6.0
:Description: None









30021
^^^^^


:Message: Failed to list folder "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.











30022
^^^^^


:Message: Deleting "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 1.6.0
:Description: None









30023
^^^^^


:Message: Successfully deleted "%(path)s".
:Groups: authenticated, success, file-operation, operation-delete, ssh
:From version: 1.6.0
:Description: None









30024
^^^^^


:Message: Failed to delete "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, operation-delete, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.











30025
^^^^^


:Message: Renaming "%(from)s" to "%(to)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :from: Current file/folder path.


  :path: Future file/folder path.


  :to: Future file/folder path.











30026
^^^^^


:Message: Successfully rename "%(from)s" to "%(to)s".
:Groups: authenticated, success, file-operation, operation-rename, ssh
:From version: 1.6.0
:Description: None
:Data:
  :from: Old file/folder path.


  :path: New file/folder path.


  :to: New file/folder path.











30027
^^^^^


:Message: Failed to rename "%(from)s" to "%(to)s". %(details)s
:Groups: authenticated, failure, file-operation, operation-rename, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.


  :from: Current file/folder path.


  :path: New file/folder path.


  :to: Future file/folder path.











30028
^^^^^


:Message: Creating folder "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 1.6.0
:Description: None









30029
^^^^^


:Message: Successfully created folder "%(path)s".
:Groups: authenticated, success, file-operation, operation-create-folder, ssh
:From version: 1.6.0
:Description: None









30030
^^^^^


:Message: Failed to create folder "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, operation-create-folder, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.











30031
^^^^^


:Message: Deleting folder "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 1.6.0
:Description: None









30032
^^^^^


:Message: Successfully delete folder "%(path)s".
:Groups: authenticated, success, file-operation, operation-delete, ssh
:From version: 1.6.0
:Description: None









30033
^^^^^


:Message: Failed to delete folder "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, operation-delete, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.











30034
^^^^^


:Message: Getting attributes for "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 1.6.0
:Description: None









30035
^^^^^


:Message: Successfully got attributes for "%(path)s".
:Groups: authenticated, success, file-operation, ssh
:From version: 1.6.0
:Description: None









30036
^^^^^


:Message: Failed to get attributes for "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.











30037
^^^^^


:Message: Setting attributes for "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 1.6.0
:Description: None









30038
^^^^^


:Message: Successfully set attributes for "%(path)s".
:Groups: authenticated, success, file-operation, ssh
:From version: 1.6.0
:Description: None









30039
^^^^^


:Message: Failed to set attributes for "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.











30040
^^^^^


:Message: Close file "%(path)s" for failed %(mode)s transfer. Read %(total_read)s bytes at %(read_speed)s bytes/second and wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, failure, failure-specific, file-operation, ssh
:From version: 3.40.0
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


:Message: Close file "%(path)s" for failed read transfer. Read %(total_read)s bytes at %(read_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, failure, failure-specific, file-operation, operation-read, ssh
:From version: 3.40.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,











30042
^^^^^


:Message: Close file "%(path)s" for failed write transfer. Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, failure, failure-specific, file-operation, operation-write, ssh
:From version: 3.40.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











30043
^^^^^


:Message: Successfully opened "%(path)s" in "%(mode)s" mode, requested as "%(requested_path)s".
:Groups: authenticated, success, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :mode: Open mode requested for the file


  :path: Virtual path of the opened file.


  :requested_path: The path as it was requested by the client.











30044
^^^^^


:Message: Failed to open "%(path)s" in "%(mode)s" mode, requested as "%(requested_path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :mode: Open mode requested for the file


  :requested_path: The path as it was requested by the client.











30045
^^^^^


:Message: Failed to read from file "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.











30046
^^^^^


:Message: Failed to write to file "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.











30047
^^^^^


:Message: Failed to close file "%(path)s" after opening for %(mode)s. Read %(total_read)s at %(read_speed)s and wrote %(total_write)s at %(write_speed)s in %(duration)s seconds. %(details)s
:Groups: authenticated, failure, failure-high, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :mode: Mode in which the file was opened.











30048
^^^^^


:Message: SFTP request not supported. %(details)s
:Groups: authenticated, failure, ssh
:From version: 5.3.0
:Description: None









30049
^^^^^


:Message: Could not read SSH key received from client. %(details)s
:Groups: operational, session, failure, ssh
:From version: 2.10.0
:Description: None









30050
^^^^^


:Message: Disconnecting the SSH connection. %(details)s
:Groups: authenticated, failure, ssh
:From version: 1.8.0
:Description: None









30051
^^^^^


:Message: New client connection denied. Too many concurrent SSH connections.
:Groups: session, failure, failure-specific, ssh
:From version: 1.8.0
:Description: None









30052
^^^^^


:Message: Failed to handle SFTP command %(command)s. %(details)s
:Groups: session, failure, failure-critical, ssh
:From version: 5.3.0
:Description: None









30053
^^^^^


:Message: Reading link for "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 2.4.0
:Description: None









30054
^^^^^


:Message: Successfully read link for "%(path)s".
:Groups: authenticated, success, file-operation, ssh
:From version: 2.4.0
:Description: None









30055
^^^^^


:Message: Failed to read link for "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 2.4.0
:Description: None
:Data:
  :details: More details about the failure.











30056
^^^^^


:Message: Making link for "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 2.4.0
:Description: None









30057
^^^^^


:Message: Successfully made link for "%(path)s".
:Groups: authenticated, success, file-operation, ssh
:From version: 2.4.0
:Description: None









30058
^^^^^


:Message: Failed to make link for "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 2.4.0
:Description: None
:Data:
  :details: More details about the failure.











30059
^^^^^


:Message: Extended requests are not supported by the SFTP protocol.
:Groups: authenticated, failure, failure-specific, ssh
:From version: 2.4.0
:Description: None









30060
^^^^^


:Message: Canonical file name requested for "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 2.4.0
:Description: None









30061
^^^^^


:Message: Failed to get attributes for opened file "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 2.4.0
:Description: None
:Data:
  :details: More details about the failure.











30062
^^^^^


:Message: Setting attributes on opened files not implemented for "%(path)s".
:Groups: authenticated, failure, file-operation, ssh, failure-specific
:From version: 2.4.0
:Description: None









30063
^^^^^


:Message: Fail to send data to peer. Closing SSH session. %(details)s
:Groups: authenticated, failure, failure-critical, ssh
:From version: 5.3.0
:Description: None









30064
^^^^^


:Message: SCP session closed.
:Groups: authenticated, informational, ssh
:From version: 2.5.0
:Description: None









30065
^^^^^


:Message: Internal error. Failed to process the SCP request. %(details)s
:Groups: operational, authenticated, failure, failure-critical, ssh
:From version: 2.5.0
:Description: None









30066
^^^^^


:Message: Failed to process '%(command)s' command request. %(details)s
:Groups: operational, authenticated, failure, failure-critical, ssh
:From version: 3.45.0
:Description: None
:Data:
  :command: Name of the requested command.











30067
^^^^^


:Message: Close file "%(path)s" after successful read. Read %(total_read)s bytes at %(read_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, success, file-operation, operation-read, ssh
:From version: 3.7.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :mode: Mode in which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,











30068
^^^^^


:Message: Close file "%(path)s" after successful write. Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, success, file-operation, operation-write, ssh
:From version: 3.7.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :mode: Mode in which the file was opened.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











30069
^^^^^


:Message: Authentication requested for username with invalid encoding "%(username)s".
:Groups: session, failure, ssh, failure-specific
:From version: 3.20.0
:Description: None
:Data:
  :username: Raw value of the requested username.











30070
^^^^^


:Message: Authentication requested with a password with invalid encoding.
:Groups: session, failure, failure-specific, ssh
:From version: 3.20.0
:Description: None









30071
^^^^^


:Message: Invalid remote SSH server identity for location %(name)s. Configured "%(expected_fingerprint)s", remote sent "%(actual_fingerprint)s". 
:Groups: session, failure, failure-critical, failure-specific, ssh, client-side
:From version: 2.9.0
:Description: None
:Data:
  :actual_fingerprint: Fingerprint received from the remote server.


  :expected_fingerprint: Configured fingerprint.


  :name: Name of the location associated with this event











30072
^^^^^


:Message: Location %(name)s connected to the SSH server.
:Groups: session, informational, ssh, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the location associated with this event











30073
^^^^^


:Message: Connection to SSH server "%(server_version)s" was lost for location %(name)s. Protected using host-key:%(host_key)s key-exchange:%(key_exchange)s in-hmac:%(in_hmac)s in-cipher:%(in_cipher)s out-hmac:%(out_hmac)s out-cipher:%(out_cipher)s
:Groups: session, informational, ssh, client-side
:From version: 3.0.0
:Description: None
:Data:
  :host_key: Host key algorithm in used to identify the server-side.


  :in_cipher: Cipher used for received data.


  :in_hmac: Hash-based message authentication code for received data.


  :key_exchange: Key exchange algorithm used by the connection.


  :name: Name of the location associated with this event


  :out_cipher: Cipher used for sent data.


  :out_hmac: Hash-based message authentication code for sent data.


  :server_version: The SSH product detected on the server.











30074
^^^^^


:Message: Ignoring setting attributes for opened file "%(path)s".
:Groups: authenticated, failure, file-operation, ssh, failure-specific
:From version: 3.51.0
:Description: None









30076
^^^^^


:Message: Client SFTP started for "%(name)s" using "%(credentials_type)s".
:Groups: authenticated, informational, ssh, client-side
:From version: 3.0.0
:Description: None
:Data:
  :credentials_type: The type of authenticated used. (Since 4.27.0)


  :name: Name of the location associated with this event











30077
^^^^^


:Message: Client SFTP subsystem closed for location %(name)s.
:Groups: authenticated, informational, ssh, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the location associated with this event











30078
^^^^^


:Message: Failure while authenticating the SFTP client for "%(name)s" using methods: %(methods)s. %(details)s
:Groups: operational, session, ssh, failure, failure-high, client-side
:From version: 3.0.0
:Description: None
:Data:
  :methods: List with all methods tried to authenticate.


  :name: Name of the location which failed at the authentication process.











30079
^^^^^


:Message: SSH Banner received: %(message)s
:Groups: session, informational, ssh, client-side
:From version: 3.29.0
:Description: None
:Data:
  :message: The message sent by the server.











30080
^^^^^


:Message: SSH rekey successfully completed.
:Groups: session, informational, ssh, client-side
:From version: 3.31.0
:Description: None









30081
^^^^^


:Message: Successfully got attributes for opened file "%(path)s".
:Groups: authenticated, informational, file-operation, ssh
:From version: 3.51.0
:Description: None









30082
^^^^^


:Message: Remote client disconnected %(code)s:%(details)s.
:Groups: authenticated, informational, ssh
:From version: 5.0.0
:Description: None









30083
^^^^^


:Message: Remote server disconnected %(code)s:%(details)s.
:Groups: authenticated, informational, ssh, client-side
:From version: 5.0.0
:Description: None



















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































HTTP/HTTPS protocol
===================








































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































40000
^^^^^


:Message: Unauthorized request for "%(uri)s". %(details)s
:Groups: session, failure, http
:From version: 1.8.0
:Description: None
:Data:
  :uri: URI for which the request was made.











40001
^^^^^


:Message: Static web resource could not be found: %(uri)s
:Groups: session, informational, http
:From version: 1.8.0
:Description: None
:Data:
  :uri: URI associated with this request.











40002
^^^^^


:Message: Failed to get attributes for "%(path)s". Details: %(details)s
:Groups: authenticated, failure, http, file-operation
:From version: 2.3.0
:Description: None









40003
^^^^^


:Message: Internal error. Failed to retrieve "%(uri)s". %(title)s. %(details)s
:Groups: session, failure, failure-critical, http
:From version: 1.8.0
:Description: None
:Data:
  :title: Name of the error.


  :uri: URI associated with this request.











40004
^^^^^


:Message: Opened file for reading at "%(path)s".
:Groups: authenticated, informational, http, file-operation
:From version: 1.8.0
:Description: None









40005
^^^^^


:Message: HEAD request done for file at "%(path)s".
:Groups: authenticated, informational, http, file-operation
:From version: 1.8.0
:Description: None









40006
^^^^^


:Message: Listing folder at "%(path)s".
:Groups: authenticated, informational, http, file-operation
:From version: 1.8.0
:Description: None









40007
^^^^^


:Message: HTTP/HTTPS file access successfully started in "%(real_path)s" as "%(virtual_path)s".
:Groups: authenticated, informational, http
:From version: 1.8.0
:Description: None
:Data:
  :real_path: Path on the server's filesystem where session was initiated.


  :virtual_path: Path of the folder in the virtual filesystem where sessions was initiated.











40008
^^^^^


:Message: Redirecting from "%(uri)s" to "%(redirect_uri)s".
:Groups: authenticated, informational, http
:From version: 1.8.0
:Description: None
:Data:
  :redirect_uri: New URI where request will redirect.


  :uri: Initial URI request.











40009
^^^^^


:Message: Client HTTPS did not send a valid certificate. "%(details)s".
:Groups: session, failure, http
:From version: 1.8.0
:Description: None









40010
^^^^^


:Message: New folder created at "%(path)s".
:Groups: authenticated, success, http, file-operation
:From version: 2.3.0
:Description: None









40011
^^^^^


:Message: Failed to create new folder "%(path)s". Details: %(details)s
:Groups: authenticated, failure, http, file-operation
:From version: 2.3.0
:Description: None









40012
^^^^^


:Message: Successfully removed file at "%(path)s".
:Groups: authenticated, success, http, file-operation
:From version: 2.3.0
:Description: None









40013
^^^^^


:Message: Failed to remove file at "%(path)s". "%(details)s"
:Groups: authenticated, failure, http, file-operation
:From version: 2.3.0
:Description: None









40014
^^^^^


:Message: Failed to list folder content at "%(path)s". Details: %(details)s
:Groups: authenticated, failure, http, file-operation
:From version: 2.3.0
:Description: None
:Data:
  :details: More details about the error.











40015
^^^^^


:Message: HTTP session timeout after %(timeout)s seconds.
:Groups: authenticated, informational, http
:From version: 5.2.0
:Description: None
:Data:
  :timeout: Number of seconds of inactivity after which the session expired.











40016
^^^^^


:Message: Downloading multiple files as ZIP archive started. Initial requested members: %(initial_count)s.
:Groups: authenticated, informational, http
:From version: 5.4.0
:Description: None
:Data:
  :initial_count: Number of selected files or folders.











40017
^^^^^


:Message: Close successful upload file at "%(path)s". Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, success, http, file-operation
:From version: 2.3.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











40018
^^^^^


:Message: Forcing client disconnection at "%(uri)s" after receiving %(size)s bytes in body. Response: %(code)s %(details)s
:Groups: session, failure, failure-high, http
:From version: 2.3.0
:Description: None
:Data:
  :code: HTTP disconnection response code.


  :message: HTTP response message.


  :size: Received bytes for body content


  :uri: URI for which client was disconnected.











40019
^^^^^


:Message: Bad request for "%(path)s". Requested as "%(uri)s". %(details)s
:Groups: authenticated, failure, http, file-operation
:From version: 2.3.0
:Description: None
:Data:
  :details: More details about the failure.


  :uri: Full URI of the bad request.











40020
^^^^^


:Message: Internal error. Failed initializing request handler. %(details)s
:Groups: session, failure, failure-critical, http
:From version: 2.4.0
:Description: None
:Data:
  :details: Details about the error.











40021
^^^^^


:Message: File opened for writing at "%(path)s". Path requested as "%(requested_path)s.
:Groups: authenticated, informational, http, file-operation
:From version: 2.4.0
:Description: None









40022
^^^^^


:Message: File closed. Failed to upload file at "%(path)s". Path requested as "%(requested_path)s. Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds. %(details)s
:Groups: authenticated, failure, http, file-operation
:From version: 2.4.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.











40023
^^^^^


:Message: Internal error. Failed processing the request for "%(uri)s". %(details)s
:Groups: session, failure, failure-critical, http
:From version: 2.10.0
:Description: None
:Data:
  :tb: Debug information for this error.


  :uri: URI associated with this request.











40024
^^^^^


:Message: Internal error. Failed processing the headers for "%(uri)s". %(details)s
:Groups: session, failure, failure-critical, http
:From version: 2.11.0
:Description: None
:Data:
  :tb: Debug information for this error.


  :uri: URI associated with this request.











40025
^^^^^


:Message: Successful download of multiple files as ZIP archive. Total members: %(count)s.
:Groups: authenticated, success, http
:From version: 5.4.0
:Description: None
:Data:
  :count: Number of files and directories in the archive.











40026
^^^^^


:Message: Successfully removed folder at "%(path)s".
:Groups: authenticated, success, http, file-operation
:From version: 2.11.0
:Description: None









40027
^^^^^


:Message: Failed to remove folder at "%(path)s". "%(details)s"
:Groups: authenticated, failure, http, file-operation
:From version: 2.11.0
:Description: None









40028
^^^^^


:Message: Failed to decode name for file "%(name)s" in "%(operation)s" operation. The request for this file was ignored.
:Groups: authenticated, failure, failure-specific, http
:From version: 2.12.0
:Description: None
:Data:
  :name: Name of the file which failed


  :operation: Name of the file transfer operation











40029
^^^^^


:Message: HTTP/HTTPS connection closed on the server-side due to a failure. "%(details)s"
:Groups: session, failure, http
:From version: 3.6.0
:Description: None









40030
^^^^^


:Message: Folder at "%(path)s" already exist for create request.
:Groups: authenticated, informational, http, file-operation
:From version: 3.0.0
:Description: None









40031
^^^^^


:Message: Client session was re-authenticated since previous credentials were no longer accepted by the server.
:Groups: authenticated, informational, http, client-side
:From version: 3.27.0
:Description: None









40032
^^^^^


:Message: HTTP/HTTPS connection closed on the client-side to %(hostname)s. Session fully established: %(session_established)s
:Groups: authenticated, informational, http, client-side
:From version: 3.27.0
:Description: None
:Data:
  :hostname: Name use to initiate the connection. This can be IP address or FQDN


  :session_established: Whether the connection was established, or the connection was lost during setup.











40033
^^^^^


:Message: HTTP/HTTPS connection created on the client-side as %(hostname)s. Server certificate: %(certificate)s. Used encryption: %(encryption)s.
:Groups: authenticated, informational, http, client-side
:From version: 3.27.0
:Description: None
:Data:
  :certificate: Details for the server's certificate.


  :encryption: Method and cipher used by this connection.


  :hostname: Name use to initiate the connection. This can be IP address or FQDN.











40034
^^^^^


:Message: Successfully listed folder at "%(path)s".
:Groups: authenticated, success, http, file-operation
:From version: 3.28.0
:Description: None









40035
^^^^^


:Message: Failed to open file for reading at "%(path)s". Details: %(details)s
:Groups: authenticated, failure, http, file-operation
:From version: 3.28.0
:Description: None









40036
^^^^^


:Message: HEAD requested for folder at "%(path)s".
:Groups: authenticated, informational, http, file-operation
:From version: 3.29.0
:Description: None









40037
^^^^^


:Message: Closing the HTTP session.
:Groups: authenticated, informational, http
:From version: 3.37.0
:Description: None









40038
^^^^^


:Message: Public access is forbidden. %(details)s
:Groups: session, failure, http
:From version: 3.40.0
:Description: None









40039
^^^^^


:Message: Successfully downloaded file from "%(path)s". Read %(total_read)s bytes at %(read_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, informational, http, file-operation
:From version: 3.46.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,











40040
^^^^^


:Message: File closed. Failed to download file from "%(path)s". Read %(total_read)s bytes at %(read_speed)s bytes/second in %(duration)s seconds. %(details)s
:Groups: authenticated, failure, http, file-operation
:From version: 3.46.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :read_speed: Average bytes / second read.


  :total_read: Total bytes read from the file,











40041
^^^^^


:Message: Failed to download multiple files as ZIP archive. %(details)s
:Groups: authenticated, failure, http
:From version: 3.46.0
:Description: None









40042
^^^^^


:Message: HTTP request failed for %(url)s as part of a redundant request. Will retry after %(retry_interval)s seconds. %(details)s
:Groups: process, operational, failure, failure-high
:From version: 3.51.0
:Description: None
:Data:
  :url: URL which failed.











40043
^^^^^


:Message: Trigger "%(name)s" requested for: %(files)s.
:Groups: authenticated, informational
:From version: 3.54.0
:Description: None
:Data:
  :files: Files for which the trigger was requested.











40044
^^^^^


:Message: Failed to start AS2 receive ID "%(message_id)s" in "%(real_path)s" from "%(as2_from)s" to "%(as2_to)s". MDN: %(mdn_info)s. %(details)s
:Groups: authenticated, failure, http
:From version: 4.5.0
:Description: None
:Data:
  :tb: Details to troubleshoot this issue.











40045
^^^^^


:Message: Started AS2 receive ID "%(message_id)s" in "%(real_path)s" from "%(as2_from)s" to "%(as2_to)s". MDN: %(mdn_info)s. Signed: %(signature)s. Encrypted: %(encryption)s. Compressed: %(is_compressed)s.
:Groups: authenticated, informational, file-operation, http
:From version: 4.5.0
:Description: None









40046
^^^^^


:Message: Successful AS2 receive ID "%(message_id)s" at "%(real_path)s" from "%(as2_from)s" to "%(as2_to)s". MDN: %(mdn_info)s. Signed: %(signature)s %(digest)s. Encrypted: %(encryption)s. Compressed: %(is_compressed)s.
:Groups: authenticated, success, file-operation, http
:From version: 4.5.0
:Description: None









40047
^^^^^


:Message: Failed AS2 receive ID "%(message_id)s" at "%(real_path)s" from "%(as2_from)s" to "%(as2_to)s". MDN: %(mdn_info)s. Signed: %(signature)s %(digest)s. Encrypted: %(encryption)s. Compressed: %(is_compressed)s. %(details)s
:Groups: authenticated, failure, file-operation, http
:From version: 4.5.0
:Description: None









40048
^^^^^


:Message: Failed to start AS2 send ID "%(message_id)s" at "%(real_path)s" from "%(as2_from)s" to "%(as2_to)s". MDN: %(mdn_info)s. Content signature: %(signature)s. Encrypted: %(is_encrypted)s. Compressed: %(is_compressed)s. %(details)s
:Groups: authenticated, failure, file-operation, http
:From version: 4.5.0
:Description: None









40049
^^^^^


:Message: Failed to send AS2 send ID "%(message_id)s" at "%(real_path)s" from "%(as2_from)s" to "%(as2_to)s". MDN: %(mdn_info)s. Content signature: %(signature)s. Encrypted: %(is_encrypted)s. Compressed: %(is_compressed)s. %(details)s
:Groups: authenticated, failure, file-operation, http
:From version: 4.5.0
:Description: None









40050
^^^^^


:Message: Started AS2 send ID "%(message_id)s" at "%(real_path)s" from "%(as2_from)s" to "%(as2_to)s". MDN: %(mdn_info)s. Content signature: %(signature)s. Encrypted: %(is_encrypted)s. Compressed: %(is_compressed)s.
:Groups: authenticated, informational, file-operation, http
:From version: 4.5.0
:Description: None









40051
^^^^^


:Message: Successful AS2 send ID "%(message_id)s" at "%(real_path)s" from "%(as2_from)s" to "%(as2_to)s". MDN: %(mdn_info)s. Content signature: %(signature)s. Encrypted: %(is_encrypted)s. Compressed: %(is_compressed)s.
:Groups: authenticated, informational, file-operation, http
:From version: 4.5.0
:Description: None









40052
^^^^^


:Message: Failed to send AS2 async MDN for ID "%(message_id)s" at "%(real_path)s" from "%(as2_from)s" to "%(as2_to)s". MDN: %(mdn_info)s. Signed: %(signature)s %(digest)s. Encrypted: %(encryption)s. Compressed: %(is_compressed)s. %(details)s
:Groups: authenticated, failure, file-operation, http
:From version: 4.9.0
:Description: None









40053
^^^^^


:Message: HTTP/HTTPS connection created.
:Groups: session, informational, http
:From version: 4.27.0
:Description: None









40054
^^^^^


:Message: HTTP/HTTPS connection closed. Client certificate: %(certificate)s. Used encryption: %(encryption)s. %(details)s
:Groups: session, informational, http
:From version: 4.27.0
:Description: None
:Data:
  :certificate: Certificate sent by the client over the connection.


  :details: Details about the reason the connection was closed.


  :encryption: The cipher suite used to protect the connection.











40055
^^^^^


:Message: Successfully renamed file from "%(from)s" to "%(to)s".
:Groups: authenticated, success, http, file-operation, operation-rename
:From version: 2.3.0
:Description: None
:Data:
  :from: Old file/folder path.


  :path: New file/folder path.


  :to: New file/folder path.











40056
^^^^^


:Message: Failed to rename file from "%(from)s" to "%(to)s". "%(details)s"
:Groups: authenticated, failure, http, file-operation, operation-rename
:From version: 2.3.0
:Description: None
:Data:
  :from: Old file/folder path.


  :path: New file/folder path.


  :to: New file/folder path.











40057
^^^^^


:Message: Internal error during HTTP/HTTP service processing for "%(uri)s". "%(details)s"
:Groups: session, failure, failure-critical
:From version: 4.29.0
:Description: None
:Data:
  :uri: The page that generated this error.











40058
^^^^^


:Message: Failed to read file at "%(path)s". Details: %(details)s
:Groups: authenticated, failure, failure-high, http, file-operation
:From version: 4.35.0
:Description: None









40059
^^^^^


:Message: Failed to write file at "%(path)s". Details: %(details)s
:Groups: authenticated, failure, failure-high, http, file-operation
:From version: 4.35.0
:Description: None











































































































































































































































































































































































































































































































































































































































































































































Management and Web Manager Events
===================================
















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































50000
^^^^^


:Message: Request does not contains an session id.
:Groups: session, failure, failure-specific, local-manager
:From version: 2.1.0
:Description: None









50001
^^^^^


:Message: Authentication failed. %(details)s
:Groups: session, failure, local-manager
:From version: 2.1.0
:Description: None









50002
^^^^^


:Message: Process state read for "%(path)s" from manager API.
:Groups: administration, informational, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :path: The part of the process that was accessed.











50003
^^^^^


:Message: Internal error while applying the requested change from local manager. "%(details)s".
:Groups: administration, failure, failure-critical, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :details: Details about the error.











50004
^^^^^


:Message: Internal JSON-RPC error: %(details)s
:Groups: operational, administration, failure, failure-critical, local-manager
:From version: 2.1.0
:Description: None









50005
^^^^^


:Message: All requested changes successfully applied. Changes: %(changes)s. Results: %(results)s.
:Groups: administration, operational, success, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :changes: List of changes applied.


  :results: List of results after applying changes.











50006
^^^^^


:Message: Not all requested changes successfully applied. Changes: %(changes)s. Results: %(results)s.
:Groups: operational, administration, failure, failure-specific, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :changes: List of changes applied.


  :results: List of results after applying changes.











50007
^^^^^


:Message: %(kind)s administrator "%(name)s" logged in local manager as role "%(role)s".
:Groups: administration, success, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :kind: The type of the authenticated administrator.


  :name: Name of administrator that was authenticated.


  :role: Name of the role associated with this administrator.











50009
^^^^^


:Message: Administrative operation denied. %(details)s
:Groups: administration, failure, local-manager
:From version: 4.15.0
:Description: None









50010
^^^^^


:Message: Administrator logged out from local manager.
:Groups: administration, informational, local-manager
:From version: 2.1.0
:Description: None









50011
^^^^^


:Message: Bad format for requested changes: %(changes)s. %(details)s
:Groups: administration, failure, failure-high, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :changes: Changes are requested by local-manager.











50012
^^^^^


:Message: Failed to apply requested change: "%(details)s".
:Groups: administration, failure, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :details: Details about the error.











50013
^^^^^


:Message: Failed to process action for runnable with UUID %(uuid)s: %(details)s
:Groups: session, failure, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :details: More details about the error.


  :uuid: UUID of the requested runnable.











50014
^^^^^


:Message: Web Manager request failed. %(details)s
:Groups: operational, authenticated, failure, local-manager
:From version: 4.0.0
:Description: None









50015
^^^^^


:Message: Internal error. Failed processing the action for runnable with UUID: %(uuid)s. %(details)s
:Groups: session, failure, failure-critical, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :uuid: UUID of the requested runnable.











50016
^^^^^


:Message: Failed to get content of database "%(database_uuid)s". %(details)s
:Groups: operational, authenticated, failure, failure-high, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :details: Error details.











50017
^^^^^


:Message: Configuration synchronization from node.
:Groups: administration, success, local-manager
:From version: 4.14.0
:Description: None









50018
^^^^^


:Message: Failed to apply the "%(operation)s" configuration change for "%(target)s": %(details)s
:Groups: operational, administration, failure, failure-high, local-manager
:From version: 4.27.0
:Description: None
:Data:
  :operation: The configuration operation that was performed,


  :target: The identification of the component for which the configuration was attempted.











50019
^^^^^


:Message: Failed to get configuration for database "%(database_uuid)s". Source: %(source)s. %(details)s
:Groups: operational, authenticated, failure, failure-high, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :details: Error details.


  :source: Data source name











50020
^^^^^


:Message: Failed to get %(source)s data since database "%(database_uuid)s" is not started.
:Groups: operational, authenticated, informational, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :source: Data source name











50021
^^^^^


:Message: Failed to get data. Unknown source: "%(source)s".
:Groups: operational, authenticated, informational, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :source: Data source name.











50022
^^^^^


:Message: Failed to get %(source)s database configuration for: "%(database_uuid)s".
:Groups: operational, authenticated, informational, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :source: Data source name











50023
^^^^^


:Message: Failed to process the management action. %(details)s
:Groups: operational, authenticated, failure, failure-high, local-manager
:From version: 2.9.0
:Description: None









50024
^^^^^


:Message: Failed to generate SSH key or SSL key/csr. %(details)s
:Groups: operational, authenticated, failure, failure-high, local-manager
:From version: 2.12.0
:Description: None









50025
^^^^^


:Message: Internal error. Failed processing database entries. %(details)s
:Groups: operational, authenticated, failure, local-manager
:From version: 3.0.0
:Description: None









50026
^^^^^


:Message: Successfully generated CSV logs from %(database_uuid)s.
:Groups: operational, authenticated, success, local-manager
:From version: 3.1.0
:Description: None
:Data:
  :database_uuid: UUID of the database.











50027
^^^^^


:Message: Error occurred while generating CSV logs from %(database_uuid)s. %(details)s
:Groups: operational, authenticated, failure, local-manager
:From version: 3.1.0
:Description: None
:Data:
  :database_uuid: UUID of the database.


  :tb: Debug information with the error trace.











50028
^^^^^


:Message: Embedded database "%(db_uuid)s" operation took %(duration)s seconds to retrieve %(size)s results.
:Groups: informational, authenticated, local-manager
:From version: 4.31.0
:Description: None
:Data:
  :db_uuid: UUID of the database.


  :duration: Number of seconds it took to perform the operation.


  :size: Number of rows returned.





































































































































































































































































































































































































































































































































































Transfer and client-side functionality
======================================
























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































60000
^^^^^


:Message: File "%(path)s" was modified in monitored path.
:Groups: transfer, informational, client-side
:From version: 2.6.0
:Description: None.









60001
^^^^^


:Message: File "%(from_path)s" was renamed in monitored path to "%(to_path)s".
:Groups: transfer, informational, client-side
:From version: 2.6.0
:Description: None
:Data:
  :from_path: Initial path.


  :to_path: Final path.











60002
^^^^^


:Message: Command failed: %(details)s
:Groups: authenticated, failure, failure-critical, client-side
:From version: 3.0.0
:Description: None









60003
^^^^^


:Message: File "%(path)s" was created in monitored path.
:Groups: transfer, informational, client-side
:From version: 2.6.0
:Description: None









60004
^^^^^


:Message: File "%(path)s" exists in the monitored path and will be transferred.
:Groups: transfer, informational, client-side
:From version: 3.6.0
:Description: None









60005
^^^^^


:Message: Error occurred while taking a snapshot for "%(path)s". Retrying %(retries_left)s more times after %(delay)s seconds. %(details)s
:Groups: location-operation, failure, client-side
:From version: 3.19.0
:Description: None









60006
^^^^^


:Message: Transfer delayed for "%(path)s". %(details)s
:Groups: transfer, informational, client-side
:From version: 3.36.0
:Description: None
:Data:
  :path: Path to the file for which a transfer was delayed.











60007
^^^^^


:Message: Executing command "%(name)s" for "%(path)s".
:Groups: transfer-job, informational, client-side
:From version: 2.7.0
:Description: None
:Data:
  :destination_path: Path to destination file.


  :source_path: Path to source file.











60008
^^^^^


:Message: Command "%(name)s" was successful for "%(path)s". Output "%(output)s". Error "%(error)s". Exit code "%(exit_code)s".
:Groups: transfer-job, success, client-side
:From version: 2.7.0
:Description: None
:Data:
  :destination_path: Path to destination file.


  :error: Error text produced by the command.


  :exit_code: Exit code of the command


  :output: Output text produced by the command.


  :source_path: Path to source file.











60009
^^^^^


:Message: Command "%(name)s" failed for "%(path)s". Output "%(output)s". Error "%(error)s". Exit code "%(exit_code)s". %(details)s
:Groups: transfer-job, failure, client-side
:From version: 2.7.0
:Description: None
:Data:
  :destination_path: Path to destination file.


  :error: Error text produced by the command.


  :exit_code: Exit code of the command


  :output: Output text produced by the command.


  :source_path: Path to source file.











60010
^^^^^


:Message: Source and destination ready. Start %(transfer_type)s for "%(path)s" with a size of %(size)s bytes. Content action: %(content_action)s.
:Groups: transfer-job, informational, client-side
:From version: 2.9.0
:Description: None
:Data:
  :content_action: The action done to change the content of the file during the transfer.


  :size: Size of the source file in bytes.


  :transfer_type: Describe if this is a upload/push, download/pull or local-to-local transfer.











60011
^^^^^


:Message: Failed to transfer "%(path)s". Will retry %(count)s more. Next try after %(wait)s seconds. %(details)s
:Groups: transfer-job, failure, client-side, file-operation
:From version: 3.0.0
:Description: None
:Data:
  :count: Number of times the transfer will be retried from now on.


  :wait: Number of seconds to wait before retrying.











60012
^^^^^


:Message: Successful %(transfer_type)s for file "%(path)s" to "%(destination_path)s" with a size of %(size)s bytes of which %(transferred_size)s bytes were transferred in %(duration)s seconds at %(speed)s kB/s.
:Groups: transfer-job, success, client-side, file-operation
:From version: 2.9.0
:Description: None
:Data:
  :destination_path: Path on the destination location.


  :source_path: Path on the source location.











60013
^^^^^


:Message: Error occurred while %(transfer_type)s for file "%(path)s" of %(size)s bytes of which %(transferred_size)s bytes were transferred in %(duration)s seconds at %(speed)s kB/s. %(details)s
:Groups: transfer-job, failure, client-side, file-operation
:From version: 2.9.0
:Description: None









60014
^^^^^


:Message: Failed to open source file "%(path)s" for reading. %(details)s
:Groups: transfer-job, failure, client-side, file-operation
:From version: 2.9.0
:Description: None









60015
^^^^^


:Message: Failed to open destination file "%(path)s" for writing. %(details)s
:Groups: transfer-job, failure, client-side, file-operation
:From version: 2.9.0
:Description: None









60016
^^^^^


:Message: Transfer job failed at %(step_name)s after all retries. The following files failed: %(failed_paths)s. The following files succeeded: %(success_paths)s.
:Groups: transfer-job, failure, failure-high, failure-specific, client-side
:From version: 2.9.0
:Description: None
:Data:
  :failed_list: List of paths which failed.


  :failed_paths: Comma separated paths which failed.


  :step_name: Name of the step at which transfer failed.


  :success_list: List of path which were successfully transferred to the destination.


  :success_paths: Comma separated paths which were successfully transferred to the destination.











60017
^^^^^


:Message: Transfer succeeded for source %(paths)s to %(destination_paths)s.
:Groups: transfer-job, success, client-side
:From version: 2.9.0
:Description: None
:Data:
  :destination_paths: List of destination paths which were transferred.


  :paths: Comma-separated source paths which were transferred to the destination.


  :success_list: List of source paths which were transferred.











60018
^^^^^


:Message: Internal error. Failed executing transfer for "%(path)s" at "%(step_name)s". %(details)s
:Groups: transfer-job, failure, failure-critical, client-side
:From version: 2.9.0
:Description: None









60019
^^^^^


:Message: Less than %(minimum_count)s files were successfully transferred in the last %(success_interval)s seconds. Transfer count: %(transfer_count)s.
:Groups: transfer, failure, failure-specific, client-side
:From version: 5.1.0
:Description: None
:Data:
  :minimum_count: The configured minimum transferred files.


  :success_interval: Time interval in seconds used to count the transferred files.


  :transfer_count: Number of files successfully transferred in the configured interval.











60020
^^^^^


:Message: Action "%(action)s" scheduled  in "%(seconds)s" seconds by "%(date)s" for transfer "%(name)s".
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :action: Name of the scheduled action.


  :date: Date and time at which the action was scheduled.


  :name: Name of the transfer for which the action was scheduled.











60021
^^^^^


:Message: Transfer "%(name)s" started in "%(state)s" state.
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the started transfer.


  :state: The name of the state in which the transfer was started.











60022
^^^^^


:Message: Scheduled action "%(action)s" executed for transfer "%(name)s".
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :action: Name of the scheduled action.


  :name: Name of the transfer for which the action was scheduled.











60023
^^^^^


:Message: Transfer "%(name)s" has detected a "%(action)s" action scheduled for "%(expected_date)s", but its execution time has already passed. It was re-scheduled for now.
:Groups: transfer, failure, failure-specific, client-side
:From version: 3.0.0
:Description: None
:Data:
  :action: Name of the scheduled action.


  :expected_date: Date and time at which the action was scheduled in ISO format.


  :name: Name of the transfer for which the action was scheduled.











60024
^^^^^


:Message: Keep alive call failed for resource "%(name)s" . %(details)s
:Groups: authenticated, failure, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the resource for which the keep alive was called.











60025
^^^^^


:Message: Failed to archive "%(path)s" as "%(archive_path)s". %(details)s
:Groups: transfer-job, failure, client-side
:From version: 2.10.0
:Description: None
:Data:
  :archive_path: Destination path of the archive.











60026
^^^^^


:Message: File "%(path)s" was successfully archived as "%(archive_path)s".
:Groups: transfer-job, success, client-side
:From version: 2.10.0
:Description: None
:Data:
  :archive_path: Destination path of the archive.











60027
^^^^^


:Message: Invalid overwrite rule configuration "%(details)s" for transfer "%(name)s".
:Groups: transfer-job, failure, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the transfer with invalid configuration.











60028
^^^^^


:Message: Fail to transfer file "%(path)s" for "%(name)s". File already exists on the destination and transfer is not configured to overwrite it.
:Groups: transfer-job, failure, failure-specific, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the transfer associated with this event.











60029
^^^^^


:Message: Remote file "%(path)s" is going to be overwritten for transfer "%(name)s".
:Groups: transfer-job, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the transfer associated with this event.











60030
^^^^^


:Message: Remote file "%(existing_path)s" was renamed to "%(path)s" to prevent overwriting it for "%(name)s".
:Groups: transfer-job, success, client-side
:From version: 3.0.0
:Description: None
:Data:
  :existing_path: Previous path of the existing file on the destination.


  :name: Name of the transfer associated with this event.


  :path: New path of the existing file, after rename operation.











60031
^^^^^


:Message: File "%(path)s" is going to be transfered as "%(destination_path)s" for "%(name)s" as a file with same name already exists on the destination.
:Groups: transfer-job, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :destination_path: Path on the destination where file will be transferred.


  :name: Name of the transfer associated with this event.











60032
^^^^^


:Message: Start collecting files for batch transfer "%(name)s" with an interval of %(seconds)s seconds starting with "%(path)s".
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the transfer.


  :seconds: Number of seconds used for batch interval.











60033
^^^^^


:Message: Added to the execution queue the %(kind)s transfer for "%(name)s" with %(count)s files: %(files)s.
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :count: Number of files in the batch.


  :files: Human readable list of the scheduled files


  :kind: The type of this transfer


  :name: Name of the transfer.


  :queue: List of the scheduled files











60034
^^^^^


:Message: Canceled execution of batch transfer for "%(name)s" with %(count)s files.
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :count: Number of files in the batch.


  :name: Name of the transfer.











60035
^^^^^


:Message: Closed with success "%(path)s" on "%(location)s" after opening for %(mode)s. Read: %(read_size)s. Write: %(write_size)s
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.











60036
^^^^^


:Message: Closed with failure "%(path)s" on "%(location)s" after opening for %(mode)s. %(details)s
:Groups: failure, failure-high, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.











60037
^^^^^


:Message: Failed to read "%(path)s" on "%(location)s" after opening for %(mode)s. %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.











60038
^^^^^


:Message: Failed to write "%(path)s" on "%(location)s" after opening for %(mode)s. %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.











60039
^^^^^


:Message: Started monitoring "%(path)s" on "%(location)s" (recursive %(recursive)s).
:Groups: success, authenticated, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :recursive: Flag to signal if monitoring is recursive.











60040
^^^^^


:Message: Stopped monitoring "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60041
^^^^^


:Message: Operation to check the existence of "%(path)s" was successful on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60042
^^^^^


:Message: Failed to check that "%(path)s" exists on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60043
^^^^^


:Message: Successfully renamed "%(from)s" to "%(to)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :path: The new name of the file.


  :to: The new name of the file.











60044
^^^^^


:Message: Failed to rename "%(from)s" to "%(to)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :path: The new name of the file.


  :to: The new name of the file.











60045
^^^^^


:Message: Successfully deleted file "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60046
^^^^^


:Message: Failed to delete file "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60047
^^^^^


:Message: Successfully deleted directory (recursive %(recursive)s) "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :recursive: `True` when a recursive request was made











60048
^^^^^


:Message: Failed to delete directory (recursive %(recursive)s) "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :recursive: `True` when a recursive request was made











60049
^^^^^


:Message: Successfully created directory "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60050
^^^^^


:Message: Failed to create directory "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60051
^^^^^


:Message: Successfully listed directory "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60052
^^^^^


:Message: Failed to list directory "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60053
^^^^^


:Message: Successfully opened "%(path)s" for reading on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60054
^^^^^


:Message: Failed to open file "%(path)s" for reading on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60055
^^^^^


:Message: Successfully opened "%(path)s" for writing on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60056
^^^^^


:Message: Failed to open file "%(path)s" for writing on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60057
^^^^^


:Message: Successfully opened "%(path)s" for appending on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60058
^^^^^


:Message: Failed to open file "%(path)s" for appending on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60059
^^^^^


:Message: Successfully touched "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60060
^^^^^


:Message: Failed to touch "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60061
^^^^^


:Message: Successfully copied local "%(path)s" to local "%(to)s" (overwrite %(overwrite)s) on "%(location)s".
:Groups: success, file-operation, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :overwrite: True if copy operation was done with overwrite enabled.


  :path: Old name of the file.


  :to: The new name of the file.











60062
^^^^^


:Message: Failed to copy local "%(path)s" to local "%(to)s" on "%(location)s". %(details)s
:Groups: location-operation, failure, file-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :overwrite: True if copy operation was done with overwrite enabled.


  :path: Old name of the file.


  :to: The new name of the file.











60063
^^^^^


:Message: Sending keep alive call for resource "%(name)s".
:Groups: authenticated, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the resource for which the keep alive was called.











60064
^^^^^


:Message: Executing "%(condition)s" commands on destination for "%(name)s".
:Groups: transfer-job, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :condition: Condition for which the commands are executed.


  :name: Name of the transfer for which the commands are executed.











60065
^^^^^


:Message: Successfully executed "%(condition)s" commands on destination for "%(name)s".
:Groups: transfer-job, success, client-side
:From version: 3.0.0
:Description: None
:Data:
  :condition: Condition for which the commands are executed.


  :name: Name of the transfer for which the commands are executed.











60066
^^^^^


:Message: Failed to execute "%(condition)s" commands on destination for "%(name)s". %(details)s
:Groups: transfer-job, failure, client-side
:From version: 3.0.0
:Description: None
:Data:
  :condition: Condition for which the commands are executed.


  :name: Name of the transfer for which the commands are executed.











60067
^^^^^


:Message: Disconnecting as resource "%(name)s" was idle for %(seconds)s seconds.
:Groups: authenticated, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the resource associated with this event.


  :seconds: Number of seconds after which resource is configured to disconnect on idle.











60068
^^^^^


:Message: Reconnecting as resource "%(name)s" is configured to always keep the connection alive.
:Groups: authenticated, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the resource associated with this event.











60069
^^^^^


:Message: Failed to close source "%(path)s" after failing to open destination "%(destination_path)s". %(details)s
:Groups: transfer-job, file-operation, failure, failure-high, client-side
:From version: 3.12.0
:Description: None
:Data:
  :destination_path: Path of the destination file which failed to be opened.


  :source_path: Path of the source file which failed to be closed.











60070
^^^^^


:Message: Transfer temporarily paused for file "%(path)s" at %(step_name)s as %(location)s is not yet available. All the other files are paused waiting for the location automatic (re)connection.
:Groups: transfer-job, informational, client-side
:From version: 3.10.0
:Description: None









60071
^^^^^


:Message: Successfully got attributes for "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.20.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60072
^^^^^


:Message: Failed to get attributes for "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.20.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.











60073
^^^^^


:Message: Start executing transfer for "%(name)s" with %(count)s files: %(files)s.
:Groups: transfer-job, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :count: Number of files in the batch.


  :files: List of the scheduled files


  :name: Name of the transfer.


  :type: The type of this transfer











60074
^^^^^


:Message: Snapshot with %(total_files)s files and %(total_directories)s directories for "%(path)s".
:Groups: transfer, informational, client-side
:From version: 3.48.0
:Description: None
:Data:
  :path: Path which was listed


  :total_directories: Number of directories which were detected.


  :total_files: Number of files which were detected and were matching the filter.











60075
^^^^^


:Message: Not transferring file "%(path)s" in the monitored path. %(reason)s
:Groups: transfer, informational, client-side
:From version: 4.0.0
:Description: None
:Data:
  :reason: Event which triggered the attempt to transfer this file.











60076
^^^^^


:Message: Skipping source file "%(path)s" as it already exist on destination.
:Groups: transfer-job, informational, client-side
:From version: 4.0.0
:Description: None









60077
^^^^^


:Message: Successfully removed archived file "%(path)s" older than %(days)s days.
:Groups: transfer, informational, client-side
:From version: 3.51.0
:Description: None









60078
^^^^^


:Message: Transfer job canceled for "%(path)s" at "%(step_name)s".
:Groups: transfer-job, failure, failure-specific, client-side
:From version: 4.3.0
:Description: None









60079
^^^^^


:Message: Conflicting content detected for source file "%(path)s". Consider increasing the 'stable_interval' configuration. %(details)s
:Groups: transfer, failure, client-side
:From version: 4.3.0
:Description: None
:Data:
  :reason: Event which triggered the attempt to transfer this file.











60080
^^^^^


:Message: Removing file from transfer queue "%(path)s" as it was removed from the source location.
:Groups: transfer, informational, client-side
:From version: 4.3.0
:Description: None









60081
^^^^^


:Message: Transfer failed for "%(path)s" at "%(step_name)s". %(details)s
:Groups: transfer-job, failure, client-side
:From version: 4.3.0
:Description: None









60082
^^^^^


:Message: Location %(location)s for %(step_name)s is now available to transfer "%(path)s".
:Groups: transfer-job, informational, client-side
:From version: 4.4.0
:Description: None









60083
^^^^^


:Message: Configured "stable_interval" ignored as it is smaller than "changes_poll_interval". %(stable_interval)s seconds used instead.
:Groups: transfer, failure, failure-specific, client-side
:From version: 4.4.0
:Description: None









60084
^^^^^


:Message: Failed to delete parent directory %(path)s for a source file. %(details)s
:Groups: transfer, failure, client-side
:From version: 4.10.0
:Description: None









60085
^^^^^


:Message: Failed to start monitoring "%(path)s" on "%(location)s". Will automatically retry when the location is connected. %(details)s
:Groups: failure, transfer, client-side
:From version: 4.23.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.






























