File system access
==================

..  contents:: :local:


Overview
--------

This page describes how SFTPPlus handles native file system access on both
Unix-like and Windows platforms for the server-side operations.
While running on a specific operating system, it provides the extra features
provided by that operating system.


File and Folder Names
---------------------

The characters allowed in the file names handled by SFTPPlus have no restrictions from SFTPPlus,
but the operating system under which SFTPPlus runs might impose certain restrictions on the file names.
For example, on Linux the colon (:) character is allowed in a file name, while Windows will reject it.

There is no limit on file name length imposed by SFTPPlus.
For compatibility, it is recommended to use file names with less than 255 characters.
This is a common limit imposed by the EXT4 filesystem on Linux or the NTFS filesystem on Windows.

The full path of a file or directory, the name of the file itself together with all its parents and directory separators,
can be longer than 255 characters.
For compatibility, it is recommended to keep the total path length below 32.767 characters.


Unix-like systems
^^^^^^^^^^^^^^^^^

Folder / file names that contain only space characters are fully supported on
Unix-like systems: Linux and macOS.
Names containing leading or trailing spaces are preserved as is.

Names can contain ASCII characters or Unicode names encoded using UTF-8,
with the exception for the forward-slash (/) or the null character.

..  note::
    If you require to handle names using a character encoding scheme other than `UTF-8`, please contact us.


Windows
^^^^^^^

On Windows, leading and trailing spaces from file names are stripped by the operating system.
Due to this, names with only space characters are converted into names with no characters, invalidating them.

ASCII and Unicode characters are supported.
The name of a file can't contain any of the following characters: `/ \ : * " ? < > |`
This is a limit defined by the Windows operating system.


File system permissions for application and operating system accounts
---------------------------------------------------------------------

When accounts are authenticated as operating systems accounts
(local, domain, or remote), they will observe the same file system permissions
as those defined in the local file system.
In other words, the file system access will be granted according to user
permissions for the local file system.
This way, you can have multiple accounts accessing the same file or folder,
each account having its own permissions.
The permissions that are set is completely dependent on each use case.
For example, you may only want to set read-only permission if you only want
users to have read-only permission.

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


Using Windows Network shared folders
------------------------------------

When running SFTPPlus on Windows, SFTPPlus can use the Windows
operating system functionalities to access CIFS/SMB network shared resources
(files or folder).
SFTPPlus does not directly support the CIFS (Microsoft Windows Network Shares)
protocol.
This is why SMB/CIFS support is not available on the Unix-like
operating systems: Linux and macOS.

The Microsoft Windows UNC
(short for Universal Naming Convention or Uniform Naming Convention) path
format is used to access a network share.
SFTPPlus supports the Microsoft Windows UNC paths.

For example, to configure the home folder for a user named ``johnd`` as the
``users\johnd`` folder of a ``ftp-files`` remote shared resource
hosted by the server ``srv01.example.com``,
you can set up the `home_folder_path` configuration as::

    [accounts/6602-4622-8dfa]
    name = johnd
    home_folder_path = \\srv01.example.com\ftp-files\users\johnd

Remote Windows Network shares are also available via symbolic links,
which will create an alias that can be accessed using a local path format.

For example, you can set up a home folder as ``c:\ftp-files\johnd`` which will
provide access for an user to local files as for any account,
but will also have a folder named ``sales-team`` for which the files are
stored as a remote shared resource named ``sales-ftp`` hosted on a
machine named ``srv01.example.com``.
The `mklink` command below need to be executed in an elevated command.::

    mklink /D c:\ftp-files\johnd\sales-team \\srv01.example.com\sales-ftp

Then configure the account as::

    [accounts/6602-4622-8dfa]
    name = johnd
    home_folder_path = c:\ftp-files\johnd

In the above configuration, an FTP file like ``/sales-team/report.csv`` will
be accessed from the the ``srv01.example.com`` server, while a path like
``/project-status.prj`` will be served from the
``c:\ftp-files\johnd\project-status.prj`` path.

When the SFTPPlus service is executed using a local account (and not an
AD account), the remote server should have an account with the same username
and the same password.
Otherwise, Windows will deny access to Windows Network Shares.
This is because the files on the network drive are accessed using the local
account and remote server has no method to authenticate it.

In order for SFTPPlus to access network resources, the service under which
SFTPPlus operates need to be associated with a dedicated service account.

This means that when the SFTPPlus MFT process tries to access a Windows Share,
the OS will ask for the real user to authenticate itself to that Window Share.

Using the default SYSTEM account will not work, as this is not a real account
and it will not have access to remote drivers.


Locked accounts
---------------

Lock access is specified by `lock_in_home_folder` in the account's settings.

In locked accounts, the account is locked inside the home folder path and
access to files and folders outside the home folder path will be denied.

Application accounts are always inside their home folder and will not have
access to files outside the home folder.

Operating System accounts have further configuration options:

* Deny access to files and folders outside the home folder.

* Inherit the account’s group configuration.


Locked to home folder
^^^^^^^^^^^^^^^^^^^^^

:Scenario:
    If an account is locked and the home folder is set to ``/home/user1/``, the
    user is locked inside the home folder.
    The home folder path is now the root folder visible to the client.
    When a client lists the folder contents of ‘/upload’, the request is mapped
    in accordance to the home folder.
    Therefore it is mapped to ``/home/user1/upload`` on the local file system.


Not locked to home folder
^^^^^^^^^^^^^^^^^^^^^^^^^

:Scenario:
    If an account is not locked inside the home folder, a request to list the
    relative file path ``/upload/`` folder will be mapped to the ``/upload``
    folder on the local file system.


Absolute and relative path handling in locked accounts
------------------------------------------------------

You can use absolute or relative file paths when specifying a home folder to
lock an account to.

Absolute and relative file paths when used in locked_in_home folder accounts
differ to the paths used inside the configuration file as mentioned
:ref:`in the section on absolute and relative paths <absolute-relative-paths>`.

To avoid potentially creating ambiguous behaviour in setting lock access, opt
to specify an absolute file path instead of a relative file path.


Locked to home folder - use of absolute file paths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Scenario:
    When a locked account specifies an absolute file path outside the home
    folder, they will not be able to access that folder.
    For example, an account with a home folder of ``/home/user1/`` and states
    an absolute file path to navigate to ``/home/user2/upload`` will be unable
    to access the folder.


Locked to home folder - use of relative file paths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Scenario:
    When a client navigates to a folder via relative file path, like
    ``/upload/``, they will be able to access that folder.


Not locked to home folder - use of absolute file paths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Scenario:
    When an account that is not locked to the home folder specifies an absolute
    file path to a destination outside that folder, it is able to access that
    folder.
    For example, if an account with a home folder of ``/home/user1`` navigates
    to a file path outside its home folder to ``/home/user2/upload`` it will
    be able to access that folder.
    This is also dependent on the account having privileges on the OS to access
    that particular folder.


Not locked to home folder - use of relative file paths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Scenario:
    Similar to the scenario of a locked home folder account, when a user
    navigates to a folder via relative file paths, they will also be able
    to access that folder.


Support for symbolic links and hard links
-----------------------------------------

A symbolic link is a special type of file pointing to the location of another
file, while a hard link is basically a reference or a label associated
to a file.
SFTPPlus supports both types of file links, but you should be aware
of the following constraints:

* A hard link can be used only for files and not directories
* A hard link can be used only for files on the same volume
* New hard links cannot be created from SFTPPlus on any protocol
* Symbolic links creation is supported only for the SFTP protocol, however,
  it works on all platforms.

If a hard link references a file outside the user home folder,
SFTPPlus will allow access to it.

SFTPPlus will not allow the creation of symbolic links outside the
home folder, preventing users from bypassing their home folder boundaries.

For symbolic links created outside of the STPPlus application
and which point to a file or folder outside
the user home folder,
SFTPPlus will follow the link.
In this way, you can explicitly configure an account to have access to
specific files and folders outside of its home folder.

Symbolic links are supported on Windows for local paths as target,
as well as remote Windows Shares using UNC paths as target.


.. _operation-home-folder-structure:

Home folder structure
---------------------

You can use the `home_folder_structure` configuration option to define a list of directories that are automatically created for any account associated to this group.

When an account is associated to multiple groups,
all directories defined in `home_folder_structure` configuration of each group are created.

The directories are created at login time, after a successful authentication.

The configured directories are configured relative to the `home_folder_path`.
You can't configure directories to be created outside of the `home_folder_path`.
Do not include the drive letter.
Do not use absolute paths.

The `home_folder_structure` directories should be defined using slash (/) delimiter,
even when the account is targeted for a Windows system.

Parent directories are automatically created.

Below is an example usage for `home_folder_structure`::

        [groups/92ad5b32-d8d7]
        name = inbox-group
        home_folder_structure =
          /inbox/invoices
          /inbox/orders

        [groups/39f6f072-19dc]
        name = outbox-group
        home_folder_structure =
          /outbox/
          /outbox/reports

        [accounts/a6cb0a1e-8af5-429d-a28c-b027bbb8b245]
        name = JohnD
        group = 92ad5b32-d8d7, 39f6f072-19dc
        home_folder_path = C:\file-server\users\JohnD

When user `JohnD` is authenticated, the following directories are
automatically created, in this order:

* ``C:\file-server\users\JohnD\inbox``
* ``C:\file-server\users\JohnD\inbox\invoices``
* ``C:\file-server\users\JohnD\inbox\orders``
* ``C:\file-server\users\JohnD\outbox``
* ``C:\file-server\users\JohnD\outbox\reports``


Virtual folders
---------------

Virtual folders are directories that can be accessed outside of the account's locked home folder,
but available as paths inside the user's home folder.

Virtual folders act as symbolic links.

As for real folders, permissions for virtual folders can be defined at the
account configuration level or inherited from group configuration.

Virtual folders and their parents in the path cannot be changed
through file transfer operations.
That is, an account cannot delete, rename,
set attributes, or change the root virtual folder, or its parent or
grandparents.
Even if SFTPPlus permissions allow for deleting a folder,
the operation of deleting the root virtual folder will fail.

Accounts can still modify or delete files and folders which are inside the
virtual folders, as per the current permissions set in SFTPPlus.

Virtual folders are mapped starting from the root folder.


Example virtual folder configuration and scenario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following is a scenario for a user, ``JohnD`` requiring access to
virtual folders.

The user, ``JohnD``, has ``C:\Users\JohnD`` as the home folder path,
and access to these folders::

    C:\Users\JohnD
    C:\Users\JohnD\download

In SFTPPlus, this user is associated with the following `group` and `account`
configuration.
Notice that `virtual_folders` are listed in the ``d32e-653a-98da`` group.
The account, ``JohnD``, is not only a part of this group but it is also
inheriting the group's configuration settings::

    [groups/d32e-653a-98da]
    name = Sales
    virtual_folders =
        /virtual-in-root, C:\Storage\base
        /read-only-reports, C:\Storage\reports
        /upload/team/emea, C:\Storage\teams\sales
    permissions = allow-full-control
        /read-only-reports/*, allow-list, allow-read

    [accounts/7521-bb32-6cce]
    name = JohnD
    group = d32e-653a-98da
    home_folder_path = C:\Users\JohnD
    permissions = inherit

When a file transfer session is commenced, the session will make available to
the user the following list of folder structure to file transfer clients::

    /                      -> C:\Users\JohnD
    /download              -> C:\Users\JohnD\download
    /upload                -> Virtual folder with 'team' as single member
    /upload/team           -> Virtual folder with 'sales' as single member
    /upload/team/emea      -> C:\Storage\teams\sales
    /upload/team/emea/jobs -> C:\Storage\teams\sales\jobs
    /virtual-in-root       -> C:\Storage\base
    /virtual-in-root/vid   -> C:\Storage\base\vid
    /read-only-reports     -> C:\Storage\reports
    /read-only-reports/us  -> C:\Storage\reports\us

In addition, the following permissions are also applied to these folders::

    /                      -> Full control
    /download              -> Full control, including ability to remove the
                              folder.
    /upload                -> Only list, since this is a virtual folder.
    /upload/team           -> Only list, since this is a virtual folder.
    /upload/team/sales     -> Full control, but cannot delete the folder since
                              it is a virtual folder.
    /upload/team/emea/jobs -> Full control, but cannot delete the folder
                              itself.
    /virtual-in-root       -> Full control, but cannot delete the folder
                              itself.
    /virtual-in-root/vid   -> Full control, can also delete the `vid` folder.
    /read-only-reports     -> Only allow reading files and listing folders.
    /read-only-reports/us  -> Only allow reading files and listing folders.


With the configurations above, the file transfer administrator can be assured
that ``JohnD`` has access to the appropriate virtual folders with the right
access controls.

..  note::

    On Linux, virtual folders are case-sensitive.
    On Windows and macOS, virtual folders are case-insensitive and are always
    represented in lowercase.


..  note::

    You cannot have a virtual folder sharing the same name as a real folder
    or file that already exists at the same path that is represented by the
    virtual folder.


Virtual folders from multiple groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an account is a member of multiple groups,
it gets access to all the virtual folders defined for the associated groups.

For example, based on the configuration from below, user JohnD will have
access to both `/sales-emea` and `/sales-uk` virtual folders::

    [groups/d32e-653a-98da]
    name = Sales EMEA
    enabled = yes
    virtual_folders =
        /sales-emea, C:\Storage\sales\EMEA

    [groups/2a2e-823a-76de]
    name = Sales UK
    enabled = yes
    virtual_folders =
        /sales-uk, C:\Storage\sales\UK

    [accounts/7521-bb32-6cce]
    name = JohnD
    group = d32e-653a-98da, 2a2e-823a-76de
    home_folder_path = C:\Users\JohnD
    permissions = inherit


Virtual folders with dynamic username-based paths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When configuring the virtual folders of a group, you can define some using the name of the authenticated user.
The username placeholder can be used for both virtual paths and real paths.

With the below example, user ``JohnD`` will see the following files:

* / (root) -> D:/file-server/uk-office
* /JohnD ->  D:/users/JohnD
* /support-JohnD ->  D:/file-server/JohnD-support-queue
* /infrastructure - D:/file-server/infrastructure

Note that the `${USER}` placeholder can be inserted in any part of the path.
Here is the configuration::

    [groups/2a2e-823a-76de]
    name = UK Office
    enabled = yes
    home_folder_path = ${SHARED}D:\file-server\uk-office
    virtual_folders =
        /${USER}, D:\users\${USER}
        /support-${USER}, D:\file-server\${USER}-support-queue
        /infrastructure, D:\file-server\infrastructure

    [accounts/7521-bb32-6cce]
    name = JohnD
    group = 2a2e-823a-76de
    home_folder_path = inherit
    permissions = inherit


Virtual folders and authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During the authentication process, SFTPPlus will check that no real path
exists with the same name as one of the configured virtual paths.
If these paths are found, the authentication fails and the connection is
rejected.

For example, if there is a user with ``C:\Users\JohnD`` as the home folder
path and the following folders::

    C:\Users\JohnD
    C:\Users\JohnD\upload

And they have the following virtual folder configured::

    virtual_folders = /upload/team/sales, C:\Storage\teams\sales

The user will fail to authenticate since the real path
``C:\Users\JohnD\upload`` is accessible inside the user's home folder as
``/upload``.
When this occurs, a conflict is detected with the virtual path
``/upload/team/sales`` and the authentication will fail.

Administrators can mitigate this issue by ensuring that no real path
exists with the same name as one of the configured virtual paths.
