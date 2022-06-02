Windows EventLog
================

This is an event handler that send SFTPlus events to the Windows Eventlog
service.

..  contents:: :local:


Introduction
------------

SFTPPlus can be configured with multiple Windows EventLog event handlers.

The `name` configuration option is used as *Source Name* for the logs.

The name identifier should not include `*`, `?`, `-` and `\\` characters.
Space characters are allowed.

All events are sent to the `Application` category using the
`Informational` level.

The Windows Event ID is the same as the general server event ID.
For more information on server events, please see :doc:`/events/index`.

..  note::
    Our roadmap includes adding configurable log level options.
    Please contact us to find out more about our roadmap progress.

..  warning::
    When using the `-` character in the source name identifier, `Windows
    Event Log Viewer` will display an incomplete name as the source.
    This is a bug in `Windows Event Log Viewer`, and does not affect
    the information stored in the log.
    The detailed view displays accurate data.

.. include:: /configuration-events/events-commons.include.rst
