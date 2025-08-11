Upgrade to version 2
====================

..  contents:: :local:


Introduction
------------

SFTPPlus version 2 was released in 2013.
It is no longer a supported version.
The information on this page is provided for legacy deployments.

If you are still using SFTPPlus version 1 and you plan to upgrade,
get in touch with our support team.
They can help you upgrade to the latest supported version.


Upgrading from versions 1 to 2
------------------------------

Upgrading from a 1.x version to a 2.x version requires preservation
of the configuration data, reinstallation of the server, and
integration of the existing data into the new system.


* Make sure the system is in maintenance mode and there are no active file
  transfers.

* Stop the SFTPPlus service.

* Copy the configuration files to a backup location. Optionally, consider
  copying the log files as well.

* Uninstall the SFTPPlus version running on your server.

* Download the latest version of SFTPPlus Serve 2.x and install it on your
  machine.

..  note::
    The main changes that were introduced with version 2.0 are highlighted
    below.
    Please consult the :doc:`Release Notes<./release-notes>` in
    order to have a more detailed view of particular changes in each release.

You will notice the new version is now using a single configuration file.
The settings contained by the `server.config`, `users.config`,
`sftp-service.config`, `ftp-service.config` and `ftpsi-service.config`
will need to be manually migrated to the new `server.ini` configuration file.
This can be done by following the instructions below.

The sample `server.ini` configuration file includes some explanatory comments.
However, for a thorough understanding of all the options, please consult
our documentation.

The `services_` prefix has been removed from *all* configuration options.
When moving information from one file to the other, please remember to
delete the prefix, otherwise the option will be ignored.


Migrating Server configuration options
--------------------------------------

The options defined under the `[services]` section in the `server.config` file
have to be copied over to the `[server]` section in `server.ini`.

All `services_` prefixes should be deleted.

The `services_users_configuration_file` option is no longer of any use,
as the users are defined in the same configuration file.
Therefore, it should be removed.

New attributes have to be defined in the [server] section: the UUID, ``name``,
and ``description``.
More information about each of them can be found in the documentation files.


Migrating Log configuration options
-----------------------------------

The options defined under the [log] section in the `server.config` file have
to be copied over to the [log] section in `server.ini`.

No other changes are required.


Migrating Services configuration options
----------------------------------------

Services configurations are now defined using a new section marker in the
`server.ini` file.

Each service now has a universally unique identifier (UUID) and a human
readable short name. This allows rename operations and operating multiple
services in a cluster environment.
For more details see :doc:`documentation</configuration/introduction>`.

For example, to update the service configuration for a service named
``ftp-partners`` with the following configuration::

    [services/d7623fb2-4e1f-483e-8599-f5599ac15eb1]
    name = ftp-partners
    service_enabled = yes

Please use the example below to update the `services` configuration section::

    [services/550e8400-e29b-41d4-a716-446655440000]
    name = ftp-partners
    enabled = yes

The service configuration options have been moved from dedicated files into
the main configuration file.

All configuration options in the `[service]` section of each service
configuration file need to be copied inside the dedicated section for
each service in `server.ini`, along with specific configurations in
`server.config`.

Here is an example of a service section definition for an FTP protocol::

    [services/550e8400-e29b-41d4-a716-446655440000]
    name = ftp-partners
    enabled = yes

Protocol options copied from ``configuration/ftp-service.config`` file::

    [services/b9787c72-2c8b-4725-a049-ee628aa0abc1]
    name = ftps
    banner = Welcome to the FTP/FTPS Service.
    passive_port_range = 9000 - 9200

All `services_` prefixes need to be removed, otherwise those options will be
completely ignored.


Migrating groups and users configuration
----------------------------------------

Groups and accounts configurations have been moved from the dedicated file
into the main configuration file.
All accounts and groups should now have an associated UUID.

`OS_GROUP` is now a regular group, and accounts are not automatically
associated to this group.
We recommend renaming it as `os_group`, to suggest that it is just a normal
group.

`APPLICATION_GROUP` has been renamed as `DEFAULT_GROUP`.
`DEFAULT_GROUP` is automatically associated to all accounts for which a group
was not explicitly defined.
These are operating system accounts not defined in the configuration
file or legacy SFTPPlus WebAdmin accounts.

The `${DEFAULT_GROUP}` placeholder has been renamed as `${DEFAULT_OS_GROUP}`.
The new name should make it clear that it is referring to a group defined by
the operating system.

The `${DEFAULT_USER}` placeholder has been renamed as `${DEFAULT_OS_USER}`.
The new name should make it clear that it is referring to an account defined by
the operating system.

Configuration sections for groups are now in the format
``[groups/550e8400-e29b-41d4-a716-446655440001]``, and the name of the group
is now a configuration option.
``550e8400-e29b-41d4-a716-446655440001`` is the group unique ID.
The `type` configuration option is no longer of any use.

Configuration sections for accounts are now in the format
``[accounts/550e8400-e29b-41d4-a716-446655440000]``, and the name of the account
is now a configuration option.
``550e8400-e29b-41d4-a716-446655440000`` is the account unique ID.
This allows renaming for accounts.

Here is an example of a new accounts definition::

    [accounts/550e8400-e29b-41d4-a716-446655440000]
     name = john
     type = application
