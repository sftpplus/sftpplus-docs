Configuration principles
========================

..  contents:: :local:


Introduction
------------

The server provides a wide range of configuration options, which can be
managed using one of the following methods:

 * Using the web-based graphical user interface.
   To learn more, please visit the
   :doc:`Local Configuration Manager </configuration/local-manager>` page.
 * Editing the configuration file using your preferred text editor.
   Please see the :doc:`Configuration File</configuration/configuration-file>`
   section for more information.

..  note::
    Parallel configuration using both methods should work, but it is
    not supported.

Following a successful installation, the server will start
with a sample configuration file which enables the Local Manager
service together with the default FTPS and SFTP file transfer services.

You can configure the server starting from this sample configuration file,
using one of the above described configuration methods.

Before proceeding, here are some suggestions regarding which areas one should
start with:

 * Generating new configuration file, SSH keys and self-signed certificates;
 * Customizing the server;
 * Adding services and configuring them according to your needs;
 * Managing groups and users access rights.


Universally unique identifiers
------------------------------

To keep a reference of its entities (servers/accounts/services/groups/etc.),
the server configuration is defined using universally unique identifiers.

While managing the configuration using the Local Manager, you will not have
to generate UUIDs, and most of the time the Local Manager's user interface
will hide the complexity of working with UUIDs.

A universally unique identifier (UUID) is an identifier standard used in
software construction, standardized by the Open Software Foundation (OSF)
as part of the Distributed Computing Environment (DCE).

Here is a sample UUID::

    550e8400-e29b-41d4-a716-446655440000

UUIDs are used by the server to support the renaming of accounts, services,
servers, etc., and to provide a detailed audit of all activities performed by
an entity, even before or after renaming it.

Since UUIDs are designed for computer usage, each UUID has an associated
`name` configuration option.
The `name` option is the human-readable identifier of an entity, and it can
be changed at any time, allowing easy renaming of services, accounts, groups,
etc.

In the context of distributed systems, the usage of UUIDs enables
identifying information without significant central coordination.
This allows the server to participate in a distributed cluster for high
performance or high availability/resilience architectures.

For simple deployments, you can also use any string as a universally unique
identifier, as long as you make sure it is not used for another entity.
We recommend using a universally unique identifier different from the main name
for that entity (account/group/service/etc.), so that later you can perform
rename operations.

We recommend using ``UUIDs`` as per the standard RFC4122 format.

..  note::
    UUID value should not include the forward slash `/` or the vertical bar `|` characters.


Default configuration values
----------------------------

Inside the configuration file, when a configuration option is missing
from a section, the default value is applied.

For example, when the default value for the `enabled` configuration option
is `Yes`, in the following configurations both `implicit_section` and
`defined_section` will have `enabled` set to `Yes`::

    [services/6ff190cc-8d34-4669-a4f9-4d33f7f60a75]
    name = 'implicit_section'

    [services/0d987297-118b-4ad3-94c2-ffb3347fc462]
    enabled = Yes
    name = 'defined_section'

The default value of each configuration option is included as part of the documentation for that option.

When an option is defined as required (`Optional: No`),
it will not have a default value and SFTPPlus will fail to process the component associated with that option.


Comma-separated values
----------------------

Some configuration options allow defining multiple values in CSV
(comma-separated value) format.
When a specific value contains a comma, the whole value should be
enclosed in double quotation marks.
For example, to dispatch to path ``/some/destination,with,commas/`` you
should configure the value as::

    [event-handlers/6ff190cc-8d34]
    dispatch_rule = move, *.pdf, "/some/destination,with,commas/"

When a specific value contains a comma and quote, the whole value should
be enclosed in double quotation marks,
and the quotation character itself be represented as two
consecutive double quotation marks.
For example, to dispatch to path ``/some/new,destination"with"quotes/`` you
should configure the value as::

    [event-handlers/6ff190cc-8d34]
    dispatch_rule = move, *.pdf, "/some/new,destination""with""quotes/"

When a specific value contains only quotes and no commas, you don't need to
enclose the whole value in double quotation marks.
For example, to dispatch to path ``/some/destination"with"quotes/`` you
should configure the value as::

    [event-handlers/6ff190cc-8d34]
    dispatch_rule = move, *.pdf, /some/destination"with"quotes/


.. _absolute-relative-paths:


Absolute and relative paths
---------------------------

When a configuration option requires a path on the local filesystem, the path
can be set as an absolute or relative path.

When relative paths are used inside the configuration file, in all cases,
they will be relative to the server's installation folder.

For example, in the following case `log/server.log` will be either
``/opt/sftpplus/log/server.log`` or, on
Windows, ``C:\Program Files\SFTPPlus\log\server.log``::

    [event-handlers/d7623fb2-4e1f-483e-8599-f5599ac15eb1]
    type = local-file

    path = log/server.log

Similarly, the `ssh_authorized_keys_path` text file configuration will be
expanded to ``/opt/sftpplus/.ssh/authorized_keys`` or, on
Windows, ``C:\Program Files\SFTPPlus\.ssh\authorized_keys``::

    [accounts/1ee4337a-22f7-4a67-9a77-5c3a508a8158]
    name = test_user
    type = application
    enabled = No
    home_folder_path = /home/test_user
    ssh_authorized_keys_path = .ssh/authorized_keys

..  note::
    `ssh_authorized_keys_path` is not expanded to
    ``/home/test_user/.ssh/authorized_keys`` or, on Windows, to
    ``C:\Users\test_user\.ssh\authorized_keys``.


Configuration changes for active connections or users
-----------------------------------------------------

Many of the configuration changes are only applied to newly created
connections or newly authenticated users.
An active connection or a user will not be abruptly disconnected due to a
configuration change.

If you want to enforce a new configuration for all the active users, a full
server restart is required.
This will disconnect all the active connection and users will have to
reconnect and re-authenticate using the new configuration.
