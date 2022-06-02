Let's Encrypt client / CertBot
==============================

..  contents:: :local:


Introduction
------------

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
--------

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
-------------

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
------------

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
