Transfers
=========

A transfer configuration defines the rules based on which files or folders
are transferred between two locations or inside a location.

..  contents:: :local:


Adding a new transfer via Local Manager
---------------------------------------

A new location can be added or changed via Local Manager below.

See below for an example of an initial configuration for a move transfer.

..  image:: /_static/gallery/gallery-add-transfer.png


Adding a new transfer via text configuration
--------------------------------------------

Adding a new transfer configuration is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``transfers/`` and followed by
the transfer's UUID.

The transfer's UUID can be any unique string used to identify the transfer.
Once defined, the UUID should not be changed.

For more information about UUIDs, please see
:doc:`the dedicated UUID documentation </configuration/introduction>`.

For example, to add a new transfer configuration of type `monitor`
called **Exported orders**::

    [transfers/00feb81f-a99d-42f1-a86c-1562c3281bd9]
    name = Exported orders
    description = Nightly orders exported by the accounting application.
    type = copy
    source_path = path/to/exported_orders
    recursive = y
    destination_path = path/to/exported_orders


enabled
-------

:Default value: 'Yes'
:Optional: No
:From version: 2.6.0
:Values: * Yes
         * No
:Description:
    Determines whether the transfer should be automatically started
    at server startup.


name
----

:Default value: ''
:Optional: No
:From version: 2.6.0
:Values: * Any text.
:Description:
    Human-readable short text used to identify this transfer.


description
-----------

:Default value: ''
:Optional: Yes
:From version: 2.6.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this transfer.


.. include:: /configuration/location-watch.include.rst


delete_source_on_success
------------------------

:Default value: `Yes`
:Optional: yes
:Values: * `Yes`
         * `No`
:From version: 4.0.0
:Description:
    Whether to delete the source file after a successful transfer.

    You can use the `archive_success_path` configuration option to have the file removed from the source directory and moved into another directory.

    If the transfer fails, the source is not removed,
    even when this is set to `Yes`.


delete_source_parent_delay
--------------------------

:Default value: `0`
:Optional: yes
:Values: * Number of seconds
:From version: 4.10.0
    This defines whether the parent directory of the source file is also
    removed on successful transfer.

    Set it to `0` to not delete the source directory.

    It is configured with a number of seconds after which, if no other file
    is transferred inside the targeted directory, the directory is removed.

    The parent directory is not removed right away to allow other external
    application to write all the required files for that directory.

    The base source directory is never removed.
    This configuration only removes the direct parent directory of the file that was transferred.
    The directory is not removed if it contains other files or directories.

    The configuration is valid for both local and remote source locations.

    ..  note::
        This configuration is ignored for non-recursive transfers.
        This configuration has no effect if the source file is not
        configured to also be removed via `delete_source_on_success`.


source_filter_age
-----------------

:Default value: Empty
:Optional: Yes
:From version: 3.51.0
:Values: * Number of seconds
:Description:
    This option can be used to instruct SFTPPlus to ignore older files.

    It is configured as a number of seconds.
    Files with a modified time older than the configured number of seconds
    are not transferred.

    Leave it empty or set it to `0` to transfer all files, regardless of
    the modified time.


transfer_memory_duration
------------------------

:Default value: `0`
:Optional: Yes
:Values: * Number of days
:From version: 4.0.0
:Description:
    The number of days to keep track of files transferred in the past.

    Already transferred files are not re-transferred as long as
    they have the same name, size, and modified timestamp.
    This is only true for transfers newer than the configured number of days.

    Use the default value of `0` to not keep track of transferred files
    and to transfer any file found in the source directory.


ignore_duplicate_paths
----------------------

:Default value: `No`
:Optional: Yes
:Values: * Yes
         * No
:From version: 4.0.0
:Description:
    When set to `Yes` this relaxes the rules based on which duplicated files
    are not re-transferred, by ignoring a file as long as it has the same
    path and name.
    The file is not re-transferred, even when it has a new size or modified
    date.

    For duplicated files to be recognized,
    the `transfer_memory_duration` needs to be enabled.
    This configuration is ignored when `transfer_memory_duration = 0`.


destination_uuid
----------------

:Default value: `Local file system`
:Optional: Yes
:Values: * UUID of a defined location.
         * Empty - local file system location.
:From version: 2.10.0
:To version: None
:Description:
    UUID of the location used as the destination for this transfer or empty to use the local file system location.


destination_path
----------------

:Default value: Empty
:Optional: Yes
:Values: * Absolute path on the local file system.
         * Relative path to the server installation folder.
:From version: 2.10.0
:To version: None
:Description:
    Path to the destination folder of this transfer.


destination_temporary_suffix
----------------------------

:Default value: Empty
:Optional: Yes
:From version: 3.45.0
:Values: * Empty.
         * Short text.
:Description:
    This option allows uploading a file using a temporary name,
    renaming to its initial name once all the file's content was transferred.

    Leave it empty to always transfer a file to its destination using
    the original name.

    ..  note::
        This configuration option is ignored when `destination_path_actions`
        is set using the `temporary-suffix` or `fixed-path` actions.


batch_interval
--------------

:Default value: `0`
:Optional: Yes
:Values: * `0` to disable batch transfer.
         * Number of seconds to wait for new files to be part of a batch.
:From version: 3.0.0
:To version: None
:Description:
    You can configure the transfer to send each file as an independent transfer,
    or group multiple files into a single transfer.
    This is called a time-based batch transfer.

    ..  note::
        This option is ignored when `batch_marker_path` is defined.
        A transfer can only run as time-based batching or file marker batching.

    If the transfer of one or more files from the batch fails in batch mode,
    the whole transfer is considered to have failed.
    The transfer is considered to have been successful only when all files
    from a batch have been successfully transferred.

    A batch transfer is started if no new changes are recorded in the
    configured time interval.
    Each new change will reset the time interval.

    If a transfer is stopped or fails while a batch transfer is waiting for the
    batch interval, the whole batch will be canceled, and no files will be
    transferred.

    If a transfer is suspended while a batch transfer is waiting for the
    batch interval, the files accumulated until then will be transferred.

    To disable batch mode and transfer each file as an individual transfer,
    set this to `0`.

    When batch mode is disabled, `execute_before`, `execute_after_success`
    and `execute_after_failure` commands are executed for each individual
    file.

    When the batch mode is enabled, `execute_before` is called before
    transferring the first file from the batch, while the
    `execute_after_success` and `execute_after_failure` commands are called
    after the last file from the batch was transferred.


batch_marker_path
-----------------

:Default value: ''
:Optional: Yes
:Values: * Name of a file.
         * Globbing expression.
         * Regular expression.
         * Multiple names of files or expressions. One per line. (Since 4.22.0)
:From version: 3.36.0
:Description:
    You can configure the transfer to wait for a file with a specific
    file path or file path pattern before transferring the files.

    This is called a file marker-based batch transfer.

    The marker file needs to be located inside the source path.

    The matching expression should be defined in such a way as to match the whole path of the targeted file,
    and not just the file name.

    Multiple expressions can be defined to configure the transfer to wait for multiple files.
    Each expression should match a single file.

    When one expression is matching multiple files, the transfer will fail.
    This indicates a likely misconfiguration, which could cause non-deterministic transfers.

    For transfer with a recursive source, you can configure the marker at any place inside the source sub-directories.
    The batch transfer will include any files located in the same directory as the batch marker as well as any files in the sub-directories.

    The transfer will start 15 seconds after the marker file was detected.

    Leave it empty to not delay the transfer based on a marker/flag file path.

    For more details about defining a transfer with a file marker,
    see the :doc:`transfer operation guide </operation-client/transfers>`.


execute_timeout
---------------

:Default value: 30
:Optional: Yes
:From version: 4.11.0
:Values: * Number of seconds
:Description:
    This defines the time interval in seconds allowed for the execution
    of external commands.
    If the external command is still running after the configured duration,
    it's automatically terminated with an error.

    When defined with a value lower or equal to zero the default timeout
    value is used.


execute_before
--------------

:Default value: Empty
:Optional: Yes
:From version: 2.7.0
:Values:
    * Path to local script or executable to call before a file is
      transferred.
    * Empty
:Description:
    The executable is called with the full path to the file that is about to
    be transferred.

    This should be configured only with the path and without any other command line arguments.
    You can use a wrapping script/batch file to have the executable called with a set of default arguments or to call multiple executables.

    The following environment variables are also set:

    * `SOURCE_PATH` - is set to the source path of the processed file.

    * ``DESTINATION_PATH`` - is set to the path on the destination for the file.
      (Since: 3.20.0)

    For batch transfers, only the first file from the batch is sent as an
    argument.

    The transfer continues only if the command's exit code is `0`.
    This means that when the exit code is not `0`, the file is not transferred
    (copied, moved, etc.), and no other actions are done for this transfer.

    When the source location is remote and the destination is a local location
    the command will be called with a path that does not exist yet, as this is
    executed before the actual transfer takes place.

    ..  note::
        On Windows, executables located in Unicode paths and monitored Unicode
        paths are not yet supported.

    ..  note::
        Remote-to-remote transfers are not supported.

    Leave it empty to not execute any command before a transfer.


execute_after_success
---------------------

:Default value: Empty
:Optional: Yes
:From version: 2.9.0
:Values:
    * Path to local script or executable to call after a file is
      successfully transferred.
    * Empty
:Description:
    Please see the description of the `execute_before` configuration option.

    For batch transfers, the command is called with the path of the last
    file from the batch.

    The command is not called when `execute_before` fails.


execute_after_failure
---------------------

:Default value: Empty
:Optional: Yes
:From version: 2.9.0
:Values:
    * Path to local script or executable to call after a file fails to be
      transferred.
    * Empty
:Description:
    Please see the description of the `execute_before` configuration option.

    For batch transfers, the command is called with the path of the last
    file from the batch.

    This is called once, after all retries have been executed.
    The command is not called if `execute_before` fails.


execute_on_destination_before
-----------------------------

:Default value: Empty
:Optional: Yes
:From version: 3.0.0
:Values:
    * List of commands to be executed in the destination location.
    * Empty
:Description:
    Before starting the transfer of a file or a batch,
    execute in the destination location the list of configured commands.

    Each command should be defined on a separate line or delimited with a
    semicolon (;).

    You can use the following variables inside the commands:

    * `{source.path}` - the full path on the source location
    * `{source.name}` - the full file name on the source location
    * `{destination.path}` - the full path on the destination location
    * `{destination.name}` - the full file name on the destination location

    The commands are executed using an embedded client-shell.
    The shell is already connected to the destination location.
    There is no need for an explicit *open* command.
    For the list of supported commands, please check the
    :doc:`client-shell documentation</operation-client/client-shell>`.

    Transfer continues only if commands are successful.
    When one of the commands fails, the file is not transferred (copied /
    moved / etc.), and no other actions are completed for this transfer.

    ..  note:
        In the case that you need to execute more commands in the remote location,
        or you cannot implement your workflow using the available commands, contact us.


execute_on_destination_after_success
------------------------------------

:Default value: Empty
:Optional: Yes
:From version: 3.0.0
:Values:
    * List of commands to be executed in the destination location.
    * Empty
:Description:
    See description of the `execute_on_destination_before` configuration
    option.

    The commands are executed if the file or the batch has been successfully transferred.


execute_on_destination_after_failure
------------------------------------

:Default value: Empty
:Optional: Yes
:From version: 3.0.0
:Values:
    * List of commands to call after a file fails to be transferred.
    * Empty
:Description:
    See description of the `execute_on_destination_before` configuration
    option.

    The commands are executed if the file or the batch transfer has failed.


archive_success_path
--------------------

:Default value: Empty
:Optional: Yes
:From version: 3.0.0
:Values:
    * Path on the local filesystem.
    * Empty
:Description:
    Path to a folder in the local file system used to keep a copy of
    successfully transferred files.

    To disable archiving, leave this option empty.

    To prevent overwriting previous files, new files are copied to the archive
    folder with timestamps inserted in their names.

    Timestamps are inserted before file extensions.
    When a file has no extension, the timestamp is appended to the file name as
    an extension.

    Timestamps have the following format::

        .YEAR-MONTH-DAY-HOUR-MINUTES-SECONDS-MILLISECONDS-RANDOM

    A file named ``README.rst`` will be archived as
    ``README.2014-12-03-13-00-57-967636-036.rst``, while a file named
    ``README`` is ``README.2014-12-03-13-00-57-967636-036``.

    ..  note::
        Archiving is disabled when a transfer source or destination location
        is not a local folder.


archive_failure_path
--------------------

:Default value: Empty
:Optional: Yes
:From version: 3.0.0
:Values:
    * Path in the local file system.
    * Empty
:Description:
    Path to the local folder in the local file system used to keep a copy of unsuccessful started file transfers.

    To disable archiving, leave this option empty.

    When `execute_before` or `execute_on_destination_before` commands fail,
    the file transfer is not considered started, and the archiving stage is
    not executed.

    To prevent overwriting previous files, new files are copied to the archive
    folder with timestamps inserted in their names.
    See `archive_success_path` for more details about the timestamp format.

    When the remote file is partially transferred, the partial file is
    archived.

    ..  note::
        When the source is in a remote location and the file has not yet been copied to the local file system, an empty file is copied to the archive.

    ..  note::
        Archiving is disabled when a transfer has both source and destination
        as remote locations.


archive_format
--------------

:Default value: `timestamp-always`
:Optional: Yes
:From version: 4.0.0
:Values:
    * `timestamp-always`
    * `exact`
:Description:
    This configuration defines the way archive files are created.

    `timestamp-always` will archive all files using a timestamp.
    It will mirror the directory structure from the source folder.

    `exact` will store the files using the same name and will mirror the directory structure from the source folder.
    If a file with the same name already exists, the new file is archived with a timestamp.


archive_retention_period
------------------------

:Default value: `0`
:Optional: Yes
:From version: 3.51.0
:Values:
    * Number of days.
    * `0`
:Description:
    Number of days after which older archived files for a transfer are
    automatically removed.

    SFTPPlus will check for old achieved files when the transfer
    starts and twice per day.

    Leave it to `0` to keep all the files.


retry_count
-----------

:Default value: `2`
:Optional: Yes
:From version: 3.0.0
:Values:
    * 0
    * Positive integer
:Description:
    This is the number of times a failed file transfer is retried.

    When set to `0`, failed file transfers are never retried.

    For batch mode transfers, each failed transfer of a file inside the batch
    is retried.


retry_wait
----------

:Default value: `60`
:Optional: Yes
:From version: 3.0.0
:Values:
    * 0
    * Positive integer
:Description:
    Number of seconds to wait before retrying a failed transfer.

    When set to `0`, there will be no waiting time.
    As soon as a file transfer fails, it will be retried.


schedule
--------

:Default value: Empty
:Optional: Yes
:From version: 3.0.0
:Values:
    * Empty to have the transfer always active.
    * Comma-separated list of ``24HOUR:MINUTE-ACTION_NAME`` actions.
    * Comma-separated list of ``WEEKDAY-24HOUR:MINUTE-ACTION_NAME`` actions.
    * Multiple lines of comma-separated values of actions.
:Description:
    Comma-separated list with scheduled actions for this transfer.

    Times are defined using a 24-hour based on the local time zone.

    Supported actions are:

    * `start`
    * `stop`

    Week day values were introduced in version 3.44.0.
    Here are the valid week day values, in ISO 8601 order:

    * Monday
    * Tuesday
    * Wednesday
    * Thursday
    * Friday
    * Saturday
    * Sunday

    For longer schedule definition you can define the actions across multiple
    lines.

    Time resolution is one minute.
    Please contact us if you need a higher resolution.

    For more details about defining a transfer with a scheduler,
    see the :doc:`transfer operation guide
    </operation-client/transfers>`.


overwrite_rule
--------------

:Default value: `fail`
:Optional: Yes
:From version: 3.0.0
:Values:
    * `fail` - abort transfer if the destination file already exists.
    * `overwrite` - always overwrite existing files with the content
      of the new source files.
    * `disable` - don't check for existing files and always try to transfer the file.
    * `skip` - don't transfer the source file when the destination exists.
    * `timestamp-always` - always transfer the source file with an amended
      timestamp and prevent accidental overwriting on the destination.
    * `timestamp-to-new-file` - transfer the source file with a timestamp
      only if a file with the same original name exists at the destination.
    * `timestamp-to-existing-file` - transfer the source file with the original
      name and, when a file with the same original name exists at the
      destination, rename the existing file at the destination.

:Description:
    The rule used to decide how a transfer handles the overwriting of an existing file at the destination.

    When the file is transferred with `temporary-suffix`, it will check for the existence of the final file name on the destination,
    not the file name with the temporary suffix.

    When set to `overwrite` it will emit an event when the destination file is overwritten.

    When set to `skip` it will not transfer the source file and the source file is not removed from the source directory.
    An event is emitted to inform that the file was skipped.

    ..  note::
        The transfer does nothing to prevent external applications
        from tampering with the existing file during a transfer.
        It assumes that no other application is managing the local or
        remote files during a transfer.


destination_path_actions
------------------------

:Default value: Empty
:Optional: Yes
:From version: 3.36.0
:Values: * ``path-match-expression, transformation, parameter-1, parameter-2``
         * ``path-match-expression, transformation``
         * List of rules, separated by newlines.
:Description:
    Rules defining the action taken to the destination path and file name,
    as transferred to the destination location.

    This is a comma-separated configuration value.

    The first value is the full source path-matching expression for the source file with a path relative to the configured `source_path`.
    `Globbing expression
    <http://en.wikipedia.org/wiki/Glob_%28programming%29>`_ or
    `regular expression <http://en.wikipedia.org/wiki/Regular_expression>`_
    can be used.
    For more details, see the :doc:`matching expression
    documentation.</configuration/matching-expression>`

    The second value is the name of the action performed on the
    source file name and source path in order to define the destination
    file name and destination path.

    You can specify multiple rules, one per line.
    Leading and trailing spaces are ignored.
    Empty lines are ignored.

    When a path is matching multiple rules, it will have the effect of
    multiple actions applied for the same path.
    The actions are applied one by one,
    from top to bottom as defined in the configuration.
    The result from the first action is used as the input for the
    second action.

    Leave it empty to not define any actions and have the same
    file path and file name as from the source.

    When action rules are defined, and the current transferred file
    does not match any rule, the transfer will fail.
    You can use a file `*, no-action` rule to explicitly instruct
    SFTPPlus that you don't want an action for the file names not
    matching any of the previous rules.

    The supported actions are:

    * `transform` - This is the generic operation based on which the destination path can be defined as a different name in comparison with the source path.
      The whole path can be transformed, not only the filename.
      It can be used for a rename operation,
      as well as for inserting a timestamp.
    * `only-filename` - Use only the source file name and discard the source
      path. This results in a flattened destination.
      This action has no parameters.
    * `replace-separator` - Takes a single parameter, which is the character(s)
      used to replace the source path separator.
    * `lowercase` - Will use the same file path as source, but in all lower
      case. This action has no parameters.
    * `temporary-suffix` - Will use a temporary file name suffix to transfer
      the file, renaming it back after all the content was transferred.
    * `temporary-prefix` - Will use a temporary file name prefix to transfer
      the file, renaming it back after all the content was transferred.
    * `fixed-path` - Will use the same path for all the transferred files.
    * `no-action` - Will keep the file path and file name as in the
      source. This action has no parameters.

    For more details and examples on the available actions,
    see :doc:`the client-side file transfer usage guide.
    </operation-client/transfers>`


destination_fallback_path
-------------------------

:Default value: Empty
:Optional: Yes
:From version: 4.24.0
:Values: * Empty.
         * Path on destination.
:Description:
    This option allows defining a destination path that is used when failing to copy the file to the normal destination path.

    This option is designed to be used with non-recursive transfers.
    When used with recursive transfers the functionality of this option is limited.
    SFTPPlus will not try to create a missing destination sub-directory.
    It will also not try to create the missing sub-directories inside the fallback path.
    Instead, files for missing sub-directories are attempted to be delivered to the fallback path,
    without creating the source directory structure in the fallback directory.
    Get in touch with our support team,
    if you want SFTPPlus to create the source directory structure inside the fallback directory.

    This is designed to be used together with `destination_path_actions`,
    when the destination path is dynamic.

    See also the `operation guide here <../operation-client/transfers.html#fallback-destination-path>`_.
