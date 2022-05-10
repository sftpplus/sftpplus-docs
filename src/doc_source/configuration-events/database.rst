Embedded Database
=================

To configure an event handler which persists events using the embedded
SQLite database, use the type `database`.

Multiple embedded databases can be configured for storing different type of
events.


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
