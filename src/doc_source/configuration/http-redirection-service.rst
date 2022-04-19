HTTP Redirection Service
========================

..  contents:: :local:


General description
-------------------

The `http-redirect` service allows to configure an HTTP server with the sole
purpose of redirecting to another service on a different port.

This can be used to redirect HTTP requests to an HTTPS-only file transfer
service.

Below is an example of such a redirection service::

    [services/9ac4-1054-f0e4]
    name = HTTP to HTTPs redirection
    type = http-redirect
    address = 0.0.0.0
    port = 80
    redirect_url = https://your.domain.tld/home/
    headers = Strict-Transport-Security: max-age=1607040; includeSubDomains


Configuration options
---------------------

Below you can find the list of available configuration options.


redirect_url
^^^^^^^^^^^^

:Default value: Empty
:Optional: No
:Values: * Absolute URL
:From version: 3.52.0
:Description:
    This configuration option is used to define the URL to which any request
    made to this service is redirected.


headers
^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Single header with name and value.
         * Multiple headers, each header on a separate line.
:From version: 3.52.0
:Description:
    This configuration option can be used to extend the list of headers
    returned by SFTPPlus for each HTTP response.

    Each line should start with header name , followed by `:`, and ending with
    the header's values.


accepted_origins
^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Comma-separated values of fully qualified domain names.
         * Comma-separated pairs of FQDN:PORT values.
:From version: 3.52.0
:Description:
    When running behind a load balancer, you can configure the list of
    domain names handled by the load balancer for which SFTPPlus
    should accept the forwarded requests.

    Leave it empty when SFTPPlus is not behind a load balancer.
