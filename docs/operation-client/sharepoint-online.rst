SharePoint Online sites
=======================

..  contents:: :local:


Overview
--------

This page describes how to configure Entra ID and SharePoint Online to allow SFTPPlus to manage files from a SharePoint Online sites, hosted in the Azure Cloud.

Check the separate :doc:`reference documentation for SharePoint Online</configuration-client/sharepoint-online>`,
which describes all the configuration options available for a `sharepoint-online` location.

There are 2 main non-SFTPPlus components that needs to be configured:

* Entra ID authentication and authorization
* SharePoint Online sites permissions

SFTPPlus will connect to the SharePoint Online server using the MS Graph HTTPS API.

The authentication to MS Graph is done via the Entra ID OAuth2 HTTPS method.


Paths configuration
-------------------

The path configured for SFTPPlus for a SharePoint Online site document library is different from the *web URL* used by SharePoint Online.

In SharePoint Online the URL is defined as ``https://sftpplus.sharepoint.com/sites/test-site/test_lib?id=%2Fsites%2Ftest-site%2FReports%2F2025``

In SFTPPlus the path is configured as ``/Reports/2025``, without adding the site name.


Limitations
-----------

* SharePoint Online is only supported in the `Global service`,
  without support for government cloud.
  This is due to SFTPPlus using permanent delete operation.
  Get in touch if you plan to deploy SFTPPlus in an Azure government cloud.
* The paths configured for SharePoint Online in SFTPPlus are case sensitive.
* SFTPPlus can only handle folders with up to 1000 files.
* The rename/move operation is supported only inside the same Document Library.
  This is a limitation of the MS Graph API.
  Each Document Library is a handles as separate Azure Drive.
* When removing a file or folder,
  SFTPPlus will perform a permanent delete.
  Files and folders aren't sent to the recycle bin.
  Get in touch if you need to move files to recycle bin instead of removing them.
* A SharePoint Online location is dedicated to a single SharePoint site.
  If you need to transfer files between multiple SharePoint sites,
  you will need to create one location for each site.


Migration from WebDAV to SharePoint OAuth2
------------------------------------------

The SFTPPlus `webdav` location can be used to access files hosted by SharePoint Online, in a similar way to the SFTPPlus dedicated `sharepoint-online` location.

The main difference between `webdav` and `sharepoint-online` is that `webdav` location is implicitly associated with any site from your organization.
For `sharepoint-online` you need to setup separate permissions for each site you want to give SFPPlus access to.

As a result of this, paths for `webdav` location will contain the site name.
In `webdav` the path is configured as ``/sites/test-site/Reports/2025``.
In `sharepoint-online` the path is configured as ``/Reports/2025``, without adding the site name.

Other differences:

* `webdav` used the *SAML* username + password authentication, using a service account.
  This is considered legacy usage as it requires a dedicated Office365 user license.
* `webdav` user is associated with your organization and has implicit access to any site
* `webdav` used the standard HTTP WebDAV protocol, the same one used for on-premise SharePoint sites.
* `sharepoint-online` uses the *OAUth2* application-id + secret authentication.
* `sharepoint-online` uses HTTP MS Graph API.
* `sharepoint-online` application-id is associated to a single site.
  You need to create separate explicit association for each site you want to give SFTPPlus access to.

Advantages of `webdav`:

* Permissions are set using UI tools and SFTPPlus access is configured just like any other user.
* File changes are recorded in the SharePoint Details - Activity section.
* Support for on-premise SharePoint deployments.

Disadvantages of `webdav`:

* Requires an additional Office365 license.
* The multi-factor authentication should be disabled for the Office365 account used by SFTPPlus.
* For SharePoint Online, Microsoft will remove support for this access method.

Advantages of `sharepoint-online`:

* No need for an additional Office365 license.
* Multi-factor authentication can be enabled to the full organization without any exceptions.

Disadvantages of `sharepoint-online`:
* Requires administrative access to Azure EntraID to setup the SFTPPlus application id and secret.
* No UI to setup permissions to a site. You will need to use PowerShell command line tools
* Permissions can only be set as read-only, read-write, manage, full to the whole site. There is no support to setup separate permissions for SharePoint site items like document libraries.
* File changes are recorded as `SharePoint App` without any activity details.


Entra ID Authentication
-----------------------

To connect to a SharePoint Online site you need to set up an Entra ID application registration for SFTPPlus.

The SFTPPlus application will be registered for your directory ID (tenant ID) and will receive a unique application ID.

This is done via the Entra ID `App registrations` page.

As part of the application registration process you also need to define a client secret.
This is configured inside the SFTPPlus location as the `password` configuration option.

The generated directory ID and application ID found in Entra ID are configured inside the SFTPPlus location configuration.

The OAuth2 `Client Credentials Grant` authentication flow is used by SFTPPlus.

This requires setting up the API permissions, using `Application permissions`.
Make sure the API permissions are **not** defined as `Delegated permissions`.

The permissions need to be added to `MS Graph`:

* Sites.Selected

..  note::
    After adding the permissions you need to `Grant admin consent` on the SFTPPlus EntraID application for your organization.

SFTPPlus access to SharePoint Online sites is fully automated,
without user interaction.
The access is done using the identity of the SFTPPlus application registered via Entra ID, as opposed to an Entra ID domain user.

SharePoint Online admins will need to provide specific site access for SFTPPlus applications to access the files hosted by the Document Libraries from sites.

When you register the STPPlus application in Entra ID with `Sites.Selected`,
Entra ID will not allow access to any SharePoint site from your organization.

You will need to grant access for the SFTPPlus Entra ID application to the SharePoint Sites that you want SFTPPlus to manage the files.

You can read more about the `Sites.Selected` permission in this `Microsoft Devblog post <https://devblogs.microsoft.com/microsoft365dev/updates-on-controlling-app-specific-access-on-specific-sharepoint-sites-sites-selected/>`_.

More advanced permissions are available.
Check the Microsoft documentation page covering the `Selected permissions in OneDrive and SharePoint <https://learn.microsoft.com/en-us/graph/permissions-selected-overview>`_.


Site permissions via SharePoint App Permissions
-----------------------------------------------

Site level permissions can be configured using the SharePoint Online App registration administrative page.

You need to configure the permissions for each site or sub-site that SFTPPlus will access.

Start by identifying the base URL of your SharePoint Online site.
For most organizations this will be ``https://<your-organization>.sharepoint.com/sites/<site-name>``.
For example, for our test site this is ``https://proatria.sharepoint.com/sites/manual-test-site``.

To access the SharePoint Online App Permissions page, go to the following URL, replacing the ``<site-name>`` with your site name::

    https://<your-organization>.sharepoint.com/sites/<site-name>/_layouts/15/appinv.aspx

Below is an example of the page.

..  container:: image-1

    ..  image:: /static/operation/sharepoint-entra-app-permissions.png
        :width: 800
        :align: center

Enter the SFTPPlus application ID in the `App Id` field and click on `Lookup`.
For `App domain` enter a dummy value like `localhost`.
For `Redirect URI` enter a dummy value like `https://localhost`.
SFTPPlus does not use these values, but they are required by the SharePoint Online form.

For the `App's permission request` use the following value::

    <AppPermissionRequests AllowAppOnlyPolicy="true">
        <AppPermissionRequest
            Scope="http://sharepoint/content/sitecollection/web"
            Right="Write"/>
    </AppPermissionRequests>

You can read more about the available permissions in the `SharePoint App Permissions documentation <https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/>`_.


Site permissions via PowerShell
-------------------------------

Site level permissions can be configured using the PowerShell command line tools.

Start by making sure you use PowerShell version 7.5 or newer.
The default PowerShell found on Windows Server 2022 or older **does not work** with the SharePoint PowerShell commands.
To install PowerShell 7 on Windows Server, `check the Windows install guide <https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5#msi>`_.

To install PowerShell on Linux, `check the Linux install guide <https://learn.microsoft.com/en-us/powershell/scripting/install/install-ubuntu>`_.

Make sure that the PowerShell SharePoint Online command line tools are installed in PowerShell::

    PS> Install-Module PnP.PowerShell

Register your PowerShell SharePoint Online command to your Azure Tenant so that you can perform administrative operations from the command line.
This only needs to be done one.
If you already have SharePoint Online PowerShell commands setup, you should skip this step.
You can find more info on the PNP Documentation page dedicated to `app registration <https://pnp.github.io/powershell/articles/registerapplication.html>`_::

    PS> $tenantID = "8fc59c4c-8266-11f0-b73a-b77dd4453999"
    PS> Register-PnPEntraIDAppForInteractiveLogin -ApplicationName "PnP PowerShell" -SharePointDelegatePermissions "AllSites.FullControl" -Tenant $tenantID

When you register a new `PNP PowerShell` app, you will get an app ID.
Set this ID as a PowerShell variable.
If you already have the app registered, you can get the ID via Azure Portal.

Start by defining your configuration variables::

    $siteURL = "https://sftpplus.sharepoint.com/sites/test-site"
    $appID = "SFTPPlus-Entra-APP-ID"
    $pnpID = "YOUR-PNP-PowerShell-APP-ID"

..  note::
    Note that we have 2 application IDs.
    `$pnpID` is the PowerShell to management application for your sites.
    This has administrative permissions.
    `$appID`` is the SFTPPlus application ID which we will configured with limited permissions.

Connect / enabled the PowerShell management access to SharePoint Online::

    PS> Connect-PnPOnline -Url $siteURL -clientId $pnpID

Check that the connection was successful and that you can list the libraries in your site. This can be used to double check that you are connected to the expected site::

    PS> Get-PnPList

Add SFTPPlus access to this site.
We setup minimal read and write permissions.
Managed and full access is not required by SFPPlus::

    PS> Grant-PnPAzureADAppSitePermission -AppId $appID -DisplayName 'SFTPPlus Manual read/write' -Permissions Write

..  note::
    For SharePoint Online, `write` will automatically give `read` permissions.
    If SFTPPlus only needs to read files from SharePoint online,
    without writing or deleting files, you can configured it using the `read` permission.

Check the configured permissions.
You can use `Revoke-PnPAzureADAppSitePermission -PermissionId <Id>` to revoke a previously granted permission::

    PS> Get-PnPAzureADAppSitePermission
