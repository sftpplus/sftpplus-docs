Administrators
==============

..  contents:: :local:

Administrators are dedicated to accessing the
:doc:`Local Manager administration service </configuration/local-manager>`.
They cannot be used for file transfer operations.

In order to simplify configuration management for a large number of
administrators, the administrators are associated to a role.

This allows, for example, to easily disable access for all administrators
associated to a particular role by simply disabling the role instead of having
to disable every administrator.


Roles
-----

The roles represent a collection of permissions for Local Manager
administrators that can be individually turned on and off.

Roles can also be associated to operating system groups.
In this way, you can allow access for administrators defined in operating
system groups, e.g. using a Domain Controller or other centralized identity
management systems, just like you would for an application-level administrator.

A role can be shared between operating system groups and application-level
administrators.

..  note::
     The name ``role`` is used to avoid confusion with groups of regular
     accounts.


Adding a new role via Local Manager
-----------------------------------

Roles can be added or changed via Local Manager below.

..  image:: /_static/gallery/gallery-add-role.png


Adding a new role via text configuration
----------------------------------------

Adding a new role is done by creating a new section inside the configuration
file.
The name of the section should be prefixed with ``roles/`` and followed by the
role's UUID.

The role's UUID can be any unique string used to identify the role.
Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/general>`.

For example, to add a new role named **SuperAdmins**::

    [roles/a904e3a6-a59b-4bbf-8abd-edcae4d3774f]
    name = SuperAdmins
    enabled = Yes
    description = Administrators having unrestricted access to Local Manager.


Adding a new administrator via Local Manager
--------------------------------------------

Administrators can be added or changed via Local Manager below.

..  image:: /_static/gallery/gallery-add-admin.png


Adding a new administrator via text configuration
-------------------------------------------------

Adding a new administrator is done by creating a new section inside the
configuration file.
The name of the section should be prefixed with ``administrators/`` and
followed by the administrator's UUID.

The administrator's UUID can be any unique string used to identify the
administrator.
Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/general>`.

An administrator can be an application-level account defined for accessing the
Local Manager or a local operating system account belonging to an
operating system group associated to a role.

For example, to add a new administrator named **sa-admin**::

    [administrators/804aab78-70c0-4e1d-8480-4979e169a0a2]
    name = sa-admin
    enabled = Yes
    description = Administrator account for our super admin.
    password = $5$rounds=1000$utwEAUxeFBXSF0Uf$klQTAMRygQfijPXMYZCddVug
    role = 404aab78-70c0-4e1d-8480-4979e169a0a4

..  note::
    The server does not support authentication of operating system
    administrators that are used for multiple roles.
    In this case, the result is undefined.

..  note::
    Administrator names and passwords longer than 150 characters
    are not allowed by SFTPPlus.
    Generating passwords longer than 128 characters is not possible either.
    These restrictions prevent denial of service attacks.


Configuration options for roles
-------------------------------

The following configuration options are available for roles:


enabled
^^^^^^^

:Default value: `Yes`
:Optional: Yes
:From version: 2.1.0
:Values: * `Yes`
         * `No`
:Description:
    This option specifies whether or not to disable access for all
    administrators.

    ..  note::
        If the administrator is disabled, Local Manager will show an
        authentication failed message if login is attempted.


name
^^^^

:Default value: ''
:Optional: No
:From version: 2.1.0
:Values: * Any text.
         * Name of an existing group defined in the operating system.
:Description:
    Human-readable short string used to identify this role.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 2.1.0
:Values: * Any character string.
:Description:
    Human-readable text that describes the purpose of this role.


source_ip_filter
^^^^^^^^^^^^^^^^

:Default value: `Empty`
:Optional: Yes
:From version: 4.14.0
:Values: * IPv4 address
         * IPv6 address
         * Classless Inter-Domain Routing subnet notation.
         * Comma-separated list of IPv4, IPv6 addresses, or CIDR values.
         * Empty

:Description:
    This option defines the source IP addresses (v4 or v6) from which
    administrators in this role are allowed to authenticate.

    Leave empty to allow any IP address.


permissions
^^^^^^^^^^^

:Default value: `*, all`
:Optional: Yes
:From version: 4.15.0
:Values: * Multiple lines of comma-separated definitions of permissions
         * target-rule, comma, separated, actions
:Description:
    This defines the permissions available to administrators associated to
    this role.

    When this option is empty, the role has full access.

    The option is defined as a list of one or more definitions of permissions,
    with one definition per line.

    A definition of permissions is a comma-separated list of values.
    The first value is an expression defining the targeted elements of the
    permissions.
    The remaining values are the actions allowed to be performed on the
    targeted elements.

    The following element target classes are available:

    * `configuration` - includes all the configuration elements
    * `sync_pull` - allows reading full configuration by a secondary instance
      for synchronization.

    The following actions are available:

    * `all` - allow any action
    * `read` - allow reading the current configuration value or the state of a
      component
    * `update` - allow modifying / updating the value of a configuration or
      the state (start/stop) of a component
    * `create` - allow creating new configuration values
    * `delete` - allow removing existing configuration values
    * `deny` - this is a special value designed for complex scenarios
      and which will deny any action and stop processing any other rules.
      Most of the time you will not need to use it as the `deny` action is
      applied by default for any target.

    If no actions are defined for a definition, the `all` action is used by
    default.

    The `deny` action is an exception.
    Once a target reaches the `deny` action the operation is denied
    and no further rules are checked.
    It takes precedence over any other configured action.

    When the `all` action is configured together with other actions like
    `create` or `update`, they are ignored and only the `all` action is used.

    To allow an action, it must be matched with an explicit permission rule.

    The order of the rules doesn't matter,
    unless your configuration contains a rule using the `deny` action.

    The rules are checked from top to bottom.
    If an action is not explicitly allowed by permissions rule,
    the process continues to check following defined permissions rules.

    For example, to create a role in which administrators are
    allowed to read/view the full configuration,
    modify the existing groups,
    and create and delete accounts,
    you can use the following configuration::

        [roles/70c0-4e1d-8480]
        name = users-admin
        permissions =
          configuration, read
          configuration/identity/accounts, create, delete, update
          configuration/identity/groups, create, update

    More information and examples are available on the
    :doc:`Administrators authorization </operation/admin-authorization>` page.


Options for administrators
--------------------------

The following configuration options are available for administrators.


enabled
^^^^^^^

:Default value: `Yes`
:Optional: Yes
:From version: 2.1.0
:Values: * `Yes`
         * `No`
:Description:
    This option specifies whether or not to enable access for this
    administrator.


name
^^^^

:Default value: ''
:Optional: No
:From version: 2.1.0
:Values: * Any alphanumeric string including `space`, `_` or `-`.
:Description:
    Human-readable short string used to identify this administrator.

    It also represents the ``login`` or ``username`` value for this
    administrator.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 2.1.0
:Values: Any character string.
:Description:
    Human-readable text that identifies the person or entity to use
    this administrator account and/or describes the account's purpose.

    Example::

        [administrators/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
        description = Administrator from the SA team.
                     Contact: someone@email.tld
        name = sa-operator


password
^^^^^^^^

:Default value: `Disabled`
:Optional: Yes
:From version: 2.1.0
:Values: * Password encrypted using a one-way cryptographic hash function.
         * `Disabled` or empty field.
:Description:
    This option specifies the password used for validating the
    credentials for this administrator.

    It is stored encrypted using the cryptographic hash function SHA-256.

    To get the hashed password please check how to :ref:`generate encrypted
    passwords using admin-commands <generate-encrypted-password>`.

    When the password is set to `Disabled` or left blank, the administrator
    will not be able to authenticate, even if the `enabled` option is set to
    `yes`.


source_ip_filter
^^^^^^^^^^^^^^^^

:Default value: `inherit`
:Optional: Yes
:From version: 4.14.0
:Values: * IPv4 address
         * IPv6 address
         * Classless Inter-Domain Routing subnet notation.
         * Comma-separated list of IPv4, IPv6 addresses, or CIDR values.
         * Empty
         * `inherit`

:Description:
    This option defines the source IP addresses (v4 or v6) from which
    administrators are allowed to authenticate.

    Leave it empty to allow any IP address.

    Set it to `inherit` to use the value from the role.


multi_factor_authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:From version: 4.0.0
:Values: * OTP Authentication URL
         * Empty.
:Description:
    This option specifies the One-Time Password shared secret associated
    with this administrator, stored as an `otpauth://` URL, as defined by
    the `Google Authenticator
    <https://github.com/google/google-authenticator/wiki/Key-Uri-Format>`_

    More information on 2-step authentication is available in the
    :doc:`cryptography guide </standards/cryptography>` page.


role
^^^^

:Default value: `DEFAULT-ROLE`
:Optional: No
:From version: 2.1.0
:Values: * UUID for the role associated with this administrator.
:Description:
    Human-readable short string used to identify this role.
