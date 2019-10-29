.. container:: tags pull-left

    `server-side`
    `security`
    `authentication`


Integrating with an LDAP Server
###############################

..  contents:: :local:


Basic Operation
===============

To perform a successful authentication, SFTPPlus will connect to the LDAP
server, BIND the connection to validate the credentials, retrieve the LDAP
entry for the same DN (distinguished name) used to bind the connection and then
close the connection.

Empty passwords, or passwords containing only space or tab characters are
rejected by SFTPPlus right away and are not forwarded to the LDAP server.

You can use an LDAP server to authentication file transfer service accounts,
as well as Local Manager service administrators.

Even if SFTPPlus supports SSH-key or SSL/X.509 certificate based
authentication, when using the LDAP authentication method, only
username/password credentials are supported.
This is due to the limitation in the LDAP protocol.

The main aspect which needs to be configured is mapping the simple `username`
provided as part of the file transfer protocol authentication step to the
DN used by LDAP.
This is done using the `bind_dn` and the `username_attribute` configuration
options.

Using the following `bind_dn` configuration::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    bind_dn = dc=example,dc=com
    username_attribute = cn

The FTP authentication step will translate the `username` ``John`` into::

    cn=John,dc=example,dc=com

An FTP authentication session for ``John`` will look like this::

    $ ftp ftp.server.example.com 21
    Connected to ftp.server.example.com.
    220 (SFTPPlus_VER) Welcome to the FTP server.
    Name: John
    Password: *****

Successfully authenticated file transfer accounts are associated to the
default group.

Successfully authenticated administrator accounts are associated to the
default role.


Retrieving the configuration for a username
===========================================

Once the account is authenticated, SFTPPlus will perform a search on LDAP
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

An FTP authentication session using type `absolute` will look like this::

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


An FTP authentication session using type `relative` will look like this::

    $ ftp uit.example.com 10023
    Connected to uit.example.com.
    220 Welcome to the FTP Service.
    Name: cn=john,ou=det
    Password: *****

This will perform the LDAP BIND using DN - cn=john,ou=det,dc=example,dc=com


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

With this method, only usernames in UPN format are supported.
Down-Level Logon Name is not supported.

Using this method has a small performance penalty, as without knowing the
full DN of the targeted account, SFTPPlus will need to search the LDAP tree
withing all the available accounts.

SFTPPlus can be configured to allow only users from a specific
`Organization Unit` and only using the LDAP name, and not the UPN username::

    [authentications/f691a41b-0eca-4135-8369-5b9f2600ebd6]
    bind_dn_type = parent
    bind_dn = OU=sales,OU=eu,dc=example,dc=com
    username_attribute = cn

An FTP authentication session for DN
``CN=john_doe,OU=sales,OU=eu,dc=example,dc=com``
using just the LDAP CN looks like::

    $ ftp uit.example.com 10023
    Connected to uit.example.com.
    220 Welcome to the FTP Service.
    Name: john_doe
    Password: *****

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


Enable access to the Local Manager service
==========================================

While the LDAP server holds all the accounts for your organization,
most probably only a few of those accounts should get **administration** access
to the Local Manager services.

By default, SFTPPlus will not allow administration accounts to the LDAP
account.

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

Without any explicit configuration, SFTPPlus will associate any LDAP account
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

The first line will contain the fallback group
which is used when there is no match on any of the other rules.
The other lines are defined as comma separated lines of 3 elements.
The first element is the name of the LDAP attribute.
The second element is the value of the LDAP attribute
which can be matched based on a strict value (case insensitive),
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
it will be associated with the SFTPPlus group with UUID `e232-ad2a-db3c`.
The group for `operationalUnit` is not matched as `memberOf` is defined
first and SFTPPlus will use that::

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

The matching rules are executed from top-down and will stop at the
first match.

When the entry has none of the attributes used for matching,
the fallback group is used.

When the LDAP entry for the account has multiple values for the same
LDAP attributes used as part of group mapping expression, and multiple
values matches multiple group mapping expression, then the exact result may
different based on the LDAP server implementation.
