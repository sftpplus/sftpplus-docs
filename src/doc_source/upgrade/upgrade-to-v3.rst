Upgrade to version 3
====================

..  contents:: :local:


Introduction
------------

SFTPPlus version 3 was released in 2015.
It is no longer a supported version.
The information on this page is provided for legacy deployments.

If you are still using SFTPPlus version 3 and you plan to upgrade to latest SFTPPlus version,
get in touch with our support team.
They can help you upgrade to the latest supported version.


Upgrading from version 2 to version 3
-------------------------------------

When upgrading from versions 2 to version 3,
it is required to first uninstall the existing SFTPPlus version.
Reinstall SFTPPlus and integrate the existing configuration in the new system.

There are significant changes for the logging and authentication parts.

The upgrade steps are describe below:

* It is recommended to perform the upgrade in a maintenance window and make
  sure there are no active file transfers.

* Stop the SFTPPlus service.

* Copy the configuration directory to a backup location.
  Optionally, consider copying the log files as well.

* Uninstall the SFTPPlus version running on your server.

* Download the latest version of SFTPPlus 3, and install it on your
  machine.

In version 3, the default configuration file is still named `server.ini`.

To enable the new authentication method for `application` and `os`
accounts, you will need to update the `authentications` option inside the
`[server]` section, and add a dedicated method for application accounts.

Below is what the relevant parts of the `[server]` configuration should look
like::

    [server]
    authentications = application-uuid, os-uuid, OTHER-AUTH-UUID
    manager_authentications = application-uuid

    [authentications/03288e36-cf6b-4bd5-a9be-f421372f17e6]
    enabled = Yes
    type = application
    name = Application Accounts
    description = This authentication method allows authentication accounts
        defined in this configuration file.

    [authentications/6d51ed1e-35ec-41d7-8b51-53e56c716212]
    enabled = Yes
    type = os
    name = Operating System Accounts
    description = Accounts provided by the operating system.

To migrate the authentication of global SFTPPlus accounts, remove the
`sftpplus_webadmin` option from the `server` section::

    [server]
    sftpplus_webadmin = http://wsftp.example.com:8080/SFTPPlus/

And replace it with a dedicated `authentications` method::

    [server]
    authentications = OTHER-AUTH-UUID, legacy-webadmin-uuid, MORE-AUTH-UUID

    [authentications/9g51ed1e-35ec-41d7-8b51-53e56c716313]
    enabled = Yes
    type = legacy-webadmin
    name = Legacy SFTPPlus Webadmin

    url = http://wsftp.example.com:8080/SFTPPlus/

To migrate the account `report`, create a new event handler.
In the configuration file, replace::

    [report]
    database = sqlite-db-uuid

With a new `event-handlers` section::

    [event-handlers/8cace339-a2ee-4899-b64e-db2478821b9e]
    enabled = No
    type = account-activity
    name = Account activity
    description = Report last successful login for accounts and administrators.

    database = sqlite-db-uuid

To migrate the file log handler, remove the `logs` handler section::

    [logs/03288e36-cf6b-4bd5-a9be-f421372f17e6]
    enabled = Yes
    name = Default Local Log File
    description = Append logs to a file on the local filesystem.

    type = file

    path = log/server.log

And replace it with a dedicated `event-handlers` section::

    [event-handlers/00feb81f-a99d-42f1-a86c-1562c3281bd9]
    enabled = Yes
    name = Default Local Log File
    description = Append logs to a file on the local filesystem.

    type = local-file

    path = log/server.log

To migrate the Windows EventLog log handler, remove the `logs` handler
section::

    [logs/f643a93d-94d5-4b41-b723-a63a00e3c902]
    enabled = Yes
    name = SFTPPlus Server
    description = Send logs to Windows Event Log Service on local machine.

    type = eventlog

And replace it with a dedicated event handler of `type` ``windows-eventlog``::

    [event-handlers/515361f1-d976-4fe0-979b-0651e2bf591d]
    enabled = Yes
    name = STFPPlus
    description = Send logs to Windows Event Log Service on local machine.

    type = windows-eventlog

To migrate the WebAdmin HTTP Post Request log handler, remove the `logs`
section for the Webadmin HTTP Post::

    [logs/e16af067-8974-4c0d-ae89-eb5f3d59fd65]
    name = Default_WebAdmin
    enabled = No
    name = WebAdmin HTTP Post
    description = Hook to WebAdmin over HTTP.

    type = http-post
    format = webadmin

    url = http://int.example.com/SFTPPlus/AuditAddSimple.php

And create a new `event-handlers` section as::

    [event-handlers/03288e36-cf6b-4kd5-a9be-f421372f17e6]
    enabled = No
    name = WebAdmin HTTP Post
    description = Send logs to Legacy WebAdmin over HTTP.

    type = http
    format = legacy-webadmin

    url = http://int.example.com/SFTPPlus/AuditAddSimple.php

To convert legacy SQLite/MySQL database loggers, you should delete section(s)::

    [logs/0ef580fe-45cb-47e0-b434-c0e44557b364]
    enabled = Yes
    name = SQLite Legacy Log Handler
    description = Send logs to local SQLite file in legacy mode.

    type = sqlite
    path = log/server.db3

And add two new sections, one for the `databases` and one for the
`event handlers`::

    [databases/27b8e2b1-7971-416d-af14-6a8aae2ac46e]
    enabled = Yes
    name = SQLite
    description = SQLite file database connection.

    type = sqlite
    path = log/server.db3

    [event-handlers/22a9d8fb-068d-4a63-8d5d-0ce94ef22a25]
    enabled = Yes
    name = SQLite Event Handler
    description = Store events in local SQLite file.
    type = database
    database = sqlite-db-uuid

If there is already a section for the desired database, you do not need to
create a section for it, just make sure to use the existing database UUID.

Make sure your database UUID matches the one configured for the event handler
in order to pair them.

For MySQL logger(s), you should delete the `logs` section::

    [logs/6d51ed1e-35ec-41d7-8b51-53e56c716212]
    enabled = No
    name = MySQL Legacy Log Handler
    description = Send logs to MySQL database in legacy mode.

    type = mysql

    address = 172.20.0.24
    port = 3306
    username = test
    password = test
    database = test

And create two new sections for `databases` and `event-handlers`::

    [databases/ac547e16-a3ff-4fc3-a6ab-142af2744f50]
    enabled = No
    name = MySQL
    description = MySQL database connection.

    type = mysql

    address = 172.20.0.24
    port = 3306
    username = test
    password = test
    database = test

    [event-handlers/7db823d8-05f8-4481-be98-b87a826ded28]
    enabled = No
    name = MySQL Event Handler
    description = Store events in a MySQL database
    type = database
    database = mysql-db-uuid

The above note on SQLite's database section also applies to MySQL's database
section.

To migrate the Syslog log handler, remove the `logs` handler section::

    [logs/27a31405-a963-4fb9-b4ee-09d415b1a30a]
    enabled = Yes
    name = Syslog Backup
    description = Sends logs to backup syslog server.

    type = syslog

    url = udp://127.0.0.1:
    port = 514

And replace it with a dedicated `event-handlers` section::

    [event-handlers/1ee4337a-22f7-4a67-9a77-5c3a508a8158]
    enabled = Yes
    name = Syslog Backup
    description = Sends logs to backup syslog server.

    type = syslog

    url = udp://127.0.0.1:514

For converting the database log handler into an event handler, remove the
`logs` section::

    [logs/bdfe8e48-5100-4d8a-bac1-441ebc04f9a7]
    enabled = Yes
    name = SQLite Log Handler
    description = Send logs to local SQLite file.
    type = database
    database = sqlite-db-uuid

And replace it with a dedicated `event-handlers` section::

    [event-handlers/681f5f5d-0502-4ebb-90d5-5d5c549fac6b]
    enabled = Yes
    name = Database Event Handler
    description = Send logs to local SQLite file.
    type = database
    database = sqlite-db-uuid
