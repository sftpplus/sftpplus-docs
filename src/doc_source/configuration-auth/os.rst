Operating system / Domain users
===============================

..  contents:: :local:


Introduction
------------

The `os` authentication method can be used to grant access to SFTPPlus services
for local users of the operating system that is running SFTPPlus.

To prevent accidentally allowing SFTPPlus access to local users,
the default SFTPPlus configuration rejects OS users.
You need to explicitly configure the `allowed_groups` option to include
the names of the OS groups for which you want to allow access to SFTPPlus services.

The `os` authentication can also be used to authenticate administrators for the Web Manager service.
For this, you need to explicitly define a group or a set of groups
in the `manager_allowed_groups` configuration option.

..  warning::
    On Linux systems, this authentication method can only be used
    when the SFTPPlus service is started as `root`.
    This restriction is enforced by the default Linux security model.

You can overwrite some of the account's settings (e.g. home folder path), by
defining an account of type `os` inside the configuration file.

The `os` authentication method will authenticate the following account types:

* Windows Local Accounts on Windows systems.
* Windows Active Directory Accounts, when SFTPPlus runs on a Windows system
  which is part of a domain.
* Linux accounts with passwords defined in the ``/etc/passwd`` file or
  by the Name Service Switch library.
* Linux accounts with passwords defined in the ``/etc/shadow`` file.

There are three types of accounts for operating system users:

* `os` - OS accounts for which file transfers are performed as the OS user.
* `os user` - OS accounts for which file transfers are performed as the SFTPPlus service account.
* `os with config` - OS accounts also configured through SFTPPlus, for which file transfers are performed as the OS user. Their passwords are still managed by the operating system.


Linux PAM
---------

On systems supporting PAM, PAM can also be used for authenticating users
with username and password credentials.

On many Linux systems, PAM is used for enabling various authentication methods
such as LDAP, System Security Services Daemon (SSSD), and PKCS#11 smart cards.

When the PAM authentication request returns *PAM_SUCCESS*, the account is authorized.
Any response other than *PAM_SUCCESS* results in the local account being rejected.

PAM only handles authentication.
The account configuration is retrieved using the same generic OS API.

..  note::
    The SFTPPlus' `pam` authentication method will only use PAM for the
    `authentication` operation.
    PAM is not used for managing accounts, sessions, or passwords.
    Please get in touch with us if you need to integrate PAM accounts and
    session management with SFTPPlus.

.. include:: /configuration-auth/authentication-commons.include.rst


Windows Security Policy settings
--------------------------------

SFTPPlus can be configured to authenticate Windows accounts, both local ones and domain accounts.
In addition, the SFTPPlus Windows Service can be configured to run as a dedicated service account.
If both conditions apply, the dedicated service account requires the following `user rights assignments`:

* `Back up files and directories <https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/back-up-files-and-directories>`_
* `Restore files and directories <https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/restore-files-and-directories>`_
* `Take ownership of files or other objects <https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/take-ownership-of-files-or-other-objects>`_

These permissions are required to allow SFTPPlus to:

* Discover the path to the default user home folder
* Create the default user home folder
* Set the user home folder as owned by the user itself.


access_filesystem_as_service_user
---------------------------------

:Default value: `No`
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 5.12.0
:Description:
    When set to `Yes`, authenticated OS local accounts
    use the SFTPPlus service account for filesystem access.
    After the users are authenticated, they are handled inside SFTPPlus as application accounts
    with access to OS resources configured at the OS level for the local user running SFTPPlus.

    This simplifies filesystem configuration at the operating system level.
    System administrators only need to setup the file hierarchy with permissions for the SFTPPlus service account.
    Then, the SFTPPlus web-based manager is used to define the actual access for each authenticated user.

    When this is set to `No`, the actual file access for each user is defined using
    SFTPPlus' Web Manager within the constraints of the low-level OS filesystem permissions.


pam_usage
---------

:Default value: `fallback`
:Optional: Yes
:Values: * `fallback`
         * `exclusive`
         * `service` (Since 5.12.0)
         * Empty
:From version: 3.3.0
:Description:
    Defines how to use PAM for for authenticating accounts using username and
    password credentials.

    The default mode is `fallback`.
    In this mode it first tries to authenticate accounts based on the
    ``/etc/passwd`` file.
    If the password is set in the operating system as one of the following
    `x`, `NP`, `*NP*` or `*`, it will continue to authenticate with PAM.

    In `exclusive` mode, the PAM authentication operations are executed under
    the root account.
    Only PAM is used for username and password authentications.

    In `service` mode, the PAM authentication operation are executed under
    the regular SFTPPlus service account.
    Only PAM is used for username and password authentications.
    The `service` mode might not be available on most Linux systems
    because PAM is usually configured to require `root` privileges.
    You can only use the `service` mode effectively
    if your Linux system is configured to allow PAM access for non-root accounts.

    Leave it empty to completely disable PAM usage.

    ..  note::
        On Windows, this option is always disabled
        because PAM is not available on Windows.


pam_service
-----------

:Default value: `login`
:Optional: Yes
:Values: * Name of a PAM service.
:From version: 3.3.0
:Description:
    Name of the PAM service used for account authentication requests.


allowed_groups
--------------

:Default value: Empty
:Optional: No
:Values: * Empty
         * OS group name
         * `${ALL_OS_GROUPS}`
         * Comma-separated list of OS group names.
:From version: 3.35.0
:Description:
    Defines an operating system group or a list of OS groups with users that
    are allowed by this authentication method.

    When this is empty, no OS account is accepted.
    You need to define a list of group names for which to allow access.
    For example, if you need to allow all users from the local system, you can
    typically use the default `users` group available on both Windows and Linux.

    If you absolutely need to allow access to all OS users from all OS groups,
    set this to `${ALL_OS_GROUPS}`.
    This should be the only value, and you can't mix `${ALL_OS_GROUPS}` with
    other group names.

    ..  note::
        This configuration takes operating system group names and not
        SFTPPlus group names.


base_groups
-----------

:Default value: Empty
:Optional: yes
:Values: * Empty
         * Group UUID.
         * Comma separated list of group UUIDs.
:From version: 4.23.0
:Description:
    Defines the SFTPPlus groups that are associated with any authenticated user.

    Leave empty to not have any default group and only use the groups associated via OS configuration.

    The first configured base group is also the primary group.


group_association
-----------------

:Default value: `base-groups`
:Optional: No
:Values: * `base-groups` (since 4.23.0)
         * `base-and-os-groups` (since 4.23.0)
         * `group-name`
         * `group-name-with-default`
:From version: 4.11.0
:Description:
    Defines how the SFTPPlus groups are associated with authenticated users
    for which no explicit association is defined inside the SFTPPlus
    configuration.

    When set to `base-groups` it will associate an OS user to the list of groups defined by the `base_groups` option.

    When set to `base-and-os-groups` it will associate an OS user to the list of groups defined by the `base_groups` option and any other group that has the same name as one of the groups defined by the `allowed_groups` option.

    When set to `group-name`, it will associate the user with the SFTPPlus group having the same name as the operating system group of this user.
    If the user is a member of multiple OS groups,
    the first group defined in `allowed_groups` will be used.
    If no SFTPPlus group is found with the same name, the authentication fails.

    When set to `group-name-with-default`, it will try to associate the user with an SFTPPlus group having the same name as the first OS group.
    It will use the default SFTPPlus group if no SFTPPlus group is found to have the same name as the OS group.

    ..  note::
        When an OS account is explicitly defined inside SFTPPlus configuration
        the `group_association` is ignored and the account's groups
        configuration is used instead.


manager_allowed_groups
----------------------

:Default value: Empty
:Optional: Yes
:Values: * Empty
         * OS group name
         * Comma-separated list of OS group names.
:From version: 3.37.0
:Description:
    Defines an operating system group or a list of OS groups with users that
    are allowed by this method to be used for the Web Manager service.

    When this is empty, any administrators are denied.

    ..  note::
        This configuration takes operating system group names and not
        SFTPPlus group names.


base_roles
----------

:Default value: Empty
:Optional: yes
:Values: * Empty
         * Role UUID.
         * Comma-separated list of role UUIDs.
:From version: 4.27.0
:Description:
    Defines the SFTPPlus roles that are associated with any authenticated administrator.

    Leave empty to not have any default role and only use the roles associated via OS configuration.

    The first configured role is also the primary role.


role_association
----------------

:Default value: `base-roles`
:Optional: No
:Values: * `base-roles`
         * `base-and-os-groups`
:From version: 4.11.0
:Description:
    Defines how the SFTPPlus roles are associated with authenticated administrators.

    When set to `base-roles` it will associate the administrator to the list of roles defined by the `base_roles` option.

    When set to `base-and-os-groups` it will associate an administrator to the list of roles defined by the `base_roles` option and any other role that has the same name as one of the groups defined by the `manager_allowed_groups` option.


Windows Domain Accounts
-----------------------

When SFTPPlus is installed on a machine belonging to a Domain
Controller, it can be configured to allow accounts from a Domain Controller to
access the files located on the server.
These accounts are authenticated using the `os` authentication method.

For Domain Controller accounts, there is the option for the username to be
provided in the user principal name (UPN) format::

    USERNAME@EXAMPLE.COM

To specify the domain, you should use UPN format, not the legacy NebBIOS names.

..  note::
    Active Directory accounts are only available when SFTPPlus is
    running on a Windows operating system.
    If you want to allow Active Directory accounts to access an SFTPPlus
    instance running on Unix-like systems, please contact our support team.
