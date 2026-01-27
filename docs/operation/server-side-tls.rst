Server-side TLS configuration
=============================

..  contents:: :local:


Introduction
------------

File transfer protocols such as FTPS or HTTPS use TLS (Transport Layer Security) to provide privacy and data integrity between client and server applications.

The configuration options for these protocols in SFTPPlus include settings for certificates, TLS versions, mutual TLS, and cipher suites.

This page provides detailed information about these configuration options and how to set them up in SFTPPlus.

For a complete reference of all available options, check the separate configuration pages for each protocol:

* :doc:`FTPS </configuration-server/ftp-service>`
* :doc:`HTTPS </configuration-server/http-service>`
* :doc:`Admin Web Console </configuration/local-manager>`


TLS server key and certificate
------------------------------

For a TLS based server to operate, a valid server certificate and the corresponding private key are required.
The TLS protocol only supports a single certificate and private key pair for each protocol instance.
That is, for an FTPS or HTTPS service, you can only configure a single certificate and private key pair.

When your server is accessed using multiple hostnames or IP addresses, it is important to ensure that the server certificate is valid for all the hostnames or IP addresses that clients will use to connect to the server.
This is achieved by generating a certificate request for multiple Subject Alternative Names (SANs) in the server certificate.

**Subject alternative names**

When configuring the server certificate, it is important to ensure that the certificate includes the appropriate Subject Alternative Names (SANs) that match the hostnames or IP addresses clients will use to connect to the server.
This ensures that clients can successfully verify the server's identity during the TLS handshake.


TLS versions and cipher suites
------------------------------

SFTPPlus allows you to configure a list of supported TLS versions and cipher suites for FTPS and HTTPS services.

When a remote client connects to the server, such as a FTPS client or a web browser,
SFTPPlus will propose the list of configured TLS versions and cipher suites.
The client will also send their own list of supported TLS versions and cipher suites.
The SFTPPlus server will then select the highest mutually supported TLS version and a cipher suite from the client's proposed list that is also supported by the server.

The TLS versions and cipher suites are configured using the `ssl_allowed_methods` and `ssl_cipher_list` options respectively.


Mutual TLS authentication
-------------------------

Mutual TLS authentication, also known as two-way TLS or client certificate authentication, is an optional feature that can be enabled for FTPS and HTTPS services in SFTPPlus.

The default TLS authentication mechanism used by FTPS and HTTPS services is server only authentication, also known as anonymous authentication.
In this mode, only the server presents its certificate to the client during the TLS handshake.
The client verifies the server's certificate to ensure it is connecting to the intended server.
The server does not request or verify any certificate from the client.
This is achieved by leaving the `tls_mutual_certification_authorities` configuration option empty.

To enable mutual TLS authentication, you need to configure the `tls_mutual_certification_authorities` option with a list of trusted Certificate Authorities (CAs) or trusted client certificates.

The trusted certificates are configured via vault items.

When mutual TLS authentication is enabled,
both the server and the client present their certificates to each other during the TLS handshake.
The server verifies the client's certificate against a list of trusted Certificate Authorities (CAs) specified in the `tls_mutual_certification_authorities` configuration option.
If the client's certificate is valid and trusted, the TLS handshake proceeds, and the client is authenticated.
If the client's certificate is invalid or not trusted, the TLS handshake fails, and the connection is terminated.

Expired certificates are also rejected during the mutual TLS authentication process.


Certificate only authentication
-------------------------------

In some scenarios, you may want to authenticate FTPS or HTTPS clients based solely on their certificates without requiring a password.
The username is still required to identify the user account and it should match the common name (CN) in the client's certificate.

To enable certificate-based authentication,
you need to configure the `tls_mutual_certification_authorities` option so that SFTPPlus will require the clients to send a valid certificate during the TLS handshake.

Make sure that the configured trusted certification authorities will issue certificates while validating the common name (CN) to match the allowed username.


Web manager TLS configuration
-----------------------------

All the available TLS configuration options for FTPS and HTTPS services are available to be configured from the Web manager console.

The UI will only display TLS versions or ciphers available for the current SFTPPlus version.
