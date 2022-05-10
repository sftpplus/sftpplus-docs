Extract Archive / Uncompress
============================

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
----------------

:Default value: ``real_path``
:Optional: Yes
:Values: * Event data member name.
:From version: 3.43.0
:Description:
    This is the name of the event's structured data member used to get the
    path which will be handled by this event.

    This is a case-insensitive value.


destination_path
----------------

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
------------------------

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
--------

:Default value: Empty
:Optional: Yes
:Values: * Event data member name.
:From version: 4.0.0
:Description:
    This is the password used to decrypt archives.

    Leave if empty if the archives are not encrypted.

    For ZIP files, only the `ZipCrypto / Zip Legacy` encryption is supported.
