AS2 Server
==========

..  contents:: :local:


Introduction
------------

SFTPPlus can receive files using the EDIINT AS2 protocol defined in the
`RFC 4130 <https://tools.ietf.org/html/rfc4130>` standard.

This page covers receiving files over AS2.
If you want to send files over AS2, check the :doc:`dedicated HTTP AS2 transfer </operation-client/as2-send>` documentation page.

Received content can be confirmed using the
message disposition acknowledgment (MDN) method defined in
`RFC 3798 <https://tools.ietf.org/html/rfc3798>`.

File content can be compressed as defined in
`RFC 5402 <https://tools.ietf.org/html/rfc5402>`, encapsulated in a
CMS (Cryptographic Message Syntax) MIME entity.


HTTP method
-----------

The AS2 messages should be sent using the `POST` HTTP request verb/method.

The `HEAD` HTTP verb is provided as a way to validate the HTTP basic authentication credentials,
without triggering any AS2 file transfer.


HTTPS security
--------------

The AS2 connections are secured at the transport layer by the HTTPS protocol.
In this regard, the SFTPPlus AS2 server is configured just like any other HTTPS server.
The SFTPPlus HTTPS server allows transfering files over web browser, AS2, REST, WebDAV by using a shared HTTPS server.
There is no need to set up separate HTTPS servers for each file transfer type.

Mutual-TLS authentication is supported at the HTTPS level.

Check the :doc:`dedicated HTTPS server </configuration-server/http-service>` documentation page, to learn more about how to configure the HTTPS security.

For legacy transfers, SFTPPlus allows exchanging AS2 files over an HTTP server.


Configuration example
---------------------

The SFTPPlus HTTPS server can be configured to receive files over AS2.
This is done by configuring the AS2 URL fragment.
This is an URL name that SFTPPlus will use to know that the received content should be handled as AS2 message.

Below is a configuration example.
In the following sections of this page, we will discuss the details of each configuration part and AS2 operation like authentication, encryption, MDN, etc.

The public AS2 site is available at the `https://example.tld/as2receive` URL,
where the `as2receive` URL fragment is defined by the `as2_receive_name`
configuration option::

    [services/9ac4-1054-f0e4]
    name = HTTPS with AS2 File Transfer Service
    type = https

    as2_organization = ACME Org
    as2_receive_name = as2receive
    as2_pending_path = /as2/pending
    as2_receive_path = /as2/receive
    as2_receive_private_certificate = as2-server-certificate-uuid

    [accounts/4a48fbf4-d029]
    name = johnd
    home_folder_path = C:/Users/JohnD
    ; One or more certificates used by the remote partner to sign the
    ; received files.
    as2_trusted_certificates = johnd-certificates-uuid
    as2_require_http_authentication = no

    [accounts/758185de-d029]
    name = janer
    home_folder_path = C:/Users/JaneR
    as2_require_http_authentication = yes
    password = $6$rounds=80000$GE5tScXoFSfkMgBd$cDi7KLiu8X5gKkXC8d9FblkKG46p
    as2_trusted_certificates = janer-certificates-uuid
    permissions =
        allow-full-control
        *.exe, deny-full-control

    [vault-items/as2-server-certificate-uuid]
    type = private-certificate
    name = AS2 server certificate
    content =
        ----BEGIN RSA PRIVATE KEY-----
        MIICXgIBAAKBgQDOoZUYd8KMYbre5zZIwR+V6dO2+cCYVS46BHbRbqt7gczkoIWh
        EXAMPLE key with diferrent armour
        Wh+QF3UArO8r8RYv3HRcnBjrGh+yEK93wIifVNGgy63FIQ==
        -----END RSA PRIVATE KEY-----
        -----BEGIN CERTIFICATE-----
        MIICaDCCAdGgAwIBAgIBDjANBgkqhkiG9w0BAQUFADBGMQswCQYDVQQGEwJHQjEP
        MORE CERTIFICATE CONTENT
        JZQaMjV9XxNTFOlNUTWswff3uE677wSVDPSuNkxo2FLRcGfPUxAQGsgL5Ts=
        -----END CERTIFICATE-----

    [vault-items/johnd-certificates-uuid]
    type = trusted-certificates
    name = AS2 certificates for user John D
    content = -----BEGIN CERTIFICATE-----
        MIICpTCCAg6gAwIBAgIIP8vt0MYYvNIwDQYJKoZIhvcNAQELBQAwRjELMAkGA1UE
        MORE CERTIFICATE CONTENT
        JZQaMjV9XxNTFOlNUTWswff3uE677wSVDPSuNkxo2FLRcGfPUxAQGsgL5Ts=
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        MIICoDCCAgmgAwIBAgIIKk0/vqmeDb4wDQYJKoZIhvcNAQELBQAwODELMAkGA1UE
        MORE CERTIFICATE CONTENT
        6sXcntbQ8jyu8fNCjoVKGUe9gsgZOK2KapWxU7HzvulVQslcOcWG3mM=
        -----END CERTIFICATE-----

    [vault-items/janer-certificates-uuid]
    type = trusted-certificates
    name = AS2 certificates for user Jane R
    content = -----BEGIN CERTIFICATE-----
        BAYTAkdCMQ8wDQYDVQQKEwZDaGV2YWgxFDASBgNVBAsTC0NoZXZhaCBUZXN0MRIw
        EAYDVQQDEwlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAM6h
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        ulGy7rwJI9Me95aG53BrjMbBKk1qaHuNXa3PJjcgVmPelwPcbzk5Wl4E57dLN+eh
        4Rf/Qyi9HBdtrDf19OzBmBs7W7pO9LPo5/usHlyVAgMBAAGjZDBiMBMGA1UdJQQM
        -----END CERTIFICATE-----

With the above configuration, files received via AS2 for account `johnd` are
temporarily stored in `C:/Users/JohnD/as2/pending`.
The signature of those files is checked against the list of certificates configured by the *trusted-certificates* vault item associated with the `johnd` account.
Once the AS2 transfer is complete and the AS2 content is validated,
the files are moved to `C:/Users/JohnD/as2/receive`.

The files received by the `janer` account are temporarily stored in `C:/Users/JaneR/as2/pending` and then moved into `C:/Users/JaneR/as2/receive`.
The connections for `janer` will need to be authenticated using an username and password via the *HTTP Basic* authentication method.
Without a valid HTTP username and password, the AS2 messages are rejected.
This behaviour is controlled by the `as2_require_http_authentication` configuration option.

At the same time, any file with a name ending in `.exe` uploaded by account `janer` is rejected.

..  note::
    Encrypted received messages should be encrypted using an RSA key.
    DSA public key-based encryption is not supported.
    Contact us if you need to encrypt AS2 messages using DSA.

When signed files are received,
SFTPPlus will validate the configuration using the public certificate configured in the `as2_trusted_certificates` vault item in the *user account*.

When encrypted files are received,
SFTPPlus will decrypt them using the private key defined via the `as2_receive_private_certificate` configuration option of the HTTP(S) *AS2 server*.

When signed message disposition notifications (MDN) are requested,
SFTPPlus will sign them using the private key configured at `as2_receive_private_certificate`, defined by the *AS2 server*.


AS2 message authentication
--------------------------

You add an AS2 partner by creating a normal SFTPPlus file transfer account,
having the same account name as the AS2 partner ID.

The default AS2 user authentication is done by checking the signature of the received files.
This implies that the file needs to be fully received before validating the user identity.

Non-authenticated AS2 messages are supported and the account name will match the value of the `AS2-From` HTTP header.
You need to explicitly configure an account to not require HTTP authentication for AS2 messages.
This is done using the `as2_require_http_authentication` account configuration option.

While the AS2 messages are received, the partial files,
and the files that are not yet validated,
are stored in the home path as configured for each user,
in a sub-directory defined by the `as2_pending_path` configuration.

After the AS2 message is fully received and validated,
the files from the AS2 messages are stored in the home path as configured for each user,
in a sub-directory defined by the `as2_receive_path` configuration.

Files received via AS2 will have to comply with the general security policy and permissions,
similar to any other file transfer protocol.

Below is an example in which the configuration will allow a partner with
ID ``AS2 Trade aMjV9XxNTFO`` to send AS2 messages without HTTP authentication.
It is highly recommend to restrict the source IP for this account,
as without HTTP authentication anyone can send messages for this account,
just by knowing the name of the trading partner::

    [accounts/4a48fbf4-d029]
        name = AS2 Trade aMjV9XxNTFO
    home_folder_path = C:/Users/JohnD
    as2_require_http_authentication = No
    source_ip_filter = allow 24.12.231.0/24

If you can deploy a configuration in which source IP filtering is enabled,
we recommend to add a long and hard to guess value for your trading partner.
This is why the above example uses the ``aMjV9XxNTFO`` value in the
``AS2 Trade aMjV9XxNTFO`` partner name.


Username and password or mutual TLS authentication
--------------------------------------------------

With the default method,
anyone from the Internet with access to your HTTPS/AS2 server can push files over the AS2 protocol.

We recommend setting up the message exchange with your AS2 partner using username and password or username and TLS certificate credentials authentication.

For HTTP authenticated requests,
SFTPPlus uses the `username` found in the AS2 HTTP authentication
request to recognize and authorize an AS2 partner.
In this case,
the `AS2-From` value found in an AS2 message is only informative,
but it is required in all messages by the AS2 standard.


File name
---------

SFTPPlus will try to use the `Content-Disposition` HTTP header as the file name of the received AS2 message.

If no `Content-Disposition` header is found in the AS2 request describing
the name of the required file, SFTPPlus will store the received data using
the name `as2-received-file.TIMESTAMP`, where TIMESTAMP is replaced with
the date and time at which the file transfer was initiated.
To use a different filename for this case,
define the `as2_default_filename` configuration option.


Async MDN delivery
------------------

The delivery for asynchronous(ASYNC) MDN is retried 5 times,
waiting 1 minutes for the first retry, then 2 minutes,
and waiting 1 minute more with each retry.

The async MDN HTTPS request is made using the same TLS methods and
ciphers configured for the HTTPS service over which the initial AS2 message
was received.

When the remote partner is requesting an async MDN over HTTPS, the remote
HTTPS connection is authenticated using the HTTPS SSL/TLS certificates
configured for the associated account as part of the `as2_async_mdn_https_trusted_certificates` vault item *trusted-certificates*.

Our recommendation is to set up file transfers with your AS2 partner using
synchronous MDN. This simplify the network configuration and provides
improved security.

Setting `as2_async_mdn_https_trusted_certificates` to an empty value disables async MDN support entirely.
Setting it to `disabled` values allows async MDN but disables the security check of the remote peer's certificate.

Asynchronous MDN response delivery errors will emit a dedicated failure event.

No extra event is emitted on the successful delivery of synchronous or
asynchronous MDNs,
other than the general event for the successful receiving of the AS2 message.
