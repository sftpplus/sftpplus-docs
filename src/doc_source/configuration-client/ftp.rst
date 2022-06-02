FTP
===

An `ftp` location provides access to an FTP server over the unencrypted mode.

Only username and password credentials are supported.

..  warning:
    When a FTP location is used, the username and password are sent in
    plaintext over the network.

..  contents:: :local:

.. include:: /configuration-client/locations-commons.include.rst


address
-------

:Default value: Empty
:Optional: No
:Values: * Host name or IP address of the FTP server.
:From version: 3.0.0
:Description:
    Address of the FTP server. IP or host name.


port
----

:Default value: `21`
:Optional: Yes
:Values: * Number, greater than 0.
:From version: 3.0.0
:Description:
    Port number to connect to the FTP server.


username
--------

:Default value: Empty
:Optional: No
:From version: 3.0.0
:Values: * Text.
:Description:
    Username used to authenticate to the FTP server.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 3.0.0
:Values: * Plain text password.
         * Empty.
:Description:
    This option specifies the password used to connect to the FTP server.

    It is defined in plain text format and sent over the network in plain text
    without any transport protection.


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
