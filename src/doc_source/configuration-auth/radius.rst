RADIUS
======

The `radius` authentication method can be used to authenticate
`application` type accounts by delegating the authentication to a remote RADIUS UDP server.

..  contents:: :local:


Introduction
------------

When an authentication request is made for a file transfer session,
SFTPPlus will use the provided credentials (username and password)
and forward them to the configured RADIUS server for validation.

All authentication request are made using `NAS-Port = 0`.
Contact our support team if you need to authenticate using a different NAS
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

.. include:: /configuration-auth/authentication-commons.include.rst


address
-------

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
----

:Default value: `1812`
:Optional: Yes
:Values: * Port number.
:From version: 4.10.0
:Description:
    Port number used by the remote RADIUS server.


password
--------

:Default value: ''
:Optional: No
:Values: * Clear text
:From version: 4.10.0
:Description:
    This is the shared secret defined between the RADIUS server and the SFPPlus application used to secure the communication.

    Before version 4.24.0 this configuration was named `shared_secret`.
    It was renamed to `password`` to help make it easier to audit sensitive
    information.


authentication_type
-------------------

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
-----------------------

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
-------

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
--------

:Default value: '0'
:Optional: Yes
:Values: * Integer number
:From version: 4.13.0
:Description:
    Value of the RADIUS `NAS-Port` used for the access request.

    For most configurations, this can be set to 0 (zero).


debug
-----

:Default value: 'no'
:Optional: Yes
:Values: * `yes`
         * `no`
:From version: 4.13.0
:Description:
    When enabled, emit low-level protocol debug messages.


.. _conf-radius_group_mapping:

group_mapping
-------------

:Default value: ''
:Optional: Yes
:Values: * Group UUID.
         * Comma separated RADIUS attribute name, matching value,
           and single group UUID.
         * Comma separated RADIUS attribute name, matching value,
           and multiple groups UUID (Since 4.20.0).
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

    Subsequent lines will contain at least 3 comma separated values.
    The first value is the name of the RADIUS attribute, which is a case
    insensitive value.
    The second value is a matching expression used to match the value of the
    RADIUS attribute.
    The remaining values are the SFTPPlus groups UUID associate to the user.
    The first group in this list is the primary group.

    You can use the `${CONTINUE}` value instead of the group UUID to instruct
    SFTPPlus to continue authenticating using the next methods from the
    authentication chain.

    Leave this configuration option empty to use the default
    SFTPPlus group configuration.
