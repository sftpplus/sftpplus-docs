HTTP(S) file download
=====================

The `http-pull` location allows downloading content from a remote HTTP or HTTPS server.
The download is stored in a file.

..  note::
    The `http-pull` location is designed to be used only as the source for a transfer.
    Get in touch if you need to push / upload files to a remote HTTP server.

In the simplest form, this allows to perform an `HTTP GET` request on any URL and store the result into a file.

The location can also pull the content of a remote URL, using a `POST`` or a `PUT` request.
The request can be made with an empty request body, or with a configured content body.
The request can also be made using a set of configurable headers.

For more complex scenarios, SFTPPlus can make the request to an URL,
with the request body based on an arbitrary local file.
The local file acts as the "seed" for the destination file.

This location is designed for remote HTTP servers that don't provide a way to get the list of available files,
and don't have any means to get the attribute of a file, before a download request.
This is why the `source_path` and `source_filter` configuration options are ignored when used for an `http-pull` source location.

For standard HTTP based file transfer protocol, SFTPPlus provides dedicated locations,
such as the WebDav/SharePoint or the Azure Files location.

For authenticating on the remote HTTP server, the `HTTP Basic Auth` method is used.
Get in touch if you need a different authentication method.

Unlike a web browser, to protect the HTTPS connection you will have to
explicitly configure the list of trusted CA and the location of the CRLs.

..  contents:: :local:

.. include:: /configuration-client/locations-commons.include.rst


url
---

:Default value: Empty
:Optional: No
:Values: * text
:From version: 4.23.0
:Description:
    Full URL address of the HTTP server resource or page from where the file content is pulled.

    Or if you need a custom port number use::

        url = https://files.example.com/path/to/resource

    When this is defined as an `http://` URL, the TLS/SSL configuration options are ignored.


username
--------

:Default value: Empty
:Optional: Yes
:From version: 4.23.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote server.
    Leave it empty if the remote server has no authentication.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 4.23.0
:Values: * Plain text password.
         * Empty.
:Description:
    This option specifies the password used to connect to the HTTP server.

    It is defined in plain text format and sent over the network protected
    by the HTTPS connection.


request_method
--------------

:Default value: `GET`
:Optional: Yes
:Values: * `GET`
         * `POST`
         * `PUT`
:From version: 4.23.0
:Description:
    The HTTP method to use when making the request on the remote server.

    You can configure it to values like `POST` or `PUT`.
    The value is case-insensitive.

    When left empty, it will default to `GET`.


request_body
------------

:Default value: `Empty`
:Optional: Yes
:Values: * Any text
         * `seed-file`
:From version: 4.23.0
:Description:
    Content used for the body of the HTTP request sent to the remote server.

    Leave empty to send a request with an empty body.

    When configured to `seed-file` it will make the request with having the body the content of a local file
    detected in the `source_path` configuration of each transfer.

    This configuration is ignored when `request_method` is configured with the `GET` option.


request_headers
---------------

:Default value: `Empty`
:Optional: Yes
:Values: * `HEADER_NAME: HEADER VALUE`
         * Multiple headers, one header per line.
:From version: 4.23.0
:Description:
    The list of headers used for the HTTP request to send to the remote server.

    Leave empty to send a request without extra headers.

    Each header is defined using `NAME: VALUE` format.
    Multiple headers can be defined, one header per line.

    In the example below, 2 extra headers are sent::

        request_headers =
            X-Stream-Type: reports
            Content-Type: application/octet-stream

    The requests will always contain the following standard headers,
    required for basic HTTP operations:

    * `Host`
    * `User-Agent``
    * `Content-Length`
    * `Authorization` (if authentication is enabled)


response_code
-------------

:Default value: `2*`
:Optional: Yes
:Values: * text
         * matching expression
:From version: 4.23.0
:Description:
    The expected HTTP response code for a successful request.

    This is used to detect a failed request and to trigger the retry mechanism.

    It can be configured to a fixed value like `200` or `201`.
    It can also be configured to a matching expressing like `2*` or `200 | 201`,
    for which in the first case it will match any code starting with `2`
    or for the second case,
    it will accept `200` or `201`.

    When the remote server returns a different response code,
    it is considered a failure and the transfer is retried,
    based on the transfer configuration.

    When left empty, it will consider any response a success.


response_file_name
------------------

:Default value: `http-pull.file`
:Optional: Yes
:Values: * fixed text
:From version: 4.23.0
:Description:
    The name of the local file used to store the body of the response,
    when this is used as the source location.

    This option is ignored when the location is used as the destination location.

    It can be a fixed name or a template used to generate dynamic file names.

    For example, when configured below, it will store the content of the `url` as a local file named ``stock-results.xml``::

        response_file_name = stock-results.xml


.. include:: /configuration/ssl-client.include.rst
.. include:: /configuration/ssl.include.rst
