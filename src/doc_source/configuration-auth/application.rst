SFTPPlus embedded users
=======================

An `application` authentication method can be used to authenticate users
based on accounts defined in the configuration file of SFTPPlus.

It will authenticate accounts of type `application`.

..  contents:: :local:

.. include:: /configuration-auth/authentication-commons.include.rst


allowed_groups
--------------

:Default value: Empty
:Optional: Yes
:Values: * Empty
         * Group UUID
         * Comma-separated list of group UUIDs.
:From version: 4.0.0
:Description:
    Defines a group or a list of groups with users that
    are allowed by this authentication method.

    When this is empty, any account is accepted as long as it has valid
    credentials.

    For an account that is a member of multiple groups,
    the authentication succeeds when at least one of those groups is found
    in the `allowed_groups` list.

    ..  note::
        This option applies to group UUID values, not group names.
        This makes it possible to rename a group without having to update
        this configuration option.


strict_group_access
-------------------

:Default value: `no`
:Optional: Yes
:Values: * `yes`
         * `no`
:From version: 5.14.0
:Description:
    When enabled,
    accounts that are members of multiple groups will have their group membership filtered based on the list of `allowed_groups` for this authentication method.

    When `strict_group_access` is not enabled,
    the authenticated accounts will get access based on all their associated groups.

    For example, with the below configuration::

        [authentications/a0d20dae-5287-11f0-9f81-33973af0e22d]
        allowed_groups = Group-A
        strict_group_access = no

    If user ``JohnD`` is member of both ``Group-A`` and ``Group-B``,
    the user is authenticated and the user will get access based on the configuration of both ``Group-A`` and ``Group-B``

    When `strict_group_access` is enabled,
    the authenticated accounts will only get access based on the allowed groups.
    For example, with the below configuration::

        [authentications/a0d20dae-5287-11f0-9f81-33973af0e22d]
        allowed_groups = Group-A, Group-B
        strict_group_access = yes

    If user ``JohnD`` is member of both ``Group-A``, ``Group-B``, and ``Group-C``,
    the user is authenticated and the user will get access based only on the configuration of ``Group-A`` and ``Group-B``.
    The virtual folders and permissions granted by ``Group-C`` are not enabled for the user.
