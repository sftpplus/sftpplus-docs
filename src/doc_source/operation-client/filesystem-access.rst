File system access
==================

..  contents:: :local:


Overview
--------

This page describes how SFTPPlus handles native file system access on both
Unix-like and Windows platforms for the client-side operations.


File system permissions
^^^^^^^^^^^^^^^^^^^^^^^

For accounts authenticated as server application accounts, all accounts
are mapped to the same OS account and they will have the same permissions.

For application accounts, all file system activity will be executed under the
account specified by the `[server]` account configuration option.
Application accounts are locked into their home directories.

The client would need close to full control with permissions.

Windows administrators can further allocate advanced permission settings.
In this case, they can also choose to exclude the following
permissions - `Read Permissions`, `Change Permissions`, `Take Ownership`, and
`Write Extended Attributes`.

Files on Windows having the `read-only` attribute set are removed, renamed,
moved, and copied without getting an access denied error.

..  warning::
    `Read-only` files cannot be modified, but they can be copied, moved,
    renamed, or deleted.
    It is possible that moving, renaming, or deleting a read-only file can
    cause a program that relies on that file to stop working properly.
