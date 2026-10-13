Server-side path permissions
############################

..  contents:: :local:


Enforcement across file transfer protocols
==========================================

SFTPPlus applies the same account and group path permissions to server-side file operations over SFTP, SCP, FTP, FTPS, HTTP, HTTPS, and other supported file transfer protocols.
The requested operation must be allowed by both SFTPPlus permissions and the underlying storage permissions, such as operating system file permissions.
The client protocol does not provide a way to bypass these checks.

Permissions apply to the *virtual path* visible to the file transfer client, rather than the physical path on the server's storage.
They are not attached to individual files or folders, so a rule can also control paths that do not exist yet.
For example, a rule can restrict uploads based on the destination filename or extension.

`default_permissions` is a comma separated list of permissions used when no path rule matches.
`path_permissions` contains one rule per line: a glob or regular expression followed by at least one comma separated permission.
The individual permissions are described below.

Rules are checked in order.
The first matching rule supplies all permissions for the path, replacing the default permissions for that operation.
Later rules are not considered after a match.
For expression syntax, see :doc:`matching expressions</configuration/matching-expression>`.


Editing permissions in the Web Manager
======================================

Account and group pages provide separate editors for default and path permissions.
For default permissions, select or search for a permission to add its tag.
Use the remove button on a tag to remove that permission.
For each path rule, use the permission tags below its matching expression to add or remove permissions.
Removing all tags leaves the selection empty so you can choose permissions.
For accounts, select `inherit` to use the primary group's defaults.
Selecting `inherit` removes all other default permissions.
Selecting another permission replaces `inherit`.
`allow-full-control` and `deny-full-control` are also exclusive selections.

To add a path rule, enter a matching expression, choose at least one permission, and select *Add*.
The initial permission is `allow-list`, which you can change before adding the rule.
Edit the expression or permissions in the table, and use the arrow buttons to change rule precedence.
The first matching rule applies, so place specific rules before more general rules.

A row with no permissions remains visible while editing but is excluded from the saved configuration.
Selecting a permission activates it again.
Use the X button to delete a row from the table.
Apply changes from the review page to save the configuration.


Group inheritance for permissions
=================================

An account with `default_permissions = inherit` uses default permissions from its primary group.
If `inherit` is combined with other account default permissions, the other values are discarded and the primary group's defaults apply.
Default permissions from secondary groups never apply.

Path rules from all associated groups are inherited when either `default_permissions` or `virtual_folders` is set to `inherit` on the account.
This ensures that inherited virtual folders bring their group path permissions with them, even when the account defines its own default permissions.
The primary group's rules come first, followed by secondary groups in the order listed for the account.

The account's `path_permissions` rules are added before the inherited group rules.
An empty value, which is the default, adds no account rules and does not disable inherited rules.
This option does not accept `inherit`; inheritance is controlled through `default_permissions` and `virtual_folders`.

For example, these groups allow reading files by default and writing files under `/shared/`::

    [groups/education]
    name = Education
    default_permissions = allow-read
    path_permissions =
        /shared/*, allow-read, allow-write

    [groups/archive]
    name = Archive
    default_permissions = deny-full-control
    path_permissions =
        /archive/*, allow-read

The following account inherits both groups' path rules and adds a more specific restriction::

    [accounts/alice]
    name = alice
    type = application
    group = education, archive
    default_permissions = inherit
    virtual_folders =
    path_permissions =
        /shared/private/*, deny-full-control

The account rule is checked first, so access to `/shared/private/` and its contents is denied when the path matches that rule.
Other paths under `/shared/` use the primary group's read and write permissions.
Paths under `/archive/` use the secondary group's read permission.
Unmatched paths use the primary group's default read permission; the secondary group's default denial is ignored.

An account can instead define its own default permissions while inheriting virtual folders::

    default_permissions = allow-list
    virtual_folders = inherit
    path_permissions =

All group path rules still apply in this case.
The account's `allow-list` default applies only when none of those rules matches.

To use only account permissions, set explicit default permissions and do not inherit virtual folders::

    default_permissions = allow-read
    virtual_folders =
    path_permissions =

An explicit list of account virtual folders can also be used in place of the empty `virtual_folders` value.


Migrating older configurations
==============================

Existing account and group `permissions` settings are automatically split into `default_permissions` and `path_permissions`.
The first line supplies the default permissions, and subsequent lines supply the path rules.
Legacy accounts with empty or inherited permissions become `default_permissions = inherit` with an empty `path_permissions` value.
Legacy group settings with an empty value use `allow-full-control` defaults and no path rules.

The inheritance rules above apply after migration.
In particular, inheriting virtual folders also inherits group path rules when an account has custom default permissions.

For the configuration option references, see :doc:`accounts` and :doc:`groups`.


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
    virtual_folders =
    default_permissions = allow-read, allow-write
    path_permissions =

"Deny" permissions take precedence over "allow" permissions.
If you set `allow-read, deny-full-control`, the effective permission would be
`deny-full-control`, and read access would be denied.
The implicit `deny-read` implied by `deny-full-control` takes precedence
over the explicit `allow-read` configuration.


Default and Per-Path Permissions
================================

In the example below the account `johnd` has its home folder in
`c:\\Users\\johnd\\ftp-files` and access is locked (chrooted, jailed) in that
folder.
The file transfer client sees that folder as its root folder.
The `/inbox/*` path matching expression will apply to the files and folders
from `c:\\Users\\johnd\\ftp-files\\inbox\\` ::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    virtual_folders =
    enabled = True
    type = application
    name = johnd
    home_folder_path = c:\Users\johnd\ftp-files
    default_permissions = allow-read
    path_permissions =
        /inbox/*, allow-full-control

The `default_permissions` option applies to paths that do not match any rule in `path_permissions`.
Path rules are checked in order, and the first matching rule supplies all permissions for that path.
Later rules are not checked after a match.

The configuration below shows an account which has read access to any file.
Regardless of its location, it can read or write CSV files.
It has full control permissions to any files or folders inside the
`/inbox/` folder.
It can delete / create files and folders inside `inbox` which is located
in the root of the base folder.
Note that the rule for CSV files has both `allow-read` and
`allow-write` permission
since a path specific rule will replace the default permissions::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    virtual_folders =
    default_permissions = allow-read
    path_permissions =
        /inbox/*, allow-full-control
        *.csv, allow-read, allow-write

For the configuration example below,
the account will only have write access to CSV files located outside of the
`/inbox/` folder.
For the `/inbox/` folder, it still has full control::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    virtual_folders =
    default_permissions = allow-read
    path_permissions =
        /inbox/*, allow-full-control
        *.csv, allow-write

The order in which the rules are defined is important.
A good practice is to define them starting with the most specific and ending
with the most generic.
In the configuration example defined below,
the account does not have the right to delete CSV files located in the
`/inbox/` folder.
This is because the rule for `inbox` is defined after the generic
rule for CSV files::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    virtual_folders =
    default_permissions = allow-read
    path_permissions =
        *.csv, allow-write
        /inbox/*, allow-full-control

The previous examples were all using the simple globbing rules.
For complex path matching expressions, you can use regular expressions.
For example, to give `allow-write` access to files prefixed by a number,
you can use::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    virtual_folders =
    default_permissions = allow-read
    path_permissions =
        m/\d+-.*/, allow-write

Regular expressions can also be used to exclude matching paths.
The `e/` expression below matches paths that do not end in `.pdf`.
It grants read and write access to those paths, while PDF files retain the
default read permission::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    virtual_folders =
    default_permissions = allow-read
    path_permissions =
        e/.*\.pdf$/, allow-read, allow-write

Path matching expressions apply to both files and folders.
For example, the configuration example below will allow full control to any
file or folder inside `/inbox/`, but the `/inbox` folder itself will have
the `allow-read` permission since it does not match the `/inbox/*` expression::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    virtual_folders =
    default_permissions = allow-read
    path_permissions =
        /inbox/*, allow-full-control

For more details about the available expressions, see the
:doc:`matching expression documentation.
</configuration/matching-expression>`


Permissions for dynamic username-based paths
============================================

When configuring the permissions of a group, you can target paths that include the name of the authenticated user.

In the example below, when the account `JohnD` is authenticated,
it gets full access to the path `/queue/JohnD/pending`.
Note that the `${USER}` placeholder can be used anywhere in the path's name::

    [groups/202da724-a73d-4590-abfb-0717cded0d86]
    default_permissions = allow-list, allow-write
    path_permissions =
        /inbox/*, allow-read
        /queue/${USER}/pending*, allow-full-control


Folders and their members
=========================

As permissions are based on the path,
there are a few caveats that you should be aware of.

In the following examples you will get `allow-full-control` for folder
`/inbox/` and for any path inside it, like `/inbox/test.text` or
`/inbox/sub/folder/file.txt`.
At the same time, you also get `allow-full-control` for a folder named
`/inbox-qa/`, as this path is matching the `/inbox*` expression::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    virtual_folders =
    default_permissions = allow-read
    path_permissions =
        /inbox*, allow-full-control

When you want to limit permissions for a specific folder and any of its
subfolders,
the configuration should be defined as the example below.
In this case, a path like `/inbox-qa/` will only get `allow-read`::

    [accounts/202da724-a73d-4590-abfb-0717cded0d86]
    virtual_folders =
    default_permissions = allow-read
    path_permissions =
        /inbox, allow-full-control
        /inbox/*, allow-full-control


allow-full-control Permission
=============================

The `allow-full-control` permission permits any file transfer operation on the matching path.
Other allow permissions in the same rule are redundant.
The `deny-full-control` permission takes precedence when both are present.


deny-full-control Permission
============================

The `deny-full-control` permission denies every file transfer operation on the matching path, including operations allowed by other permissions in the same rule.


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

The `allow-traverse` permission allows
an account to only see the folders during normal directory listings.

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

Both the source and destination paths must allow renaming.
Each path must grant `allow-rename` or `allow-full-control`.


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
