General location options
========================

..  contents:: :local:


Introduction
------------

A location configuration provides the required information to allow
SFTPPlus to connect to local or remote locations in order to perform
file transfers between locations.

Please consult the `type` configuration option to see the list of
supported location types.

Locations are auto-started when a transfer or another component needs them and
the location is not started and connected.

They are also fault-tolerant, allowing retries for interrupted connections.

Transfers using a failed location will also fail and will
not trigger a new connection attempt for the location.
In this type of scenario, the failed location must be manually started first,
after resolving the initial error.


Adding a new location via Web Manager
-------------------------------------

A new location can be added or changed via Web Manager below.
Options will differ depending on which location type is used.

See below for an example of an initial configuration with the FTPES location.

..  image:: /_static/gallery/gallery-add-ftps-location.png


Adding a new location via text configuration
--------------------------------------------

Adding a new location configuration is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``locations/`` and followed by
the location's UUID.

The location's UUID can be any unique string used to identify the location.
Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/introduction>`.

For example, to add a new location configuration of type `filesystem`
called ``Local file system``::

    [locations/b904e6h6-c295-4ccf-8abd-edcae4d3324f]
    name = Local file system
    description = File system accesses as service account.
    type = filesystem
