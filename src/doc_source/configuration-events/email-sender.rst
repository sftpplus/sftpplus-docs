.. _conf-handler-email-sender:

Email sender
============

To configure an event handler which sends emails to an SMTP server, use the
type `email-sender`.

The emails will be sent over SMTP or ESMTP and SFTPPlus will act as an
SMTP client.

The emails will be sent using a resource of type
:ref:`Email Client<conf-resource-email-client>`.

..  contents:: :local:

.. include:: /configuration-events/events-commons.include.rst


email_to_recipients
-------------------

:Default value: ''
:Optional: Yes
:Values: * Email address
         * UUID of a group (Since 4.25.0)
         * UUID of an account (Since 4.25.0)
         * Event-based template (Since 4.25.0)
         * Comma-separated list of emails
         * Comma-separated list of emails, group UUIDs, account UUIDs or templates. (Since 4.25.0)
:From version: 3.4.0
:Description:
    Comma-separated list of addresses where to send emails.

    If this list is not defined, emails will be sent using the general
    email resource recipients configuration.

    The list can also be configured using UUIDs of accounts and groups.
    For an account uuid, the email is sent to the address configured for that account.
    For a group uuid, the email is sent to all the users from the group that have an email address configured.
    If the account has no email address configured, the email message is skipped.
    (Since 4.25.0)

    A template can be used to generate the email address, based on the values found in the event.
    For example, `{account.email}` is replaced with the primary email address configured for an account.


email_cc
--------

:Default value: ''
:Optional: Yes
:Values: * Email address
         * UUID of a group (Since 4.25.0)
         * UUID of an account (Since 4.25.0)
         * Event-based template (Since 4.25.0)
         * Comma-separated list of emails
         * Comma-separated list of emails, group UUIDs, account UUIDs or templates. (Since 4.25.0)
:From version: 3.44.0
:Description:
    Comma-separated list of secondary recipients whose names are visible
    to one another and to the primary recipients.

    Leave it empty to not use CC.


email_bcc
---------

:Default value: ''
:Optional: Yes
:Values: * Email address
         * UUID of a group (Since 4.25.0)
         * UUID of an account (Since 4.25.0)
         * Event-based template (Since 4.25.0)
         * Comma-separated list of emails
         * Comma-separated list of emails, group UUIDs, account UUIDs or templates. (Since 4.25.0)
:From version: 3.44.0
:Description:
    Comma-separated list of tertiary recipients whose names are invisible
    to each other and to the primary and secondary recipients.

    Leave it empty to not use BCC.


email_associated_files
----------------------

:Default value: Empty
:Optional: Yes
:Values: * Empty
         * `attachment`.
:From version: 3.18.0
:Description:
    When set to `attachment`, an email (as multi-part MIME) is sent
    with the associated file as an attachment.
    The file path is taken from the `real_path` property of an event data.

    The maximum allowed file size equals to 5MB.
    If the file can't be attached or is larger than 5MB, then the email is
    not sent and an audit event is created for this failure.

    When set to the empty value, an email is sent without an attachment.


email_subject
-------------

:Default value: ``[{id}] [{component.name}] New event from SFTPPlus``
:Optional: No
:Values: * Plain text template
:From version: 3.4.0
:Description:
    Template used for the subject field of the sent email.

    The `email_subject` can be configured using a format string like
    ``New Event {id} from {account.name}``.

    .. include:: /configuration/event-context-variables.rst.include


email_body
----------

:Default value: ``[{timestamp.cwa_14051}] {message}{LF}{LF}{data_json}``
:Optional: Yes
:Values: * Plain text with newline as the only non-printable characters.
:From version: 3.18.0
:Description:
    Template used for the body of the sent email.

    .. include:: /configuration/event-context-variables.rst.include

    Using these variables the `email_body` can be configured, for
    example, like the following::

        [event-handlers/b9787c72-2c8b-4725-a049-ee628aa0abc1]
        email_body = {id} {message}
          Content over multiple lines

          Event attached data:
          {data_json}
