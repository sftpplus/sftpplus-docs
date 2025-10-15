Send files over AS2
===================

..  contents:: :local:


Introduction
------------

This page describes how to configure SFTPPlus to send file to a remote AS2 server.

Check the separate :doc:`reference documentation for AS2</configuration-client/as2>`,
which describes all the configuration options available for a `as2` location.

`AS2` is a file transfer protocol defined on top of the HTTP protocol.

The AS2 protocol specifications from
`RFC 4130 <https://tools.ietf.org/html/rfc4130>`_ define the protocol
as a peer-to-peer **push only** protocol.

You can control when to send (push/upload) files to your AS2 partner.

You can't control the exact time when a file is received and you can't trigger
a receive (pull / download file request) from your AS2 partner.
When you need to receive files from your AS2 partner, they are required to
push those files to you.

If you need to receive files over AS2, you will need to use the HTTP AS2
server protocol as documented on
:doc:`the HTTP AS2 service configuration page </operation/http>`.

This section documents setting up a transfer to send files over AS2.


Location configuration
----------------------

In order to setup a successful AS2 transfer,
you need to define an AS2 location.

For a successful transfer, it's important to configure matching AS2 identifiers with your partners.

The `as2_partner_identifier` should match the value set with your AS2 partner configuration.

The SFTPPlus own AS2 identifier, is defined using the `as2_own_identifier` option.
It should match the same value as the one set in your AS2 partner configuration.

For example, when your AS2 ID is `ACME-Inc-AS2` and your partner's AS2 ID
is `Ajax-Corp-AS2`, the following SFTPPlus configuration options are required::

    [locations/898e42e8-5800-11ef-a825-8376b75b88a8]
    type = as2
    name = Ajax-Corp Connection

    as2_own_identifier = ACME-Inc-AS2
    as2_partner_identifier = Ajax-Corp-AS2


AS2 certificates
----------------

When sending files over HTTPS AS2, you will most commonly have two sets of
SSL certificates:

* HTTPS SSL/TLS file transport certificates. These are usually obtained and
  signed by a trusted 3rd party certificate authority (CA)
* AS2 encryption and signature certificates. These can be self-signed
  certificates.

Using the `as2_send_security` configuration option, you can control whether
files sent by SFTPPlus over AS2 are encrypted and signed, only signed,
only encrypted, or neither signed nor encrypted.

Using the `as2_mdn_receipt` configuration option, you can control whether
to request a MDN receipt confirmation (signed or unsigned) when sending a file.

You can set encryption and digest algorithms via the
`as2_encryption_algorithm` and `as2_signature_algorithm` configuration options.

When sent files are to be signed, SFTPPlus signs them using the private key
configured in the `as2_own_private_key` option for the location configuration.

When sent files are to be encrypted, SFTPPlus encrypts them using the public key
from the first partner certificate configured in the
`as2_partner_certificates` option for the location configuration.

When receiving a signed MDN, SFTPPlus validates the signature using any
of the partner certificates configured in the
`as2_partner_certificates` option for the location configuration.


MDN Received Content MIC
------------------------

When a MDN is received, the SFTPPlus AS2 client will try to validate the received data against the `Received-Content-MIC` value found in the MDN.

SFTPPlus client will use the digest algorithm defined via `as2_signature_algorithm` to validated the value from `Received-Content-MIC`.

This means that even when you are sending unsigned payload or requested unsigned MDN,
you will still need to configure a value for the `as2_signature_algorithm` configuration option.


Asynchronous MDN
----------------

Before planning to deploy an AS2 transfer that will use asynchronous MDN,
we highly encourage to consider using the synchronous MDN delivery options.

The configuration of synchronous MDN is much simpler and involves SFTPPlus initiating only outgoing connections, without having to setup your firewall to allow incoming connections.

..  note::
    Asynchronous MDN is not supported when SFTPPlus is deployed behind a load balancer on which more than 1 node is active at the same time.

To implement asynchronous MDN delivery, SFTPPlus will first send the actual file payload to the remote server and instruct the remote server that asynchronous MDN is configured for this transfer.

The remote AS2 server will then connect back to SFTPPlus over HTTP or HTTPS.
This means that in order to receive the asynchronous MDN message,
SFTPPlus needs to act as an active HTTP/HTTPS server and allow incoming connections.

To receive the asynchronous MDN message, the AS2 location needs to be configured with a reference to the SFTPPlus HTTP/HTTPS server that will handle the incoming connections.

At the same time, the AS2 location needs to be configured with the public full URL of the SFTPPlus HTTP/HTTPS server.

Consider the example below in which we have SFTPPlus HTTPS server listening on port 10443 and the AS2 location sending files to the remote partner at `http://as2.ajax-corp.com:4433/as2/inbound`::

    [services/dd100446-581a-11ef-9afd-ebb75b483ff7]
    enabled: Yes
    name: SFTPPlus HTTPS Server
    type: https
    port: 10443
    as2_receive_name: /as2receive

    [locations/898e42e8-5800-11ef-a825-8376b75b88a8]
    name = Ajax-Corp Connection
    type = as2
    url = http://as2.ajax-corp.com:4433/as2/inbound

    as2_mdn_receipt = async-signed
    as2_async_mdn_server_uuid = dd100446-581a-11ef-9afd-ebb75b483ff7
    as2_async_mdn_url = https://ftp.sftpplus.com:10443/as2receive/mdn

The AS2 location is configured with `as2_async_mdn_server_uuid` containing the reference to the HTTPS server.
The `as2_async_mdn_url` is used to configure the public URL at which the remote AS2 partner can connect back to send the MDN message.

Note that the public DNS name is unknown to the SFTPPlus HTTPS server,
so it needs to be configured in the AS2 location.
The DNS configuration is out of scope for SFTPPlus server configuration.

If the SFTPPlus HTTP server is configured to receive an AS2 message at URL path `/as2receive`, the MDN messages will be received at path `/as2receive/mdn`.

The asynchronous MDN URL is designed to be used as part of the AS2 protocol,
and not designed for manual interaction.
If you try to open the URL in a web browser you will see the message
`Use HTTP POST method to send your request`.
This is expected and can be used to check that the URL is accessible to your AS2 partners.
