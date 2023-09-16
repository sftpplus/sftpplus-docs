Banning users
=============

A `deny-username` authentication method can be used to block/deny
authentication for a configured list of denied users.

You can use it for file transfer services, as well as for the Local Manager
service.

..  note::
    Add this authentication method as the first one in the list of
    active authentication methods to make sure the users are not
    authenticated earlier by other authentication methods.

..  contents:: :local:

..  include:: /configuration-auth/authentication-commons.include.rst


usernames
---------

:Default value: ''
:Optional: Yes
:Values: * Comma-separated list of usernames.
:From version: 3.0.0
:Description:
    Comma-separated list of usernames denied by this
    authentication method.

    The check is done in a case-insensitive way.

    Usernames should be defined in lower-case.
