..  _contact us: mailto:support@proatria.com


Transfers operations
====================

..  contents:: :local:


Introduction
------------

This page describes how to implement client-side transfers using SFTPPlus

Check the separate :doc:`reference documentation for transfers</transfer/transfers>`,
which describes all the configuration options available when defining a transfer.

There is a separate documentation page :doc:`dedicated to transfers scheduling</transfer/transfer-scheduling>`,
which goes into more detail about how to scheduled transfers.

Transfers are the pro-active component of SFTPPlus.
While a file transfer service only acts in response to requests from remote
clients, transfers actively check local or remote paths and initiate transfers
based on changes in those folders.

Transfers are executed by transferring files between a source location and
a destination location.


Source Location
---------------

Source location changes are detected by regularly checking the source folder
for changes.

When a change is observed in the monitored source location, the monitor emits one of the following event types:

* File modified
* File/folder created
* File/folder deleted
* File/folder moved

Here is a list of file system changes that are **ignored**:

* **Folder modified** (since they are emitted whenever a member is
  created / removed / moved inside that folder)
* Permissions / Security / Attribute changes

For transfers of type `Local filesystem only`, created, moved, or removed
folders will only emit an informational log event, without triggering the
prior transfer command.
The same behaviour is present when a file is removed.

For transfers of type `other than` `Local filesystem only`, folder events
and file removed events are ignored, and no informational event is emitted.

Source events are observed **only inside the configured path**, and the server
will ignore events outside the configured path.
While in most cases this is the desired result, it affects 'moved' events.
`Moved events` are only observed inside the location path.
When you move a file **from a path outside** the monitored path,
a `create` event is emitted.
When you move a file **to a path outside** the monitored path,
a `delete` event is emitted.

A transfer can monitor only direct ancestors of a folder, for **non-recursive**
monitors, or all ancestors for **recursive** ones.

When the source location is not available (for example, its connection failed
after all retries) the transfer will become `stalled` and no files will be transferred.


Source File Transfer
--------------------

Once changes are observed in the source, SFTPPlus will start doing the actual
transfer of the file's content.

Multiple files might be created at the source at the same time.
All of them are observed as soon as they are stable.

To limit the load to the remote destination, SFTPPlus will only transfer one file at a time.
Multiple files are not transferred in parallel at the same time.

All the files detected in the source folder of a transfer are placed into a
queue.
As soon as the current file is transferred, a new file is picked from the
queue.

To thwart erroneous behaviour, SFTPPlus will only keep files in the queue up to 100 000 files.
If more files are created and not transferred, the transfer will fail and stop.


Recursive Source Transfer
-------------------------

A recursive transfer is one in which you configure the base path
for a transfer and SFTPPlus will traverse the whole path and sub-path and
transfer files from there.

You can configure a transfer to check the source path for any file which
is found in the source path itself or in any of the sub-paths.

The source path can be on a local filesystem or remote location such as a
SFTP or FTPS server.

See below for an example:

..  image:: /static/guides/recursivefiletransfer.png
    :alt: Example of a recursive file transfer via the changes poll interval
    :align: center

The files will be transferred to the destination using a folder structure
relative to the source path.
On destination, the parent folder of each file is automatically created.
The full source path hierarchy is not preserved.

For a recursive source transfer, there is a performance issue to consider.
For each sub-folder, SFTPPlus will need to make a separate request
(local or remote) to get the content and attributes of each member of that folder.
When you have 1000 sub-folders, SFTPPlus will make at least 1000 requests.

In contrast, if you set up a non-recursive file transfer scenario,
the files will be transferred only from a single folder and will make a
single request.

See below for a simplified example:

..  image:: /static/guides/nonrecursivefiletransfer.png
    :alt: A non-recursive file transfer using specific transfer rules
    :align: center

In the above scenario,
only two sub-folders have transfer rules associated with them.
This means that SFTPPlus will only monitor filesystem changes within those
two sub-folders, and not with the main home folder.
Transfers are triggered based on the rules relevant to the two folders.
Other benefits to this method beyond performance include;
greater control for the administrator for their managed file transfer setup,
more detailed logging of events associated with the transfer and monitored
folders,
and better troubleshooting capacity if the issues are traced back to the
transfer rules themselves.

In addition, specific transfer rules can be configured based on custom
conditions to trigger the transfer.
The conditions could depend on factors such as the schedule, the file type
(if not all files), the directory itself, directory actions that trigger
the transfer rule and more.


Transferring files generated by slow producers
----------------------------------------------

To ensure that your files are always correctly processed by SFTPPlus or other
managed file transfer products, ensure that files:

* Do not have the final content.
* Do not have the final name.
* Are not placed in the final location.

When using the product to transfer files that are generated dynamically by
other software, it can be very difficult to configure a stable delay that
works in all cases.

One option is to set up very long stable intervals, but this comes with the
drawback of delaying the processing of all the files.

We have encountered situations where the generated files were written to with
interruptions -- significant delays between writes.
Since both the file size and last modified timestamp remain unchanged,
SFTPPlus considers the file stable after the stable interval passes, thus
attempting to transfer it.

Because it is still kept open by the process generating it, you end up
either transferring an incomplete file or failing to transfer it if the
other process has opened it exclusively.

As a workaround and suggested approach for these cases, we recommend using
either a different (temporary) folder for generating the files or using
an extension filter for ignoring them. Both are detailed below.

The move/rename operation is atomic on Unix-like systems.

Based on our experience, this operation is quick on all modern operating
systems even if for large file sizes.

When the final location or the files with final filenames have the final
content, you can set up a short stable delay interval,
which makes SFTPPlus act upon the final files as fast as possible.


Using a different folder
^^^^^^^^^^^^^^^^^^^^^^^^

The solution is to store the file into a temporary folder, different
from the transfer source folder, until it is completed.

Once the file is complete, it can be moved to the transfer source folder.


Using a filename filter
^^^^^^^^^^^^^^^^^^^^^^^

Another approach is to configure a filename filter for the transfer.
This way, only files matching the filter are considered valid for transferring.

The software that generates the file can use either a different extension or
a suffix while the file is being generated and renamed on completion.

If you have a significant number of files in the transfer source folder, we
recommend the previous solution, as all the files will have to be checked
against the filter, which might impact performance
when there are thousands of them.


Delete Source Directories
-------------------------

For recursive transfers, you can configure SFTPPlus to automatically delete the parent source directory,
when that directory becomes empty.

Below is an example in which, after successfully transferring a file from path
``E:\\Reports\\2020-12-28\\sales.pdf``, the file is removed right away
while the parent is removed after 1 hour, if there are no other files
in the same source path::

      [transfers/15d46e5a-25f6-11e9-87b3-0b5ae5eda581]
      source_path = E:\Reports\
      delete_source_on_success = True

      delete_souorce_parent_delay = 3600

Any other file transferred from the same parent source path will reset the
delay after which the delete operation is executed.


Destination Location
--------------------

The destination's locations are accessed only when a file which needs to be
transferred is detected on the source location.

When the destination location is not available, the changes detected on the source location are still observed but no transfer is attempted.
As soon as the destination location is available again, new changes observed
on the destination will be processed.

The transfer will automatically start or resume the destination location
when needed.
It will not try to start the destination location when the location has
failed.


Stop / Cancel a transferred file
--------------------------------

When a transfer is stopped, any pending file is cancelled.

The current data transfer is stopped and no other actions are executed for
that transfer.


Transferring files with a temporary name
----------------------------------------

A transfer can be configured to send / upload / push the file's content
using a temporary name, renaming to its initial name once all the
data was received by the server.

This is done using the `destination_temporary_suffix` configuration option.

In the example below, the content of the file `E:\Reports\INV-2019-08-23.pdf`
is sent to the remote server as a file `/inbox/INV-2019-08-23.pdf.tmp`.
Once the file was received on the server, it is renamed from
`/inbox/INV-2019-08-23.pdf.tmp` to `/inbox/INV-2019-08-23.pdf`::

      [transfers/15d46e5a-25f6-11e9-87b3-0b5ae5eda581]
      source_path = E:\Reports\
      destination_path = /inbox

      destination_temporary_suffix = .tmp

When `destination_temporary_suffix` is configured, any file transfer
to the destination will be done using a temporary name.

In the case in which you only want a selected set of files transferred
using temporary names or want to transfer files using a temporary prefix,
you can leave `destination_temporary_suffix` empty
and set `destination_path_actions` with the `temporary-suffix` or
`temporary-prefix` actions.
See the dedicated documentation for the
:ref:`temporary-suffix <configuration-temporary-suffix>` action.


Transferring to legacy / restricted remote servers
--------------------------------------------------

In order to transfer a file, SFTPPlus performs a set of extra operations
in addition to the actual request to upload the file's content.
For example, it can check if a file already exists at the destination
in order to prevent on overwrite.

When dealing with legacy servers, some of these extra operations might not
be supported.
You can also have to deal with a remote server which restricts operations
other than the actual file transfer itself.

SFTPPlus allows sending a file using only the basic file upload operations
provided by the transfer protocol.

Below is a list of configuration options which trigger extra requests:

* Set the remote location with `idle_connection_keepalive_interval = 0`.
  In this way, SFTPPlus does not trigger idle folder listing in order to
  force keeping the connection opened.

* Disable destination overwriting rule with `overwrite_rule = disable`.
  In this way, SFTPPlus does not perform an extra request to check if a remote
  file already exists.


Configuring the Destination File Name and Path
----------------------------------------------

The `destination_path_actions` option can be defined for a transfer
and will allow using a destination path and file name different than the
source path and file name.
In this way, you can define transfers to dynamic destination paths.

This is configured using a set of rules which are applied based on
expression matching the source path.

To highlight misconfiguration or omission in configuration,
when a transfer has a `destination_path_actions` configured and
it tries to transfer files not matching any of the configured rules,
SFTPPlus will stop the whole transfer with a failure and will not process
any further files.

The base destination path, as defined in `destination_path`
is not affected by the file path and file name transformation.

A transfer can have multiple rules defined for the same path and the
actions will be applied in series.
The result from one action will be passed to the next one.
Having the following configuration::

    [transfers/313a9679-bc15-42e9-80ef-e2305959a3d1]
    enabled: yes
    name: copy-to-remote

    recursive: yes
    source_path: c:\out\sales
    source_filter: *
    delete_source_on_success: Yes

    destination_uuid: 5f304286-8d56-41f9-ba57-420a2303e90c
    destination_path: /Outbox/

    destination_path_actions:
      *.pdf, only-filename
      *.pdf, lowercase

the files will be transferred as follows::

    c:\out\sales\Report.PDF          -> /Outbox/report.pdf
    c:\out\sales\18\Jan\Outcome.PDF  -> /Outbox/outcome.pdf

In the following sections, you will find detailed information for each of the available actions.


no-action
^^^^^^^^^

The `no-action` rule does not change the transferred path or name.

It is used to explicitly inform SFTPPus that you don't want a transformation
for certain file types and to transfer the file with the same path and name
as is found on the source.


transform
^^^^^^^^^

The `transform` action is the generic operation that can be used to
define a destination path and name, different from the source path.

The whole path can be transformed, not only the filename.

Any transformed path will be transferred to a path relative to the path configured via `destination_path`.
Use the `{ignore_destination_path}` placeholder at the start of transformation rule to ignore the configured destination path.

------------

It can be used for generic rename operations for which the result is
defined based on regular expression groups.
Each regex matching group is available via the `{group.N}` variable,
where `{group.0}` is the whole source and `{group.1}` is the first
matched group.

Having the following configuration::

    recursive: no
    source_path: c:\out\sales
    destination_path: /Outbox/
    destination_path_actions:
      m/(std-|prv-)(.*)/, transform, final_{group.2}

the files will be transferred as follows::

    c:\out\sales\std-Report.PDF      -> /Outbox/final_Report.PDF
    c:\out\sales\prv-Outcome.txt     -> /Outbox/final_Outcome.txt

------------

The following placeholders are available based on the source file,
relative to the base source path:

* `{path.source}` - the path including file name, relative to the base source
  path for this transfer.
* `{path.directory_path}` - the path of the source file's directory,
  relative to the configured base source path.
* `{path.file_name}` - the file name, including the extension.
* `{path.file_base}` - the file name without the extension.
* `{path.file_extension}` - the file extension.
* `{ignore_destination_path}` - to instruct that the configured `destination_path` should be ignored.

Having the following configuration::

    source_path: c:\out\sales
    destination_path: /Outbox/
    destination_path_actions:
      *.pdf, transform, {path.directory_path}/Preview-{path.file_name}
      *.txt, transform, {path.directory_path}/{path.file_base}-Estimation{path.file_extension}

the files will be transferred as follows::

    c:\out\sales\Report.PDF          -> /Outbox/Preview-Report.PDF
    c:\out\sales\Report.txt          -> /Outbox/Report-Estimation.txt
    c:\out\sales\EMEA\Income.PDF  -> /Outbox/EMEA/Preview-Income.PDF
    c:\out\sales\EMEA\Income.txt  -> /Outbox/EMEA/Income-Estimation.txt

----------

It can be used for inserting a timestamp in an arbitrary position,
based on the current date and time.
The following placeholders are available:

  * `{now.cwa_14051}` - Human readable date and time
  * `{now.iso_8601}` - ISO 8601 date and time
  * `{now.iso_8601_fractional}`
  * `{now.iso_8601_local}`
  * `{now.iso_8601_basic}`
  * `{now.iso_8601_compact}` - ISO 8601 compatible with Windows file names
  * `{now.timestamp}` - Unix timestamp

Having the following configuration::

    source_path: c:\out\sales
    destination_path: /Outbox/
    destination_path_actions:
      *.pdf, transform, {now.iso_8601_compact}-{group.0}
      *.txt, transform, {path.directory_path}/{path.file_base}-{now.iso_8601_compact}{path.file_extension}

the files will be transferred as follows::

    c:\out\sales\Report.PDF          -> /Outbox/20210121T244503-Report.PDF
    c:\out\sales\Report.txt          -> /Outbox/Report-20210121T244503.txt
    c:\out\sales\EMEA\Income.PDF  -> /Outbox/EMEA/20210121T244503-Income.PDF
    c:\out\sales\EMEA\Income.txt  -> /Outbox/EMEA/Income-20210121T244503.txt

-----------

The `transform` action can be used for transferring files into different
destination paths,
in which the destination path is selected based on the source path.
To implement that, the transformed destination path should be absolute paths.

Having the following configuration::

    source_path: c:\out\sales
    destination_path: /Out/
    destination_path_actions:
      *.pdf, transform, /Staging/{path.source}
      *.txt, transform, final-{path.file_name}

the files will be transferred as follows::

    c:\out\sales\Report.PDF          -> /Staging/Report.PDF
    c:\out\sales\Report.txt          -> /Out/final-Report.txt
    c:\out\sales\EMEA\Income.PDF  -> /Staging/EMEA/Income.PDF
    c:\out\sales\EMEA\Income.txt  -> /Out/EMEA/Income.txt

-----------

The `transform` action can be used for transferring files to path relative to the working directory, as defined by the remote server.
The `{ignore_destination_path}` placeholder at the start of a transformation expression, is used to trigger this functionality.
Having the `{ignore_destination_path}` inside the transformation expression will not trigger the relative path transfers.

Having the following configuration::

    source_path: c:\out\sales
    destination_path: /Out/
    destination_path_actions:
      *.txt, transform, final-{path.file_name}
      *.confirm, transform, {ignore_destination_path}{path.file_base}.done

the files will be transferred as follows::

    c:\out\sales\Report.txt          -> /Out/final-Report.txt
    c:\out\sales\EMEA\Income.txt  -> /Out/Income.txt
    c:\out\sales\EMEA\Income.confirm  -> Income.done


only-filename
^^^^^^^^^^^^^

The `only-filename` transformation is used to flatten a path defined
across multiple directories by using only the file name.

The parent path as found in the source is ignored.

This can be used to transfer a recursive transfer on the source to a non-recursive transfer on the destination.

Having the following configuration::

    [transfers/313a9679-bc15-42e9-80ef-e2305959a3d1]
    enabled: yes
    name: copy-to-remote

    recursive: yes
    source_path: c:\out\sales
    source_filter: *
    delete_source_on_success: Yes

    destination_uuid: 5f304286-8d56-41f9-ba57-420a2303e90c
    destination_path: /Outbox/

    destination_path_actions:
      *.pdf, only-filename
      *.txt, no-action

the files will be transferred as follows::

    c:\out\sales\Report.PDF          -> /Outbox/Report.PDF
    c:\out\sales\Report.txt          -> /Outbox/Report.txt
    c:\out\sales\18\Jan\Outcome.PDF  -> /Outbox/Outcome.PDF
    c:\out\sales\18\Jan\Outcome.txt  -> /Outbox/18/Jan/Outcome.txt


.. _configuration-temporary-suffix:

temporary-suffix
^^^^^^^^^^^^^^^^

The `temporary-suffix` action allows uploading a file using a temporary name,
then renaming to the initial name once all the file content was transferred.

..  note::
    The `temporary-suffix` action is required only when a selected subset of
    files need to be transferred with temporary names.

    It can also be used in combination with other actions.

    When you want all files transferred with temporary names
    and no other actions are required for the files,
    it is recommended to use the dedicated `destination_temporary_suffix` configuration option.

It takes a single option consisting of the characters used as the temporary
suffix.

With the following configuration, the file ``c:\out\sales\report.pdf`` will
be first transferred to ``/Outbox/report.pdf.tmp``, then finally renamed to
``/Outbox/report.pdf``::

    [transfers/313a9679-bc15-42e9-80ef-e2305959a3d1]
    enabled: yes
    name: push-to-remote

    source_path: c:\out\sales
    source_filter: *
    delete_source_on_success: Yes

    destination_uuid: 5f304286-8d56-41f9-ba57-420a2303e90c
    destination_path: /Outbox/

    destination_path_actions:
      *.pdf, temporary-suffix, .tmp

When a transfer fails before completing the transfer of the file's content,
the incompletely transferred file on the destination keeps the temporary suffix.


temporary-prefix
^^^^^^^^^^^^^^^^

The `temporary-prefix` action allows uploading a file using a temporary
prefixed name,
renaming to the initial name once all the file content was transferred.

It takes a single option consisting of the characters used as the temporary
prefix.

With the following configuration, the file ``c:\out\sales\report.pdf`` will
be first transferred to ``/Outbox/TEMP_report.pdf``, then finally renamed to
``/Outbox/report.pdf``::

    [transfers/313a9679-bc15-42e9-80ef-e2305959a3d1]
    enabled: yes
    name: push-to-remote

    source_path: c:\out\sales
    source_filter: *
    delete_source_on_success: Yes

    destination_uuid: 5f304286-8d56-41f9-ba57-420a2303e90c
    destination_path: /Outbox/

    destination_path_actions:
      *.pdf, temporary-prefix, TEMP_

When a transfer fails before completing the transfer of the file's content,
the incompletely transferred file on the destination keeps the temporary prefix.


replace-separator
^^^^^^^^^^^^^^^^^

The `replace-separator` transformation is used to flatten a path defined across multiple directories and convert it into a simple file name.

It takes a single option which is the character or characters used to
substitute the path separators.
Depending on the source filesystem, it will replace the `/` or `\\` character.

For recursive transfers, the destination path in this transformation
is relative to the base `source_path`.

Having the following configuration::

    [transfers/313a9679-bc15-42e9-80ef-e2305959a3d1]
    enabled: yes
    name: copy-to-remote

    recursive: yes
    source_path: c:\out\sales
    source_filter: *
    delete_source_on_success: Yes

    destination_uuid: 5f304286-8d56-41f9-ba57-420a2303e90c
    destination_path: /Outbox/

    destination_path_actions:
      *.pdf, replace-separator, --
      *.txt, replace-separator, _

the files will be transferred as follows::

    c:\out\sales\Report.PDF          -> /Outbox/Report.PDF
    c:\out\sales\Report.txt          -> /Outbox/Report.txt
    c:\out\sales\report.csv          -> Fail as it does not match any rule.

    c:\out\sales\18\Jan\Report.PDF   -> /Outbox/18--Jan--Report.PDF
    c:\out\sales\18\Jan\Report.txt   -> /Outbox/18_Jan_Report.txt
    c:\out\sales\18\Jan\report.csv   -> Fail as it does not match any rule.


lowercase
^^^^^^^^^

The `lowercase` is a simple transformation that will transfer the file using destination file path and file name all in lower case.
It takes no options.

..  note::
    If the remote filesystem is case-insensitive and a file with the same
    name (but different cases) exists, the remote name is kept.

Below is an example for the `lowercase` transformation::

    [transfers/313a9679-bc15-42e9-80ef-e2305959a3d1]
    enabled: yes
    name: copy-to-remote

    recursive: yes
    source_path: /out/sales
    source_filter: *
    delete_source_on_success: Yes

    destination_uuid: 5f304286-8d56-41f9-ba57-420a2303e90c
    destination_path: /Outbox/

    destination_path_actions:
      *.pdf, lowercase
      *, no-action

With the above configuration, the following files will be transferred as exemplified below.
Note that the base destination path as defined in the transfer configuration,
is not affected by the file path and file name transformation.
Files like ``report.txt`` are transferred since they match the
`no-action` rule::

    /out/sales/Report.PDF          -> /Outbox/report.pdf
    /out/sales/Report.txt          -> /Outbox/Report.txt

    /out/sales/Jan/Report.PDF      -> /Outbox/jan/report.pdf
    /out/sales/Jan/Report.txt      -> /Outbox/Jan/Report.txt


fixed-path
^^^^^^^^^^

The `fixed-path` action is a simple transformation that will transfer the file using a fixed destination.
It takes a single option, the full destination path.
The `destination_path` configuration is ignored for the `fixed-path` action.

..  note::
    If this action is enabled, the value defined at `destination_temporary_suffix` is ignored.
    You can still enable the temporary file name functionality by using the dedicated `temporary-prefix` or `temporary-suffix` actions.

Below is an example for the `fixed-path` transformation::

    [transfers/313a9679-bc15-42e9-80ef-e2305959a3d1]
    enabled: yes
    name: copy-to-remote

    recursive: yes
    source_path: /out/sales
    source_filter: *
    delete_source_on_success: Yes

    destination_uuid: 5f304286-8d56-41f9-ba57-420a2303e90c
    destination_path: /Outbox/

    destination_path_actions:
      *, fixed-path, //'PDEB.OU11.DRSAFG(+1)'

With the above configuration, the following files will be transferred
as exemplified below.
Note that the base destination path as defined in the transfer configuration,
is ignored::

    /out/sales/Report.PDF          -> //'PDEB.OU11.DRSAFG(+1)'
    /out/sales/Report.txt          -> //'PDEB.OU11.DRSAFG(+1)'

    /out/sales/Jan/Report.PDF      -> //'PDEB.OU11.DRSAFG(+1)'
    /out/sales/Jan/Report.txt      -> //'PDEB.OU11.DRSAFG(+1)'


Fallback destination path
-------------------------

When using the `destination_path_actions` to define a transfer with dynamic destination path,
some transfer might fail as the *computed* destination path doesn't exist.

The `destination_fallback_path` configuration can be used as a *catchall* method to ensure the remote files are transferred to the destination location.

For example, if you want to pull reports from a server,
and automatically route them into directories using `destination_path_actions`,
and one of the route targets does not exist,
you can route them to a fallback folder.

A transfer can have multiple actions defined for the same path, and the
actions will be applied in series.
The result from one action will be passed to the next one.

.. code-block:: ini
   :emphasize-lines: 10

    [transfers/313a9679-bc15-42e9-80ef-e2305959a3d1]
    enabled: yes
    name: pull-partner-reports

    recursive: no
    source_uuid: 5f304286-8d56-41f9-ba57-420a2303e90c
    source_path: /remote/partner/

    destination_path: D:\reports\acme-inc\others
    destination_fallback_path: D:\reports\acme-inc\unknown

    destination_path_actions:
      m/.*report_(.*).pdf/, transfer, D:\reports\acme-inc\{group.1}\{path.file_name}
      *, no-action

Assuming that the following directories exist on the local filesystem,
which is the destination::

    D:\reports\acme-inc\sales\    -> receives sales reports
    D:\reports\acme-inc\stocks\   -> receives stocks reports
    D:\reports\acme-inc\unknown\  -> catchall for other report files
    D:\reports\acme-inc\others\   -> catchall for any non-report file.

the files will be transferred as follows::

    /remote/partner/report_sales_Jan.pdf    -> D:\reports\acme-inc\sales\report_sales_Jan.pdf
    /remote/partner/report_stocks_Jan.pdf   -> D:\reports\acme-inc\stocks\report_stocks_Jan.pdf
    /remote/partner/report_toys_Jan.pdf     -> D:\reports\acme-inc\unknown\report_toys_Jan.pdf
    /remote/partner/returns_Jan.pdf         -> D:\reports\acme-inc\others\returns_Jan.pdf

Note that `report_toys_Jan.pdf` is not copied into the ``others`` directory.
It's copied into the ``unknown`` directory.
It has the pattern of a *report* file,
but there is no dedicated report folder named `toys` on the destination
to receive it.


Source content conversion on the fly
------------------------------------

When performing a transfer, SFTPPlus can convert the content of the source file and write the transformed content to the destination while keeping the source file unchanged.

The content conversion is done on the fly / on the wire, without changing the content of the source file.

Below is an example for configuring a transfer to upload a source file with UTF-16 encoding by writing the content on the remote location using ASCII encoding::

    [transfers/313a9679-bc15-42e9-80ef-e2305959a3d1]
    enabled: yes
    name: copy-utf16-remote-ascii

    recursive: no
    source_path: /out/sales
    source_filter: *
    delete_source_on_success: Yes

    destination_uuid: 5f304286-8d56-41f9-ba57-420a2303e90c
    destination_path: /Outbox/

    destination_content_actions:
      *.txt, encoding, utf-16-to-ascii
      *, no-action

With the above configuration, a file named `/out/sales/Report.txt` that is stored on the source disk as UTF-16 is transferred to `/Outbox/Report.txt` as ASCII content, while the source file is kept as UTF-16.

A file named `/out/sales/Report.pdf` is transferred to the destination,
having the exact content as the source file::

    /out/sales/Report.pdf          -> /Outbox/Report.pdf with unmodified content.
    /out/sales/Report.txt          -> /Outbox/Report.txt with ASCII encoding.

For the `encoding, utf-16-to-ascii` action,
if the source file has no BOM, UTF-16LE is assumed as the default value.
Get in touch with us if you need to handle UTF-16BE as the default encoding.


Transfer States
---------------

A transfer can be in one of the following states:

* `Stopped` - the transfer is not active and is not configured to be active at
  any time.
* `Started` - the transfer is active and processing files from the source.
* `suspended` - the transfer was started, but it is outside of its activity
  schedule.
* `Source failed` - the source location is not available and files at the source are not processed.
  Processing will be started as soon as the source location is available,
  either by fixing the errors and manually starting it or by an automated
  location reconnection process.
* `Destination failed` - The destination location is not available.
  Processing will resume as soon as the destination location is available,
  either by fixing the errors or manually starting it.
* `Failed` - a critical error occurred while executing the transfer and the
  transfer was stopped. Manual intervention is required to restart the
  transfer.


Location States
---------------

A location can be in one of the following states:

* `Stopped` - no transfer is using this location and it was not manually
  started.
* `Started` - the location is connected to the remote location.
* `Disconnected` - the location is not connected to the remote location, but it
  will auto-reconnect when required by a transfer.
* `Failed` - the location failed to connect to the remote location.
  Manual intervention is required to restart the location.


Fault-tolerant transfers
------------------------

SFTPPlus will do its best to perform the requested transfers and under certain circumstances will retry on transfer failures.

From the configuration, you can define the number of times to retry and the
time interval to wait after retries.

Once all retries are exhausted, the transfer will fail and SFTPPlus will no
longer try to process/transfer that file.

Files that were previously failed to be transferred,
can be processed/transferred again by restarting the transfer.


Fault-tolerant source monitoring
--------------------------------

When a transfer is started, SFTPPlus will check for the required
permissions to monitor the source path for changes,
the configured path exists and this path is valid.

If the source path was available at startup, but after some time it is no longer available and it fails to get the content of the source path,
SFTPPlus will retry the after `changes_poll_interval` seconds.

This is done for a number of time configured by the `retry_count` option.
An event is emitted on each failure.

Once the source path is available again, the transfer is resumed and new or changed files will be transferred.

The most common errors found on all supported protocols are:

* Source path not found.
* Source path without reading or listing permissions.
* Connection closed while the source was checked.


Resumed transfers
-----------------

Resuming unfinished transfers, either upload or download, is supported
across available file transfer protocols as follows:

========== ========== ========
 Protocol   Download   Upload
========== ========== ========
 FTP/FTPS   Yes        Yes
 SFTP       Yes        Yes
 SCP        No         No
 HTTP       Yes        No
========== ========== ========

..  note::
    Our roadmap includes adding support for resuming transfers across all
    available protocols.
    In the case that resume support is not available for your preferred transfer protocol, please contact us.


Hard Links and Symbolic Links
-----------------------------

Hard links and symbolic links are observed as normal files.

When both the link and original are monitored, changes to the link will trigger
notifications for the original file as well as any other hard links pointing
to it.

When only the link is monitored, changes to the source will also trigger notifications.


Resolving duplicate / successive events
---------------------------------------

When an event occurs at the source location, it is not signaled right away.
A buffer time interval is used to remove duplicate events and emit the event
only once the file or folder is stable.

For example, when a large file is copied, the operating system will emit a
stream of events after each intermediary change.
The monitor will queue these changes and merge them into a single event.

The time frame in which duplicate events are resolved is `1 second`.
After an event occurs, it waits 1 second before emitting the event.
If no event occurs for the same source, the event is emitted.
Otherwise, the event is merged and the time interval is extended by another
second in which it can be further merged with another event, or emitted.

Here is the list of events that are emitted.
Path is used as a generic reference to a file or a folder:

* Existing - for paths that are already present when the process is started.
* Modify - for a path that has a changed size or modify time.
* Delete - for a path that is no longer in the monitored path.
  Either removed from there or moved to a path that is not monitored.
* Create - for a path that has appeared in the monitored path.
  Either created there or moved from a path that is not monitored.
* Moved - for a path that was renamed / moved inside the monitored path.

Here are the rules based on which events are resolved:

* Existing + Modify = Existing
* Existing + Delete = Ignore

* Modify + Modify = Modify (and wait for next event)
* Modify + Delete = Delete (without delay)
* Modify + Move = Move + Modify (modify is last)

* Create + Modify = Create (and wait for next event)
* Create + Delete = Discard (file was created for a very short time)
* Create + Move = Create (at the moved path)

* Delete.File + Create.File = Modify (the file was completely replaced)
* Delete.Folder + Create.File  = Create.File

* Moved + Created = Moved + Created (with delay)
* Moved + Modified = Moved + Modified (with delay)
* Moved + Deleted = Deleted for the source path


Executing commands using pre/post transfer executables or scripts
-----------------------------------------------------------------

SFTPPlus allows configuring a transfer to execute at certain transfer steps:

* Execute before processing a source file
* Execute after the success of a file transfer
* Execute after the failure of a file transfer

The configuration from this example,
will copy (indicated by `delete_source_on_success: No`) files from a source
(indicated by `source_path` and `source_uuid`) to a destination (indicated
by `destination_path` and `destination_uuid`).
A `timestamp-always` is set in the `overwrite_rule` in order to always
copy the source file with an amended timestamp and prevent accidental
overwriting on the destination.
It will poll (via `changes_poll_interval`) for changes to the folder every
``5`` seconds.
After ``10`` seconds of no changes to a file (indicated by `stable_interval`),
it will consider the file stable and ready to be processed.

A script (saved as a local file at
``C:\acme\sftpplus\transfer-jobs\after-success.bat``) is executed once a file
that has been successfully transferred is considered stable.

The script is configured as::

    [transfers/7db823d8-05f8-4481-be98-b87a826ded28]
    execute_after_success = C:\acme\sftpplus\transfer-jobs\after-success.bat

There are additional processing actions within the custom script.
Processing actions include:

* Creating a zipped archive from a target source.
* Affixing a date to the archive.
* Moving the archive to another destination.

An example of the above configuration::

    [transfers/7db823d8-05f8-4481-be98-b87a826ded28]
    enabled = Yes
    name = inbox-transfer
    description = Transfer Inbox files.
    source_uuid = local-file-system-source-uuid
    source_path = C:\acme\sftpplus\accounting\inbox
    delete_source_on_success: No
    destination_uuid = local-file-system-destination-uuid
    destination_path = C:\acme\sftpplus\accounting\inbox-final
    execute_after_success = C:\acme\sftpplus\transfer-jobs\after-success.bat
    stable_interval = 10
    changes_poll_interval = 5
    overwrite_rule = timestamp-always
    batch_interval = 0
    retry_count = 0
    retry_wait = 0


Executing pre-/post- transfer destination commands
--------------------------------------------------

SFTPPlus allows configuring a transfer to execute a list of commands via the
following options:

* Execute after success on destination
* Execute before on destination
* Execute before success on destination.

These commands need to be available in the SFTPPlus `client-shell`
implementation.

To check what commands are available, please start the `client-shell` and
run::

    > help

To find out more about a particular command, run::

    > help COMMAND_NAME

These commands are configured as part of the Transfer section in the Local
Manager GUI and it can be added in the configuration text file like below::

    [transfers/99feb83f-a99d-42f1-a86c-1562c3281bb6]
    name = transfer_sample
    execute_on_destination_after_success = rename /path1 /path2; delete /path3
    execute_on_destination_before = client-shell-COMMAND /file/path
    execute_on_destination_before =
    rename /path-to/  /path2
    delete /path3

Transfers can execute either a single command or multiple commands.

Multiple commands are separated by a semicolon (;) or on a separate line.

.. include:: /operation/location-watch-about.include.rst


Batch transfer operation
------------------------

The default transfer operation for SFTPPlus is to transfer a file
as soon as it is detected and considered stable.
Each file will be processed as an independent transfer.
The pre/post command hooks and events are executed
as a separate process for each file.


File name or path-based batch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can configure SFTPPlus to wait and batch/group the files based on a file with a specific path or name.
This is done by using the `batch_marker_path` configuration option.
You can configure an exact file path,
a pattern matching a path,
or a list of exact file paths or path matching expressions.

The transfer will start only after the source contains all the files matching configured `batch_marker_path`.
The transfer can wait for one file or a fixed number of multiple files.

There is a 15 seconds delay before it begins transferring all the previous files.
Should there be new files created within the 15 seconds interval after the marker,
these files will be included in the batch transfer.

When filtering source files that are to be transferred,
the filtering rules should also include the file marker.
That is, when the `source_filter` option is used,
the batch marker file should be included in both `source_filter` and `batch_marker_path` expressions.

..  note::
    The matching expression is for the full file path and not only for the file name.
    If you want to match a file name `complete.txt` located in any directory you should configure it as `*complete.txt`.

The marker file or files are also transferred.

For more details about defining a file marker,
see the :doc:`matching expression documentation
</configuration/matching-expression>`.

The following example will filter the source for both `.pdf` and `.desc` files.
The transfer will start 15 seconds after a `report.desc` file is generated in any of the subdirectories for ``c:\jobs\reports``.
For example, in ``c:\jobs\reports\ACC-2018-09-23\report.desc`` or ``c:\jobs\reports\ACC-2018-09-24\report.desc`` ::

    [transfers/a4747959-25de-470a-b76e-afe08071a70d]
    enabled: yes
    name: Move report set.
    description: Move all report files once the report is finalized.
       A report.desc file is generated by the external reporting process
       to signal that the process is complete.

    recursive: Yes
    source_uuid: c4b74ed0-b952-4edc-be24-7d8e1e6d8068
    source_path: c:\jobs\reports
    source_filter: m/*.(pdf|desc)/
    delete_source_on_success: Yes

    destination_uuid: 92eb50d4-bfc2-4b15-a369-f0d74dc68dac
    destination_path: /dropbox/

    batch_interval: 0
    batch_marker_path: *done.desc

With the configuration from above, assume that you have the following files::

    c:\jobs\reports\ACC-123\in.pdf
    c:\jobs\reports\ACC-123\out.pdf
    c:\jobs\reports\ACC-123\response\report.pdf
    c:\jobs\reports\MON-542\office.pdf
    c:\jobs\reports\MON-542\storage.pdf
    c:\jobs\reports\MON-542\response\report.pdf
    c:\jobs\reports\MON-542\done.desc

then the following actions are taken on these files::

    c:\jobs\reports\ACC-123\in.pdf               - Not transferred
    c:\jobs\reports\ACC-123\out.pdf              - Not transferred
    c:\jobs\reports\ACC-123\response\report.pdf  - Not transferred
    c:\jobs\reports\MON-542\office.pdf           - Transferred
    c:\jobs\reports\MON-542\storage.pdf          - Transferred
    c:\jobs\reports\MON-542\response\report.pdf  - Transferred
    c:\jobs\reports\MON-542\done.desc            - Transferred

The batch marker should match a single file for a certain directory and
its descendants.
The following file structure is valid and the files will be transferred since
the marker files are in different folders which are not a descendant of
another::

    c:\jobs\reports\ACC-123\in.pdf
    c:\jobs\reports\ACC-123\out.pdf
    c:\jobs\reports\ACC-123\done.desc            - Marker file
    c:\jobs\reports\MON-542\storage.pd
    c:\jobs\reports\MON-542\done.desc            - Marker file

The following file structure will fail since ``MON-542\response\report.pdf``
is triggered by both ``MON-542\response\done.desc`` and
``MON-542\done.desc`` ::

    c:\jobs\reports\MON-542\done.desc        - Marker file
    c:\jobs\reports\MON-542\storage.pdf      - Triggered by MON-542\done.desc
    c:\jobs\reports\MON-542\resp\done.desc   - Marker file
    c:\jobs\reports\MON-542\resp\report.pdf  - Triggered by MON-542\done.desc
                                               and MON-542\resp\done.desc


Multiple batch markers
^^^^^^^^^^^^^^^^^^^^^^

A transfer can be configured to delay starting the batch files only after a specific set of files are present in the source directory.

The following example will filter the source for both `.pdf` and `.desc` files.
The transfer will start after a `report.desc` file is generated in any of the subdirectories for ``c:\jobs\reports``.
The start is delayed by `stable_interval` plus 3 seconds after no other file is added to the batch.
Files added after the marker will still be included in the same batch and will delay the start of the batch.

For example, in ``c:\jobs\reports\ACC-2018-09-23\report.desc`` or ``c:\jobs\reports\ACC-2018-09-24\report.desc`` ::

    [transfers/a4747959-25de-470a-b76e-afe08071a70d]
    enabled: yes
    name: Move report set.
    recursive: No
    source_uuid: c4b74ed0-b952-4edc-be24-7d8e1e6d8068
    source_path: c:\jobs\reports
    source_filter: *.pdf | *.marker
    delete_source_on_success: Yes
    destination_uuid: 92eb50d4-bfc2-4b15-a369-f0d74dc68dac
    destination_path: /dropbox/

    batch_interval: 0
    batch_marker_path:
      *expenses.done
      *orders.done

Having the above configuration, assuming the following files are present in the source,
the transfer will not start just yet, since the ``orders.done`` marker file is not yet detected::

    c:\jobs\reports\June-expenses.pdf
    c:\jobs\reports\June-expenses.done
    c:\jobs\reports\June-orders.pdf

The transfer will start as soon as the ``c:\\jobs\\reports\\June-orders.done`` file is detected
and all the files are transferred together::

    c:\jobs\reports\June-expenses.pdf
    c:\jobs\reports\June-expenses.done
    c:\jobs\reports\June-orders.pdf
    c:\jobs\reports\June-orders.done


Time-based batch transfers
^^^^^^^^^^^^^^^^^^^^^^^^^^

By using the `batch_interval` configuration option,
you can instruct SFTPPlus to only start transferring files once no new files
are detected in the specified time interval.

All the files detected during this interval will be transferred together as a
single transfer.
The pre/post command hooks and events are executed once for the batch of files.


Batch transfer and scheduling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a transfer is stopped and there are files queued for a batch transfer,
SFTPPlus will not transfer the files but will instead emit a warning to
inform the user of this action.

When a transfer is suspended, and there are files in a batch that are not yet
triggered, the files are not transferred and no warning info is emitted.
The files will be transferred once the transfer is resumed and the batch
is triggered by one of the batch triggering conditions.

When a batch transfer is in progress and the transfer is suspended, the
active batch will continue to be transferred.


Pushing files to mainframe systems
----------------------------------

The IBM z/OS (OS/390) mainframe operating system provides 2 main methods
to access files:

* MVS record-oriented data access methods (PDS PDS/E) backed by sequential
  or direct access storage devices (DASD).
* UNIX System Services (USS) using regular Unix paths file `/parent/file.txt`.

The UNIX System Services provide a standard POSIX path which can be handled similarly to the way Linux of macOS file access works.

SFTPPlus supports uploading files to a record-oriented dataset and setting the
options for the upload.

Dovetail Co:Z SFTP for z/OS or Tectia SFTP Server for z/OS provide various
extensions to facilitate interoperability for MVS datasets.

Below is an example for setting the record format and the logical record length
for pushing a file to a server using Tectia SFTP.
Each file is appended to the `PDEB.OU11.DRSAFG` data set.
The destination path is set to the UNIX root (`/`), but it is ignored, as we
configure the transfer for a fixed path.
File transfer advice strings (FTADV) is used to specify z/OS specific options::

    destination_uuid: 44cef305-4f01-43b4-9894-6394e91d50db
    destination_path: /
    destination_path_actions:
        *, fixed-path, "/FTADV:RECFM=FB,LRECL=1024/___//'PDEB.OU11.DRSAFG(+1)'"

Here is an example for a similar transfer to a Co:Z SFTP server::

    destination_uuid: 44cef305-4f01-43b4-9894-6394e91d50db
    destination_path: /
    execute_on_destination_before: ls /+lrecl=1024,recfm=fb
    destination_path_actions:
        *, fixed-path, //PDEB.OU11.DRSAFG(+1)
