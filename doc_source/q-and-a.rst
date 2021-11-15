Frequent Questions and Answers
==============================

..  contents:: :local:


Users and group configuration
-----------------------------


How to disable operating system accounts not defined in the configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SFTPPlus will associate all operating system accounts not defined
in the configuration file with the group named `DEFAULT_GROUP`.

To disable these accounts you will have to disable the `DEFAULT_GROUP` group.

Here is an example of a disabled `DEFAULT_GROUP`::

    [groups/DEFAULT_GROUP]
    enabled = No
    type = group


How to enable only a subset of the operating system accounts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To enable only a subset of the operating system accounts, you will first need
to disable the default group associated with OS accounts, `DEFAULT_GROUP`,
and then create a new group dedicated to the specific OS accounts that you
want to enable on the server.

Here is an example in which `DEFAULT_GROUP` is disabled, a new group is
created with the name `os_file_transfer`, and the specific OS account
``mike`` is associated with the new group::

    [groups/DEFAULT_GROUP]
    enabled = No
    type = group

    [groups/eg3b699a-8954-4257-aabe-437e21f37a10]
    name = os_file_transfer
    enabled = Yes
    type = group
    home_folder_path = ${OS_HOME}
    ssh_authorized_keys_path = Disabled
    allow_certificate_authentication = No

    [accounts/df3b699a-1122-4257-aabe-437e21f37a14]
    name = mike
    enabled = yes
    type = os
    group = os_file_transfer
    home_folder_path = Inherit

..  note::
    No password is defined for the ``mike`` account.
    As an `os` account, the password is provided by the operating system.
    `home_folder_path` is set as `Inherit` for ``mike``, so that it will
    use the group's home folder path.
    If the group's `home_folder_path` is defined as `${OS_HOME}`, it will
    be retrieved from the operating system.


What is the 0.0.0.0 IP address?
-------------------------------

When SFTPPlus is started or running and the configuration is still unchanged
since installing, the log will show a large amount of entries regarding the IP
address `0.0.0.0`.
This is the expected behavior as many of the services which are part of the
initial configuration are listening for new connections using `0.0.0.0`.

To quote Wikipedia, "In the context of servers, 0.0.0.0 means 'all IPv4
addresses on the local machine'."
If a host has two IP addresses, 192.168.1.1 and 10.1.2.1, and a server running
on the host listens on 0.0.0.0, it will be reachable at both of those IPs."

In the context of client-side connection, `0.0.0.0` means that SFTPPlus will
let the OS decide which source IP to use for connecting to a server.
With such a configuration, a client-side connection can use different source IP
address, based on the destination IP.
The operating system will automatically choose the optimal source IP address to
be used for a client-side connection.


How to configure an account to use a home folder path provided by the OS
------------------------------------------------------------------------

For accounts authenticated via the operating system, the server can be
configured to use the home folder path provided by the operating system.
This is done by using the special value `${OS_HOME}` as the configured path.
The `${OS_HOME}` placeholder is also available for groups, so multiple
accounts can be configured using this placeholder.

Here is an example::

    [groups/03288e36-cg9b-4bd5-a9be-f421372f17e6]
    name = GroupA
    enabled = yes
    type = group
    home_folder_path = ${OS_HOME}

    [accounts/03289h36-cf6b-4bd5-a9be-f421372f17e6]
    name = mary_smith
    enabled = yes
    type = os
    group = some_group
    home_folder_path = Inherit

    [accounts/09288e36-cf6b-4bd5-a9be-f421372f17e5]
    name = joe_accounting
    enabled = yes
    type = os
    group = other_group
    home_folder_path = ${OS_HOME}


FTP and FTPS Service
--------------------


How to generate an X.509 SSL self-signed certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can generate a self-signed certificate using the following `openssl`
command::

    $ openssl req \
      -x509 -nodes -days 365 \
      -newkey rsa:1024 -keyout certificate_key.pem -out certificate.pem

To generate a valid certificate, the Common Name (CN) fields should be set to
the server's address (for server certificates) or the client's user name
(for client certificates).

The command will generate the following files:

 * ``certificate_key.pem`` - Private key file used only by the certificate
   holder.

 * ``certificate.pem`` - Public certificate file used by all peers that need to
   validate the identity of the certificate's holder.


|Mutual_SSC|
^^^^^^^^^^^^

.. |Mutual_SSC| replace::
    How to implement mutual X.509 SSL authentication using only self-signed
    certificates?

First of all, you will need to create pairs of self-signed certificates and
keys for the client and the server.

You should have the following files:

 * ``server_key.pem`` - the server's private key.
 * ``server_cert.pem`` - the server's self-signed certificate.
 * ``client_key.pem`` - the client's private key.
 * ``client_cert.pem`` - the client's self-signed certificate.

To connect and validate the server, the client will use the following files:

 * ``client_cert.pem`` and client_key.pem for identifying the client to the
   server.
 * ``server_cert.pem`` as the accepted Certificate Authority.

To accept and validate the client, the server will use the following files:

 * ``server_cert.pem`` and server_key.pem for identifying the server to the
   client.
 * ``client_cert.pem`` as the accepted Certificate Authority.


How to enable PKI X.509 SSL certificate-based authentication in FTPS?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SSL certificate-based authentication allows clients to authenticate using
username and SSL certificate pair credentials.
A password is no longer required in this case.

To enable SSL certificate-based authentication, you will have to set the
following option inside the FTP/FTPS service configuration section (located by
default in `configuration/server.ini`)::

    [services/00feb81f-a99d-42f1-a86c-1562c3281bd9]
    name = ftps
    enable_ssl_certificate_authentication = Yes

This option is enabled by default, so you should already have this option set.

A valid SSL certificate should have the value of the Common Name (CN) field
match the authenticated username.


How to disable SSL certificate-based authentication?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To disable SSL certificate-based authentication, you will have to set the
following option inside the FTP/FTPS service configuration section (located by
default in `configuration/server.ini`)::

    [services/11feb81f-a99d-42f1-a86c-1562c3281bd9]
    name = ftp
    enable_ssl_certificate_authentication = No

After disabling SSL certificate-based authentication, you must check that
password-based authentication is enabled, otherwise clients will have no
other authentication method available to log in.


SSH (SFTP/SCP) Service
----------------------


How to generate RSA and DSA SSH private and public keys?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Local Manager service provides a tool for generating new SSH keys
or converting existing SSH keys.


How to enable / disable SSH key-based authentication?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please refer to
:doc:`the SSH service configuration page<configuration/ssh-service>`.


How to use PKI X.509 SSL certificates for authenticating over SFTP?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At this moment, the SFTPPlus SFTP service does not support PKI X.509
SSL certificate authentication.
SSL certificate authentication, together with self-signed SSL certificates
are supported using the FTPS protocol.
For more information, please refer to
:doc:`FTP/FTPS service configuration page<configuration/ftp-service>`.

The reason why SSL certificate authentication is not available for SFTP
is that this is not a standard authentication method for the SSH and the SFTP
protocols.

Implementing such a feature would involve breaking the compatibility of
SFTPPlus with all other standard SFTP clients and
forcing customers to use our non-standard SFTPPlus SFTP Client implementation.

We are aware that in some cases some partners are willing to
make this trade-off.
This is why we plan to add SSL certificate support for SFTP in the near future.
