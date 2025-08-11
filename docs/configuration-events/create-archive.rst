Create archive / compress
=========================

The `create-archive` event handler can be configured to create an archive
based on one or more files associated with the event.

When creating archives of format GZIP (.gz extension) if the associated
event has multiple files, it will compress each file as separate archives.

When creating archives of format ZIP (.zip extension) if the associated
event has multiple files, it will compress all files as a single archive.

The create archive event handler only handles direct file paths.
Recursive directory paths are not yet supported.

..  contents:: :local:

.. include:: /configuration-events/events-commons.include.rst


archive_format
--------------

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
------------

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
----------------

:Default value: ``real_path``
:Optional: Yes
:Values: * Event data member name.
:From version: 4.7.0
:Description:
    This is the name of the event's structured data member used to get the
    path which will be handled by this event.

    This is a case-insensitive value.


destination_path
----------------

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
--------------

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
------------------------

:Default value: `Yes`
:Optional: yes
:Values: * `Yes`
         * `No`
:From version: 4.7.0
:Description:
    Whether to delete the source files after a successful archive creation.

    If creating the archive fails,
    the source is not removed, even when this is set to `Yes`.
