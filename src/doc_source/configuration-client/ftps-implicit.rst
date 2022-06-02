Implicit FTPS
=============

An `ftpsi` location provides access to an Implicit FTPS server.

..  contents:: :local:

.. include:: /configuration-client/locations-commons.include.rst


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

:Default value: `990`
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
         * Empty
:Description:
    This option specifies the password used to connect to the server.

    It is defined in plain text format and sent over the network protected
    by the TLS protocol.


debug
-----

:Default value: 'No'
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 4.0.0
:Description:
    When enabled, the location will emit events with id `20000`,
    containing low-level debug messages for the file transfer protocol.

    ..  warning::
        When this is enabled, emitted events may include used password
        in plain text.


.. include:: /configuration/ssl.include.rst
