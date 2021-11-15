Terminology
###########

While using this documentation, you will encounter a set of concepts and terms
from the secure file transfer domain.
You may already know and understand some of the terms, while the meaning for
others might be unclear.

This section tries to describe the meaning and usage of these special
concepts and terms.

..  contents:: :local:


AAA
---

AAA refers to Authentication, Authorization and Accounting.
It is a system to mediate and manage network access based on the process of
identifying a user (authentication), granting or denying access to the user
(authorization) and keeping track of the user's activities on the network
resource.


Account
-------

The set of all configurations required to authenticate and authorize a client
session.
Examples of data stored in an account are username, accepted credentials,
home folder, ability to create missing home folders, and list of shared folders.
The account configuration can be stored by the operating
system or can be provided by SFTPPlus.


Application account
-------------------

An account for which the configuration is entirely provided by SFTPPlus.


Client
------

A remote party initiating connections to the server and requesting file
management operations.


Component
---------

Components are the building blocks of the SFTPPlus product used to implement
managed file transfers.

File transfer services, authentication methods, transfers, resources and event
handlers are all components.


Configuration file
------------------

A file on the local file system used for storing configurations for the server
or for a specific service.


Configuration option
--------------------

A distinct entry inside a configuration file describing server behaviour.


Configuration section
---------------------

A group of related options inside the configuration file.
For example, the configuration file can define options for multiple services,
and the set of all options related to a specific service are grouped inside a
configuration section.


Credentials
-----------

A pair of ``username`` / ``secret`` values used for authorizing a
client session.
The ``secret`` can be a password, an SSH key, an SSL private key/certificate,
or it can take other forms.


Event
-----

An event signals that an action has just happened during the product's
operation.
The event is defined by a five digit number grouped together by protocol or
functionality.
Within each event are details about the event message, groups, description,
data and more.
Events can be logged for auditing and alerting purposes.


Event attribute
---------------

When an event is triggered, it will contain a set of attributes providing
details about the event which has just occurred.

Examples of event attributes include `id` which identifies the nature of the
event and `created` which contains the date and time of the event's occurrence.


Event data attribute
--------------------

Each emitted event, besides the standard structured attributes, has an
associated arbitrary data structure known as the `data event attribute`.

While all the other event attributes have a well defined structure which is
the same for all events, the data attribute will differ based on each event.


Event data member
-----------------

The non-fixed event data attribute is composed of multiple event data members.

The data event attribute usually has multiple data members.

For example, a data member found in many of the emitted events is `path`
which contains the path of the associated file or `details` which
contains more details about an error condition.


Event handler
-------------

A component provided by the product which can be linked to a specific event
in order perform a certain operation.

Event handlers can send the event to Windows EventLog, Syslog, or via email.
It can perform operations on files associated with that event.


File path - Absolute
--------------------

An absolute file path contains all subdirectories leading to a folder.
``/home/user1/upload`` is an example leading to the ``upload`` folder.


File path - Relative
--------------------

A relative file path references to the folder's directory name.
``/upload`` is an example where the file path leads to the ``upload`` folder
from a specified default directory.


FTP
---

A standard network protocol used to transfer files from one host to another
over a TCP-based network, such as the Internet or an internal LAN.
For transferring a file, an FTP session requires two separate TCP connections,
one for the commands and another one for the data transfer.
This can complicate the setup of firewalls or network monitoring tools.


FTPS Explicit (AUTH TLS/SSL)
----------------------------

In explicit mode, the FTPS client must **explicitly** request security from the
FTPS server, and then step up to use a mutually agreed encryption method.


FTPS Implicit
-------------

In implicit mode, the FTPS client is immediately expected to challenge the FTPS
server with a TLS/SSL ClientHello message.
If such a message is not received by the FTPS server, the server should drop
the connection.


Home folder
-----------

By default, all accounts are locked into a dedicated home folder and access is
restricted to files and folders within.


Location
--------

This refers to a folder that the software will either watch for new files, in
the case of client use, or will put new files in the case of server use.
These are configurable and can include local or remote folders.


.. _term-mft:

Managed File Transfer (MFT)
---------------------------

This refers to software or service that manages the secure transfer of data
from one computer to another through a network (e.g., the Internet).
MFT software is marketed to corporate enterprises as an alternative to
using ad-hoc file transfer solutions such as FTP, HTTP, and others.
MFT suites are often characterized by functionality for multiple protocols,
encryption, automation, auditability, and integration.


Operating system service
------------------------

This is a long-running background OS process that does not interact with the
user through keyboard, mouse, or monitor.
On Unix-like systems, these services are also called daemons,
while on Windows they are called Windows services.


Operating system account
------------------------

An account based on configuration provided by the operating system.
The operating system can provide a set of information for the account such as
the accepted password or home folder path.
The configuration for an OS account can be extended with custom values provided
by SFTPPlus.


Process
-------

The operating system process under which SFTPPlus is executed.


Protocol
--------

The rules defining how client and server interact for performing file transfer
operations.


Server
------

The sum of all services interacting between them or with external clients in
order to perform file management operations.


Service
-------

A component of the server specialized in performing a well-defined set of
operations.
For example, the FTP service will perform all operations using the
FTP transfer protocol.
The authentication and authorization services provide all operations required
by other services in order to authenticate remote clients.

This should not be confused with the operating system services, such as
the Windows services or the daemons in Unix-like systems.


Session
-------

The sum of all file transfer operations starting with client authentication and
ending with client disconnection.


SFTP
----

A network protocol designed to provide secure file transfer and manipulation
facilities over an SSH transport and session layer.
In contrast with the FTP protocol, SFTP uses the same connection for command
and data transfers. It provides low-level file handling commands such as: open
file, read section from file, close.
On the other hand, FTP only provides a single RETR command which
does all low-level file management.


Transfer operation
------------------

A single file management command taking place inside a client session.
For example, listing the content of a folder is one *transfer operation*,
while downloading the content of a file is another one.


Username
--------

A unique identifier used during the authorization process for a client session.
The username is the key used for validating credentials and retrieving
information for an account.
