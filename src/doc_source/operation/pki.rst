.. container:: tags pull-left

    `client-side`
    `server-side`
    `security`


Public Key Infrastructure (PKI)
===============================

..  contents:: :local:


Introduction
------------

This page contains information aimed at SFTPPlus administrators working with
file transfer services or protocols that utilize a Public Key Infrastructure
(PKI).
This page contains a general overview for further understanding of PKI.
For operational details, please consult the section relevant to the
file transfer service.
For further readings on security concepts in relation to PKI, please go to our
:doc:`dedicated section here </guides/security>`.


About PKI
---------

If you are administering services on HTTPS or FTPS, you are already utilizing
the benefits of a PKI.
Such benefits include the ability to create, manage, distribute, use,
store and revoke digital certificates in order to ensure a secure manner of
electronically transferring information.


Establishing trust through public key encryption
------------------------------------------------

Trust in PKI is established by using Public Key Encryption.
In a Public Key Encryption system, each party operates with pairs of keys.
Those keys may be *private* or *public*.
A PKI binds these keys, the public keys, to respective identities such as
individuals, applications, or organizations.
Possession of a private key will prove the identity of the party.
For this reason, a private key should never be shared.

For example, with SFTP services where there is an SSH connection being
established, trust is formed directly by the client accepting the server's
public key.


Establishing trust through X.509 certificates
---------------------------------------------

*X.509 certificates* is the correct terminology to what is
colloquially referred to as SSL certificates.
The term *SSL certificate* became common due to the adoption of the
X.509 certificate format by Netscape when it designed the original version of
the SSL (Secure Socket Layer) protocol.
SSL is now deprecated and replaced by TLS, but use of the term
*SSL certificate* is still common, and will likely persist for the near
future.

In an SSL/TLS connection, trust is established using a trusted third party
(TTP) which is the Certificate Authority (CA).
This is an entity that digitally signs and publishes the public key bound to
a user.
For the case of multiple CAs, the process of certificate chaining,
expanded further in this section, can further establish trust.

In addition, there is also the root certificate which contains the
public key of the CA server and other details such as the serial number,
issuer, thumbprint (fingerprint) algorithm and
fingerprint hash for the certificate,
public key, validity dates, subject and so on.


SSL/TLS host and server validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the FTPS or HTTPS protocol is used, the configured certificate must
be issued with the Subject Alternative Name (`subjectAltName`) or the
Common Name (CN) containing the address used by the HTTPS or FTPS clients to
connect to the server.

Multiple services can share the same set of keys and certificates.

If you have server-side certificates issued with different Common Names (CN),
such as ``CN=acme-test.com`` and ``CN=acme1-test.com``, ensure that there is a
corresponding client certificate for each each of the CNs involved or that the
name of the account is the same as the configured CN.

The port number is not included in SSL/TLS certificate validation.

When validating and troubleshooting SSL/TLS host and server,
check both server-side and client-side error logs as the issue may be on the
client or server-side certificates.
If you only have access to the client-side or the server-side logs,
such as working with external partners, please get in touch with them to
obtain logs from the other side.

When there is an error code and message, the log information corresponds with
the diagnostic information provided by
`OpenSSL <https://www.openssl.org/docs/man1.0.2/apps/verify.html>`_.


Certificate Chaining
--------------------

The X.509 standard used by SSL and TLS includes a model for setting up a
hierarchy of certificate authorities.

At their core, SSL and TLS protocols use X.509 certificates to validate
connection endpoints.
To allow verification of the authenticity of these certificates, they are
digitally signed by a certificate authority (CA).

In a similar manner, a certificate authority's certificate is signed by a
higher level CA which delegates its trust to what is called an
intermediate certificate authority.

This chain of trust can be traced back to a certificate signed by a CA known
as a "Root Certificate Authority".
A Root CA is an authority whose certificate is considered ultimately trusted.

This whole process is called certificate chaining.

Unlike operating systems and browsers, SFTPPlus is not distributed with a
single list of root CAs.

SFTPPlus contains a couple of narrow down lists of Root CAs,
but each are targeted to a specific usage.
For example, with the SharePoint Online AA list, you will only set the
component to accept from peer certificates signed by Microsoft IT SSL SHA2 and
nothing else.

Administrators are required to explicitly configure the list of trusted
root CAs,
together with their intermediate CAs and the associated CRLs.

The certificate chain must be in X.509 standard in the PEM format.
For example, a certificate chain `ca-cert-chain.pem`
may include the following certificates::

    subject=/CN=INTERMEDIATE SUBJECT HERE
    issuer=/C=UK/O=SUBJECT_OF_THE SIGNER HERE
    -----BEGIN CERTIFICATE-----
    MIICKzCCAZSgAwIBAgIBATANBgkqhkiG9w0BAQUFADA4MQswCQYDVQQGEwJVSzEP
    .... CERT CONTENT ....
    DEeUaTP4ebc05hvHIgyrHdhzXXTRpYTcL8PXHcoh3Q==
    -----END CERTIFICATE-----

    subject=/CN=ROOT CA
    issuer=/CN=ROOT CA as root is self signed
    -----BEGIN CERTIFICATE-----
    MIICKzCCAZSgAwIBAgIBATANBgkqhkiG9w0BAQUFADA4MQswCQYDVQQGEwJVSzEP
    .... CERT CONTENT ....
    JtNIblnr7VTXcOiB15uakQ==
    -----END CERTIFICATE-----

Below is another example, this time from our website, using the
`openssl s_client` tool where part of the results contain details of
the certificate chain::

    CONNECTED(00000003)
    depth=1 C = BE, O = GlobalSign nv-sa, CN = AlphaSSL CA - SHA256 - G2
    verify error:num=20:unable to get local issuer certificate
    ---
    Certificate chain
     0 s:/OU=Domain Control Validated/CN=*.sftpplus.com
       i:/C=BE/O=GlobalSign nv-sa/CN=AlphaSSL CA - SHA256 - G2
     1 s:/C=BE/O=GlobalSign nv-sa/CN=AlphaSSL CA - SHA256 - G2
       i:/C=BE/O=GlobalSign nv-sa/OU=Root CA/CN=GlobalSign Root CA
    ---


Working with SSL certificates, PKI and CA
-----------------------------------------


Supported country codes
^^^^^^^^^^^^^^^^^^^^^^^

SFTPPlus supports generated certificate signing requests using country
codes as specified by the
`ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_
standard codes.

`Exceptionally reserved
<https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Exceptional_reservations>`_
codes as assigned by ISO 3166/MA are also supported.

In case you require to generate a CSR using a country code not
currently supported by SFTPPlus, please contact us.


Generating self-signed certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can generate a self-signed certificate using the following command::

   openssl req \
     -x509 -nodes -days 365 \
     -newkey rsa:1024 -keyout certificate_key.pem -out certificate.pem

To generate a valid certificate, the Common Name (CN) fields should be set to
the server address (for server certificates) or the client username (for client
certificates).

The command will generate the following files:

 * ``certificate_key.pem`` - private key file, to be used only by the
   certificate holder.
 * ``certificate.pem`` - public certificate file that can be used by all peers
   who want to validate the certificate holder's identity.


Mutual authentication using only self-signed certificates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, you will need to create two pairs of self-signed certificates and keys
for the client and server.

You should have the following files:

 * ``server_key.pem`` - server private key
 * ``server_cert.pem`` - server self-signed certificate
 * ``client_key.pem`` - client private key
 * ``client_cert.pem`` - client self-signed certificate

To connect and validate the server, the client will use the following files:

 * ``client_cert.pem`` and client_key.pem for identifying the client to the
   server
 * ``server_cert.pem`` as the accepted Certificate Authority

To accept and validate the client, the server will use the following files:

 * ``server_cert.pem`` and server_key.pem for identifying the server to the
   client
 * ``client_cert.pem`` as the accepted Certificate Authority
