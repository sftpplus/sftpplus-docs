File Dispatcher
===============

The `file-dispatcher` event handler can be configured to handle files to one
or multiple directory paths based on a matching expression.

This section describes the available configuration options.
For more details about the scenarios in which you can use this event handler,
check :doc:`the file dispatcher usage guide.</guides/file-dispatcher>`


dispatch_rules
--------------

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
-----------

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
----------

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
------------------

:Default value: 30
:Optional: Yes
:Values: * Number
:From version: 4.15.0
:Description:
    Number of seconds to allow for the external process to execute before
    forcefully closing it.

    A configured value must be equal to or greater than 1.


fallback_rule
-------------

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
--------------------

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
------------------

:Default value: `real_path`
:Optional: Yes
:Values: * Event data member name.
:From version: 3.20.0
:Description:
    This is the name of the event's data attribute used to get the path
    or the list of paths which will be dispatched by this event.

    This is a case-insensitive value.


dispatch_delay
--------------

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
----------------------------

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
--------------

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
-------------------------

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
