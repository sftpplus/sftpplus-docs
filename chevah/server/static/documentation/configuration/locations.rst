Locations
=========

..  contents:: :local:


Introduction
------------

A location configuration provides the required information to allow
SFTPPlus to connect to local or remote locations in order to perform
file transfers between locations.

Please consult the `type` configuration option to see the list of
supported location types.

Locations are auto-started when a transfer or another component needs them and
the location is not started and connected.

They are also fault-tolerant, allowing retries for interrupted connections.

Transfers using a failed location will also fail and will
not trigger a new connection attempt for the location.
In this type of scenario, the failed location must be manually started first,
after resolving the initial error.


Adding a new location via Local Manager
---------------------------------------

A new location can be added or changed via Local Manager below.
Options will differ depending on which location type is used.

See below for an example of an initial configuration with the FTPES location.

..  image:: /_static/gallery/gallery-add-ftps-location.png


Adding a new location via text configuration
--------------------------------------------

Adding a new location configuration is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``locations/`` and followed by
the location's UUID.

The location's UUID can be any unique string used to identify the location.
Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/general>`.

For example, to add a new location configuration of type `filesystem`
called ``Local file system``::

    [locations/b904e6h6-c295-4ccf-8abd-edcae4d3324f]
    name = Local file system
    description = File system accesses as service account.
    type = filesystem


Location options
----------------

Each location configuration section has the following configurations:


name
^^^^

:Default value: ''
:Optional: No
:From version: 2.8.0
:Values: * Any text.
:Description:
    Human-readable short text used to identify this location.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 2.8.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this location.


type
^^^^

:Default value: ''
:Optional: No
:From version: 2.6.0
:Values: * `filesystem` - Local file system.
         * `sftp` - SFTP protocol v3 over SSH v2.
         * `ftp` - FTP protocol without any encryption.
         * `ftpse` - Explicit FTPS protocol.
         * `ftpsi` - Implicit FTPS protocol.
         * `webdavs` - WebDAV over HTTPS.
         * `as2` - AS2 over HTTP or HTTPS
         * `azure-file` - Azure File Service.
         * `smb` - SMB / Windows Share
:Description:
    This option specifies the type of the location.
    Each type has a set of specific configuration options


idle_connection_timeout
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `300`
:Optional: Yes
:From version: 3.0.0
:Values: * Number of seconds after which idle connections are disconnected.
         * 0 - To disable timeouts.
:Description:
    Disconnect the connection to the remote peer if the location
    has not received any requests for the configured number of seconds.

    Keep-alive command requests are ignored, and the connection will be
    automatically disconnected if keep-alive is the only command requested
    in the configured interval.

    Disconnected locations will automatically reconnect when a new request
    is made.

    If the remote peer closed the connection before the local configured
    timeout, the connection is left closed, and it will be automatically
    recreated when a new command is requested.

    Set to `0` to always keep the connection active, by forcing
    reconnection when the remote peer closes the connection.


idle_connection_keepalive_interval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `0`
:Optional: Yes
:From version: 3.0.0
:Values: * Number of seconds
:Description:
    Send a keep-alive command every N seconds to avoid having the connection
    disconnected by the other peer due to inactivity.

    Set to `0` to disable keep-alive commands.

    The keep-alive command does not reset the idle connection timeout,


connection_retry_count
^^^^^^^^^^^^^^^^^^^^^^

:Default value: `12`
:Optional: Yes
:From version: 3.9.0
:Values: * Number of retries
:Description:
    Number of times to retry connection to the location, when the
    initial connection fails.

    Set to `0` to not retry.


connection_retry_interval
^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `300`
:Optional: Yes
:From version: 3.9.0
:Values: * Number of seconds
:Description:
    Number of seconds to wait between connection attempts.

    Set to `0` to retry right away without any delay.


Local File System Location
--------------------------

A `local file system location` is accessed using the operating system's
file system.

For now, no extra configuration options are available for this location type.

..  note::
    For the moment, local file system locations can't be defined from the
    Local Manager GUI.
    There is a single default local filesystem which is
    available inside the GUI and which can not be removed.


SFTP Location
-------------

An `sftp location` provides access to an SFTP (version 3) server over SSH
(version 2).
This does not include access over SCP.

As the connection is done in non-interactive mode, the identity of the remote
SSH server needs to be verified, so that credentials are not sent to an
untrusted remote SSH server.

To validate the remote SSH server, the fingerprint of its public key is
stored as a hexadecimal string in the `ssh_server_identity` option.

An SSH server can authenticate users using either a password or an SSH key.


ssh_server_identity
^^^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: No
:Values: * MD5 Hexadecimal, delimited by colons
         * SHA1 Base64
         * SHA256 Base64
         * OpenSSH Public Key
         * X.509 certificate
         * Multiple identities on multiple lines.
         * `set-on-first-connection`
:From version: 3.51.0
:Description:
    This configuration defines the identity of the remote SSH server.

    It can be defined as an MD5, SHA1, or SHA256 fingerprint.

    You can also define it as an OpenSSH public key or an X.509 SSL/TLS
    certificate.

    To automatically configure with the identity of the server found during the
    first connection, you can use the `set-on-first-connection` option.
    For security reasons, we do not recommend this option.
    This option is not available for cluster operations when the remote
    SFTP service has more than one SSH server identity.

    When you are connecting to a remote SSH / SFTP service which is deployed
    as a cluster or as a disaster recovery failover it is possible that each
    node/server from the cluster to have its own identity.
    You will need to configure SFTPPlus with the identity of each server
    by defining multiple identities on separate lines.

    This configuration is mandatory and critical for securing the SSH
    connection.
    When the server's key fingerprint cannot be verified, all connections
    are rejected.


address
^^^^^^^

:Default value: ''
:Optional: No
:Values: * Host name or IP address of the SFTP server.
:From version: 2.8.0
:Description:
    Address of the remote SSH server. IP or DNS name.


port
^^^^

:Default value: ''
:Optional: No
:Values: * Number, greater than 0.
:From version: 2.8.0
:Description:
    Port number of the remote SSH server.


username
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 2.8.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote SSH server.


password
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 2.8.0
:Values: * Plain text password.
         * `Disabled` or empty.
:Description:
    This option specifies the password used to connect to the remote SSH server.
    It is provided in plain text.
    To disable password authentication, set this to an empty string.

    When `ssh_private_key` is defined and configured to a private key which
    is stored in encrypted mode, this holds the password used to
    decrypt the private key.


ssh_private_key
^^^^^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.0.0
:Values: * Absolute path on the local filesystem.
         * Content of the SSH private key (Since 3.40.0).
         * `Disabled` or empty.
:Description:
    SSH private key used to authenticate to the remote SSH server.
    Leave it empty to disable SSH key authentication.

    It can be configured with a path on the local filesystem containing the
    content of the SSH key.

    You can also define the content of the SSH key directly as a text value.
    In this case the configuration will look like the following example.
    It's important to start each line with at least one space character and
    keep the number of leading spaces constant::

        [locations/b904e6h6-c295-4ccf-8abd-edcae4d3324f]
        name = SFTP Acme Server
        type = sftp
        ssh_private_key = -----BEGIN RSA PRIVATE KEY-----
            Proc-Type: 4,ENCRYPTED
            DEK-Info: AES-128-CBC,ACD9A45C68DD1924FF2A1A54BE2A7BF4

            RAHH7yMbPk/vrhT5jkSDGIUdH+nG0OQpeSWcQXd4JJ6pqdJh/cw/havtxlHFp1yz
            ...
            MORE SSH KEY CONTENT
            ...
            Pkf+23OGZln2dLz/pkJkiRRzmsWgT2hUv/EK4NYRQq1kEAXLf3J6xZqLlR3ZBLJm
            -----END RSA PRIVATE KEY-----

    We recommend to store the key in PEM OpenSSH format, but Putty or Tectia
    formats are also supported.

    When the configured key is encrypted, the value configured in `password`
    is used to decrypt the key.


proxy
^^^^^

:Default value: ''
:Optional: Yes
:Values: * `URI` like expression.
         * `socks5://12.342.421.2:8899`
:From version: 3.31.0
:Description:
    This option configures a proxy to be used when making connection
    to the remote server.

    When no port is defined, it will use port `1080`.

    Leave it empty to disable proxy usage.

    For now, only the SOCKS5 without authentication is supported.
    The DNS resolution will be delegated to the SOCKS server.


.. include:: /configuration/ssh-cipher-list.include.rst


FTP Location
------------

An `ftp location` provides access to an FTP server over the unencrypted mode.

Only username and password credentials are supported.

..  warning:
    When a FTP location is used, the username and password are sent in
    plaintext over the network.


address
^^^^^^^

:Default value: ''
:Optional: No
:Values: * Host name or IP address of the FTP server.
:From version: 3.0.0
:Description:
    Address of the FTP server. IP or host name.


port
^^^^

:Default value: `21`
:Optional: Yes
:Values: * Number, greater than 0.
:From version: 3.0.0
:Description:
    Port number to connect to the FTP server.


username
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 3.0.0
:Values: * Text.
:Description:
    Username used to authenticate to the FTP server.


password
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.0.0
:Values: * Plain text password.
         * `Disabled` or empty.
:Description:
    This option specifies the password used to connect to the FTP server.

    It is defined in plain text format and sent over the network in plain text
    without any transport protection.


debug
-----

:Default value: 'No'
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 4.0.0
:Description:
    When enabled, the location will emit events with id `20000`,
    containing low-level debug messages for the file transfer protocol.

    ..  warning::
        When this is enabled, emitted events may include used password
        in plain text.


Explicit FTPS Location
----------------------

An `explicit ftps location` provides access to an Explicit FTPS server.

..  note::
    The explicit FTPS location is an experimental feature.


address
^^^^^^^

:Default value: ''
:Optional: No
:Values: * Host name or IP address of the FTP server.
:From version: 3.13.0
:Description:
    Address of the server. IP or host name.

    In order to check the identity of the remote server the address should
    be provided as FQDN.
    IP addresses are not supported by the server identity validation process.


port
^^^^

:Default value: `21`
:Optional: Yes
:Values: * Number, greater than 0.
:From version: 3.13.0
:Description:
    Port number to connect to the server.


username
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 3.13.0
:Values: * Text.
:Description:
    Username used to authenticate to the server.


password
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.13.0
:Values: * Plain text password.
         * `Disabled` or empty.
:Description:
    This option specifies the password used to connect to the server.

    It is defined in plain text format and sent over the network protected
    by the TLS protocol.

.. include:: /configuration/ssl.include.rst


ftps_ccc
^^^^^^^^

:Default value: `Disabled`
:Optional: Yes
:From version: 3.13.0
:Values: * `Passive`
         * `Disabled`
         * Empty
:Description:
    This option specifies whether the security of the FTPS command connection
    should be downgraded to plain text after authentication.

    Leave it empty to keep the command connection secure.

    When this option is enabled, the SSL/TLS layer is shutdown after
    authenticating.
    The rest of the control channel communication will be done
    over an unencrypted connection.

    For more details about using this configuration option please check the
    dedicated documentation for the :ref:`FTPS CCC modes <operation-ftps-ccc>`.


Implicit FTPS Location
----------------------

An ``implicit ftps location`` provides access to an Implicit FTPS server.

..  note::
    The implicit FTPS location is an experimental feature.


address
^^^^^^^

:Default value: ''
:Optional: No
:Values: * Host name or IP address of the FTP server.
:From version: 3.13.0
:Description:
    Address of the server. IP or host name.

    In order to check the identity of the remote server the address should
    be provided as FQDN.
    IP addresses are not supported by the server identity validation process.


port
^^^^

:Default value: `990`
:Optional: Yes
:Values: * Number, greater than 0.
:From version: 3.13.0
:Description:
    Port number to connect to the server.


username
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 3.13.0
:Values: * Text.
:Description:
    Username used to authenticate to the server.


password
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.13.0
:Values: * Plain text password.
         * `Disabled` or empty.
:Description:
    This option specifies the password used to connect to the server.

    It is defined in plain text format and sent over the network protected
    by the TLS protocol.


.. include:: /configuration/ssl.include.rst


WebDAV over HTTPS Location
--------------------------

A `webdavs` location provides access to a WebDAV server over a protected HTTPS
connection.

SharePoint Online is the only WebDAV server currently supported.
Only username and password credentials are supported to authenticate against
the WebDAV server provided by SharePoint Online as part of the Office 365
claims-based authentication.

It is assumed that the WebDAV server handles the path in a case-insensitive
manner.
Please get in touch if your WebDAV server is case-sensitive.

Unlike a web browser, to protect the HTTPS connection you will have to
explicitly configure the list of trusted CA and the location of the CRLs.


url
^^^

:Default value: ''
:Optional: No
:Values: * URL
:From version: 4.11.0
:Description:
    Full URL address of the WebDAV server root page.

    For SharePoint Online you can define it as::

        url = https://YOUR-SITE.sharepoint.com

    For generic WebDAV servers you can define it as::

        url = https://files.example.com
        or
        url = https://files.example.com/path/webdav/resource

    Or if you need a custom port number use::

        url = https://files.example.com/path/webdav/resource

    When this is defined as an `http://` URL, the SSL configuration options
    are ignored.


username
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 3.20.0
:Values: * Text.
:Description:
    Username used to authenticate to the WebDAV server.


password
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.0.0
:Values: * Plain text password.
         * `Disabled` or empty.
:Description:
    This option specifies the password used to connect to the WebDAV server.

    It is defined in plain text format and sent over the network protected
    by the HTTPS connection.


proxy
^^^^^

:Default value: ''
:Optional: Yes
:Values: * `URI` like expression.
         * `connect://12.342.421.2:3128`
:From version: 3.20.0
:Description:
    This configuration adds the proxy used to connect to the final URL.

    For now, only the HTTP/1.1 CONNECT tunneling proxy method is supported.


authentication_method
^^^^^^^^^^^^^^^^^^^^^

:Default value: 'sharepoint-online'
:Optional: Yes
:Values: * `sharepoint-online`
         * `basic-authentication-scheme`
:From version: 4.12.0
:Description:
    The authentication method to use for connecting to the WebDAV server.

    The default value of `sharepoint-online` is used for the
    Microsoft SharePoint Online cloud service authenticated
    via the Microsoft single sign-on process.

    Another supported method is `basic-authentication-scheme`,
    the HTTP "Basic" access authentication, as per
    `RFC 7617 <https://tools.ietf.org/html/rfc7617>`_.


allow_insecure_http
^^^^^^^^^^^^^^^^^^^

:Default value: 'No'
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 4.12.0
:Description:
    When set to `Yes`, the WebDAV connection is made via insecure HTTP
    instead of HTTPS.

    ..  warning::
        This is useful for testing or troubleshooting,
        but is strongly discouraged in production,
        because it sends all communication including passwords and data
        as plaintext over the network.


.. include:: /configuration/ssl.include.rst


AS2 over HTTPS or HTTP Location
-------------------------------

An `as2` location allows sending files to a remote AS2 server.

The `as2` location can only be used for sending files over AS2.
If you need to receive files over the AS2 protocol, you will need to
configure the HTTP file transfer service.

Unlike a typical web browser connection, to protect an AS2 HTTPS connection
you will have to explicitly configure the list of trusted CAs and
the location of the CRLs.


url
^^^

:Default value: ''
:Optional: No
:Values: * .
:From version: 4.5.0
:Description:
    Receiving URL for your partner.

    SFTPPlus will use this URL to send files to your AS2 partner.

    When this is defined as an `http://` URL, the SSL configuration options
    are ignored.


username
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 4.5.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote AS2 partner server.

    Leave it empty when the remote AS2 partner doesn't require authentication.


password
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 4.5.0
:Values: * Plain text password.
         * Empty.
:Description:
    This option specifies the password used to connect to the remote
    AS2 partner server.

    It is ignored when `username` is empty.


as2_own_identifier
^^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: No
:From version: 4.5.0
:Values: * Text.
:Description:
    Identifier for your own local AS2 organization sending the files.


as2_own_certificate
^^^^^^^^^^^^^^^^^^^

:Default value: 'General server SSL certificate'
:Optional: No
:From version: 4.5.0
:Values: * PEM certificate.
         * PEM certificate and PEM private key.
:Description:
    Certificate for your own local AS2 organization used when
    signing files sent to a remote AS2 partner.

    The certificate should be configured in PEM format.

    This configuration can also contain the private key associated to the
    certificate.

    This can be empty when sending unsigned files.


as2_own_private_key
^^^^^^^^^^^^^^^^^^^

:Default value: 'General server SSL private key'
:Optional: No
:From version: 4.5.0
:Values: * PEM private key.
:Description:
    Certificate for your own local AS2 organization used when
    signing files sent to a remote AS2 partner.

    The certificate should be configured in PEM format.

    This configuration can also contain the private key associated to the
    certificate.


as2_partner_identifier
^^^^^^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: No
:From version: 4.5.0
:Values: * Text.
:Description:
    Identifier for the remote AS2 partner receiving the files.


as2_partner_certificates
^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: No
:From version: 4.5.0
:Values: * PEM certificate
         * Multiple PEM certificates
:Description:
    Certificate in PEM format used to encrypt files sent to the AS2
    partner and to validate the received signed MDN.

    You can define multiple PEM certificates for the case in which the partner
    uses different certificates for signing and encryption.

    Old and new PEM certificates can be defined at the same time
    for a partner's certificate rollover.

    When sending encrypted files, the first configured PEM certificate will
    be used for the encryption operation.


as2_send_security
^^^^^^^^^^^^^^^^^

:Default value: 'signed-and-encrypted'
:Optional: yes
:From version: 4.5.0
:Values: * `signed-and-encrypted`
         * `signed`
         * `encrypted`
         * `disabled`
:Description:
    This defines the method used to secure the file transfers on top of
    the standard security provided by the HTTPS protocol.

    When encrypting file content, the first certificate defined at
    `as2_partner_certificates` is used.

    When signing file content, the digest/hashing algorithm defined in
    `as2_signature_algorithm` is used.

    When defined as `disabled`, files are sent unsigned and unencrypted.


as2_mdn_receipt
^^^^^^^^^^^^^^^

:Default value: 'sync-signed'
:Optional: yes
:From version: 4.5.0
:Values: * `sync-signed`
         * `sync-unsigned`
         * `disabled`
:Description:
    This defines the method used to request the
    message disposition notifications (MDN) receipt.

    When requesting a signed MDN, it will make the request using the
    digest/hashing algorithm defined in `as2_signature_algorithm`.

    When defined as `disabled`, it will not request an MDN receipt.


as2_encryption_algorithm
^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: 'aes256'
:Optional: yes
:From version: 4.5.0
:Values: * `3des`
         * `aes128`
         * `aes192`
         * `aes256`
:Description:
    Symmetric encryption algorithm used to encrypt sent files.

    All algorithms use the Cipher Block Chaining (CBC) mode and PKCS#1 v1.5
    padding.


as2_signature_algorithm
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: 'sha256'
:Optional: yes
:From version: 4.5.0
:Values: * `md5`
         * `sha1`
         * `sha224`
         * `sha256`
         * `sha348`
         * `sha512`
:Description:
    Digest / Hashing algorithm used when signing sent files and
    requesting the MDN receipt.


as2_content_type
^^^^^^^^^^^^^^^^

:Default value: 'application/octet-stream'
:Optional: Yes
:From version: 4.5.0
:Values: * MIME content type
:Description:
    MIME content type used when sending AS2 files.


.. include:: /configuration/ssl.include.rst


Azure File Service Location
---------------------------

An `azure-file` location provides access over HTTPS to the
Azure File Service of an Azure Storage account.

The files stored in Azure File Service shares are accessible via the
SMB protocol and HTTP API.
Azure Files is specifically a network file system.
SFTPPlus will use the HTTPS-based API to manage the files.

The HTTPS connections will use the default list of `secure` ciphers and will
accept TLS v1.0, TLS v1.1 and TLS v1.2 protocols.

..  note::
    Unsecured HTTP access is not available.

..  note::
    The current implementation is tested using
    General-purpose v2 (GPv2) accounts.

Only storage account names with access keys are currently supported.
Please get in touch if you plan to use Azure Active Directory or
shared access signatures.

The path / url to the Azure File storage is case-sensitive.

When using Azure File locations, the source or destination path will be
defined as the name of the share (to or from where files are transferred)
followed by the targeted directory inside that share.
The path will look like ``/SHARE-NAME/DIR-IN-ROOT/PARENT-DIR``.

The requests made by SFTPPlus to the Azure Storage server are done using
the ``sftpplus-azure-file-UUID`` format.
Where UUID is a unique identifier for this location.
This can be used inside Azure Storage Analytics to identify the operations
done by this location.
The request ID will look like::

    x-ms-client-request-id: sftpplus-azure-file-60ec1329-cc5d-416e-81b9-7c22


username
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 3.36.0
:Values: * Text.
:Description:
    Name of the Azure Storage Account.


password
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.36.0
:Values: * Plain text.
:Description:
    Any of the two access keys for the Azure storage account.

    It should be specified in Base64 format.
    This is the default format presented by the Azure Portal.


SMB / Windows Share Location
----------------------------

An `smb` location provides access to an SMB version 3
(Server Message Block or Windows Share) server over TCP.
This does not include access over UDP or version 1 or 2.

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
^^^^^^^

:Default value: ''
:Optional: No
:Values: * Host name or IP address of the server.
:From version: 4.13.0
:Description:
    Address of the remote SSH server. IP or DNS name.

    If you are using Azure Files the address will have the following format:
    ``ACCOUNT_NAME.file.core.windows.net`` where ACCOUNT_NAME is replaced
    with your Azure Storage account name.


port
^^^^

:Default value: `445`
:Optional: No
:Values: * Number, greater than 0.
:From version: 4.13.0
:Description:
    Port number of the remote server.


username
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 4.13.0
:Values: * Text.
:Description:
    Username or storage account name used to authenticate to the remote server.

    Anonymous (guest) access is not yet supported.
    Contact us if you need support for connecting to a Windows Share without
    a username and password.


password
^^^^^^^^

:Default value: ''
:Optional: No
:From version: 4.13.0
:Values: * Plain text password.
         * `Disabled` or empty.
:Description:
    This option specifies the password or key used to connect to the remote
    server.
    It is provided in plain text.
