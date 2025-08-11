Anonymous users
===============

An `anonymous` authentication method can be used to authenticate a specific
`application type` account by ignoring the provided password or any other
credential.

..  contents:: :local:


Introduction
------------

This authentication is implemented based on the
`RFC 1635 <https://tools.ietf.org/html/rfc1635>`_ but it can also be used
for SFTP/SCP or HTTP/HTTPS services.

Once authenticated, the `anonymous` account will have the same permissions
as the account with which it's associated.
The audit events are recorded under the associated account name and not the
`anonymous` account.

..  note::
    This authentication method can't be used with the Web Manager service.

The `anonymous` account is locked inside the home folder and will have
full access to all files and directories located in the home folder, just like
a normal application account.

..  image:: /static/gallery/gallery-add-anon-auth.png

.. include:: /configuration-auth/authentication-commons.include.rst


anonymous_account_uuid
----------------------

:Default value: ''
:Optional: No
:Values:
    * UUID of the application account with which this account is
      associated.
:From version: 3.2.0
:Description:
    This is the UUID of the application account associated with the
    `anonymous` account.
