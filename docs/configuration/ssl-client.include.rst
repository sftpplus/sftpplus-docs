tls_trusted_certificates
------------------------

:Default value: `set-on-first-connection`
:Optional: Yes
:Values: * Vault item UUID
         * `set-on-first-connection`
         * `pin-public-key`
         * `disable-identity-security`
:From version: 5.22.0
:Description:
    This is used to validate the identity of the remote server.

    Remote server identity can only be validated when the remote address or URL is configured using a fully-qualified domain name.
    IP-based validation would always fail as this is not a method accepted by Certificate Authorities (CAs).

    ..  warning::
        When `disable-identity-security` is set, the identity of the remote server is not validated.
        All remote servers are accepted without validating their TLS/SSL certificates.
        Communication is encrypted and data is protected in transit.
        This can result in an encrypted connection to an unknown server.

    When `set-on-first-connection` is used, the Certificate Authority of the remote server is configured automatically.
    The `set-on-first-connection` configuration value is automatically replaced by the actual CA chain of the remove server on the very first connection.
    For all subsequent connections, the server identity is validated against the automatically configured CA chain.

    When `pin-public-key` is set, SFTPPlus accepts server certificates that have the same public key
    as the one discovered during the first connection to this server.
    This is used to implement certificate and public key pinning.
    SFTPPlus only pins the public key.
    This can be used for self-signed server certificates.

    You can configure the client to validate the server's identity based on
    a fixed list of public keys.
    In this way, you can implement public key pinning.
    When public key validation is used, the public key infrastructure (PKI) certificate policies are not enforced.
    For example, the server certificate is accepted even if it's expired or issued for a different hostname.

    Only servers using certificates signed by one of the configured Certificate Authorities are allowed to communicate with this client.
