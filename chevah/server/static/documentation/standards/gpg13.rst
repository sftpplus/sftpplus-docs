.. container:: tags pull-left

    `client-side`
    `server-side`
    `security`


Protective Monitoring Obligations
#################################

Her Majesty's Government (HMG) Information Assurance (IA) practitioners will
have Protective Monitoring obligations, already laid down in national IA policy
and HMG IA Standard No. 1 & 2 supplement.

The `Good Practice Guide <https://www.ncsc.gov.uk/guidance/protective-monitoring-hmg-ict-systems-gpg-13>`_
was developed to provide guidance on meeting these obligations.
Further details are supplied by the NCSC.

To help assist those with Protective Monitoring obligations, we have created
this page to outline which portion of SFTPPlus functionality applies to a
Protective Monitoring Control.

As mentioned in the Guide, organisations are reminded that any particular
Protective Monitoring product or service is subject to some form of *independent
assurance* plus extensive acceptance testing by the business.

..  contents:: :local:


PMC1 Accurate Time in Logs
==========================

* SFTPPlus logs contain accurate time stamps for the events recorded.

Example log of a file being processed details the timestamp of these
actions:

    | 40021 2017-01-30 11:56:41 Process user 127.0.0.1:50568 File opened for
      upload at "/Reports/February-2017-Report.PDF".
    | 40017 2017-01-30 11:56:41 Process user 127.0.0.1:50568 Successfully
      uploaded file at "/Reports/February-2017-Report.PDF".


PMC-2 Recording Related to Business Traffic Crossing a Boundary
===============================================================

* SFTPPlus will keep a detailed log of any file which is transferred (push /
  pulled).
  This can include details about the initial transfer request and
  the status of the request finalization (success / failure).

* For activities like AV detection, the software can function suitably when AV
  applications are installed.
  See the :doc:`page on interoperability with antiviruses</guides/antivirus>`
  for more details.


PMC-3 Recording relating to suspicious behaviour at a boundary
==============================================================

As this PMC relates to network activity at the boundary with a view to
detecting suspect activity, this is more related to activities outside the
scope of the software such as boundary firewalls.


PMC-4 Recording on Internal Workstation, Server or Device Status
================================================================

* SFTPPlus status changes are recorded in the log and meets the objective of
  this PMC which is to detect changes to device status and configuration.

Examples of such changes include:

1. Changes to file transfer services such as enabling a service or changing the
   listening port.
2. Changes to different identity and authentication providers of an account.
3. Changes to components that implement custom business logic for file transfer
   workflows.
4. Changes to the component state are tracked such as the start / stop / failure
   states.
5. And more as a multitude of components make up the file transfer process.


PMC-5 Recording Relating to Suspicious Internal Network Activity
================================================================

* Unsuccessful attempts are logged and the administrator will be able to review
  these.

An example of an unsuccessful OS authentication attempt is below:

    | 20136 2016-11-17 09:31:55 Process Unknown 127.0.0.1:49569 Account "alice"
      forbidden by os authentication "Operating System Accounts" using
      "password" Credentials denied


PMC-6 Recording Relating to Network Connections
===============================================

* SFTPPlus will log any connection attempt on any of its ports configured to
  listen for file transfer services.

Even if the data communicated over those connections is not a file transfer
protocol, this activity is logged.
For example, an SSH connection attempt is recorded as seen in the logs for the
PMC-7 section.


PMC-7 Recording of Session Activity by User and Workstation
===========================================================

* Session activity by the user is logged.

Each network connection is uniquely identified using the source IP and port.
This information will be associated to any actions logged for the activity by a
connection.

Once a connection is successfully authenticated, the authenticated account is
associated with any action done by that connection as long as the connection
continues being authenticated.

An example of such activity is below:

    | 30014 2017-01-17 11:56:42 Process Unknown 127.0.0.1:50568 New SSH
      connection made.
    | 20137 2017-01-17 11:56:42 single-server-uuid 127.0.0.1:50568 Account
      "eric" of type "os" authenticated as "eric" by os authentication
      "Operating System Accounts" using ssh-key.
    | 30011 2017-01-17 11:56:42 Process user 127.0.0.1:50568 Subsystem SFTP
      successfully started in "/Operations/eric" as "/".
    | 30060 2017-01-17 11:56:42 Process user 127.0.0.1:50568 Canonical file
      name requested for ".".
    | 30019 2017-01-17 11:56:43 Process user 127.0.0.1:50568 Listing folder "/"
      30020 2017-01-17 11:56:43 Process user 127.0.0.1:50568 Successfully
      listed folder "/".


PMC-8 Recording on Data Backup Status
=====================================

* The audit trail is made available in `log/` for Unix-like systems and
  `.\log` for Windows.
  It is available for data backup by the administrator.

Currently there is no option to remove/clean log entries stored in a database
from within the SFTPPlus software.
More details about the audit trail at the
:doc:`event handlers</configuration/event-handlers>` page.

One thing to note is that if log rotation is not enabled, the log file can grow
to an extremely large size.
Log rotation can be enabled in this scenario. When log rotation is enabled,
there is a value to keep all rotated files via `rotate_count` in the
:doc:`event handlers</configuration/event-handlers>` page.


PMC-9 Alerting Critical Events
==============================

* The administrator can set up email notifications based on event rules.

For example, when a connection fails the authentication step for an event with
ID `20078` is created in the log system. Use an email notification event
handler to send emails each time an event with ID `20078` is created by the
log/audit system.

Further details in the
:doc:`email notifications</guides/email-notifications>` page.


PMC-10 Reporting on The Status of The Audit System
==================================================

* Should there be failure in obtaining log recordings in the first place, these
  messages can help meet PMC-8.

For example, if there is a failure to start logging, the details are in
*stdout*:

    | 27.0.0.1:64175 Failed to get logs data since database
      "mysql-db-uuid" is not started.

When an email notification is setup but there is a misconfiguration to the
``email-client`` resource, this is also logged. The example below is for an
event ID ``20076``, which triggered an email notification but led to an error:

    | 20174 2017-01-29 20:20:05 log-email-handler Process 127.0.0.1:0 Failed
      to handle event 20076 by "Log Email Handler". User timeout caused
      connection failure.


PMC-11 Production of sanitised and statistical management reports
=================================================================

* As the PMC relates to management feedback activities, it is outside the scope
  of the software.


PMC-12 Providing a Legal Framework for Protective Monitoring Activities
=======================================================================

* SFTPPlus can help organisations meet the Aware segmentation model of this
  Protective Monitoring Control as it is dependent on meeting, at the minimum,
  PMC-7.
