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
It formulates outgoing emails as though they were coming from an email client.
Access to an SMTP server is necessary.

When setting up email notifications, the first step is to create an
:ref:`Email Client resource <conf-resource-email-client>`.

Inside the resource configuration,
you will define the server address and port,
as well as authentication credentials.

Any errors related to email delivery are sent by the remote SMTP server to
the configured `email_from_address`.
Make sure you have defined a valid email, in order to receive delivery
related errors.

A single email client resource can be used by multiple email notifications.


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
