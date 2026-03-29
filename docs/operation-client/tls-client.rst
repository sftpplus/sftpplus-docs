TLS client configuration
========================

..  contents:: :local:


Introduction
------------

SFTPPlus acts as a TLS client in the following scenarios:

* authentication over HTTPS with custom API or Azure AD or other OpenID Connect or OAuth2 API servers,
* authenticating via LDAPS,
* connecting to HTTPS servers for WebDAV, AS2, Azure, or other cloud transfers,
* connecting to HTTPS server for sending event notifications,
* connecting to SMTP servers.


Validating the identity of the remote server
--------------------------------------------

In order to keep the confidentiality of transmitted data,
it is critical to ensure that it is only exchanged with trusted remote servers.

Confidential information should never be exchanged with untrusted or unknown servers.

This is a challenge when using public Internet connections to servers hosted by cloud providers, or connecting to an organization that has various servers distributed across the world or in various disaster recovery configurations.

For example, for disaster recovery or high availability servers,
the IP address of the server can change at any time.

PKI, or Public Key Infrastructure, is a framework used to manage digital keys and certificates,
enabling secure communication and transactions over the Internet.
It provides a way to verify the authenticity of the remote server, and ensures the confidentiality and integrity of the data communication.

PKI is used by SFTPPlus to validate the identity of the remote TLS servers.
PKI is the backbone of secure communication on the Internet,
ensuring confidentiality, integrity, and authentication.

In SFTPPlus, two configuration options are used in order to validate the identity of a server::

* Remote server URL or Domain Name
* Remote server Certification Authority chain

When connecting to a TLS server, SFTPPlus receives from it a copy of its certificate during the TLS handshake.
Alongside this certificate, the server typically also sends copies for the certificates of the CA (Certification Authority) that has issued its certificate.

The server's certificate contains a list of server names for which it is valid.

SFTPPlus uses the server name (extracted from the URL or the address configuration) to verify that the provided certificate matches the expected server.

Configuring a server URL or address using IP address or private/local names causes this validation to fail,
as the certificates are only valid for public domain names.

..  note::
    If you are using a private Certification Authority,
    you can generate certificates for private domain names.
    SFTPPlus will validate and accept these private certificates
    when using a DNS server that resolves the corresponding private domain names.

Today, it's much harder for an attacker to fraudulently obtain a public certificate,
as Certification Authorities have implemented better security checks, and all issued certificates are publicly disclosed.

Read more about `Certificate Transparency <https://en.wikipedia.org/wiki/Certificate_Transparency> here`.


Public Certification Authorities
--------------------------------

An important functionality of the Public Key Infrastructure system
is that any public Certification Authority can issue valid certificates for the same public domain name.

When exchanging files with public clouds or with partners that might have servers spread across multiple data centers or multiple clouds,
it's not easy to find out which Certification Authority is used by your partner.

SFTPPlus includes a list of public Certification Authorities that can be configured as a starting point for establishing a secure public connection with a remote server.

You don't need to provide the name or root certificate of any Certification Authority.
As long as the remote server uses a certificate issued by one of the public CAs, you can configure SFTPPlus as::

    tls_trusted_certificates = MOZILLA-CA

This uses the vault item with UUID `MOZILLA-CA` which is a CA list that is updated with each SFTPPlus release.
This list is defined by the Mozilla Corporation for the Firefox web browser.

You can read more about `Mozilla's CA Certificate Program here <https://wiki.mozilla.org/CA>`.


A series of bundle CAs are distributed with SFTPPlus.
They can be configured together and mixed with other CA certificates.
The bundle CAs are available under the following names:

* `MOZILLA-CA` - All the root certification authorities accepted by the Mozilla's CA Certificate Program
* `GOOGLE-CA` - All the root certification authorities handled by Google Trust Services
* `LETS-ENCRYPT-CA` - For Let's Encrypt X3 certificate authority.
* `MICROSOFT-CA` - For all Microsoft IT CA certificates.
  Used by SharePoint Online and other services provided by Microsoft.
* `DIGICERT-CA` - For all Digicert CA certificates.
* `GO-DADDY-CA` - For all GoDaddy Certificate Bundles, G2 With Cross to G1.

To configure a component to accept the remote peer certificates signed by
Microsoft IT CA, which is the CA used by SharePoint Online,
you can set the configuration as::

    tls_trusted_certificates = MICROSOFT-CA


Certification Authority Pinning
-------------------------------

A feature of the Public Key Infrastructure system is that any public Certification Authority
can issue valid certificates for the same public domain name.
At the same time, certificates for non-public domain names
can be issued by private or internal Certification Authorities.

SFTPPlus can be configured to automatically set the Certification Authority used by the remote server
during the first connection to the server.
To do so, define the configuration as::

    tls_trusted_certificates = set-on-first-connection

During the initial connection, the `set-on-first-connection` value gets replaced inside the configuration with a vault item containing the discovered Certification Authority certificate chain.
You no longer see the `set-on-first-connection` value, as it was automatically replaced and will now reference a vault item.

The `set-on-first-connection` has some limitations.
It can't be used with remote servers that:

* use self-signed certificates (see `pin-public-key` for self-signed certificates),
* use multiple Certification Authorities,
* do not advertise the CA chain as part of the TLS handshake,
* use Explicit FTPS. Only Implicit FTPS is supported.

..  FIXME:5459:
    Update above documentation once we support explicit FTPS.

You can also define pre-configured Certification Authority certificates,
using a configuration similar to this example.
The format for the certificates is BASE64 PEM::

    as2_partner_trusted_certificates = fda4313a-066c-11f1-af6d-1f1082a083ea

    [vault-items/fda4313a-066c-11f1-af6d-1f1082a083ea]
    name = ACME AS2 Partner Certificates
    type = trusted-certificates
    content = -----BEGIN CERTIFICATE-----
        MIICaDCCAdGgAwIBAgIBDjANBgkqhkiG9w0BAQUFADBGMQswCQYDVQQGEwJHQjEP
        PEM CONTENT FOR INTERMEDIARY CERTIFICATION AUTHORITY. IF ANY.
        JZQaMjV9XxNTFOlNUTWswff3uE677wSVDPSuNkxo2FLRcGfPUxAQGsgL5Ts=
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        MIICaDCCAdGgAwIBAgIBDjANBgkqhkiG9w0BAQUFADBGMQswCQYDVQQGEwJHQjEP
        PEM CONTENT FOR ROOM CERTIFICATION AUTHORITY
        JZQaMjV9XxNTFOlNUTWswff3uE677wSVDPSuNkxo2FLRcGfPUxAQGsgL5Ts=
        -----END CERTIFICATE-----

If, at any time, a remote server's certificate expires or is reissued by a different Certification Authority,
the connections to it will start to fail, as the remote server's identity can no longer be validated by SFTPPlus
in such a configuration.

The connection would also fail if the URL or address configured to connect to the remote server do not match the URLs or addresses found in the certificate advertised by the remote server during the TLS handshake.


Certificate and Public Key Pinning
----------------------------------

Public Key Pinning (PKP) is an advanced security mechanism used to defend against man-in-the-middle attacks involving fraudulent digital certificates.

In most cases, you should use either the list of public Certification Authorities from Mozilla or our lists of predefined certificates for Let's Encrypt and/or Microsoft.
This is described above on this page.

Before implementing key pinning, consider implementing Certification Authority pinning instead.
This provides a greater flexibility, allowing the remote server to renew or generate a new private key, without any extra-configuration from your side.

Key pinning for a TLS client, such as SFTPPlus, specifies which public key and certificates it expects to receive during a TLS handshake to a certain remote server.
This helps prevent a man-in-the-middle attack for a known remote server,
even if somehow the attacker has obtained a valid public certificate for the server's domain name.

For example, an attacker can obtain a valid public certificate due to a defect or security issue with a public Certification Authority, or by infiltrating a public Certification Authority.

Key pining can be used in the following scenarios:

* high security environments in which the remote server configuration is static,
* private servers or software appliances using self-signed certificates,
* legacy servers for which the certificate has expired and can't be renewed.

Key pinning is especially useful for legacy or in-house applications,
being much preferable to entirely disabling server identity validation.

SFTPPlus implements public key pinning.
This means that the remote server can renew its certificate and no configuration change is required for SFTPPlus.
A certificate renewal is a new certificate that was issued for the same private key.
The remote server can also obtain a certificate from a different Certification Authority, and
no configuration changes are required on the SFTPPlus side
as long as the certificate is requested for the same private key.

..  warning::
    When public key pinning is used, SFTPPlus does not require the remote server's
    certificate to match the URL or address name.
    It also does not check for certificate expiration.

SFTPPlus can be configured to automatically set the pinned public key
during the first connection to the remote server.
To do so, define the configuration as::

    tls_trusted_certificates = pin-public-key

After the initial connection, the `pin-public-key` value gets replaced inside the configuration with a vault item containing the public key advertised by the remote server during the TLS handshake.

You can configure SFTPPlus to pin a specific public key using the following configuration.
The public key PEM format can be the format described in RFC 7468 or X.509 SubjectPublicKeyInfo PEM ("BEGIN PUBLIC KEY") from RFC 5280.

You specify the public key in PEM format::

    tls_trusted_certificates = 12345678-1234-5678-1234-567812345678

    [vault-items/12345678-1234-5678-1234-567812345678]
    name = Trusted Keys for Server XYZ
    type = pinned-keys
    content = -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqVNXiyZJUoMZMuAy1VP6
        MORE CONTENT OF THE PUBLIC KEY
        p+ElxaJNjzW7GLZ3Etog6APB5jgXH2lHzP8bYv55bnepiHzmgZVA9u0B2SBLil1m
        TwIDAQAB
        -----END PUBLIC KEY-----

For services operated by multiple servers,
for example distributed across multiple regions,
you can configure multiple public keys.
Multiple public keys can also be used in preparation for a remote server rotating its public key.
You can also configure the vault items using the PEM certificate format.
**Only the public key part** of the certificate is used for validation.
The certificate validity dates or subject alternative names are ignored.
The configuration will look like::

    tls_trusted_certificates = 12345678-1234-5678-1234-567812345678

    [vault-items/12345678-1234-5678-1234-567812345678]
    name = Trusted Keys for Server XYZ
    type = pinned-keys

    content =
        -----BEGIN CERTIFICATE-----
        MIICTDCCAbWgAwIBAgIBATANBgkqhkiG9w0BAQUFADBGMQswCQYDVQQGEwJHQjEP
        PEM CERTIFICATE IS ALSO VALID FOR KEY PINNING
        JtNIblnr7VTXcOiB15uakQ==
        -----END CERTIFICATE-----

        -----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqVNXiyZJUoMZMuAy1VP6
        ANOTHER KEY CONFIGURED
        -----END PUBLIC KEY-----

If the remote server later advertises a different public key, the connection to the remote server
will fail to start,
as the remote server's identity can no longer be validated by SFTPPlus
in such a configuration.
