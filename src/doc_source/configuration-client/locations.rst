General Location Options
========================

..  contents:: :local:


Introduction
------------

A location configuration provides the required information to allow
SFTPPlus to connect to local or remote locations in order to perform
file transfers between locations.

Please consult the `type` configuration option to see the list of
supported location types.

Locations are auto-started when a transfer or another component needs them and
the location is not started and connected.

They are also fault-tolerant, allowing retries for interrupted connections.

Transfers using a failed location will also fail and will
not trigger a new connection attempt for the location.
In this type of scenario, the failed location must be manually started first,
after resolving the initial error.


Adding a new location via Local Manager
---------------------------------------

A new location can be added or changed via Local Manager below.
Options will differ depending on which location type is used.

See below for an example of an initial configuration with the FTPES location.

..  image:: /_static/gallery/gallery-add-ftps-location.png


Adding a new location via text configuration
--------------------------------------------

Adding a new location configuration is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``locations/`` and followed by
the location's UUID.

The location's UUID can be any unique string used to identify the location.
Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/general>`.

For example, to add a new location configuration of type `filesystem`
called ``Local file system``::

    [locations/b904e6h6-c295-4ccf-8abd-edcae4d3324f]
    name = Local file system
    description = File system accesses as service account.
    type = filesystem


Location options
----------------

Each location configuration section has the following configurations:


name
^^^^

:Default value: Empty
:Optional: No
:From version: 2.8.0
:Values: * Any text.
:Description:
    Human-readable short text used to identify this location.


description
^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 2.8.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this location.


type
^^^^

:Default value: ''
:Optional: No
:From version: 2.6.0
:Values: * `filesystem` - Local file system.
         * `sftp` - SFTP protocol v3 over SSH v2.
         * `ftp` - FTP protocol without any encryption.
         * `ftpse` - Explicit FTPS protocol.
         * `ftpsi` - Implicit FTPS protocol.
         * `webdavs` - WebDAV over HTTPS.
         * `as2` - AS2 over HTTP or HTTPS
         * `azure-file` - Azure File Service.
         * `smb` - SMB / Windows Share
:Description:
    This option specifies the type of the location.
    Each type has a set of specific configuration options


idle_connection_timeout
^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^

:Default value: `12`
:Optional: Yes
:From version: 3.9.0
:Values: * Number of retries
:Description:
    Number of times to retry connection to the location, when the
    initial connection fails.

    Set to `0` to not retry.


connection_retry_interval
^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `300`
:Optional: Yes
:From version: 3.9.0
:Values: * Number of seconds
:Description:
    Number of seconds to wait between connection attempts.

    Set to `0` to retry right away without any delay.
