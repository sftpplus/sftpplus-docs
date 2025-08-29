.. _events-operation:


Operation events
================


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





20018
^^^^^

:Message: Failed to reload the signature keys. %(details)s.
:Groups: operational, process, failure, failure-critical
:From version: 5.14.0
:Description: None



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
:Groups: authentication, session, failure, failure-specific
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
:Description: Generated when failing to validate the certificate of the peer.
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





20044
^^^^^

:Message: Content rule triggered for %(path)s. %(rule_details)s
:Groups: operational, authenticated, success
:From version: 5.16.0
:Description: The event handler was triggered for a file that has a content matching one of the configured rules.
:Data:
  :path: Path of the file that triggered the event


  :rule_details: Details of the rule for which the content was matched.





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
:Groups: analytics, process, informational
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
:Groups: analytics, process, failure
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
:Groups: analytics, process, failure, failure-high
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





20113
^^^^^

:Message: Failed to read ingress JSON events. %(details)s
:Groups: operational, authenticated, failure, failure-high
:From version: 5.12.0
:Description: None



20114
^^^^^

:Message: Certificate warning for %(component_name)s. Expires in %(expires_in_days)s days. %(details)s
:Groups: operational, process, failure, failure-high
:From version: 5.12.0
:Description: None
:Data:
  :component: Component associated with the certificate


  :expires_in_days: Number of days for which the certificate is still valid.


  :name: Name of the component associated with thie certificate.





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





20118
^^^^^

:Message: Failed to send events to remote controller. Will retry in %(interval)ss. %(details)s
:Groups: operational, session, failure, failure-high
:From version: 5.12.0
:Description: None



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
:Groups: authentication, session, failure
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
:Groups: authentication, authenticated, informational
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
:Groups: operational, session, failure, failure-high
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

:Message: Authentication rejected by "%(method_name)s" for the account "%(username)s" using %(credentials_type)s. %(details)s
:Groups: authentication, session, failure, failure-high
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
:Groups: component-activation, authenticated, success
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
:Groups: component-activation, authenticated, success
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
:Groups: component-activation, authenticated, failure
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
:Groups: component-activation, authenticated, failure
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
:Groups: analytics, failure, process, failure-high
:From version: 4.24.0
:Description: Emitted when failed to perform a transfer analytics operation.



20192
^^^^^

:Message: Last day client-side transfer statistics. Successful files %(success_files)s, retried files %(retried_files)s, success jobs %(success_jobs)s, failed jobs %(failure_jobs)s, total size %(total_size)s bytes, total duration %(total_duration)s seconds.
:Groups: analytics, informational, process, client-side
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
:Groups: analytics, process, success
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
:Groups: analytics, process, failure, failure-specific
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


