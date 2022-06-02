.. _conf-resource-email-client:

Email client
============

..  contents:: :local:


Introduction
------------

An `email-client` is configured to allow SFTPPlus to send emails as an
SMTP client via a remote SMTP server.

You will need to specify the address or the fully qualified domain name of the
SMTP server to use and the value to be used by this client for the `From`
field.


address
-------

:Default value: ``127.0.0.1``
:Optional: No
:From version: 3.4.0
:Values: * An IP address or a host name.
:Description:
    This option specifies the IP address or the host name of the
    remote server.


port
----

:Default value: ``25``
:Optional: No
:From version: 3.4.0
:Values: * A port number for the server.
:Description:
    This option specifies the IP port of the remote server.


username
--------

:Optional: Yes
:Default value: ''
:Values: * text
         * empty
:From version: 3.4.0
:Description:
    Username used to connect to the server.

    Leave it empty to disable SMTP authentication.


password
--------

:Optional: Yes
:Default value: ''
:Values: * Plain text password.
:From version: 3.4.0
:Description:
    Password used to connect to the server.

    Ignored when no username is defined.


email_from_address
------------------

:Default value: ``no-reply@sftpplus.example.com``
:Optional: No
:Values: * email.address@example.com
         * Some Name <email.address@example.com>
         * "Name, Some" <email.address@example.com>
:From version: 3.4.0
:Description:
    Email address used in the `From` field of messages sent from this server.

    You can specify just an email address or a name and email address.

    ..  note::
        While you can configure any email address, including one which doesn't
        exist, it is recommended to set up a real email address.

        In this way, you will receive email delivery errors.


email_to_recipients
-------------------

:Default value: Empty
:Optional: Yes
:Values: * email.address@example.com
         * email.address@example.com, other.team@example.com
:From version: 4.1.0
:Description:
    Email address or addresses used as the default recipients for email
    sent by SFTPPlus.

    This value is used when no explicit recipient is defined for an
    event handler or other email sender component.
