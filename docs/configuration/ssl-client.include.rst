ssl_certificate_authority
-------------------------

:Default value: `set-on-first-connection`
:Optional: Yes
:Values: * PEM content of a CA chain (Since 3.40.0)
         * PEM content of a pinned public key (Since 5.1.0)
         * Absolute path to a local file
         * `set-on-first-connection` (Since 5.0.0)
         * `pin-public-key` (Since 5.1.0)
         * `${MOZILLA_CA_ROOTS}` (Since 5.0.0)
         * `${GOOGLE_CA_ROOTS}` (Since 5.11.0)
         * `${DIGICERT_CA_ROOTS}` (Since 5.12.0)
         * `${LETS_ENCRYPT_X3_CA}`
         * `${MICROSOFT_IT_CA}`
         * `${GO_DADDY_G2_G1}`
         * `disable-identity-security` (Since 5.0.0)
:From version: 1.6.0
:Description:
    This is used to validate the identity of the remote server.

    Remote server identity can only be validated when the remote address or URL is configured using a fully-qualified domain name.
    IP-based validation would always fail as this is not a method accepted by Certificate Authorities (CAs).

    Configured certificates need to be in PEM format.

    Multiple Certificate Authorities can be configured, one after the other.
    They can be multiple root CAs or intermediate CAs.

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

    This can be defined as an absolute path on the local filesystem to a
    file containing the certificates of the
    Certificate Authorities used to validate the remote peer.

    A series of bundle CAs are distributed with SFTPPlus.
    They can be configured together and mixed with other CA certificates.
    The bundle CAs are available under the following names:

    * `${MOZILLA_CA_ROOTS}` - All the root certification authorities accepted by the Mozilla's CA Certificate Program
    * `${GOOGLE_CA_ROOTS}` - All the root certification authorities handled by Google Trust Services
    * `${LETS_ENCRYPT_X3_CA}` - For Let's Encrypt X3 certificate authority.
    * `${MICROSOFT_IT_CA}` - For all Microsoft IT CA certificates.
    * `${DIGICERT_CA_ROOTS}` - For all Digicert CA certificates.
      used by SharePoint Online and other services provided by Microsoft.
    * `${GO_DADDY_G2_G1}` - For all GoDaddy Certificate Bundles,
      G2 With Cross to G1.

    Only servers using certificates signed by one of the configured Certificate Authorities are allowed to communicate with this client.

    Leave it empty to disable checking the identity of the remote server.
