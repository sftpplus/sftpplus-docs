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

For example, to create a role in which administrators are only allow updating the name of users and groups while denying updating any other option and creating or deleting groups,
the following configuration can be used::


    [roles/70c0-4e1d-8480]
    name = allow-name-updates
    permissions =
      configuration, read
      configuration/accounts/*/name, update
      configuration/groups/*/name, update

To only allow creating, deleting, and updating users and groups the following
configuration can be used::

    [roles/70c0-4e1d-8480]
    name = user-group-administrators
    permissions =
      configuration, read
      configuration/accounts/*, all
      configuration/groups/*, all


Available permission targets
============================

Below is a list of the target groups that can be targeted based on
member UUIDs, with or without an option name::

* me
* configuration/accounts[/{UUID}]
* configuration/groups[/{UUID}]
* configuration/roles[/{UUID}]
* configuration/administrators[/{UUID}]
* configuration/authentications[/{UUID}]
* configuration/resources[/{UUID}]
* configuration/event_handlers[/{UUID}]
* configuration/services[/{UUID}]
* configuration/locations[/{UUID}]
* configuration/transfers[/{UUID}]
* operation/authentications[/{UUID}]
* operation/resources[/{UUID}]
* operation/event_handlers[/{UUID}]
* operation/services[/{UUID}]
* operation/locations[/{UUID}]
* operation/locations/{UUID}/browse/[{PATH}]
* operation/transfers[/{UUID}]
* node_variables
* status

Values in square brackets are optional.
Values in curly brackets should be replaced with the actual UUID or PATH.

You can target a class of configurations,
or any configuration of a certain type.
The following examples are valid:

* me/* - target any configuration of the current authenticated administrator
* configuration/services/* - target the configuration of any service
* configuration/services/FTPS-server-UUID/* - target any configuration for the service with UUID ``FTPS-service-UUID``
* configuration/services/\*/name/ - target all the name options for any service
* configuration/services/FTPS-server-UUID/name - target only the `name` option for the service with UUID ``FTPS-service-UUID``
* operation/services/* - target the status of any service
* operation/services/FTPS-service-UUID/* - target the status of the service with UUID ``FTPS-service-UUID``.

The following configurations do not have a member UUID, so they can only be
targeted using the option name:

* configuration/server
* configuration/server/*
* configuration/server/**OPTION-NAME**/
* status

There is a special permission target named `sync` used to configure
synchronization between the cluster controller and the cluster nodes.
Administrative roles assigned to real persons should not use this target.


Multi-role permissions
======================

An administrator can have multiple roles,
each with its specific set of permissions.
When an administrator has multiple roles,
their permissions are defined as the union of all permissions of their roles.

The order of permissions are defined by the order in which the administrator is associated to their roles.

For example, with the following configuration::

    [roles/21951ed4-c281]
    name = Transfers Operator
    permissions =
      /operation/*, read
      /configuration/transfers/*, all
      /operation/transfers/*, all

    [roles/94a9caefd093-4677]
    name = Users Operator
    permissions =
      /operation/*, read
      /configuration/*, read
      /configuration/accounts/*, all

    [administrator/dca95a60-dca2]
    name = John Admin
    roles = 21951ed4-c281, 94a9caefd093-4677

The `John Admin` administrator will have the following permissions,
based on the order in which the administrator roles are configured::

      /operation/*, read
      /configuration/transfers/*, all
      /operation/transfers/*, all
      /configuration/*, read
      /configuration/accounts/*, all


Multi-role deny permissions
===========================

An administrator with multiple roles accumulates all the
permissions of those roles.

If you want to define a role that blocks accumulating permissions
from other roles, you can use the `deny` permission action in
that role. Then use that role as first in the list of multiple roles
for one or more administrators.

For example, with the configuration below::

    [roles/6b4b0fc2-e9c1]
    name = Read Only Admin
    permissions =
      /operation/*, read
      /configuration/*, read
      /operation/*, deny
      /configuration/*, deny

    [roles/94a9caefd093-4677]
    name = Users Operator
    permissions =
      /operation/*, read
      /configuration/*, read
      /configuration/accounts/*, all

    [administrator/dca95a60-dca2]
    name = John Admin
    roles = 6b4b0fc2-e9c1, 94a9caefd093-4677

When administrator `John Admin` is authenticated it will have the following permissions::

      /operation/*, read
      /configuration/*, read
      /operation/*, deny
      /configuration/*, deny
      /configuration/accounts/*, all

Since the `/configuration/*, deny` is explicitly configured in the primary role `Read Only Admin`,
it denies access to `/configuration/accounts/*, all`.
In this way, the `John Admin` administrator remains a read-only account.

The order used to configure the roles associated to an administrator is important.
In the above example, if the administrator is configured with `Users Operator` as the primary role
(configuration `roles = 94a9caefd093-4677, 6b4b0fc2-e9c1`),
the administrator has read/write access to accounts configurations.


Allow administrators to change own configuration (for example password)
=======================================================================

To allow an administrator to create, delete, and update users and groups without changing the configuration of other administrators,
the following configuration can be used.
The `own` prefix can be used to allow the administrator to change own configuration such as the password of the multi-factor authentication token::

    [roles/70c0-4e1d-8480]
    name = user-group-administrators
    permissions =
      own/password_update, all
      own/multi_factor_authentication, all
      configuration, read
      configuration/accounts/*, all
      configuration/groups/*, all
