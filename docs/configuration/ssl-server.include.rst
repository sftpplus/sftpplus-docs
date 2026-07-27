tls_active_session_limit
------------------------

:Default value: `7200` (2 hours)
:Optional: Yes
:Values: * Number of seconds greater than or equal to `10`
:From version: 5.24.0
:Description:
    Number of seconds after which an active TLS session is considered expired and a new TLS handshake is required.

    This controls the duration for which new connections can reuse an existing TLS session, which can improve performance by avoiding the overhead of a full TLS handshake for each new connection.

    The minimum value is 10 seconds to prevent performance degradation due to frequent handshakes.

    The maximum value is 604,800 seconds (7 days).


tls_mutual_certification_authorities
------------------------------------

:Default value: Empty
:Optional: Yes
:Values: * Vault item UUID
         * Comma-separated list of vault item UUIDs
         * Empty
:From version: 5.20.0
:Description:
    This is used only for certificate-based peer validation and mutual TLS authentication.

    It's configured with one or multiple `trusted-certificates` vault item UUIDs.

    When mutual TLS is configured for this protocol,
    the SFTPPlus server will enforce two-way SSL/TLS authentication/handshake validation for every incoming connection.

    For a successful connection, make sure the remote peer sends a valid certificate.
    If the connection fails, the event with ID `40054` is emitted.

    Only client connections using certificates signed by one of these trusted certificates are permitted to communicate to this server.

    Leave it empty to disable checking the issuer of the peer's certificates.
    When disabled, connection peers are not required to send a certificate.
    If the peer sends a certificate, it is ignored.
