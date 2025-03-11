Local file system monitor
=========================

..  contents:: :local:


Introduction
------------

This page describes the configuration options available for the local
file system monitor resource.

The resource allows monitoring local file systems and emitting audit log events once files or sub-directories are changed inside the monitored path.

If the configured path does not exist, the monitor will fail to start.

If the configured path to monitor is removed while the resource is running,
its content is reported as removed and the resource will continue to monitor
the path and wait for it to be created.
The resource monitor will not stop or fail.


.. include:: /operation/location-watch-about.include.rst

Below you can find the list of available configuration options for resources of
the monitor type, other than the standard resource configuration options.

.. include:: /configuration/location-watch.include.rst


retry_count
-----------

:Default value: `5`
:Optional: Yes
:From version: 5.1.0
:Values:
    * 0
    * Positive integer
:Description:
    It is the number of retries in the case the monitored directory is no longer available.
    The retries for a failed source directory, are done after `changes_poll_interval` seconds.
    If the directory is still not available after all retries,
    the whole resource fails and will need to be manually started,
    after investigating the root cause of the error.

    When set to `0`, failed operations are never retried and the
    resource is stopped on first failure.


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
