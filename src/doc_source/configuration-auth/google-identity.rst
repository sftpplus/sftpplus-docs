Google Identity
===============

..  contents:: :local:


Introduction
------------

The `google-identity` method is used to implement single sign-on authentication using the Google Identity service.

This allows using Google accounts to authenticate in SFTPPlus as administrators or file transfer accounts.

Google accounts that want to access SFTPPlus need to be member in at least one **security label group**.
To improve security and avoid accidentally giving access to SFTPPlus,
users that are member of *mailing groups* are not accepted by SFTPPlus.

To integrate SFTPPlus with a Google account,
you need to set the Google Cloud API details in SFTPPlus.
Google Identity is part of the Google Cloud service.
At the same time, some SFTPPlus details needs to be added to your Google Cloud setup.
In this way, SFTPPlus and Google Cloud are aware of each other and can work together.

Google Cloud provides both authentication and authorization processes.
For SFTPPlus integration, Google Identity is primarily used for authentication.
You have to define the authorization rules inside the SFTPPlus configuration.

It is recommended to configure the Google Identity authentication method as the first method in your authentication chain,
before the `SFTPPlus Application Accounts` authentication.

It is recommended to created dedicated **security label groups** for the client or administrators of SFTPPlus.

SFTPPlus always asks to confirm the selected Google user for authentication.
Get in touch if you would like SFTPPlus to automatically use the default Google user without a prompt.

The Google Identity authentication process should finalize in less than two minutes.
For security reasons, SFTPPlus rejects delayed authentication requests.

For SFTPPlus to integrate with the Google Identity authentication,
it needs to be able to initiate **outgoing connections** to the Google Cloud over HTTPS port 443.
Make sure your firewall allows outgoing connections.
An HTTP proxy can be used by SFTPPlus to connect to Google Cloud.

Below is the list of sub-domains used by SFTPPlus to communicate with Google Cloud:

* accounts.google.com
* oauth2.googleapis.com
* cloudidentity.googleapis.com
* openidconnect.googleapis.com
* www.googleapis.com

..  note::
    When using the Google authentication with SFTPPlus running behind a reverse proxy or an API gateway,
    make sure one of the following headers is set by your proxying setup:
    `X-Forwarded-Proto`, `X-Forwarded-Host`, `X-Forwarded-For`, or the `Forwarded` headers.
    When using the `X-Forwarded-Host` header, make sure it contains the port number in its value.

..  note::
    Only authenticating administrators and HTTPS file transfer users are supported.
    Get in touch if you need to authenticate SFTP or FTPS users.


Google Identity app configuration
---------------------------------

Besides defining the Google Identity authentication method inside the SFTPPlus configuration,
you also need to define SFTPPlus inside your Google Cloud console.

SFTPPlus interacts with Google Cloud as an OpenID Connect and OAuth2 application.

There are 4 main actions to configure inside your organization Google Cloud Console:

* Create a dedicated project for SFTPPlus in Google Cloud. You can also use an existing project and enable the `Cloud Identity` API for the SFTPPlus project.
* Setup Google Auth Platform for the SFTPPlus project
* Create credentials for SFTPPlus.
* Setup the authentication consent page and access scope.
* In Google Workspaces Admin, grant access to Google users for the SFTPPlus project.


Google Cloud project setup
^^^^^^^^^^^^^^^^^^^^^^^^^^

A Google Cloud project is used to setup the SFTPPlus interaction with the Google Cloud services.
We recommend creating a separate project for each SFTPPlus installation.

From Google Cloud `API Library <https://console.cloud.google.com/apis/library>`_, enable the `Cloud Identity <https://console.cloud.google.com/apis/library/cloudidentity.googleapis.com>`_ API.

When searching for `cloud identity` inside Google **API Library**, make sure to select `Google Enterprise API` from the **Category** filter.


Google Auth Platform setup
^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have created a new project or selected an existing project,
assuming `Cloud Identity` is enabled,
start by setting up the `Google Auth Platform <https://console.cloud.google.com/auth/overview/create>`_ for your project.

**Branding**

In the **Branding** page, add information to be visible to SFTPPlus users during the Google authentication process.

**Audience**

In the **Audience** page, leave `internal` as the user type.

This way, SFTPPlus is limited to accessing Google Workspace users within your organization.

**Clients**

In the **Clients** page, create a new OAuth 2.0 Client for SFTPPlus.

The credentials are used to identify and authorize access to Google Cloud for a specific SFTPPlus installation or deployment.

Select `Web Application` as the *application type*, then define a name for these credentials.
Our suggestion is to use a name like `SFTPPlus UK PROD-01` or something that indicates which SFTPPlus installation uses these credentials.

`Authorized JavaScript origins` are not required for SFTPPlus, it can be left empty.

`Authorized redirect URIs` configuration is required for SFTPPlus operation.

Define the URL using the following format,
where `SERVER:PORT` is replaced with the address for your HTTPS web file browser,
and `AUTH-UUID` with the unique ID of this authentication method:
`https://SERVER.COM:PORT/?redirect-AUTH-UUID`

**Data access**

Use the *Add or remove scope* button to configure the scopes required by SFTPPlus.

The following API scopes are required:

* `openid` - for generic authentication
* `https://www.googleapis.com/auth/userinfo.email` - for finding the email and using it as username
* `https://www.googleapis.com/auth/cloud-identity.groups.readonly`


Google Workspace Access
^^^^^^^^^^^^^^^^^^^^^^^

Inside the `Google Admin console <https://admin.google.com/u/1/ac/owl>`_, go to `Security > Access and data control > API controls`.

Select `Manage 3rd party apps`, then proceed with adding the SFTPPlus application.

Click `Configure new app`.
Use the client ID of the credentials that were previously created for SFTPPlus and click `Search`.

Once the SFTPPlus credentials are located, you can enable access for SFTPPlus to all users from your organization or to selected organization units.

From the `Access to Google Data` configuration page, select `Specific Google data`, then continue to confirm the new configuration.

..  note::
    At this point, Google Cloud only allows settings access to 3rd party web apps based on the *Organizational Unit*.

-----

.. include:: /configuration-auth/authentication-commons.include.rst


client_id
---------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 5.11.0
:Description:
    Client ID of the SFTPPlus credentials inside Google Cloud API.
    This value is obtained after creating new credentials for SFTPPlus.


password
--------

:Default value: Empty
:Optional: Yes
:Values: * plain text
:From version: 5.11.0
    This is the client secret generated by Google Cloud API for the SFTPPlus application.


base_groups
-----------

:Default value: Empty
:Optional: yes
:Values: * Empty
         * Group UUID.
         * Comma-separated list of group UUIDs.
:From version: 5.11.0
:Description:
    Defines the SFTPPlus groups that are associated with any authenticated users.

    Leave empty to not have any default group, and only use the groups associated via Google Cloud.

    The first configured base group is also the primary group.


group_association
-----------------

:Default value: `base-groups`
:Optional: No
:Values: * `base-groups`
         * `base-and-cloud-groups`
:From version: 5.11.0
:Description:
    Defines the SFTPPlus groups that are associated with authenticated users.

    When set to `base-groups`, it associates an authenticated Google user with the
    list of groups configured via the `base_groups` configuration option.

    When set to `base-and-cloud-groups`,
    it associates the user with the list of groups defined via the `base_groups` option
    and the SFTPPlus groups having the same name as the Google groups that this user is a member of.

    If the user is associated with Google groups not configured on SFTPPlus, those groups are ignored.

    If no Google groups are found for this user, only the base groups are used.

    If the authenticated user has no associated SFTPPlus group in Google cloud and `base_groups` is empty, the authentication fails.

    The Google Identity groups are associated with SFTPPlus groups if they have the same name.
    The matching of the groups is case-sensitive.


base_roles
----------

:Default value: Empty
:Optional: yes
:Values: * Empty
         * Role UUID.
         * Comma-separated list of role UUIDs.
:From version: 5.11.0
:Description:
    Defines the SFTPPlus roles that are associated with an authenticated administrator.

    The first configured base role is also the primary role.

    ..  danger::
        When this option is defined (not empty),
        any Google cloud user that is accepted as part of the SFTPPlus Google cloud application configuration is allowed to connect to the SFTPPlus management web console.

        We recommend creating a dedicated Google Cloud application dedicated to the SFTPPlus management web console,
        which is **separated** from the Google Cloud application dedicated to file transfers.


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
    and the SFTPPlus roles having the same name as the Google groups that this user is a member of.

    If the user is associated with Google groups for which there is no configured role in SFTPPlus, those groups are ignored.

    If no Google groups are found for this user matching any existing SFTPPlus role,
    only the base roles are used.

    If the authenticated user has no associated SFTPPlus roles in Google cloud and `base_roles` is empty, the authentication fails.

    The Google groups are associated with SFTPPlus roles if they have the same name.
    The matching of the roles is case-sensitive.


proxy
-----

:Default value: ''
:Optional: Yes
:Values: * `URI` like expression.
         * `connect://12.342.421.2:3128`
         * `disabled` (since 5.14.0)
:From version: 5.11.0
:Description:
    This configures the proxy used by SFTPPlus to connect to the cloud services.

    For now, only the HTTP/1.1 CONNECT tunnelling proxy method is supported.

    Leave it empty to use the general proxy configuration.


remove_username_suffix
----------------------

:Default value: Empty
:Optional: Yes
:Values: * Text
         * Multiple values, one value per line.
:From version: 5.14.0
:Description:
    Suffix of the Google ID username to be removed by SFTPlus when generating the username used for file transfer operations.

    You can configure SFTPPlus to remove multiple suffixes.
    Define each suffix that should be removed on a separate line.
    The first suffix matching the Google username is used,
    while the remaining are ignored.

    For example, if the Google username is ``Jane.R@sftpplus.example.com``,
    and you want SFTPPlus to handle the user as ``Jane.R``, you can configure
    this as ``remove_username_suffix = @sftpplus.example.com``.


api_scopes
----------

:Default value: Empty
:Optional: Yes
:Values: * Google Cloud API scope name
         * Multiple scope names, one scope per line.
:From version: 5.14.0
    This allows SFTPPlus to ask for extra Google Cloud API permissions when an account is authenticated.

    The extra API access token is available to the SFTPPlus Python API extensions.
    It is used for implementing custom extensions that integrate with Google Cloud.

    You can leave this empty if you don't plan to use custom SFTPPlus extensions.

    Multiple API scopes can be defined.
    Each scope should be defined on a separate line.
