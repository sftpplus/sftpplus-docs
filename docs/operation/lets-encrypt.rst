Let's Encrypt Certificate Automation
====================================

..  contents:: :local:


General description
-------------------

Via the `lets-encrypt` resource, SFTPPlus can act as an ACME client, in order
to generate or renew certificates signed by Let's Encrypt's CA.

Let’s Encrypt is a free, automated, and open certificate authority (CA),
run for the public’s benefit.
It is a service provided by the Internet Security Research Group (ISRG).
It offers everyone a convenient way to get fairly large numbers of
SSL/TLS/X.509 certificates,
in an automated way, completely for free.

You can find out more about Let's Encrypt by `visiting the dedicated website
<https://letsencrypt.org>`_.

The IETF-standardized ACME protocol, RFC 8555, is the ACME v2 protocol used by
SFTPPlus when interacting with the Let's Encrypt service.

The ACME v1 protocol is deprecated as of November 2019,
therefore no longer supported in the latest version of SFTPPlus.

You can still use SFTPPlus with ACME v1 until June 2021, assuming that
your first request for your certificate was issued before November 2019
and you keep using SFTPPlus version 3.53.0 or older.

This page focuses on the implementation and operation of SFTPPlus'
Let's Encrypt ACME client.
For configuration information, refer to the dedicated
:doc:`Let's Encrypt configuration reference
</configuration/resources>` page.

SFTPPlus acts as an embedded `certbot`.
Installing `certbot` is not required.
SFTPPlus includes its own Let's Encrypt client that is independent of `certbot`.


Available Challenge
-------------------

A *challenge* is a method/process used by SFTPPlus to prove that
it has control over a specific domain.
This is done in order to prevent other people from obtaining certificates
for the domains you own.

`HTTP-01` is the only challenge supported, and it uses port 80.
SFTPPlus provides a self-contained implementation of the `HTTP-01` challenge.
There is no need for an external web server or a separate `certbot`.

Wildcard certificates are not supported by the HTTP-01 challenge, hence
not supported in SFTPPlus.
As a workaround, you can create a single certificate with up to 100 names.

`TLS-SNI-01`, which uses port 443 is not supported,
as it was `discontinued for security reasons
<https://community.letsencrypt.org/t/50811>`_.

`DNS-01` requires configuration of a DNS server on port 53,
and it's not supported.
Most often, the DNS server doesn't run on the same machine as SFTPPlus,
making the deployment more complicated
and introducing dependencies on external services.


HTTP-01 Challenge Deployment
----------------------------

In order for SFTPPlus to prove that it is the legitimate owner of the
requested domain,
the Let's Encrypt server will ask SFTPPlus to host a file at a fixed URL.

For example, to get a certificate for domain `ftp.example.com`, the SFTPPlus
server should be reachable at `http://ftp.example.com:80/`.

This means that port `80` should be open on the server hosting the
SFTPPlus instance, or be forwarded to the SFTPPlus instance.

In order to successfully obtain a certificate for a domain like
``ftp.your-domain.com`` you need to configure your DNS so that the
``ftp.your-domain.com`` domain will resolve to an IP address used by
SFTPPlus.
The DNS record should be configured and active before making any
certificate requests.


Running SFTPPlus behind a firewall or load balancer
---------------------------------------------------

When SFTPPlus is behind a firewall or a load balancer,
it's important to make sure that port 80 is forwarded to
SFTPPlus' Let's Encrypt resource.

In such a setup, SFTPPlus's Let's Encrypt resource can be configured with any
port, as long as the public port 80 is forwarded to SFTPPlus.


Running SFTPPlus together with an external web server on port 80
----------------------------------------------------------------

If you already have another server on port `80` handling
the ``http://ftp.your-domain.com/`` URLs,
you should configure a proxy or redirection for the
`.well-known/acme-challenge/` URL.

Any request made to ``http://ftp.your-domain.com/.well-known/acme-challenge/``
should be forwarded to ``http://12.23.45.67:1234/.well-known/acme-challenge/``
where ``12.23.45.67`` and ``1234`` is the IP address and port of the
SFTPPlus instance.


Setting Let's Encrypt for a new service
---------------------------------------

SFTPPlus can automatically manage the SSL/TLS certificates for any file
transfer service which uses it.

When adding a new service, a Let's Encrypt issued certificate might not
be already available.
The new service will start with a provisional self-signed certificate.
SFTPPlus will automatically update the certificate as soon as a new
certificate is obtained from Let's Encrypt.

A self-signed certificate is auto-generated with each new SFTPPlus
installation, and used by default for services created via the Web Manager.

By starting with a self-signed certificate, you can validate that all the
other configurations are set up and working according to your needs.
Once the service works with a self-signed certificate, you can move to
using Let's Encrypt certificates.


Certificate Generation / Renewal
--------------------------------

When the SFTPPlus `lets-encrypt` resource starts,
it will automatically generate certificates for all newly configured
domains.
At start, it will check all the previously generated certificates and
automatically renew certificates which are **older than 60 days**.

Any certificate generated by Let's Encrypt is **valid for 90 days**.

While the SFTPPlus `lets-encrypt` resource is running,
it will schedule automatic renewal for the configured domains, one per day.

Once a certificate is generated or renewed, SFTPPlus will automatically
restart the file transfer services configured to use those certificates.

If a certificate is about to **expire in less than 15 days**, SFTPPlus will
emit a dedicated failure event and will try again the next day.

When `lets'encrypt` is started for the first time for a file transfer service,
there is no previous certificate available for that service.
The service requires a certificate in order to start.
SFTPPlus will use **a temporary TLS placeholder** certificate while a new certificate is obtained from Let's Encrypt.
This placeholder certificate is automatically generated when SFTPPlus is installed and is regenerated at each update.


Account Registration
--------------------

No manual or external account creation is required.

SFTPPlus will automatically create an account and register it to the
Let's Encrypt server.

A registered account is required before asking the Let's Encrypt server to
issue new certificates.

If you already have a Let's Encrypt account and would like to use that
account for the certificates managed by SFTPPlus,
get in touch at support@proatria.com,
and we will provide instructions for setting up an existing account.


Store keys and certificates as files
------------------------------------

You can configure the SFTPPlus Let's Encrypt resource to automatically save the generated keys and certificates as files in a local directory of your choice.

It will store the keys and certificates using a directory structure similar to the one used by `certbot`.
There is a sub-directory for each certificate.
Separate files are created for the private key, the certificate, the ca chain, and the certificate+ca chain.

For example, with the configuration provided below::

    [resources/17c97aa6-1c17-4485-878c-68b427b82f35]
    type = lets-encrypt
    name = lets-encrypt-public

    store_directory = /etc/ssl

When a Let's Encrypt certificate for domains `example.com, www.example.com` is obtained, the following files are saved:

* /etc/ssl/example.com_www.example.com/privkey.pem - Private key for the certificate.
* /etc/ssl/example.com_www.example.com/fullchain.pem - All certificates, including the domain certificate and_the certification authority chain certificates.
* /etc/ssl/example.com_www.example.com/chain.pem - Only the domain certificate.
* /etc/ssl/example.com_www.example.com/cert.pem - The certification authority chain certificates.

Each time the keys and certificate files are updated, the event with ID `20015` is emitted for each domain.

The keys and certificates files are also recreated each time the Let's Encrypt resource is started.
If the content of the certificate is updated the event with ID `20015` is emitted.

When failing to store the keys and certificates on the local filesystem, the event with ID `20009` is emitted.

When `store_directory` is not configured, no external key or certificate file is created.

..  note::
    SFTPPlus does not automatically delete unused certificates or expired certificates.
    Let's Encrypt certificates are valid for 90 days.
    You can safely delete any files older than 90 days.


Testing and Experimentation
---------------------------

You can check that SFTPPlus' Let's Encrypt resource
is correctly configured by accessing the following URL from a remote computer:
``http://ftp.your-domain.com/.well-known/acme-challenge/test.txt``.

You should see a page with the `Let's Encrypt Ready` text.

For testing or casually checking out the Let's Encrypt integration,
we highly recommend testing against the Let's Encrypt staging environment
before using the Let's Encrypt production environment.

This will allow you to get things right before issuing trusted certificates,
and reduce the chance of hitting the request rate limits.

The `acme_url` configuration option is used to instruct SFTPPlus to use
different Let's Encrypt environments.

For production, the configuration will look like::

    [resources/17c97aa6-1c17-4485-878c-68b427b82f35]
    type = lets-encrypt
    name = lets-encrypt-public

    address = 0.0.0.0
    port = 80
    acme_url = https://acme-v02.api.letsencrypt.org/directory


For testing/staging, the configuration will look like::

    [resources/17c97aa6-1c17-4485-878c-68b427b82f35]
    type = lets-encrypt
    name = lets-encrypt-testing

    address = 0.0.0.0
    port = 80
    acme_url = https://acme-staging-v02.api.letsencrypt.org/directory


Let's Encrypt Request Limits
----------------------------

The main Let's Encrypt ACME server imposes a set of limits, in terms of how
often you can request new certificates.

SFTPPlus does not impose any extra limit, and will rely on the limits defined
on the remote Let's Encrypt / ACME server.

You will see an error message when SFTPPlus operations exceed a certain
limit.

You can find up to date information about the certificate generation
limits on the
`Let's Encrypt Rate Limit <https://letsencrypt.org/docs/rate-limits/>` page.

When testing an SFTPPlus deployment, use the Let's Encrypt staging environment,
as documented in previous sections.
