Introduction
------------

This page is dedicated to the configuration options available for connecting to an Azure storage account.

For more information about how to implement Azure Storage (BLOB or Files) based transfers,
see the separate documentation page for :doc:`implementing Azure BLOB and Files transfers</operation-client/azure-blob-files>`.


username
--------

:Default value: Empty
:Optional: No
:From version: 3.36.0
:Values: * Text.
:Description:
    Name of the Azure Storage Account.


authentication_method
---------------------

:Default value: `access-key`
:Optional: Yes
:Values: * `access-key`
         * `entra-id`
:From version: 5.23.0
:Description:
    The authentication method to use for connecting to the Azure cloud.

    The default value of `access-key` is used when authentication is done using one of the *security keys* defined for the storage account.

    Use `entra-id` to authenticate using OAuth 2.0 access tokens from the Microsoft Entra.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 3.36.0
:Values: * Plain text.
:Description:
    Any of the two access keys for the Azure storage account or the OAuth2 client secret.

    For `authentication_method = access-key`, this is one of the two
    access keys for the Azure storage account.
    It should be specified in Base64 format.
    This is the default format presented by the Azure Portal.

    For `authentication_method = entra-id`, this is the OAuth2 client
    secret and should be provided as-is, not in Base64 format.


directory_id
------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 5.23.0
:Description:
    Directory (tenant) ID of the SFTPPlus inside the Entra ID.
    This value can be viewed after registering SFTPPlus in Entra ID via the `App registrations` page.

    Only used when `authentication_method = entra-id`.


application_id
--------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 5.23.0
:Description:
    Application (client) ID of the SFTPPlus inside the Entra ID.
    This value is obtained after registering SFTPPlus in Entra ID via the `App registrations` page.

    Only used when `authentication_method = entra-id`.
