Local file system monitor service
=================================

This page describes the configuration options available for the local
file system monitor service.

..  contents:: :local:


General description
-------------------

The local file system monitor service allows the server to monitor local
file systems and emit audit log events once files or sub-directories are
changed inside the monitored path.

If the configured path does not exist, the service will fail to start.

If the configured path to monitor is removed while the service is running,
its content is reported as removed and the service will continue to monitor
the path and wait for it to be created.
The service monitor will not stop or fail.


.. include:: /operation/location-watch-about.include.rst


Configuration options
---------------------

Below you can find the list of available configuration options for services of
the monitor type, other than the standard service configuration options.

.. include:: /configuration/location-watch.include.rst


warn_non_modified_files_interval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `0`
:Optional: Yes
:Values: * Number of seconds.
:From version: 3.5.0
:Description:
    Age in seconds after which an event is triggered for files which are
    not modified in that time.

    A separate event is emitted for each file.

    Set it to `0` to disable triggering this type of events.

    ..  warning::
        This option is in the experimental stage.
        It might be changed in future versions in a way which is not backward
        compatible.
