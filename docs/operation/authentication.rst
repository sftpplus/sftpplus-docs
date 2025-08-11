Accounts Authentication
#######################

..  contents:: :local:


Introduction
============

SFTPPlus provides multiple ways in which an account or administrator
can be authenticated.

The server-side security of SFTPPlus is designed based on the
Authentication, Authorization and Accounting (AAA) components.

This page will focus on the Authentication component.
For the Authorization part, check
:doc:`the authentication documentation</operation/authorization>`
while for the Accounting, check
:doc:`the account documentation</guides/event-handlers>`.

Here are a few methods / sources used to authenticate accounts.
For a full list please check the
:doc:`authentication methods configuration</configuration-auth/index>`:

* Anonymous Account
* Application Account (SFTPPlus accounts persisted in a configuration file)
* Operating System Local Account
* Windows Domain Accounts
* Legacy SFTPPlus WebAdmin accounts
* HTTP resource

These accounts can be authenticated by various types of credentials.
Below is a list of supported credentials:

* Username and password provided by the operating system
* Username and password via a domain controller
* Username and password provided in a configuration file
* Username and SSH RSA/DSA keys
* Username and SSL certificates.

..  note::
    SSH RSA/DSA keys credentials are only available when used with SFTP.

    SSL certificate credentials are only available when used with FTPS.

    On the Windows operating system, SSH RSA/DSA key and SSL certificates
    credentials are only available for application accounts, i.e. Windows
    local or domain accounts can be authenticated only based on
    username and password credentials.

While supporting multiple authentication methods and hence multiple
account identity providers, there is the risk of overlapping account
names / IDs, the same account being provided by multiple sources.

The server will check each authentication method in the configured order and
will stop checking other providers at the first source accepting or rejecting
the credentials.
If the source cannot give an accept / reject answer, since the account name /
ID is unknown, the server will ask the next identity source provider.

The authentication process will check to see if there is a valid
request for a new file transfer session.
If the check confirms the provided credentials,
it will return the configuration for the requested account.


Password Policy
===============

In SFTPPlus you can define the password policy used when setting new passwords.

NIST's current password guidelines from 2018, as defined in
Special Publication 800-63-3 Digital Authentication Guidelines, include:

* Minimum password length should be 8 characters,
  with a maximum of no less than 64
* All ASCII and UNICODE characters should be allowed
* Check against a list of “known-bad” passwords
* Remove knowledge-based authentication
* Stop practice of regular password expiration
* Don’t allow password hints
* Remove composition rules
  (i.e., “your password needs to contain at least one upper and
  lowercase character and one special character”),
  and instead focus on longer passwords
* Passwords need to be hashed, salted and stretched

Below you can find how SFTPPlus matches the NIST recommendations:

* You can configure the minimum size for passwords, and SFTPPlus allows
  setting passwords as long as 200 characters.
* The default security policy requires a password of minimum 11 characters.
* When the password strength check is enabled,
  passwords are checked against a list of common, weak, or bad passwords.
  The check includes dates and usernames.
* All ASCII and Unicode characters are allowed.
* Knowledge-based authentication and password hints are not
  available in SFTPPlus.
* Passwords are hashed and salted before being stored,
  and these operations are repeated 80.000 times for each password.

The password policy used to check newly defined password is configured via
the following configuration options from the `[server]` section:

* `password_minimum_strength` - enforce a minimum strength
* `password_minimum_length` - enforce a minimum length
* `password_history` - enforce the number of unique new passwords before an
  old password can be reused.
* `password_hashing_scheme` - defines the function used to hash passwords.

The password strength policy is designed to replace the composite policy rules
that often fail both ways, allowing weak passwords (such as P@ssword1) and
disallowing strong passwords (such as Wow...doestcst).

To require a password policy with a minimum of 12 characters and
`strength` of `best` you can define it as::

    [server]
    password_minimum_strength = 4
    password_minimum_length = 12
    password_history = 10

The password strength is determined using the
`zxcvbn password strength estimator <https://blogs.dropbox.com/tech/2012/04/zxcvbn-realistic-password-strength-estimation/>`_
created by Daniel Lowe Wheeler from Dropbox Inc.


Emailing account credentials
============================

An administrator can send over email the password and the TOTP code
for a new account.
For an existing account, the above can also be sent over email
when updating its credentials.

The following are required in order to send such emails:

* The `Email-Client` resource is configured with a valid email server.
* The account created or modified is defined with an email address as name
  or a dedicated email address is entered for it.

Passwords can only be emailed at account creation or
when updating an account's password.
No other scenario is supported.
This is because the server does not store passwords in a plain text format.
For security reasons,
passwords are stored in a format which makes it practically impossible
to retrieve plain text passwords, even if you have access to the stored values.


Windows Domain Accounts on servers running Active Directory
===========================================================

How does SFTPPlus authenticate Windows Domain accounts?

SFTPPlus uses the Windows API to authenticate Windows Domain accounts via a
Domain Controller, the server running the Active Directory service.

This option only works on Windows machines which is part of the domain as a
"member server".

In terms of SFTPPlus configuration, the software does not interact directly
with Active Directory nor the LDAP server in creating an account.

SFTPPlus only uses the existing Windows authentication capabilities of
existing accounts.


Authenticating with Windows Domain Accounts
-------------------------------------------

There are 3 main configuration cases:

* Domain account configured via default group
* Domain accounts configured via augmented SFTPPlus config
* Domain account configured via augmented SFTPPlus config with inherited
  values from group

This guide focuses on the first two cases.

As for the final case, as this is not a common case, please email Pro:Atria
should you require support.

While this guide is written for those new to SFTPPlus in mind, administrators
can also edit these configurations through the text file equivalent residing
in the `server.ini` configuration file.


Augmenting domain accounts with SFTPPlus account configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following will help guide you in setting up a new SFTPPlus `os` account
that is an existing Windows Domain account.

This setup adds an authentication layer on top of the OS account and thus
allowing account access and ability to conduct file transfers using
SFTPPlus.

These steps assume that the OS account/s and settings already exists.

----

In Web Manager, create a new Account with the type Operating System (`os`).

If the new SFTPPlus `os` account is a Windows Domain Controller Account, the
username is provided in the UPN format (like ``username@domain.com``).
This format is needed if there is an Active Directory forest.

..  image:: /static/operation/windowsdomain-user.png

----

You can allow the account to create a new folder in the account using the
home folder's path (``c:\\ftp-files``) and make sure to lock access.

..  image:: /static/operation/windowsdomain-accounthomefolder.png

----

When SFTPPlus first authenticates the account ``username@domain.com``,
it will create a folder for the `username` as the home
folder path.

In the screenshot below, we can see that for ``john@test.acme.com``, SFTPPlus
will create a folder in the home folder path.

The final path for this account is now ``c:\\ftp-files\\john``.

..  image:: /static/operation/windowsdomain-filesystem.png


Authenticating without any account configuration via DEFAULT_GROUP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For those setting up multiple accounts, they have the additional
option of using the `groups` configuration.

In this way, `groups` is used to configure the 'Missing home folder' section.

In the screenshot below, the missing home folder is configured so that the OS
account is the owner of this folder.

The account is then associated with this `group` in the Accounts section for
that particular account.

One item to note is that if the user configuration is missing and then this
`DEFALT_GROUP` is used.

..  image:: /static/operation/windowsdomain-homefolder-group.png


Troubleshooting Windows Domain authentication
---------------------------------------------

Should there be issues in authenticating, make sure to check the server logs
or the activity reports available in the Web Manager GUI.

For example, if the device has connectivity issues with the domain controller
(if the account is a domain controller account), there may be problems
authenticating the surrounding services that use it, such as SFTPPlus.
The issue may be transient, or if it's ongoing please check with the
administrator of the domain controller.

Another common error is to list the account's UUID as part of the
authentication method for the service that the account will
be using to transfer files (such as `ftp`).
This method should only be used for authentication UUID, not the account UUID.

If you are intending to use another type of authentication, such as an LDAP
bind, make sure that this authentication method UUID is added to the service.


Source IP address-based access
==============================

SFTPPlus source IP-based access is designed to augment the firewall rules.
For improved security and performance, it's recommended to setup both firewall and SFTPPlus source IP access rules.

The configuration examples from this section use accounts and groups to explain the source IP-based access.
The same configuration is used for administrators and roles.

Using a firewall, you can configure the networking layer to only allow connections to the file transfer service from a set of IP addresses.
Once a source IP is allowed by firewall rules, connections originating from that IP can be used by any available accounts/users.

Using the SFTPPlus account or group `source_ip_filter` rules,
you can restrict the access of a source IP to only a specific account or group.

The `source_ip_filter` rules can be used for 2 main purposes:

* Define the list of authorized account source IP addresses.
  This is done using the `source_ip_filter` configured directly at the account level.
* Define conditional group association for an account, based on the account source IP address.
  This is done at the group configuration level.

The rules define `deny` or `allow` actions.
They can be associated with a single IP or an IP range (using CIDR notation).

Multiple `deny` or `allow` rules can be defined to accommodate even the most complex requirements.

When defining the `source_ip_filter` rules the `ACTION IP-OR-CIDR` format is used.
There is an implicit order-based priority, the rules are applied from top to bottom.

The account's `source_ip_filter` defines the conditional source IP/CIDR allowed for authentication.

At the group level, the filtering defines the conditional source IP/CIDR for which the group is associated with the authenticating account.

..  warning::
    When implementing source IP based restrictions for accounts associated with multiple groups
    or administrators associated with multiple roles,
    the permissions should be designed using additive rules.

    Each group or role should add additional access permissions.

    They should not be designed to remove/restrict access to resources.
    If designed to remove/restrict access to resources and the source IP doesn't match a role or group,
    those restrictions will not be applied.


Account-level configuration
---------------------------

The `source_ip_filter` can be defined for the account's configuration.

For the following examples, there is no source IP filtering rule defined in the group associated with the account.
Further in this section, there are examples with source IP filtering rules defined at the group level.

When set with an empty value, no extra source IP restrictions are defined for the account.
The source IP rules defined in the associated groups will still apply.


In the example below, there is no `source_ip_filter` rule directly defined for the account.
There is a restriction for ``10.3.4.0/24`` IP range defined in the group.
This is why this account can only authenticate from a source IP within that range::

    [accounts/5432ca3-bbd5-9432-be31-b4318ddea4]
    name = john-d
    enabled = yes
    type = application
    description = Allow access from anywhere.
    group = 87dc321-87dc
    source_ip_filter =

    [groups/87dc321-87dc]
    name = sales-team
    enabled = Yes
    description = Allow association from anywhere.
    source_ip_filter = allow 10.3.4.0/24

When `source_ip_filter` is not empty, and the source IP of the connection does not match any rule, an implicit `deny` rule is applied as a fallback.

In the simplest configuration, exemplified below, the user is allowed access from a single IP address.
All IPs other than ``10.3.4.1`` are implicitly denied authentication::

    [accounts/5432ca3-bbd5-9432-be31-b4318ddea4]
    name = john-d
    enabled = yes
    type = application
    description = Allow access only from own VPN.
    group = 87dc321-87dc
    source_ip_filter = allow 10.3.4.1

    [groups/87dc321-87dc]
    name = sales-team
    enabled = Yes
    description = Allow association from anywhere.
    source_ip_filter =

In a slightly more complex configuration, the user is allowed to authenticate from a set of IP addresses.
All source IP addresses not matching the configured `allow` rules are implicitly denied authentication::

    [accounts/5432ca3-bbd5-9432-be31-b4318ddea4]
    name = john-d
    enabled = yes
    type = application
    description = Access from own VPN or internal network.

    source_ip_filter =
      allow 10.3.4.1
      allow 192.168.0.0/24

In a more complex configuration, the user is allowed from a single source IP address associated with a VPN client.
Any other IP address from the range allocated to the VPN is denied authentication.
At the same time, authentication from any other private or public IP address is allowed.
Below is an example in which `deny` and `allow` rules can be used with overlapping IP ranges.
There are two explicit rules at the end to allow any source IP not matched by any of the previous rules::

    [administrators/762dea-81bc-7321-ade3-9721134]
    name = jane-r
    enabled = yes
    type = application
    description = Access from own VPN, explicitly deny other VPN IPs
      and allow from anywhere else.

    source_ip_filter =
      allow 10.3.4.1
      deny 10.3.4.0/24
      allow 0.0.0.0/0
      allow ::/0


Single group inheritance
------------------------

Accounts don't have to define their own `source_ip_filter` rules.
Accounts can inherit the rules as defined in the associated groups.

Below is a simple example in which two accounts are associated with a single group.
The group has a simple configuration that allows any IP address from the ``10.23.0.0/24`` or ``172.27.0.0/16`` ranges.
Source IPs outside of these ranges are implicitly denied.
The semantic is similar to account-level configuration.
Multiple accounts can share the same source IP access list via the group association::

    [accounts/5432ca3-bbd5-9432-be31-b4318ddea4]
    name = john-d
    enabled = yes
    type = application
    group = 87dc321-87dc
    description = Sales team member without explicit IP filtering.
    source_ip_filter =

    [accounts/762dea-81bc-7321-ade3-9721134]
    name = jane-r
    enabled = yes
    type = application
    group = 87dc321-87dc
    description = Another team member without explicit IP filtering.
    source_ip_filter =

    [groups/87dc321-87dc]
    name = sales-team
    enabled = Yes
    description = Sales team can authenticate from the VPN and internal IP ranges.
    source_ip_filter =
      deny 10.23.0.1
      allow 10.23.0.0/24
      allow 172.27.0.0/16

Accounts ``john-d`` and ``jane-r`` are allowed from IPs such as ``10.23.0.173`` or ``172.27.3.21``,
but denied from any other IP, for example from ``10.23.0.1`` or ``35.12.4.142``.

The source IP filtering inheritance is implicit.
The account's `source_ip_filter` can be left empty.


Multiple group association
--------------------------

When the account is associated with multiple groups,
you can conditionally associate a group based on the account's source IP address.

In the example below, account ``john-d`` is associated either with the ``sales team``, when connecting from the IP range ``172.27.0.0/16``,
or with the ``support`` team, when connected from source IP ``10.2.2.0/24``.
Connections from other IP addresses are rejected for ``john-d``, as the account is associated with groups that only allow connections from defined IP ranges::

    [accounts/5432ca3-bbd5-9432-be31-b4318ddea4]
    name = john-d
    enabled = yes
    type = application
    group = 87dc321-87dc, be21982a-3423
    description = Account inheriting from multiple groups.
      There is no explicit IP filtering at account level configuration.
    source_ip_filter =

    [groups/87dc321-87dc]
    name = sales-team
    enabled = Yes
    description = Sales team authenticates from the VPN IP range.
    source_ip_filter =
      allow 192.168.124.0/16

    [groups/be21982a-3423]
    name = support-team
    enabled = Yes
    description = Support team authenticates from the internal IP range.
    source_ip_filter =
      allow 10.2.2.0/24


Account-specific filtering with multiple group association
----------------------------------------------------------

When the account is associated with multiple groups,
the source IP filtering rules for the associate groups are used.
However, the account can define its specific source IP access rules,
that take priority over the group rules.

In this case, the list of source IPs allowed for the groups is no longer used for the account authentication step.
The list of source IPs configured at the group-level are used only for controller the conditions under which the account is associated with that group.

In the example below, account ``john-d`` is associated with the ``sales team`` and the ``support team``.
The ``sales`` team allows connections from the IP range ``172.27.0.0/16``, representing the VPN range.
The ``support`` team allows connections from the source IP range ``10.2.2.0/24``, representing the internal IP range.
The account has an explicit source IP filter to allow authenticating only from the IP addresses allocated to this user.
Any other IP address is rejected for the account.

With this configuration, when the account connects from source IP ``192.168.124.23``,
it is associated with the ``sales`` team.
When connecting from source IP ``10.2.2.23``, the account is associated with both the ``support`` and the ``sales`` teams::

    [accounts/5432ca3-bbd5-9432-be31-b4318ddea4]
    name = john-d
    enabled = yes
    type = application
    group = 87dc321-87dc, be21982a-3423
    description = Account inheriting from multiple groups.
      There is no explicit IP filtering at account level configuration.
    source_ip_filter =
      allow 192.168.124.23
      allow 10.2.2.23

    [groups/87dc321-87dc]
    name = sales-team
    enabled = Yes
    description = Sales team can access from any VPN IP or internal range.
    source_ip_filter =
      allow 192.168.124.0/16
      allow 10.2.2.0/24

    [groups/be21982a-3423]
    name = support-team
    enabled = Yes
    description = Support team can access from internal IP range.
    source_ip_filter =
      allow 10.2.2.0/24


Auto-disabling inactive accounts
================================

An account can be configured to become disabled if no successful authentication was done in the last N days.

..  note::
    For this functionality to work the `Analytics engine` resource needs to be running.

This is done using the `disable_on_inactivity` configuration option.

The same configuration option is also available for group.
It will disable the accounts which are configured with the group as the primary group.

When an account is auto-disabled the event with ID 20195 is emitted to help audit the configuration change.

When the account was never successfully authenticated, the account creation date is considered as the last activity for that account.

If there is no record of a successful login and the account has no `created` configuration value,
the account is not auto-disabled.
Its creation time will be set to the current time
so that eventually it can be auto-disabled if not active.
An error event with ID 20196 is emitted.


Allowing users to change their password
=======================================

You can configure whether to allow file transfer users to change their own
password, or whether to have their password updated only by administrators.

Only application accounts defined inside SFTPPlus Web Manager can have
their password changed.

Operating system accounts, domain accounts, LDAP accounts, and other accounts
defined in external systems can't have their password changed via SFTPPlus.

When an account is allowed to change its password, it can do this using
the password update command available for each transfer protocol.

FTP/FTPS, SFTP/SCP, and HTTP/HTTPS protocols,
each have a different method to change the current user's password.
You can find more details about changing the password as part of the
operational documentation for each protocol / file transfer service type.

For example, in the following configuration we have user `johnd`, which can
change its own password, and user `billing-sap`, which can't change its
own password::

    [groups/2fd149b3-9fdb-49d0-8666-3c28f151f64d]
    name = partners
    enabled = Yes
    allow_own_password_change = Yes

    [groups/87dc321-87dc-aedf-1123-cd5328aef4]
    name = automation
    enabled = Yes
    allow_own_password_change = No

    [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
    name = johnd
    enabled = yes
    type = application
    group = 2fd149b3-9fdb-49d0-8666-3c28f151f64d
    description = Account used by John Doe from ACME Inc to push reports.

    [accounts/5432ca3-bbd5-9432-be31-b4318ddea4]
    name = billing-sap
    enabled = yes
    type = application
    group = 87dc321-87dc-aedf-1123-cd5328aef4
    description = Account used by billing automation system to pull reports.


Disabling all users from a group
================================

The `Enabled` configuration option for a group, affects the state of
all users from that group.

For example, the following configuration will disable access to any account
from the ``partners`` group, while the accounts from the ``accounting`` group
will have access granted based on the account's configuration::

    [groups/0a3f3aa7-50d2-44ef-9456-4f0beb69cf7d]
    name = accounting
    enabled = Yes

    [groups/804aab78-70c0-4e1d-8480-4979e169a0a2]
    name = partners
    enabled = No

While a group is enabled, specific accounts can be disabled by setting the
``enabled`` property for the specific account.

.. _inherited-home-folder-path:


Inherited Home Folder Path and Authorized SSH Keys File
=======================================================

The `home_folder_path` and `ssh_authorized_keys_path` configuration options
for a group may contain the `${USER}` placeholder which will be replaced with
the name for each account.
If the value for this option does not contain `${USER}`, the home folder
will be a sub-folder of the configured path.

For example, in the following configuration::

    [groups/2fd149b3-9fdb-49d0-8666-3c28f151f64d]
    name = partners
    enabled = Yes
    home_folder_path = /home/${USER}/reports

    [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
    name = john
    enabled = yes
    type = application
    group = 2fd149b3-9fdb-49d0-8666-3c28f151f64d
    home_folder_path = Inherited

The `home_folder_path` for account ``john`` will be mapped as
``/home/john/reports``.


Exception in home folder path resolution
----------------------------------------

SFTPPlus allows defining accounts with usernames containing any character.
When translating a username into a folder name there are certain restriction,
due to the low level filesystem provided by the operating system.

This is why, when a username contains any of these characters ``\/:*?"<>|``,
SFTPPlus will replace them with ``.`` (dot).

In this way it will not generate invalid path on Windows.
It will also make things easier when migrating between a Windows and
a Unix-like system.


Configuration without the ${USER} placeholder
---------------------------------------------

If the `home_folder_path` defined for a group does not contain the
`${USER}` placeholder, the account name will be appended to the path
defined by the `home_folder_path`.
For example, in the following configuration::

    [groups/2fd149b3-9fdb-49d0-8666-3c28f151f64d]
    name = partners
    enabled = Yes
    home_folder_path = c:\Users

    [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
    name = john
    enabled = yes
    type = application
    group = 2fd149b3-9fdb-49d0-8666-3c28f151f64d
    home_folder_path = Inherited

The `home_folder_path` for account ``john`` will be mapped as
``c:\\Users\\john``.

For groups, setting `home_folder_path` to ``c:\\Users`` has the same effect
as setting it to ``c:\\Users\\${USER}``.
When the `${USERS}` placeholder is
not used, it is automatically appended to the group's home folder path.


Home Folder Path for Windows Domain Accounts
--------------------------------------------

For Windows Domain accounts, the ``@`` character is replaced with the ``.``
character.
In the following example,
the `home_folder_path` for Windows Domain account ``ben@dc-domain.tld``
will be mapped as ``c:\\Users\\ben.DC-DOMAIN.TLD``::

    [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f5]
    name = ben@dc-domain.tld
    enabled = yes
    type = os
    group = 2fd149b3-9fdb-49d0-8666-3c28f151f64d
    home_folder_path = Inherited


Account setup for anonymous authentication
==========================================

In Accounts, create an account of type `Application Account`.  Since it is
used for anonymous authentication, choose a relevant name.
Configure its home folder.

In Authentications, ensure that anonymous authentication is defined/enabled.
Edit the account's method configuration and select a user to be mapped to the
anonymous account.
This user will be the account that was recently created in the first paragraph
of this section.

Go to the Status page and double check that the anonymous authentication method
referred to above is running (started).

If not, manually start it.


To restrict anonymous authentication to a particular service:
-------------------------------------------------------------

In the Server page, make a note of all existing UUIDs in the Authentications
field.

In the Status page, select to edit select to edit the configuration of the
service you want to allow the anonymous account to.

Add all the UUIDs that are already used globally including the UUID
from the anonymous authentication.


To allow/enable anonymous authentication in any service:
--------------------------------------------------------

In the Server page, add the UUID of the authentication method to the
Authentications list.

To locate this UUID, go to the Authentications page,
select the anonymous authentication method and copy the Identifier string.

Run a test on the service to ensure the new settings are applied.

The following events represent a successful anonymous authentication:

    | 20137 2016-12-13 14:23:29 test-server-uuid Unknown 127.0.0.1:4831 Account
      "user" of type "application" authenticated as "anonymous" by anonymous
      authentication "auth-anonymous" using password.
