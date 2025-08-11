headers
^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Single header with a name and at least one value.
         * Multiple headers, each header on a separate line.
:From version: 3.34.0
:Description:
    This configuration option can be used to extend the list of headers
    returned by SFTPPlus for each HTTP response.

    Each line should start with the header name, followed by `:`.
    Each line should end with the header's values.

    For example::

        [services/9ac4-1054-f0e4]
        name = HTTPS File Transfer Service
        type = https
        headers = Strict-Transport-Security: max-age=1607040; includeSubDomains

    You can configure multiple headers by defining each header on a separate
    line.

    Using this configuration option, you can overwrite the `Server` header,
    in order to obscure the identity and/or version of SFTPPlus.

    If your header contains a comma,
    you will need to enclose the whole option in double quotation marks::

        [services/5300-19d0-92ce]
        type = http
        headers = "Keep-Alive: timeout=5, max=100"


accepted_origins
^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Comma-separated values of fully qualified domain names.
         * Comma-separated pairs of FQDN:PORT values.
:From version: 3.41.0
:Description:
    When running behind a load balancer or a reverse proxy,
    you can configure a list of
    domain names handled by the load balancer for which SFTPPlus
    should accept forwarded requests.

    When not using standard ports (80 for HTTP and 443 for HTTPS),
    you will also need to add the port number after the domain name.

    You might see `400 Possible CSRF` errors
    if this configuration is not set,
    as the `same-origin policy` is broken.

    Leave it empty when SFTPPlus is not behind a load balancer.


client_forwarded_header
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * empty.
         * `Forwarded`.
         * `X-Forwarded-For`.
         * Header name.
:From version: 4.14.0
:Description:
    When running behind a load balancer or a reverse proxy, you can configure
    the HTTP header to be parsed for the client's source IP address.

    When left empty, it will use the low-level TCP connection source address
    as the source peer for the authenticated user.
    This is the default value, to be used when clients are connecting
    directly to SFTPPlus server without using any proxy or balancer.

    Set it to `X-Forwarded-For` to extract the source address from the
    `X-Forwarded-For / XFF` header used by many proxies as the de-facto
    standard.
    It expects the proxy header in the following format:
    `X-Forwarded-For: <client>, <proxy1>, <proxy2>` where ``proxy1`` and
    ``proxy2`` are optional.

    The following custom and X-Forwarded-For IP address formats are supported:

    * `1.2.4.5` - IPv4 without port number
    * `1.2.4.5:6789` - IPv4 with port number
    * `2001:db8::8a2e:370:7334` - IPv6 without port number
    * `[2001:db8::8a2e:370:7334]` - IPv6 without port number
    * `[2001:db8::8a2e:370:7334]:1234` - IPv6 with port number
    * `::ffff:192.0.2.128` - IPv4-mapped IPv6 address without a port number
    * `[::ffff:192.0.2.128]:1234` - IPv4-mapped IPv6 address with a port number

    Set it to `Forwarded`, to extract the source address from the
    `Forwarded` header as defined in
    `RFC 7238 section 4 <https://www.rfc-editor.org/rfc/rfc7239#section-4>`_.

    You can set it to any other header name.
    For example, `X-ProxyUser-Ip` is the header used by some Google services,
    while other products might use an `X-Forwarded-Host` header.

    When a header value does not include a port number, port 0 is used
    as a placeholder.

    When a header name is configured and the request is missing that
    header, the request uses the TCP source address.

    If the value of the header is malformed, the request uses the
    TCP source address.

    ..  warning::
        If you are not running SFTPPlus behind a proxy or load balancer,
        leave this configuration empty.

        If you are running behind a proxy or load balancer, make sure clients
        can't bypass the proxy and connect directly to SFPPlus.
        Otherwise, clients would be able to spoof/impersonate their
        source IP addresses.

        If the proxy allows chained proxy requests
        (a client connecting to a proxy that connects to another proxy),
        make sure the closest proxy to SFTPPlus has a trust relation with all
        the other chained proxies.


.. include:: /configuration/ssl.include.rst
.. include:: /configuration/service-commons.include.rst

..  note::
    When clients use a web browser, a single session might generate
    multiple connections (e.g. one for getting the HTML page,
    one for its images, another one for its CSS files, etc.)
    This is why `maximum_concurrent_connections` is not always equal to
    the maximum number of concurrent users/sessions/clients.
