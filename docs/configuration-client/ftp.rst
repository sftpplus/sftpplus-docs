FTP
===

..  contents:: :local:


Introduction
------------

An `ftp` location provides access to an FTP server over the unencrypted mode.

This page is a reference documentation for the configuration options available for connecting to an FTP server.

For more information about how to implement FTP based transfers,
see the separate documentation page for :doc:`implementing FTP transfers</operation-client/ftp>`.

Check the separate reference documentation for
:doc:`FTP Explicit</configuration-client/ftps-explicit>`
and :doc:`FTP Implicit</configuration-client/ftps-implicit>` locations.

Only username and password credentials are supported.

..  warning:
    When a FTP location is used, the username and password are sent in
    plaintext over the network.

.. include:: /configuration-client/locations-commons.include.rst

.. include:: /configuration-client/ftp.include.rst
