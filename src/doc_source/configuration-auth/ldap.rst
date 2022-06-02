LDAP / Active Directory
=======================

The `ldap` authentication method can be used to authenticate
`application` type accounts using the information provided by a remote LDAP
server.

LDAP and Secure LDAP over TLS/SSL (LDAPS) protocols are supported.

..  note::
    Only IPv4 LDAPS servers are supported.
    If you require IPv6 LDAPS, contact our support team.
    IPv6 LDAP servers are supported when configured using
    IPv6 address literals.

..  note::
    LDAP StartTLS method is not yet supported.
    If you require it, contact our support team.

..  contents:: :local:


Introduction
------------

Simple BIND operation is used for authenticating an account against the
LDAP server in order to validate the credentials received from a file
transfer client session.

When an authentication request is made for a transfer client session, SFTPPlus
will use the provided credentials (username and password) and forward them
to the configured LDAP server for validation.

..  note::
    The LDAP authentication method is a terminal method. Once the
    authentication chain has reached it, it will either accept or reject
    the credential and will not allow any other authentication to continue
    with validating the credentials.


..  note::
    Only LDAP v3 is supported. If you require a different version
    please contact our support team.

Successfully authenticated accounts are associated to the default group,
or to a specific group based on the `group_mapping` configuration.

.. include:: /configuration-auth/authentication-commons.include.rst


address
-------

:Default value: ''
:Optional: No
:Values: * Host name.
         * Fully qualified domain name resolving an IPv4 address.
         * IPv4 address.
         * IPv6 address.
:From version: 3.13.0
:Description:
    Host name, domain name or IP address used to connect to the remote
    LDAP server.


port
----

:Default value: `389`
:Optional: Yes
:Values: * Port number.
:From version: 3.13.0
:Description:
    Port number used by the remote LDAP server to receive client connections.


secure_connection
-----------------

:Default value: `No`
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 4.11.0
:Description:
    When set to `yes` the connection to the LDAP server will be protected
    by a TLS security wrapper.
    This will enabled LDAP over TLS/SSL communication method, also called
    `LDAPS`.

    ..  warning::
        Without the `ssl_certificate_authority` configuration, the LDAPS
        connect will use TLS, but the identity of the remote server will
        not be validated.
        Use `ssl_certificate_authority` to define the certificate
        authorities allowed to issue a certificate for the remote server.


bind_dn_type
------------

:Default value: `parent`
:Optional: No
:Values: * `parent`
         * `relative`
         * `absolute`
         * `direct-username`
:From version: 3.20.0
:Description:
    This field defines the method utilized to construct the LDAP DN that is
    administered for the LDAP authentication (BIND) request.

    With `bind_dn_type` set to `parent`
    (or the 'Username generated from Bind DN` option in the Local Manager GUI),
    a distinguished name applied for the bind
    (authentication) operation is generated using the following method:
    ``cn=USERNAME,BIND_DN_VALUE``.

    Under this method, there is no need for file transfer users to consider
    the LDAP structure when providing the username.
    They can authenticate based on the usual username.

    For example, if `bind_dn` is defined as ``ou=det,dc=example,dc=com`` and
    an authentication is requested for username ``John``, the LDAP
    authentication (bind) operation is set for DN as:
    ``cn=John,ou=det,dc=example,dc=com``.

    With `bind_dn_type` set to `absolute` (or 'Absolute DN' option in the
    Local Manager GUI), the value from `bind_dn` is ignored.

    When set to `absolute`, the end users will need to specify the full DN
    as part of the username.

    When `bind_dn_type` is set to `relative` (or 'Append to bind DN' option in
    the Local Manager GUI), the provided username will be used together with
    the value configured for `bind_dn` to construct the final DN administered
    for the LDAP authentication operation.

    With `bind_dn_type` set to `direct-username`,
    the username provided as part of the file transfer authentication process
    will be directly used for the LDAP BIND operation.
    Once authenticated, SFTPPlus will use the `username_attribute` to get the
    full DN associated with this username in order to obtain the configuration
    for the authenticated account.


bind_dn
-------

:Default value: ''
:Optional: No
:Values: * Base distinguished name.
         * Multiple base DNs, one per line (Since 4.16.0)
:From version: 3.13.0
:Description:
    Base DN used to generate the distinguished name associated with the
    account which needs to be authenticated.

    The exact way in which the `bind_dn` is constructed will depend on the
    `bind_dn_type` configuration.

    For more details, consult the documentation for `bind_dn_type`.

    When `bind_dn_type` is set to `direct-username`, this is used as the
    base DN of the Active Directory group to which access is permitted.

    Multiple base DNs can be defined, one per line.
    This can be used for authenticating account from multiple organizations
    inside the same LDAP tree or for a multi-tree / forest LDAP deployment.
    They will be checked from top to bottom and the authentication will succeed
    on the first base DN in which the account is found.

    This is ignored when `bind_dn_type` is set to `absolute`.


username_attribute
------------------

:Default value: `cn`
:Optional: Yes
:Values: * Attribute name.
         * Attribute name, @FQDN.DOMAIN.COM
:From version: 3.17.0
:Description:
    The attribute name that LDAP uses to create the DN for performing the
    LDAP BIND (authentication) operation.

    It is also used to create the DN from which the user configuration is
    retrieved.

    Together with `bind_dn`, this is used to configure the full DN used for a
    specific username.

    As an example, if `bind_dn` is defined as ``dc=example,dc=com``,
    `username_attribute` is defined as `uid`, and the authentication is
    requested for username ``John``, the LDAP authentication
    (bind) operation is set for DN as: ``uid=John,dc=example,dc=com``.

    When `bind_dn_type` is `direct-username`,
    this attribute is used to search the LDAP directory and retrieve the DN
    of the authenticated account.

    ..  note::
        This option is ignored when `bind_dn_type` has any value other than
        `parent` or `direct-username`.


username_suffix
---------------

:Default value: Empty
:Optional: Yes
:Values: * Empty
         * @FQDN.DOMAIN.COM
:From version: 4.1.0
:Description:
    When `bind_dn_type = direct-username` you can use this configuration
    to define a default domain that is appended to the name of each use.

    In this way, the file transfer users can login with just the username,
    and SFTPPlus will use the full UPN for the Active Directory
    authentication request.

    The domain name should include the `@` character.
    For example: `username_suffix = @ad.example.com`.


home_folder_attribute
---------------------

:Default value: `homeDirectory`
:Optional: Yes
:Values: * Attribute name.
         * Attribute name, home path template
         * Empty value.
:From version: 3.13.0
:Description:
    Name of the attribute used to retrieve the home folder path for the
    account which is authenticated.

    When the LDAP entry associated with the authenticated account has no
    such attribute or the attribute's value is empty the authentication will
    fail.

    Leave it empty to not retrieve the home folder path from the
    LDAP entry, but rather inherit the value from the associated group.

    You can create the home folder path by combining a configurable template
    and the value stored in the LDAP attribute.
    For example to reuse the Internet Information Service (MS IIS)
    user path, you can use::

        home_folder_attribute: msIIS-FTPDir, E:\SFTP-Files\{msIIS_FTPDir}

    ..  note:
        The authentication will fail when the LDAP entry associated with the
        account to be authenticated has multiple values for the home
        folder attribute.


extension_entry_point
---------------------

:Default value: Empty
:Optional: Yes
:Values: * API extension expression.
         * Empty.
:From version: 4.16.0
:Description:
    The API entry point is defined in the format `LANGUAGE:DOTTED.ENTRY.POINT`,

    `LANGUAGE` is the name of the language in which the extension is
    written.

    `DOTTED.ENTRY.POINT` as an expression defining the package, module, and
    class name which will receive the event.

    ..  note::
        At this moment, the event handler API supports the development of
        custom handlers based on the Python programming language.

    As an example, for the file ``extension/auth_ldap_noop.py`` defining
    the ``AuthLDAPNoop`` class, the configuration will be::

        extension_entry_point = python:auth_ldap_noop.AuthLDAPNoop


extension_configuration
-----------------------

:Default value: Empty
:Optional: Yes
:Values: * JSON
         * Empty
:From version: 4.16.0
:Description:
    A JSON value which is passed to the extension.

    This is ignored when `extension_entry_point` is not defined.


search_filter
-------------

:Default value: ''
:Optional: Yes
:Values: * LDAP search expression.
         * Empty value.
:From version: 3.33.0
:Description:
    The LDAP authentication method can also filter accepted LDAP entries,
    based on an LDAP search filter,
    to restrict access to the file transfer services.

    For example, if you only want to allow access to members of the group
    `file-transfer` you can use the following search filter
    ``(memberOf=file-transfer)``

    Leave it empty to accept any LDAP entry, regardless of its attributes.

    For more information about the search filters, check the documentation
    of your LDAP server in order to discover the search capabilities supported
    by the server.


manager_search_filter
---------------------

:Default value: ''
:Optional: Yes
:Values: * LDAP search expression.
         * Empty value.
:From version: 3.37.0
:Description:
    LDAP filter to select the LDAP entries allowed to act as
    administrators for the Local Manager service.

    For example, if you only want to allow access to members of the group
    `file-transfer-admins` you can use the following search filter
    ``(memberOf=file-transfer-admins)``

    Leave it empty to deny any LDAP entry as administrator.


.. _conf-ldap_group_mapping:

group_mapping
-------------

:Default value: ''
:Optional: Yes
:Values: * Group UUID.
         * Comma separated LDAP attribute name, matching value, and group UUID.
         * Comma separated list of group UUIDs (Since 4.20.0)
         * Empty value.
:From version: 3.34.0
:Description:
    The LDAP group mapping configuration can be used to augment the LDAP data
    without updating the actual LDAP entries.

    Setting to a single group UUID, or a list of UUIDs,
    will associate all the LDAP authenticated
    accounts to the SFTPPlus groups having that UUID.
    For more details, see the
    :doc:`dedicated LDAP group mapping documentation</guides/ldap>`.

    You can create complex group mapping by specifying multiple groups which
    are selected based on targeted LDAP values.

    The matching for LDAP attribute names is case insensitive.

    Leave this configuration option empty to use the default
    SFTPPlus group configuration.

.. include:: /configuration/ssl.include.rst
