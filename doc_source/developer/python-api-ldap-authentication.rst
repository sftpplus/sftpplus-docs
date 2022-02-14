Python API LDAP Authentication
==============================

..  contents:: :local:


Introduction
------------

SFTPPlus allows developers to write custom authentication handling code to
augment the standard LDAP authentication functionality.

The extension code is executed in the main application thread.
It should not block the thread.


API interface
-------------

The code for the extension needs to be placed in a Python file (module)
inside the `extension/` folder from the SFTPPlus installation folder.
The Python file should contain a class that implements a set of methods
that are the interface of the LDAP authentication extension.

The class can have any name, but it should implement using the same method
name and all the arguments with the exact argument names.

.. autoclass:: chevah.server.extension.auth_ldap_noop::AuthLDAPNoop
    :special-members: __init__

For more details about the usage of this API get in touch with our support
team.


Usage
-----

You can find a skeleton example inside the `extension/auth_ldap_noop.py`
file of the default SFTPPlus installation.
It can be used as the base for implementing custom functionality.

This extension handler can be configured as::

    [authentications/d87d-4a3c-d732]
    type = ldap
    name = Authenticate from LDAP with Python API extension

    extension_entry_point = python:auth_ldap_noop.AuthLDAPNoop
    extension_configuration = {
        "key": "value"
        }
