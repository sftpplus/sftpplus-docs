SSH (SFTP and SCP)
==================

This page describes the configuration options available for the SSH service,
using SFTP and SCP file transfer protocols.

..  contents:: :local:


Introduction
------------

Both the SFTP and the SCP protocols make use of the SSH protocol for low-level
encryption of transferred data.
Due to this, SFTPPlus uses a generic SSH service that provides
support for both `sftp` and `scp` services.
SFTP and SCP can be independently enabled.

Multiple SSH services can share the same set of RSA and DSA host keys.

.. _ssh-key-authentication:


Configuring SSH key-based authentication on the server
------------------------------------------------------

An account can have both password and SSH keys authentication methods
enabled at the same time.
At connection time, the SSH server and client will perform a negotiation step
and the server will use only one method for authenticating the session.

Password authentication can be disabled for an account, in which case the
server will force the client to use SSH keys for authentication.

An account is configured with one or many public SSH keys (a list).
When the same account is used to connect from multiple machines, you will want
to generate one pair of SSH keys for each machine, so that a private key never
leaves the machine on which it is used.

For each account, there is an associated local file.
It contains the public SSH keys, in OpenSSH public key format, accepted during
the authentication.

To add a public key, you will have to copy the content of the public key from
the file usually named ``KEY_NAME.pub`` and paste it on a new line into the
file containing the list of allowed SSH keys.

..  note::
    There is no restriction to having an 1:1 relation between an account and
    the list of public SSH keys.
    The same list (i.e. same local file) can be associated with multiple
    accounts.

There are two main approaches for configuring SSH keys for an account:

#. Only the server's administrators can manage the list of allowed SSH keys.
   In this case the file containing allowed SSH keys is stored somewhere
   outside the account's home folder.

#. Allow an account to have access to its own list of allowed SSH keys.
   Server administrators can still manage the list.
   The file with the list of allowed public SSH keys is stored `inside`
   the account's home folder.
   This is similar to OpenSSH configuration, where the list is stored in
   ``.ssh/authorized_keys`` file.


Web Manager GUI configuration
-----------------------------

Configuring the list of authorized SSH keys for an Account:

Create a local file where public SSH keys associated with this account are
stored.
In our example, the file is located at ``c:\\Users\\sftp_access\\John_keys``

----

Go to the account's configuration page and enter the path in the
`Allowed SSH Keys Path` field.

..  image:: /static/configuration/Accounts-Allowed-SSH-Keys.png


For the above configuration, the account's home folder is in
``c:\\Users\\John`` and it has no access to manage its own SSH keys.

----

Configuring the list of authorized SSH keys for a Group:

Note that the path must contain the `${USER}` value as a placeholder linking
to the username.

..  image:: /static/configuration/Groups-Allowed-SSH-Keys.png

In the example above, the file path included `${USER}`.
The text file equivalent::

    [groups/bdfe8e48-5100-4d8a-bac1-441ebc04f9a7]
    name = Support_Group
    ssh_authorized_keys_path = /home/${USER}/.ssh/authorized_keys

In the above examples, the server will read the authorized SSH keys file
located at ``/path_to/john/authorized_keys`` for a `${USER}` called
``john``.

If the path does not include the ${USER} value, it is appended at the end.

Therefore, a file path of ``/authorized_keys`` is read as
``/path_to/authorized_keys/john`` for a `${USER}` called ``john``.

..  warning::
    Make sure that the file path is set correctly, otherwise the server will
    fail to read the authorized SSH keys file and issue a
    `No such file or directory` error.


Text file configuration
-----------------------

The `ssh_authorized_keys_path` option from the configuration file specifies
the path to the file containing the list of allowed SSH RSA/DSA public keys
for each user.

In text file configuration, the path can contain the `${USER}` value::

    [groups/DEFAULT_GROUP]
    ssh_authorized_keys_path = /home/${USER}/.ssh/authorized_keys

When ``john`` is authenticated, the server will seek out the authorized SSH
keys file ``/home/john/.ssh/authorized_keys/``.

To disable SSH key-based authentication leave this value empty,
as in the example below::

    [groups/DEFAULT_GROUP]
    ssh_authorized_keys_path =


Below you can find the list of available configuration options.

.. include:: /configuration-server/service-commons.include.rst


sftp
----

:Default value: `Yes`
:Optional: Yes
:Values: * No - To disable SFTP support.
         * Yes - To enable SFTP support.
:From version: 2.5.0
:Description:
    Enable/Disable support for the SFTP protocol.


scp
---

:Default value: `No`
:Optional: Yes
:Values: * No - To disable SCP support.
         * Yes - To enable SCP support.
:From version: 2.5.0
:Description:
    Enable/Disable support for the SCP protocol.


ssh_host_private_keys
---------------------

:Default value: Empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
         * Multiple absolute paths on the local filesystem, one per line.
         * Text version of a SSH private key.
         * Multiple concatenated SSH private keys in PEM format.
         * Empty.
:From version: 4.9.0
:Description:
    One or more SSH host private keys used by default for the SSH-based
    services (SFTP/SCP).

    It can be one or more concatenated SSH private keys in PEM format.

    It's important to start each line with at least one space character and
    keep the number of leading spaces constant::

        [server/b904e6h6-c295-4ccf-8abd-edcae4d3324f]
        name = SFTP Internal Server
        type = sftp
        rsa_private_key = -----BEGIN RSA PRIVATE KEY-----
            Proc-Type: 4,ENCRYPTED
            DEK-Info: AES-128-CBC,ACD9A45C68DD1924FF2A1A54BE2A7BF4

            RAHH7yMbPk/vrhT5jkSDGIUdH+nG0OQpeSWcQXd4JJ6pqdJh/cw/havtxlHFp1yz
            ...
            MORE SSH KEY CONTENT
            ...
            Pkf+23OGZln2dLz/pkJkiRRzmsWgT2hUv/EK4NYRQq1kEAXLf3J6xZqLlR3ZBLJm
            -----END RSA PRIVATE KEY-----
            -----BEGIN DSA PRIVATE KEY-----
            H7yMbPk/vrhT5jkSDGIUdH+nG0OQpeSWcQXd4JJ6pqdJh/cw/havtxlHFp1yz
            MORE SSH KEY CONTENT
            OGZln2dLz/pkJkiRRzmsWgT2hUv/EK4NYRQq1kEAXLf3J6xZqLlR3ZBLJm
            -----END DSA PRIVATE KEY-----

    For Putty keys, since they are not using a PEM format,
    only a single private key is supported.
    If you have to use multiple Putty keys here,
    convert them to a PEM format such as the OpenSSH one.

    You can also configure it with one or more absolute paths on the
    local filesystem to files containing private SSH keys.
    One path per line.

    We recommend to store keys in PEM OpenSSH format, but Putty or Tectia
    formats are also supported.

    ..  note::
        The SSH key types configured here are advertised during SSH handshake
        as the list of supported host key algorithms.
        If you want to restrict the RSA host key variants,
        configure the list accepted RSA host key algorithms via `ssh_cipher_list`.


dh_prime_size
-------------

:Default value: `1024, ideal`
:Optional: Yes
:Values: * Pair of comma-separated values: absolute minimum, preferred size.
:From version: 3.46.0
:Description:
    This option controls the size of the prime number used during the
    Diffie-Hellman group exchange.

    This is a single pair of comma-separated values.

    The first value defines the absolute minimum size.
    The authentication will fail if the maximum remote peer is smaller than
    the minimum size.

    The following sizes are supported:

    * 1024
    * 1536
    * 2048
    * 3072
    * 4096
    * 6144
    * 8192

    The second value defines the negotiated size used based on sizes
    announced by the client. The available are:

    * `minimum` - Use the minimum value supported by the client and server.
    * `ideal` - Use the ideal value advertised by the client.
    * `maximum` - Use the maximum value supported by the client.

    As an example, when this is configured as `dh_prime_size = 2048, ideal`
    and the client is advertising a minimum of `1024`, an ideal value of `2048`
    and a maximum of `4086`, the used value is `2048`.


before_login_message
--------------------

:Default value: `empty``
:Optional: Yes
:Values: * Any text message.
:From version: 5.11.0
:Description:
    Message used by the service to welcome users, before asking for credentials.

    The message is sent using UTF-8 encoding with the language tag at `en`.

    Leave it `empty` not to send any pre authentication message.

    ..  note::
        Most SFTP GUI clients will ignore this message.
        Only a few SFTP clients like WinSCP will show this message.

        For command line or script SFTP clients the message might interfere with the scripted functionality.
        For example, a SFTP script might expect a specif message and might break when the message is changed.


ignore_create_permissions
-------------------------

:Default value: `No`
:Optional: Yes
:Values: * `No`
         * `Yes`
:From version: 1.7.13
:Description:
    Some SFTP clients, like the OpenSSH SFTP client, will always preserve file
    and folder permissions and attributes even if -p option is not used in the
    client.

    To work around this problem, the server can be configured to ignore the
    client request to set the permissions and attributes when creating a file
    or folder.

    This also ignores setting the permissions and attributed for opened files,
    not only for opened files which were just created.

    When permissions are ignored, the default file mode (666) is applied.

    Before setting the permission, the configured `umask` value is first
    masked against the permissions.

    ..  note::
        In the case in which you want to mirror the local permissions
        and attributes,
        use the SFTP client's dedicated command for setting the permissions.

.. include:: /configuration/ssh-cipher-list.include.rst
