Explicit FTPS Location
======================

An `explicit ftps location` provides access to an Explicit FTPS server.

..  note::
    The explicit FTPS location is an experimental feature.


address
-------

:Default value: Empty
:Optional: No
:Values: * Host name or IP address of the FTP server.
:From version: 3.13.0
:Description:
    Address of the server. IP or host name.

    In order to check the identity of the remote server the address should
    be provided as FQDN.
    IP addresses are not supported by the server identity validation process.


port
----

:Default value: `21`
:Optional: Yes
:Values: * Number, greater than 0.
:From version: 3.13.0
:Description:
    Port number to connect to the server.


username
--------

:Default value: Empty
:Optional: No
:From version: 3.13.0
:Values: * Text.
:Description:
    Username used to authenticate to the server.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 3.13.0
:Values: * Plain text password.
         * Empty.
:Description:
    This option specifies the password used to connect to the server.

    It is defined in plain text format and sent over the network protected
    by the TLS protocol.

.. include:: /configuration/ssl.include.rst


ftps_ccc
--------

:Default value: Empty
:Optional: Yes
:From version: 3.13.0
:Values: * `Passive`
         * Empty
:Description:
    This option specifies whether the security of the FTPS command connection
    should be downgraded to plain text after authentication.

    Leave it empty to keep the command connection secure.

    When this option is enabled, the SSL/TLS layer is shutdown after
    authenticating.
    The rest of the control channel communication will be done
    over an unencrypted connection.

    For more details about using this configuration option please check the
    dedicated documentation for the :ref:`FTPS CCC modes <operation-ftps-ccc>`.
