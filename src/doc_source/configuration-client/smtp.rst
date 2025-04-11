Send files as email attachments
===============================

..  contents:: :local:


Introduction
------------

An `smtp` location allows sending files as email attachments.
It uses the Simple Mail Transfer Protocol (SMTP) to connect to an SMTP server and asks the server to deliver the email.

SFTPPlus acts as message transfer agent (MTA) to connect to an SMTP mail server and asks the server to deliver the email.

The location can only be used as the destination for a transfer.

All files are sent to the same set of email recipients, CCs or BCCs.
If you need to send files to a different set of email recipients you can define multiple `stmp` locations.

The SMTP mail server is configured via the :doc:`email-client resource </configuration/email-client>`

The `smtp` location configuration is used to define the recipient and the content of the email subject and body.

The email subject and body can be configured using a template.
The following variables are available:

* `{server.name}` The name of the SFTPPlus server
* `{server.uuid}` The unique ID of the SFTPPlus server
* `{location.name}` The name of the location that triggered the transfer.
* `{location.uuid}` The unique ID of the location.
* `{attachment.file_name}` The name of the file.
* `{attachment.size}` The size in bytes of the file.

Using these variables in the `email_subject` and `email_body` options you can created customized messages.
For example, for the configuration below::

    [server]
    name = AS-QA1

    [location/b9787c72-2c8b-4725-a049-ee628aa0abc1]
    type = stmp
    name = Send file to data team
    email_subject = New file from {server.name}
    email_body = A new file was received.
        The file {attachment.file_name} is attached.

        --
        This is an automated message from "{location.name}""
        Contact sysadmin@example.com

When a file with name `reports-January-2025.csv` is transferred, the email will have the subject `New file from {AS-QA1}` and the content::

        A new file was received.
        The file reports-January-2025.csv is attached.

        --
        This is an automated message from "Send file to data team"
        Contact sysadmin@example.com


SMTP mail server limitations
----------------------------

Only use this location to transfer files smaller than 10 MB.
Many mail servers will reject files with large attachments.

If you need to transfer large files,
get in touch with our support team to discuss the available options.
SFTPPlus can allow large file transfers over HTTPS or SFTP,
while still receiving email notifications.

------

Many mail servers will receive the request to send the email and the attachment,
but the actual delivery might be delayed or even rejected.

A successful transfer with SFTPPlus indicates that the file has been accepted by the SMTP server.
However, it does not indicate that the request processing has completed.
Delivery of the file is subject to the limitations, security policy and throttling of the remote SMTP server.

The SMTP mail server will confirm to SFTPPlus that the message was successfully received for processing,
but will not send the final delivery report.

This is a limitation of the SMTP protocol, introduced in 1981 for for which `S` stands for `simple`.
Get in touch with our support team to review any alternative delivery options, like AS2 or SFTP.


name
----

:Default value: Empty
:Optional: No
:From version: 5.12.0
:Values: * Any text.
:Description:
    Human-readable short text used to identify this location.


description
-----------

:Default value: Empty
:Optional: Yes
:From version: 5.12.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this location.


email_to_recipients
-------------------

:Default value: `empty`
:Optional: No
:Values: * Email address
         * Comma-separated list of emails
:From version: 5.12.0
:Description:
    Comma-separated list of addresses where to send emails.


email_cc
--------

:Default value: `empty`
:Optional: Yes
:Values: * Email address
         * Comma-separated list of emails
:From version: 5.12.0
:Description:
    Comma-separated list of secondary recipients whose names are visible
    to one another and to the primary recipients.

    Leave it empty to not use CC.


email_bcc
---------

:Default value: `empty`
:Optional: Yes
:Values: * Email address
         * Comma-separated list of emails
:From version: 5.12.0
:Description:
    Comma-separated list of tertiary recipients whose names are invisible
    to each other and to the primary and secondary recipients.

    Leave it empty to not use BCC.


email_subject
-------------

:Default value: `File received from {server.name} {location.name}`
:Optional: Yes
:Values: * Text template
:From version: 5.12.0
:Description:
    Template used for the subject field of the sent email.


email_body
----------

:Default value: `See the received file {attachment.file_name} in the attachment.`
:Optional: Yes
:Values: * Text template
:From version: 3.18.0
:Description:
    Template used for the body of the sent email.
