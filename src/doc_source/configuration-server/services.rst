Server-side services
====================

..  contents:: :local:


Introduction
------------

This page will describe how to add/remove/change any service supported
by the server.
This includes file transfer services such as an FTPS or an SFTP server,
as well as utility services such as the `Local Manager` service or the local
file system monitor service.

The server can operate an arbitrary number of services,
from a single instance / process.
Multiple services with different or similar configurations can be defined for
the same protocol.


Adding a new service via Local Manager
--------------------------------------

A new service can be added or changed via Local Manager below.
Options will differ depending on which service type is used.

See below for an example of an initial configuration with the SFTP service.

..  image:: /_static/gallery/gallery-add-sftp-service.png


Adding a new service via text configuration
-------------------------------------------

Services are added or removed by editing the configuration file.

Each service requires defining the following configuration options:

* Universally unique identifier (UUID)
* Short unique name
* IP address
* Unique port number
* File transfer protocol type
* A set of configuration options specific to each protocol type.

All configuration options for a service are grouped inside a section.
A section is started by adding a section identifier enclosed by square
brackets.
The section identifier is an arbitrary name containing only
alpha-numeric characters, underline (``_``), or dash (``-``) characters.
No spaces are allowed.

The section identifier should be prefixed with ``services/`` and followed
by the server's universally unique identifier (UUID).

A service UUID can be any unique string used to identify the server.
Once defined, the service UUID should not be changed.
To rename a service, use the ``[services/UUID]`` `name` configuration option.

The service's UUID is used for auditing purposes, i.e. to record renaming
operations, and to allow operating a service in a multi-service/multi-node
clustered environment.

For more information about UUIDs, please see
:doc:`the dedicated UUID documentation </configuration/general>`.

Below is an example of defining an FTPS service configured in implicit mode,
together with an SSH/SFTP service.
`ftps_implicit` is the FTPS service identifier, while `sftp_partners`
is the service identifier for the SSH/SFTP service::

    [services/d1bfcc20-97ec-11e2-9e96-0800200c9a66]
    enabled = Yes
    name = ftps_implicit
    type = ftpsi
    address = 0.0.0.0
    port = 10990
    description = Service used by legacy applications using server's global
        authentication methods.

    ; Other FTP-specific options.
    passive_port_range = 10000 - 11000


    [services/1ee4337a-22f7-4a67-9a77-5c3a508a8158]
    enabled = Yes
    name = sftp_partners
    type = ssh
    address = 0.0.0.0
    port = 10020
    description = Service used by external partners using service specific
        authentication methods.
    authentications = 0022b17a-30a0-4b70, ffa17005-51c2-42f1

    ; Other SSH-specific options.
    ssh_host_private_keys = path/to/ssh.key
    sftp = Yes
    scp = No


On the following sections you will find details about the configuration
options available for all the server-side services.

Each service has its own set of configuration options.
They are described on dedicated pages.


enabled
-------

:Default value: `Yes`
:Optional: Yes
:Values: * `Yes` - to automatically start the service when the server is
           started.
         * `No` - to leave the service stopped when the server is started.
:From version: 1.6.0
:To version: None
:Description:
    When a service is not automatically started, it can still be manually
    started afterwards from the Local Manager.


name
----

:Default value: ``undefined-service-name``
:Optional: No
:Values: * Any text.
:From version: 2.0.0
:To version: None
:Description:
    Human-readable short string used to identify this service.


type
----

:Default value: ''
:Optional: No
:Values: * `ftp` - for FTP and Explicit FTPS services.
         * `ftpsi` - for Implicit FTPS services.
         * `ssh` - for SSH services providing the SFTP and SCP protocols.
         * `http` - for HTTP services.
         * `http-redirect` - for HTTP Redirection services.
         * `https` - for HTTPS services.
         * `monitor` - for local file system monitor services.
         * `manager` - for Local Manager services.

:From version: 2.10.0
:To version: None
:Description:
    The main option which defines what protocol will be used for this service.

    FTP and Explicit FTPS are using the same `ftp` protocol type, since
    both protocols can be served by the same service.

    ..  note::
        The `sftp` option is also available for backward compatibility, and has
        the same effect as the `ssh` option.


protocol
--------

:Default value: ''
:Optional: No
:Values: * See `type` option.
:From version: 1.8.0
:To version: 2.10.0
:Description:
    This is the old option to configure the protocol used by the service and
    should be replaced by the `type` option.

    This option is present to assure backward compatibility.

    ..  note::
        When the `type` option is also defined, this configuration option
        is ignored.


address
-------

:Default value: '127.0.0.1'
:Optional: No
:Values: * Host name resolving to an IPv4 address
         * Fully qualified domain name resolving to an IPv4 address
         * IPv4 address
         * IPv6 address
         * `0.0.0.0`

:From version: 1.7.0
:To version: None
:Description:
    Host name or IP used to listen for incoming connections.

    To accept connections on all available IPv4 interfaces, use the
    `0.0.0.0` address.

    To accept connections on all available IPv6 interfaces, use the
    `::` address.

    ..  note::
        On some operating systems (for example Linux) setting the `address`.
        to `::` will listen to all available IPv6 and IPv4 addresses.

    ..  note::
        This option is ignored for services of type `monitor`.


port
----

:Default value: ''
:Optional: No
:Values: * Port number used for incoming connections.

:From version: 1.7.0
:To version: None
:Description:
    To avoid conflicts between different services on the same local machine,
    this must be a unique port number.
    On Unix-like systems, a root account is usually required for using ports
    below 1024.

    ..  note::
        This option is ignored for services of type `monitor`.


description
-----------

:Default value: ''
:Optional: Yes
:Values: * Any text describing the role of this service.
:From version: 1.8.0
:Description:
    This can be used for attaching notes to a service.


authentications
---------------

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of authentication `UUIDs`.
:From version: 3.2.0
:To version:
:Description:
    Comma-separated list of UUIDs for the authentication methods enabled for
    this service.

    The list should be ordered by priority.
    The service will try to use the first authentication from the list, and
    continue with  the following method if the user is not accepted.

    If this configuration option is empty or is left out the global
    authentication methods are used.

    ..  note::
        This configuration option is ignored for the `monitor` service
        as this service does not authenticate clients.


debug
-----

:Default value: 'No'
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 3.48.0
:Description:
    When enabled, the service will emit events with id `20000`
    containing low-level debug messages for the file transfer protocol.

    Configuration changes are applied only to new connections.
    Existing connections respect the `debug` configuration in use when they
    were initiated.

    ..  warning::
        When this is enabled, emitted events may include used passwords
        in plain text.
