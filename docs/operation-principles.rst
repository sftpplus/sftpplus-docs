Operation principles
====================

It operates as standalone software, runnig as a background service,
without requiring any additional dependencies,
such as a database or web server.

The configuration is done via a text file, which can be edited using any text editor,
or via an embedded web-based configuration tool, which is accessible via any modern web browser.


Supported protocol
------------------

Here is a non-exhaustive list of principles standing at the base of our product:

* Multi-protocol
* Multi-platform
* Both client and server functionality in a single product
* Automated and non-interactive client side transfer
* Easy to configure and administrate
* Can be configured via text file and command line tools
* Can be configured using a web-based configuration tool
* Stand-alone product without external dependencies - with the exception
  of the OpenSSL library.

When interacting with file transfer clients, SFTPPlus implements
standardized and de-facto file transfer protocols.
The server can interact with any file transfer client that is compliant with
one of the supported file transfer protocols:

* FTP
* FTPS Explicit (AUTH TLS/SSL)
* FTPS Implicit
* SFTP
* SCP (see note)
* HTTP
* HTTPS

All standard file management operations are implemented (upload, download,
delete file, delete folder, create file) across all supported protocols.
The server also provides protocol-specific commands, as described in
the protocol's standard specifications (RFCs).


Server and Client operations
----------------------------

SFTPPlus allows, from the server perspective, remote file transfer clients to
be securely authenticated and authorized for accessing files located on local
file systems or remote file systems (CIFS/NFS) used by the operating system
running SFTPPlus.

From the client perspective, it connects to remote file transfer servers to
perform file transfer operations.


It is designed to be totally automated, prompt-less, and without interaction.
Once installed and configured properly, it should operate in the
background and need no direct attention from the user or the administrator.


Quality assurance
-----------------

Security, correctness, easy-of-use, and file transfer capabilites are all important factors and we focus on them in this
order.

To assure correct functionality of SFTPPlus, we are continually re-building
the product after each change and run an extensivve automated test suite.
The software is tested at the source code level as well as at the end to end functional level
on all supported operating systems and hardware architectures.
