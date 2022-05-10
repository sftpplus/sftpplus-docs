Execute external script or program
==================================

The `external-executable` event handler can be configured to call an external
script or program based on an event.

The following environment variables are available to the executed script or
program:

:EVENT: ID of the event which for which it was called.
:HANDLER_UUID: UUID of this event handler.
:COMPONENT_UUID: UUID of the SFTPPlus component which has created the event.
:TIMESTAMP: Unix timestamp when this event was generated.
:PEER: Associated IP and PORT
:USER: Associated user / account.
:DATA_*:
    Data members of this event.
    For example `DATA_REAL_PATH` or `DATA_DETAILS`.

SFTPPlus will only call a maximum of 3 external commands in parallel.
External commands that need to be triggered for the generated events are queued and executed one after another.
This is done to prevent extreme usage of the OS resources.

Since you can receive 1000 files in a short period of time,
launching 1000 operating system sub-processes at the same time can result in
blocking the whole operating system by using too much memory or too many processes.
For example,
with an external executable using 100MB of memory,
calling 10 concurrent such jobs would result in a 1GB extra memory usage.

The `external-executable` event handler is designed to be used as a notification mechanism
or for calling external commands that are fast and have low-memory usage.
The event handler is not designed to operate as a sub-process manager,
nor for handling of long-running or extensive memory usage processes.

If your external executable uses more than 100MB of memory or takes longer than 10 seconds to operate,
consider redesigning your system.
For example reduce run duration or reduce the run frequency by filtering events with the `target` and `data_filter` options).


executable_path
---------------

:Default value: ''
:Optional: No
:Values: * Local filesystem path.
:From version: 3.47.0
:Description:
    Local filesystem path to the executable.


executable_arguments
--------------------

:Default value: ``{data.real_path}``
:Optional: Yes
:Values: * Plain text.
         * Variable expression.
:From version: 3.47.0
:Description:
    This configuration defines the arguments used to call the executable.

    Make sure the arguments which might contain spaces are enclosed in
    quotes.

    .. include:: /configuration/event-context-variables.rst.include


executable_timeout
------------------

:Default value: 30
:Optional: Yes
:Values: * Number
:From version: 3.47.0
:Description:
    Number of seconds to allow for the external process to execute before
    forcefully closing it.

    A configured value must be equal to or greater than 1.


concurrent_processes
--------------------

:Default value: 2
:Optional: Yes
:Values: * Number
:From version: 3.47.0
:Description:
    Maximum number of concurrent processes to execute at the same time.

    When the event handler is required to handle more events, the remaining
    events are placed in the queue and executed as soon as possible, making
    sure that only the configured number or processes are active at the same
    time.

    A configured value must be equal to or greater than 1.

    We recommend to set this based on the number of available CPUs.
