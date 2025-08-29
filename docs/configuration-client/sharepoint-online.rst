SharePoint Online Sites
=======================

An `sharepoint-online` location provides access to an SharePoint Online site hosted in Azure cloud.

..  note::
    For on-premise SharePoint sites use the `webdav` location.

..  contents:: :local:


Introduction
------------

This page covers the SFTPPlus configuration options for connecting to an SharePoint Online site.

In order for SFTPPlus to be able to connect to SharePoint Online,
SFTPPlus needs to be registered as an application on Entra ID and given read and write permissions to the specific SharePoint site.

Check the :doc:`registering SFTPPlus application for SharePoint Online </operation-client/sharepoint-online>` documentation, to find out more about how to configure Entra ID and SharePoint Online.

.. include:: /configuration-client/locations-commons.include.rst


url
---

:Default value: Empty
:Optional: No
:From version: 5.16.0
:Values: * URL
:Description:
    Base URL of your SharePoint Online site.

    This can be the root site, like `url = https://sftpplus.sharepoint.com`
    or it can be a sub-site like `url = https://sftpplus.sharepoint.com/sites/test-site`.


password
--------

:Default value: Empty
:Optional: No
:From version: 5.16.0
:Values: * OAuth2 client secret
:Description:
    This option specifies the OAuth2 client secret used to authenticate on the remote server.
    The client secret is created from the Entra ID portal, using the App Registration page.


directory_id
------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 5.16.0
:Description:
    Directory (tenant) ID of the SFTPPlus inside the Entra ID.
    This value can be viewed after registering SFTPPlus in Entra ID via the `App registrations` page.


application_id
--------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 5.16.0
:Description:
    Application (client) ID of the SFTPPlus inside the Entra ID.
    This value is obtained after registering SFTPPlus in Entra ID via the `App registrations` page.
