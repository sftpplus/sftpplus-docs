Explicit FTPS
=============

An `ftps` location provides access to an Explicit FTPS server.

..  contents:: :local:

.. include:: /configuration-client/locations-commons.include.rst

.. include:: /configuration-client/ftp.include.rst


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

.. include:: /configuration/ssl.include.rst
