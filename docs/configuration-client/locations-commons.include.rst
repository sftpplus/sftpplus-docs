name
----

:Default value: Empty
:Optional: No
:From version: 2.8.0
:Values: * Any text.
:Description:
    Human-readable short text used to identify this location.


description
-----------

:Default value: Empty
:Optional: Yes
:From version: 2.8.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this location.


type
----

:Default value: ''
:Optional: No
:From version: 2.6.0
:Values: * `filesystem` - Local file system.
         * `sftp` - SFTP protocol v3 over SSH v2.
         * `ftp` - FTP protocol without any encryption.
         * `ftpse` - Explicit FTPS protocol.
         * `ftpsi` - Implicit FTPS protocol.
         * `smb` - SMB / Windows Share
         * `as2` - AS2 over HTTP or HTTPS
         * `azure-file` - Azure File Service.
         * `azure-blob` - Azure BLOB Storage.
         * `sharepoint-online` - SharePoint via MS Graph API.
         * `oracle-database` - Oracle Database.
         * `exchange-online` - Microsoft Exchange Online.
         * `http-pull` - HTTP or HTTPS for pulling files.
         * `smtp` - SMTP protocol for sending emails.
         * `webdavs` - WebDAV over HTTPS.

:Description:
    This option specifies the type of the location.
    Each type has a set of specific configuration options


idle_connection_timeout
-----------------------

:Default value: `300`
:Optional: Yes
:From version: 3.0.0
:Values: * Number of seconds
         * 0
:Description:
    This controls the automatic disconnection from the remote server
    after the location has not received any file transfer operation requests for the configured number of seconds.

    Keep-alive command requests are not counted as file transfer operations.
    The connection gets automatically disconnected if keep-alive is the only command requested in the configured interval.

    Disconnected locations automatically reconnect when a new file transfer operation request is made.
    For example, when a new file needs to be transferred to the remote server.

    If the remote peer closes the connection before the configured timeout,
    the connection is left closed.
    It gets automatically reconnected when a new file transfer operation is requested.

    Set to `0` to always keep the connection active,
    by forcing re-connection when the remote server closes the connection.

    ..  note::
        The `idle_connection_timeout` is the maximum number of seconds before closing an idle connection to the server.
        If the remote server decides that the connection is idle and closes the connection,
        SFTPPlus doesn't try to "challenge" the server, leaving the connection closed.
        The connection is automatically reopened next time a file needs to be transferred.


idle_connection_keepalive_interval
----------------------------------

:Default value: `0`
:Optional: Yes
:From version: 3.0.0
:Values: * Number of seconds
:Description:
    Send a keep-alive command every N seconds to avoid having the connection
    disconnected by the other peer due to inactivity.

    Set to `0` to disable keep-alive commands.

    The keep-alive command does not reset the idle connection timeout,


connection_retry_count
----------------------

:Default value: `12`
:Optional: Yes
:From version: 3.9.0
:Values: * Number of retries
:Description:
    Number of times to retry connection to the location, when the
    initial connection fails.

    Set to `0` to not retry.

    When the connection still fails after all the retries,
    the location is marked as `failed` and no re-connections or transfers are attempted.
    An administrator needs to review the error, fix the issue, and manually restart the location.


connection_retry_interval
-------------------------

:Default value: `300`
:Optional: Yes
:From version: 3.9.0
:Values: * Number of seconds
:Description:
    Number of seconds to wait between connection attempts.

    Set to `0` to retry right away without any delay.
