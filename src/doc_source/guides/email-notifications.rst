.. container:: tags pull-left

    `server-side`
    `client-side`


Sending notification/alerts over emails
#######################################


Introduction
------------

SFTPPlus can be configured to send emails based on the events
generated during file transfer operations.

These emails can serve as notifications or alerts.


Add the SMTP server configuration
---------------------------------

SFTPPlus does not act as an SMTP server.
In order to send an email, SFTPPlus acts as an email client.
It will connect to an SMTP server and make a request for an email delivery.
Access to an SMTP server is necessary.

When setting up email notifications, the first step is to configure the
:ref:`Email Client resource <conf-resource-email-client>`.

Inside the resource configuration,
you will define the server address and port,
as well as authentication credentials.

Any errors related to email delivery are sent by the remote SMTP server to
the configured `email_from_address`.
Make sure you have defined a valid email, in order to receive delivery
related errors.


Set up the notification rules
-----------------------------

An event handler of type
:ref:`Send as email <conf-handler-email-sender>`
is used to define the conditions under which the email notification is sent.

While SFTPPlus performs various operations it will generate a set of events.
Each event has an ID and a set of associated attributes, like user name,
remote IP address or a file path.

We have created a dedicated article which discusses
:doc:`the details of filtering the event</guides/event-handlers>`.
Consult that page to find out more about the available filtering rules.

Once the conditions upon which the emails notification should be sent are set
(inside the event handler's configuration page),
you have the option to define the
recipients for each notification, email subject and body.

Below is a screenshot demonstrating some of the configuration options.

..  image:: /_static/guides/send-as-email-options.png
    :alt: Send as email configuration options


Email subject, recipients, or body template
-------------------------------------------

When configuring the `email_to_recipients`, `email_cc`, `email_bcc`, `email_subject`, or `email_body` options, you can defined them as a fixed value or as a template.

The template value is resolved based on the content of the emitted event.

The templates can be defined using the following structure.

.. include:: /developer/event-object.include.rst


Send emails to accounts using the configured emails
---------------------------------------------------

When configuring an user account in SFTPPlus,
you can define one or more email addresses associated to this account.

When configuring an email handler for an action triggered by an user account,
you can configure that event handler to use the email address associated to the user.

A template can be used to generate the email address
based on the values found in the event.
For example, `{account.email}` is replaced with the primary email address configured for an account.

The template can combine variable values with fixed values.
For example, `{account.name}@example.com` for an event triggered by user `john-d` will generate the email address `john-d@example.com`.
If the event data is an UUID, it is resolved to an account email or all the emails from the group.
If the resulting value is empty, the email message is skipped.

The following configuration options have support for expanding the email address
based on the account configuration:

* `email_to_recipients`
* `email_cc`
* `email_bcc`

Below, you can find a few configuration examples.
These example are based on the following group and accounts configuration::

    [groups/215cbf00-b12e-4708-8669-b8089c5009b9]
    name = Sales team

    [accounts/9cf8e8f1-1cd0-42e1-8135-858c35d52a8f]
    name = John D
    email = john.d@email.com
    group = 215cbf00-b12e-4708-8669-b8089c5009b9

    [accounts/9215cbf00-b12e-4708-8669-b8089c5009b9]
    name = Jane R
    email = jane.r@email.com, admins@example.net
    group = 215cbf00-b12e-4708-8669-b8089c5009b9

You can configure an event handle to send an email to any member of a group.
This is done using a configuration similar to the one below,
where `215cbf00-b12e-4708-8669-b8089c5009b9` is the unique ID of the group.
This sends emails to `john.d@email.com, jane.r@email.com, admins@example.net`::

    [event-handlers/6d51ed1e-35ec-41d7-8b51-53e56c716212]
    enabled = True
    type = email-sender
    name = Send to all emails of all users from the group, for any file upload.
    target = 40007
    email_to_recipients = 215cbf00-b12e-4708-8669-b8089c5009b9

You can configure an email notification to send emails to the primary email of each user.
The configuration below exemplifies this.
A file uploaded by user `John D` sends a notification to `john.d@email.com`.
A file uploaded by user `Jane R` sends a notification to `jane.r@email.com`.
Below is the example for the event handler configuration::

    [event-handlers/6d51ed1e-35ec-41d7-8b51-53e56c716212]
    enabled = True
    type = email-sender
    name = Send to primary email of the user that has uploaded the file.
    target = 40007
    email_to_recipients = {account.email}

You can also configure the email notification to send emails to all emails associated to an account, not only the primary email.
The configuration below exemplifies this.
A file uploaded by user `John D` sends a notification to `john.d@email.com`.
A file uploaded by user `Jane R` sends a notification to `jane.r@email.com` and `admins@example.net`.
Below is the example for the event handler configuration::

    [event-handlers/6d51ed1e-35ec-41d7-8b51-53e56c716212]
    enabled = True
    type = email-sender
    name = Send to any email of the user that has uploaded the file.
    target = 40007
    email_to_recipients = {account.uuid}


Reports over email
------------------

Emails sent by SFTPPlus can have an attached file.
The attached file is the same as the file associated with the event which has
triggered the email.

Combined with the 'Store in local file' event handler you can set up a system
in which certain events are stored in a separate local file.
The separate local file can be rotated daily and an 'Send as email' event
handler associated with the event generated during the file rotation and have
the rotated file attached to the email.

In this way, you can receive daily reports over email containing only the
selected events.


Amazon SES Simple Mail Transfer Protocol (SMTP) interface
---------------------------------------------------------

SFTPPlus can use Amazon SES to send emails.

The `Connecting to the Amazon SES SMTP Endpoint
<https://docs.aws.amazon.com/ses/latest/DeveloperGuide/smtp-connect.html>`_
guide from Amazon provides the DNS names for the SMTP server which can be
configures inside the SFTPPlus 'Email client' resource.

As noted in the Amazon guide, Amazon Elastic Compute Cloud (Amazon EC2)
throttles email traffic over port 25 by default.
To avoid timeouts when sending email through the SMTP endpoint from EC2,
use port `587`.

If you want to use port 25, you need to fill out a
`Request to Remove Email Sending Limitations
<https://aws.amazon.com/forms/ec2-email-limit-rdns-request>`_
to remove the throttle.
