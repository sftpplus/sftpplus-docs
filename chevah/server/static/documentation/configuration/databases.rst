Databases
=========

SFTPPlus can interact with databases in order to perform data
related operations, such as storing audit trails, activity reports, etc.

Supported databases:

* MySQL
* SQLite

The same database can be shared for different server operations.
For example, you can use the same database for audit trail and activity
reports.
You can also use separate databases if you want.

When a database is stopped, all components depending on that database are
paused.


Adding a new database via Local Manager
---------------------------------------

A new database can be added or changed via Local Manager below.

..  image:: /_static/gallery/gallery-add-database.png


Adding a new database via text configuration
--------------------------------------------

Adding a new database configuration is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``databases/`` and followed by
the database's UUID.

The database's UUID can be any unique string used to identify the database.
Once defined, the UUID should not be changed.

For more information, see
:doc:`the dedicated UUID documentation </configuration/general>`.

For example, to add a new database configuration for a `sqlite`
database called ``Staging SQLite``::

    [databases/a904e3a6-a59b-4bbf-8abd-edcae4d3324f]
    name = Staging SQLite
    description = SQLite file used for testing.
    type = sqlite
    path = path/to/sqlite/file.db3


Generic database options
------------------------

While additional options are available (depending on the database type),
each database configuration section has the following standard
configuration options:


name
^^^^

:Default value: ''
:Optional: No
:From version: 2.6.0
:Values: * Any text.
:Description:
    Human-readable short string used to identify this database.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 2.6.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this database.


type
^^^^

:Default value: ''
:Optional: No
:From version: 2.6.0
:Values: * `mysql` - For MySQL databases.
         * `sqlite` - For SQLite database files.
:Description:
    This option specifies the type of the database.


SQLite 3 local database file
----------------------------

To configure an SQLite 3 local database file, use the type `sqlite`.

The configured database requires read/write and table creation permissions,
which for SQLite translates into read/write permissions to the database file
for the account under which the server is running.

If the database file is not present, the server will try to create it.
It will not create its folder if it does not exists.

The tables are automatically created when the connection is initiated for the
first time.


path
^^^^

:Default value: `Disabled`
:Optional: Yes
:Values: * Absolute path to the local database file.
         * Relative path to the server installation folder.
:From version: 2.6.0
:To version: None
:Description:
    Path to the SQLite 3 database file.


MySQL Server
------------

To configure a MySQL database server, use the type `mysql`.

The tables are automatically created and do not need to be
explicitly created.

The account used for running the server requires read/write and table
creation permissions for the configured database.


address
^^^^^^^

:Default value: `127.0.0.1`
:Optional: Yes
:From version: 2.6.0
:Values: * An IP address or a host name.
:Description:
    This option specifies the IP address or the host name of the
    remote MySQL server.


port
^^^^

:Default value: `3306`
:Optional: Yes
:From version: 2.6.0
:Values: * A port number for the MySQL server.
:Description:
    This option specifies the IP port of the remote MySQL server.


username
^^^^^^^^

:Default value: ''
:Optional: No
:Values: * MySQL username.
:From version: 2.6.0
:To version: None
:Description:
    MySQL username used to connect to the MySQL Server.


password
^^^^^^^^

:Default value: ''
:Optional: No
:Values: * Plain text MySQL password.
:From version: 2.6.0
:To version: None
:Description:
    MySQL password used to connect to the MySQL Server.


database
^^^^^^^^

:Default value: ''
:Optional: No
:Values: * Database name.
:From version: 2.6.0
:To version: None
:Description:
    Name of the MySQL database dedicated to this SFTPPlus instance.
