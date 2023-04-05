Account interaction
===================

The `account-interaction` event handler is used to detect when one account operates on files that are accessible to another account.

It can detect files that are directly configured to an account or inherited from the group.
It detects any file, recursively, both in the home folder path as well as in any shared virtual directories.

It will emit the event with ID `20193` for each operation on any file available to other accounts,
as long as those accounts are enabled.
It will not emit the event `20193` for itself.

Events are only emitted for file operations.
Directory operations are ignored.
Get in touch if you need to receive events for directory operations.

It can be used to trigger email notifications between members of the team or trigger any other file management operation.

..  contents:: :local:

.. include:: /configuration-events/events-commons.include.rst


monitored_operations
--------------------

:Default value: `all`
:Optional: Yes
:Values: * Comma-separated values.
         * `all`
         * `created`
         * `deleted`
         * `read`
         * `moved`
         * `modified`
:From version: 4.25.0
:Description:
    Comma-separated list of file operations for which to emit notification events.

    Set it to `all` for emitting events for any file operation.
    When left empty, it will default to `all`.
    When `all` is set, any other configured value is ignored and will emit events for any file operation.

    The `read` operation is for file downloads.
    The `read` operation is not supported for the local filesystem monitor service.

    The `modified` interaction notification is only supported for the local filesystem monitor service.
