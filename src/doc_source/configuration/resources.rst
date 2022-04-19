Resources
=========

..  contents:: :local:

SFTPPlus can interact with various external resources in order to execute
related operations, such as sending emails on errors.

The resources are shared for different server operations.
For example the email client can be used for both critical errors or to
inform about a normal operation.

When a component inside the SFTPPlus requires a resource, and the resource
is not already running, that resource is automatically started.

The configurations for the available resources are automatically created when
SFTPPlus starts.

A default SQLite database is enabled in each SFTPPlus installation and has
UUID `DEFAULT-SQLITE`.
This default SQLite database is used by SFTPPlus to provide certain
functionalities like the `Account activity` report or keeping track of the
transferred files to prevent duplicate transfers.


Generic resource options
------------------------

While additional options are available (depending on the resource type),
each resource configuration section has the following standard
configuration options:


name
^^^^

:Default value: ''
:Optional: No
:From version: 3.4.0
:Values: * Any text.
:Description:
    Human-readable short string used to identify this resource.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 3.4.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this resource.


type
^^^^

:Default value: ''
:Optional: No
:From version: 3.4.0
:Values: * `sqlite` - Embedded SQLite database
         * `email-client` - Email client configuration.
         * `lets-encrypt` - Let's Encrypt ACME client.
         * `analytics-engine` - Monitor computer resources used by SFTPPlus.
:Description:
    This option specifies the type of the resource.


SQLite Database
---------------

An `sqlite` resource is configured to allow SFTPPlus to store application data
in an embedded database.

You will need to specify the path.


path
^^^^

:Default value: ``configuration/cache.db3``
:Optional: No
:From version: 4.0.0
:Values: * Path on the local filesystem.
:Description:
    The path to a file where data is stored for this database.


.. _conf-resource-email-client:

Email Client
------------

An `email-client` is configured to allow SFTPPlus to send emails as an
SMTP client via a remote SMTP server.

You will need to specify the address or the fully qualified domain name of the
SMTP server to use and the value to be used by this client for the `From`
field.


address
^^^^^^^

:Default value: ``127.0.0.1``
:Optional: No
:From version: 3.4.0
:Values: * An IP address or a host name.
:Description:
    This option specifies the IP address or the host name of the
    remote server.


port
^^^^

:Default value: ``25``
:Optional: No
:From version: 3.4.0
:Values: * A port number for the server.
:Description:
    This option specifies the IP port of the remote server.


username
^^^^^^^^

:Optional: Yes
:Default value: ''
:Values: * text
         * empty
:From version: 3.4.0
:Description:
    Username used to connect to the server.

    Leave it empty to disable SMTP authentication.


password
^^^^^^^^

:Optional: Yes
:Default value: ''
:Values: * Plain text password.
:From version: 3.4.0
:Description:
    Password used to connect to the server.

    Ignored when no username is defined.


email_from_address
^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^

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


Let's Encrypt Client / CertBot
------------------------------

The `lets-encrypt` resource allows SFTPPlus to automatically
request SSL / X.509 certificates from Let's Encrypt's Certificate
Authority.

It acts as an embedded `certbot`.

Let’s Encrypt is a free, automated, and open certificate authority (CA),
run for the public’s benefit.
It is a service provided by the Internet Security Research Group (ISRG).
It offers everyone a convenient way to get fairly large numbers of
SSL/TLS/X.509 certificates,
in an automated way, completely for free.

You can find out more about Let's Encrypt by `visiting the dedicated website
<https://letsencrypt.org>`_.

As this page focuses on configuration options, refer to the dedicated
:doc:`Let's Encrypt operations </operation/lets-encrypt>` page.

You can only have a single `lets-encrypt` resource defined.
All the file transfer services will use the same unique `lets-encrypt`
resource.

As part of the `lets-encrypt` resource configuration you define the
general options, while each service which uses Let's Encrypt certificate
will have a dedicated option with the domain for which the certificate
is issued .

Below is an example in which three file transfer services define
the domain name for Let's Encrypt::

    [resources/9ac4-1054-f0e4]
    enabled = yes
    name = Let's Encrypt Cert Generator
    type = lets-encrypt
    address = 0.0.0.0
    port = 80
    acme_url = https://acme-v02.api.letsencrypt.org/directory
    contact_email = admin-contact@your-domain.tld
    redirect_url = https://sftp.your-domain.tld/home/

    [services/1c17-4485-878c]
    name = FTPS Explicit
    type = ftp
    ssl_domains = ftps.files.example.com

    [services/17c9-7aa6-2f35]
    name = FTPS Implicit
    type = ftpsi
    ssl_domains = ftps.files.example.com

    [services/de43-bc54-342a]
    name = HTTPS Service
    type = https
    ssl_domains = www.files.example.com, files.example.com


enabled
-------

:Optional: Yes
:Default value: Yes
:Values: * Yes
         * No
:From version: 3.42.0
:Description:
    Set to `Yes` to have Let's Encrypt automatically started when
    SFTPPlus starts.

    Set it to `No` to have the resource stopped.

    You can still manually start and stop the resource from the
    Local Manager.


address
-------

:Optional: No
:Default value: N/A
:Values: * IPv4 address
         * IPv6 address
         * Fully Qualified Domain Name (FQDN).
         * 0.0.0.0
:From version: 3.42.0
:Description:
    Address on which SFTPPlus' Let's Encrypt service will listen for validating
    the HTTP-01 challenge.

    Use `0.0.0.0` to listen on all the available network interfaces.


port
----

:Optional: No
:Default value: 80
:Values: * Port number.
:From version: 3.42.0
:Description:
    Port on which SFTPPlus' Let's Encrypt service will listen for validating
    the HTTP-01 challenge.

    This must be a unique port number for the local machine, to avoid conflicts
    between different services.

    On Unix-like systems, a root account is required for using ports below 1024.


acme_url
^^^^^^^^

:Default value: `https://acme-v02.api.letsencrypt.org/directory`
:Optional: No
:Values: * URL to the ACME Server endpoint.
:From version: 3.42.0
:Description:
    When getting certificates from a server other than the public
    Let's Encrypt server,
    you can use this configuration option to instruct SFTPPlus to
    use a different ACME server.

    Also, you can use it to point to the staging Let's Encrypt server
    at `https://acme-staging-v02.api.letsencrypt.org/directory`.
    Highly recommended during initial deployment and testing.

    Most users don't need to change this configuration,
    and should use the default value.


contact_email
^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Comma-separated list of contact emails for this domain.
:From version: 3.54.0
:Description:
    Optional email contact information provided to the ACME server.

    You can provide multiple addresses as a comma-separated value.

    Let's Encrypt can use these addresses to contact you for issues
    related to certificates obtained by SFTPPlus.
    For example, the server may wish to notify you about server-initiated
    revocation or certificate expiration.

    Leave it empty to not provide any contact information.


redirect_url
^^^^^^^^^^^^

:Default value: empty
:Optional: Yes
:Values: * Absolute URL
:From version: 3.52.0
:Description:
    This configuration option is used to define the URL to which any
    request made to this service is redirected, with the exception of
    Let's Encrypt validation requests.


debug
-----

:Default value: 'No'
:Optional: Yes
:Values: * `Yes`
         * `No`
:From version: 3.50.0
:Description:
    When enabled, the service will emit events with id `20000`
    containing low-level debug messages for the HTTP protocol used by
    Let's Encrypt.

    Configuration changes are applied only to new connections.
    Existing connections respect the `debug` configuration used to
    initiate them.


Analytics and Alerts
--------------------

The `analytics` resource is defined for monitoring and recording the
activity of SFTPPlus.

For example, it collects last user login information that can be
later retrieved and displayed as a report inside the Local Manager.
The logins span across all services configured on the server (FTP, SFTP,
Local Manager, etc.).

At the configured interval, a dedicated event containing the usage counters
is generated.

Exceptional events are emitted when the usage for a resource hits a certain
value / limit.
These events can be linked with the `email-sender` event handler,
in order to raise alerts over email.

An example for monitoring resource usage every 2 minutes (120 seconds),
triggering an exceptional event
when there are more than 1000 total active connections::

    [resources/03c4-1caf-fee0]
    enabled = yes
    name = Analytics Engine
    type = analytics
    monitor_interval = 120
    connections_count_trigger = 1000


enabled
-------

:Optional: Yes
:Default value: Yes
:Values: * Yes
         * No
:From version: 4.0.0
:Description:
    Set to `Yes` to have the resource monitor enabled.

    Set it to `No` to have the resource stopped.

    You can still manually start and stop the resource from the
    Local Manager.


monitor_interval
^^^^^^^^^^^^^^^^

:Default value: 60
:Optional: No
:Values: * Number of seconds
:From version: 3.44.0
:Description:
    Time interval, in seconds, between system resources measurements.

    This value is only used for metrics which require taking constant
    snapshots of the system state.

    Login date, time, and transfer activity is recorded in real time.

    For production environments we recommend setting a value
    equal to or greater than 60 seconds.
    Lower values may impact the overall performance of the system.


memory_resident_trigger
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: 0
:Optional: Yes
:Values: * Number of bytes
         * 0
:From version: 3.44.0
:Description:
    Amount of resident / non-swapped physical memory used by SFTPPlus,
    in bytes, for which to emit an exception event if its process is using
    more than the configured value.

    On Windows, it matches the `Mem Usage` column of the task manager.
    On other OSes, it matches the `RES` column of the `top` command.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


memory_virtual_trigger
^^^^^^^^^^^^^^^^^^^^^^

:Default value: 0
:Optional: Yes
:Values: * Number of bytes
         * 0
:From version: 3.44.0
:Description:
    Total amount of virtual memory used by SFTPPlus, in bytes,
    for which to emit an exception event if its process is using
    more than the configured value.

    This includes both physical memory and swapped memory.

    On Windows, it matches the `VM Size` column of the task manager.
    On other OSes, it matches the `VIRT` column of the `top` command.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


connection_count_trigger
^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: 0
:Optional: Yes
:Values: * Number
         * 0
:From version: 3.44.0
:Description:
    Total number of connections (server-side and client-side) used by SFTPPlus
    for which to trigger an exceptional event.

    This includes the following connection categories:
    * Incoming connections made to file transfer services
    * Outgoing connections made to remote servers through configured transfers
    * Syslog / HTTP Authentication / HTTP Event Handlers connections
    * Connections made to the Local Manager service.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


file_count_trigger
^^^^^^^^^^^^^^^^^^

:Default value: 0
:Optional: Yes
:Values: * Number
         * 0
:From version: 3.44.0
:Description:
    Total number of local files used by SFTPPlus
    for which to trigger an exceptional event.

    This includes all files opened by SFTPPlus
    as part of file transfer operations or for administrative operations.

    For example, log files used by event handlers are included in this count.

    A single connection can trigger the opening of multiple local files.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.


thread_count_trigger
^^^^^^^^^^^^^^^^^^^^

:Default value: 0
:Optional: Yes
:Values: * Number
         * 0
:From version: 3.44.0
:Description:
    Total number of threads used by SFTPPlus
    for which to trigger an exceptional event.

    Take into consideration that multiple transfers can use the same thread.

    Leave it to 0 to disable triggering an event based on the usage of this
    resource.
