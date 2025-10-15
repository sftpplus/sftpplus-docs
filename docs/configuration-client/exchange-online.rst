Exchange Online Mailbox
=======================

..  contents:: :local:


Introduction
------------

An `exchange-online` location provides access to an Exchange Online mailbox.

This page is dedicated to the configuration options available for connecting to an Exchange Online mailbox.

For more information about how to implement Exchange Online mailbox based transfers,
see the separate documentation page for :doc:`implementing Exchange Online transfers</operation-client/exchange-online>`.

In order for SFTPPlus to be able to connect to Exchange Online,
SFTPPlus needs to be registered as an application on Entra ID and given permissions to read or write emails.

Check the :doc:`registering SFTPPlus application for Exchange Online </operation-client/exchange-online>` documentation, to find out more about how to configure Entra ID.

.. include:: /configuration-client/locations-commons.include.rst


username
--------

:Default value: Empty
:Optional: No
:From version: 5.4.0
:Values: * Text.
:Description:
    Email address or account for which to check the emails on the remote server.


password
--------

:Default value: Empty
:Optional: No
:From version: 5.4.0
:Values: * OAuth2 client secret
:Description:
    This option specifies the OAuth2 client secret used to authenticate on the remote server.
    The client secret is created from the Entra ID portal, using the App Registration page.


directory_id
------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 5.4.0
:Description:
    Directory (tenant) ID of the SFTPPlus inside the Entra ID.
    This value can be viewed after registering SFTPPlus in Entra ID via the `App registrations` page.


application_id
--------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 5.4.0
:Description:
    Application (client) ID of the SFTPPlus inside the Entra ID.
    This value is obtained after registering SFTPPlus in Entra ID via the `App registrations` page.
