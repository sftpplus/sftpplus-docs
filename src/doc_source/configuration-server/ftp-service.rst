FTP / Explicit FTPS / Implicit FTPS
===================================

This page describes the configuration options available for the FTP / FTPS
service.

SFTPPlus provides two ways for securing FTP transfers - explicit FTPS and
implicit FTPS.

..  contents:: :local:


Explicit FTPS
-------------

Explicit FTPS is the most widely used method.
The connections for Explicit FTPS are started just like normal FTP connections.
After the initial connection, the FTP client can ask the server to switch to
the secured Explicit FTPS mode.

The Explicit FTPS service can share the same TCP port with the
non-secured FTP service.
This is why the FTP and Explicit FTPS protocols are configured in
SFTPPlus as a single service using the `ftp` protocol.

A single service using the FTP protocol can be configured to allow only
unsecured FTP connections, to allow only secured Explicit FTPS connections, or
to allow both secured and unsecured connections.


Implicit FTPS
-------------

Implicit FTPS is a method in which the client is required to initiate
a connection using an SSL/TLS handshake.
All connections not initiated using an SSL/TLS handshake are dropped.
This does not allow sharing the same TCP port with a non-secured FTP
service, thus the Implicit FTPS service requires a dedicated port.

For more details, please check
`the dedicated FTPS article from Wikipedia
<http://en.wikipedia.org/wiki/FTPS>`_.

.. include:: /configuration-server/service-commons.include.rst


banner
------

:Default value: `Welcome to the FTP service.`
:Optional: Yes
:Values: * Any text message.
:From version: 1.6.0
:Description:
    When FTP/FTPS clients connect to the server, the server will greet them
    with this message.


passive_port_range
------------------

:Default value: All available ports provided by the operating system.
:Optional: Yes
:Values: * A range of port numbers.
         * ``MIN_PORT - MAX_PORT``
         * ``0 - 0`` to use random ports.
:From version: 1.7.0
:Description:
    When FTP/FTPS clients are requesting a passive transfer, the server will
    open a new connection that will be used for sending or receiving files
    from the client.

    By default, the server will use a random port number for the newly
    created connection.

    For example, to set a range of ports starting from 1500 and ending at
    port 2000, set the value to ``1500 - 2000`` like the following example:

        [services/27b8e2b1-7971-416d-af14-6a8aae2ac46e]
        passive_port_range = 1500 - 2000

    To use all available ports, do not define this or set it to ``0 - 0``:

        [services/27b8e2b1-7971-416d-af14-6a8aae2ac46e]
        passive_port_range = 0 - 0


    ..  note::
        `passive_port_range` is designed to help with firewalled
        configurations, but to some extent it is also a mechanism to limit the
        number of concurrent connections to the server.
        While this option is specific to the FTP protocol, there is a generic
        option, `maximum_concurrent_connections`, available to all protocols.


active_source_port
------------------

:Default value: `0`
:Optional: Yes
:Values: * A TCP port number.
:From version: 3.6.0
:Description:
    Source port used by the FTP service to initiate the active
    connections for the PORT or the EPRT requests.

    The source address is the same as address used to listen for incoming
    control connections.

    If you have a set `address` such as::

        [services/27b8e2b1-7971-416d-af14-6a8aae2ac46e]
        address = 0.0.0.0

    And your deployment requires an explicit outbound / outgoing / egress
    interface, you will need to configure an explicit `address` otherwise
    outbound connections will use the source address automatically provided by
    the operating system, based on routing table.

    When set as `0`, a random source port is used.

    ..  note::
        On Unix-like systems, elevated privileges are required to initiate
        connection from source ports below 1024.


passive_address
---------------

:Default value: Empty
:Optional: Yes
:Values: * ``1.2.3.4``
         * Empty.
:From version: 2.9.0
:Description:
    IP address advertised by the FTP service in the passive PASV request.

    When left empty, the service will automatically detect server address.

    When set to a single IP address, it will use that address in all
    PASV requests, regardless of the client's source IP.

    ..  note::
        This option is ignored for EPSV requests.


passive_wait_connection
-----------------------

:Default value: Yes
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 5.9.0
:Description:
    When set to `Yes` or `True`, SFTPPlus FTP/FTPS server will not continue to process further FTP commands,
    unless the FTP client initiates the TCP passive connections.

    SFTPPlus waits for the passive TCP connection in an attempt to improve security by reducing the probability of a 3rd party hijacking the passive connections.

    Some FTP/FTPS clients will try to send the FTP transfer commands before establishing the TCP passive connections.
    This can end up with a deadlock in which the server and client are each waiting for the other part to finalize different actions before continuing.

    Set to `No` or `False` if you observe that the file transfers are blocked with SFTPPlus server waiting for the TCP passive connection to be established.
    This can happen with file transfer clients like Globalscape.


idle_data_connection_timeout
----------------------------

:Default value: `30`
:Optional: Yes
:Values: * An integer value greater than 0, representing seconds.
:From version: 1.8.2
:Description:
    Specifies the timeout, in seconds, after which an inactive data channel is
    disconnected.
    For this number of seconds, the service will only act upon
    the data channel, without disconnecting the command channel.

    When set to 0 or a negative number, the default timeout is used.


.. include:: /configuration/ssl-server.include.rst
.. include:: /configuration/ssl.include.rst


ftps_explicit_enabled
---------------------

:Default value: `Yes`
:Optional: Yes
:Values: * `Yes` - Enable Explicit FTPS protocol.
         * `No` - Disable Explicit FTPS protocol.
:From version: 1.6.0
:Description:
    If the FTPS protocol is disabled, no secured connections are accepted.

    This will only enable Explicit FTPS secure connections, but will not
    enforce clients to use secured connections.
    Dedicated configuration options are provided for this purpose.

    Not available for the Implicit FTPS protocol.

    In SFTPPlus version 4 and older, the default value was `No`.


enable_password_authentication
------------------------------

:Default value: `Yes`
:Optional: Yes
:Values: * `Yes` - Enable password-based authentication.
         * `No` - Disable password-based authentication.
:From version: 1.7.4
:Description:
    Enable authentication based on username and password credentials.


enable_ssl_certificate_authentication
-------------------------------------

:Default value: `Yes`
:Optional: Yes
:Values: * `Yes` - Enable SSL certificate-based authentication.
         * `No` - Disable SSL certificate-based authentication.
:From version: 1.7.4
:Description:
    SSL certificate-based authentication allows clients to authenticate using
    a pair of username and SSL certificate credentials.
    A password is no longer required.

    When the SSL certificate-based authentication is disabled, ensure that
    password-based authentication is enabled, otherwise clients will have no
    authentication method available.


ftps_force_secured_command_channel
----------------------------------

:Default value: `Yes`
:Optional: Yes
:Values: * `Yes` - Only allow commands over secured connections.
         * `No` - Allow commands over both secured and unsecured connections.
:From version: 1.6.0
:Description:
    When secure command channel is forced, any attempt to send unencrypted
    commands will be rejected.

    This option will be ignored if Explicit FTPS is not enabled.

    Not available for Implicit FTPS protocol, where secured command
    is always enforced due to protocol specification.

    In SFTPPlus version 4 and older, the default value was `No`.


ftps_require_session_reuse
--------------------------

:Default value: `Yes` (Since 5.0.0)
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 4.35.0
:Description:
        To make sure the data connection is initiated by the same party
        that was previously authenticated over the command channel,
        SFTPPlus will check that the data and command channel have the
        same TLS session.

        When set to `No`, the session validation is skipped.
        It should be disabled only when support for legacy FTPS clients is required.
        When disabling this, make sure your firewall is updated to only allow connections from trusted source IP address.
        If you need to disable this, consider enabling the certificate authority validation for FTPS clients.

        ..  danger::
            When disabled, the security of the data connection is highly decreased.
            A malicious 3rd party could intercept any transferred data.

    This option is ignored for non-FTPS (implicit or explicit) connections.


ignore_ascii_data_type
----------------------

:Default value: `No`
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 3.8.0
:Description:
    This option allows configuring the FTP service to pretend that ASCII
    mode is supported, but to transfer the data in BINARY/IMAGE mode.


ascii_data_type_as_default
--------------------------

:Default value: `No`
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 3.10.0
:Description:
    This option defines whether to use ASCII as the data type for the case in
    which the client does not explicitly ask for specific data type.

    Set it to `Yes` to use ASCII/text as the default data type.

    Set it to `No` to use IMAGE/binary as the default data type.

    ..  note:
        This configuration option is ignored when `ignore_ascii_data_type`
        is set to `Yes` as the FTP service will always operate in
        binary/image mode.
