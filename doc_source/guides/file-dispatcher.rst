.. container:: tags pull-left

    `server-side`
    `client-side`
    `configuration`


File Dispatcher Event Handler
#############################

..  contents:: :local:


Introduction
============

The file dispatcher is a generic event handler which is used to perform
various actions on the files on which SFTPPlus operates.

As any event handler you can define all the available filtering rules for
defining the scope on which the handler should be triggered.

It can be used for both server-side and client-side operations.

A common server-side use case is to move the file outside of a single inbox
used by a remote account to push the files, and forward the files to a
different internal team which needs a copy of the pushed file.

For the client-side, a common use case is to move or copy the pulled files
to various local folders, once the file was copied from the remote server.

In this way there is a separation of concerns among various components which
take part in a managed file transfer process.

One component will make sure the files are received and handled using various
file transfer protocols like SFTP or FTPS.
Once the files are received via the protocols, a separate component can be
configured to further process the files, outside of the realm of FTPS or HTTPS
file transfer protocols.


Operation Principle
===================

The `file-dispatcher` event handler, when configured to be triggered for an
event will use the path attribute associated with the event and perform an
action on that path.

Not all events can be used with this event handler.
Only events which have have an associated path on the local filesystem can
be used.

For example, the events from the group `file-operation` can be used together
with the `file-dispatcher` event handler,
since those events have an event attribute pointing to path on the local
filesystem.

Using the `dispatch_attribute` configuration you can define which attribute
of the event to use for triggering the actions.

When used for server-side operations,
the file transfer actions have both a real and virtual path.
A remote file transfer client authenticated as username ``johnd``,
will upload a file using a path like ``/inbox/REPORT_123.PDF``,
this is the virtual path.
On the server, that file is actually stored as
``/storage/users/john/inbox/REPORT_123.PDF``,
this is the real path.
The `dispatch_attribute` should be configured with the real path of the file
to be handled.
Using a virtual path will cause the file not to be dispatched appropriately as
it will use the virtual (non-existent) path as the source.

The file dispatching will fail if the event does not have the configured
attribute.

..  note::
    Please make sure that you are not attaching this event handler to
    file events for which the path was not yet closed.
    In such scenarios the move operation will fail.

When the event handler starts, it will try to validate the current
configuration.
The event handler will fail to start when the configuration is invalid.

Some configuration options can only be validated at execution time,
at the moment when a certain action is triggered for an event.
In such cases the event handling will fail and the failure count will be
increased.
Such a condition can be found when configuring the dispatch handler for an
event ID which has no associated paths.


Matching expressions
====================

The `dispatch_rules` will have a matching expression defined as the second
member of the configuration.

This is used to decide the paths for which the action is triggered.

The matching expression is checked against the full path of the file.

As an example, if you want to match files based on the naming convention
`INV_NNNN.csv` (like `INV_0023.csv` or `INV_1202.csv`),
located in any directory, use a configuration similar to::

    [event-handlers/a0cf-d14500774340]
    dispatch_rules = move, */INV_*.csv, /srv/teams/invoicing

When you want to match only files inside a certain folder,
make sure to include that folder as part of the matching expression.
For example, a file named ``REPORT_123.csv`` will be moved to
``/srv/teams/invoicing`` when placed into the source folder ``/invoicing`` and
moved to ``/srv/teams/ops`` when placed into the source folder
``/operations``::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, /invoicing/REPORT_*.csv, /srv/teams/invoicing
        move, /operations/REPORT_*.csv, /srv/teams/ops

..  note::
    The `fallback_rule` has no configuration for the matching expression
    since this is used for files which are not matching any of the
    configured expressions.

For more details about the available expressions see the
:doc:`matching expression documentation.
</configuration/matching-expression>`


Regular Expressions and Grouping
================================

When regular expressions are defined for the path matching expression,
you can use the parentheses for grouping parts of the source path which,
once matched, can be used to dynamically define the destination path
based on the source path.

..  note::
    The exclusion regular expression mode (``e/some/.*.pdf``) is not supported
    for group substitution.

..  note::
    The group substitution is not available for the fallback rule as there
    is no matching expression for that configuration.

For the purpose of this section, it is assumed that you are already familiar
with the regular expression.
Here you can
`read more about
<http://en.wikipedia.org/wiki/Regular_expression#Basic_concepts>`_ the
regular expressions.

For example, to have a file which is pushed to a path
``/inbox/accounting/john/SRV_123.PDF`` and moved to the path
``/reports/john/teams/accounting/SRV_123.PDF``
use the following configuration::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, m/inbox/(.+)/(.+)/SRV_.+\.PDF/, /reports/{2}/teams/{1}/

The first pair of parentheses will match the source team name and the second
pair will match the source username.
You can then used the matched valued as `{1}` or `{2}` etc to generate the
destination path.

The first group to be matched is `{1}`.

The group matching can be used the dynamically generate the destination
directory or the generate the full destination path.

When groups are used in the configured destination and the
configuration does not end with a path separator,
it will use the configuration to generate the full path for the destination.
Otherwise, it will dynamically generate only the destination directory and
use the source filename to generate the full path.

For example, to have a file which is pushed to a path
``/users/john/SRV_123.PDF`` and moved to the path
``/staging/john-SRV_123.PDF.in`` use the following configuration::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, m/users/(.+)/(SRV_.+\.PDF)/, /staging/{1}-{2}.in

To let SFTPPlus generate the destination path and for example have the file
pushed as ``/user/john/SRV_123.PDF`` moved to the path
``/staging/john/SRV_123.PDF``, use the following configuration::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, m/users/(.+)/SRV_.+\.PDF/, /staging/{1}/


Destination path variables
==========================

The destination path can be defined to include values from
a set of dynamic variables based on each event.

Assume you have 2 accounts named ``john-d`` and ``jane-r`` with home
directories in ``C:\SFTP-In\john-d`` and ``C:\SFTP-In\jane-r`` respectively.

When ``john-d`` or ``jane-r`` uploads a file named ``/reports.xml``
inside their root folder, the actual file is received on disk as
``C:\SFTP-In\john-d\app\report.xml`` or
``C:\SFTP-In\jane-r\app\report.xml``.

You might need to move both reports into a common internal application
inbox directory with file names like
``C:\App-In\john-d_report.xml`` or ``C:\App-In\jane-r_report.xml``.

This can be done using the following configuration, in which only the files
placed inside the `app` sub-directories are moved::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, g/C:\SFTP-In\*\app\*/, C:\App-In\{account.name}-{data.file_name}

You can also define the following configuration, in which any file uploaded
by a user is moved::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, g/.*/, C:\App-In\{account.name}-{data.file_name}

or defined using regular expression syntax with matching groups enabled::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, m/(.*)/i, C:\App-In\{account.name}-{data.file_name}

..  note::
    The usage of explicit `g/EXPRESSION/` globbing matching syntax or
    regular expression with groups is required for destination path
    variables.

    This is required for backward compatibility with older configurations
    in which the destination configuration was defining only the base
    destination directory.


Destination path normalization
==============================

The destination paths are normalized and any forward slash or backward slash
is automatically converted to the path delimiter used by the operating system
hosting the STPPlus application.

For example if you have the following configuration on a Linux system,
the destination path is ``/staging/john/SRV_123.PDF``::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, m/users/(.+)/SRV_.+\.PDF/, \staging\{1}\

While with the following example on Windows
the destination path is ``C:\staging\john/SRV_123.PDF``::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, m/C:\\users\\(.+)/SRV_.+\.PDF/, c:/staging/{1}/


Advanced Regular Expressions
============================

Using the `matching_expressions` configuration, you can create a destination
path using multiple data sources, not only the path of the handled file.

At the same time, you can transform the values to uppercase or lowercase.

As an example, suppose we handle ZIP archives copied to
`/inbox/AcmeCo-reports.zip`
containing files `/sales.csv` and `/returns.csv`.
The system is configured to automatically extract the files to
the `/storage/received/` path.
Upon normal operation, this would result in `/received/sales.csv` and
`/storage/received/returns.pdf`.

However, if you want to have these files extracted as
`/received/sales-AcmeCo.csv` and
`/received/returns-AcmeCo.pdf`, you can use the following
configuration:::

    matching_expressions:
        source_path, m//inbox/(\d{6})-.+.zip/i

    dispatch_rules:
        rename, m/.+/(.+\)\.([a-z])/i, /received/{1}-{source_path.1}.{2}

Using character case transform operations, you could have the files extracted as
`/received/sales-ACMECO.csv` and
`/received/returns-ACMECO.pdf` with the following configuration::

    matching_expressions:
        source_path, m//inbox/(\d{6})-.+.zip/i

    dispatch_rules:
        rename, m/.+/(.+\)\.([a-z])/i, /received/{1}-{source_path.1_upper}.{2}


Triggering the Dispatch Rule
============================

For the `dispatch_rules` configuration option you can specify multiple rules,
one per line.

Multiple rules are checked in the order of their definition.

The dispatch will stop after the first rule which matches the current
file path.

When none of the configured path matching expression could match the path
associated with the handled event, the fallback rule is used.

When no fallback rule is defined and none of the configured expression
matches the path no action is taken by the event handler.


Events with multiple paths
==========================

Some events emitted by SFTPPlus have associated multiple paths.

You can still use the file dispatcher together with those events.

The actions are executed for each of the associated files.

The event handling operation is aborted when failing to perform the
configured action for one of the associated files.
In this case the remaining files are not actioned.


File Overwrite Prevention
=========================

The file dispatcher will not overwrite existing file and the whole dispatch
process will fail if one of the configured destinations already contains
a file with the same name.


Handling of temporary / transient files
=======================================

It is common to have an external client or process pushing a file using
a temporary name and rename to the final name once the transfer is
complete.

In this case, you can use the `dispatch_delay` option to configure
the file dispatcher to execute the dispatching with a delay.
This will allow the file to be created with a final name.


Retry on errors
===============

The file dispatcher can be configured to retry the operation on error.

It can wait a configurable number of seconds before retrying.


Automatically creating destination folders
==========================================

The default behaviour of the file dispatcher event handler is to fail when
the destination does not exist.

The `create_destination_folder` configuration option can be used to
automatically create the destination.

To create the parent for the destination folder,
set the event handler as the following example.
To prevent accidental configurations,
the event handler will still fail if the path to the parent folder does not
exist::

    [event-handlers/f040be6a-e158]
    create_destination_folder = parent


Copy Action
===========

The `copy` action will create copies of the source file in each
of the configured destinations.

If for any reason the file fails to be successfully copied to any of the
destination, the process of copying to the remaining destination is aborted.

For example, to have a file named RPT_123.xml copied to both
``/data/teams/invoicing/RPT_123.xml`` and ``/data/teams/ops/RPT_123.xml``,
use the following configuration::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        copy, */rpt_*.xml, /srv/teams/invoicing, /srv/teams/ops


Move Action
===========

The `move` action will create copies of the the source file in each
of the configured destinations.

Once the file is copied to all the destinations, it will delete the source
file.
This is the reason why it is named `move`.

If for any reason the file fails to be successfully copied to any of the
destination, the source file is not removed.

For example, to have a file named RPT_123.xml copied to both
``/data/teams/invoicing/RPT_123.xml`` and ``/data/teams/ops/RPT_123.xml`` and
then removed from the source, use the following configuration::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move, */rpt_*.xml, /srv/teams/invoicing, /srv/teams/ops


Move With Timestamp Action
==========================

The `move-with-timestamp` is similar to the `move` action but files are
created in the destination with a timestamp inserted at the end of the filename
but before the file extension.

When the file has no extension, the timestamp is suffixed.

This action is useful to dispatch files and mitigate the risk of overwriting
existing files.

The timestamp has a sub-seconds resolution.
The resolution is depended on the host operating system.

Besides the sub-second resolution,
the timestamp includes a random number so that even when you have multiple
files generated in the same sub-second,
they will still have different timestamps.

For example, to have a file named RPT_123.xml copied to both
``/data/teams/invoicing/RPT_123.2013-02-24-16-50-43-983422-042.xml`` and
``/data/teams/ops/RPT_123.2013-02-24-16-50-43-983422-042.xml`` and
then removed from the source, use the following configuration::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        move-with-timestamp, */rpt_*.xml, /srv/teams/invoicing, /srv/teams/ops


Rename Action
=============

The `rename` action does a rename of source path to destination path.

The rename is done on the full path.
You can use it to move a file from one path to another.

It is called renamed, since it can only be used with a single destination.
This is done in order to differentiate it from our other `move` actions,
which are performed on multiple destinations.

As long as the source and destination are on the same filesystem, the
operation will be atomic and instant.

The operation will fail if the destination already exists.

For example, to have a file named ``RPT_123.xml``
pushed to ``/inbox/reports`` folder,
renamed to ``/data/teams/ops/RPT_123.xml``,
use the following configuration::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        rename, /inbox/reports/rpt_*.xml, /srv/teams/ops


Rename with Unix Timestamp Prefix Action
========================================

The `rename-prepend-unixtime` action does a rename of source path to
destination path.

The renaming is done with prepending the Unix timestamp (with milliseconds)
to the source filename.

For example, to have a file named ``RPT_123.xml``
pushed to ``/inbox/reports`` folder,
renamed to ``/data/teams/ops/0031550404.009876-RPT_123.xml``,
use the following configuration::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        rename-prepend-unixtime, /inbox/reports/rpt_*.xml, /srv/teams/ops


Delete Action
=============

The `delete` action will delete the source path.
It does not require any configured destinations.


Ignore Operation Action
=======================

The `ignore` action will not perform any action on the path.
It does not require any configured destinations.

This action can be used to implement exceptions from a more generic rule
that might be configured in the same event handler.


For example, to have any XML file moved to another directory, with the
exception of XML files starting with `test-` you can use
something similar to following configuration::

    [event-handlers/f040be6a-e158]
    dispatch_rules =
        ignore, /import/test-*.xml
        move, /inbox/*.xml, /srv/db-app/import


Execute Action
==============

The `execute` action allows you to call an external executable or script
and pass a set of arguments that most often will include the source file path.

This action is useful to reuse the file name matching selection present in
the dispatch files and integrate it with custom external actions.

It is configured as a comma separated list of values, to make it easy to handle
spaces in the executable source path or the targeted file.

The first value is the path to the executable or script that is invoked for
the configured file pattern.

The remaining values are arguments used when calling the executable.
Remember to add commas between arguments.

For example, we move a local file to an S3 bucket using the AWS CLI.
It assumes that you are running SFTPPlus in an EC2 for which the S3 bucket role
was enabled at the instance level::

    [event-handlers/f040be6a-e158]
    target = 40017
    executable_timeout: 60
    dispatch_rules =
        execute, *.csv, /bin/aws, s3, move, {data.real_path}, https://test-bucket/{data.file_name}, --acl=private


It expects the execute command to finalize after `executable_timeout` seconds
and to exit with code `0`.

Any other exit code is considered an error and it will retry to process the
file based on the configured retry rules.

The following environment variables are set when calling the external
executable:

* `SOURCE_PATH` - path to the file that is dispatched
* `ARGUMENTS` - space separated list of configured arguments for the dispatcher
