OS-level Authentication Method
==============================

An `os` authentication method can be used to authenticate users
based on the authentication methods provided by the operating system.

It can also be used to authenticate administrators for the Local Manager
service.
For this, you will need to explicitly define a group or a set of groups
in the `manager_allowed_groups` configuration options.
By default, no administrators are allowed.

..  warning::
    On Unix-like systems, this authentication method can only be used
    when the SFTPPlus service is started as `root`.

You can overwrite some of the account's settings (e.g. home folder path), by
defining an account of type `os` inside the configuration file.

The `os` authentication method will authenticate the following account types:

* Windows Local Accounts on Windows systems.
* Windows Active Directory Accounts, when SFTPPlus runs on a Windows system
  which is part of a domain.
* Linux accounts with passwords defined in the ``/etc/passwd`` file or
  by the Name Service Switch library.
* Linux accounts with passwords defined in the ``/etc/shadow`` file.

On systems supporting PAM, PAM can also be used for authenticating users
with username and password credentials.

On many Unix-like systems, PAM is used for enabling various authentication
methods, such as LDAP, PKCS#11 smart cards, or fingerprint authentication.

When the PAM authentication request returns *PAM_SUCCESS*, the account is
authorized.
Any response other than *PAM_SUCCESS* will reject the account.

PAM only handles authentication.
The account configuration is retrieved using the same generic OS API.

..  note::
    The SFTPPlus' `pam` authentication method will only use PAM for the
    `authentication` operation.
    PAM is not used for managing accounts, sessions, or passwords.
    Please get in touch with us if you need to integrate PAM accounts and
    session management with SFTPPlus.


pam_usage
---------

:Default value: `fallback`
:Optional: Yes
:Values: * `fallback`
         * `exclusive`
         * Empty
:From version: 3.3.0
:Description:
    Defines how to use PAM for for authenticating accounts using username and
    password credentials.

    The default mode is `fallback`.
    In this mode it will first try to authenticate accounts based on the
    ``/etc/passwd`` file.
    If the password is set in the operating system as one of the following
    `x`, `NP`, `*NP*` or `*`, it will continue to authenticate with PAM.

    In `exclusive` mode, it will exclusively use PAM for username and password
    authentications.

    Leave it empty to completely disable PAM usage.

    ..  note::
        On Windows, this option is always disabled as SFTPPlus has no support
        for PAM on this platform.


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


group_association
-----------------

:Default value: `DEFAULT_GROUP`
:Optional: No
:Values: * GROUP-UUID
         * `group-name`
         * `group-name-with-default`
:From version: 4.11.0
:Description:
    Defines the SFTPPlus group that is associated with authenticated users
    for which no explicit association is defined inside the SFTPPlus
    configuration.

    When set with the identifier (UUID) of a SFTPPlus group,
    it will associate any user with that SFTPPlus group.

    When set to `group-name`, it will associate the user with the
    SFTPPlus group having the same name as the operating system group of
    this user.
    If the user is a member of multiple groups,
    the first group defined in `allowed_groups` will be used.
    If no SFTPPlus group is found with the same name, the authentication fails.

    When set to `group-name-with-default`, it will try to associate the user
    with a SFTPPlus group having the same name as the OS group.
    It will use the default SFTPPlus group if no SFTPPlus group is found having
    the same name as the OS group.

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
    are allowed by this method to be used for the Local Manager service.

    When this is empty, any administrators are denied.

    ..  note::
        This configuration takes operating system group names and not
        SFTPPlus group names.


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
