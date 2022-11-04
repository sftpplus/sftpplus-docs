Local file system monitor service
=================================

..  contents:: :local:


Introduction
------------

This page describes the configuration options available for the local
file system monitor service.


The service allows monitoring local file systems and emitting audit log events once files or sub-directories are changed inside the monitored path.

If the configured path does not exist, the service will fail to start.

If the configured path to monitor is removed while the service is running,
its content is reported as removed and the service will continue to monitor
the path and wait for it to be created.
The service monitor will not stop or fail.


.. include:: /operation/location-watch-about.include.rst

Below you can find the list of available configuration options for services of
the monitor type, other than the standard service configuration options.

.. include:: /configuration/location-watch.include.rst


file_age_notification
---------------------

:Default value: `0`
:Optional: Yes
:Values: * Number of seconds.
:From version: 4.0.0
:Description:
    Age in seconds after which an event is triggered for files which are
    not modified in that time.

    A separate event is emitted for each file.

    Set it to `0` to disable triggering this type of events.

    It will check for older files based on the `changes_poll_interval`
    configuration.


file_age_auto_delete
--------------------

:Default value: `0`
:Optional: Yes
:Values: * Number of seconds.
:From version: 3.52.0
:Description:
    Age in seconds after which a file is automatically deleted if it is
    still found in the monitored path.

    A separate event is emitted for each deleted file.

    Set it to `0` to disable automatically deleting files.

    It will check for older files based on the `changes_poll_interval`
    configuration.


monitored_operations
--------------------

:Default value: `all`
:Optional: Yes
:Values: * Comma-separated values.
         * `disable`
         * `all`
         * `exist`
         * `create`
         * `modify`
         * `rename`
         * `delete`
:From version: 3.52.0
:Description:
    Comma-separated list of file operations for which to emit notification
    events.

    Each action has a separate event ID.

    Set it to `all` for emitting events for any file operation.

    Set it to `disable` to not emit events for file operations.

    If both `all` and `disable` are defined at the same time, the monitor will
    emit events for all file operations, ignoring the `disable` value.
