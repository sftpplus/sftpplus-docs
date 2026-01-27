ssl_domains
-----------

:Default value: Empty
:Optional: Yes
:Values: * Fully qualified domain name (FQDN)
         * Comma separated list of fully qualified domain names
         * Empty
:From version: 3.42.0
    This configuration option defines the domain for which SFTPPlus will
    request certificates from the Let's Encrypt server.

    The same domain can be shared by multiple services.

    The domain name is handled as a case-insensitive lower case value.

    You can generate a certificate with multiple domain names
    (Subject Alternative Name - SAN), by defining a comma-separated list of
    domain names.
    The first name from the list is used as the common name of the certificate,
    while the remaining names are used for the SAN extension.

    For this option to be used, you need to define a `lets-encrypt` resource.


tls_private_certificate
-----------------------

:Default value: Empty
:Optional: Yes
:Values: * UUID of a `private-certificates` vault item.
         * Empty
:From version: 5.20.0
:Description:
    The private key and certificate to be used by this component for TLS communication.

    This certificate is sent to the remote peer during the SSL/TLS handshake process.

    When left empty, the default certificate is used.


ssl_certificate_revocation_list
-------------------------------

:Default value: Empty
:Optional: Yes
:Values: * Comma separated list of CRL paths or HTTP URLs.
         * `crl-distribution-points`
         * `${MICROSOFT_IT_CRL}`
         * Empty
:From version: 1.6.0
:Description:
    It defines the locations from where one or more CRLs will be loaded.

    Multiple CRLs are defined as a comma separated list.

    It supports local files with absolute paths,
    in either of the following formats:

    * ``file:///unix/absolute/test-ca.crl``
    * ``file://c:\\windows\\absolute\\test-ca.crl``

    Retrieving the CRL over HTTP is also supported.
    The HTTP request is done using non-persistent HTTP/1.1 connections.
    The URL will look as follows:

    * ``http://example.com/some.crl``

    CRL distribution points (CDP) are supported by using the
    `crl-distribution-points` configuration value.

    When CRL distribution points are configured, the local certificate
    defined at `ssl_certificate` needs to have the CDP extension.
    The CDP advertised in the local certificate is loaded at startup in
    order to validate the configuration.

    The distribution points configuration is mutually exclusive with local
    file or HTTP url configurations.
    When the certificate revocation list is configured to use CDP, all other
    configured CRL location are ignored.

    ..  warning::
        HTTP redirection is not yet supported for CRL URLs.
        You have to configure the exact URL for the CRL.

    Leave it empty to disable certificate revocation checks.

    The certificate revocation list can only be used when the component is
    configured with CA certificates stored in a single file in PEM format.

    When multiple or chained CA certificates are configured the CRL is only
    checked for the peer's certificate and not for the CA certificate or for
    an intermediate CA.

    ..  warning::
        CDP publishing Delta CRL are not supported.

    ..  note::
        If the certificate defines multiple HTTP-based distribution points in
        the CDP extension, only the first HTTP URI is used.
        All non HTTP or the other HTTP URIs are ignored.

    The CRL file should be stored in PEM or DER format.

    ..  note::
        This option is ignored if `ssl_certificate_authority` is not
        enabled.


ssl_certificate_revocation_list_refresh
---------------------------------------

:Default value: `0`
:Optional: Yes
:Values: * Number of seconds
         * `0`
:From version: 2.8.0
:Description:
    This defined the number of seconds after which a configured CRL is
    reloaded by this component.

    When set to `0`, the CRL file is initially loaded at startup and then
    loaded again after the `Next Update` field advertised in the CRL.

    If the *Next Publish* extension is present in the CRL and this option
    is set to `0`, the CRL will be loaded again at the date and time
    specified in the *Next Publish* extension.

    If the CRL does not advertise the *Next Update* field you will have
    to configure a number of seconds after which the CRL should be reloaded,
    otherwise you will get a configuration error.

    For example, a value of `86400` means that the CRL will be re-read
    after one day.

    For more details about the CRL reloading see
    :doc:`the documentation for CRL reloading rules </standards/protocols-overview>`

    ..  note::
        This option is ignored if ``ssl_certificate_authority`` is not
        enabled.


ssl_cipher_list
---------------

:Default value: `secure`
:Optional: Yes
:Values: * List of SSL/TLS ciphers in OpenSSL format.
         * `secure`
:From version: 1.7.4
:Description:
    This defined the list of ciphers accepted by this component while
    communicating over the network.

    The special keyword `secure` contains all the algorithms that we
    currently consider secure.

    Connections are closed if the remote peer has no common cipher in its
    list of configured ciphers.

    When left empty, it will default to the `secure` configuration.

    More information about the accepted values can be found at the
    :doc:`cryptography guide </standards/cryptography>`

    The format for this value is the same as the one used for defining the
    OpenSSL cipher list.
    More information can be found on the `OpenSSL site <https://www.openssl.org/docs/man1.1.1/man1/ciphers.html>`_.


ssl_allowed_methods
-------------------

:Default value: `secure`
:Optional: Yes
:Values: * `secure`
         * `all`
         * `tlsv1.0`
         * `tlsv1.1`
         * `tlsv1.2`
         * `tlsv1.3`
:From version: 1.7.4
:Description:
    This defines the comma-separated list of SSL and TLS methods that are
    accepted by this component during the secure communication handshake.

    Set this to `secure` to allow only the TLS methods that are currently
    considered secure. For now, this is TLS 1.2 and TLS 1.3 but this might
    be changed in the future.
    Any other configured value is ignored.

    Set this to `all` to allow any supported SSL or TLS method.
    Any other configured value is ignored.

    Currently, the following methods are officially supported:

    * `tlsv1` or `tlsv1.0`, which is TLS 1.0.
    * `tlsv1.1`, which is TLS 1.1.
    * `tlsv1.2`, which is TLS 1.2.
    * `tlsv1.3`, which is TLS 1.3.

    ..  note::
        `SSLv3` is still supported, but highly discouraged, due to the SSLv3
        POODLE vulnerability.
        In the case that you need to interact with an old SSL
        implementation that only supports `SSLv3`, it is highly recommended
        to force the usage of the non-CBC cipher `RC4-SHA` by configuring as::

            [services/681f5f5d-0502-4ebb-90d5-5d5c549fac6b]
            ssl_cipher_list = RC4-SHA

    Support for SSLv3 will be removed in future versions.

    SSLv2 is no longer supported since it is not secure.

    In version 2.8.0, the following new methods were added:
    `tlsv1.0` (alias for tlsv1), `tlsv1.1` and `tlsv1.2`

    Support for `tlsv1.3` was added in version 3.47.0.

    Prior to version 4.17.0, this was configured as a space separated value.
