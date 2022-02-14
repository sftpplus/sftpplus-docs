ssl_domains
^^^^^^^^^^^

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


ssl_certificate
^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
         * Certificate in PEM text format (Since 3.40.0).
         * Certificate in PKCS12 / PXF binary format (Since 4.0.0).
         * Empty
:From version: 1.6.0
:To version: None
:Description:
    This can be defined as an absolute path on the local filesystem
    to the file containing the SSL certificate or chain of certificates
    used by the component.

    File content should be encoded in the Privacy-Enhanced Mail (PEM) or
    PKCS12 / PFX formats.

    File extension should be `.p12` or `.pfx` for the file to be recognized
    as a PCKS-12 certificate.
    The password for the PCKS12 / PFX certificate should be set in the
    `ssl_key_password` configuration option.

    ..  note::
        The path should not be longer than 256 characters.

    You can also define the content of the certificate as text in PEM format.
    In this case the configuration will look as in the following example.
    It's important to start each line with at least one space character and
    keep the number of leading spaces constant::

        ssl_certificate = -----BEGIN CERTIFICATE-----
            MIICaDCCAdGgAwIBAgIBDjANBgkqhkiG9w0BAQUFADBGMQswCQYDVQQGEwJHQjEP
            ...
            MORE CERTIFICATE DATA
            ...
            JZQaMjV9XxNTFOlNUTWswff3uE677wSVDPSuNkxo2FLRcGfPUxAQGsgL5Ts=
            -----END CERTIFICATE-----

    When the value contains both the certificate and the key, the configuration
    will look as in the following example::

        ssl_certificate = -----BEGIN RSA PRIVATE KEY-----
            MIICXgIBAAKBgQDOoZUYd8KMYbre5zZIwR+V6dO2+cCYVS46BHbRbqt7gczkoIWh
            ...
            MORE KEY DATA
            ...
            Wh+QF3UArO8r8RYv3HRcnBjrGh+yEK93wIifVNGgy63FIQ==
            -----END RSA PRIVATE KEY-----
            -----BEGIN CERTIFICATE-----
            MIICaDCCAdGgAwIBAgIBDjANBgkqhkiG9w0BAQUFADBGMQswCQYDVQQGEwJHQjEP
            ...
            MORE CERTIFICATE DATA
            ...
            JZQaMjV9XxNTFOlNUTWswff3uE677wSVDPSuNkxo2FLRcGfPUxAQGsgL5Ts=
            -----END CERTIFICATE-----

    This certificate is sent to the remote peer during the SSL/TLS handshake
    process.

    The certificate file can contain both the certificate and the private key,
    in which case you don't need to set the path to the private key.
    Only supported for PEM encoding.

    The certificate file can contain the full chain of certificates.
    The targeted certificate should be first in the file,
    followed by the chained certificates.
    It will advertise the certificate chain in the same order as listed in
    the file.
    Only supported for PEM encoding.
    (Since 3.22.0)

    For server-side components using TLS/SSL secure communication, this
    configuration option is required.
    If no value is defined here, the global `ssl_certificate` value is
    used.

    For the client-side component using TLS/SSL, you can disable sending the
    certificate as part of the handshake, by leaving this configuration
    option empty.


ssl_key
^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
         * Key as PEM text format (Since 3.40.0).
         * Empty
:From version: 1.6.0
:Description:
    This can be defined as an absolute path on the local filesystem to the
    X.509 private key file used by this component.

    File content should be encoded in the Privacy-Enhanced Mail (PEM) format.

    ..  note::
        The path should not be longer than 256 characters.

    When the value is defined as PEM text, the configuration
    will look as in the following example::

        ssl_key = -----BEGIN RSA PRIVATE KEY-----
            MIICXgIBAAKBgQDOoZUYd8KMYbre5zZIwR+V6dO2+cCYVS46BHbRbqt7gczkoIWh
            ...
            MORE KEY DATA
            ...
            Wh+QF3UArO8r8RYv3HRcnBjrGh+yEK93wIifVNGgy63FIQ==
            -----END RSA PRIVATE KEY-----

    If `ssl_certificate` is not defined, any value defined for this
    `ssl_key` configuration is ignored
    and the global `ssl_key` value is used.

    If the value defined in `ssl_certificate` option already contains
    the private key, this option can be omitted by leaving it empty.


ssl_key_password
^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Password as plain text.
         * Empty
:From version: 1.7.19
:Description:
    This is used to define the password of the private key, when the private
    X.509 key is stored as an encrypted file.

    Leave it empty to not use a password for the private key file.


ssl_certificate_authority
^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Absolute path on the local file.
         * Content of the CA chain (Since 3.40.0).
         * `${LETS_ENCRYPT_X3_CA}`
         * `${MICROSOFT_IT_CA}`
         * `${GO_DADDY_G2_G1}`
         * Empty
:From version: 1.6.0
:Description:
    This can be defined as an absolute path on the local filesystem to a
    file containing the certificates of the
    Certificate Authorities used to validate the remote peer.

    This is used only for certificate-based peer validation.
    To add the CA certificate for an SSL certificate for this component,
    simply add it to `ssl_certificate`, possibly together with other
    certificates needed to complete the full chain of certificates.

    The remote peer identity can only be validated when the remote address
    is configured using a fully qualified domain name.
    IP based validation will always fail, this is not a method accepted
    by the public certificate authorities.

    You can define the content of the CA as text in PEM format.

    When the value is defined as PEM text, the configuration
    will look as in the following example::

        ssl_certificate_authority = -----BEGIN CERTIFICATE-----
            MIICaDCCAdGgAwIBAgIBDjANBgkqhkiG9w0BAQUFADBGMQswCQYDVQQGEwJHQjEP
            ...
            MORE CERTIFICATE DATA
            ...
            JZQaMjV9XxNTFOlNUTWswff3uE677wSVDPSuNkxo2FLRcGfPUxAQGsgL5Ts=
            -----END CERTIFICATE-----

    When a certificate authority is defined, this will result
    in initiating the two-way SSL/TLS authentication/handshake validation.
    For a successful connection, make sure the remote peer sends a valid
    certificate.
    If the connection fails, the event with ID `40009` is emitted.

    The certificate authority file should be stored as a file in PEM format.
    For multiple CA, place all certificates in the same file.

    A series of bundle CA are distributed with SFTPPlus.
    They can be configured together and mixed with other CA certificates.
    The bundle CAs are available under the following names:

    * `${LETS_ENCRYPT_X3_CA}` - For Let's Encrypt X3 certificate authority.
    * `${MICROSOFT_IT_CA}` - For all Microsoft IT CA certificates,
      used by SharePoint Online and other services provided by Microsoft.
    * `${GO_DADDY_G2_G1}` - For all GoDaddy Certificate Bundles,
      G2 With Cross to G1.

    To configure a component to accept the remote peer certificates signed by
    Microsoft IT CA, which is the CA used by SharePoint Online,
    you can set the configuration as::

        ssl_certificate_authority = ${MICROSOFT_IT_CRL}

    This defines the path on the local filesystem to a file containing
    the certificate in PEM format for the single certificate authority
    or multiple authorities authorities with which this component
    will communicate.

    Only peer connections using certificates signed by one of
    these certificate authorities will be permitted to communicate to this
    component.

    When this component should communicate with peers holding certificates
    issued by multiple certificate authorities, put each CA certificate in
    PEM format inside a single file.

    Leave it empty to disable checking the issuer of the peer's certificates.

    When certificate authority check is disabled, connection peers are not
    required to send a certificate.
    If the peer sends a certificate, it is ignored.


ssl_certificate_revocation_list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    :doc:`the documentation for CRL reloading rules </guides/security>`

    ..  note::
        This option is ignored if ``ssl_certificate_authority`` is not
        enabled.


ssl_cipher_list
^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^

:Default value: `tlsv1 tlsv1.1 tlsv1.2 tlsv1.3`
:Optional: Yes
:Values: * `tlsv1.0`
         * `tlsv1.1`
         * `tlsv1.2`
         * `tlsv1.3`
:From version: 1.7.4
:Description:
    This defines the space separated list of SSL and TLS methods that are
    accepted by this component during the secure communication handshake.

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
