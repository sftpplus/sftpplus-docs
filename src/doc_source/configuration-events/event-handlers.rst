Event Handlers
==============

..  contents:: :local:


Introduction
------------

Event handlers are triggered by server events, and each event handler performs
a specific action.

Please see the `type` configuration option for the list of all supported
types of event handlers.
For more information on using event handlers, please see
:doc:`the usage instructions page </guides/event-handlers>`.

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

..  note::
    Check the documentation for the `type` configuration option to get a list
    of all the supported event handlers.


Adding a new event handler via Local Manager
--------------------------------------------

A new event handler can be added or changed via Local Manager below.
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
:doc:`the dedicated UUID documentation </configuration/general>`.

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


Event handler options
---------------------

Each event handler configuration has the following options:


name
^^^^

:Default value: ''
:Optional: No
:From version: 2.10.0
:Values: * Any text.
:Description:
    Human-readable short text used to identify this event handler.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 2.10.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this event handler.


type
^^^^

:Default value: ''
:Optional: No
:From version: 2.10.0
:Values: * `file-dispatcher` - Dispatch a file into one or multiple paths.
         * `http` - HTTP POST request (unsecured).
         * `local-file` - Append events to a file located on the local file
           system.
         * `email-sender` - Send emails as an SMTP client.
         * `windows-eventlog` - Send events to Windows EventLog Service.
         * `standard-stream` - Send events to standard output.
         * `syslog` - Local Unix socket or remote IP:PORT address for Syslog.
         * `create-archive` - Create/Compresses one or more files.
         * `extract-archive` - Extract/Uncompressed a file.
         * `external-executable` - Execute an external script or program.
         * `openpgp` - Encrypt/Decrypt files using OpenPGP.
         * `rabbitmq` - Publish event to RabbitMQ AMQP 0-9-1 server.
         * `extension` - For custom event handlers implemented using our API.
:Description:
    This option specifies the type of the event handler.
    Each type has a set of specific configuration options.
    Please see below for more details.


target
^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of event ids.
         * Comma separated list of event ids starting with an exclamation mark.
         * Leave empty to handle all events.
:From version: 2.10.0
:Description:
    Define a comma separated list of event ids to have the event handler
    triggered only for those events.

    When you want to have it triggered for all the events,
    excepting a few events you should prefix each event id with the exclamation
    mark (!).

    Leave it empty to handle all events.

    ..  note::
        Combining the two methods is not supported as the same result
        can be achieved by allowing only the desired events, all the others
        will be ignored.


groups
^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of event groups.
         * Comma separated list of event groups
           starting with an exclamation mark.
         * Empty.
:From version: 3.39.0
:Description:
    Defines the list of event groups for which this handler
    is active.

    When you want to handle all the events,
    except for the ones from a set of groups,
    prefix the group names with the exclamation mark (!).

    An event can be a member of one or multiple groups.
    The event is handled if any of its groups is found in the list
    of configured allowed groups.
    The event is not handled if any of its groups is found in the list
    of configured ignored groups (starting with !).

    Leave it empty to handle events from all groups.


usernames
^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of usernames.
         * Comma separated list of usernames starting with an exclamation mark.
         * Leave empty to handle all events.
:From version: 3.9.0
:Description:
    Comma separated list of usernames whose events are handled by
    this event handler.
    A username can include OS accounts, application accounts, and any accounts
    accepted by any authentication method including external HTTP accounts.

    When you want to have it triggered for all the events,
    excepting a few events you should prefix each username with the exclamation
    mark (!).

    Leave it empty to handle events from any users or events which are
    not associated with any user.


components
^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of UUIDs.
         * Comma separated list of UUIDs starting with an exclamation mark.
         * Leave empty to handle all events.
:From version: 3.18.0
:Description:
    Comma separated list of component UUIDs for which events are handled by
    this event handler.

    When you want to have it triggered for all the events,
    excepting a few events you should prefix each UUID with the exclamation
    mark (!).

    Leave it empty to handle events emitted by any component.


source_addresses
^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Comma separated list of IP addresses.
         * List of IP addresses starting with an exclamation mark.
         * Empty.
:From version: 3.40.0
:Description:
    Comma separated list of source IP addresses of the remote peers,
    which are handled by this event handler.

    When you want to have it triggered for all the addresses,
    excepting a few addresses you should prefix each address with the
    exclamation mark (!).

    Leave it empty to handle events emitted by any source address.


data_filter
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of data member name and filter expression.
         * Leave empty to handle all events.
:From version: 3.22.0
:Description:
    Comma separated definition with name of attribute data member and
    the targeted matching expression.

    Data member names are configured with insensitive cases.

    For more details about the available expressions see the
    :doc:`matching expression documentation.
    </configuration/matching-expression>`

    The following example will extract the to be matched/filtered value
    from the `path` data member of the event.
    The extracted value is then matched against the ``*/folderA/*`` globbing
    expression::

        [event-handlers/b904ed23-a234-4ccf-8abd-edcae4d3324f]
        data_filter = path, */folderA/*

    See :doc:`the usage instructions </guides/event-handlers>` for
    more operational details.

    You can filter only based on a single data member with a single
    matching expression.

    Leave it empty to not filter based on the event's attached data.


fail_after_errors
^^^^^^^^^^^^^^^^^

:Default value: `10`
:Optional: Yes
:From version: 3.0.0
:Values: * An integer number greater than 0.
         * `0` Disabled.
:Description:
    Number of consecutive errors after which the event handler will
    automatically stop with a failed state.

    Setting this to `0` will disable the feature.
    The event handler will no longer stop regardless of the number of errors
    encountered.
