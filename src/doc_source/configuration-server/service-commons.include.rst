enabled
-------

:Default value: `Yes`
:Optional: Yes
:Values: * `Yes` - to automatically start the service when the server is
           started.
         * `No` - to leave the service stopped when the server is started.
:From version: 1.6.0
:Description:
    When a service is not automatically started, it can still be manually
    started afterwards from the Web Manager.


name
----

:Default value: ``undefined-service-name``
:Optional: No
:Values: * Any text.
:From version: 2.0.0
:Description:
    Human-readable short string used to identify this service.


type
----

:Default value: ''
:Optional: No
:Values: * `ftp` - for FTP and Explicit FTPS services.
         * `ftpsi` - for Implicit FTPS services.
         * `ssh` - for SSH services providing the SFTP and SCP protocols.
         * `http` - for HTTP services.
         * `http-redirect` - for HTTP Redirection services.
         * `https` - for HTTPS services.
         * `monitor` - for local file system monitor services.
         * `manager` - for Web Manager services.

:From version: 2.10.0
:Description:
    The main option which defines what protocol will be used for this service.

    FTP and Explicit FTPS are using the same `ftp` protocol type, since
    both protocols can be served by the same service.

    ..  note::
        The `sftp` option is also available for backward compatibility, and has
        the same effect as the `ssh` option.


address
-------

:Default value: '127.0.0.1'
:Optional: No
:Values: * Host name resolving to an IPv4 address
         * Fully qualified domain name resolving to an IPv4 address
         * IPv4 address
         * IPv6 address
         * `0.0.0.0`

:From version: 1.7.0
:Description:
    Host name or IP used to listen for incoming connections.

    To accept connections on all available IPv4 interfaces, use the
    `0.0.0.0` address.

    To accept connections on all available IPv6 interfaces, use the
    `::` address.

    ..  note::
        On some operating systems (for example Linux) setting the `address`.
        to `::` will listen to all available IPv6 and IPv4 addresses.

    ..  note::
        This option is ignored for services of type `monitor`.


port
----

:Default value: ''
:Optional: No
:Values: * Port number used for incoming connections.

:From version: 1.7.0
:Description:
    To avoid conflicts between different services on the same local machine,
    this must be a unique port number.
    On Unix-like systems, a root account is usually required for using ports
    below 1024.

    ..  note::
        This option is ignored for services of type `monitor`.


description
-----------

:Default value: ''
:Optional: Yes
:Values: * Any text describing the role of this service.
:From version: 1.8.0
:Description:
    This can be used for attaching notes to a service.


authentications
---------------

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of authentication `UUIDs`.
:From version: 3.2.0
:To version:
:Description:
    Comma-separated list of UUIDs for the authentication methods enabled for
    this service.

    The list should be ordered by priority.
    The service will try to use the first authentication from the list, and
    continue with  the following method if the user is not accepted.

    If this configuration option is empty or is left out the global
    authentication methods are used.

    ..  note::
        This configuration option is ignored for the `monitor` service
        as this service does not authenticate clients.


debug
-----

:Default value: 'No'
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 3.48.0
:Description:
    When enabled, the service will emit events with id `20000`
    containing low-level debug messages for the file transfer protocol.

    Configuration changes are applied only to new connections.
    Existing connections respect the `debug` configuration in use when they
    were initiated.

    ..  warning::
        When this is enabled, emitted events may include used passwords
        in plain text.


idle_connection_timeout
-----------------------

:Default value: `300`
:Optional: Yes
:Values: * Positive number
:From version: 1.7.19
:Description:
    This is defined as the number of seconds after which idle connections are disconnected.

    The service will close the connection if a client connection is idle for a configurable amount of time.
    Any authenticated connections are automatically logged out.

    When set to `0` or a negative number, it will use the default value.


maximum_concurrent_connections
------------------------------

:Default value: `10000`
:Optional: Yes
:Values: * Number of maximum concurrent connections accepted by the service.
         * `0` - To disable the limit.
:From version: 1.7.19
:Description:
    Maximum number of allowed concurrent connections for this service.

    This limit is imposed by each service, and it is not a global
    limit for all services active on the server.
