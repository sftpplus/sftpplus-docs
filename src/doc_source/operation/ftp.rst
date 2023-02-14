FTP/FTPS Usage
==============

..  contents:: :local:


Introduction
------------

This page contains information about the server-side usage
and behaviour of the FTP commands implemented by the FTP service/server.

The FTP/FTPS implementation is designed to follow the RFCs as much as possible
and mimic the behaviour found in the VSFTPD implementation without sharing
any source code.


Available FTP server commands
-----------------------------

Our goal for SFTPPlus is to implement all FTP commands described in
dedicated RFC specifications.

Below is a list with currently supported commands.
Most commands are defined in the original RFC 959.
In `RFC 5797 <https://tools.ietf.org/html/rfc5797#page-6>`_ you can check
the exact RFC associated with a command.

* `APPE` Request an upload with appending to existing file.
* `AUTH` Set up a secure control channel. RFC 4217
* `CCC` Clear control channel security. RFC 2228 4217
* `CDUP` Change to the parent directory.
* `CLNT` Receive name of the client software.
* `CWD` Change working directory.
* `DELE` Delete a file.
* `EPRT` Request an extended active connection. RFC 2428
* `EPSV` Request an extended passive connection. RFC 2428
* `FEAT` Advertise the features supported by the server. RFC 2389
* `LANG` Negotiate language to present server greetings and the textual part
  of command responses. RFC 2640. Only Enligsh is supported.
* `LIST` List a directory on the server using a format similar to the Unix
  `ls` command.
* `MDTM` File Modification Time. With support for setting the modification
  time. RFC 3659
* `MFMT` Modify Fact: Modification Time. draft-somers-ftp-mfxx-04
* `MKD` Make a directory on the server.
* `MLST` Listing for machine processing over the control channel. RFC 3659
* `MLSD` Listing for machine process over the data channel. RFC 3659
* `MODE` Set transfer mode. Only the `stream` mode is supported.
* `NLST` List only the names of directory members.
* `NOOP` Does nothing. Used to keep the session alive.
* `OPTS` Specify options for the command to follow.
* `PASS` Set the password for authenticating in the current session.
* `PASV` Request a passive connection.
* `PBSZ` Negotiate the buffer size for the secure data transfer. Any value is
  accepted, but ignored. RFC 4217
* `PORT` Request an active connection.
* `PROT` Negotiate the data connection security level. RFC 4217
* `PWD` Print the working directory.
* `QUIT` Close the session.
* `RETR` Request a download.
* `RMD` Remove a directory on the server.
* `RNFR` First part of a rename request.
* `RNTO` Second part of a rename request.
* `SITE` Custom SFTPPlus FTP service command.
* `SIZE` Return the size of the file. RFC 3659
* `STOR` Request an upload.
* `STRU` Define the file structure mode. Only the `F - File` code is
  supported.
* `SYST` Return the system type. Always returns the Unix type to hide server
  identity.
* `TVFS` A Trivial Virtual File Store. RFC 3659
* `TYPE` Define type of file to be transferred. Only the `I` (binary),
  `A` (ASCII), and `U` (Unicode) types are supported.
* `USER` Set username for the current session.
* `XCUP` Obsolete variant for `CDUP` RFC 775
* `XCWD` Obsolete variant for `CWD` RFC 775
* `XMKD` Obsolete variant for `MKD` RFC 775
* `XPWD` Obsolete variant for `PWD` RFC 775
* `XRMD` Obsolete variant for `RMD` RFC 775

The list of available `SITE` commands is:

* `CHMOD` change permissions for a target path. Not available on Windows.
* `UTIME` set the modification timestamp.
* `IDLE` equivalent to `NOOP` command
* `PSWD` change the password for the authenticated user.


FTP command completion code and message
---------------------------------------

For every command requested by the FTP client, SFTPPlus will reply with a
completion code and a human readable text.

Based on the FTP standard (RFC 959), well behaved FTP clients should only look
at the completion code and ignore the human readable text.
The codes are for use by programs and the text is usually intended for
human users to review the programs' activity.

While the completion codes are well documented in the FTP standards, the
content of the human readable text is left undocumented.

In SFTPPlus the content of the human readable text is not documented and
can't be configured. To improve compatibility with the FTP clients we try to
follow the human readable messages produced by the VSFTPD open source FTP/FTPS
server.
Please report any inconsistency in the content of the human readable
text sent together with the completion codes.

When an operation fails due to a permission or authorization error, SFTPPlus
will return error code `553`.
VSFTPD returns `553` for authorization error (ex upload is completely disabled)
and `550` for filesystem permission errors.
SFTPPlus uses `553` to make it easier to differentiate a normal file not found
error from a permission error.


FTP Data Types - ASCII vs BINARY
--------------------------------

SFTPPlus supports only the ASCII and IMAGE/BINARY data types.

When no explicit data type is requested by the client-side, the server will
consider the data type as IMAGE/BINARY.

The default data type can be changed using
:doc:`the FTP service configuration </configuration-server/ftp-service>`.

..  note::
    The RFC 959 defines the default type as ASCII but in SFTPPlus the default
    mode is IMAGE to match the behaviour found for the SFTP and HTTPS,
    the implementation found in the previous versions of SFTPPlus,
    and the VSFTPD implementation.

When the IMAGE/BINARY data type is used, files are transferred as they are,
without any changes to their content.

When the ASCII data type is used, the source peer will convert any new line
delimiters to the standard FTP delimiter `CRLF`.

..  note::
    In ASCII mode, the `SIZE` command will return the size of the file as
    stored on the server and not as transferred with new line conversion as
    mandated by the RFC 959 for ASCII mode transfers.

    This is done to prevent denial of service attack (DoS) and to match the
    behavior found in the VSFTPD implementation.

Since SFTPPlus is designed as a cross-platform solution, when SFTPPlus is the
source of the transfer (for example when responding to the RETR command), it
will convert both Unix and Windows new line delimiters to the FTP new line
delimiters.

When SFTPPlus acts as the destination of the transfer, it will convert the
new lines only when running on Unix-like systems, as the FTP and Windows new
line delimiters are the same.

The FTP/FTPS service can be configured to pretend that ASCII mode is provided,
but to transfer the actual data based on IMAGE/BINARY mode.
For more details, check the configuration section.


Globbing in FTP commands
------------------------

SFTPPlus supports globbing / wildcards expressions for both
`LIST` and `NLST` commands for matching direct member names.

The following wildcards are available:

 * `*` - matches any number of characters
 * `?` - matches exactly one character
 * `[ and ]` - matches exactly one character from the group of characters
   listed inside the brackets.

Check the following examples to get a better understanding of globbing
and the usage of wildcards.

All examples are based on the following folder structure::

    a_file.txt
    other_extension.file.doc
    other_file.txt
    some_empty_folder
    some_file1.txt
    some_file11.txt
    some_file2.txt
    some_folder
    some_folder/file2.txt

Running ``LIST *`` will return the following members::

    a_file.txt
    other_extension.file.doc
    other_file.txt
    some_empty_folder/
    some_file1.txt
    some_file11.txt
    some_file2.txt
    some_folder/

..  note::
    ``some_folder/file2.txt`` is excluded from the result, since the match
    is not recursive.

Running ``LIST some_empty_folder/*`` will return an empty result set.

Running `LIST *.txt` will return any file or folder ending with ``.txt``::

    a_file.txt
    other_file.txt
    some_file1.txt
    some_file11.txt
    some_file2.txt

Running `LIST some_file?.txt` will return::

    some_file1.txt
    some_file2.txt

..  note::
    ``some_file11.txt`` is excluded from the result since ``?`` matches a
    single character only.

Running ``LIST [ao]*`` will return any file or folder starting with ``a`` or
``o``::

    a_file.txt
    other_extension.file.doc
    other_file.txt

Running ``LIST [bc]*`` will return an empty result set since no file or
folder starts with ``b`` or ``c``.

Globbing will not work if applied recursively.

Any of the commands listed below will result in a failure::

    ftp> LIST */file*
    ftp> LIST some_*/file2.txt
    ftp> NLST som?/*

Both LIST and NLST commands will only list direct (first level) folder members.


Changing permissions for files and folders
------------------------------------------

On Unix-like systems, the server supports the `SITE CHMOD` command, which
allows changing permissions for a target path.

`SITE CHMOD` is not specified in the FTP standard and it is not available
on Windows, since permissions on Windows are different from those on Unix-like
systems.

The syntax for the `SITE CHMOD` command is::

    ftp> SITE CHMOD mode path

where `mode` is an octal permission mode and `path` is the targeted path.

To change the permissions to `644` for file ``some/file name.txt``, the command
is::

    ftp> SITE CHMOD 644 some/file name.txt

..  note::
    The server will only consider the significant bits from the
    requested permissions and ignore any extra bits. This is why setting
    a mode like 10000644 will succeed.


Changing modification time for files
------------------------------------

The `MDTM`, 'MFMT' or `SITE UTIME` commands can be used for setting the
modification time of a file.

The date and time are handed using GMT.

To get the modification time for the file ``some/file name.txt``, the command
and the response are::

    < MDTM some/file name.txt
    > 213 20160705132316

To change the modification time to the 24th of September 2014 for file
``some/file name.txt``, the command and the response are::

    < MDTM 20160929043300 some/file name.txt
    > 213 File modification time set.

   > MFMT 20160929043300 some/file name.txt
   < 213 Modify=20160929043300; some/file name.txt

   > SITE UTIME 20160929043300 some/file name.txt
   < 213 File modification time set.

Modification time can be read and set for files and directories.

Time can also be set using milliseconds by using the input formated as
exemplified below::

   > MFMT 20160929043300.14312 some/file name.txt
   < 213 Modify=20160929043300.14312; some/file name.txt


Disclosing system type with SYST command
----------------------------------------

When the SYST command is issued to the server, the FTP client wants to know
the operating system type used by the server.
To prevent any potential security issue and to keep the operating system
anonymous, the server will always respond with a generic `UNIX Type: L8`
answer.


Data channel usage
------------------

Based on FTP specifications, all commands are sent using a dedicated
command channel.
Command responses are sent by the server using the same channel.

All data transfers, including folder listing, are sent over a different
data channel.
Only a single data channel can be active at any given time.

This is how the FTP implementation behaves when for example it receives both
PASV and PORT command for a data channel which was not yet used::

    < PASV
    > 227 Entering Passive Mode (127,0,0,1,35,40).
    > PORT 127,0,0,1,35,41

    FTP COMMAND PAUSE HERE UNTIL PASV REQUEST TIMES OUT

    < 200 PORT OK
    < 125 Data connection already open, starting transfer
    drwxrwxr-x   3 1001      1001                 4096 Jul 24 12:00 man

When a data channel is active and the client requests a new data channel,
the previous data channel is forcibly closed, even if already connected,
and a new data channel is created.


Passive connections (PASV) implementation details
-------------------------------------------------

When a client requests the PASV command, SFTPPlus will open the data
connection and waits for the client to connect to the new data channel.
Unless the client connects to the data channel, no other command is processed.

When the FTP/FTPS service is accessed from behind a NAT, using the standard
`PASV` commands, clients will get a response containing the server internal
IP address, rather than the external address used by the NAT server.
This is not an implementation error in SFTPPlus, but a design problem
of the standard PASV command, which was defined in 1985 in RFC 959.

RFC 2428 was created to solve this problem and it adds `EPSV` command
(extended PASV).
Whenever possible, FTP clients are encouraged to use EPSV rather than PASV and
EPRT rather than PORT command.

In the case that you have legacy FTP clients without EPSV support to connect to
your FTP / FTPS server from behind the NAT, the FTP service configuration
provides the `passive_address` configuration option as a way to work around
this problem.
For more details please check the
:doc:`FTP service configuration page </configuration-server/ftp-service>`.

When `passive_address` is defined and you have FTP clients which connect
from the same LAN (not passing the NAT), they will still get the NAT
IP address in PASV responses.
As a way to get around this, you can create a new FTP service, on a different
port, dedicated to internal LAN clients.
For this new service, leave the `passive_address` configuration option empty.


Active connections (PORT) source address and port
-------------------------------------------------

For active connection, an FTP or FTPS server will initiate the data channel
connection as a TCP client.

For these connection types, the destination address and port are specified
by the client as part of the `PORT` / `EPRT` commands.

By default, for these connections, SFTPPlus will use any **source** address or
source port, letting the operating system choose the actual value.
Most operating systems will use a port number in the range allocated to
the `ephemeral ports <https://en.wikipedia.org/wiki/Ephemeral_port>`_.

Some (legacy) FTP clients require that all active data channel connections
are initiated from port 20 or a different configurable port.

You can also use a single source port in the case when the outgoing traffic
should be filtered by the firewall.

SFTPPlus can be configured to use a specific source port number.
For more details please check the
:doc:`FTP service configuration page </configuration-server/ftp-service>`.


Restarting a transfer
---------------------

Support for restarting an upload/append or download request is provided using
the FTP `REST` command.

After a successful or failed transfer, the offset is always set to 0.

When `REST` is used together with the `APPE` command, it will behave just like
the `STOR` command.
That is, the data is not appended, but will be stored at the specified offset.


UTF-8 support
-------------

SFTPPlus will always use the UTF-8 encoding for file names and paths.

Support for UTF-8 is advertised by the FTP server in the response of the
FEAT command and `OPTS UTF8` command is supported as well.


.. _operation-ftps-ccc:

Usage of the CCC (Clear Command Channel) command
------------------------------------------------

The CCC command is defined in `RFC 2228 <https://tools.ietf.org/html/rfc2228>`_
and `RFC4217 <https://tools.ietf.org/html/rfc4217>`_.

If the server and client support the CCC command, it can be used to revert a
control channel connection protected using SSL/TLS to plain text mode, no
security.

The usage of the CCC decreases the security of the connection.

Most firewall devices can only inspect unencrypted PASV/PORT commands in order
to open the expected data port (port negotiated by server-client) in an
automatic manner.

The usage of the CCC can be avoided by defining a static port range for the
data connections.

If static port range for the data connection does not meet your requirements,
the usage of the CCC command can be used to implement an authentication
process which is still secured by TLS/SSL.

In most of the scenarios, the CCC command is used to shut down the SSL/TLS
layer after the authentication step.
The rest of the control channel communication will be done over an unencrypted
connection.

On the **server-side**, when the CCC command is requested by a client,
the SFTPPlus server will always initiate the SSL/TLS shutdown,
after the reply is sent to the client.
That is, the reply to the CCC command is still sent over a protected
connection.

On the **client-side**, while the CCC command takes no argument,
it can be implemented in two modes:

* **passive mode** - client-side will not initiate the shutdown,
  but instead, wait for the server-side to do it.
  Will not reply to the shutdown from the server

* **active mode** - not supported yet - client-side initiates the shutdown
  and waits for a reply from the server, before sending further commands.


Date and time handling
----------------------

SFTPPlus will display the modified date and time of a file using the format
of the Unix `ls` command.

The date and time are displayed using the server's local timezone.

Files and folder modified in the current year will have the year omitted and
will show the time with a precision of seconds, include hour and seconds.

Here is an example for a file and folder for current year::

    -rw-rw-r--   1 John      srv           18 Sep 04 11:26 test_file
    drwxrwxr-x   2 Mark      adm         4096 Aug 13 12:01 remote_get_dir

When the files or folders are modified in the previous years, the result
will include the modified year but will omit the time.

Here is an example for a file and folder for previous years::

    -rw-rw-r--   1 John      srv           18 Feb 28 2014 test_file
    drwxrwxr-x   2 Mark      adm         4096 Apr 17 2012 remote_get_dir

MLST, MLSD and other commands designed for machine processing
will show the time in UTC timezone as specified in the RFCs.


Listings for Machine Processing (MLST and MLSD)
-----------------------------------------------

As documented in `RFC 3659 <https://tools.ietf.org/html/rfc3659#section-7>`_,
the MLST and MLSD commands are intended to standardize
the file and directory information returned by the FTP server.

The following facts (file attributes are supported):

* size
* type, with `OS.unix=slink` for symbolic links.
* perm
* modify
* unique

When MLST is requested, the full path is always displayed.

When MLSD is requested the target directory is displayed with full path,
while all members are the target directory are displayed with only their
names.

When requesting MLSD for a file, the server will respond with a more
specific `550 Requested action not taken: /path is not a directory` error,
rather than `501 Syntax error in parameters or arguments` as documented in
the RFC.


SSL certificate-based authentication
------------------------------------

SSL certificate-based authentication allows clients to authenticate using
username and SSL certificate pair credentials.
A password is no longer required in this case.

This applies to both implicit FTPS (FTPIS) and explicit FTPES (FTPES) and is
not available for plain FTP.

Note that while the page references SSL certificate authentication,
the certification in question is the PKI X.509 certificate format.

If you are intending to generate an X.509 SSL self-signed certificate and/or
implementing mutual X.509 SSL authentication using only self-signed
certificates please go to the
:doc:`Q and A section for the FTP and FTPS Service </q-and-a>`.

To enable SSL certificate-based authentication, set the following option inside
the FTP/FTPS service configuration section (located by default in
configuration/server.ini)::

    [services/03288e36-cf6b-4bd5-a9be-f421372f17e6]
    type = ftp
    name = FTPS Explicit Server
    ftps_explicit_enabled: Yes

    enable_ssl_certificate_authentication = Yes

In the Local Manager FTPS services configuration, set to
`Enable SSL certificate-based authentication`.

This option is enabled by default, so you should already have this option set.

FTPS clients who want to authenticate using username and SSL certificate will
have to send an SSL certificate signed by an allowed Certificate Authority
(CA), as configured by the `ssl_certificate_authority` configuration option.
The SSL certificate presented by the client should have the value of the
Common Name (CN) field match the authenticated username.

Each account should have `allow_certificate_authentication = yes`
(Allow SSL certificates` in Local Manager) or enabled by group inheritance.

Based on the following account configuration, SSL certificate authentication
is enabled, and FTPS clients should provide a certificate issued for
CN ``JohnD`` ::

    [accounts/03288e36-cf6b-4bd5-a9be-f421372f17e6]
    name = JohnD
    allow_certificate_authentication = Yes

The CN field and username matching is case-sensitive.
A certificate issued for CN ``JohnD`` will not be valid for an account
with name ``johnd`` (all lowercase).

Setting `enable_ssl_certificate_authentication = No` will disable SSL-based
authentication and accounts will have to authenticate using other methods,
like username and password.

After disabling SSL certificate-based authentication, you must check that
password-based authentication is enabled.
Otherwise, clients will have no other authentication method available to log
in::

    [services/03288e36-cf6b-4bd5-a9be-f421372f17e6]
    type = ftpsi
    name = FTPS Implicit Server

    enable_ssl_certificate_authentication = No
    enable_password_authentication = Yes


Password-based authentication
-----------------------------

Password-based authentication is the most common authentication method used
with FTP and FTPS.

To enable/disable it use the `enable_password_authentication` configuration
option available for each FTP or FTPS services.

When disabling password authentication, make sure other authentication methods
are enabled.
For example, the following configuration disables password authentication
and enables SSL-based authentication::

    [services/03288e36-cf6b-4bd5-a9be-f421372f17e6]
    name = FTPS Implicit Server
    type = ftpsi

    enable_password_authentication = no
    enable_ssl_certificate_authentication = Yes


User password change
--------------------

You can configure an account to allow updating its own password.
When enabled, users can change their password over the FTP and FTPS protocol
using the `SITE PSWD` command.

To change the password, users must provide the current password.

When changing the password, both current and new passwords are provided in
text format.

Here is an example of changing the current password
`correcthorsebatterystaple` to new password `Ltime@go-inag~faaa!`::

    SITE PSWD correcthorsebatterystaple Ltime@go-inag~faaa!

If the current or new password contains a space character, both passwords need
to be enclosed in double quotes and separated by a single space.
The double quotes characters from the password does not need to be
escaped in any way:

Here is an example of changing current password `Ex1st"n0w"` with
`Wow doestcst`. Note that the current password contains double quotes
characters::

    SITE PSWD "Ex1st"n0w"" "Wow doestcst"

..  note::
    The current or new passwords can't contain the `" "` string
    (double quotes followed by one space, followed again by double quotes).


Load Balancer
-------------

The FTP/FTPS services of SFTPPlus can be integrated in a DNS-based
load balancing solution.

FTP/FTPS services can function behind a layer 4 load balancer,
as long as **only active data connections** are used.

SFTPPlus requires no extra configuration when using a layer 4 TCP balancer
with active data connections.

When functioning behind a DNS load balancer,
each FTP/FTPS node needs to have the `passive_address` configured to its
own IP.

You can't use a layer 4 TCP load balancer with **passive data connections**.
This is because SFTPPlus server will use 2 independent connections
for a passive data connection,
one for the FTP command and the other for the FTP data.

With load balancing it is possible that those 2 connections
are sometimes directed to 2 different SFTPPlus servers.

For passive data connection we recommend using a **DNS load balancer** or
switch to using the SFTP protocol.

AWS Network Load Balancer and Azure Load Balancer are examples of layer 4
load balancers.
