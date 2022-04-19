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


Local File
----------

To configure an event handler which sends events to a local file system,
use the type `local-file`.

Event entries are appended to the file, and the file can be configured to be
rotated by external tools or automatically rotated by the server, based on
size or time rules.
The log format can be specified using the `entry_content` configuration
option.

..  warning::
   Please enable rotation, otherwise the log file can grow to an extremely
   large file.


path
^^^^

:Default value: `log/server.log`
:Optional: No
:Values: * Local path.
         * Local path with variables.
:From version: 2.1.0
:Description:
    This option specifies the path to a file where the events are to be stored.

    You can use a set of variables as part of the path, which will be
    replaced with actual values once the event handler is started.

    For example, to include the hostname in the log file name, you can define
    it as::

        [event-handlers/b904ed23-a234-4ccf-8abd-edcae4d3324f]
        path = /var/logs/sftpplus-{host.name}.log

    The following variables are supported (case-insensitive):

    * `{host.name}` - The name of the host.
    * `{host.fqdn}` - The fully qualified domain name of the host.


rotate_external
^^^^^^^^^^^^^^^

:Default value: `No`
:Optional: Yes
:Values: * Yes
         * No
:From version: 2.1.0
:Description:
    This is used when external applications for rotating the files are
    employed.
    When this option is set, the server will monitor the file
    and will reopen the file handler if the file was moved by an external log
    rotating system.

    ..  note::
        Rotating log files using external applications is not available on
        Windows, as the server will always keep a file handler to the log
        file, which prevents any external application from moving the log file.


rotate_at_size
^^^^^^^^^^^^^^

:Default value: `0`
:Optional: Yes
:Values: * Number of bytes at which the file will be rotated.
         * `Disabled` or 0 to disable rotation based on file size.
:From version: 2.1.0
:Description:
    The server can be configured to handle file rotation by
    itself, based on file size.
    To enable file rotation based on file size, set this to the size for which
    the file will be rotated.
    The size is defined in bytes.
    For example, to enable file rotation at ``10 MB``, you will need to set the
    value of ``10,485,760``.

    ..  warning::
        Size-based rotation is ignored when `rotate_on` is configured.

        In order to enable size-based
        rotation it is required to disable the `rotate_on` configuration option
        by setting value to `Disabled`.


rotate_on
^^^^^^^^^

:Default value: `Disabled`
:Optional: Yes
:Values: * `DAY_NUMBER day-of-month`
         * `HOUR:MINUTES time-of-day`
         * `Disabled`
:From version: 3.13.0
:Description:
    To configure file rotation based on calendar day or daily at certain time,
    set this to the calendar day or time at which the file will be rotated.

    The rotation is only done when the handler is running.
    If the handler is stopped at the time of a configured rotation, it will
    not rotate the file and will only rotate at the next time when it is
    running.

    The calendar day is expressed as an integer number (from 1 to 31) that
    represents the day of a month and the word 'day-of-month'.

    The time is expressed as two integers separated by double colon,
    the first representing the hour (from 0 to 23) and the second
    representing minutes (from 0 to 59).

    The file is rotated each month at the start of the specified day or
    each day at the specified time.
    When configured with `day-of-month` the rotation happens at
    ``00:00 / 12AM`` hour in the rotation day.

    If the month doesn't have the specified calendar day
    (like February doesn't have 30th day), the file will be rotated on
    the last day of the month.

    For example, `2 day-of-month` means rotate the file on the second
    day of every month. ``14:32 time-of-day`` means rotate the file
    every day at 14 / 2PM, 32 minutes and 0 seconds, local time.

    ``31 day-of-month`` means rotate the file on the last day of
    every month (i.e. in April, the file would be rotated on 30th
    April).
    ``30 day-of-month`` means rotate the file on 30th day of each month
    (but in February it would be rotated on the last day).

    When a file is rotated, the base file is renamed, and its new file
    name is formatted using the following format
    `base-file-name.YYYY-MM-DD` for monthly-based rotation or
    `base-file-name.YYYY-MM-DDThhmmss.sssss` for daily-based rotation.
    `base-file-name` is replaced with base log file name (e.g. `server.log`),
    `YYYY` is replaced with the current year,
    `MM` is replaced with the current month,
    `DD` with the current day of the month,
    `hh` with the current hour,
    `mm` with current minute and
    `ss.ssssss` with current second and microsecond.

    For example, if the base file name is `server.log` and today is
    10th August 2016, the rotated file is named ``server.log.2016-08-10``.
    For daily rotation at 14:30, the file is named
    ``server.log.2016-08-10T143000.000``.

    If the rotated log file with such name already exists, then it is
    replaced by the newest file.

    ..  warning::
        To enable rotation based on calendar day or time of day it is required
        to disable the`rotate_external` configuration option.


rotate_count
^^^^^^^^^^^^

:Default value: `0`
:Optional: Yes
:Values: * number
         * `0` to keep all rotated files.
         * `-1` to enable rotation in place.
:From version: 2.1.0
:Description:
    This option defines whether to keep all rotated log files, to rotate the
    log file in place or to keep the only certain amount of rotated log
    files.

    By default, all rotated log files are kept.

    If log rotation in place is enabled, then on rotation, the log
    file content is removed and no rotated file is created.

    If it is configured (using an positive integer number) to keep specific
    number of rotated files, the oldest rotated log files are deleted.

    When `rotate_at_size` is enabled, rotated file names will contain the
    rotation number appended to the base file name.
    For example, with this configuration::

        [event-handlers/b904ed23-a234-4ccf-8abd-edcae4d3324f]
        rotate_count = 5
        path = log/app.log

    You would get ``log/app.log``, ``log/app.log.1``, ``log/app.log.2``, up to
    ``log/app.log.5``.
    The file being written to is always `log/app.log`.

    When `rotate_on` is enabled, rotated file names will contain
    ``YEAR-MONTH-DAY-HOUR-MINUTE-SECOND`` appended to the base name.

    For a file rotated at ``2012-04-25 15:34:00`` with a base file name
    ``log/app.log``, the rotated file name will be
    ``log/app.log.2012-04-25-15-34-00``.


.. _conf-eventhandlers-local-file-entry-content:

entry_content
^^^^^^^^^^^^^

:Default value: `{timestamp.iso_8601_local} {id} {component.uuid}
                {account.name} {account.peer.address}:{account.peer.port}
                {message}`
:Optional: Yes
:Values: * Format string.
:From version: 3.13.0
:Description:
    The log format can be configured using a format string.
    By default, every line starts with the event id but this can be changed.
    For example, to show the date first, only the peer address and a Unix
    newline::

        [event-handlers/b904ed23-v254-4ccf-8abd-edcae4d3324f]
        entry_content = {timestamp.cwa_14051} {id} {account.peer.address}
        {message} {LF}

    If the format string does not end with a newline character
    (``{LF}`` or ``{CR}{LF}``) it will be added accordingly to the current
    platform (i.e. ``LF`` on Unix-like systems and ``CR+LF`` on Windows).

    .. include:: /configuration/event-context-variables.rst.include

..  note::
    This configuration is ignored if the ``structured_fields`` option is set.


structured_fields
^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma separated event fields.
:From version: 3.21.0
:Description:
    When this configuration option is defined, the log handler will store
    log entries in a CSV file with the header being the field names.

    The value should be a comma separated list of fields such as::

        [event-handlers/b904ed23-v254-4ccf-8abd-edcae4d3324f]
        structured_fields = timestamp.cwa_14051, id, account.peer.address,
        message

    Leaving this option empty disables CSV logging.

    The `entry_content` configuration is ignored when the option is not empty.

    ..  note::
        When changing this configuration, the header will only be written when
        it is opening a new file.

    .. include:: /configuration/event-context-variables.rst.include


Standard Stream
---------------

The `standard-stream` event handler can be used for formatting the events
for the standard output.


entry_content
^^^^^^^^^^^^^

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


Windows EventLog Event Handler
------------------------------

SFTPPlus can be configured with multiple Windows EventLog event handlers.

The `name` configuration option is used as *Source Name* for the logs.

The name identifier should not include `*`, `?`, `-` and `\\` characters.
Space characters are allowed.

All events are sent to the `Application` category using the
`Informational` level.

The Windows Event ID is the same as the general server event ID.
For more information on server events, please see :doc:`/events/index`.

..  note::
    Our roadmap includes adding configurable log level options.
    Please contact us to find out more about our roadmap progress.

..  warning::
    When using the `-` character in the source name identifier, `Windows
    Event Log Viewer` will display an incomplete name as the source.
    This is a bug in `Windows Event Log Viewer`, and does not affect
    the information stored in the log.
    The detailed view displays accurate data.


HTTP POST Event Handlers
------------------------

The HTTP POST Event Handler is where you can integrate SFTPPlus with your
web resource.
To read more, please go to
:doc: `the Developer Documentation </developer/http-api-event-handler>`.

In this section you will find the configuration option available to the
`http` event handler.


url
^^^

:Default value: ''
:Optional: No
:Values: * `URL`
         * Comma separated list of URLs (Since 3.51.0)
:From version: 2.10.0
:Description:
    Full URL for a resource used to receive the event details.
    For example: ``http://www.acme.io/http-post-hook-url``

    You can define a fall-back/redundant URL using a comma separates list of
    URLs.
    The first URL from the list will be used. When failing to get a response
    for the first URL, the remaining URLs are tried.
    Since 3.51.0.


timeout
^^^^^^^

:Default value: `120`
:Optional: Yes
:Values: * Number of seconds.
:From version: 4.16.0
:Description:
    Duration, in seconds, to wait for a response from the HTTP server.

    If a response is not received during this period, the event handling fails.


retry_count
^^^^^^^^^^^

:Default value: `2`
:Optional: Yes
:From version: 3.48.0
:Values:
    * 0
    * Positive integer
:Description:
    This is the number of times a failed request is retried.

    When set to `0`, requests are never retried.

    The HTTP POST request is retried on connection errors or when the server
    returns a 5XX HTTP code.


retry_increase
^^^^^^^^^^^^^^

:Default value: `10`
:Optional: Yes
:From version: 3.48.0
:Values:
    * 0
    * Positive real number
:Description:
    Number of seconds to add to each wait period before retrying.

    This is also the value of the first retry wait period.

    When set to `0`, there will be no waiting time, a retry is performed
    right away.


username
^^^^^^^^

:Default value: ''
:Optional: yes
:From version: 3.30.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote HTTP server.

    Leave this value empty in order to leave out HTTP Basic authentication.

    ..  warning::
        For now, only HTTP Basic authentication is supported.
        This will send the username and password in clear text.


password
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.30.0
:Values: * Plain text password.
         * Empty.
:Description:
    Password associated with the configured `username`.


http_content_type
^^^^^^^^^^^^^^^^^

:Default value: `json`
:Optional: Yes
:Values: * `custom`
         * `json`
         * `legacy-webadmin`
         * `soap`
         * `xml`
:From version: 3.0.0
:Description:
    Format used to send the event over HTTP.

    Use `custom` to send the event as a custom Jinja2 template formated value.

    Use `json` to send the event as JSON formated.

    Use `soap` to send the event as human readable XML SOAP envelope.

    Use `xml` to send the event as machine readable application/xml.

    Use `legacy-webadmin` to send the events to the SFTPPlus WebAdmin server.

.. include:: /configuration/ssl.include.rst


expected_response
^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Empty
         * Matching expression (globbing or regular expression)
:From version: 4.2.0
:Description:
    If the result result of a web-hook is not returned by the
    server with the HTTP status header, but by the content of the
    response, you can use this configuration to define an
    expected expression for a valid response.

    You can read more about how to use this configuration
    :doc: `in the HTTP API Developer</developer/http-api-event-handler>`
    documentation page.

    Leave this configuration empty to accept any response.


headers
^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Header-Name: Header-Value
         * Multiple headers on separate lines
:From version: 4.2.0
:Description:
    This defines a set of extra headers which are sent with each HTTP request.


extra_data
^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * JSON string with variables.
         * EMPTY
:From version: 3.38.0
:Description:

    When left empty the HTTP request is sent using the standard SFTPPlus format
    associated with each content type.

    When this is defined, it will be configured as a template used to send the
    body of the HTTP request.

    When defined for `json` content, it defines the extra JSON values to be
    included in the HTTP POST payload.

    The JSON can be nested and contain multiple objects/dictionaries.
    The root JSON object can't be an array.

    JSON key and values can contain variables which will be replaced based
    on the event's data.

    For example to send the event as an Slack Incoming WebHook message::

        [event-handlers/b904ed23-v254-4ccf-8abd-edcae4d3324f]
        url = https://hooks.slack.com/services/n2unjSpQQ4L6JIOrHoO9CKXl
        http_content_type = json
        extra_data = {
            "text": "{id} {message}"
            "username": "{account.name}"
            }

    To send the event as custom text message::

        [event-handlers/b904ed23-v254-4ccf-8abd-edcae4d3324f]
        url = https://hooks.slack.com/services/n2unjSpQQ4L6JIOrHoO9CKXl
        http_content_type = custom
        headers = Content-Type: text/plain
        extra_data = New event with ID {id} from {account.name}. {message}

    For more details and examples see the :doc:`HTTP API
    documentation.</developer/http-api-event-handler>`

    Below you can find all the available variables.

    .. include:: /configuration/event-context-variables.rst.include

    Not available for `http_content_type = legacy-webadmin`.

    You can define a fall-back/redundant URL using a comma separates list of
    URLs.
    The first URL from the list will be used. When failing to get a response
    for the first URL, the remaining URLs are tried.


Syslog Event Handler
--------------------

To configure an event handler which sends events to a Syslog server, use
the type `syslog`.

It can send logs to a local Unix socket, for example ``/dev/log``, or to a
remote ``IP:PORT`` address.

All messages are logged with the ``daemon`` facility and ``info`` severity.
They are formatted conforming to
`RFC 3164 <https://tools.ietf.org/html/rfc3164>`_, also known as syslog-bsd.
Messages can be plain 7-bit ASCII or UTF-8 encoded.

The process name used when formatting the message is configurable via the
[server] option.

When using TCP and the connection to the server is lost, it will try to
reconnect and will not handle any event until the connection is established.


url
^^^

:Default value: Empty
:Optional: Yes
:From version: 3.8.0
:Values: * `file://some-relative/path`
         * `file:///an/absolute/path`
         * `tcp://address:port`
         * `tcp://address`
         * `udp://address:port`
         * `udp://address`
:Description:
    This option specifies the location of the Syslog server.

    It supports local Unix domain sockets defined as relative or absolute paths,
    as well as TCP or UDP addresses.
    The `file://PATH` configuration is only supported on Linux and macOS.

    UDP support is implemented based on
    `RFC 5424 <https://tools.ietf.org/html/rfc5424>`_.
    When no port is specified for UDP, it will use `514` as the default port.

    TCP support is implemented based on
    `RFC 6587 <https://tools.ietf.org/html/rfc6587>`_
    When no port is specified for TCP, it will use `601` as the default port.


Embedded Database
-----------------

To configure an event handler which persists events using the embedded
SQLite database, use the type `database`.

Multiple embedded databases can be configured for storing different type of
events.


path
^^^^

:Default value: ''
:Optional: No
:Values: * Path on the local filesystem.
:From version: 4.0.0
:Description:
    UUID of the database to which the logs are sent.


auto_delete
^^^^^^^^^^^

:Default value: 0
:Optional: Yes
:Values: * Number of days
:From version: 3.42.0
:Description:
    Define the number of days after which older events are automatically
    removed from the database.

    Set it to `0` to keep all events, regardless of their age.

    ..  note::
        The removal of older entries is done when the handler starts
        and every 4 hours.


.. _conf-handler-email-sender:

Email Sender
------------

To configure an event handler which sends emails to an SMTP server, use the
type `email-sender`.

The emails will be sent over SMTP or ESMTP and SFTPPlus will act as an
SMTP client.

The emails will be sent using a resource of type
:ref:`Email Client<conf-resource-email-client>`.


email_to_recipients
^^^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of email addresses.
:From version: 3.4.0
:Description:
    Comma separated list of addresses where to send emails.

    If this list is not defined, emails will be sent using the general
    email resource recipients configuration.


email_cc
^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of email addresses.
:From version: 3.44.0
:Description:
    Comma separated list of secondary recipients whose names are visible
    to one another and to the primary recipients.

    Leave it empty to not use CC.


email_bcc
^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma separated list of email addresses.
:From version: 3.44.0
:To version: None
:Description:
    Comma separated list of tertiary recipients whose names are invisible
    to each other and to the primary and secondary recipients.

    Leave it empty to not use BCC.


email_associated_files
^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Empty
         * `attachment`.
:From version: 3.18.0
:Description:
    When set to `attachment`, an email (as multi-part MIME) is sent
    with the associated file as an attachment.
    The file path is taken from the `real_path` property of an event data.

    The maximum allowed file size equals to 5MB.
    If the file can't be attached or is larger than 5MB, then the email is
    not sent and an audit event is created for this failure.

    When set to the empty value, an email is sent without an attachment.


email_subject
^^^^^^^^^^^^^

:Default value: ``[{id}] [{component.name}] New event from SFTPPlus``
:Optional: No
:Values: * Plain text.
:From version: 3.4.0
:Description:
    Template used for the subject field of the sent email.

    The `email_subject` can be configured using a format string like
    ``New Event {id} from {account.name}``.

    .. include:: /configuration/event-context-variables.rst.include


email_body
^^^^^^^^^^

:Default value: ``[{timestamp.cwa_14051}] {message}{LF}{LF}{data_json}``
:Optional: Yes
:Values: * Plain text.
:From version: 3.18.0
:Description:
    Template used for the body of the sent email.

    .. include:: /configuration/event-context-variables.rst.include

    Using these variables the `email_body` can be configured, for
    example, like the following::

        [event-handlers/b9787c72-2c8b-4725-a049-ee628aa0abc1]
        email_body = {id} {message}{LF}{LF}{data_json}


File Dispatcher
---------------

The `file-dispatcher` event handler can be configured to handle files to one
or multiple directory paths based on a matching expression.

This section describes the available configuration options.
For more details about the scenarios in which you can use this event handler,
check :doc:`the file dispatcher usage guide.</guides/file-dispatcher>`


dispatch_rules
^^^^^^^^^^^^^^

:Default value: ''
:Optional: No
:Values: * ``dispatch-action, file-match-expression, destination-path-1``
         * ``dispatch-action, file-match-expression, path-1, path-2``
         * ``dispatch-action, file-match-expression``
         * List of rules, separated by newlines.
:From version: 3.5.0
:Description:
    This is a comma separated configuration value.

    First value is the file dispatching action.
    The supported actions are:

    * `move`
    * `move-with-timestamp`
    * `rename`
    * `rename-prepend-unixtime`
    * `delete`
    * `copy`
    * `execute`
    * `ignore`

    Second value is the the full path matching expression. `Globbing expression
    <http://en.wikipedia.org/wiki/Glob_%28programming%29>`_ or
    `regular expression <http://en.wikipedia.org/wiki/Regular_expression>`_
    can be used.
    For more details see the :doc:`matching expression
    documentation.</configuration/matching-expression>`

    The remaining values are paths to which the file is dispatched.
    The file is dispatched into the configured destinations observing the
    configured order.
    Certain actions do not need a destination path.

    When regular expressions are used for the path matching configuration,
    the destination path can be dynamically generated
    based on regex matching groups and event specific variables.

    .. include:: /configuration/event-context-variables.rst.include

    For more details see
    :doc:`the file dispatcher usage guide.</guides/file-dispatcher>`

    You can specify multiple rules, one per line.
    Leading and trailing spaces are ignored.


retry_count
^^^^^^^^^^^

:Default value: `0`
:Optional: Yes
:From version: 4.5.0
:Values:
    * 0
    * Positive integer
:Description:
    This is the number of times a failed file dispatching actions is retried.

    When set to `0`, failed actions are never retried.


retry_wait
^^^^^^^^^^

:Default value: `60`
:Optional: Yes
:From version: 4.5.0
:Values:
    * 0
    * Positive integer
:Description:
    Number of seconds to wait before retrying a failed action.

    When set to `0`, there will be no waiting time.
    As soon as a file action fails, it will be retried.


executable_timeout
^^^^^^^^^^^^^^^^^^

:Default value: 30
:Optional: Yes
:Values: * Number
:From version: 4.15.0
:Description:
    Number of seconds to allow for the external process to execute before
    forcefully closing it.

    A configured value must be equal to or greater than 1.


fallback_rule
^^^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * ``dispatch-action, destination-path-1``
         * ``dispatch-action, path-1, path-2``
         * ``dispatch-action``
:From version: 3.5.0
:Description:
    This is a comma separated configuration value.

    This is a single rule which defines how to dispatch files which were not
    matched by any of the rules defined at `dispatch_rules`.

    Leave it empty to do nothing for files which don't match any expression.

    First value is the file dispatching action.
    It supports all actions from `dispatch_rules`.

    The remaining values are paths to which the file is dispatched.
    The files are dispatched using the same process as for `dispatch_rules`.


matching_expressions
^^^^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: No
:Values: * attribute name, regular expression
         * List of rules, separated by newlines.
:From version: 4.0.0
:Description:
    This is a comma-separated configuration value.

    First value is the name of the attribute from which to collect data for the
    rename operations.

    Second value is the full path matching expression. `Globbing expression
    <http://en.wikipedia.org/wiki/Glob_%28programming%29>`_ or
    `regular expression <http://en.wikipedia.org/wiki/Regular_expression>`_
    can be used.
    For more details see the :doc:`matching expression
    documentation.</configuration/matching-expression>`

    You can specify multiple rules, one per line, to source the rename
    operation from multiple values.
    Leading and trailing spaces are ignored.


dispatch_attribute
^^^^^^^^^^^^^^^^^^

:Default value: `real_path`
:Optional: Yes
:Values: * Event data member name.
:From version: 3.20.0
:Description:
    This is the name of the event's data attribute used to get the path
    or the list of paths which will be dispatched by this event.

    This is a case-insensitive value.


dispatch_delay
^^^^^^^^^^^^^^

:Default value: `0`
:Optional: Yes
:Values: * Number of seconds.
:From version: 4.2.0
:Description:
    Number of seconds to delay the execution of the dispatch action.

    If the targeted file no longer exists after the delay, the
    dispatch execution is canceled and an event is emitted.

    Set it to 0 to execute the dispatching right away.


destination_temporary_suffix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 4.8.0
:Values: * Empty.
         * Short text.
:Description:
    Allows copying or moving a file to the destination using a temporary name,
    renaming to its initial name once all the file's content was processed.

    Leave it empty to always copy a file to its destination using
    the original name.

    ..  note::
        The temporary name is only used for copy or move operations.
        It it not used for rename or delete operations.


overwrite_rule
^^^^^^^^^^^^^^

:Default value: `fail`
:Optional: Yes
:From version: 4.8.0
:Values:
    * `fail` - abort dispatching if destination file already exists.
    * `overwrite` - always overwrite existing files with the content
      of the new source files.
    * `disable` - don't check for existing file and always try to handle the
      file.
    * `skip` - don't dispatch the source file when destination exists.

:Description:
    Rule used to decide how to handle the overwriting of an
    existing file at the destination.

    When set to `overwrite` it will emit an event when the destination
    file is overwritten.

    When set to `skip` it will not handle the file and the source file
    is not removed.
    An event is emitted to inform that the file was skipped.

    When set to `fail` the event handling will fail.
    The existing file is not overwritten and the source files are not
    removed.


create_destination_folder
^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * `parent`
         * Empty
:From version: 3.31.0
:Description:
    This configuration can be used to instruct SFTPPlus to create the
    destination folder, in case they do not exist.

    This is a case-insensitive value.

    Set it to `parent` to create the parent directory of the destination file.

    Leave it empty to not have the destination automatically created and
    fail when destination does not exist.


Create Archive / Compress
-------------------------

The `create-archive` event handler can be configured to create an archive
based on one or more files associated with the event.

When creating archives of format GZIP (.gz extension) if the associated
event has multiple files, it will compress each file as separate archives.

When creating archives of format ZIP (.zip extension) if the associated
event has multiple files, it will compress all files as a single archive.

The create archive event handler only handles direct file paths.
Recursive directory paths are not yet supported.


archive_format
^^^^^^^^^^^^^^

:Default value: `zip`
:Optional: Yes
:Values: * `zip`
         * `gzip`
:From version: 4.7.0
:Description:
    The format used to create the archive.

    The following formats are supported:

     * zip - Standard ZIP file.
     * gzip - GZ archive file - GNU ZIP.


archive_name
^^^^^^^^^^^^

:Default value: `{fullname}{archive_extension}`
:Optional: Yes
:Values: * Single format for both single file and multi file archives
         * SINGLE_FILE_FORMAT, MULTI_FILE_FORMAT
:From version: 4.7.0
:Description:
    This configuration defines the name of the archive to be created.

    By default, it is the name of the file to be archived with the archive
    format extension appended to it.
    For example for archiving the `report.TXT` file as GZIP, the resulting
    archive name is `report.TXT.gz`.

    You can define different configuration options for when the archive
    contains a single file or multiple files.
    This is defined using a comma-separated value.
    The first value is used to define the archive file name for single file
    archives.
    The second value is used to define the archive file name for multi file
    archives.

    For example with the following configuration
    `archive_name = ARC_{fullname}-approve{archive_extension}`
    a single file ZIP archive for the file `report.TXT` is created as
    `ARC_report.TXT-approve.zip`.

    When multiple files are archived and the configuration contains a single
    value, the archive name is based on a random member of the files to be
    archived.

    For example with the following configuration
    `archive_name = ARC_{fullname}.zip, {year.decimal}-archive.ZIP`
    a single file ZIP archive for the file `report.TXT` is created as
    `ARC_report.TXT.zip` while a multi file archive is created as
    `2020-archive.ZIP`

    When defining the file name format the following placeholders are
    supported:

        * {fullname} - Name of the single file, including the extension.
        * {archive_extension} - Extension based on the archive format,
          including the leading dot character.
        * {year.decimal} - Year with century as a decimal number. Example: 2009
        * {year.no_century} - Year without century as a zero-padded decimal
          number. Example: 09
        * {month.decimal} - Month as a decimal number. Example: 9
        * {month.padded} - Month as a zero-padded decimal number. Example: 09
        * {month.name} - Month as locale’s full name. Example: September
        * {month.abbreviated} - Month as locale’s abbreviated name.
          Example: Sep
        * {day.padded} - Day of the month as a zero-padded decimal number.
          Example: 07
        * {day.decimal} - Day of the month as a decimal number. Example: 7
        * {day.of_year_padded} - Day of the year as a zero-padded decimal
          number. Example: 250
        * {day.name} - Weekday as locale’s full name. Example: Friday
        * {day.abbreviated} - Weekday as locale’s abbreviated name.
          Example: Fri
        * {hour.padded_24} - Hour (24-hour clock) as a zero-padded decimal
          number. Example: 16
        * {hour.decimal_24} - Hour (24-hour clock) as a decimal number.
          Example: 16
        * {hour.padded_12} - Hour (12-hour clock) as a zero-padded decimal
          number. Example: 04
        * {hour.decimal_12} - Hour (12-hour clock) as a decimal number.
          Example: 4
        * {hour.am_pm} - Equivalent of either AM or PM.
        * {minute.padded} - Minute as a zero-padded decimal number.
          Example: 05
        * {minute.decimal} - Minute as a decimal number. Example: 5
        * {second.padded} - Second as a zero-padded decimal number.
          Example: 04
        * {second.decimal} - Second as a decimal number. Example: 4


source_attribute
^^^^^^^^^^^^^^^^

:Default value: ``real_path``
:Optional: Yes
:Values: * Event data member name.
:From version: 4.7.0
:Description:
    This is the name of the event's structured data member used to get the
    path which will be handled by this event.

    This is a case-insensitive value.


destination_path
^^^^^^^^^^^^^^^^

:Default value: empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
:From version: 4.7.0
:Description:
    The path where the archive is created.

    Leave it empty to extract the files in the same path as the source file.

    If the destination path already contains the file which is
    going to be extracted, the operation fails and the existing
    file is not overwritten.


overwrite_rule
^^^^^^^^^^^^^^

:Default value: `fail`
:Optional: Yes
:From version: 4.7.0
:Values:
    * `fail` - abort transfer if destination file already exists.
    * `overwrite` - always overwrite existing files with the content
      of the new source files.
    * `disable` - don't check for existing file and always try to transfer the
      file.
    * `skip` - don't transfer the source file when destination exists.

:Description:
    Rule used to decide how to handle the overwriting of an
    existing archive at the destination.

    When set to `overwrite` it will emit an event when the destination
    file is overwritten.

    When set to `skip` it will not handle the file and the source file
    is not removed.
    An event is emitted to inform that the file was skipped.

    When set to `fail` the event handling will fail.
    The existing archive is not overwritten and the source files are not
    removed.


delete_source_on_success
^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `Yes`
:Optional: yes
:Values: * `Yes`
         * `No`
:From version: 4.7.0
:Description:
    Whether to delete the source files after a successful archive creation.

    If creating the archive fails,
    the source is not removed, even when this is set to `Yes`.


Extract Archive / Uncompress
----------------------------

The `extract-archive` event handler can be configured to extract
archive / compressed files to a specific destination.

The event handler will automatically detect the format of the source
file based on its extension.

The following formats are supported:

 * gzip - extract GZ file, e.g. file-name.ext.gz to file-name.ext.
 * tar - extract content of TAR archive to destination path.
 * tar.gz - extract content of TAR.GZ archive to destination path.
 * tar.bz2 - extract content of TAR.BZ2 archive to destination path.
 * zip - Extract as standard ZIP.

The event handler will fail if the file to be extracted from the archive
already exists.

The handler will fail if the archive has members which are to be extracted
outside of the `destination_path` or with characters not accepted by the
local filesystem.

For TAR/TAR.GZ/TAR.BZ2 archives, only regular files and directories
are supported.
Symbolic links, device and character files are not supported.

The handler can be associated with events containing a list of files.
It will try to handle each file associated with the event and will stop at
the first failure.


source_attribute
^^^^^^^^^^^^^^^^

:Default value: ``real_path``
:Optional: Yes
:Values: * Event data member name.
:From version: 3.43.0
:Description:
    This is the name of the event's structured data member used to get the
    path which will be handled by this event.

    This is a case-insensitive value.


destination_path
^^^^^^^^^^^^^^^^

:Default value: empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
:From version: 3.43.0
:Description:
    The path where the archive is extracted or files are
    decompressed.

    Leave it empty to extract the files in the same path as the
    source archive/compressed file.


overwrite_rule
^^^^^^^^^^^^^^

:Default value: `fail`
:Optional: Yes
:From version: 4.7.0
:Values:
    * `fail` - abort transfer if destination file already exists.
    * `overwrite` - always overwrite existing files with the content
      of the new source files.
    * `disable` - don't check for existing file and always try to transfer the
      file.
    * `skip` - don't transfer the source file when destination exists.

:Description:
    Rule used to decide how to handle the overwriting of an
    existing file at the destination.

    When set to `overwrite` it will emit an event when the destination
    file is overwritten.

    When set to `skip` it will not handle the file and the source file
    is not removed.
    An event is emitted to inform that the file was skipped.

    When set to `fail` and the archive contains at least one member file that
    already exist on destination, the extract process fail with a partial
    archive extraction.


delete_source_on_success
^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `Yes`
:Optional: yes
:Values: * `Yes`
         * `No`
:From version: 3.43.0
:Description:
    Whether to delete the source archive after a successful
    extraction.

    If extracting / uncompressing the archive fails, the source is
    not removed, even when this is set to `Yes`.


password
^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Event data member name.
:From version: 4.0.0
:Description:
    This is the password used to decrypt archives.

    Leave if empty if the archives are not encrypted.

    For ZIP files, only the `ZipCrypto / Zip Legacy` encryption is supported.


Encrypt / Decrypt using OpenPGP
-------------------------------

The `openpgp` event handler can be configured to encrypt or decrypt
files using the OpenPGP standard.

All files with the `.pgp` or `.gpg` extensions are decrypted,
all the other files are encrypted.

Encrypted files will have the `.pgp` extension appended to their filename.

The handler can be associated with events containing a list of files.
It will try to handle each file associated with the event and will stop at
the first failure.


encryption_public_keys
^^^^^^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * ASCII armored public PGP keys
:From version: 4.0.0
:Description:
    Lists of public PGP keys used for the encryption operation.

    It can contain one or multiple public PGP keys in printable ASCII format.

    Leave it empty if you don't want to use asymmetric encryption.


decryption_private_keys
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * ASCII armored private PGP keys
:From version: 4.0.0
:Description:
    Lists of private PGP keys used for the decryption operation.

    It can contain one or multiple private PGP keys in printable ASCII format.

    Leave it empty if you don't want to use asymmetric encryption.


passphrase
^^^^^^^^^^

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 4.0.0
:Description:
    Passphrase/password for encrypting/decrypting files using
    symmetric OpenPGP cryptography.

    Leave it empty if you don't want to use symmetric encryption.


encryption_extension
^^^^^^^^^^^^^^^^^^^^

:Default value: `.pgp`
:Optional: Yes
:Values: * Text to be appended after the file name.
:From version: 4.0.0
:Description:
    File extension used for the files encrypted by the handler.

    Encrypted files will have the configured text appended
    to the original name.

    This value is case-sensitive.


encryption_cipher
^^^^^^^^^^^^^^^^^

:Default value: AES128
:Optional: Yes
:Values: * AES128
         * AES192
         * AES256
         * CAST5
         * 3DES
:From version: 4.0.0
:Description:
    Cipher used for symmetric encryption.

    This value is not used when `passphrase` is not defined,
    as that is required for symmetric encryption.

    This value is case-insensitive.


source_attribute
^^^^^^^^^^^^^^^^

:Default value: ``real_path``
:Optional: Yes
:Values: * Event data member name.
:From version: 4.0.0
:Description:
    Name of the event's structured data member
    used to get the path to be handled.

    This is a case-insensitive value.


destination_path
^^^^^^^^^^^^^^^^

:Default value: empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
:From version: 4.0.0
:Description:
    The path where the resulting files are encrypted/decrypted.

    Leave it empty to perform file operations in the path of the source files.


overwrite_rule
^^^^^^^^^^^^^^

:Default value: `fail`
:Optional: Yes
:From version: 4.7.0
:Values:
    * `fail` - abort transfer if destination file already exists.
    * `overwrite` - always overwrite existing files with the content
      of the new source files.
    * `disable` - don't check for existing file and always try to transfer the
      file.
    * `skip` - don't transfer the source file when destination exists.

:Description:
    Rule used to decide how to handle the overwriting of an
    existing file at the destination.

    When set to `overwrite` it will emit an event when the destination
    file is overwritten.

    When set to `skip` it will not handle the file and the source file
    is not removed.
    An event is emitted to inform that the file was skipped.


delete_source_on_success
^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `Yes`
:Optional: yes
:Values: * `Yes`
         * `No`
:From version: 4.0.0
:Description:
    Whether to delete the source file after a successful operation.

    If encrypting/decrypting the source file fails, the source is
    not removed, even when this is set to `Yes`.


Execute external script or program
----------------------------------

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


executable_path
^^^^^^^^^^^^^^^

:Default value: ''
:Optional: No
:Values: * Local filesystem path.
:From version: 3.47.0
:Description:
    Local filesystem path to the executable.


executable_arguments
^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^

:Default value: 30
:Optional: Yes
:Values: * Number
:From version: 3.47.0
:Description:
    Number of seconds to allow for the external process to execute before
    forcefully closing it.

    A configured value must be equal to or greater than 1.


concurrent_processes
^^^^^^^^^^^^^^^^^^^^

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


RabbitMQ AMQP 0-9-1 Publisher
-----------------------------

The `rabbitmq` event handler is used to trigger an AMQP publish operation
based on an audit event.


url
^^^

:Default value: ''
:Optional: No
:Values: * `URL`
         * Comma separated list of URLs
:From version: 4.10.0
:Description:
    URL, without username and password for the RabbitMQ server.

    The username and password are configured as separate values for audit
    and security considerations.

    Use `amqp://host:port/virtual_host` for non-TLS connections.
    Use `amqps://host:port/virtual_host` for TLS connections.

    When `port` is not specified it will use port `5672` for non-TLS and
    port `5671` for TLS connections.

    When `virtual_host` is not specified, it will use the default virtual host.


username
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 4.10.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote RabbitMQ server.


password
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 4.10.0
:Values: * Plain text password.
:Description:
    Password associated with the configured `username`.


exchange
^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Text value
:From version: 4.10.0
:Description:
    The name of the exchange where messages are published.

    Leave it empty to use the default exchange.


routing_key
^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Text value
:From version: 4.10.0
:Description:
    The value of the routing key used when publishing the message.

    In the most simple case, this is the name of a RabbitMQ queue.


payload_template
^^^^^^^^^^^^^^^^

:Default value:
:Optional: No
:Values: * Static text value
         * Format string
:From version: 4.10.0
:Description:
    The payload of the published message itself.

    It can be a static text value used for all the events.

    You can also generate dynamic payloads based on event data.

    .. include:: /configuration/event-context-variables.rst.include


retry_count
^^^^^^^^^^^

:Default value: `2`
:Optional: Yes
:From version: 4.10.0
:Values:
    * 0
    * Positive integer
:Description:
    This is the number of times a failed connection or request or is retried.

    When set to `0`, requests are never retried.


retry_increase
^^^^^^^^^^^^^^

:Default value: `10`
:Optional: Yes
:From version: 4.10.0
:Values:
    * 0
    * Positive real number
:Description:
    Number of seconds to add to each wait period before retrying.

    This is also the value of the first retry wait period.

    When set to `0`, there will be no waiting time, a retry is performed
    right away.


.. include:: /configuration/ssl.include.rst


Extension API
-------------

The `extension` event handler can be configured to allow the creation of custom
event handlers implemented using the SFTPPlus API.

The extensions code will be placed inside the `extension` folder located in
the SFTPPlus base installation folder.

This event handler is targeted towards application developers.


entry_point
^^^^^^^^^^^

:Default value: empty
:Optional: No
:Values: * ``python:dotted.path.EntryClassHandler``
:From version: 3.28.0
:Description:
    The API entry point is defined in the format `LANGUAGE:DOTTED.ENTRY.POINT`,

    `LANGUAGE` is the name of the language in which the extension is
    written.

    `DOTTED.ENTRY.POINT` as an expression defining the package, module, and
    class name which will receive the event.

    ..  note::
        At this moment, the event handler API supports the development of
        custom handlers based on the Python programming language.

    As an example, for the file ``extension/demo_handler.py`` defining
    the ``DemoEventHandler`` class, the configuration will be::

        entry_point = python:demo_handler.DemoEventHandler

    See :doc:`Python API Event Handler</developer/python-api-event-handler>`
    developer documentation for more details about how to use
    the event handler.


configuration
^^^^^^^^^^^^^

:Default value: empty
:Optional: Yes
:Values: * Free text
:From version: 4.0.0
:Description:
    A text value which is passed to the event handler together with each
    event.

    You can set it as JSON for structured data or BASE64 for binary data
    and decode it in the event handler.
