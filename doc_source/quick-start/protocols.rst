Overview of Supported File Transfer Protocols
=============================================

..  contents:: :local:


Introduction
------------

For those not familiar with the supported file transfer protocols, this page
serves as an introduction to the protocols.

Not all protocols are available for both server-side and client-side
implementations.


FTP
---

**Protocol supported on both Server-side and Client-side**

Shortform for File Transfer Protocol, the objectives of FTP are 1) to
promote sharing of files (computer programs and/or data), 2) to encourage
indirect or implicit (via programs) use of remote computers, 3) to shield a
user from variations in file storage systems among hosts, and 4) to
transfer data reliably and efficiently.
FTP, though usable directly by a user at a terminal, is designed mainly for use
by programs.
`Source from RFC 959 <https://www.ietf.org/rfc/rfc959.txt>`_.

Even though FTP is offered, it is highly recommended that a secure protocol
be used.
Please read on for other recommendations.


Explicit FTPS / FTPES (over TLS)
--------------------------------

**Protocol supported on both Server-side and Client-side**

Explicit FTPS / FTPES is a security extension of FTP.

In explicit mode, an FTPS client must "explicitly request" security from
an FTPS server and then step up to a mutually agreed encryption method.
If a client does not request security, the FTPS server can either allow
the client to continue in insecure mode or refuse the connection.
`Source from FTPS wiki <https://en.wikipedia.org/wiki/FTPS>`_.

Please note that the "implementation of this protocol extension does not
ensure that each and every session and data transfer is secure, it merely
provides the tools that allow a client and/or server to negotiate an
acceptable or required level of security for that given session or data
transfer."
`Source from RFC 4217 <https://tools.ietf.org/html/rfc4217#page-5>`_


Implicit FTPS / FTPIS (over SSL)
--------------------------------

**Protocol supported on Server-side**

Implicit FTPS / FTPIS is a security extension of FTP.

In implicit mode, an FTPS client is expected to "immediately expected to
challenge the FTPS server with a TLS ClientHello message.
If such a message is not received by the FTPS server, the server should drop
the connection."

This protocol extension is considered to be a deprecated SSL negotiation
mechanism (`Source from IETF Appendix A Auth FTP SSL <https://tools.ietf.org/html/draft-murray-auth-ftp-ssl-07#appendix-A>`_) and unlike Explicit FTPS is not
defined in RFC 4217.


SFTP (over SSH version 2)
-------------------------

**Protocol supported on both Server-side and Client-side**

SFTP, shortform of SSH File Transfer Protocol and also Secure File Transfer
Protocol, is a network protocol that allows for file access, transfer and
management capabilities over the SSH (Secure Shell) protocol channel.
It is thus considered one of the secure protocols to implement.

SFTP is designed to be used to implement a secure remote file system
service and also a secure file transfer service.

SFTP should run over a secure channel, SSH, so that the server has already
authenticated the client. The identity of the client user should also be
available to the protocol.

The SFTP protocol follows a simple request-response model.

Each request and response contains a sequence number and multiple
requests may be pending simultaneously.
There are a relatively large number of different request messages, but a small
number of possible response messages.
Each request has one or more response messages that may be returned in result
(e.g., a read either returns data or reports error status).
`Source from IETF Secure Shell Working Group Internet Draft 13 <https://tools.ietf.org/html/draft-ietf-secsh-filexfer-13>`_.

It is worth nothing that SFTPPlus is only an SFTP/SCP server and does not
support certain mechanisms of an SSH server such as virtual terminal or
remote execution.


SCP (over SSH version 2)
------------------------

**Protocol supported only on Server-side**

SCP, shortform of Secure Copy Protocol, is another network protocol with
file transfer capabilities over the SSH (Secure Shell) protocol channel.
The implementation of SCP within SFTPPlus is limited.
SCP is a simple,
non-standard protocol, with no official public specification.
SFTPPlus is only an SFTP/SCP server and does not execute external 'scp'
applications.
It only supports file upload and download,
without support for file management operations such as rename, delete, etc.
Only remote execution of the 'scp' command is allowed.
Support for recursive operations is not yet implemented.

Unlike SFTP, this protocol has some limited capabilities, such as in file
management.
We recommend that SFTP be used instead.


HTTP
----

**Protocol supported only on Server-side**

HTTP, shortform for Hypertext Transfer Protocol, is an application-level
protocol for distributed, collaborative, hypermedia information
systems.
It is a generic, stateless, protocol which can be used for
many tasks.
`Source from RFC 2616 <https://tools.ietf.org/html/rfc2616>`_.
While HTTP is available, it is highly recommended the HTTPS be implemented.


HTTPS
-----

**Protocol supported only on Server-side**

HTTPS, shortform for HTTP over TLS, provides security measures in using
HTTP via SSL and its successor, TLS.

The HTTPS service can be invoked by starting SFTPPlus and accessing the
service via the URL on a web browser.
Once accessed, you will be able to see the graphical interface designed to work
in any web browser.

For those wishing to use a web browser option with their file transfer
needs, HTTPS is recommended.


WebDAV over HTTPS
-----------------

**Protocol supported only on Client-side**

Shortform for Web Distributed Authoring and Versioning, WebDAV is the extension
to the HTTP protocol allowing clients to perform remote web content authoring
operations.
`Source from RFC 2518 <https://tools.ietf.org/html/rfc2518>`_.

The SFTPPlus implementation will be utilizing the HTTPS extension on
client-side only with the authentication mechanism based on the claim-based
method from Office 365 SharePoint Online service.


Azure Files over HTTPS
----------------------

**Protocol supported only on Client-side**

SFTPPlus can exchange files with the Azure Files service provided by the
Azure Storage account.

The communication is done over HTTPS.
HTTP access is not supported.
