Authentication, Users and Admins
================================

An authentication method configuration provides the required information to
allow SFTPPlus to use a specific method in order to authenticate
file transfer accounts and administration account.

Below is the list of supported authentication methods.

..  note::
    Not all authentication method types support authenticating the
    administrators for the Web Manager service.

The identity configuration defines the users, groups, administrators and roles created as part of the SFTPPlus application.

For these users and administrators the full life-cycle is managed by SFTPPlus.



..  toctree::
    :maxdepth: 1

    introduction
    accounts
    groups
    administrators
    roles
    application
    os
    http
    local-file
    ldap
    entra-id
    google-identity
    okta-oidc
    radius
    deny-username
    ip-time-ban
    anonymous
