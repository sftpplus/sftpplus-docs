HTTP / HTTPS Service
====================

..  contents:: :local:


General description
-------------------

The `http` / `https` service allows the same level of file access as the
other available file transfer services, such as FTPS or SFTP.

When configured for a ``some.example.com`` address and the ``10080`` port, the
service will be available at the URL ``http://some.example.com:10080``, and it
will redirect users to the start URL ``http://some.example.com:10080/home/``.

As this page focuses on configuration options, please refer to the dedicated
:doc:`HTTP/HTTPS perations</operation/http>` page.


Configuration options
---------------------

Below you can find the list of available configuration options.


headers
^^^^^^^

:Default value: `empty`
:Optional: Yes
:Values: * Single header with name and value.
         * Multiple headers, each header on a separate line.
:From version: 3.34.0
:Description:
    This configuration option can be used to extend the list of headers
    returned by SFTPPlus for each HTTP response.

    Each line should start with header name ending in `:` and followed by the
    header's values.

    For example::

        [services/9ac4-1054-f0e4]
        name = HTTPS File Transfer Service
        type = https
        headers = Strict-Transport-Security: max-age=1607040; includeSubDomains

    You can configure multiple headers by defining each header on a separate
    line.

    Using this configuration option, you can overwrite the `Server` header,
    so that clients will no longer see that the server is an SFTPPlus instance
    or a specific version of SFTPPlus.

    If your header contains a comma,
    you will need to enclose the whole option in double quotation marks.

        [services/5300-19d0-92ce]
        type = http
        headers = "Keep-Alive: timeout=5, max=100"


theme_path
^^^^^^^^^^

:Default value: `empty`
:Optional: Yes
:Values: * Absolute path on local filesystem.
:From version: 3.42.0
:Description:
    Absolute path to a local directory containing the files required to
    customize the HTTP transfer service.

    The folder needs to contain at least the 'main.css' and `main.js` files.

    Leave it empty when you don't want to customize the appearance of the
    HTTP file transfer service.


accepted_origins
^^^^^^^^^^^^^^^^

:Default value: `empty`
:Optional: Yes
:Values: * Comma-separated values of fully qualified domain names.
         * Comma-separated pairs of FQDN:PORT values.
:From version: 3.41.0
:Description:
    When running behind a load balancer, you can configure the list of
    domain names handled by the load balancer for which SFTPPlus
    should accept the forwarded requests.

    When not using standard ports (80 for HTTP and 443 for HTTPS),
    you will also need to add the port number after the domain name.

    You might see `400 Possible CSRF` errors
    if this configuration is not set,
    as the `same-origin policy` is broken.

    Leave it empty when SFTPPlus is not behind a load balancer.


public_account
^^^^^^^^^^^^^^

:Default value: `empty`
:Optional: Yes
:Values: * UUID to application account.
         * Empty.
:From version: 3.40.0
:Description:
    This configuration option can be used to make a set of files available
    over HTTP/HTTPS without requiring an username or password.

    The files for this account will be available under the `/public/` URL.

    Leave it empty to not allow public access.
    Trying to access the '/public/' URL will result in
    `404 Page Not Found` error.

    Credentials will still be required when accessing the '/home/' URL,
    which is dedicated to the private/protected access.

    Using a dedicated application account to configure public access allows
    you to set fine grained access to the public files.
    The public files are not limited to read-only access.

    Only application accounts defined in the main configuration are
    supported.
    OS accounts or external application accounts are not supported.

..  note::
    SSL-specific options are only available for the `https` service type.

..  warning::
    When the `ssl_certificate_authority` configuration option is enabled,
    web browsers should include an SSL certificate signed by the same
    certificate authority.


announce_session_authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `yes`
:Optional: Yes
:Values: * `yes`
         * `no`
:From version: 3.40.0
:Description:
    When set to `no` the session authentication is still available, but it
    will not be advertised as part of the `www-authenticate` header.

.. include:: /configuration/service-http.include.rst
