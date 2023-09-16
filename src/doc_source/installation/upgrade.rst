Upgrade Procedures
==================

..  contents:: :local:


Introduction
------------

Before proceeding with any upgrade, ensure that SFTPPlus, along with all file
transfer services, are stopped.

Initializing the configuration or the service account and groups
is not required for an upgrade.

When upgrading from version 4.26.0 or newer to the latest version
on Linux and macOS,
you can use the included ``bin/update.sh`` script
providing as a parameter the latest SFTPPlus package for your OS.
This takes care of all the necessary steps
while backing up your current installation.
If you wish to rollback the update, the backed-up installation can be used
to revert to the previous version through the ``bin/rollback.sh`` script.

The following directories are used for backing up the existing installation
when updating to the latest version or rolling back to a previous version using
the provided shell scripts (assuming the default ``sftpplus-mft`` service name):

* ``/opt/sftpplus_backups/sftpplus-mft_UPDATE_AUTO_BACKUP``

* ``/opt/sftpplus_backups/sftpplus-mft_ROLLBACK_AUTO_BACKUP``

Contact us if you need to store in a location other than
``/opt/sftpplus_backups`` the automatic backups saved
when updating and rolling back the current installation of SFTPPlus.

In the case that you need to rollback to a backup other than the one
automatically saved by the ``bin/update.sh`` script, you can provide
the path to its directory as a parameter to the ``bin/rollback.sh`` script.

If upgrading on Windows or from a previous version,
there are different procedures that you can follow, depending
on the version to be upgraded:

* When upgrading from versions 4.x to latest version,
  you can extract the files
  or run the installer using the same installation path.

* When upgrading from versions 3.x to latest version,
  you can extract the files
  or run the installer using the same installation path.

* When upgrading from versions 2.x to latest, it is required to uninstall first
  and reinstall the server and integrate the existing configuration in the
  new system.
  There are significant changes for the logging and authentication parts.

* When upgrading from versions pre-2.0 to latest, one should be aware
  that major configuration changes have been implemented and the process should
  be performed with care.


..  note::
    Regardless of the chosen upgrade procedure,
    check if any custom paths are used for the installation.
    Documentation instructions use default paths and may
    need to be modified accordingly.

In all cases, the configuration files should be backed up before proceeding
with the upgrade, otherwise the configuration data will be lost.

Consult the :doc:`Server Release Notes<../release-notes>`,
as it contains detailed information about the steps required
for upgrading between specific versions.


Upgrading from trial version
----------------------------

Once you have obtained the full version of the software, follow the upgrade
instructions under
"Upgrading from version 4.X.X to a newer one" or
"SFTPPlus manual upgrade on Linux and macOS", depending on your OS.


Upgrading from Windows 32bit to Windows 64bit
---------------------------------------------

As long as a 32bit Windows version of SFTPPlus is upgraded to a 64bit version
using the same installation path, no extra steps are required on top of the
normal upgrade procedure.

Note that the default installation path for 32-bit Windows applications is
`C:\\Program Files (x86)\\SFTPPlus`, while for 64-bit applications it is
`C:\\Program Files\\SFTPPlus`.
In this case you will need to follow these steps:

1. Backup the current configuration directory from
   `C:\\Program Files (x86)\\SFTPPlus\configuration`.
2. Uninstall the existing 32bit SFTPPlus application.
3. Install the new 64bit SFTPPlus application.
4. After 64bit SFTPPlus is installed, go to Windows services and stop the
   `SFTPPlus MFT` service.
5. Copy the previous configuration from
   `C:\\Program Files (x86)\\SFTPPlus\\configuration` to
   `C:\\Program Files\\SFTPPlus\\configuration`
6. Go to Windows Services and start the `SFTPPlus MFT` service.


Upgrading from SFTPPlus Version 3 Windows service
-------------------------------------------------

SFTPPlus vesion 2 and version 3 were running inside Windows using an embedded Windows service controller.

In SFTPPlus version 4 and newer, a separate dedicated Windows service controller is used.

Any SFTPPlus that was initially installed based on version 4.1.0 or newer, already has the
newest controller installed and configured.
No extra changes are required when upgrading.

SFTPPlus installation that were initially installed using an older version of SFTPPlus,
will receive a warning message in the web Administration Console or in the logs.

A reinstall of the SFTPPlus Windows service is required.
Reinstalling the whole SFTPPlus installation is **not** required.
Only the Windows Service needs a reinstall.

To reinstall the Windows service follow these steps:

* Stop the current SFPPlus Windows service.
* From the SFTPPlus installation directory run as administrator the `service-uninstall.bat` script.
* From the SFTPPlus installation directory run as administrator the `service-install.bat` script.
* Open the Windows Service administration tool, find the SFTPPlus service and open the `Properties` window.
* From the `Log on` tab, configure the Windows service account and password to be used to run SFTPPlus.
* Restart the SFTPPlus service.


Upgrading from version 4.X.0 to a newer 4.Y.Z
---------------------------------------------

On Windows, you can choose to upgrade the system by running the self
installing archive.
This is similar to a new installation, but you will
have to use the **same installation path** as the one in your
current installation.

It is very important that you check the latest version and changes, as well
as recommended upgrade procedures in the :doc:`Server
Release Notes<../release-notes>`.

* Before proceeding with the upgrade, ensure the system is in maintenance mode
  and there are no active file transfers.

* Stop the SFTPPlus service.

* Copy the configuration directory to a backup location.

* Run the installer and use the same installation path as the one of
  your current version.


Upgrading from version 3 to 4.Y.Z
---------------------------------

You can install latest SFPPlus 4.Y.Z over an existing version 3 installation,
similar to normal upgrade.

Below is the list of manual configuration change required when upgrading from
SFTPPlus version 3 to a newer 4.Y.Z version:

* If you are still using a SFTPPlus init script from version 2.10.0 or older,
  replace the `--start` command line argument with the `start` subcommand.

* Remove clear text passwords for accounts and replace them with hashed-based
  version.
  This can be done by setting new passwords via the Local Manager web-based
  management console.
  You can also generate hashed version of the password by using the
  `admin-commands generate-password` command line.

* If you are using `rotate_each` configuration,
  replace it with the `rotate_on` configuration.

* `address`, `port`, and `path` configuration options are now removed from
  the Syslog event handler.
  SFTPPlus will automatically try to use existing `address`, `port`, and `path`
  values and present them as the `url` configuration.
  If you are not already using the `url` configuration option, you need
  to update it, especially if you have `address = 127.0.0.1`.

* The `digital-signature-validation` event handler is no longer supported.
  It was replaced by a Python Extension.
  Below is a sample configuration for the new Python extension::

    [event-handlers/1655e38c-8851-11e9-95ff-e362f4e9d3ee]
    enabled: yes
    type: extension
    name: Digital Signature Validation

    target: 10078

    entry_point:
      python:chevah.server.extension.digital_signature.ValidateCSV_RSASSA_PSS
    configuration: {
      "signer_certificate_path": "test_data/pki/file-signing-cert.pem",
      "ssl_certificate_authority": "test_data/pki/ca-cert.pem",
      "ssl_certificate_revocation_list": ["test_data/pki/ca.crl"],
      "ssl_certificate_revocation_list_refresh": 10
      }

* SFTPPlus is now configured with a single SMTP email client resource.
  If your configuration already contains an email client resource, it will
  be automatically migrated to a resource with UUID `DEFAULT-EMAIL-CLIENT`.
  If your configuration has multiple email client resources, you will need
  to manually edit the configuration file and set the `DEFAULT-EMAIL-CLIENT`
  to the email client resource that you want to use.
  The other email client resources are ignored and can be manually removed.

* SFTPPlus is now configured with resource monitor having the
  `DEFAULT-ANALYTICS` UUID.
  If your configuration already contains an resource monitor, it will
  be automatically migrated to a resource with UUID `DEFAULT-ANALYTICS`.

* The database event handler now only support SQLite3 embedded databases and
  is configured with the direct path ot the database file.
  SFTPPlus will automatically try to migrate the configuration and use
  `log/server.db3` as the path to the log file.
  You need to review the configuration for the event handler to make sure it
  was correctly migrated.

* SFTPPlus' `process-monitor` resource was renamed as the `analytics` resource.
  You can continue to use `process-monitor` as the type name for this resource.

* SFTPPlus now provides an embedded analytics component.
  The previous `account-activity` event handler was integrated into this new
  analytics component.
  If your configuration already contains an `account-activity` event
  handler, it will be automatically migrated.

* SFTPPlus now supports a single SMTP client configuration. The previous
  email configuration is automatically migrated as
  `[resources/DEFAULT-EMAIL-CLIENT]`.

* Configuration for Let's Encrypt certificate generation is now always
  present inside the configuration file as `[resources/DEFAULT-LETS-ENCRYPT]`.
  If you don't have Let's Encrypt support enabled, this configuration
  is created under the disabled state.

* SFTPPlus now has a separate embedded databases used for storing the
  event logs and another dedicated databased used to store internal state.
  The internal state database configuration is automatically created under
  `[resources/DEFAULT-SQLITE]`

* The embedded SFTPPlus authentication configuration is now always present
  inside the configuration file as `[authentications/DEFAULT-AUTHENTICATION]`.

* When authenticating operating systems accounts, you now have to define
  the list of OS groups for which to allow access.
  If you want to allow access to all OS groups, you can use the
  `${ALL_OS_GROUPS}` marker::

    [authentications/os-uuid]
    enabled: Yes
    type: os
    name: Operating System Accounts
    description: Accounts provided by the operating system.
    allowed_groups = ${ALL_OS_GROUPS}

* The `type` configuration for a transfer was removed and replaced by
  `delete_source_on_success`.
  SFTPPlus will automatically update the configuration at start.
  The following equivalence applies:

  * `type = copy` -> `delete_source_on_success=No`
  * `type = move` -> `delete_source_on_success=Yes`

* If you are using the SFTPPlus PHP Webadmin authentication,
  you will have to replace it with a generic "HTTP Request"
  authentication method.
  The legacy WebAdmin authentication method is no longer supported.
  If your previous url was configured as
  "http://admin.example.com/SFTPPlus" you should
  now use "http://admin.example.com/SFTPPlus/TransferLoginSimple.php"


Upgrading from version 2.X.X to 3.Y.Y
-------------------------------------

Upgrading from a 2.x version to a 3.x version requires preservation of the
configuration data, reinstallation of the server, and
integration of the existing data into the new system.

* It is recommended to perform the upgrade in a maintenance window and make
  sure there are no active file transfers.

* Stop the SFTPPlus service.

* Copy the configuration directory to a backup location.
  Optionally, consider copying the log files as well.

* Uninstall the SFTPPlus version running on your server.

* Download the latest version of SFTPPlus 3, and install it on your
  machine.

In version 3, the default configuration file is still named `server.ini`.

To enable the new authentication method for `application` and `os`
accounts, you will need to update the `authentications` option inside the
`[server]` section, and add a dedicated method for application accounts.

Below is what the relevant parts of the `[server]` configuration should look
like::

    [server]
    authentications = application-uuid, os-uuid, OTHER-AUTH-UUID
    manager_authentications = application-uuid

    [authentications/03288e36-cf6b-4bd5-a9be-f421372f17e6]
    enabled = Yes
    type = application
    name = Application Accounts
    description = This authentication method allows authentication accounts
        defined in this configuration file.

    [authentications/6d51ed1e-35ec-41d7-8b51-53e56c716212]
    enabled = Yes
    type = os
    name = Operating System Accounts
    description = Accounts provided by the operating system.

To migrate the authentication of global SFTPPlus accounts, remove the
`sftpplus_webadmin` option from the `server` section::

    [server]
    sftpplus_webadmin = http://wsftp.example.com:8080/SFTPPlus/

And replace it with a dedicated `authentications` method::

    [server]
    authentications = OTHER-AUTH-UUID, legacy-webadmin-uuid, MORE-AUTH-UUID

    [authentications/9g51ed1e-35ec-41d7-8b51-53e56c716313]
    enabled = Yes
    type = legacy-webadmin
    name = Legacy SFTPPlus Webadmin

    url = http://wsftp.example.com:8080/SFTPPlus/

To migrate the account `report`, create a new event handler.
In the configuration file, replace::

    [report]
    database = sqlite-db-uuid

With a new `event-handlers` section::

    [event-handlers/8cace339-a2ee-4899-b64e-db2478821b9e]
    enabled = No
    type = account-activity
    name = Account activity
    description = Report last successful login for accounts and administrators.

    database = sqlite-db-uuid

To migrate the file log handler, remove the `logs` handler section::

    [logs/03288e36-cf6b-4bd5-a9be-f421372f17e6]
    enabled = Yes
    name = Default Local Log File
    description = Append logs to a file on the local filesystem.

    type = file

    path = log/server.log

And replace it with a dedicated `event-handlers` section::

    [event-handlers/00feb81f-a99d-42f1-a86c-1562c3281bd9]
    enabled = Yes
    name = Default Local Log File
    description = Append logs to a file on the local filesystem.

    type = local-file

    path = log/server.log

To migrate the Windows EventLog log handler, remove the `logs` handler
section::

    [logs/f643a93d-94d5-4b41-b723-a63a00e3c902]
    enabled = Yes
    name = SFTPPlus Server
    description = Send logs to Windows Event Log Service on local machine.

    type = eventlog

And replace it with a dedicated event handler of `type` ``windows-eventlog``::

    [event-handlers/515361f1-d976-4fe0-979b-0651e2bf591d]
    enabled = Yes
    name = STFPPlus
    description = Send logs to Windows Event Log Service on local machine.

    type = windows-eventlog

To migrate the WebAdmin HTTP Post Request log handler, remove the `logs`
section for the Webadmin HTTP Post::

    [logs/e16af067-8974-4c0d-ae89-eb5f3d59fd65]
    name = Default_WebAdmin
    enabled = No
    name = WebAdmin HTTP Post
    description = Hook to WebAdmin over HTTP.

    type = http-post
    format = webadmin

    url = http://int.example.com/SFTPPlus/AuditAddSimple.php

And create a new `event-handlers` section as::

    [event-handlers/03288e36-cf6b-4kd5-a9be-f421372f17e6]
    enabled = No
    name = WebAdmin HTTP Post
    description = Send logs to Legacy WebAdmin over HTTP.

    type = http
    format = legacy-webadmin

    url = http://int.example.com/SFTPPlus/AuditAddSimple.php

To convert legacy SQLite/MySQL database loggers, you should delete section(s)::

    [logs/0ef580fe-45cb-47e0-b434-c0e44557b364]
    enabled = Yes
    name = SQLite Legacy Log Handler
    description = Send logs to local SQLite file in legacy mode.

    type = sqlite
    path = log/server.db3

And add two new sections, one for the `databases` and one for the
`event handlers`::

    [databases/27b8e2b1-7971-416d-af14-6a8aae2ac46e]
    enabled = Yes
    name = SQLite
    description = SQLite file database connection.

    type = sqlite
    path = log/server.db3

    [event-handlers/22a9d8fb-068d-4a63-8d5d-0ce94ef22a25]
    enabled = Yes
    name = SQLite Event Handler
    description = Store events in local SQLite file.
    type = database
    database = sqlite-db-uuid

If there is already a section for the desired database, you do not need to
create a section for it, just make sure to use the existing database UUID.

Make sure your database UUID matches the one configured for the event handler
in order to pair them.

For MySQL logger(s), you should delete the `logs` section::

    [logs/6d51ed1e-35ec-41d7-8b51-53e56c716212]
    enabled = No
    name = MySQL Legacy Log Handler
    description = Send logs to MySQL database in legacy mode.

    type = mysql

    address = 172.20.0.24
    port = 3306
    username = test
    password = test
    database = test

And create two new sections for `databases` and `event-handlers`::

    [databases/ac547e16-a3ff-4fc3-a6ab-142af2744f50]
    enabled = No
    name = MySQL
    description = MySQL database connection.

    type = mysql

    address = 172.20.0.24
    port = 3306
    username = test
    password = test
    database = test

    [event-handlers/7db823d8-05f8-4481-be98-b87a826ded28]
    enabled = No
    name = MySQL Event Handler
    description = Store events in a MySQL database
    type = database
    database = mysql-db-uuid

The above note on SQLite's database section also applies to MySQL's database
section.

To migrate the Syslog log handler, remove the `logs` handler section::

    [logs/27a31405-a963-4fb9-b4ee-09d415b1a30a]
    enabled = Yes
    name = Syslog Backup
    description = Sends logs to backup syslog server.

    type = syslog

    url = udp://127.0.0.1:
    port = 514

And replace it with a dedicated `event-handlers` section::

    [event-handlers/1ee4337a-22f7-4a67-9a77-5c3a508a8158]
    enabled = Yes
    name = Syslog Backup
    description = Sends logs to backup syslog server.

    type = syslog

    url = udp://127.0.0.1:514

For converting the database log handler into an event handler, remove the
`logs` section::

    [logs/bdfe8e48-5100-4d8a-bac1-441ebc04f9a7]
    enabled = Yes
    name = SQLite Log Handler
    description = Send logs to local SQLite file.
    type = database
    database = sqlite-db-uuid

And replace it with a dedicated `event-handlers` section::

    [event-handlers/681f5f5d-0502-4ebb-90d5-5d5c549fac6b]
    enabled = Yes
    name = Database Event Handler
    description = Send logs to local SQLite file.
    type = database
    database = sqlite-db-uuid


Upgrading from versions 1.X.X to 2.Y.Y
--------------------------------------

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
    Please consult the :doc:`Release Notes<../release-notes>` in
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The options defined under the [log] section in the `server.config` file have
to be copied over to the [log] section in `server.ini`.

No other changes are required.


Migrating Services configuration options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


SFTPPlus manual upgrade on Linux and macOS
------------------------------------------

To upgrade SFTPPlus to the latest version, you have to stop its
running service, then extract and copy the new files over the
existing installation sub-directory.
Before proceeding with the upgrade, ensure you have a backup copy of the
server configuration file.

To find out more about the latest version and changes from your version to
latest release, please consult
the :doc:`Server Release Notes<../release-notes>`.
