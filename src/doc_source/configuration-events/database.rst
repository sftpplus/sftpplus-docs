Embedded database
=================

..  contents:: :local:


Introduction
------------

To configure an event handler which persists events using the embedded
SQLite database, use the type `database`.

Multiple embedded databases can be configured for storing different type of
events.

When using the database event handler, SFTPPlus will store / update
the newly generated events in an embedded SQLite3 database file.

The default configuration, will store the logs for the last 7 days.
You can configure the number of days to meet your log retention policy.


SQLite low-level details
------------------------

The default database is stored in a file named `log/server.db3`.
You can configure this name or configure SFTPPlus to store different log types in separate database files.

Inside the SQLite file,
the name of the database used to store the logs is `chevah_log_entries`.
In SQLite, to check all the fields from the table, you can use::

    | sqlite> SELECT * FROM sqlite_master WHERE type='table' and
      name='chevah_log_entries';

To prevent excessive filesystem fragmentation, the size of the SQLite file will never decrease.
When rows are removed they are marked as removed and will be overwritten with new rows.
If you need to claim the free space, you can use the `VACUUM` command.

..  note::
    The SQLite `VACUUM` command cleans the main database by copying its contents to a temporary database file and reloading the original database file from the copy.
    During the execution of this command, the database disk usage might double.

To reclaim the disk space, use the `VACUUM` command::

    sqlite> VACUUM ;

You can use the SFTPPlus SQLite file with your own tools and script to implement custom reporting or task.

.. include:: /configuration-events/events-commons.include.rst


path
----

:Default value: ''
:Optional: No
:Values: * Path on the local filesystem.
:From version: 4.0.0
:Description:
    UUID of the database to which the logs are sent.


auto_delete
-----------

:Default value: 0
:Optional: Yes
:Values: * Number of days
:From version: 3.42.0
:Description:
    Define the number of days after which older events are automatically
    removed from the database.

    Set it to `0` to keep all events, regardless of their age.

    ..  note::
        The removal of older entries is done when the handler starts
        and every 4 hours.
