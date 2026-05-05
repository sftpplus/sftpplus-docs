Azure BLOB and Azure Files
==========================

..  contents:: :local:


Overview
--------

This page describes how to configure Entra ID and Azure Storage to allow SFTPPlus to manage files from Azure BLOB or Azure Files, hosted in the Azure Cloud.

Check the separate reference documentation for :doc:`Azure BLOB</configuration-client/azure-blob>` and :doc:`Azure Files</configuration-client/azure-file>`,
which describes all the available configuration options.

SFTPPlus will connect to the Azure Storage service using the HTTPS REST API.

The authentication is done via either *Access Keys* or *Entra ID OAuth2*.


Paths configuration
-------------------

The path / url to the Azure File / BLOB storage is case-sensitive.

When using Azure File / BLOB locations, the source or destination path will be
defined as the name of the share or container (to or from where files are transferred),
followed by the targeted directory inside that share.
The path will look like ``/SHARE-NAME/DIR-IN-ROOT/PARENT-DIR`` or ``/CONTAINER-NAME/DIR-IN-ROOT/PARENT-DIR``.


Limitation for Azure BLOB
-------------------------

The Azure BLOB service is designed to work as an `object` storage system,
and not as a file-system.

The main difference between Azure BLOB and other file storage systems,
is the lack of support for folders / directories.

The directory hierarchy is created by using a naming convention,
in which the file name contains a directory delimiter character.
Files are still stored in a flat structure.

A major implication, is that there are no empty folders.
Folders are generated based on sections of a file name,
thus you can't just have a folder without a file.

At the same time, getting the files from a folder is implemented by searching for all the files for which their names start with that folder name.
This means that when you list a folder that doesn't exist the result is an empty list.

The current SFTPPlus integration with Azure BLOB has the following limitations:

* Authentication using shared access signatures is not supported.

If any of these limitations are a blocker for implementing SFTPPlus according to your specifications, get in touch with our support team.
We can extend SFTPPlus to meet your requirements.


Limitations for Azure Files
---------------------------

The current SFTPPlus integration with Azure Files has the following limitations:

* Authentication using shared access signatures is not supported.


Entra ID and RBAC authentication
--------------------------------

To access Azure Storage via SFTPPlus, you need to handle two distinct "planes" of security:

* SFTPPlus application registration as a *service principal*
* Azure RBAC (Role-Based Access Control)

Start by setting up an Entra ID application registration for SFTPPlus.
You can also use an already registered Entra ID application, for example when you have SFTPPlus already configured to connect to SharePoint Online or Outlook/Exchange.

The SFTPPlus application will be registered for your directory ID (tenant ID) and will receive a unique application ID.

This is done via the Entra ID `App registrations` page.

As part of the application registration process you also need to define a client secret.
This is configured inside the SFTPPlus location as the `password` configuration option.

The generated directory ID and application ID found in Entra ID are configured inside the SFTPPlus location configuration.

The OAuth2 `Client Credentials Grant` authentication flow is used by SFTPPlus.

No *API permissions* are required for Azure BLOB or Files.
Azure Storage is a built-in "first-party" service and relies almost entirely on RBAC (Role-Based Access Control) for the data security.

Registering an Entra ID application does not automatically grant access to the data inside your storage account.
You must assign a role to your SFTPPlus Application (Service Principal):

* Navigate to your Storage Account or specific Blob Container in the Azure Portal.
* Select Access Control (IAM).
* Click Add -> Add role assignment.
* Assign one of the available roles to your registered application.

The role assignment can be done at one of the following 2 levels:

* storage account - applies to any containers or file shares from that storage account.
* container or file share - applies only to that particular container or file share.

The following roles are **required at the storage account level**:

* `Reader` - Allows SFTPPlus to discover the list of available containers and file shares.
  This does not give read access to the files inside the containers or shares.

The following roles are recommended and can be set either at storage account level, or for each individual container or file share:

* `Storage Blob Data Reader` - For read only access to Azure BLOB
* `Storage Blob Data Contributor`- For read and write access to Azure BLOB
* `Storage File Data Privileged Reader` - For read-only access to Azure Files
* `Storage File Data Privileged Contributor` - For read and write access to Azure Files


Access Keys authentication
--------------------------

The access key authentication method will give full access to all the container and file shares available to the storage account.

To authenticate using one of the two available access keys for an Azure Storage account,
set the value of that key to the `password` option and select `access-key` as the authentication method.

The configuration will look like this::

    [locations/87af55d6-3a7e-11f1-9d95-f36d76dc533b]
    name = Support BLOB files
    type = azure-blob
    username = az-acme-support-storage

    authentication_method = access-key
    password = CONTENT_OF_ONE_OF_THE_KEYS


Keeping the source directory to Azure BLOB
------------------------------------------

When a transfer is configured with an Azure container as source
and configured to delete the source file on a success transfer,
the source folder might end up being empty.

In Azure BLOB, empty folders don't exist,
and SFTPPlus will generate an error when the source folder of a transfer doesn't exist.

To keep the source folder in Azure BLOB, it is recommended to always keep a file in the source directory.

You can configure the SFTPPlus transfer to ignore that file.

For example, you can create a file name ``.keep`` and configure a transfer to ignore it as::

    source_path = /manual-container/source/folder
    source_filter: ! .keep


HTTPS requests
--------------

SFTPPlus will connect to the Azure cloud using HTTPS. Connections will use the default list of `secure` ciphers and TLS v1.2 or TLS v1.3 protocols.

The requests made by SFTPPlus to the Azure Storage server are done using
the ``sftpplus-azure-blob-UUID`` or ``sftpplus-azure-file-UUID`` format.
Where UUID is a unique identifier for this location.
This can be used inside Azure Storage Analytics to identify the operations
done by this location.
The request ID will look like::

    x-ms-client-request-id: sftpplus-azure-blob-60ec1329-cc5d-416e-81b9-7c22
    or
    x-ms-client-request-id: sftpplus-azure-file-60ec1329-cc5d-416e-81b9-7c22
