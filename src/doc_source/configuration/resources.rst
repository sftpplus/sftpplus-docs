Resources
=========

..  contents:: :local:


Introduction
------------

SFTPPlus can interact with various external resources in order to execute
related operations, such as sending emails on errors.

The resources are shared for different server operations.
For example the email client can be used for both critical errors or to
inform about a normal operation.

When a component inside the SFTPPlus requires a resource, and the resource
is not already running, that resource is automatically started.

The configurations for the available resources are automatically created when
SFTPPlus starts.

A default SQLite database is enabled in each SFTPPlus installation and has
UUID `DEFAULT-SQLITE`.
This default SQLite database is used by SFTPPlus to provide certain
functionalities like the `Account activity` report or keeping track of the
transferred files to prevent duplicate transfers.


Generic resource options
------------------------

While additional options are available (depending on the resource type),
each resource configuration section has the following standard
configuration options:


name
^^^^

:Default value: ''
:Optional: No
:From version: 3.4.0
:Values: * Any text.
:Description:
    Human-readable short string used to identify this resource.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.4.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this resource.


type
^^^^

:Default value: ''
:Optional: No
:From version: 3.4.0
:Values: * `sqlite` - Embedded SQLite database
         * `email-client` - Email client configuration.
         * `lets-encrypt` - Let's Encrypt ACME client.
         * `analytics-engine` - Monitor computer resources used by SFTPPlus.
:Description:
    This option specifies the type of the resource.
