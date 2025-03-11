source_path
-----------

:Default value: Empty
:Optional: Yes
:Values: * Absolute path on the local file system.
         * Relative path to the server installation folder.
:From version: 2.10.0
:Description:
    Path to the monitored source folder.


recursive
---------

:Default value: `No`
:Optional: Yes
:From version: 2.10.0
:Values: * Yes
         * No
:Description:
    Determines whether the monitor should look for source files and folders
    only in the configured path, or recurse in all its descendant folders.


changes_poll_interval
---------------------

:Default value: `10`
:Optional: Yes
:From version: 3.0.0
:Values: * Number of seconds.
:Description:
    This is the time interval that defines the delay used to observe
    the changes in the monitored path and compare snapshots, a record of any
    changes, in a monitored folder.

    When set to zero or a negative number, the default value is used.


stable_interval
---------------

:Default value: `10`
:Optional: Yes
:From version: 2.10.0
:Values: * Number of seconds.
:Description:
    This is the interval after which a file is considered stable if no changes
    are made to it.

    These values should be greater than the value of `changes_poll_interval`.


source_filter
-------------

:Default value: Empty
:Optional: Yes
:From version: 2.10.0
:Values: * `Globbing expression containing wildcard characters`.
         * `Regular expression`
         * Empty
:Description:
    It can be configured using a
    `Globbing expression
    <http://en.wikipedia.org/wiki/Glob_%28programming%29>`_ or
    `regular expression <http://en.wikipedia.org/wiki/Regular_expression>`_.

    It defines the pattern used to select source files to be transferred.
    For more details about the syntax used by this configuration option see the
    :doc:`matching expression documentation.</configuration/matching-expression>`

    Only files matching the expression will be transferred.

    A globbing expression can contain multiple file mask filtering rules,
    separated by the pipe character `|`.

    If a globbing expression doesn't include path separators,
    it only matches the file name.
    The parent path is ignored.

    When using regular expressions, only file names are matched.

    Leave it empty to transfer all files.

    Since 4.16.0, the globbing expression can be used to filter based on
    the full file path, not only on the file name part.
