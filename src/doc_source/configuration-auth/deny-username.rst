Banning users
=============

..  contents:: :local:


Introduction
------------

A `deny-username` authentication method can be used to block/deny
authentication for a configured list of denied users.

You can use it for any file transfer service.

..  note::
    Add this authentication method as the first one in the list of
    active authentication methods to make sure the users are not
    authenticated earlier by other authentication methods.


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

    The check is case-insensitive.

    Usernames should be defined in lower-case.

    This list is not used to deny access to the Web Manager console.


administrators
--------------

:Default value: ''
:Optional: Yes
:Values: * Comma-separated list of names.
:From version: 5.12.0
:Description:
    Comma-separated list of administrator names denied by this authentication method.

    The check is case-insensitive.

    Usernames should be defined in lower-case.

    This list is not used to deny access to the file transfer services.

    Leave it empty to allow any username to authenticate as administrators.
    The value of `administrators =`` in the INI file means that administrators are explicitly defined and that you don't want to block any admin.

    ..  note::
        When the `administrators` configuration option is not defined at all inside the .INI configuration file,
        not even as an empty value,
        the value from the `usernames` configuration option is used instead.
        When you don't have `administrators =` in the INI file,
        it means that this is a pre 5.12 configuration file and it is automatically migrated so that the behaviour for 5.12 is similar to that of the older versions.
