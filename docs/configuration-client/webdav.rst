WebDAV / SharePoint On-Premise
==============================

..  contents:: :local:


Introduction
------------

A `webdavs` location provides access to a WebDAV server over a protected HTTPS
connection.

On-premise, self-hosted, SharePoint servers are supported.
Only username and password credentials are supported to authenticate against
the WebDAV server.

It is assumed that the WebDAV server handles the path in a case-insensitive
manner.
Please get in touch if your WebDAV server is case-sensitive.

Unlike a web browser, to protect the HTTPS connection you will have to
explicitly configure the list of trusted CA and the location of the CRLs.

For Azure Cloud SharePoint Online sites,
check the :doc:`documentation for the dedicated sharepoint-online location. </operation-client/sharepoint-online>`

This page is a reference for the configuration options available
for a `webdavs` location.

.. include:: /configuration-client/locations-commons.include.rst


url
---

:Default value: Empty
:Optional: No
:Values: * URL
:From version: 4.11.0
:Description:
    Full URL address of the WebDAV server root page.

    For SharePoint Online you can define it as::

        url = https://YOUR-SITE.sharepoint.com

    For generic WebDAV servers you can define it as::

        url = https://files.example.com
        or
        url = https://files.example.com/path/webdav/resource

    Or if you need a custom port number use::

        url = https://files.example.com/path/webdav/resource

    When this is defined as an `http://` URL, the SSL configuration options
    are ignored.


username
--------

:Default value: Empty
:Optional: No
:From version: 3.20.0
:Values: * Text.
:Description:
    Username used to authenticate to the WebDAV server.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 3.0.0
:Values: * Plain text password.
         * Empty.
:Description:
    This option specifies the password used to connect to the WebDAV server.

    It is defined in plain text format and sent over the network protected
    by the HTTPS connection.


proxy
-----

:Default value: Empty
:Optional: Yes
:Values: * `URI` like expression.
         * `connect://12.342.421.2:3128`
         * `disabled` (since 5.14.0)
:From version: 3.20.0
:Description:
    This configuration adds the proxy used to connect to the final URL.

    For now, only the HTTP/1.1 CONNECT tunneling proxy method is supported.

    Leave it empty to use the general proxy configuration.

    Set to `disable` to disable using a proxy.


authentication_method
---------------------

:Default value: 'sharepoint-online'
:Optional: Yes
:Values: * `sharepoint-online`
         * `basic-authentication-scheme`
:From version: 4.12.0
:Description:
    The authentication method to use for connecting to the WebDAV server.

    The default value of `sharepoint-online` is used for the
    Microsoft SharePoint Online cloud service authenticated
    via the Microsoft single sign-on process.

    Another supported method is `basic-authentication-scheme`,
    the HTTP "Basic" access authentication, as per
    `RFC 7617 <https://tools.ietf.org/html/rfc7617>`_.


allow_insecure_http
-------------------

:Default value: 'No'
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 4.12.0
:Description:
    When set to `Yes`, the WebDAV connection is made via insecure HTTP
    instead of HTTPS.

    ..  warning::
        This is useful for testing or troubleshooting,
        but is strongly discouraged in production,
        because it sends all communication including passwords and data
        as plaintext over the network.


.. include:: /configuration/ssl-client.include.rst
.. include:: /configuration/ssl.include.rst
