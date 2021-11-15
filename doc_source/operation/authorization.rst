Accounts Authorization
######################

.. contents:: :local:


Introduction
============

The server-side security of SFTPPlus is designed based on the
Authentication, Authorization and Accounting (AAA) components.

This pages focuses on the Authorization component.
For the Authentication part, check
:doc:`the authentication documentation</operation/authentication>`
while for the Accounting, check
:doc:`the account documentation</guides/event-handlers>`.

Once an account is authorized as part of the login procedure of each file
transfer service, SFTPPlus will receive the configuration for that account.

As part of the account's configuration, the `permissions` option is dedicated
to defining access rights to files and folders.

The permissions are applied to all of the files and folders that are available
in that account.


Effective Permissions
=====================

In SFTPPlus, permissions are defined based on paths, and are
not attached to actual files or directories.
Permissions are applied based on a path-matching expression.

One advantage of this method is that you can define permissions for files
and folders not created yet.

Another advantage against traditional file system permissions is that,
for example, it's easy to set different permissions based on file extension.

Different permissions can be applied for different files and folders
available to an account.

The path used for selecting permissions is the *virtual path*.
That is the path as it is visible to the file transfer client, and not the
actual full path on the server storage.


Combined Permissions and Precedence
===================================

When establishing permissions, you need to specify whether an operation should
be accepted (allow) or rejected (not allow / deny) for the targeted path.

An account can have multiple permissions.

In this case, an operation permission is granted if it is permitted by at
least one of the configured permissions.

For example, to allow reading and writing files and to disallow creating or
deleting folders, you can set the permissions as::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    permissions = allow-read, allow-write

"Deny" permissions take precedence over "allow" permissions.
If you set `allow-read, deny-full-control`, the effective permission would be
`deny-full-control`, and read access would be denied..
The implicit `deny-read` implied by `deny-full-control` takes precedence
over the explicit `allow-read` configuration.


Global and Per-Path Permissions
===============================

In the example below the account ``johnd`` has its home folder in
``c:\Users\johnd\ftp-files`` and access is locked (chrooted, jailed) in that
folder.
File transfer client will see that folder as their root folder.
The ``/inbox/*`` path matching expression will apply to the files and folders
from ``c:\Users\johnd\ftp-files\inbox\`` ::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    enabled = True
    type = application
    name = johnd
    home_folder_path = c:\Users\johnd\ftp-files
    permissions =
        allow-read
        /inbox/*, allow-full-control

The first set of permissions are called *global permissions* and they apply
to any path for which there is no explicit configuration.

The permission rules are checked from the first to the last configuration,
in the order that is added in the configuration file.
As soon as a path matches an expression, it will apply the
permissions associated to that expression and continue on
with the check until the process is finished.
Global permissions are applied when it is found that no expression has
matched the path.

The configuration below shows an account which has read control to any file.
Regardless of its location, it can read or write CSV files.
It has full control permissions to any files or folders inside the
``/inbox/`` folder.
It can delete / create files and folders inside ``inbox`` which is located
in the root of the banse folder.
Note that the rule for CSV files has both `allow-read` and
`allow-write` permission
since a path specific rule will replace the defined global permissions::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    permissions =
        allow-read
        /inbox/*, allow-full-control
        *.csv, allow-read, allow-write

For the configuration example below,
the account will only have write access to CSV files located outside of the
``/inbox/`` folder.
For the ``/inbox/`` folder, it still has full control::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    permissions =
        allow-read
        /inbox/*, allow-full-control
        *.csv, allow-write

The order in which the rules are defined is important.
A good practice is to define them starting with the most specific and ending
with the most generic.
In the configuration example defined below,
the account does not have the the right the delete CSV files located in the
``/inbox/`` folder.
This is because the rule for ``inbox`` is defined after the generic
rule for CSV files::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    permissions =
        allow-read
        *.csv, allow-write
        /inbox/*, allow-full-control

The previous examples were all using the simple globbing rules.
For complex path matching expressions, you can use regular expressions.
For example, to give `allow-write` access to files prefixed by a number,
you can use::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    permissions =
        allow-read
        m/\d+-.*/, allow-write

Regular expressions can also be used to negate an expression.
The configuration example below allows `allow-read` permission to any file,
while granting `allow-write` permissions for PDF files::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    permissions =
        allow-write
        e/.*\.pdf/, allow-read

The path matching expression will only take into consideration the path
regardless of whether the path points to a file or a folder.
For example, the configuration example below will allow full control to any
file or folder inside ``/inbox/``, but the ``/inbox`` folder itself will have
the `allow-read` permission since it does not match the `/inbox/*` expression::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    permissions =
        allow-read
        /inbox/*, allow-full-control

For more details about the available expressions, see the
:doc:`matching expression documentation.
</configuration/matching-expression>`


Folders and their members
=========================

As permissions are based on the path,
there are a few caveats that you should be aware of.

In the following examples you will get `allow-full-control` for folder
``/inbox/`` and for any path inside it, like ``/inbox/test.text`` or
``/inbox/sub/folder/file.txt``.
In the same time, you also get `allow-full control` for a folder named
``/inbox-qa/``, as this path is matching the ``/inbox*`` expression::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    permissions =
        allow-read
        /inbox*, allow-full-control

When you want to limit permissions for a specific folder and any of its
subfolders,
the configuration should be defined as the example below.
In this case, a path like ``/inbox-qa/`` will only get `allow-read`::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    permissions =
        allow-read
        /inbox, allow-full-control
        /inbox/*, allow-full-control


allow-full-control Permission
=============================

When an account is set with `allow-full-control` permissions, it can perform
any file transfer operation.

All extra permissions are ignored.


deny-full-control Permission
============================

When an account is set with `deny-full-control` permissions, it can't perform
any file transfer operation.

All extra permissions are ignored, and any action is denied.


allow-read Permission
=====================

With the `allow-read` permission,
an account can obtain the attributes and read the contents of existing files.

It cannot set attributes, read the target of symbolic links,
list folders or delete or rename files or folders.


allow-list Permission
=====================

The `allow-list` permission allows
an account to list the contents of a folder and get the attributes for the
files in that folder.

It also allows reading the target of symbolic links.


All other operations are denied.
For example, it cannot set attributes, delete or rename files or folders
in the targeted folder.


allow-traverse Permission
=========================

The `allow-travere` permission allows
an account to only see the folders during a normal listing operations.

It behaves like the `allow-list` permission, but non-folder members are hidden.

The FTP NLST command is not allowed under this permission.
NLST is only allowed with `allow-list`.
Please get in touch if you need `allow-traverse` to allow the FTP NLST command.

All other operations are denied.
For example, it will not allow getting the attributes for files.


allow-create-folder Permission
==============================

With the `allow-create-folder` permission, an account can create
new folders.

All other operations are denied.
For example, this permission does not allow creating files or renaming folders.


allow-write Permission
======================

With the `allow-write` permission, an account can create new files,
overwrite or append the content of existing files.

All other operations are denied.
For example, this permission does not allow reading files or listing folders.


allow-rename Permission
=======================

Using the `allow-rename` permission, an account can rename existing files.

The rename operation allows overwriting existing files as part of the rename
process.

The `allow-rename` permission needs to be set for both source and destination.
Otherwise, either the source or destination path will require full permissions.


allow-delete-file Permission
============================

With the `allow-delete-file` permission, an account can delete existing files.

All other operations are denied.
For example, this permission does not allow deleting folders or writing
to existing files.


allow-delete-folder Permission
==============================

With the `allow-delete-folder` permission, an account can delete existing
folders.

All other operations are denied.
For example, this permission does not allow deleting files or renaming
existing folders.


allow-set-attributes Permission
===============================

With the `allow-set-attributes` permission, an account can set the
attributes of existing files and folders.

All other operations are denied.
For example, this permission does not allow writing to existing files or
creating folders.
