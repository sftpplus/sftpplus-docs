SMB / Windows Share Location
============================

An `smb` location provides access to an SMB
(Server Message Block or Windows Share) server over TCP.

SMB versions 3 and 2 are supported, but version 1 is not.
Access over UDP is not included either.

The location only requires configuring the server address and credentials.
The actual share names and paths used for a file transfer are defined as part
of the transfer path configuration.

The communication with the SMB server is encrypted and all messages are
signed.
Contact us if you need access to legacy Windows shares that don't support
encryption or message signing.

..  warning::
    When accessing an Azure Files share authenticated using storage account key
    from outside the Azure cloud,
    it is highly recommended to secure your connection to the Azure cloud
    using private endpoints, site-to-site, or point-to-site VPN.
    Azure Files storage account key authentication is based on NTLM and is
    vulnerable to man-in-the-middle attacks.

..  note::
    On-premises Active Directory Domain Services or
    Azure Active Directory Domain Services authentication methods via
    Kerberos are not yet supported.


address
-------

:Default value: Empty
:Optional: No
:Values: * Host name or IP address of the server.
:From version: 4.13.0
:Description:
    Address of the remote SSH server. IP or DNS name.

    If you are using Azure Files the address will have the following format:
    ``ACCOUNT_NAME.file.core.windows.net`` where ACCOUNT_NAME is replaced
    with your Azure Storage account name.


port
----

:Default value: `445`
:Optional: No
:Values: * Number, greater than 0.
:From version: 4.13.0
:Description:
    Port number of the remote server.


username
--------

:Default value: Empty
:Optional: No
:From version: 4.13.0
:Values: * Text.
:Description:
    Username or storage account name used to authenticate to the remote server.

    Anonymous (guest) access is not yet supported.
    Contact us if you need support for connecting to a Windows Share without
    a username and password.


password
--------

:Default value: Empty
:Optional: No
:From version: 4.13.0
:Values: * Plain text password.
         * Empty
:Description:
    This option specifies the password or key used to connect to the remote
    server.
    It is provided in plain text.


require_encryption
------------------

:Default value: 'yes'
:Optional: No
:From version: 4.16.0
:Values: * `yes`.
         * `no`.
:Description:
    This option defines whether SFTPPlus requires SMB encryption when
    connecting to the remote share.

    With modern servers it is recommended to keep this option set to `yes` to
    make use of the highest level of available security.

    On Windows 2008 and Windows 7 or older version of Windows, SMB encryption
    is not supported.
    To connect to these shares you will need to set this configuration to `no`.
