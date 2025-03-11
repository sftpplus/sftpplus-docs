Introduction to event handlers
==============================

..  contents:: :local:


General presentation
--------------------

The most common event handlers are the ones sending events to a specific
destination.
Each destination is configured using an event handler.
Each event handler has its own configuration and is used for sending the
event in a certain format or according to certain rules.

For example, you can configure one event handler to store the logs in
automatically rotated files and another one to send the logs to Windows
Events or a remote Syslog server.

The server can be configured with an arbitrary number of handlers and you
can configure multiple handlers of the same type.

For more information on using event handlers, please see
:doc:`the usage instructions page </guides/event-handlers>`.


Adding a new event handler via Web Manager
------------------------------------------

A new event handler can be added or changed via Web Manager below.
Options will differ depending on which event handler is used.

..  image:: /_static/gallery/gallery-add-event-handler.png


Adding a new event handler via text configuration
-------------------------------------------------

Adding a new event handler is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``event-handlers/`` and
followed by the handler's UUID.

The handler's UUID can be any unique string used to identify the event handler.
Once defined, the UUID should not be changed.

For more information about UUIDs, please see
:doc:`the dedicated UUID documentation </configuration/introduction>`.

For example, to add a new event handler of type `http`
called ``Critical Errors`` to be triggered when events with id
`1345` or id `2456` and by user ``mary`` or ``john`` occur,
you could use this configuration example::

    [event-handlers/b904ed23-a234-4ccf-8abd-edcae4d3324f]
    name = Critical Errors
    description = Send critical errors as HTTP notifications using JSON.
    type = http
    http_content_type = json

    timeout = 30

    target = 1345, 2456
    usernames = mary, john
