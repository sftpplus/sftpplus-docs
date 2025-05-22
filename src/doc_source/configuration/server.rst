Server's process
================

..  contents:: :local:


Introduction
------------

When launched, the server starts a series of file transfer services, using
various file transfer protocols.
It also starts the internal services used by all file transfer services;
for example, the authentication service and the log service.

All services are executed under a single server process.

This page describes general server configuration options and options
affecting all file transfer services.


You can access the section via the 'Server' page in Web Manager.

..  image:: /_static/gallery/gallery-test-server.png

----

For text configuration, options affecting all services are grouped inside the
``server`` section.

Below is another sample for the ``server`` section as a text configuration::

    [server]
    uuid = 530019d0-92ce-11e2-9e96-0800200c9a66
    name = Short_Name_For_Server
    description = Long text describing the server
    account = sftpplus
    umask = 022
    authentications = 0022b17a-30a0-4b70, ffa9-bd05-51c2-42f1


uuid
----

:Default value: ``single-server-uuid``
:Optional: No
:Values: * An unique identifier among all servers active in a deployment
         * Alphanumeric and dash ('-') character.
           No space characters.
:From version: 2.0.0
:Description:
    The universally unique identifier (UUID) allows the server to be
    identified when multiple servers are active in the same deployment.

    It can be any unique string, but we recommend using the UUID standard
    format.

    When aggregating audit entries (logs) or authentication requests from
    multiple servers, the UUID is used to identify the source server.

    UUIDs are intended to be used for low-level server implementations.
    For a human-readable name, please use the `name` attribute.

..  note::
    Once a UUID is defined, it is not recommended to change it.

    To generate a UUID value, please check the dedicated documentation for
    :ref:`admin-commands generate-uuid <generate-uuid>`.

    For more details, please check `Wikipedia's article on UUID
    <http://en.wikipedia.org/wiki/Universally_unique_identifier>`_.


name
----

:Default value: ``single-server-name``
:Optional: No
:Values: * Human-readable name for this server.
         * This may be a fully qualified domain name (FQDN).
         * Any text.
:From version: 2.0.0
:Description:
    This is a human-readable companion for the UUID.

    As long as the UUID is not changed, you can change the name at any time,
    and the server will still be recognized in a multiple deployment
    architecture.


description
-----------

:Default value: ''
:Optional: Yes
:Values: * Free form text describing this server.
:From version: 2.0.0
:Description:
    This can be used for any free form text attached to this server.
    It can include contact information about the system administrator, comments
    or other details specific to the installation.


product_key
^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Empty
         * `server-only`
         * `client-only`
:From version: 4.21.0
:Description:
    The current version of SFTPPlus doesn't require any product key in order to operate.
    Both server-side and client-side functionalities are available inside
    the same product.
    This configuration is here to prepare for the introduction of a `product key` in the next major release.

    This configuration option can now be used to simplify the available configuration options from the web management interface.

    Set this value to `server-only` to only see the configuration options relevant to file transfer servers operations.

    Set this value to `client-only` to only see the configuration options relevant to automated client transfer operations.

    Managed file transfer configuration options like the event handler or the activity audit are always available from the web console.


account
-------

:Default value: ``sftpplus``
:Optional: Yes
:Values: * A user under which the server will operate.
         * Empty
:From version: 1.6.0
:Description:
    This is a system account used by the server to run its main operations with
    restricted privileges on Unix-like systems.

    To disable running the server under a dedicated account leave this
    value empty.

..  note::
    This option is ignored on Windows systems, where the server will operate
    under the same account as the one used for starting the server.


umask
-----

:Default value: ``022``
:Optional: Yes
:Values: * Filemask in octal format.
:From version: 1.7.0
:Description:

    User mask file permissions (filemask) used for creating
    new files and folders on the server.

    When creating new files, the server will use the 0666 mode, masked with
    the value of umask.

    When creating new folders, the server will use the 0777 mode, masked with
    the value of umask.

..  note::
    This option is ignored on Windows systems.


authentications
---------------

:Default value: `DEFAULT-AUTHENTICATION`
:Optional: Yes
:Values: * List of authentication UUIDs.
:From version: 2.10.0
:To version:
:Description:
    Comma-separated list of UUIDs with global authentication methods enabled on
    this server.

    The list should be ordered by priority.
    The server will try to use the first authentication from the list, and
    continue with the next method if the user is not accepted.

    When not present, it defaults to the SFTPPlus embedded authentication.

..  note::
    When a service defines its own authentication list, this global
    configuration is ignored.


password_minimum_strength
-------------------------

:Default value: `4`
:Optional: Yes
:Values: * 0
         * 1
         * 2
         * 3
         * 4
:From version: 3.43.0
:To version:
:Description:
    This defines the minimum strength element of the password policy
    applied when setting passwords through Web Manager.

    This does not enforce the policy for already defined passwords or
    for passwords defined outside of SFTPPlus, such as OS passwords.

    The available values are from `0` to `4` where `0` is a weak password
    while `4` is a password which is considered strong.

    The following minimum lengths are defined for each strength level:

    * 0 - no length limit.
    * 1 - 4 characters
    * 2 - 7 characters
    * 3 - 9 characters
    * 4 - 11 characters


password_minimum_length
-----------------------

:Default value: `8`
:Optional: Yes
:Values: * Number
:From version: 3.43.0
:To version:
:Description:
    This defines the minimum length element of the password policy
    applied when setting passwords through Web Manager.

    This does not enforce the policy for already defined passwords or
    for passwords defined outside of SFTPPlus, such as OS passwords.

    Set it to `0` to disable password length checking.


password_history
----------------

:Default value: `8`
:Optional: Yes
:Values: * Number
:From version: 4.10.0
:To version:
:Description:
    This defines the number of unique new passwords that must be associated
    with a user account before an old password can be reused.

    Set it to `0` to disable the password history policy.

    If `password_history` was previously enabled and is now disabled,
    updating the password for an account will clear the history
    of previously used passwords for that account.


password_hashing_scheme
-----------------------

:Default value: `crypt-sha512`
:Optional: Yes
:Values: * `crypt-sha512`
         * `crypt-sha256`
         * `pbkdf2_sha512`
         * `pbkdf2_sha256`
:From version: 3.51.0
:To version:
:Description:
    This defines the function used to hash the passwords of the
    internal SFTPPlus user and administrator accounts. Not
    applicable for OS accounts.

    The following hash functions are supported:

    * `crypt-sha512` - Unix Crypt SHA-512
    * `crypt-sha256` - Unix Crypt SHA-256
    * `pbkdf2-sha512` - RSA PKCS #5 based on SHA-512
    * `pbkdf2-sha256` - RSA PKCS #5 based on SHA-256

    For more info see the dedicated
    :doc:`Modular Crypt Password Hashing </standards/cryptography>` section
    from our Supported Cryptographic Standards documentation page.


ssl_certificate
---------------

:Default value: Empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
         * Certificate in PEM text format.
         * Certificate in PKCS12 / PXF binary format.
         * Empty
:From version: 1.6.0
:Description:
    Certificate or chain of certificates in Privacy-Enhanced Mail (PEM) format
    or an absolute path on the local filesystem for a file containing
    a certificate or a chain of certificates in PEM format
    to be used by default for TLS/SSL services.

    File content must be encoded in the Privacy-Enhanced Mail (PEM) or
    the PKCS12 / PFX formats.


ssl_key
-------

:Default value: Empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
         * Key as PEM text format.
         * Empty
:From version: 4.0.0
:Description:
    X.509 private key in Privacy-Enhanced Mail (PEM) format
    or an absolute path on the local filesystem for a file containing
    a X.509 private key to be used by default for TLS/SSL services.


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

    For Putty keys, since they are not using a PEM format,
    only a single private key is supported.
    If you have to use multiple Putty keys here,
    convert them to a PEM format such as the OpenSSH one.

    You can also configure it with one or more absolute paths on the
    local filesystem to files containing private SSH keys.
    One path per line.


blocking_filesystem
-------------------

:Default value: No
:Optional: Yes
:Values: * Yes
         * No
:From version: 5.5.0
:Description:
    When handling files from the local filesystem of the operating system,
    SFTPPlus assumes files are always available and filesystem operation is not blocking.

    When using non-local filesystem,
    especially high-latency ones like a slow NFS server,
    it can happen that filesystem operations are blocking, which might have the side-effect
    of apparently freezing SFTPPlus.

    In such cases, set this configuration to `Yes` to improve the responsiveness of SFTPPlus.

    ..  note::
        The current SFTPPlus version only supports blocking filesystems for the server-side SFTP protocol.
        Support for more protocols will be added in future releases.

    ..  attention::
        Enable this option has an important performance penalty of about 70%.


failover_interval
-----------------

:Default value: 0
:Optional: Yes
:From version: 5.13.0
:Values: * Number of seconds
:Description:
    This is the number of seconds used to increase the `stable_interval` configuration option for all transfers and filesystem monitors on this node.

    This allows configuring *primary* and *secondary* nodes, in which the transfer are first executed on the primary node. If the primary node fails to transfer the files, the secondary node will try to transfer the files again with a delay configured via the `failover_interval`.

    You should set this to `0` for the *primary node*.

    This is primarily designed to be used as part of cluster operations.
    For more details, see the
    :doc:`transfers cluster </cluster/transfers>` documentation page.
