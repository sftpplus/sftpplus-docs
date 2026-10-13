Analytics and alerts
====================

..  contents:: :local:


Introduction
------------

The `analytics` resource is defined for monitoring and recording the
activity and state of SFTPPlus.

For example, it collects last user login information that can be
later retrieved and displayed as a report inside the Web Manager.
The logins span across all services configured on the server (FTP, SFTP,
Web Manager, etc.).

At the configured interval, a dedicated event containing the usage counters is generated.

Exceptional events are emitted when the usage for a resource hits a certain
value / limit.
These events can be linked with the `email-sender` event handler,
in order to raise alerts over email.

An example for monitoring resource usage every 2 minutes (120 seconds),
triggering an exceptional event
when there are more than 1000 total active connections::

    [resources/03c4-1caf-fee0]
    enabled = yes
    name = Analytics Engine
    type = analytics
    monitor_interval = 120
    connections_count_trigger = 1000


.. _configuration-analytics-certificate-warnings:

Certificate and PGP key expiration warnings
-------------------------------------------

The `analytics` resource warns when configured certificates or PGP keys have expired or are about to expire.
Each warning triggers an event with code `20114` and identifies the affected component and certificate or PGP key setting.
The checks run when SFTPPlus starts and once per day, at midnight.

Certificate expiration warnings are also visible in the Web Manager to administrators whose :doc:`roles </administration/roles>` grant read access to the `analytics` resource.
This access reveals the names and UUIDs of affected components, including accounts and locations, even when the administrator has no direct read access to those components.
Viewing a warning does not grant access to the component's configuration.
Administrators need the appropriate read and edit permissions for the affected component to resolve the warning.

The checks cover the general server TLS certificate and certificates configured for enabled services, authentication methods, and event handlers.
Certificates configured for locations and resources are also checked, including components such as FTPS locations and email clients that start on demand.
Private certificates and configured trusted certificates are checked.
PGP keys configured for signing, verification, encryption, and decryption in enabled OpenPGP event handlers are also checked.
PGP keys without an expiration date do not generate expiration warnings.

For a set of trusted certificates, a warning reports the earliest certificate expiration.
Pinned certificates and public keys are excluded from these checks.

AS2 certificates are checked for both sending locations and receiving services, together with partner certificates configured for enabled accounts.
HTTPS certificates configured for asynchronous AS2 MDN responses are also checked.


.. _configuration-analytics-account-warnings:

Account and password expiration warnings
----------------------------------------

The `analytics` resource checks enabled accounts for upcoming account and password expiration when SFTPPlus starts and once per day, at midnight.
Warnings appear in the Web Manager and generate event `20068`.

The `account_expiration_warning` and `password_expiration_warning` options specify how many days before expiration to generate warnings.
Set either option to `0` to disable its warnings.
Accounts and passwords without an expiration date, or that have already expired, do not generate expiration warnings.

Administrators can view these warnings when their roles grant read access to the `analytics` resource.
The access rules described in :ref:`configuration-analytics-certificate-warnings` also apply to account and password warnings.


enabled
-------

:Optional: Yes
:Default value: Yes
:Values: * Yes
         * No
:From version: 4.0.0
:Description:
    Set to `Yes` to have the resource monitor enabled.

    Set it to `No` to have the resource stopped.

    You can still manually start and stop the resource from the
    Web Manager.


monitor_interval
----------------

:Default value: 60
:Optional: No
:Values: * Number of seconds
:From version: 3.44.0
:Description:
    Time interval, in seconds, between system checks.

    This value is only used by analytics functionality that requires constant monitoring.
    For example, checking the resource usage or auto-disabling of inactive accounts.

    Login date, time, and transfer activity is recorded in real time.

    For production environments we recommend setting a value
    equal to or greater than 60 seconds.
    Lower values may impact the overall performance of the system.


memory_resident_trigger
-----------------------

:Default value: 0
:Optional: Yes
:Values: * Number of bytes
         * 0
:From version: 3.44.0
:Description:
    Amount of resident / non-swapped physical memory used by SFTPPlus,
    in bytes, for which to emit an exception event if its process is using
    more than the configured value.

    On Windows, it matches the `Mem Usage` column of the task manager.
    On other OSes, it matches the `RES` column of the `top` command.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


memory_virtual_trigger
----------------------

:Default value: 0
:Optional: Yes
:Values: * Number of bytes
         * 0
:From version: 3.44.0
:Description:
    Total amount of virtual memory used by SFTPPlus, in bytes,
    for which to emit an exception event if its process is using
    more than the configured value.

    This includes both physical memory and swapped memory.

    On Windows, it matches the `VM Size` column of the task manager.
    On other OSes, it matches the `VIRT` column of the `top` command.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


connection_count_trigger
------------------------

:Default value: 0
:Optional: Yes
:Values: * Number
         * 0
:From version: 3.44.0
:Description:
    Total number of connections (server-side and client-side) used by SFTPPlus
    for which to trigger an exceptional event.

    This includes the following connection categories:
    * Incoming connections made to file transfer services
    * Outgoing connections made to remote servers through configured transfers
    * Syslog / HTTP Authentication / HTTP Event Handlers connections
    * Connections made to the Web Manager service.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


file_count_trigger
------------------

:Default value: 0
:Optional: Yes
:Values: * Number
         * 0
:From version: 3.44.0
:Description:
    Total number of local files used by SFTPPlus
    for which to trigger an exceptional event.

    This includes all files opened by SFTPPlus
    as part of file transfer operations or for administrative operations.

    For example, log files used by event handlers are included in this count.

    A single connection can trigger the opening of multiple local files.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


thread_count_trigger
--------------------

:Default value: 0
:Optional: Yes
:Values: * Number
         * 0
:From version: 3.44.0
:Description:
    Total number of threads used by SFTPPlus
    for which to trigger an exceptional event.

    Take into consideration that multiple transfers can use the same thread.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


certificate_expiration_warning
------------------------------

:Default value: 21
:Optional: Yes
:Values: * Number of days
         * 0
:From version: 5.15.0
:Description:
    A warning is generated in Web Manager and an event is emitted if
    SFTPPlus is configured with a certificate that is about to expire in less than the configured number of days.

    Set it to `0` to disable triggering these alerts.

    See :ref:`configuration-analytics-certificate-warnings` for details about the checks and the certificates they cover.


account_expiration_warning
--------------------------

:Default value: 21
:Optional: Yes
:Values: * Number of days
         * 0
:From version: 5.24.0
:Description:
    An event is emitted if an account is enabled and is configured to expire in less than the configured number of days.

    No event is emitted for accounts that don't have an expiration date configured
    or which are already expired.

    This is configured as number of days.

    This is checked once per day, at midnight, and when SFTPPlus starts.

    Set it to `0` to disable triggering these alerts.

    See :ref:`configuration-analytics-account-warnings` for details about the checks and administrator access.


password_expiration_warning
---------------------------

:Default value: 14
:Optional: Yes
:Values: * Number of days
         * 0
:From version: 5.24.0
:Description:
    An event is emitted if an account is enabled and is configured with a password that is about to expire in less than the configured number of days.

    No event is emitted when the password is already expired.

    This is configured as number of days.

    This is checked once per day, at midnight, and when SFTPPlus starts.

    Set it to `0` to disable triggering these alerts.

    See :ref:`configuration-analytics-account-warnings` for details about the checks and administrator access.


account_auto_disable_grace_interval
-----------------------------------

:Default value: `7`
:Optional: Yes
:Values: * Number of days
:From version: 5.15.0
:Description:
    Number of days to delay auto-disabling of an inactive account,
    based on date it was last changed.

    Inactive accounts are accounts that don't have successful logins,
    in the time interval configured for each account or each group using the `disable_on_inactivity` configuration option.

    For example, when an account is auto-disabled,
    you can manually re-enable the account and the `account_auto_disable_grace_interval` is the interval for which the account remains active.
    If no successful logins are performed in the grace interval,
    the account will be auto-disabled again.

    This configuration is also used for accounts that don't have any login records at all.
    For those accounts, the account configuration changed date is used as the base for the grace period.

    This should be configured with a value equal or greater than 1 day.

    It is recommended to configure it to a value smaller than the one configured for the `disable_on_inactivity` option set for accounts or groups.
