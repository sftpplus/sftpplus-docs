Azure Active Directory
======================

The `azure-ad` method is used to implement single sign-on authentication based on the Azure Active Directory service.

..  contents:: :local:


Introduction
------------

To integrate SFTPPlus with the online Azure Active Directory,
you will need to set the Azure AD details in SFTPPlus,
and the SFTPPlus ones in the Azure AD configuration.
In this way, SFTPPlus and Azure AD will be aware of each other and will work together.

Azure AD provides both authentication and authorization processes.
For SFTPPlus integration, Azure AD is primarily used for authentication.
You will define the authorization rules inside the SFTPPlus configuration.
It is recommended to configure the Azure AD authentication method as the first method in your authentication chain,
before the `SFTPPlus Application Accounts` authentication.

The Azure AD *authentication* process handles identifying and validating the access from an account/user/person.
The SFTPPlus *authorization* process handles the set of file access permissions for the authenticated user.

..  note::
    Only Azure AD public cloud is supported for now.
    If you use Azure cloud for US Gov, China, or Germany get in touch with us for more information.

From Azure AD you can configure it to allow authentication for all Azure AD users,
for an explicit set of Azure AD users,
or only for Azure AD users that are associated with SFTPPlus groups having the same name as the Azure AD security group.

SFTPPlus will always ask to confirm the selected Azure AD user for authentication.
Get in touch if you would like SFTPPlus to automatically use the active Azure AD user without a prompt.

When the user signs out (logout) from SFTPPlus only the SFTPPlus session is finalized.
The Azure AD authentication session is kept and the user is not automatically signed out from Azure AD.
This allows the user to access SFTPPlus without entering the password again.
Also, if the user is already signed in to Azure AD,
authenticating to SFTPPlus will not trigger a new Azure AD authentication process.
Some extra authentication steps might be required, depending on your security policy.
For example, you might need to confirm a multi-factor authentication request.

The Azure AD authentication process should finalize in less than 2 minutes.
For security reasons, SFTPPlus will reject delayed authentication requests.

For SFTPPlus to integrate with the Azure AD authentication,
it needs to be able to initiate **outgoing connections** to the Microsoft/Azure Cloud over HTTPS port 443.
Make sure your firewall allows outgoing connections.
An HTTP proxy can be used by SFTPPlus to connect to the Azure Cloud.
Below is the list of services used by SFTPPlus to communicate with Azure Cloud:

* login.microsoftonline.com
* graph.microsoft.com


..  note::
    Only HTTPS file transfer user authentication is supported.
    Get in touch if you need to authenticate SFTP users, FTPS users, or administrators using Azure AD.


Azure AD app configuration
--------------------------

Besides defining the Azure AD authentication method inside the SFTPPlus configuration,
you will also need to define SFTPPlus inside your Azure AD directory.

Start by adding SFTPPlus to your Azure AD, by using the `App registrations` page from Azure.

SFTPPlus interacts with Azure AD as an OpenID Connect and OAuth2 application.

Use `New registration`, define a name (ex SFTPPlus) and select `Single tenant`.

`Redirect URI` is required for SFTPPlus operation. Select `Web` and define the URL using the following format,
where `SERVER:PORT` will be replaced with the address for your HTTPS web file browser,
and `AUTH-UUID` with the unique ID of this authentication method:
`https://SERVER.COM:PORT/__chsps__/login?redirect-AUTH-UUID`

..  note::
    Only single-tenant authentication is supported.
    Only a single Azure AD authentication method can be enabled for one HTTPS file transfer server.
    When multiple Azure AD authentications are defined, only the first one is used.
    Get in touch if you need support for multitenant or personal Microsoft accounts.

Once the SFTPPlus application is registered inside Azure you can optionally configure the logout URL.
From `Essentials -> Redirect URIs`, define the front-channel logout URL:
`https://SERVER.COM:PORT/__chsps__/logout`

No application secret is required.
SFTPPlus will use the Azure public keys to validate the ID and access tokens.

From the Azure AD App registrations `Authentication` page,
the following options need to be enabled to allow the SFTPPlus to authenticate the Azure AD users.
From the `Implicit grant and hybrid flows` section:

* Access tokens (used for implicit flows)
* ID tokens (used for implicit and hybrid flows)

To associate Azure AD groups with SFTPPlus groups, the `Directory.Read.All` API permissions will be requested.
No explicit `API permissions` configuration is required.
Azure AD will ask each user to confirm the permissions.

For manual configuration, the following API permissions are required.
All permissions are `Delegated`:

* openid - for generic authentication
* User.Read - for generic authentication
* Directory.Read.All - Delegated (for Azure AD group association)

Other configuration options are available in Azure AD via the `Enterprise applications` page.
On the `Enterprise applications -> Properties` you can configure a general 'Enable/Disable' option for the SFTPPlus application.
`Assignment required?` configuration is important and it defines whether access to SFTPPlus
is allowed by default to all your Azure AD users, or you need to grant explicit access to SFTPPlus for Azure AD users.

From the `Enterprise applications -> Users and groups` page, you can grant explicit access to SFTPPlus to your Azure AD users.


.. include:: /configuration-auth/authentication-commons.include.rst


directory_id
------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 4.22.0
:Description:
    Directory (tenant) ID of the SFTPPlus inside the Azure AD.
    This value can be viewed after registering SFTPPlus in Azure AD via the `App registrations` page.


application_id
--------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 4.22.0
:Description:
    Application (client) ID of the SFTPPlus inside the Azure AD.
    This value is obtained after registering SFTPPlus in Azure AD via the `App registrations` page.


base_groups
-----------

:Default value: Empty
:Optional: yes
:Values: * Empty
         * Group UUID.
         * Comma-separated list of group UUIDs.
:From version: 4.22.0
:Description:
    Defines the SFTPPlus groups that are associated with any authenticated users.

    Leave empty to not have any default group and only use the groups associated via Azure AD.

    The first configured base group is also the primary group.


group_association
-----------------

:Default value: `base-groups`
:Optional: No
:Values: * `base-groups`
         * `base-and-azure-groups`
:From version: 4.22.0
:Description:
    Defines the SFTPPlus groups that are associated with authenticated users.

    When set to `base-groups`, it will associate any Azure AD user with the
    list of groups configured via the `base_groups` configuration option.

    When set to `base-and-azure-groups`,
    it will associate the user with the list of groups defined via the `base_groups` option
    and the SFTPPlus groups having the same name as the Azure AD security groups that this user is a member of.
    If the user is associated with Azure AD groups not configured on SFTPPlus, those groups are ignored.
    If no Azure AD groups are found for this user, only the base groups are used.
    If the authenticated user has no associated SFTPPlus group in Azure AD and `base_groups` is empty, the authentication fails.
    The Azure AD groups are associated with SFTPPlus groups if they have the same name.
    The matching is case-sensitive.


proxy
-----

:Default value: ''
:Optional: Yes
:Values: * `URI` like expression.
         * `connect://12.342.421.2:3128`
:From version: 4.23.0
:Description:
    This configures the proxy used by SFTPPlus to connect to the cloud services required by Azure AD.

    For now, only the HTTP/1.1 CONNECT tunneling proxy method is supported.


remove_username_suffix
----------------------

:Default value: Empty
:Optional: Yes
:Values: * Text
         * Multiple values, one value per line.
:From version: 4.23.0
:Description:
    Suffix of the Azure AD username to be removed by SFTPlus when generating the username used for file transfer operations.

    You can configure SFTPPlus to remove multiple suffixes.
    Define each suffix that should be removed on a separate line.
    The first suffix matching the Azure AD username is used,
    while the remaining are ignored.

    For example, if the Azure AD username is ``Jane.R@sftpplus.onmicrosoft.com``,
    and you want SFTPPlus to handle the user as Jane.R, you can configure
    this as ``remove_username_suffix = @sftpplus.onmicrosoft.com``.
