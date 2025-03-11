Introduction to server-side file transfers
==========================================

..  contents:: :local:


Introduction
------------

This page will describe how to add/remove/change any service supported
by the server.
This includes file transfer services such as an FTPS or an SFTP server,
as well as utility services such as the `Web Manager` service or the local
file system monitor service.

The server can operate an arbitrary number of services,
from a single instance / process.
Multiple services with different or similar configurations can be defined for
the same protocol.


Adding a new service via Web Manager
------------------------------------

A new service can be added or changed via Web Manager below.
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
:doc:`the dedicated UUID documentation </configuration/introduction>`.

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
