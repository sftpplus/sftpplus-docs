HTTP / HTTPS Client Operations
==============================

..  contents:: :local:


Introduction
------------

SFTPPlus will act as an HTTP/HTTPS client in both server-side related operation
as well as client-side transfers.

Below is a non-exhaustive list of operations which involve acting as HTTP
client:

* HTTP authentication method - using persistent connection
* Updating a CRL list (ex as part of CDP) - using non-persistent connection
* Sending events over HTTP - using persistent connection
* Transferring files over WebDAV - using persistent connection


HTTP Connection Audit
---------------------

Most of the HTTP operations are done over a pool of persistent HTTP connections.
This means that multiple HTTP operations, while executed in a serial way,
will use the same HTTP connection.
If multiple HTTP operations are done in parallel, multiple concurrent HTTP
connection are created.

An event is emitted each time an HTTP/HTTPS connection is opened or closed.
The event will contain the actual IP address and port used by the connection,
as well as the requested hostname.

The request might be made to ``intra.your-company.com``, but when that DNS name
has multiple IP addresses, the audit event will contain the IP address used
for that connection.

For HTTPS connections, it will also show the certificate and cipher used to
protect the connection.


HTTP Proxy for Client
---------------------

Most of the client side operations can be via an HTTP proxy.

When the HTTP proxy is use, the events emitted for the HTTP operations
will use the tunneled address, even if the actual connection is done to the
proxy address.

To ensure accuracy, you should also audit the proxy to get an authoritative
view of the actual network connections.


Send files with AS2 over HTTP or HTTPS
--------------------------------------

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
service as documented on
:doc:`the HTTP AS2 service configuration page </operation/http>`.

This section documents setting up a transfer to send files over AS2.

----------

In order to setup a successful AS2 transfer, you need to configure matching
AS2 identifiers with your partners.

On your side, you need to configure the `as2_partner_identifier` SFTPPlus
option to the exact same value set in your AS2 partner configuration.

When defining your own AS2 identifier using the `as2_own_identifier`
option, the exact same value must be set in your AS2 partner configuration.

For example, when your AS2 ID is `ACME-Inc-AS2` and your partner's AS2 ID
is `Ajax-Corp-AS2`, the following SFTPPlus configuration options are required::

    as2_own_identifier = ACME-Inc-AS2
    as2_partner_identifier = Ajax-Corp-AS2

----------

When sending files over HTTPS AS2, you will most commonly have two sets of
SSL certificates:

* HTTPS SSL/TLS file transport certificates. This are usually obtained and
  signed by a trusted 3rd party certificate authority (CA)
* AS2 encryption and signature certificates. This can be self-signed
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


WebDAV over HTTPS Extension
---------------------------

The HTTPS WebDAV extension is supported on the client-side while interacting
with the Office 365 SharePoine Online server.

Uploading empty files to SharePoint is not supported.

When defining a path you can use the `space` character instead of the URL
Percent Encoding `%20` character.

If a path contains the `+` (plus) sign, it may not be replaced with the
`space` or URL Percent `%20` Encoding characters.

The SharePoint WebDAV Path is case-insensitive.
For the transferred files, the names are kept using the cases presented by
the WebDAV server.

Please see our :doc:`WebDAV User's Guide </guides/webdav>` page for a guide on
getting started with WebDAV.
