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
