SFTP
====

An `sftp location` provides access to an SFTP (version 3) server over SSH
(version 2).
This does not include access over SCP.

..  contents:: :local:


Introduction
------------

As the connection is done in non-interactive mode, the identity of the remote
SSH server needs to be verified, so that credentials are not sent to an
untrusted remote SSH server.

To validate the remote SSH server, the fingerprint of its public key is
stored as a hexadecimal string in the `ssh_server_identity` option.

An SSH server can authenticate users using either a password or an SSH key.

.. include:: /configuration-client/locations-commons.include.rst


ssh_server_identity
-------------------

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
-------

:Default value: Empty
:Optional: No
:Values: * Host name or IP address of the SFTP server.
:From version: 2.8.0
:Description:
    Address of the remote SSH server. IP or DNS name.


port
----

:Default value: Empty
:Optional: No
:Values: * Number, greater than 0.
:From version: 2.8.0
:Description:
    Port number of the remote SSH server.


username
--------

:Default value: Empty
:Optional: No
:From version: 2.8.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote SSH server.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 2.8.0
:Values: * Plain text password.
         * Empty.
:Description:
    This option specifies the password used to connect to the remote SSH server.
    It is provided in plain text.
    To disable password authentication, set this to an empty string.

    When `ssh_private_key` is defined and configured to a private key which
    is stored in encrypted mode, this holds the password used to
    decrypt the private key.


ssh_private_key
---------------

:Default value: Empty
:Optional: Yes
:From version: 3.0.0
:Values: * Absolute path on the local filesystem.
         * Content of the SSH private key (Since 3.40.0).
         * Empty.
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
-----

:Default value: Empty
:Optional: Yes
:Values: * `URI` like expression.
         * `socks5://12.342.421.2:8899`
         * Empty
:From version: 3.31.0
:Description:
    This option configures a proxy to be used when making connection
    to the remote server.

    When no port is defined, it will use port `1080`.

    Leave it empty to disable proxy usage.

    For now, only the SOCKS5 without authentication is supported.
    The DNS resolution will be delegated to the SOCKS server.


.. include:: /configuration/ssh-cipher-list.include.rst
