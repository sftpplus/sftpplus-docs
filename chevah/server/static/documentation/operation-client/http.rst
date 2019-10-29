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


WebDAV over HTTPS Extension
---------------------------

The HTTPS WebDAV extension is supported on the client-side while interacting
with the Office 365 SharePoine Online server.

Uploading empty files to SharePoint is not supported.

When defining a path you can use the `space` character instead of the URL
Percent Encoding `%20` character.

If a path contains the `+` (plus) sign, it may not be replaced with the
`space` or URL Percent `%20` Encoding characters.

The SharePoint WebDAV Path is case insensitive.
For the transferred files, the names are kept using the cases presented by
the WebDAV server.

Please see our :doc:`WebDAV User's Guide </guides/webdav>` page for a guide on
getting started with WebDAV.
