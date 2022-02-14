Identity and Access Management for administrators (IAM)
#######################################################

..  contents:: :local:


Introduction
============

The operations available to administrators are defined based on a list of
allowed actions targeting the managed SFTPPlus components.

The Identity and Access Management (IAM) configuration is implemented
in SFTPPlus using the following configuration elements:

* administrators - defines the authentication and the identity of
  administrators
* roles - defines the allowed access for administrators.


Administrators configuration
============================

As a best practice, it is recommended to create an administrator configuration
for each person interacting with SFTPPlus as an administrator.

When configuring an administrator, you define a name/username and a password.

..  warning::
    Having multiple persons sharing the same administrator name and password
    is not recommended because it makes it harder to audit the actions of each
    administrator.

The configuration of an administrator also includes the associated role.

All the access permissions for the administrators are configured via the
associated role.


Role configuration
==================

When configuring a role, you define its name and a list of permissions.

By defining multiple roles, you can implement a separation of duties and have
different levels of administrative access.

Each permission definition consists of:

1. an expression matching the permission target
2. a list of permission actions.

You can define a single permission-matching expression to target multiple
configuration options or a class of configuration options.

To only allow updating the name of users and groups while denying updating any
other option and creating or deleting groups, the following configuration
can be used::


    [roles/70c0-4e1d-8480]
    name = allow-name-updates
    permissions =
      configuration, read
      configuration/identity/accounts/*/name, update
      configuration/identity/groups/*/name, update

To only allow creating, deleting, and updating users and groups the following
configuration can be used::

    [roles/70c0-4e1d-8480]
    name = user-group-administrators
    permissions =
      configuration, read
      configuration/identity/accounts/*, all
      configuration/identity/groups/*, all


Available permission targets
============================

Below is a list of the target groups that can be targeted based on
member UUIDs, with or without an option name::

* configuration/identity/accounts
* configuration/identity/accounts
* configuration/identity/groups
* configuration/identity/roles
* configuration/identity/administrators
* configuration/authentications
* configuration/locations
* configuration/resources
* configuration/services
* configuration/transfers
* authentications
* locations
* resources
* services
* transfers
* status

You can target a class of configurations,
or any configuration of a certain type.
The following examples are valid:

* configuration/services/* - target the configuration of any service
* configuration/services/FTPS-server-UUID/* - target any configuration for the
  service with UUID ``FTPS-service-UUID``
* configuration/services/\*/name/ - target all the name options for any service
* configuration/services/FTPS-server-UUID/* - target only the name
  option for the service with UUID ``FTPS-service-UUID``
* services/* - target the status of any service
* services/FTPS-service-UUID/* - target the status of the service with UUID
  ``FTPS-service-UUID``.

The following configurations do not have a member UUID, so they can only be
targeted using the option name:

* configuration/server
* configuration/server/*
* configuration/server/**OPTION-NAME**/
* status

There is a special permission target named `sync_pull` used to configure
synchronization.
Administrative roles assigned to real persons should not use this target.
