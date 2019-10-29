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


UTF-8 support
-------------

SFTPPlus will always use the UTF-8 encoding for file names and paths.

The FTP client informs the server about UTF-8 support by sending the
`OPTS UTF8` command, if UTF-8 support is advertised by the server.

If server supports the CLNT command, the client will also issue the `CLNT`
command, before issuing the `OPTS` command.


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

When no certificate authority is defined, SFTPPlus will not check the
identity of the remote server.

When a certificate authority is defined for a FTPS server, SFTPPlus will
check that the certificate presented by the server is signed by the trusted
certificate authority and that the certificate was issued for the CN or
Alternate Name matching the name used in the SFTPPlus configuration file.

Server identity validation is only supported when the server address is
defined as DNS names / FQDN.
It is not supported when the server is defined as an IP address.

On top of that, the certificate is not accepted when outside of its
validity period.

If a certificate revocation list is defined, it will also check whether
the certificate presented by the server was not revoked.

When the certificate presented by the server has the Subject Alternative Name
defined, the CN field is ignored.


Authenticating FTPS with username and X.509 certificate
-------------------------------------------------------

SFTPPlus can use the username and an X.509 certificate as credentials
during the authentication process.

This assumes that the remote server supports this type of credentials.

When the certificate is accepted as the credential, the configured password is
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
