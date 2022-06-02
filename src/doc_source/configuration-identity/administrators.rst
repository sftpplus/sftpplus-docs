Administrators
==============

Administrators are dedicated to accessing the
:doc:`Local Manager administration service </configuration/local-manager>`.
They cannot be used for file transfer operations.

In order to simplify configuration management for a large number of
administrators, the administrators are associated to a role.

This allows, for example, to easily disable access for all administrators
associated to a particular role by simply disabling the role instead of having
to disable every administrator.

..  contents:: :local:


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
:doc:`the dedicated UUID documentation </configuration/introduction>`.

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

:Default value: Empty
:Optional: Yes
:From version: 2.1.0
:Values: * Password encrypted using a one-way cryptographic hash function.
         * Empty.
:Description:
    This option specifies the password used for validating the
    credentials for this administrator.

    It is stored encrypted using the cryptographic hash function SHA-256.

    To get the hashed password please check how to :ref:`generate encrypted
    passwords using admin-commands <generate-encrypted-password>`.

    When the password left empty, the administrator
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


roles
^^^^^

:Default value: `DEFAULT-ROLE`
:Optional: No
:From version: 4.16.0
:Values: * UUID of a role.
         * Comma-separated UUID of roles
:Description:
    This option defines the roles associated with this administrator.

    It can be configured with one or multiple role UUIDs.

    The first UUID is the primary role of this administrator.

    Updating this configuration doesn't impact the sessions of
    already authenticated administrators, which continue to use
    the old configuration value.
    The new value is only used for new authentications.
