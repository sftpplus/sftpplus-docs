Local file
==========

To configure an event handler which sends events to a local file system,
use the type `local-file`.

..  contents:: :local:


Introduction
------------

Event entries are appended to the file, and the file can be configured to be
rotated by external tools or automatically rotated by the server, based on
size or time rules.
The log format can be specified using the `entry_content` configuration
option.

..  warning::
   Please enable rotation, otherwise the log file can grow to an extremely
   large file.

.. include:: /configuration-events/events-commons.include.rst


path
----

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
---------------

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
--------------

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
---------

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
------------

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
-------------

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
-----------------

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
