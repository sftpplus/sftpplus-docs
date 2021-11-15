Authentication methods
======================

..  contents:: :local:

An authentication method configuration provides the required information to
allow SFTPPlus to use a specific method in order to authenticate
file transfer accounts and administration account.

You can define multiple authentication methods.
You can configure the order in which these methods are used.

Consult the `type` configuration option to see the list of supported
authentication methods.

..  note::
    Not all authentication method types support authenticating the
    administrators for the Local Manager service.


Adding a new authentication method via Local Manager
----------------------------------------------------

A new authentication method can be added or changed via Local Manager below.
Options will differ depending on which authentication method is used.

See below for an example starting configuration for the LDAP method of
authentication.

..  image:: /_static/gallery/gallery-add-ldap-auth.png


Adding a new authentication method via text configuration
---------------------------------------------------------

Adding a new authentication method is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``authentications/`` and
followed by the method's UUID.

The method's UUID can be any unique string used to identify the authentication
method. Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/general>`.

For example, to add a new authentication method of type `http`
called ``First tier partners``::

    [authentications/b904ed23-a234-4ccf-8abd-edcae4d3324f]
    name = First tier partners
    description = Authentication based on the DUSI web application.
    type = http


Activating an authentication method
-----------------------------------

Once defined, authentication methods require explicit activation by
defining the ordered list of active authentication methods for the
`server` authentication configuration option.

In this way, you can define multiple authentication methods and
set their priorities.
Once an account is successfully authenticated using a set method, the server
will not try the remaining methods.

The following example will define a configuration in which the
authentication with UUID ``b904ed23-a234-4ccf-8abd-edcae4d3324f`` is tried
first.
If the first method cannot authenticate the account, the server
will try to authenticate it using the method with UUID ``ed123e-4d4724f``::

    [server]
    name = VSP server
    description = Frontend for FG partners.

    authentications = b904ed23-a234-4ccf-8abd-edcae4d3324f, ed123e-4d4724f


Authentication method options
-----------------------------

Each authentication method configuration has the following options:


name
^^^^

:Default value: ''
:Optional: Yes
:From version: 2.10.0
:Values: * Any text.
:Description:
    Human-readable short text used to identify this method.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 2.10.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this authentication
    method.


type
^^^^

:Default value: ''
:Optional: No
:From version: 2.10.0
:Values: * `application` - Application accounts.
         * `os` - Accounts authenticated by the OS.
         * `http` - HTTP (unsecured).
         * `ip-time-ban` - Ban an IP address for a time interval.
         * `deny-username` - Deny authentication based on usernames.
         * `anonymous` - Anonymous account authentication.
         * `ldap` - Authenticate against an LDAP server.
         * `local-file` - Authenticate the accounts from a separate local file.
:Description:
    This option specifies the type of the method. Each type has a set
    of specific configuration options


Application-level Authentication Method
---------------------------------------

An `application` authentication method can be used to authenticate users
based on accounts defined in the configuration file of SFTPPlus.

It will authenticate accounts of type `application`.


allowed_groups
^^^^^^^^^^^^^^

:Default value: `empty`
:Optional: Yes
:Values: * `empty`
         * Group UUID
         * Comma-separated list of group UUIDs.
:From version: 4.0.0
:Description:
    Defines a group or a list of groups with users that
    are allowed by this authentication method.

    When this is empty, any account is accepted as long as it has valid
    credentials.

    ..  note::
        This option applies to group UUID values, not group names.
        This makes it possible to rename a group without having to update
        this configuration option.


OS-level Authentication Method
------------------------------

An `os` authentication method can be used to authenticate users
based on the authentication methods provided by the operating system.

It can also be used to authenticate administrators for the Local Manager
service.
For this, you will need to explicitly define a group or a set of groups
in the `manager_allowed_groups` configuration options.
By default, no administrators are allowed.

..  warning::
    On Unix-like systems, this authentication method can only be used
    when the SFTPPlus service is started as `root`.

You can overwrite some of the account's settings (e.g. home folder path), by
defining an account of type `os` inside the configuration file.

The `os` authentication method will authenticate the following account types:

* Windows Local Accounts on Windows systems.
* Windows Active Directory Accounts, when SFTPPlus runs on a Windows system
  which is part of a domain.
* Linux accounts with passwords defined in the ``/etc/passwd`` file or
  by the Name Service Switch library.
* Linux accounts with passwords defined in the ``/etc/shadow`` file.

On systems supporting PAM, PAM can also be used for authenticating users
with username and password credentials.

On many Unix-like systems, PAM is used for enabling various authentication
methods, such as LDAP, PKCS#11 smart cards, or fingerprint authentication.

When the PAM authentication request returns *PAM_SUCCESS*, the account is
authorized.
Any response other than *PAM_SUCCESS* will reject the account.

PAM only handles authentication.
The account configuration is retrieved using the same generic OS API.

..  note::
    The SFTPPlus' `pam` authentication method will only use PAM for the
    `authentication` operation.
    PAM is not used for managing accounts, sessions, or passwords.
    Please get in touch with us if you need to integrate PAM accounts and
    session management with SFTPPlus.


pam_usage
^^^^^^^^^

:Default value: `fallback`
:Optional: Yes
:Values: * `fallback`
         * `exclusive`
         * `disabled`
:From version: 3.3.0
:Description:
    Defines how to use PAM for for authenticating accounts using username and
    password credentials.

    The default mode is `fallback`.
    In this mode it will first try to authenticate accounts based on the
    ``/etc/passwd`` file.
    If the password is set in the operating system as one of the following
    `x`, `NP`, `*NP*` or `*`, it will continue to authenticate with PAM.

    In `exclusive` mode, it will exclusively use PAM for username and password
    authentications.

    Set it to `disabled` to completely disable PAM usage.

    ..  note::
        On Windows, this option is always `disabled`, as SFTPPlus has no support
        for PAM on this platform.


pam_service
^^^^^^^^^^^

:Default value: `login`
:Optional: Yes
:Values: * Name of a PAM service.
:From version: 3.3.0
:Description:
    Name of the PAM service used for account authentication requests.


allowed_groups
^^^^^^^^^^^^^^

:Default value: `empty`
:Optional: No
:Values: * `empty`
         * OS group name
         * `${ALL_OS_GROUPS}`
         * Comma-separated list of OS group names.
:From version: 3.35.0
:Description:
    Defines an operating system group or a list of OS groups with users that
    are allowed by this authentication method.

    When this is empty, no OS account is accepted.
    You need to define a list of group names for which to allow access.
    For example, if you need to allow all users from the local system, you can
    typically use the default `users` group available on both Windows and Linux.

    If you absolutely need to allow access to all OS users from all OS groups,
    set this to `${ALL_OS_GROUPS}`.
    This should be the only value, and you can't mix `${ALL_OS_GROUPS}` with
    other group names.

    ..  note::
        This configuration takes operating system group names and not
        SFTPPlus group names.


group_association
^^^^^^^^^^^^^^^^^

:Default value: `DEFAULT_GROUP`
:Optional: No
:Values: * GROUP-UUID
         * `group-name`
         * `group-name-with-default`
:From version: 4.11.0
:Description:
    Defines the SFTPPlus group that is associated with authenticated users.

    When set with the identifier (UUID) of a SFTPPlus group,
    it will associate any user with that SFTPPlus group.

    When set to `group-name`, it will associate the user with the
    SFTPPlus group having the same name as the operating system group of
    this user.
    If the user is a member of multiple groups,
    the first group defined in `allowed_groups` will be used.
    If no SFTPPlus group is found with the same name, the authentication fails.

    When set to `group-name-with-default`, it will try to associate the user
    with a SFTPPlus group having the same name as the OS group.
    It will use the default SFTPPlus group if no SFTPPlus group is found having
    the same name as the OS group.

    ..  note::
        When an OS account is explicitly defined inside SFTPPlus configuration
        the `group_association` is ignored and the account's groups
        configuration is used instead.


manager_allowed_groups
^^^^^^^^^^^^^^^^^^^^^^

:Default value: `empty`
:Optional: Yes
:Values: * `empty`
         * OS group name
         * Comma-separated list of OS group names.
:From version: 3.37.0
:Description:
    Defines an operating system group or a list of OS groups with users that
    are allowed by this method to be used for the Local Manager service.

    When this is empty, any administrators are denied.

    ..  note::
        This configuration takes operating system group names and not
        SFTPPlus group names.


Windows Domain Accounts
^^^^^^^^^^^^^^^^^^^^^^^

When SFTPPlus is installed on a machine belonging to a Domain
Controller, it can be configured to allow accounts from a Domain Controller to
access the files located on the server.
These accounts are authenticated using the `os` authentication method.

For Domain Controller accounts, there is the option for the username to be
provided in the user principal name (UPN) format::

    USERNAME@EXAMPLE.COM

To specify the domain, you should use UPN format, not the legacy NebBIOS names.

..  note::
    Active Directory accounts are only available when SFTPPlus is
    running on a Windows operating system.
    If you want to allow Active Directory accounts to access an SFTPPlus
    instance running on Unix-like systems, please contact our support team.


Local File Authentication Method
--------------------------------

A `local-file` authentication method allows defining accounts and groups in
a separate configuration file.

The file uses the same format and configuration options as the main
configuration file.
Only accounts and groups configurations are read from this file.
Any other configurations present in the file are ignored.

The accounts and groups defined for this authentication method are independent
to the main SFTPPlus application.
The accounts defined in the external file can only be configured with
groups defined in the same external file.
They can't be configured with groups from the main configuration file.

Only application accounts can be defined to be used by this authentication
method.

..  note::
    This authentication method can't be used with the Local Manager services.

The external file is automatically reloaded every 5 minutes.
This means that it can take up to 5 minutes for the changes to be visible.


path
^^^^

:Default value: ''
:Optional: No
:Values: * Path on the local filesystem
:From version: 3.33.0
:Description:
    Absolute path to a file, local to the server, in which the
    accounts and groups configurations are stored for this authentication
    method.


external_management
^^^^^^^^^^^^^^^^^^^

:Default value: 'yes'
:Optional: yes
:Values: * `yes`
         * `no`
:From version: 3.37.0
:Description:
    Set to `yes` when you want the file used to store the identities for this
    authentication to be managed by an external process.
    For example using a configuration management system.
    When set to `yes` it will automatically reload the changes every 5 minute.

    Set to `no` when you want to use the Local Manager to manage the identities
    for this authentication.
    When set to `no`, changes done to the file outside of the Local Manager
    are ignored.


LDAP Authentication Method
--------------------------

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


address
^^^^^^^

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
^^^^

:Default value: `389`
:Optional: Yes
:Values: * Port number.
:From version: 3.13.0
:Description:
    Port number used by the remote LDAP server to receive client connections.


secure_connection
^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^

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
^^^^^^^

:Default value: ''
:Optional: No
:Values: * Base distinguished name.
:From version: 3.13.0
:Description:
    Base DN used to generate the distinguished name associated with the
    account which needs to be authenticated.

    The exact way in which the `bind_dn` is constructed will depend on the
    `bind_dn_type` configuration.

    For more details, consult the documentation for `bind_dn_type`.

    When `bind_dn_type` is set to `direct-username`, this is used as the
    base DN of the Active Directory group to which access is permitted.

    This is ignored when `bind_dn_type` is set to `absolute`.


username_attribute
^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^

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


multi_factor_authentication_attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Attribute name.
         * `Empty`.
:From version: 4.12.0
:Description:
    Name of the LDAP attribute used to store the multi-factor
    authentication parameters for SFTPPlus users.
    For example, when the MFA parameter for an SFTPPlus user is stored in
    an LDAP attribute named ``totpSharedSecret``, the configuration shows::

        multi_factor_authentication_attribute = totpSharedSecret

    When `multi_factor_authentication_attribute` is defined, MFA
    authentication is enforced in SFTPPlus for all LDAP users.

    For now, only the TOTP MFA method is supported.
    Values stored in LDAP for this attribute should use the
    Google Authenticator Key URI format.
    For example, an LDIF value to be stored by the LDAP server::

        totpSharedSecret: otpauth://totp/FSrv:admin?secret=PRIVATE&issuer=FSrv

    ..  danger::
        This multi-factor authentication method should only be used when
        end users don't have direct access to their MFA parameter
        stored on the LDAP server.
        Otherwise, an SFTPPlus user can retrieve their MFA
        secret from LDAP, and bypass this security measure.


search_filter
^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Group UUID.
         * Comma separated LDAP attribute name, matching value, and group UUID.
         * Empty value.
:From version: 3.34.0
:Description:
    The LDAP group mapping configuration can be used to augment the LDAP data
    without updating the actual LDAP entries.

    Setting to a single group UUID will associate all the LDAP authenticated
    accounts to the SFTPPlus group associated with this UUID.
    For more details, see the
    :doc:`dedicated LDAP group mapping documentation</guides/ldap>`.

    You can create complex group mapping by specifying multiple groups which
    are selected based on targeted LDAP values.

    The matching for LDAP attribute names is case insensitive.

    Leave this configuration option empty to use the default
    SFTPPlus group configuration.

.. include:: /configuration/ssl.include.rst


RADIUS Authentication Method
----------------------------

The `radius` authentication method can be used to authenticate
`application` type accounts by delegating the authentication to a remote
RADIUS UDP server.

When an authentication request is made for a file transfer session,
SFTPPlus will use the provided credentials (username and password)
and forward them to the configured RADIUS server for validation.

All authentication request are made using `NAS-Port = 0`.
Contact our support team is you need to authenticat using a different NAS
port number.

For now, PAP, CHAP, MS-CHAP-V1 and MS-CHAP-V2 are supported.
Contact us if you need EAP-MD5 or other authentication protocols.

..  note::
    Only UDP transport protocol is supported.
    If you require TCP support, contact our support team.

Successfully authenticated accounts are associated to the default group,
or to a specific group based on the `group_mapping` configuration.

The implementation follows the
`RFC 2865 <https://tools.ietf.org/html/rfc2865>`_ standard.

It supports multiple Filter-ID attributes, but this usage is not encouraged
by `RFC 5080 <https://tools.ietf.org/html/rfc5080>`_.

..  warning::
    Only use RADIUS over internal networks.
    RADIUS relies on MD5 and is not FIPS compliant.


address
^^^^^^^

:Default value: ''
:Optional: No
:Values: * Host name.
         * Fully qualified domain name resolving an IPv4 or IPv6 address.
         * IPv4 address.
         * IPv6 address.
:From version: 4.10.0
:Description:
    Host name, domain name or IP address used to connect to the remote
    RADIUS server.


port
^^^^

:Default value: `1812`
:Optional: Yes
:Values: * Port number.
:From version: 4.10.0
:Description:
    Port number used by the remote RADIUS server.


shared_secret
^^^^^^^^^^^^^

:Default value: ''
:Optional: No
:Values: * Clear text secret.
:From version: 4.10.0
:Description:
    This is the shared secret defined between the RADIUS server and the
    SFPPlus application used to secure the communication.


authentication_type
^^^^^^^^^^^^^^^^^^^

:Default value: 'ms-chap-v2'
:Optional: Yes
:Values: * `pap`
         * `chap`
         * `ms-chap-v1`
         * `ms-chap-v2`
:From version: 4.13.0
:Description:
    The authentication type to use when sending the credentials to the
    RADIUS server.

    Use `pap` for Password Authentication Protocol as specified in the main
    RADIUS documentation. Uses MD5.

    Use `chap` for Challenge-Handshake Authentication Protocol as specified in
    the main RADIUS documentation. Uses MD5.

    Use `ms-chap` for the Microsoft version of the
    Challenge-Handshake Authentication Protocol as specified in
    `RFC 2548 <https://datatracker.ietf.org/doc/html/rfc2548>`_.

    Use `ms-chap-v2` for the Microsoft
    Challenge-Handshake Authentication Protocol Version 2 as specified in
    `RFC 2759 <https://datatracker.ietf.org/doc/html/rfc2759>`_.

    ..  warning::
        The current security standards no longer consider MS-CHAP-v2 as a
        secure authentication method.
        MS-CHAP-v2 is still in used as there are many legacy products using
        it.

        With any authentication method, only use RADIUS over secure networks.


continue_authentication
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `No`
:Optional: Yes
:Values: * Yes
         * No
:From version: 4.10.0
:Description:
    Whether to continue and try other authentication methods when RADIUS
    server has rejected the authentication request for the current user.

    If the connection to the RADIUS server fails without receiving any
    response from the server,
    the authentication fails right away.

    ..  note::
        This configuration is for continuing the authentication chain when
        the RADIUS server has rejected the access request.

        See `group_mapping = ${CONTINUE}` for continuing the authentication
        chain on success.


timeout
^^^^^^^

:Default value: `60`
:Optional: Yes
:Values: * Number of seconds.
:From version: 4.13.0
:Description:
    Duration, in seconds, to wait for a response from the RADIUS server.

    If a response is not received during this period, the authentication fails.

    ..  note::
        If the `idle_connection_timeout` value of a service is lower
        than the RADIUS `timeout`,
        then the login attempt may fail before the RADIUS server responds.


nas_port
^^^^^^^^

:Default value: '0'
:Optional: Yes
:Values: * Integer number
:From version: 4.13.0
:Description:
    Value of the RADIUS `NAS-Port` used for the access request.

    For most configurations, this can be set to 0 (zero).


debug
^^^^^

:Default value: 'no'
:Optional: Yes
:Values: * `yes`
         * `no`
:From version: 4.13.0
:Description:
    When enabled, emit low-level protocol debug messages.


.. _conf-radius_group_mapping:

group_mapping
^^^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Group UUID.
         * Comma separated RADIUS attribute name, matching value,
           and group UUID.
         * Empty value.
:From version: 4.10.0
:Description:
    The group mapping configuration can be used to associate a successfully
    authenticated user with an SFTPPlus group, based on the RADIUS attributes
    found in the `Access-Accept` message.

    Setting to a single group UUID will associate all the RADIUS authenticated
    accounts to the same SFTPPlus group.

    You can create complex group mapping by specifying multiple groups which
    are selected based on RADIUS attribute names and values.
    Define group mappings, one rule per line.

    The first line should always contain a single value which is the default
    group used in the case in which no RADIUS attribute is matched.

    Subsequent lines will contain 3 comma separated values.
    The first value is the name of the RADIUS attribute, which is a case
    insensitive value.
    The second value is a matching expression used to match the value of the
    RADIUS attribute.
    The third value is the SFTPPlus group UUID used to associate the
    authenticated user to.

    You can use the `${CONTINUE}` value instead of the group UUID to instruct
    SFTPPlus to continue authenticating using the next methods from the
    authentication chain.

    Leave this configuration option empty to use the default
    SFTPPlus group configuration.


HTTP Authentication Method
--------------------------

An `http` authentication method asks a remote HTTP resource to authenticate
an account and provide the account's configuration.

..  note::
    This authentication method can't be used with the Local Manager services.

To get more details about the request format and the expected result,
see the dedicated
:doc:`HTTP authentication protocol documentation
</developer/http-api-authentication>`.


url
^^^

:Default value: ''
:Optional: No
:Values: * URL
         * Comma separated list of URLs (Since 3.51.0)
:From version: 2.10.0
:Description:
    Full URL of a resource used to authenticate an account.

    You can define a fall-back/redundant URL using a comma separates list of
    URLs.
    The first URL from the list will be used. When failing to get a response
    for the first URL, the remaining URLs are tried.
    Since 3.51.0.


timeout
^^^^^^^

:Default value: `120`
:Optional: Yes
:Values: * Number of seconds.
:From version: 4.13.0
:Description:
    Duration, in seconds, to wait for a response from the HTTP server.

    If a response is not received during this period, the authentication fails.


username
^^^^^^^^

:Default value: ''
:Optional: yes
:From version: 3.30.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote HTTP server.

    Leave this value empty in order to leave out HTTP Basic authentication.

    This will overwrite any custom `Authorization` header set via the
    `headers` configuration option.

    ..  warning::
        For now, only HTTP Basic authentication is supported.
        This will send the username and password in clear text
        (BASE64 encoded).


password
^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.30.0
:Values: * Plain text password.
         * Empty.
:Description:
    Password associated with the configured `username`.


headers
^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 4.4.0
:Values: * Header-Name: Header-Value
         * Multiple headers on separate lines
:Description:
    This defines a set of extra headers which are sent with each HTTP request.


test_at_start
^^^^^^^^^^^^^

:Default value: 'Yes'
:Optional: Yes
:From version: 4.5.0
:Values: * Yes
         * No
:Description:
    When set to `Yes` it will check at startup that the configured URL
    can be reached and fail to start if the URL is not available to respond
    to authentication requests.


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

.. include:: /configuration/ssl.include.rst


Deny Authentication Method
--------------------------

A `deny-username` authentication method can be used to block/deny
authentication for a configured list of denied users.

You can use it for file transfer services, as well as for the Local Manager
service.

..  note::
    Add this authentication method as the first one in the list of
    active authentication methods to make sure the users are not
    authenticated earlier by other authentication methods.


usernames
^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Comma-separated list of usernames.
:From version: 3.0.0
:Description:
    Comma-separated list of usernames denied by this
    authentication method.

    The check is done in case-insensitive mode, by comparing against the
    lower-case name.

    Usernames should be defined in lower-case.


Ban IP for a time interval
--------------------------

An `ip-time-ban` authentication method can be used to block/deny
authentication requests coming from a specific IP address if they generate
a number of consecutive authentication failures.
This option can be used to help mitigate DDOS attempts to SFTPPlus services.

The ban is active for a time interval, after which authentication requests
made from the IP address are accepted again.

When the authentication method is restarted it will reset its internal
record of source IP addressed which have previously generated failed
authentication requests.

When the same authentication method is used for multiple file transfer services
and the Local Manager services, it will use a single internal state for
each username.
Multiple consecutive authentication failures for different services have the
same effect as multiple consecutive authentication failures for the same
service.

..  note::
    Add this authentication method as the first one in the list of
    active authentication methods to make sure the users are not
    accepted earlier by other authentication methods.

..  warning::
    SFTPPlus is behind a load balancer, make sure that Proxy Protocol version 2
    is enabled on both the load balancer and SFTPPlus file transfer services.
    Otherwise all the authentication requests will be made using the
    load balancer own IP address and not the client IP address.

..  warning::
    Do not use this method if SFTPPlus is behind a Proxy/Gateway or any other
    network device which does not preserve the source IP address of the
    initial authentication request or does not support Proxy Protocol v2

    The ban applies to the source IP address used to initiate the
    authentication requests.

    If SFTPPlus server is behind a Proxy/Gateway, all requests will come from
    the gateway's own IP address.

    Check that your network is not vulnerable to
    `IP address spoofing <https://en.wikipedia.org/wiki/IP_address_spoofing>`_
    .


ban_interval
^^^^^^^^^^^^

:Default value: `3600`
:Optional: Yes
:Values: * Number of seconds.
:From version: 3.2.0
:Description:
    Number of seconds for which authentication requests from the source IP
    are denied.

    Default interval is 1 hour.


ban_after_count
^^^^^^^^^^^^^^^

:Default value: `5`
:Optional: Yes
:Values: * Number of failed attempts.
:From version: 3.2.0
:Description:
    Number of consecutive failed authentications which will result in blocking
    the source IP.


Anonymous Authentication Method
-------------------------------

An `anonymous` authentication method can be used to authenticate a specific
`application type` account by ignoring the provided password or any other
credential.

This authentication is implemented based on the
`RFC 1635 <https://tools.ietf.org/html/rfc1635>`_ but it can also be used
for SFTP/SCP or HTTP/HTTPS services.

Once authenticated, the `anonymous` account will have the same permissions
as the account with which it's associated.
The audit events are recorded under the associated account name and not the
`anonymous` account.

..  note::
    This authentication method can't be used with the Local Manager service.

The `anonymous` account is locked inside the home folder and will have
full access to all files and directories located in the home folder, just like
a normal application account.

..  image:: /_static/gallery/gallery-add-anon-auth.png


anonymous_account_uuid
^^^^^^^^^^^^^^^^^^^^^^

:Default value: ''
:Optional: No
:Values:
    * UUID of the application account with which this account is
      associated.
:From version: 3.2.0
:To version: None
:Description:
    This is the UUID of the application account associated with the
    `anonymous` account.
