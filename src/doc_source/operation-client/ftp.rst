FTP/FTPS Client Side Operation Mode
===================================

..  contents:: :local:


Introduction
------------

This page contains information about the usage and behaviour of the FTP
commands implemented by the FTP location/client.

The FTP/FTPS implementation is designed to follow the RFCs as much as possible.

The client-side is designed to work with old and new FTP implementation.
It will use the FEAT command to discover and make use of the advance
functionalities provided by the server.
In the absence of the FEAT command it will assume that the FTP server is a
bare minimum FTP server-side implementation.


FTP command usage
-----------------

Below is the list of FTP commands required to be implemented on the FTP server-side,
for the FTP location to operate:

* USER
* PASS (optional for FTPS, as FTPS can have certificate authentication)
* TYPE I
* PASV
* RETR (required when location is the transfer source)
* LIST (required when location is the transfer source)
* STOR (required when location is the transfer destination)

Below is the list of command required for Implicit FTPS:

* PBSZ
* PROT P

The Explicit FTPS locations requires the same set of commands as for FTP and Implicit FTPS with the addition of:

* AUTH TLS
* CCC (optional)

To transfer a file to a FTP destination with temporary name, these FTP commands are required:

* RNFR
* RNTO

To verity that a file on destination is not overwritten, the following commands are required:

* LIST
* MSLT (if the server supports it, otherwise LIST is used)

The following command are also used by SFTPPlus,
but they are not required.
SFTPPlus will fallback to a default behaviour,
when the server doesn't supports them:

* FEAT
* CLNT - only if advertised in FEAT
* OPTS UTF8 ON - only if advertised in FEAT
* MODE S
* STRU F
* PWD - used to detect remote filesystem separator. defaults to Unix paths.


UTF-8 support
-------------

SFTPPlus will always use the UTF-8 encoding for file names and paths.

The FTP client informs the server about UTF-8 support by sending the
`OPTS UTF8` command, if UTF-8 support is advertised by the server.

If server supports the CLNT command, the client will also issue the `CLNT`
command, before issuing the `OPTS` command.


PASV data channel IP address
----------------------------

The FTP client implementation from SFTPPlus will always use the same IP
address for the command and data channel.

The IP address returned by the PASV command is ignored.

In this way, the PASV command implementation is similar to the
ESPV (Extended PASV) command.


Date and Time
-------------

The FTP protocol, as designed tens of years ago, doesn't include time
zone information or support for detecting the time zone used by the server.

Beside that, the standard LIST command implemented by all FTP servers will
return the date and time in a format which is not defined by the FTP
standard.

For the moment SFTPPlus will assume that the server and client are on the
same timezone.
Due to this, for correct operation the client and server need to have the same
timezone and have the time synchronized.

It will try to extract the date and time from the LIST command, assuming that
it it similar to the result presented by the Unix `ls` command.

When running on Windows, SFTPPlus will not be able to handle
dates before the year 1970 and after the year 2038.


Validating the identity of the remote FTPS server
-------------------------------------------------

It is important to define a certificate authority that is associated
to the peer.
The role of a CA (or certificate authority) is not only to be the issuer
for digital certificates,
but it is also central within the PKI (public key infrastructure) in
building the trust required for both the subject/owner of the certificate
(such as a local peer)
and the recipient/or party that is reliant on the certificate (such as
a remote peer).

Without defining a CA, the trust model is incomplete and the remote serve
certificates are not validated.

To define a certificate authority, the administrator must add the following
to the location configuration::

    [locations/234a-bc34-9812]
    ssl_certificate_authority: path/to/ca-cert.pem
    adderss: same.name-as-CN-or-SAN.tld

Once a CA is defined, SFTPPlus will
check that the certificate presented by the remote peer is signed by the
trusted CA and that the certificate was issued for the
CN or if relevant, the Subject Alternative Name.

Server identity validation is only supported when the server address is
defined as DNS names / FQDN.
It is not supported when the server is defined as an IP address.

On top of that, the certificate is not accepted when outside of its
validity period.

If a certificate revocation list is defined, it will also check whether
the certificate presented by the server was not revoked.
To link a certificate revocation list, please add the following::

    ssl_certificate_revocation_list: path/to/crl-distribution-points
    ssl_certificate_revocation_list_refresh = value


Authenticating FTPS with username and X.509 certificate
-------------------------------------------------------

SFTPPlus can use the username and an X.509 certificate as credentials
during the authentication process.

This assumes that the remote server supports this type of credentials.

For client validation, the client proving its identity to the remote server,
ensure that the client key and certificate specified by the
`ssl_key` and `ssl_certificate` configuration options.

When the SFTPPlus client-side does not send its certificate due to a
misconfiguration, the server-side might not
accept the SSL/TLS connection and will emit an SSL handshake error message.

Once the certificate is accepted as the credential, the configured password is
ignored and not sent to the server.

If the certificate is rejected as the credentials, it will fall back to using
the password credentials and will send the password to the server.


Checking the existence of remote paths
--------------------------------------

For servers which support the `MLST` command as defined in RFC 3659, SFTPPlus
will use the command to determine the existence of remote files and folders.

The `MLST` command provides the best performance as it only uses the
already established command channel.
No new connection or SSL/TLS handshake is required.

When `MLST` is missing, SFTPPlus will use the `LIST` command and check if the
parent folder contains the targeted path.

Without the `MLST` command and with parent folders containing tens of members,
the `exist` operation will be significantly slower.
For each operation a new data channel is created, and for FTPS this means
that a new SSL/TLS handshake is performed.

When the remote server returns the error code `550` SFTPPlus will consider
that the file does not exists.

..  note::
    Most FTP server implementation will return the same error code `550` for
    `Path not found` and `Permission denied` error.
    When listing of the folder is not permitted but file write operation is
    permitted this can lead to the file being overwritten.
    The list operation fails and lets SFTPPlus know that file does not exist,
    but then the write operation will succeed as write is allowed.
