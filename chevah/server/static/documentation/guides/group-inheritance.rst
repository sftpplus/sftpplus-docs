.. container:: tags pull-left

    `server-side`
    `security`
    `since-version:3.28.0`


Group inheritance for permissions
=================================

..  contents:: :local:


We created this short guide as the starting resource for those interested
in using SFTPPlus groups to allocate account permissions.

Permissions can be set on the operating system level (for example, via changing
the Windows file and folder permissions setting) but they can also be set on
the application level via the SFTPPlus groups configuration.
Please note that the OS permissions is overrides the application-level
permissions set in SFTPPlus.

Let's say you need better control to allocate permissions based on groups of
users.

To give you an example of how the group `permissions` configuration option
work, ``bob``, ``charlie`` and ``alice`` are three accounts with permissions
set to upload FTP files.
They belong in a group called ``Education_Group_A``::

    [groups/b904e6a6-d29f-4ccf-8abd-edcae4d3324f]
    name = Education_Group_A
    enabled = Yes
    permissions = read

We set the ``Education_Group_A`` group to only have `allow-read` permissions,
meaning that the accounts in this group can only upload files,
download existing files or obtain the attributes of files.

If one of the users, ``alice``, requires additional permissions to create a
folder while maintaining the permissions for ``bob`` and ``charlie``, the user
``alice`` will need to be allocated into another group that has
`allow-full-control` permission.

You cannot change the settings for ``Education_Group_A``, in order to fix the
``alice`` account since the changes will also affect the other users in that
group, in this case ``bob`` and ``charlie``.

For example, even when account is configured with
:ref:`full-control permissions<configuration-groups-permissions>` in SFTPPlus,
if the OS does not permit the account to read, write, delete and create files
or folders, it will still fail with a permission error.


Managing user-level permissions and group inheritance
-----------------------------------------------------

Administrators can set user-level permissions that will override a group
permissions.

Let's say ``alice`` can only have read permissions::

    [accounts/4b535c97-c15a-4632-8b29-9aca6cff5ce8]
    name = alice
    type = application
    group = b904e6a6-d29f-4ccf-8abd-edcae4d3324f
    permission = allow-read

The ``charlie`` account can only have write permissions::

    [accounts/dc90e2c7-1149-4b8b-9e7e-91f96c4c607a]
    name = charlie
    type = application
    group = b904e6a6-d29f-4ccf-8abd-edcae4d3324f
    permission = allow-write

And the rest of the users (in this case, one of them is ``bob``) in the
``Education_Group_A`` group need `allow-full-control` permissions::

    [accounts/30548ad7-0090-4c44-82d2-cfcc1c4b7351]
    name = bob
    type = application
    group = b904e6a6-d29f-4ccf-8abd-edcae4d3324f
    permission = Inherit

    [groups/b904e6a6-d29f-4ccf-8abd-edcae4d3324f]
    name = Education_Group_A
    enabled = Yes
    permissions = allow-full-control

On the user configuration sections for ``alice`` and ``charlie`` you can set
their own permissions, while ``bob`` will inherit permissions set by
``Education_Group_A``.
Once set, SFTPPlus will respect the user-level permissions set for ``alice``
and ``charlie`` even though the ``Education_Group_A`` group has ``full-control``
permission.


More information
----------------

You can read more about the configuration options in the
:ref:`group configurations page<configuration-groups-permissions>`.

You can use SFTPPlus to implement AAA (Authentication, Authorization and
Accounting) systems in order to track user activities
and to control their access to resources on the network.

This guide focused on the Authorization component.
For information on covering the Authentication process,
check :doc:`the authentication section</operation/authentication>`,
and for the Accounting process, see
:doc:`the account documentation</guides/event-handlers>`.
