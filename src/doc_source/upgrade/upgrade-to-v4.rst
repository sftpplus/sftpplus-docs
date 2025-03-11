Upgrade to version 4
====================

..  contents:: :local:


Introduction
------------

SFTPPlus version 4 was released in 2020.
Version 4 is no longer in active development.
It was superseded by version 5, released in 2024.

Version 4 is still supported until 2027.

If you are still using SFTPPlus version 2 or older,
and you plan to upgrade, get in touch with our support team.
They can help you upgrade to the latest supported version.


Upgrade process from version 3
------------------------------

You can install latest SFTPPlus version 4 over an existing version 3 installation,
similar to normal upgrade.

The configuration file is automatically updated.

During the installation you need to use the same instance name and destination path,
as the initial install.

Check if any custom paths or instance names are used for your installation.

You can check the installation path and instance name using the event `20072` from the log file, or the information deployed in the Web Manager Console.

Below are the default values:
* Installation path: `C:/Program Files/SFTPPlus/`
* Instance name: `SFTPPlus`


Functionality changes
---------------------

* If you are still using a SFTPPlus init script from version 2.10.0 or older,
  replace the `--start` command line argument with the `start` subcommand.

* Remove clear text passwords for accounts and replace them with hashed-based
  version.
  This can be done by setting new passwords via the Local Manager web-based
  management console.
  You can also generate hashed version of the password by using the
  `admin-commands generate-password` command line.
  If you want to automatically convert any plain text passwords to hashed-based passwords,
  upgrade to SFTPPlus version 5.

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

* The database event handler now only support SQLite3 embedded databases and
  is configured with the direct path ot the database file.
  SFTPPlus will automatically try to migrate the configuration and use
  `log/server.db3` as the path to the log file.
  You need to review the configuration for the event handler to make sure it
  was correctly migrated.

* SFTPPlus now has a separate embedded databases used for storing the
  event logs and another dedicated databased used to store internal state.
  The internal state database configuration is automatically created under
  `[resources/DEFAULT-SQLITE]`


Configuration changes from version 3 to version 4
-------------------------------------------------

Below is the list of low-level configuration change made when upgrading from SFTPPlus version 3 to a newer version 4:


* If you are using `rotate_each` configuration,
  replace it with the `rotate_on` configuration.

* `address`, `port`, and `path` configuration options are now removed from
  the Syslog event handler.
  SFTPPlus will automatically try to use existing `address`, `port`, and `path`
  values and present them as the `url` configuration.
  If you are not already using the `url` configuration option, you need
  to update it, especially if you have `address = 127.0.0.1`.


* SFTPPlus is now configured with resource monitor having the
  `DEFAULT-ANALYTICS` UUID.
  If your configuration already contains an resource monitor, it will
  be automatically migrated to a resource with UUID `DEFAULT-ANALYTICS`.

* SFTPPlus' `process-monitor` resource was renamed as the `analytics` resource.
  You can continue to use `process-monitor` as the type name for this resource.

* SFTPPlus now provides an embedded analytics component.
  The previous `account-activity` event handler was integrated into this new
  analytics component.
  If your configuration already contains an `account-activity` event
  handler, it will be automatically migrated.

* Configuration for Let's Encrypt certificate generation is now always
  present inside the configuration file as `[resources/DEFAULT-LETS-ENCRYPT]`.
  If you don't have Let's Encrypt support enabled, this configuration
  is created under the disabled state.

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
