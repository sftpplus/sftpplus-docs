ssl_certificate_authority
-------------------------

:Default value: Empty
:Optional: Yes
:Values: * PEM content of a CA chain (Since 3.40.0)
         * PEM content of a public key (Since 5.1.0)
         * Absolute path to a local file.
         * `${LETS_ENCRYPT_X3_CA}`
         * `${MICROSOFT_IT_CA}`
         * `${GO_DADDY_G2_G1}`
         * Empty
:From version: 1.6.0
:Description:
    This is used only for certificate-based peer validation and mutual TLS
    authentication.

    Configured certificates need to be in PEM format.

    Multiple certificates authorities (CAs) can be configured, one after the other.
    They can be multiple root CAs or intermediate CAs.

    This option can be defined as an absolute path on the local filesystem to a
    file containing the certificates of the
    Certificate Authorities used to validate the remote peer.

    When a certification authority is configured for this server,
    the server will enforce two-way SSL/TLS authentication/handshake validation
    for every incoming connection.

    For a successful connection, make sure the remote peer sends a valid
    certificate.
    If the connection fails, the event with ID `40054` is emitted.

    Only client connections using certificates signed by one of
    these Certificate Authorities is permitted to communicate to this
    server.

    When this server should communicate with peers holding certificates
    issued by different certificate authorities, put all the CA certificates in
    PEM format inside a single file.

    You can configure the server to validate the peer certificates based on
    a fixed list of public keys.
    In this way, you can implement public key pinning.
    When public key validation is used, the public key infrastructure (PKI) certificate policies are not enforced.
    For example, the peer certificate is accepted even if it's expired.
    This is done by configuring the values in PEM public key format.

    Leave it empty to disable checking the issuer of the peer's certificates.
    When certificate authority check is disabled, connection peers are not
    required to send a certificate.
    If the peer sends a certificate, it is ignored.
