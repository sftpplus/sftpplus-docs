Accounts
========

..  contents:: :local:


Introduction
------------

SFTPPlus can be configured to allow both `application` and
`operating system` accounts supplied by third party identity providers.

The account's configuration, as defined at login time,
is used during the entire file transfer session.
Users need to re-authenticate to use an updated configuration.

SFTPPlus specific / application / virtual accounts are defined inside the
main configuration file.

Accounts for which the authentication is provided by the operating system can
also be defined inside the main configure file to augment or overwrite
the account configuration provided by the operating system.
For example, you can authenticate an account using the operating system, but
once authenticated use a different home folder, other than the one provided by
the operating system.

Each account has a dedicated folder, called the `home folder`, which can be
accessed using one of the available file transfer protocols.

..  warning::
    For security reasons, by default, SFTPPlus will restrict
    access of each user to only the files and folders located inside the home
    folder.

..  note::
    Account names and passwords longer than 150 characters
    are not allowed by SFTPPlus.
    Generating passwords longer than 128 characters is not possible either.
    These restrictions prevent denial of service attacks.


Configuring administrators
--------------------------

Administrators are only dedicated to accessing the Local Manager.
For documentation around configuring administrators, please go to
:doc:`the Administrators section</configuration/administrators>`.


Adding a new account via Local Manager
--------------------------------------

Accounts can be added or changed via Local Manager.
Options will differ depending on which account type is used.

..  image:: /_static/gallery/gallery-add-account.png


Adding a new account via text configuration
-------------------------------------------

Accounts can be added or changed by editing the configuration file.

Configurations for each account are grouped inside an account section.
A section name is prefixed by an ``accounts/`` text followed by the account's
universally unique identifier (UUID), all surrounded by square
brackets.

The account's UUID can be any unique string used to identify the account.
Once defined, the UUID should not be changed.

For more information about UUIDs, please see
:doc:`the dedicated UUID documentation </configuration/general>`.

The following example defines two accounts, one called ``john``, which
is an application type account, and another named ``anna``, which is an account
authenticated by the operating system::

    [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
    name = john
    type = application
    group = 9e3c5562-9b86-43da-a984-1d8751f2f060
    enabled = Yes
    password = $5$H9V1qKBj/2Xx7tTT$xEvdSQWQ94G3okDS2XCnJ580I2W7X
    home_folder_path = /path/to/john
    permissions: read

    [accounts/745fff10-4370-4d75-a172-21819046c76f]
    name = anna
    type = os
    group = 01d2e30b-05f7-40c3-a86d-58744995970d
    enabled = Yes
    home_folder_path = /path/to/anna/files
    permissions: inherit

Each configuration option available for an account or a group is explained
in the following sections.


New accounts
------------

Adding a new account is done by creating a new section inside the
configuration file.

For example, to add a new account named ``mark``::

    [accounts/514e5b73-e9a4-46ce-a9c0-96c3d7eabf3b]
    name = mark
    enabled = Yes
    type = application
    group = fb40336d-8e5b-4275-950e-5f76fc387281
    description = DESCRIPTION_OR_MORE_DETAILS
    home_folder_path = /PATH/TO/USER/HOME
    password = $5$H9V1qKBj/2Xx7tTT$xEvdSQWQ94G3okDS2XCnJ580I2W7X
    permissions: read, write


Application accounts configuration
----------------------------------

Application accounts are special accounts only available inside the SFTPPlus
application.

All application accounts will be mapped inside the operating system to
the operating system account configured using the ``server`` account
configuration option.

If no group is defined for an application account, it will be attached to
the `DEFAULT_GROUP` group.

..  note::
    It is highly recommended to define an explicit group
    (other than the `DEFAULT_GROUP`) for each application account.
    This will make the configuration file much easier to understand by removing
    any implicit behaviour associated with an unspecified group.


Operating system accounts configuration
---------------------------------------

SFTPPlus allows operating system accounts to access their files
once they are authenticated by providing a set of valid credentials.

The OS accounts are mapped to the authenticated OS user.
The low level file access rights will be enforced by the operating
system permissions based on the OS user and not the SFTPPlus service user.

When an operating system account creates new files or folders, the ownership
for those files or folders will be set to that account.

..  note::
    On Windows, if an account is a member of the Administrators group, the
    owner will be set to the `Administrators` Group.

For operating system accounts, SFTPPlus will validate the user's
credentials against the operating system authentication mechanism.

An operating system account can be configured to use the same home
folder as the one provided by the operating system.
Or it can be configured to use a custom home folder, specific for file transfer
operations.

The server allows the authentication of operating system accounts not defined
in the configuration file.
These accounts are associated with the `DEFAULT_GROUP` group, and the
group's properties are applied.

For Domain Controller accounts, the username must be provided in the
user principal name (UPN) format: `USERNAME@EXAMPLE.COM`


Configuration options available to all account types
----------------------------------------------------

Most of the configuration options available for an account are optional.
When a configuration option is not explicitly defined inside an account
section, the default value for that option will be applied.

Some of the configuration options can also take the `Inherit` value.
In this case, the value for this option will be defined based on the group
configuration.
More information about available group options can be found in the
:doc:`Groups configuration <groups>` documentation.

Here are some examples::

    [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
    name = john
    enabled = yes
    type = application
    group = ccac2941-261d-4797-af5f-b4fd1453bf59
    password = $5$H9V1qKBj/2Xx7tTT$xEvdSQWQ94G3okDS2XCnJ580I2W7X
    home_folder_path = c:\Users\John\transfer_files
    create_home_folder = yes
    ssh_authorized_keys_path = c:\Users\John\authorized_keys

    [accounts/514e5b73-e9a4-46ce-a9c0-96c3d7eabf3b]
    name = mark
    enabled = yes
    type = os
    group = 0a3f3aa7-50d2-44ef-9456-4f0beb69cf7d
    home_folder_path = /home/mark/transfer_files
    create_home_folder = Inherit
    ssh_authorized_keys_path = /home/mark/.ssh/authorized_keys

    [accounts/459245-7ea4-49ce-e4c0-98d3d7eabf3b]
    name = mike
    enabled = yes
    type = application
    group = ccac2941-261d-4797-af5f-b4fd1453bf59
    home_folder_path = /home/mike/
    ssh_authorized_keys_content = ssh-rsa AAAAB3NzaC1yc2EAAAADAQAB mike@comment


name
^^^^

:Default value: ''
:Optional: No
:From version: 2.0.0
:Values: * Any text.
:Description:
    Human-readable short string used to identify this account.

    It is used as the login name in the authentication process.


enabled
^^^^^^^

:Default value: `Yes`
:Optional: Yes
:From version: 1.6
:Values: * `Yes`
         * `No`
:Description:
    This option specifies whether or not this account is enabled.

    This option is overwritten by the group configuration option.
    If the group associated with this account is disabled, the account is also
    disabled, no matter what value is defined in the account's configuration
    option.
    If a role has been disabled, the administrator associated with that
    role will still be enabled.
    However, it will show an authentication failed message when a login attempt
    is made.


type
^^^^

:Default value: `application`
:Optional: Yes
:From version: 1.6
:Values: * `application`
         * `os`
:Description:
    This option specifies the type of the account.

    * Accounts of type `application` are defined entirely by the server
    * Accounts of type `os` are defined in the operating system, but
      some more attributes can be added when used in SFTPPlus.


group
^^^^^

:Default value: `DEFAULT_GROUP`
:Optional: No
:From version: 1.8.2
:Values: * UUID of the group associated with this account.
:Description:
    This option specifies the group to which this account is associated.

    The value is the group's UUID and not the group's name.
    This allows renaming the group without having to update the configuration
    for all the accounts associated with the group.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 1.7
:Values: * Any character string.
:Description:
    This is a human-readable text that describes the entity
    using this account or the purpose of the account.

    Example::

        [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
        name = john
        description = Incoming files from John Doe as part of ACME Inc.


email
^^^^^

:Default value: ''
:Optional: Yes
:Available since: 3.43.0
:Values: * Email address.
:Description:
    Email address associated with this account.


created
^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 4.12.0
:Values: * ISO 8601 date
         * ISO 8601 combined date and time
         * ISO 8601 combined date, time, and timezone
:Description:
    This records the date and time when this account was created.

    Date and time are defined in ISO 8601 format for combined date and time.
    Beside the standard format ``YYYY-MM-DD HH:MM:SSZ`` in UTC, it supports
    a few relaxed formats like:

    * YYYY-MM-DD
    * YYYY-MM-DD HH:MM:SS
    * YYYY-MM-DD HH:MM:SS+hh
    * YYYY-MM-DD HH:MM:SS+hh:mm

    When no timezone is defined, it will use the local timezone.

    When no time is defined, it will assume the time as 00:00:00 (midnight).

    When a date is defined, it needs to have the full year, month and day.


home_folder_path
^^^^^^^^^^^^^^^^

:Default value: `Inherit`
:Optional: Yes
:From version: 1.6
:Values: * A path to a folder located in the operating system's file system.
         * `${OS_HOME}` - to use the home folder path provided by the
           operating system.
         * `Inherit` - to get the value from the associated group.

:Description:
    This option specifies the base path to the account's home folder.
    The home folder is used as the initial folder for new connections.

    When defined, it should be defined as an absolute path.

    When this option is set to `Inherit`, the value defined for the
    account’s group will apply.
    For a better understanding, please follow the :ref:`explanations
    and examples on proprieties inheritance <inherited-home-folder-path>`.

    ..  note::
        On Linux and macOS systems, the home folder path is case-sensitive,
        to match the file system provided by the operating system.

    ..  note::
        For domain accounts, the server cannot automatically create missing
        Windows home folders, also known as *user profiles*.
        Because of this, you cannot use `${OS_HOME}` placeholder
        when configuring the `home_folder_path` for a domain account.

        For domain accounts, a regular folder can be set as
        `home_folder_path`.
        The folder can be automatically created, just as for regular accounts.


virtual_folders
^^^^^^^^^^^^^^^

:Default value: `inherit`
:Optional: Yes
:From version: 4.5.0
:Values: * Comma-separated values of virtual path to real path mappings.
         * List of virtual path rules, one mapping per line.
         * `inherit`
         * Empty.
:Description:
    By defining one or more virtual folders, you can allow access to
    selected files which are located outside an account's locked home
    folder.

    This is a comma-separated list of values containing two elements -
    the virtual path and the real path.

    For more details and examples on how to configure virtual folders,
    see the
    :doc:`filesystem access documentation</operation/filesystem-access>`.

    Leave it empty to not have any virtual folders.

    Set it to `inherit` to use the virtual folders from the group.


required_credentials
^^^^^^^^^^^^^^^^^^^^

:Default value: `inherit`
:Optional: Yes
:From version: 4.10.0
:Values: * `password`
         * `ssh-key`
         * `password, ssh-key`
         * `any`
         * `Inherit`
:Description:
    This defines the set of valid credentials required for authenticating this
    account.

    Set it to `password` to authenticate the account once it provides a valid
    password.

    Set it to `ssh-key` to authenticate the account once it provides a valid
    SSH key.
    The provided key is checked against all SSH keys from the configured list.

    Set it to `password, ssh-key` to authenticate the account only if
    it provides both a valid password AND a valid SSH key.

    Set it to `any` to authenticate the account once it provides
    any type of credentials, e.g. a valid password OR a valid SSH key.

    When this option is empty or set to `Inherit`,
    the value defined for the account's group applies.


ssh_authorized_keys_path
^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 1.7.0
:Values: * Path to a file on the local filesystem.
         * Path to a directory on the local filesystem.
         * Empty
         * `Inherit`
:Description:
    This option specifies whether or not the server will permit
    access using a list of public SSH keys retrieved from the specified file
    or from any file found inside the specified directory path.

    When configured as a single file,
    it can contain multiple public SSH keys in OpenSSH format,
    each key on a separate line.

    When configured as a path to a folder,
    it will read all files found in that folder, and try to load
    SSH public keys from each of them.
    The public keys can be stored in any standard format
    (OpenSSH, Tectia SSH, PuTTY, etc).

    The files should be readable by the account under which the SFTPPlus
    process operates.

    Failure occurs if private keys are found in the configured path.

    More details about SSH key authentication can be found
    :ref:`in the dedicated section <ssh-key-authentication>`.

    To disable reading SSH public keys from local files let it empty.

    This feature is not available in Windows for local or domain accounts.
    Use application accounts for implementing SSH key-based authentication on
    Windows.

    When this option is set to `Inherit`, the value defined for the account's
    group will apply.
    For a better understanding, please follow the :ref:`explanations
    and examples on proprieties inheritance <inherited-home-folder-path>`.


ssh_authorized_keys_content
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 2.9.0
:Values: * SSH public key line in OpenSSH public key format.
         * X.509 SSL/TLS certificate.
         * Empty
:Description:
    This option specifies the list of valid SSH public keys for this account.

    The public SSH key can also be extracted from an X.509 certificate.
    When that is the case, only a single key per X.509 certificate is supported.

    To disable reading SSH public keys through this configuration option,
    leave it empty.

    You can configure multiple public keys in the following way::

        [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
        ssh_authorized_keys_content =
            ssh-rsa KEY_CONTENT_1 user1@comment
            ssh-dsa KEY_CONTENT_2 user2@comment

    ..  warning::
        Public keys must be configured, one key per line and in OpenSSH format.


source_ip_filter
^^^^^^^^^^^^^^^^

:Default value: `Inherit`
:Optional: Yes
:From version: 3.45.0
:Values: * IPv4 address
         * IPv6 address
         * Classless Inter-Domain Routing subnet notation.
         * Comma-separated list of IPv4, IPv6 addresses, or CIDR values.
         * `Inherit`
         * Empty

:Description:
    This option defines the source IP addresses (v4 or v6) from which
    file transfer clients are allowed to authenticate.

    You can configure a single source IP for which to allow authentication
    for this account.

    To allow authentication from multiple source IPs, define them as a
    comma-separated list or a range of IP addresses from the same subnet
    using the Classless Inter-Domain Routing (CIDR) notation.

    Set it to `Inherit` to use the configuration defined for the group
    associated with this account.

    Leave it empty to allow this account to be authenticated from any source
    IP address.

    ..  note::
        Host names or FQDN are not supported.
        Only IP addresses are supported.


allow_certificate_authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `Yes`
:Optional: Yes
:From version: 1.8.1
:Values: * `Yes`
         * `No`
         * `Inherit`
:Description:
    Allow this account to authenticate using SSL certificates.

    Certificates need to be issued using the same Common Name field (CN) as
    the account name.

    If SSL certificate-based authentication is not enabled, accounts will have
    to use other means of authentication.

    When this option is set to `Inherit`, the value defined for the account's
    group will apply.


as2_require_http_authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Inherit
:Optional: Yes
:From version: 4.9.0
:Values: * Yes
         * No
         * Inherit
:Description:
    This defines whether the AS2 partner is required to perform
    HTTP authentication together with the incoming AS2 message request.

    Set it to `No` to allow receiving AS2 from non-authenticated HTTP
    connections.
    SFTPPlus will still validated the signature and encryption of the
    received AS2 message.

    For increased security, we recommend setting this to `Yes`.


as2_certificates
^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 4.5.0
:Values: * Single public X.509 SSL certificate in PEM format
         * Multiple concatenated certificates in PEM format
         * Empty
:Description:
    This option specifies one or more certificates used to validate
    signatures for received files.

    The certificates should be defined in PEM format.

    Most of the time, this will be configured with a single certificate.

    Multiple certificates are usually configured when an existing certificate
    is about to expire and there is a transition period in which both
    the existing certificate and a new certificate might be used.

    For asynchronous MDNs requests, the configured certificates are used
    to validate and authenticate the remote MDN receiver server.


as2_async_mdn_ca
^^^^^^^^^^^^^^^^

:Default value: `Disabled`
:Optional: Yes
:From version: 4.9.0
:Values: * Absolute path on the local file.
         * Content of the CA chain in PEM.
         * Empty value.
         * `Disabled`
:Description:
    This is used to configure the certificate authority or the list of
    certificates authorities for validating the remote HTTPS server
    during an asynchronous MDN response.

    You can define the list of all root CA and intermediate CA in PEM format.

    It can be configured as an absolute path to a file containing all the
    CA certificates in PEM format.

    When this configuration is left empty, the async MDN are rejected.

    Set as `Disabled` to disable validating the remote peer's certificates.

    It support the same options as the
    `ssl_certificate_authority` configuration.


permissions
^^^^^^^^^^^

:Default value: `inherit`
:Optional: Yes
:From version: 3.28.0
:Values: * Comma separated list of permissions
         * `Inherit`
:Description:
    This allows access rights to be defined in the file management
    operations permitted for this account.

    When this option is set to `Inherit`, the value defined for the account's
    group will apply.
    Any other value directly configured is ignored.

    For more details see
    :ref:`the permission <configuration-groups-permissions>` documentation
    described for the group.


expire_datetime
^^^^^^^^^^^^^^^

:Default value: `None`
:Optional: Yes
:From version: 3.27.0
:Values: * ISO 8601 date
         * ISO 8601 combined date and time
         * ISO 8601 combined date, time, and timezone
:Description:
    This defines the date and time after which the account will no longer be
    authorized.

    By default, this is an empty value which will cause the account to never
    expire.

    Date and time are defined in ISO 8601 format for combined date and time.
    Beside the standard format ``YYYY-MM-DD HH:MM:SSZ`` in UTC, it supports
    a few relaxed formats like:

    * YYYY-MM-DD
    * YYYY-MM-DD HH:MM:SS
    * YYYY-MM-DD HH:MM:SS+hh
    * YYYY-MM-DD HH:MM:SS+hh:mm

    When no timezone is defined, it will use the local timezone.

    When no hour is defined, it will assume the time as 00:00:00 (midnight).
    When no minute or seconds are defined, it will assume them as 00.

    When a date is defined, it needs to have the full year, month and day.


amend_write_name
^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 3.30.0
:Values: * `uuid-prefix`
         * `Inherit`
         * Empty
:Description:
    This configurations adds the option to transparently amend the file
    name used during a file write request (write new file or append).

    Set it to `uuid-prefix` to have an UUID version 4
    prefixed to the file name.

    Remote clients are unaware of the file name being changed.
    They will make a request to upload a file with name
    ``/parent/REPORT.CSV`` and
    in the background, the SFTPPlus server will store it on disk as
    ``/parent/f1efde05-9b54-4fd7-a6cb-9fffc62cc631-REPORT.CSV``.

    When this is enabled, the write request will prevent any overwriting
    actions.
    If a file with the randomly generated name already exists, the write
    request will fail.


    When this is enabled, any request to write the file in any way
    (write new file, append, or write updates) will result in a new file
    being creating and the specific write request to be ignored.

    When this option is set to `Inherit`, the value defined for the account's
    group will apply.

    Leave it empty to not amend the file names for the upload requests.


create_home_folder
^^^^^^^^^^^^^^^^^^

:Default value: `No`
:Optional: Yes
:From version: 1.6.0
:Values: * `Yes`
         * `No`
         * `Inherit`
:Description:
    This option specifies whether or not the server should create
    the home folder for an account, in the case that it is missing.

    If this option is set to `No`, the server will not allow users for which
    the home folder is not already created.
    When set to `Yes`, the server will try to create missing home folders for
    users that are successfully authenticated.

    For application accounts, new home folders are created using the
    same account under which the server is executed.
    They will be owned by the server's service account.

    For operating system accounts, the home folders are owned by the associated
    OS accounts.
    On Windows systems, they are created by the OS together with
    the associated Windows Profile.
    On Unix-like systems, they are created by the root account,
    and the permissions are changed to the associated OS account.

    ..  warning::
        On Windows operating systems, for domain accounts for which
        `home_folder_path` is defined as `${OS_HOME}`, the server will
        not be able to create a missing home folder.
        The server will still be able to create missing home folder when using
        custom home folder paths.


Configuration options available to application accounts
-------------------------------------------------------

Some configuration options are only available for application accounts.


password
^^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 1.6.0
:Values: * Password stored as modular one-way cryptographic hash function.
         * Empty field to disable the password.
:Description:
    This option specifies the password used for authenticating this account.

    In order to make use of the secure hash algorithm,
    please check how to :ref:`generate encrypted
    passwords using admin-commands
    <generate-encrypted-password>`.

    When the password is left blank,
    the account will not be able to authenticate with an empty password,
    even if the `enabled` option is set to `yes`.

    ..  note::
        The `password` is ignored for accounts of `type` `os`.


multi_factor_authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 4.0.0
:Values: * OTP Authentication URL
         * Empty.
:Description:
    This option specifies the One-Time Password shared secret associated
    with this account, stored as an `otpauth://` URI, as defined by
    the `Google Authenticator Key URI Format
    <https://github.com/google/google-authenticator/wiki/Key-Uri-Format>`_.

    More information on 2-step authentication is available in the
    :doc:`cryptography guide </standards/cryptography>` page.


password_lifetime
^^^^^^^^^^^^^^^^^

:Default value: `inherit`
:Optional: Yes
:From version: 3.46.0
:Values: * Number of days.
         * `Inherit`
:Description:
    Number of days for which a password is valid.

    Once a new password is set, it is valid for the configured number of
    days.

    If the password is not changed for the configured number of days,
    the account is automatically disabled.
    To re-enable it, a new password needs to be set by an administrator.

    ..  note::
        To allow users to change their own passwords, make sure
        `allow_own_password_change` is enabled in the associated group.


last_password_update
^^^^^^^^^^^^^^^^^^^^

:Default value: `0`
:Optional: Yes
:From version: 3.46.0
:Values: * Unix timestamp
:Description:
    Unix timestamp for the time of the last password change.

    ..  note::
        This value is automatically updated by SFTPPlus together with the
        main `password` value.
        You should only need to set this value when password expiration
        is enabled and `password` is set via an external process.


Configuration options available to operating system accounts
------------------------------------------------------------

A few configuration options are only available for operating system accounts.


lock_in_home_folder
^^^^^^^^^^^^^^^^^^^

:Default value: `Yes`
:Optional: Yes
:From version: 1.6
:Values: * `Yes`
         * `No`
         * `Inherit`
:Description:
    Specify whether to restrict file system access to the account's
    home folder.
    When accounts are locked inside the home folder, access to
    files and folders outside the home folder path will be denied, and the home
    folder path will be the root of the available file system.


create_home_folder_owner
^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `${DEFAULT_OS_USER}`
:Optional: Yes
:From version: 1.6.0
:Values: * Name of an account defined inside the operating system.
         * `${DEFAULT_OS_USER}`
         * `Inherit`
:Description:
    When the server is configured to automatically create missing home
    folders, this option specifies who should be the owner of the newly
    created folder.

    When this option is set to `${DEFAULT_OS_USER}`, the folder owner will be
    set to the default value specified by the operating system.

    When this option is set to `Inherit`, the value defined for the account's
    group will apply.


create_home_folder_group
^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `${DEFAULT_OS_GROUP}`
:Optional: Yes
:From version: 1.6.0
:Values: * Name of a group defined by the operating system.
         * `${DEFAULT_OS_GROUP}`
         * `Inherit`
:Description:
    When the server is configured to automatically create missing home
    folders, this option specifies what group should be associated with the
    newly created folder.

    When this option is set to `${DEFAULT_OS_GROUP}`, the folder group will be
    set to the default value specified by the operating system.

    ..  note::
        On Windows operating system, `${DEFAULT_OS_GROUP}` is defined as
        the *Users* group.
        Please contact us in the case that you need different behaviour.

    When this option is set to `Inherit`, the value defined for the account's
    group will apply.
