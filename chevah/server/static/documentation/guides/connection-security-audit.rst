.. container:: tags pull-left

    `server-side`
    `client-side`
    `security`
    `audit`


Auditing the encryption used for FTPS, SFTP, SCP and HTTPS connections
######################################################################

..  contents:: :local:


Introduction
============

This guide describes how you can audit the encryption used for the
client and server side connection protected using TLS and SSH.

The TLS/SSL and SSH are different protocols judging by the low level
technical details, but serve the same purpose and
have similar behavior in terms of cryptographic operations.

They have a similar handshake protocol based on asymmetric cryptography,
encrypting the payload/data in motion using symmetric cryptography.
Both use similar data integrity mechanisms.

For TLS/SSL based file transfer protocols the provided information is:

* TLS/SSL version (TLS1.2 or TLS1.1)
* Cipher and HMAC
* Peer certificate (if any)

For SSH based file transfer protocols the provided information is::

* Host Key algorithm
* Key Exchange algorithm
* Cipher and HMAC

SFTPPlus supports only SSH version 2 which is the latest version and the
version supported and used by all the other SSH implementation.


Start of connection audit
=========================

SFTPPlus will emit events as soon as the connections are made.
These events happen at the very same moment when the connection is done.
At that point, the TLS or SSH handshake has not yet initiated, hence no
cryptography was agreed for that connection.


Start of secure connection audit
================================

All the file transfer protocols will prevent sending any user data before
the encryption handshake was not done.
Username, password, any other credentials and any file transfer data is only
sent after the connection is secured.

As soon as the connection is secured, the file transfer protocol will start
to send sensitive data.
At this point the event will inform the encryption used for the connection.

Here is an example for an Explicit FTPS connection.
The first event which signals that connection is made carried no encryption
information.
Explicit FTPS connections start as clear connection.
Th client will request a secure connection before sending username.
At this point the connection is secured and SFTPPlus will show the
encryption is used by the connection:

    | 10033 2018-02-11 16:38:26 127.0.0.1:32860
      New FTP/FTPS client connection made.
    | 10024 2018-02-11 16:38:27 127.0.0.1:32860
      Initializing secure command channel.
    | 20137 2019-06-18 09:42:36 127.0.0.1:32860
      Account "user" of type "application" from "DEFAULT_GROUP",
      authenticated as "user" by "Application Accounts" of type
      "application" using password.
    | 10059 2019-06-18 09:42:36 127.0.0.1:32860
      User successfully logged on "C:/Users/John_D" as "/".
      Command protected using TLSv1.2 ECDHE-RSA-CHACHA20-POLY1305.
      Client certificate: no certificate


End of connection audit
=======================

SFTPPlus will emit events as soon as the connections are closed.

Depending on previous setup for the the connection,
the emitted event will include information about the ciphers and
cryptographic algorithm used to protect the communication of that connection.

A connection might be closed due to failure to agree on a common encryption
method or because the peer presented cryptographic credentials which were not
trusted.
In such cases, the event will not have any information about the encryption,
as there was no encryption is used.

For example, when the client is required to provide a certificate,
but it does not do so, we can see that TLS 1.2 was used, but `None` is used
for the ciphers since the protocol did not reached cipher negotiation stage:

    | 10042 2018-02-11 16:35:17 127.0.0.1:32832
      Connection on the command channel was closed due to an error.
      Protected using TLSv1.2 None.
      Client certificate: peer did not return a certificate

In all other cases, when the connection is closed after a successful handshake,
the event will include the details of the encryption used.

For example, when no client certificate is required the close event for a
FTPS connection will look like:

    | 10030 2018-02-11 16:38:28 127.0.0.1:32860
      Data connection closed.
      Protected using TLSv1.2 ECDHE-RSA-AES256-GCM-SHA384.
      Received: 0. Sent 1836. 127.0.0.1:34106 - 127.0.0.1:32893 .
      Client certificate: no certificate

A similar event for SFTP protocol will look like:

    | 30015 2018-02-11 16:52:02 127.0.0.1:57060
      SSH connection lost from "SSH-2.0-PuTTY_Release_0.70".
      Protected using host-key:ssh-rsa
      key-exchange:diffie-hellman-group-exchange-sha256
      in-hmac:hmac-sha2-256 in-cipher:aes128-ctr
      out-hmac:hmac-sha2-256 out-cipher:aes128-ctr
