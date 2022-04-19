Server Events
=============

While the server is operational, it will generate a set of events based on
performed operations.
These events can be used for auditing and logging purposes.

An event can be logged into a log file, and the log file can be used later
for audit tasks.

Those conducting an audit or administrators wishing to be further informed of
the audit trail can cross-reference Event IDs (such as `20137`) found in the
logs.

To be further informed about the event ID's group (such as `informational` for
the `20137` event ID), search for the name in the Server Event Group page.

For configuring the server to react when an event occurs, please see
:doc:`the dedicated page</configuration/event-handlers>`.


..  toctree::
    :maxdepth: 1

    events
    groups
