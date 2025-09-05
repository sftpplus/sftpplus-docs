.. _events-ftp:


FTP / FTPS events
=================


100
^^^

:Message: Debug message.
:Groups: process, operational, informational
:From version: 1.6.0
:Description: None



1005
^^^^

:Message: Virtual path overlaps an existing file or folder.
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1006
^^^^

:Message: Could not switch process security context. %(details)s.
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1007
^^^^

:Message: Modifying a virtual path is not allowed.
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1008
^^^^

:Message: Could not write PID file at %(path)s.
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1009
^^^^

:Message: Deleting Unix root folder is not allowed.
:Groups: process, operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1013
^^^^

:Message: Failed to remove group "%(group)s" from "%(path)s". %(details)s
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1014
^^^^

:Message: Could not get home folder for user "%(username)s". %(details)s
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1015
^^^^

:Message: Failed to get primary group for user "%(username)s".
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1016
^^^^

:Message: Failed to set owner to "%(owner)s" for "%(path)s". %(details)s
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1017
^^^^

:Message: Failed to add group "%(group)s" for "%(account)s". %(details)s
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



1018
^^^^

:Message: Failed to check that user "%(account)s" exists.  %(details)s
:Groups: operational, failure, failure-high, compat
:From version: 1.6.0
:Description: None



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
:Groups: operational, authenticated, informational, ftp
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
:Groups: authenticated, informational, ftp
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
:Groups: session, informational, ftp
:From version: 1.6.0
:Description: None



10034
^^^^^

:Message: Command connection closed. Protected using %(encryption)s. Client connected with certificate: %(certificate)s
:Groups: authenticated, informational, ftp
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
:Groups: authentication, authenticated, success, ftp
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
:Groups: authenticated, informational, ftp
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
:Groups: authenticated, informational, ftp
:From version: 1.6.0
:Description: None



10066
^^^^^

:Message: Closing current FTP session.
:Groups: session, informational, ftp
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
:Groups: authenticated, informational, ftp
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
:Groups: authenticated, informational, session, ftp
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
:Groups: authentication, authenticated, failure, ftp
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
:Groups: authenticated, informational, ftp
:From version: 4.33.0
:Description: FTP TLS handshake done (server-side).
:Data:
  :certificate: Certificate sent by the client over the command channel.


  :encryption: The cipher suite used to protect the command channel.





10101
^^^^^

:Message: Secure %(channel_type)s channel successfully initialized. Protected using: %(encryption)s. Server certificate: %(certificate)s
:Groups: authenticated, informational, ftp, client-side
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
