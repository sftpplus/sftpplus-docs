idle_connection_timeout
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `300`
:Optional: Yes
:Values: * Number of seconds after which idle connections are disconnected.
         * `0` - To disable timeouts.
         * `Disabled` - To disable timeouts.
:From version: 1.7.19
:To version: None
:Description:
    The service will close the connection if a client connection is idle for
    a configurable amount of time.


maximum_concurrent_connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `10000`
:Optional: Yes
:Values: * Number of maximum concurrent connections accepted by the service.
         * `0` - To disable the limit.
         * `Disabled` - To disable the limit.
:From version: 1.7.19
:To version: None
:Description:
    Maximum number of allowed concurrent connections for this service.

    This limit is imposed by each service, and it is not a global
    limit for all services active on the server.
