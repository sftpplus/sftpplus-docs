External local file
===================

A `local-file` authentication method allows defining accounts and groups in
a separate configuration file.

..  contents:: :local:


Introduction
------------

The file uses the same format and configuration options as the main
configuration file.
Only accounts and groups configurations are read from this file.
Any other configurations present in the file are ignored.

The accounts and groups defined for this authentication method are independent
to the main SFTPPlus application.
The accounts defined in the external file can only be configured with
groups defined in the same external file.
They can't be configured with groups from the main configuration file.

There is a list of limitations when defining accounts in an external file:

* Only application accounts can be defined. OS accounts are not supported.
* The accounts can't be used as the public account for an HTTP service.
* The accounts can't be auto-disabled on inactivity.
* Administrators or roles can't be defined.

The external file is automatically reloaded every 5 minutes.
This means that it can take up to 5 minutes for the changes to be visible.

.. include:: /configuration-auth/authentication-commons.include.rst


path
----

:Default value: ''
:Optional: No
:Values: * Path on the local filesystem
:From version: 3.33.0
:Description:
    Absolute path to a file, local to the server, in which the
    accounts and groups configurations are stored for this authentication
    method.


external_management
-------------------

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

    Set to `no` when you want to use the Web Manager to manage the identities
    for this authentication.
    When set to `no`, changes done to the file outside of the Web Manager
    are ignored.
