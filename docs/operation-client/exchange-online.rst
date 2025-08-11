Exchange Online attachments
===========================

..  contents:: :local:


Overview
--------

This page describes how to configure Entra ID and Exchange Online to allow SFTPPlus to read or write emails.

There are 2 main non-SFTPPlus components that needs to be configured:

* Entra ID authentication and authorization
* Exchange Online mailbox permissions

SFTPPlus will connect to the Exchange Online server using the MS Graph HTTPS API.

The authentication to MS Graph is done via the Entra ID OAuth2 HTTPS method.


Attached files integration
--------------------------

SFTPPlus handles the files attached to to emails in a similar way to a local filesystem.

The Outlook folders are handled as normal directories,
with support for sub-directories.

All files attached to messages that belong to the same mail folder are considered as members of that mail folder.

The name of the files is generated from the email folder and the attachment name.

For example, assume that you have these 2 messages in the `/Inbox` folder:

* subject `Report for May 2024` with `report-may.pdf` and `income-2024-05-01.csv` attachments
* subject `Order ACME Ltd` with `order.xml` attachment

SFTPPlus will handle these files as::

    /Inbox/Report for May 2024-report-may.pdf
    /Inbox/Report for May 2024-income-2024-05-01.csv
    /Inbox/Order ACME Ltd-order.xml

When configuring a transfer to filter or ignore certain file names,
the filter is applied to email subject and attachment file name.

In the above example `Report for May 2024-report-may.pdf` is the filename, as observed by SFTPPlus and `Inbox` is the parent directory name.
Filter rules will be applied to this path.

When attachments are downloaded, SFTPPlus will handle each attachment as a separate file.

When removing files after a transfer, the attachments from a message are removed.
Once all attachments from a message are removed, the message is also removed.

Filename with more than 240 characters are truncated.
As long as the extension is less than 10 character, the extension is preserved.

Characters that are not valid filename character in Windows, Linux, or macOS are replaced with the hyphen (-) character.


Limitation
----------

SFTPPlus tries to accommodate all Exchange Online use cases encountered by our existing customer.

The current SFTPPlus integration with Exchange Online has the following limitations:

* Shared mail folders are not yet supported.
  Contact our support team if you need to transfer attachments from shared folders.
* Mail folders should have less than 1000 sub-folders.
* A single message should have less than 1000 attachments.
* Mail folders should have less than 1000 emails at a single given time.
  This is a limitation to improve performance and avoid reaching the API requests limit.
* It can handle mail folders with more than 1000 emails,
  as long as it is configured to remove the messages once the attachment are transferred.
* The list of available mail folders is generated when the SFTPPlus location is connected.
  If mail folders are modified (added, removed, or renamed) after the STPPlus location was started, SFTPPlus will observe the changes with a delay of 60 seconds.
  You can force a reload of the folders by manually restarting the location.

If any of these limitations are a blocker for implementing SFTPPlus according to your specifications, get in touch with our support team.
We can extend SFTPPlus to meet your requirements.


Streaming attachments to remote locations
-----------------------------------------

It's recommend to use the local filesystem as the destination location for transfers that download attachments from Exchange Online.

Due to a defect in MS Graph API, the total size of attachment is incorrectly advertise as part of the Exchange Online API.

This complicates the implementation of direct transfers to servers like AS2, which require the exact total size of the file at the start of the transfer.

Streaming support is enable in SFTPPlus by transferring the attached files twice.
Once to detect the actual file size and then for the actual transfer.
As a drawback, this can increase the network traffic.
The impact should be minimal as in general the attachment files are small.


Entra ID Authentication
-----------------------

To connect to an Office365 email account, you need to setup an Entra ID application registration for SFTPPlus.

The SFTPPlus application will be registered for your directory ID (tenant ID) and will receive a unique application ID.

This is done via the Entra ID `App registrations` page.

As part of the application registration process you also need to define a client secret.
This is configured inside the SFTPPlus location as the `password` configuration option.

The generated directory ID and application ID found in Entra ID are configured inside the SFTPPlus location configuration.

The OAuth2 `Client Credentials Grant` authentication flow is used by SFTPPlus.

This requires setting up the API permissions, using `Application permissions`.
Make sure the API permissions are not defined as `Delegated permissions`.

The permissions need to be added to `MS Graph`:

* Mail.ReadWrite

..  note::
    After adding the permissions you need to `Grant admin consent` on the SFTPPlus EntraID application for your organization.


Exchange Online permissions
---------------------------

SFTPPlus access Exchange Online mailboxes fully automated, without user interaction.
The access is done using the identity of the SFTPPlus application registered via Entra ID, as opposed to an Entra ID / domain user.

While no user interaction is needed, Exchange Online admins will need to provide specific mailbox access (using Exchange Online PowerShell) for applications' service principals to access the mailboxes.

When you register the STPPlus application in Entra ID, by default,
Entra ID will allow access to any mailboxes from your organization.

You will need to restrict access for the SFTPPlus Entra ID application only to a one mailbox or a sub-set of Exchange Online mailboxes.

This is done in 2 steps:

1. Exchange Online Portal configuration for mail-enabled group configuration
2. Exchange Online PowerShell tools for application access security.

Use the `Exchange Admin portal <https://admin.exchange.microsoft.com/#/groups>`_ to manage the `mail-enabled security group <https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/manage-mail-enabled-security-groups>`_ for SFTPPlus.

It is recommended to create a dedicated group for the SFTPPlus application.
SFTPPlus will have access to all emails for the members of the group.

Once the mail-enabled group is setup, use the PowerShell commands to restrict SFTPPlus application access only to this group.

The Azure documentation can be found `here <https://learn.microsoft.com/en-us/graph/auth-limit-mailbox-access>`_

Start by installing the Exchange Online tools::

    Install-Module -Name ExchangeOnlineManagement

Connect your PowerShell session to your organization::

    Import-module ExchangeOnlineManagement
    Connect-ExchangeOnline -Organization YOUR_DIRECTORY_ID

Restrict access for the SFTPPlus application, to only members of the mail-enabled group.
You can obtain the SFTPPlus application ID from the Entra ID app registration page and place it instead of `YOUR-SFTPPLUS-APP-ID`.
Replace `sftpplus-app@example.com` with the email address of your mail-enabled group.
You can have any text as `-Description`::

    New-ApplicationAccessPolicy -AppId YOUR-SFTPPLUS-APP-ID -PolicyScopeGroupId sftpplus-app@example.com -AccessRight RestrictAccess -Description "Restrict SFTPPlus access to members of sftpplus-app group."

You can test whether SFTPPlus Entra ID application has access to a specific mailbox using this command::

    Test-ApplicationAccessPolicy -Identity JohnD@example.com -AppId YOUR-SFTPPLUS-APP-ID
