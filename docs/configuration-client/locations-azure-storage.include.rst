Introduction
------------

The HTTPS connections will use the default list of `secure` ciphers and will
accept TLS v1.1 and TLS v1.2 protocols.

..  note::
    Unsecured HTTP access is not available.

..  note::
    The current implementation is tested using
    General-purpose v2 (GPv2) accounts.

Only storage account names with access keys are currently supported.
Please get in touch if you plan to use Azure Active Directory or
shared access signatures.

The path / url to the Azure File / BLOB storage is case-sensitive.

When using Azure File / BLOB locations, the source or destination path will be
defined as the name of the share or container (to or from where files are transferred),
followed by the targeted directory inside that share.
The path will look like ``/SHARE-NAME/DIR-IN-ROOT/PARENT-DIR`` or ``/CONTAINER-NAME/DIR-IN-ROOT/PARENT-DIR``.

The requests made by SFTPPlus to the Azure Storage server are done using
the ``sftpplus-azure-blob-UUID`` or ``sftpplus-azure-file-UUID`` format.
Where UUID is a unique identifier for this location.
This can be used inside Azure Storage Analytics to identify the operations
done by this location.
The request ID will look like::

    x-ms-client-request-id: sftpplus-azure-blob-60ec1329-cc5d-416e-81b9-7c22
    of
    x-ms-client-request-id: sftpplus-azure-file-60ec1329-cc5d-416e-81b9-7c22


username
--------

:Default value: Empty
:Optional: No
:From version: 3.36.0
:Values: * Text.
:Description:
    Name of the Azure Storage Account.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 3.36.0
:Values: * Plain text.
:Description:
    Any of the two access keys for the Azure storage account.

    It should be specified in Base64 format.
    This is the default format presented by the Azure Portal.
