Microsoft Entra ID
==================

..  contents:: :local:


Introduction
------------

The `entra-id` method is used to implement single sign-on authentication based on the Microsoft Entra ID service.

To integrate SFTPPlus with Entra ID,
you need to configure the Entra ID details in SFTPPlus,
and the SFTPPlus ones in the Entra ID configuration.
In this way, SFTPPlus and Entra ID are aware of each other and can work together.

Entra ID provides both authentication and authorization processes.
For SFTPPlus integration, Entra ID is primarily used for authentication.
You will define the authorization rules inside the SFTPPlus configuration.
It is recommended to configure the Entra ID authentication method as the first method in your authentication chain,
before the `SFTPPlus Application Accounts` authentication.

The Entra ID *authentication* process handles identifying and validating the access from an account/user/person.
The SFTPPlus *authorization* process handles the set of file access permissions for the authenticated user.

..  note::
    When using the Entra ID authentication with SFTPPlus running behind a reverse proxy or an API gateway,
    make sure one of the following headers is set by your proxying setup:
    `X-Forwarded-Proto`, `X-Forwarded-Host`, `X-Forwarded-For`, or the `Forwarded` headers.
    When using the `X-Forwarded-Host` header, make sure it contains the port number in its value.

..  note::
    Only Entra ID public cloud is supported for now.
    If you use Azure cloud for US Gov, China, or Germany get in touch with us for more information.

From Entra ID you can configure it to allow authentication for all Entra ID users,
for an explicit set of Entra ID users,
or only for Entra ID users that are associated with SFTPPlus groups having the same name as the Entra ID security group.

SFTPPlus will always ask to confirm the selected Entra ID user for authentication.
Get in touch if you would like SFTPPlus to automatically use the active Entra ID user without a prompt.

When the user signs out (logout) from SFTPPlus only the SFTPPlus session is finalized.
The Entra ID authentication session is kept and the user is not automatically signed out from Entra ID.
This allows the user to access SFTPPlus without entering the password again.
Also, if the user is already signed in to Entra ID,
authenticating to SFTPPlus will not trigger a new Entra ID authentication process.
Some extra authentication steps might be required, depending on your security policy.
For example, you might need to confirm a multi-factor authentication request.

The Entra ID authentication process should finalize in less than 2 minutes.
For security reasons, SFTPPlus will reject delayed authentication requests.

For SFTPPlus to integrate with the Entra ID authentication,
it needs to be able to initiate **outgoing connections** to the Microsoft/Azure Cloud over HTTPS port 443.
Make sure your firewall allows outgoing connections.
An HTTP proxy can be used by SFTPPlus to connect to the Azure Cloud.
Below is the list of services used by SFTPPlus to communicate with Azure Cloud:

* login.microsoftonline.com
* graph.microsoft.com

..  note::
    Only HTTPS file transfer user authentication and web management console are supported.
    Get in touch if you need to authenticate SFTP or FTPS users using Entra ID.


Entra ID app configuration
--------------------------

Besides defining the Entra ID authentication method inside the SFTPPlus configuration,
you will also need to define SFTPPlus inside your Entra ID directory.

Start by adding SFTPPlus to your Entra ID, by using the `App registrations` page from Azure.

SFTPPlus interacts with Entra ID as an OpenID Connect and OAuth2 application.

Use `New registration`, define a name (ex SFTPPlus) and select `Single tenant`.

`Redirect URI` is required for SFTPPlus operation. Select `Web` and define the URL using the following format,
where `SERVER:PORT` will be replaced with the address for your HTTPS web file browser,
and `AUTH-UUID` with the unique ID of this authentication method:
`https://SERVER.COM:PORT/?redirect-AUTH-UUID`

..  note::
    Only single-tenant authentication is supported.
    Only a single Entra ID authentication method can be enabled for one HTTPS file transfer server.
    When multiple Entra ID authentications are defined, only the first one is used.
    Get in touch if you need support for multi-tenant or personal Microsoft accounts.

`Client credentials` of type `client secret` is required to identity the SFTPPlus application to identify itself to the Entra ID authentication server.

Once the SFTPPlus application is registered inside Azure you can optionally configure the logout URL.
From `Essentials -> Redirect URIs`, define the front-channel logout URL:
`https://SERVER.COM:PORT/__chsps__/logout`

SFTPPlus will use the Azure public keys to validate the ID and access tokens.

From the Entra ID App registrations `Authentication` page,
the following options need to be enabled to allow the SFTPPlus to authenticate the Entra ID users.
From the `Implicit grant and hybrid flows` section:

* Access tokens (used for implicit flows)
* ID tokens (used for implicit and hybrid flows)

To associate Entra ID groups with SFTPPlus groups, the `GroupMember.Read.All` API permissions will be requested.
No explicit `API permissions` configuration is required.
Entra ID will ask each user to confirm the permissions.

For manual configuration, the following API permissions are required.
All permissions are `Delegated`:

* openid - for generic authentication
* User.Read - for generic authentication
* GroupMember.Read.All - Delegated (for Entra ID group association)

Other configuration options are available in Entra ID via the `Enterprise applications` page.
On the `Enterprise applications -> Properties` you can configure a general 'Enable/Disable' option for the SFTPPlus application.
`Assignment required?` configuration is important and it defines whether access to SFTPPlus
is allowed by default to all your Entra ID users, or you need to grant explicit access to SFTPPlus for Entra ID users.

From the `Enterprise applications -> Users and groups` page, you can grant explicit access to SFTPPlus to your Entra ID users.


.. include:: /configuration-auth/authentication-commons.include.rst


directory_id
------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 4.22.0
:Description:
    Directory (tenant) ID of the SFTPPlus inside the Entra ID.
    This value can be viewed after registering SFTPPlus in Entra ID via the `App registrations` page.


client_id
---------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 4.22.0
:Description:
    Application (client) ID of the SFTPPlus inside the Entra ID.
    This value is obtained after registering SFTPPlus in Entra ID via the `App registrations` page.

    Before version 5.12.0, this was named `application_id`.


password
--------

:Default value: Empty
:Optional: No
:Values: * plain text
:From version: 4.24.0
    This is the Azure client secret generated for the SFTPPlus application.


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

    Leave empty to not have any default group and only use the groups associated via Entra ID.

    The first configured base group is also the primary group.


group_association
-----------------

:Default value: `base-groups`
:Optional: No
:Values: * `base-groups`
         * `base-and-cloud-groups`
:From version: 4.22.0
:Description:
    Defines the SFTPPlus groups that are associated with authenticated users.

    When set to `base-groups`, it will associate any Entra ID user with the
    list of groups configured via the `base_groups` configuration option.

    When set to `base-and-cloud-groups`,
    it will associate the user with the list of groups defined via the `base_groups` option
    and the SFTPPlus groups having the same name as the Entra ID security groups that this user is a member of.
    If the user is associated with Entra ID groups not configured on SFTPPlus, those groups are ignored.
    If no Entra ID groups are found for this user, only the base groups are used.
    If the authenticated user has no associated SFTPPlus group in Entra ID and `base_groups` is empty, the authentication fails.
    The Entra ID groups are associated with SFTPPlus groups if they have the same name.
    The matching is case-sensitive.


base_roles
----------

:Default value: Empty
:Optional: yes
:Values: * Empty
         * Role UUID.
         * Comma-separated list of role UUIDs.
:From version: 4.27.0
:Description:
    Defines the SFTPPlus roles that are associated with any authenticated administrator.

    The first configured base role is also the primary role.

    ..  danger::
        When this option is defined (not empty),
        any Entra ID user that is accepted as part of the SFTPPlus Entra ID app registration is allowed to connect to the SFTPPlus management web console.

        We recommend creating an Entra ID app registration dedicated to the SFTPPlus management web console,
        **separate** from the Entra ID app dedicated to file transfers.

        You can then configure access to SFTPPlus management, via the Azure Portal.
        From `Entra ID -> Enterprise applications` search for the registered SFTPPlus Entra ID app,
        and from the `Users and Groups` configure the access.


roles_association
-----------------

:Default value: `base-and-cloud-groups`
:Optional: No
:Values: * `base-roles`
         * `base-and-cloud-groups`
:From version: 5.14.0
:Description:
    Defines how the SFTPPlus roles are associated with authenticated administrators.

    When set to `base-roles` it will associate the administrator to the list of roles defined by the `base_roles` option.

    When set to `base-and-cloud-groups`,
    it associates the administrator with the list of roles defined via the `base_roles` option
    and the SFTPPlus roles having the same name as the Entra ID groups that this user is a member of.

    If the user is associated with Entra ID groups for which there is no configured role in SFTPPlus, those groups are ignored.

    If no Entra ID groups are found for this user matching any existing SFTPPlus role,
    only the base roles are used.

    If the authenticated user has no associated SFTPPlus roles in Entra ID cloud and `base_roles` is empty, the authentication fails.

    The Entra ID groups are associated with SFTPPlus roles if they have the same name.
    The matching of the roles is case-sensitive.


proxy
-----

:Default value: ''
:Optional: Yes
:Values: * `URI` like expression.
         * `connect://12.342.421.2:3128`
         * `disabled` (since 5.14.0)
:From version: 4.23.0
:Description:
    This configures the proxy used by SFTPPlus to connect to the cloud services required by Entra ID.

    For now, only the HTTP/1.1 CONNECT tunneling proxy method is supported.

    Leave it empty to use the general proxy configuration.

    Set to `disable` to disable using a proxy.


remove_username_suffix
----------------------

:Default value: Empty
:Optional: Yes
:Values: * Text
         * Multiple values, one value per line.
:From version: 4.23.0
:Description:
    Suffix of the Entra ID username to be removed by SFTPlus when generating the username used for file transfer operations.

    You can configure SFTPPlus to remove multiple suffixes.
    Define each suffix that should be removed on a separate line.
    The first suffix matching the Entra ID username is used,
    while the remaining are ignored.

    For example, if the Entra ID username is ``Jane.R@sftpplus.onmicrosoft.com``,
    and you want SFTPPlus to handle the user as ``Jane.R``, you can configure
    this as ``remove_username_suffix = @sftpplus.onmicrosoft.com``.


api_scopes
----------

:Default value: Empty
:Optional: Yes
:Values: * Azure API scope name
         * Multiple scope names, one scope per line.
:From version: 4.24.0
    This allows SFTPPlus to ask the Entra ID for extra API permissions when an account is authenticated.

    The extra API access token is available to the SFTPPlus Python API extensions.
    It is used for implementing custom extensions that integrate with Entra ID.

    You can leave this empty if you don't plan to use custom SFTPPlus extensions.

    Multiple API scopes can be defined.
    Each scope should be defined on a separate line.
