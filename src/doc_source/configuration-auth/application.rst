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
