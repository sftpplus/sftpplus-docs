Standard Stream
===============

The `standard-stream` event handler can be used for formatting the events
for the standard output.


entry_content
-------------

:Default value: `{timestamp.iso_8601_local} {id} {component.uuid}
                {account.name} {account.peer.address}:{account.peer.port}
                {message}`
:Optional: Yes
:Values: * Format string.
:From version: 3.31.0
:Description:
    This option defines the format used to represent the event.

    For more information about how to configure the format, check the
    :ref:`entry_content<conf-eventhandlers-local-file-entry-content>`
    option from the Local File event handler.
