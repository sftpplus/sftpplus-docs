.. container:: tags pull-left

    `server-side`
    `security`
    `authentication`


Integrating with an LDAP Server
###############################

..  contents:: :local:


Basic Operation
===============

To perform a successful authentication, SFTPPlus connects to the LDAP
server, BINDs the connection to validate the credentials, retrieves the LDAP
entry for the same DN (distinguished name) used to bind the connection,
and then closes the connection.

Empty passwords, or passwords containing only space or tab characters are
rejected by SFTPPlus right away and are not forwarded to the LDAP server.

You can use an LDAP server to authenticate file transfer service accounts,
as well as Local Manager service administrators.

Although SFTPPlus supports SSH key-based or SSL/X.509 certificate-based
authentication, these are not supported by the LDAP authentication method
due to limitations of the LDAP protocol.

The main aspect which needs to be configured is mapping the simple `username`
provided as part of the file transfer protocol authentication step to the
DN used by LDAP.
This is done using the `bind_dn` and the `username_attribute` configuration
options.

Using the following `bind_dn` configuration::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    bind_dn = dc=example,dc=com
    username_attribute = cn

The FTP authentication step translates the `username` ``John`` into::

    cn=John,dc=example,dc=com

An FTP authentication session for ``John`` looks like this::

    $ ftp ftp.server.example.com 21
    Connected to ftp.server.example.com.
    220 (SFTPPlus_VER) Welcome to the FTP server.
    Name: John
    Password: *****

Successfully authenticated file transfer accounts are associated to the
default group.

Successfully authenticated administrator accounts are associated to the
default role.


Security considerations
=======================

When integrating SFTPPlus authentication with an LDAP server, we assume
end users only have at most read-only access to their LDAP account data
used for SFTPPlus operations.
For example, the home folder path attribute or the attributes used to
select the group membership.

With direct write access to LDAP, a user can modify their LDAP
attributes used by SFTPPlus to enforce access and permissions, therefore
bypassing the security measures defined in SFTPPlus.

..  danger::
    The security of the LDAP authentication method in SFTPPlus is compromised
    when end users have direct write access to the LDAP server.

    Having at most read-only access is appropriate.


Retrieving the configuration for a username
===========================================

Once the account is authenticated, SFTPPlus performs a search on LDAP
to retrieve the home folder for the account.

The `home_folder_attribute` configuration option can be used to specify with
LDAP attribute is used to store the home folder path.


Absolute DN as username
=======================

You can have SFTPPlus authenticate against LDAP with the full DN as the
username.

On the server-side, the only configuration needed is::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    bind_dn_type = absolute

An FTP authentication session using type `absolute` looks like this::

    $ ftp uit.example.com 10023
    Connected to uit.example.com.
    220 Welcome to the FTP Service.
    Name: cn=john,ou=det,dc=example,dc=com
    Password: *****


Relative DN as username
=======================

When users accessing file transfer services are located in different
branches of the LDAP tree, you can have accounts authenticated only with
a fragment of the complete DN.

On the server-side the only configuration needed is to set::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    bind_dn_type = relative
    bind_dn = dc=example,dc=com


An FTP authentication session using type `relative` looks like this::

    $ ftp uit.example.com 10023
    Connected to uit.example.com.
    220 Welcome to the FTP Service.
    Name: cn=john,ou=det
    Password: *****

This performs the LDAP BIND using DN - cn=john,ou=det,dc=example,dc=com


Active Directory Integration
============================

An Active Directory LDAP server can be used in the same way as any standard
LDAP server.

Since the AD LDAP server supports LDAP BIND operation using the BIND DN in
the UPN format, you can configure SFTPPlus to accept UPN as username
for a seamless experience for clients.

On the server-side, you need to enable the following configuration.
The `bind_dn` is required to let SFTPPlus know from where to retrieve
the accounts' configuration, and `username_attribute` informs which
LDAP entry is associated with the authenticated account::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    bind_dn_type = direct-username
    bind_dn = cn=Users,dc=ad,dc=example,dc=com
    username_attribute = userPrincipalName

An FTP authentication session using the UPN as username looks like::

    $ ftp uit.example.com 10023
    Connected to uit.example.com.
    220 Welcome to the FTP Service.
    Name: john.doe@ad.example.com
    Password: *****

With this method, only usernames in UPN format (user@sub.domain.com)
are supported.
Down-Level Logon Name (USER\DOMAIN) is not supported.

..  warning::
    The Active Directory user logon name can be found inside the
    "Properties" windows on the "Account" tab.
    The AD login is not the same value as the "Display name" or the name
    visible in the Users lists from the "Active Directory Users And Computers"
    application.

..  note::
    Using this method has a small performance penalty, as without knowing the
    full DN of the targeted account, SFTPPlus needs to search the LDAP tree
    withing all the available accounts.

--------

You can also have Active Directory connecting via the UPN name but without
an explicit domain name::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    bind_dn_type = direct-username
    bind_dn = cn=Users,dc=ad,dc=example,dc=com
    username_attribute = userPrincipalName
    username_suffix = @ad.example.com


An FTP authentication session using username without the domain name
looks like::

    $ ftp uit.example.com 10023
    Connected to uit.example.com.
    220 Welcome to the FTP Service.
    Name: john.doe
    Password: *****

-------

If UPN usernames are used for the authentication of users from a specific
`Organization Unit`,
the configuration should look like the following example::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    bind_dn_type = direct-username
    bind_dn = OU=sales,OU=eu,dc=example,dc=com
    username_attribute = userPrincipalName


Selective access to the file transfer services
==============================================

While the LDAP server holds all the accounts for your organization,
it might be the case that only a few of those accounts should get access
to the file transfer services.

Using the LDAP filter, you can allow access only to those accounts which
satisfy the search criteria.

For example, to only allow access to users from the ``file-transfer`` group,
you can use the following configuration::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    search_filter = (memberOf=file-transfer)


Advanced configuration for home directory path
==============================================

The LDAP authentication method can be configured to define the user home
folder path based on a configured template augmented with the the LDAP
attribute value.

For example, when LDAP server contains only the partial path to the home
directory, you can configure SFTPPlus to expand the path using the following
configuration.
This is useful when migrating from Microsoft IIS server where the path
is stored in the `msIIS-FTPDir` LDAP attribute::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    bind_dn_type = direct-username
    bind_dn = cn=Users,dc=ad,dc=example,dc=com
    username_attribute = userPrincipalName
    username_suffix = @ad.example.com
    home_folder_attribute = msIIS-FTPDir, e:\SFTP-Files\{msIIS_FTPDir}

For a user with `msIIS-FTPDir: \\AcmeCo\\report`, once authenticated,
the home folder is `E:\\SFTP-Files\\AcmeCo\\report`.

..  note::
    For LDAP attributes containing a dash (-), the dash character is replaced
    with an underscore (_) character in the expression used to define the
    full home path.


Enable access to the Local Manager service
==========================================

While the LDAP server holds all the accounts for your organization,
most probably only a few of those accounts should get **administration** access
to the Local Manager services.

By default, SFTPPlus does not allow mapping administration accounts to LDAP
accounts.

Using the LDAP filter, you can allow access only to those accounts which
satisfy the search criteria.

For example, to only allow access to users from the
``file-transfer-admins`` group, you can use the following configuration::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    manager_search_filter = (memberOf=file-transfer-admins)


SFTPPlus Group Mapping without extra LDAP attributes
====================================================

In SFTPPlus, you can associate an account of which the configuration is stored
in LDAP,
to groups for which the configuration is stored in SFTPPlus.
This can be done without adding any extra LDAP attributes to the existing
LDAP entries.

In this way you, can augment the LDAP database with SFTPPlus specific
configuration and a scalable configuration by the way of the inherited
configuration options.

Without any explicit configuration, SFTPPlus associates any LDAP account
with the default SFTPPlus group.
This is a single group, used by default for any authentication method.

For the most basic configuration, you can specify a single SFTPPlus group UUID,
and all the accounts from LDAP are associated with that group.
The group configuration is managed and stored inside SFTPPlus.

For complex configurations, you can associate different SFTPPlus groups to
LDAP accounts based on the values of existing attributes.

Below is a basic configuration syntax::

    group_mapping =
        FALLBACK-GROUP-UUID
        ldapAttributeName, MATCHING_EXPRESSION, GROUP-UUID


A set of group mapping / group association rules are defined,
each rule having 3 components:

* ldapAttributeName - this is the exact name of an LDAP attribute which is
  associated with the LDAP account
* MATCHING_EXPRESSION - this is an exact value of the LDAP attribute,
  a globbing expression or regular expression.
* GROUP-UUID - this is the UUID of a group of which configuration is stored
  and managed by SFTPPlus.

For more details, see the :doc:`matching expression
documentation</configuration/matching-expression>`.

The first line contains the fallback group
which is used when there is no match on any of the other rules.
The other lines are defined as comma separated lines of 3 elements.
The first element is the name of the LDAP attribute.
The second element is the value of the LDAP attribute
which can be matched based on a strict value (case-insensitive),
globbing or on regular expressions.
The third element is the UUID of the SFTPPlus group which should
be associated on a match.

Here is an example::

    [authentications/d87d-4a3c-d732]
    type = ldap
    name = Authenticate from LDAP

    group_mapping =
        987d-54da-db3c
        memberOf, *-apac-*, 54ae-987d-09ff
        operationalUnit, m/sales-force-[1-3]/, 8fde-54da-00aa

When an LDAP entry with the following LDIF is successfully authenticated,
it gets associated with the SFTPPlus group with UUID `e232-ad2a-db3c`.
The group for `operationalUnit` is not matched because `memberOf` is defined
first, and SFTPPlus uses that::

    dn: cn=bob,ou=people,dc=example,dc=com
    uid: bob
    cn: bob
    objectclass: top
    objectclass: person
    objectClass: inetOrgPerson
    homeDirectory: /archive/bob
    operationalUnit: sales-force-2
    memberOf: sales-apac-oceania
    memberOf: syadmin

The matching rules are executed in a top-down fashion, stopping at first match.

When the entry has none of the attributes used for matching,
the fallback group is used.

When the LDAP entry for the account has multiple values for the same
LDAP attributes used as part of group mapping expression, and multiple
values matches multiple group mapping expression, then the exact result may
different based on the LDAP server implementation.


TOTP Multi-Factor Authentication integrations with LDAP servers
===============================================================

SFTPPlus can authenticate an LDAP-based account using
a password and a TOTP code.

For example, a TOTP authentication session via FTP,
where ``SecretPass`` is the password and ``123456`` is the TOTP code,
looks like this::

    $ ftp uit.example.com 10023
    Connected to uit.example.com.
    220 Welcome to the FTP Service.
    Name: john.doe
    Password: SecretPass123456

As you can see above, the end user interaction is the same,
regardless of the low-level details of the LDAP TOTP implementation.
FTP clients only have to append the TOTP code to the actual password.

In this way, the TOTP end user experience can be integrated with any FTP/SFTP
client or process, even if the FTP/SFTP client-side software has no dedicated
support for TOTP.

Below we describe a few LDAP MFA deployment scenarios.


LDAP servers with native TOTP support
-------------------------------------

When deploying a TOTP-based multi-factor authentication through LDAP,
the ideal scenario is for your LDAP server to provide native support for
TOTP authentication.

In this scenario, SFTPPlus does not handle any part of the TOTP process,
other than just forwarding the provided username and password to the LDAP
server.

The LDAP server processes the provided username and password/code combination,
separating the actual password from the ephemeral TOTP code appended to it.

..  note::
    You don't need to use the `multi_factor_authentication_attribute`
    configuration option in this scenario.


LDAP servers with external TOTP support script
----------------------------------------------

If your LDAP server does not provide native TOTP support,
you can try enhancing your LDAP server with TOTP capabilities
by storing the password and the TOTP shared secret for each user in a separate
database.

Depending on the used TOTP parameters, every 30 seconds, a script should
then update the current LDAP password combining the actual original password
with the valid TOTP code for the current time.

In this scenario, end users can still have read-only access to the LDAP server
without any security issues,
as the TOTP shared secrets and plain text passwords are not stored on the
LDAP server.


LDAP servers with SFTPPlus TOTP support
---------------------------------------

If none of the scenarios described above are feasible,
you can configure SFTPPlus to delegate TOTP authentication.

Your LDAP server should handle the username + password authentication,
then SFTPPlus continues the authentication process to validate the
TOTP code.

.. note::
    The scenario described in this section only implements TOTP for
    SFTPPlus' authentication.
    It doesn't add TOTP support to your LDAP server.

To implement this scenario, you have to generate the TOTP shared secret
outside of the LDAP and SFTPPlus servers.

Once a TOTP shared secret is generated for a user, that value is stored in
their corresponding LDAP entry using an attribute name of your choice.
For the purpose of this documentation, we assume the TOTP shared
secret is stored using a ``totpSharedSecret`` LDAP attribute.

The SFTPPlus Authentication method can then configured as follows::

    [authentications/d87d-4a3c-d732]
    type = ldap
    name = Authenticate from LDAP

    multi_factor_authentication_attribute = totpSharedSecret

An example of LDIF data for a user's entry on the LDAP server::

    dn: cn=bob,ou=people,dc=example,dc=com
    uid: bob
    cn: bob
    objectclass: top
    objectclass: person
    objectClass: inetOrgPerson
    homeDirectory: /users/bob
    memberOf: sales-apac-oceania
    totpSharedSecret: otpauth://totp/Srv:admin?secret=TOTP_SEED&issuer=Srv

For security considerations, the end user must not be able to get access to
its ``totpSharedSecret`` LDAP attribute, for example via an LDAP connection.
However, the ``totpSharedSecret`` LDAP attribute should still be readable
from SFTPPlus through an LDAP connection.

..  danger::
    This scenario should not be deployed when end users have direct read access
    to their data in the LDAP server.
    With unrestrained access, an end user can bypass TOTP authentication
    by following these steps:

    1. The end user initiates an LDAP username and password authentication
       directly to the LDAP server.
    2. Upon successful authentication, the TOTP shared secret code is
       retrieved from the LDAP server by the end user.
    3. The end user can now authenticate to SFTPPlus
       using the username + password + a TOTP code
       computed based on the shared secret retrieved in the previous step.
    4. SFTPPlus accepts the authentication as it has both a valid password
       and a valid TOTP code.

    As demonstrated above,
    all that was needed from an end user to perform a successful authentication
    was a valid username and password, degrading a multi-factor authentication
    into a **one factor** authentication process.

    At the same time, a malicious actor could inspect the network trafic of
    an unencrypted FTP connection to retrieve the username and password+code
    used during an FTP authentication session.
    Even though a TOTP-enabled SFTPPlus doesn't allow reusing the same username
    and password+code, the malicious actor can generate new valid TOTP codes
    if the TOTP secret can be retrieved from the LDAP server as shown above.
