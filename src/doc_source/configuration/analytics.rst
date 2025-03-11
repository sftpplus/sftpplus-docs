Analytics and alerts
====================

..  contents:: :local:


Introduction
------------

The `analytics` resource is defined for monitoring and recording the
activity of SFTPPlus.

For example, it collects last user login information that can be
later retrieved and displayed as a report inside the Web Manager.
The logins span across all services configured on the server (FTP, SFTP,
Web Manager, etc.).

At the configured interval, a dedicated event containing the usage counters
is generated.

Exceptional events are emitted when the usage for a resource hits a certain
value / limit.
These events can be linked with the `email-sender` event handler,
in order to raise alerts over email.

An example for monitoring resource usage every 2 minutes (120 seconds),
triggering an exceptional event
when there are more than 1000 total active connections::

    [resources/03c4-1caf-fee0]
    enabled = yes
    name = Analytics Engine
    type = analytics
    monitor_interval = 120
    connections_count_trigger = 1000


enabled
-------

:Optional: Yes
:Default value: Yes
:Values: * Yes
         * No
:From version: 4.0.0
:Description:
    Set to `Yes` to have the resource monitor enabled.

    Set it to `No` to have the resource stopped.

    You can still manually start and stop the resource from the
    Web Manager.


monitor_interval
----------------

:Default value: 60
:Optional: No
:Values: * Number of seconds
:From version: 3.44.0
:Description:
    Time interval, in seconds, between system resources measurements.

    This value is only used for metrics which require taking constant
    snapshots of the system state.

    Login date, time, and transfer activity is recorded in real time.

    For production environments we recommend setting a value
    equal to or greater than 60 seconds.
    Lower values may impact the overall performance of the system.


memory_resident_trigger
-----------------------

:Default value: 0
:Optional: Yes
:Values: * Number of bytes
         * 0
:From version: 3.44.0
:Description:
    Amount of resident / non-swapped physical memory used by SFTPPlus,
    in bytes, for which to emit an exception event if its process is using
    more than the configured value.

    On Windows, it matches the `Mem Usage` column of the task manager.
    On other OSes, it matches the `RES` column of the `top` command.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


memory_virtual_trigger
----------------------

:Default value: 0
:Optional: Yes
:Values: * Number of bytes
         * 0
:From version: 3.44.0
:Description:
    Total amount of virtual memory used by SFTPPlus, in bytes,
    for which to emit an exception event if its process is using
    more than the configured value.

    This includes both physical memory and swapped memory.

    On Windows, it matches the `VM Size` column of the task manager.
    On other OSes, it matches the `VIRT` column of the `top` command.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


connection_count_trigger
------------------------

:Default value: 0
:Optional: Yes
:Values: * Number
         * 0
:From version: 3.44.0
:Description:
    Total number of connections (server-side and client-side) used by SFTPPlus
    for which to trigger an exceptional event.

    This includes the following connection categories:
    * Incoming connections made to file transfer services
    * Outgoing connections made to remote servers through configured transfers
    * Syslog / HTTP Authentication / HTTP Event Handlers connections
    * Connections made to the Web Manager service.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


file_count_trigger
------------------

:Default value: 0
:Optional: Yes
:Values: * Number
         * 0
:From version: 3.44.0
:Description:
    Total number of local files used by SFTPPlus
    for which to trigger an exceptional event.

    This includes all files opened by SFTPPlus
    as part of file transfer operations or for administrative operations.

    For example, log files used by event handlers are included in this count.

    A single connection can trigger the opening of multiple local files.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


thread_count_trigger
--------------------

:Default value: 0
:Optional: Yes
:Values: * Number
         * 0
:From version: 3.44.0
:Description:
    Total number of threads used by SFTPPlus
    for which to trigger an exceptional event.

    Take into consideration that multiple transfers can use the same thread.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.
