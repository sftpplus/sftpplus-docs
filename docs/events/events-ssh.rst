.. _events-ssh:


SFTP / SCP / SSH events
=======================


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

:Message: SSH protocol failure at userauth service for "%(username)s". %(details)s
:Groups: authentication, session, failure, failure-high, ssh
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
:Groups: authentication, authenticated, success, ssh
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
:Groups: session, informational, ssh
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


  :requested_path: The path as it was requested by the client.


  :total_read: Total bytes read from the file.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.





30018
^^^^^

:Message: Internal error. Failure in the SSH userauth service for "%(username)s". %(details)s
:Groups: authentication, session, failure, failure-critical, ssh
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


  :requested_path: The path as it was requested by the client.


  :total_read: Total bytes read from the file.





30042
^^^^^

:Message: Close file "%(path)s" for failed write transfer. Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, failure, failure-specific, file-operation, operation-write, ssh
:From version: 3.40.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :requested_path: The path as it was requested by the client.


  :total_write: Total bytes written to the file.


  :write_speed: Average bytes / second written.





30043
^^^^^

:Message: Successfully opened "%(path)s" in "%(mode)s" mode, requested as "%(requested_path)s".
:Groups: authenticated, success, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :mode: Open mode requested for the file.


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


  :length: Number of bytes that were attempted to be read.


  :offset: Offset in the file where the read was attempted.


  :requested_path: The path as it was requested by the client.





30046
^^^^^

:Message: Failed to write to file "%(path)s". %(details)s
:Groups: authenticated, failure, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :details: More details about the failure.


  :length: Number of bytes that were attempted to be written.


  :offset: Offset in the file where the write was attempted.


  :requested_path: The path as it was requested by the client.





30047
^^^^^

:Message: Failed to close file "%(path)s" after opening for %(mode)s. Read %(total_read)s at %(read_speed)s and wrote %(total_write)s at %(write_speed)s in %(duration)s seconds. %(details)s
:Groups: authenticated, failure, failure-high, file-operation, ssh
:From version: 1.6.0
:Description: None
:Data:
  :mode: Mode in which the file was opened.


  :requested_path: The path as it was requested by the client.





30048
^^^^^

:Message: SFTP request not supported. %(details)s
:Groups: authenticated, failure, ssh
:From version: 5.3.0
:Description: None



30049
^^^^^

:Message: Could not read SSH key received from client. %(details)s
:Groups: authentication, session, failure, ssh
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


  :requested_path: The path as it was requested by the client.





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


  :requested_path: The path as it was requested by the client.


  :total_read: Total bytes read from the file.





30068
^^^^^

:Message: Close file "%(path)s" after successful write. Wrote %(total_write)s bytes at %(write_speed)s bytes/second in %(duration)s seconds.
:Groups: authenticated, success, file-operation, operation-write, ssh
:From version: 3.7.0
:Description: None
:Data:
  :duration: Total time in seconds for which the file was opened.


  :mode: Mode in which the file was opened.


  :requested_path: The path as it was requested by the client.


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
:Data:
  :requested_path: The path as it was requested by the client.





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
