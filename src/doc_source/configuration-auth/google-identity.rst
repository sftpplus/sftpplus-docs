Google Identity
===============

..  contents:: :local:


Introduction
------------

The `google-identity` method is used to implement single sign-on authentication using the Google Identity service.

This allows using Google accounts to authenticate in SFTPPlus as administrators or file transfer accounts.

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

.. FIXME:4175:
   Below note should be removed once we support reverse proxy.
..  note::
    Using the Google authentication with SFTPPlus running behind a reverse proxy or an API gateway is not yet supported.


..  note::
    Only HTTPS file transfer user authentication and web management console are supported.
    Get in touch if you need to authenticate SFTP or FTPS users.


Google Identity app configuration
---------------------------------

Besides defining the Google Identity authentication method inside the SFTPPlus configuration,
you also need to define SFTPPlus inside your Google Cloud console.

SFTPPlus interacts with Google Cloud as an OpenID Connect and OAuth2 application.

There are 4 main actions to configure inside your organization Google Cloud Console:

* Create a dedicated project for SFTPPlus in Google Cloud. You can also use an existing project and enable the `Cloud Identity` API for the SFTPPlus project.
* Create credentials for SFTPPlus.
* Setup the authentication consent page and access scope.
* In Google Workspaces Admin, grant access to Google users for the SFTPPlus project.


Google Cloud project setup
^^^^^^^^^^^^^^^^^^^^^^^^^^

A Google Cloud project is used to setup the SFTPPlus interaction with the Google Cloud services.

In your Google API Console, start by creating a new project and setting up the `consent screen <https://console.cloud.google.com/apis/credentials/consent>`_ for the project.
You can also use an existing project.

We recommend creating a separate project for each SFTPPlus installation.

From Google Cloud `API Library <https://console.cloud.google.com/apis/library>`_, search for `Cloud Identity` and enable it.


Credentials for SFTPPlus
^^^^^^^^^^^^^^^^^^^^^^^^

The credentials are used to identify and authorize access to Google Cloud for a specific SFTPPlus installation or deployment.

Create new credentials of type `OAuth client ID` for SFTPPlus,
using the `Google Cloud API Credentials <https://console.cloud.google.com/apis/credentials>`_ page.

Select `Web Application` as the *application type* and define any name for these credentials.
Our suggestion is to use a name like `SFTPPlus UK PROD-01` or something that indicates which SFTPPlus installation uses these credentials.

`Authorized redirect URIs` configuration is required for SFTPPlus operation.

Define the URL using the following format,
where `SERVER:PORT` is replaced with the address for your HTTPS web file browser,
and `AUTH-UUID` with the unique ID of this authentication method:
`https://SERVER.COM:PORT/?redirect-AUTH-UUID`


Access consent page
^^^^^^^^^^^^^^^^^^^

The consent page is used to setup the access level for the SFTPPlus application.

Use the `OAuth consent screen` configuration to register the SFTPPlus application as an `Internal` application.
In this mode, SFTPPlus is limited to accessing Google Workspace users within your organization.

The following API scopes are required:

* `openid` - for generic authentication
* `email` - for finding the email and using it as username
* `https://www.googleapis.com/auth/cloud-identity.groups.readonly`


Google Workspace Access
^^^^^^^^^^^^^^^^^^^^^^^

Inside the `Google Admin console <https://admin.google.com/u/1/ac/owl>`_, go to `Security > Access and data control > API controls`.
You might need to click `Show more` to reveal the `Security` menu option.

Select `Manage 3rd party apps <https://admin.google.com/u/1/ac/owl/list?tab=configuredApps>`_, then proceed with adding the SFTPPlus application.

Click `Add app` and select `OAuth app name or client ID`.
Use the client ID of the credentials that were previously created for SFTPPlus and click `Search`.

Once the SFTPPlus credentials are located, you can enable access for SFTPPlus to all users from your organization or to selected groups.

From the `Access to Google Data` configuration page, select `Limited` and then continue to confirm the new configuration.

-----

When you want SFTPPlus to apply different account configuration based on the Google group membership, the Google groups must be labelled as `Security`.

To mark a group as a security group, from Google Workspace admin console go to `Directory -> Groups`,
select the group that you want to modify.
Click on the `Group information` panel.
After that, you can click on the `Label` section to see the option to define this group as a `Security` group.


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


proxy
-----

:Default value: ''
:Optional: Yes
:Values: * `URI` like expression.
         * `connect://12.342.421.2:3128`
:From version: 5.11.0
:Description:
    This configures the proxy used by SFTPPlus to connect to the cloud services.

    For now, only the HTTP/1.1 CONNECT tunnelling proxy method is supported.
