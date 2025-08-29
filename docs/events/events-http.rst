.. _events-http:


HTTP / HTTPS / AS2 / REST / Cloud events
========================================


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
:Groups: authentication, authenticated, informational, http
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



40060
^^^^^

:Message: Failed response from API backend for "%(path)s". Details: %(details)s
:Groups: authenticated, failure, failure-high, http, file-operation
:From version: 5.15.0
:Description: None
