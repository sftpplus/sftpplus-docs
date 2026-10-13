Standard output stream
======================

The `standard-stream` event handler can be used for formatting the events
for the standard output.

..  contents:: :local:

.. include:: /configuration-events/events-commons.include.rst


output_format
-------------

:Default value: `text`
:Optional: Yes
:Values: * `text`
         * `logfmt`
:From version: 6.1.0
:Description:
    Selects plain text or Logfmt output using the `entry_content` placeholders.
    New handlers created in the Web Manager use `logfmt` by default.
    See :ref:`administration-event-handlers-logfmt` for examples and formatting rules.


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

    Since version 6.1.0, missing `{data.KEY}` values produce empty text.
    Message line breaks are replaced with spaces.
