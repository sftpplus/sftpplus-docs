HTTP web service
================

An `http` authentication method asks a remote HTTP server to authenticate an account and provide the account's configuration.

..  note::
    This authentication method can't be used with the Web Manager services.

To get more details about the request format and the expected result,
see the dedicated
:doc:`HTTP authentication protocol documentation
</developer/http-api-authentication>`.

..  contents:: :local:

..  include:: /configuration-auth/authentication-commons.include.rst


url
---

:Default value: ''
:Optional: No
:Values: * URL
         * Comma separated list of URLs (Since 3.51.0)
:From version: 2.10.0
:Description:
    Full URL of a resource used to authenticate an account.

    You can define a fall-back/redundant URL using a comma separates list of
    URLs.
    The first URL from the list will be used. When failing to get a response
    for the first URL, the remaining URLs are tried.
    Since 3.51.0.


timeout
-------

:Default value: `120`
:Optional: Yes
:Values: * Number of seconds.
:From version: 4.13.0
:Description:
    Duration, in seconds, to wait for a response from the HTTP server.

    If a response is not received during this period, the authentication fails.


username
--------

:Default value: ''
:Optional: yes
:From version: 3.30.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote HTTP server.

    Leave this value empty in order to leave out HTTP Basic authentication.

    This will overwrite any custom `Authorization` header set via the
    `headers` configuration option.

    ..  warning::
        For now, only HTTP Basic authentication is supported.
        This will send the username and password in clear text
        (BASE64 encoded).


password
--------

:Default value: ''
:Optional: Yes
:From version: 3.30.0
:Values: * Plain text password.
         * Empty.
:Description:
    Password associated with the configured `username`.


headers
-------

:Default value: ''
:Optional: Yes
:From version: 4.4.0
:Values: * Header-Name: Header-Value
         * Multiple headers on separate lines
:Description:
    This defines a set of extra headers which are sent with each HTTP request.


test_at_start
-------------

:Default value: `Yes`
:Optional: Yes
:From version: 4.5.0
:Values: * `Yes`
         * `No`
:Description:
    When set to `Yes` it will check at startup that the configured URL
    can be reached and fail to start if the URL is not available to respond
    to authentication requests.


proxy
-----

:Default value: ''
:Optional: Yes
:Values: * `URI` like expression.
         * `connect://12.342.421.2:3128`
:From version: 3.20.0
:Description:
    This configuration adds the proxy used to connect to the final URL.

    For now, only the HTTP/1.1 CONNECT tunneling proxy method is supported.

.. include:: /configuration/ssl-client.include.rst
.. include:: /configuration/ssl.include.rst
