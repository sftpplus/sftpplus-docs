HTTP / HTTPS Service
====================

..  contents:: :local:


Introduction
------------

This page contains information on the usage and behaviour of the `http` and
`https` file transfer services.

The HTTP / HTTPS file transfer service provides a HTML-based interface
designed to work in any web browser,
including older versions of browsers where JavaScript or cookie features are
either not supported or enabled.

The HTTP protocol is implemented based on
`RFC 2616 <http://tools.ietf.org/html/rfc2616>`_,
while the HTTPS protocol is based on
`RFC 2818 <http://tools.ietf.org/html/rfc2818>`_.

The Web Manager GUI provides configuration options and status indications
to the state of the `http` or `https` service:

..  image:: /_static/operation/http-https-enabled.png


More resources about the HTTP / HTTPS service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For more details about the configuration options, please go to the dedicated
:doc:`HTTP/HTTPS configuration</configuration-server/http-service>` page.

For those interested in working with the HTTP Service JSON-based API, please
refer to our :doc:`Developer Documentation </developer/index>`.


File management functionality
-----------------------------

..  image:: /_static/operation/http-service.png


Above is a screenshot of the HTTP / HTTPS file management functionality.

----

..  image:: /_static/operation/http-invalid-folder-structure.png


Above is a screenshot of how errors are communicated - in this case, when an
invalid folder is being created.

----

The HTTP and HTTPS service allows the same level of file access as the other
available file transfer services such as FTPS or SFTP.

When using the file transfer service in a browser without JavaScript or
cookies, some of the advanced features are not available.

Basic features, listed below, are supported:

* Authenticate using HTTP Basic Auth method
* Navigate folders' structure
* Download files
* Create new folders
* Upload files
* Delete files and folders
* Recursive deletion of a folder


Legacy UI Appearance
--------------------

Latest versions of SFTPPlus include an updated web user interface that for
added functionality convenience are using web browser capabilities only
available in latest generation web browsers.

For legacy purposes or to avoid disrupting existing web UI file transfer
processes,
you can configure the HTTP web client to use an older version of the
user interface::

    [services/9ac4-1054-f0e4]
    name = HTTPS File Transfer Service
    type = http

    ui_version = ui-gen-1

This will use the UI available in SFTPPlus version 4.15.0 or older.

The latest UI version is `ui_version = ui-gen-2`.


Custom Appearance
-----------------

..  attention::
    The custom appearance functionality is released as a `feature preview`.
    We encourage you to try this functionality and send feedback.
    The HTML and CSS markup might be changed in future releases.

The appearance of the HTTP service pages can be customized by
overwriting the default CSS of the HTTP service pages and executing
custom JavaScript code.

Using the `theme_path` configuration option you can instruct SFTPPlus to
load a custom theme for the HTTP pages.

The theme path should contain at least the following files:

* `main.css`
* `main.js` (only available in gen1)
* `logo.svg` (only available in gen2)
* `favicon.ico`

If you don't need to customize the CSS or JavaScript leave the file empty.

The name of the HTTP/HTTPS service will be used as the page name on the login page and the file browser page.

..  note::
    When changing the service name, you will need to restart the HTTP/HTTPS service.
    Restarting the whole SFTPPlus application is not required.

The `main.css` file from the theme path is loaded as the last CSS file.
The `main.jss` file from the theme path is loaded at the end of the page as
the last JavaScript file.

The theme files are accessible inside the HTTP service as `/__chsps__/theme/`.

To load the theme files from ``C:\File-Server\Theme`` you need to configure
the service as::

    [services/9ac4-1054-f0e4]
    name = HTTPS File Transfer Service
    type = https

    theme_path = C:\File-Server\Theme

For example ``C:\File-Server\Theme\main.css`` can make buttons rounder and hide the MFA field on the login page
(while ``C:\File-Server\Theme\main.js`` can be empty)::

    .btn.btn-outlined {
        border-radius: 1.125rem;
    }

    [data-theme="login-mfa-input"] {
        display: none;
    }

Below is the list of `data-theme` HTML attributes that control the appearance of parts of the login page::

    * `data-theme="login-username-prompt"` Username label and input
    * `data-theme="login-password-prompt"` Password label and input
    * `data-theme="login-mfa-input"` MFA/TOTP code label and input
    * `data-theme="login-no-cookies"` Link to authenticate for browser without cookie enabled
    * `data-theme="login-username-password"` Button to authenticate with username/password credentials
    * `data-theme="login-oidc"` OpenID Connect or MS Entra ID login label and button
    * `data-theme="login-oidc-alternative"` Text presented when OpenID Connect is an alternative login method
    * `data-theme="login-footnotes-button"` Button that triggers the login dialog to display terms or service or usage help information.
    * `data-theme="login-footnotes-dialog"` UI dialog element in which the terms or service or usage/help information is displayed.

If you find it hard to customize certain UI elements, get in touch with us.
We will consider updating the default HTML / CSS markup to make it easier for you to apply custom CSS rules.


Custom service information link
-------------------------------

You can configure the login page to show a custom link which opens a message box with more info when pressed.

This is done using the `login_footnotes` configuration option.
This configuration option is defined on multiple lines.

To define a link with the text `Terms of Service`
that opens a message box titled `ACME Company Terms of Service`
containing your terms of services,
use a configuration similar to this example::

    [services/9ac4-1054-f0e4]
    name = HTTPS File Transfer Service
    type = https

    login_footnotes = Terms of Service
        ACME Company Terms of Service

        Posted: 21 March 2024
        Effective: 1 June 2024

        Thank you for using our product!

        These Terms of Service cover your use of the ACME Company services.
        When you use our services, you provide us your files and their content.

        These terms don't give us any rights to your content, except for the limited rights that enable us to offer these services.


Custom trigger buttons
----------------------

Using the `triggers` configuration of the HTTP and HTTPS file transfer service,
you can define one or multiple custom buttons
which are displayed on the web client page.

When defining the action name for a trigger, make sure you don't use common
operation names like `delete`, `create-folder`, `upload-file`, which will
conflict with the existing file operations.

When pressed, these buttons will emit the event with ID 40043,
event which can be linked to an event handler
to trigger one or more actions on the selected files.

The following types are available:
    * `primary` (dark blue)
    * `info` (light blue)
    * `success` (green)
    * `warning` (amber)
    * `danger` (dark red)
    * `inverse` (black)

You can define custom button types, by creating `btn-TYPE_NAME` CSS
classes inside the custom CSS file defined via `theme_path`.

The buttons can be displayed for all users, or only for the members of a
specific group.

When no group configuration is defined, the button is displayed for members
of all groups.

If you want a button to be visible to members of multiple groups, create
separate trigger definition for each group.

Below is an example of 4 buttons which will be displayed under the following
conditions.

`Approve` is a green button available only to members of the supervisor group.

`Reject` is an amber button available to members of the supervisor group and
the users group.

`Cancel` is a light-blue button available only to members of the users
groups.

`Report` button is a red button displayed for any user.

    [services/9ac4-1054-f0e4]
    name = HTTPS File Transfer Service
    type = http

    triggers:
      Approve, success, SUPERVISORS_GROUPS_UUID
      Reject, warning, SUPERVISORS_GROUPS_UUID
      Reject, warning, USERS_GROUPS_UUID
      Cancel, info, USERS_GROUPS_UUID
      Raise incident, danger

..  image:: /_static/operation/http-service-custom-buttons.png


Load Balancer
-------------

The HTTP/HTTPS services of SFTPPlus can be integrated in a
load balancing solution.

SFTPPlus requires no extra configuration
when functioning behind a layer 4 TCP balancer or DNS load balancer.

AWS Network Load Balancer and Azure Load Balancer are examples of layer 4
load balancers.

For Layer 4 load balancers,
make sure the forwarded traffic has a persistent session based on the
client's source IP address.

When using a layer 7 HTTP/HTTPS load balancer, you will need to adjust
Cross-Site Request Forgery (CSRF) protection.
This is because the HTTP load balancer is not updating some of the headers
found in the initial request when forwarding a request
to the load balanced node.
This result in a request that appears to be coming from a different site.

AWS Application Load Balancer and Azure Application Gateway are examples of
Layer 7 load balancers.

For HTTP / Layer 7 load balancers,
make sure the forwarded traffic has sticky sessions enabled.

When the HTTP/HTTP file transfer service is not configured for the
load balancer, you will see `400 Possible CSRF` errors.

When the load balancer is configured with the listeners
``https://files.example.com`` on default port 443 and
``https://www.example.com`` on port 10443, and it
forwards all requests to SFTPPlus at ``http://worker1.example.com``,
you will need to configure SFTPPlus as follows::

    [services/9ac4-1054-f0e4]
    name = HTTPS File Transfer Service
    type = http
    address = worker1.example.com
    port = 18080

    accepted_origins = files.example.com, www.example.com:10443

If you have an HTTP (unsecure) load balancer that is accesses by the users as
``http://files.example.com`` and it forwards all requests to SFTPPlus at ``http://worker1.example.com``,
you will need to configure SFTPPlus as follows,
adding `http` as the first value for `accepted_origins`::

    [services/9ac4-1054-f0e4]
    name = HTTPS File Transfer Service
    type = http
    address = worker1.example.com
    port = 18080

    accepted_origins = http, files.example.com


AS2 receive site
----------------

SFTPPlus can receive files using the EDIINT AS2 protocol defined in the
`RFC 4130 <https://tools.ietf.org/html/rfc4130>` standard.

If you want to send files over AS2, you need to use an HTTP AS2
transfer as documented on
:doc:`the HTTP AS2 transfer page </operation-client/http>`.

Received content can be confirmed using the
message disposition acknowledgment (MDN) method defined in
`RFC 3798 <https://tools.ietf.org/html/rfc3798>`.

File content can be compressed as defined in
`RFC 5402 <https://tools.ietf.org/html/rfc5402>`, encapsulated in a
CMS (Cryptographic Message Syntax) MIME entity.

We recommend setting up the message exchange with your AS2 partner
using username and password or username and SSL certificate credentials
authentication.

For HTTP authenticated requests,
SFTPPlus uses the `username` found in the AS2 HTTP authentication
request to recognize and authorize an AS2 partner.
In this case,
the `AS2-From` value found in an AS2 message is only informative,
but it is required in all messages by the AS2 standard.

The AS2 messages should be sent using the `POST` HTTP request verb/method.
The `HEAD` HTTP verb is provided as a way to validate the HTTP basic authentication credentials,
without triggering any AS2 file transfer.

You add an AS2 partner by creating a normal SFTPPlus file transfer account.

While the AS2 messages are received, the partial files are stored in the home path as configured
for each user, in a sub-directory defined by the `as2_pending_path` configuration.

After the AS2 message is fully received and validated,
the files from the AS2 messages are stored in the home path as configured for each user,
in a sub-directory defined by the `as2_receive_path` configuration.

If no `Content-Disposition` header is found in the AS2 request describing
the name of the required file, SFTPPlus will store the received data using
the name `as2-received-file.TIMESTAMP`, where TIMESTAMP is replaced with
the date and time at which the file transfer was initiated.
To use a different filename for this case,
define the `as2_default_filename` configuration option.

Files received via AS2 will have to comply with the general security
policy and permissions, similar to any other file transfer protocol.

The public AS2 site is available at the `https://example.tld/as2receive` URL,
where the `as2receive` URL fragment is defined by the `as2_receive_name`
configuration option::

    [services/9ac4-1054-f0e4]
    name = HTTPS with AS2 File Transfer Service
    type = https

    as2_organization = ACME Org
    as2_receive_name = as2receive
    as2_pending_path = /as2/pending
    as2_receive_path = /as2/receive
    as2_receive_key = -----BEGIN RSA PRIVATE KEY-----
        MIICXgIBAAKBgQDOoZUYd8KMYbre5zZIwR+V6dO2+cCYVS46BHbRbqt7gczkoIWh
        MORE RSA KEY CONTENT
        Wh+QF3UArO8r8RYv3HRcnBjrGh+yEK93wIifVNGgy63FIQ==
        -----END RSA PRIVATE KEY-----
    as2_receive_certificate = -----BEGIN CERTIFICATE-----
        MIICaDCCAdGgAwIBAgIBDjANBgkqhkiG9w0BAQUFADBGMQswCQYDVQQGEwJHQjEP
        MORE CERTIFICATE CONTENT
        JZQaMjV9XxNTFOlNUTWswff3uE677wSVDPSuNkxo2FLRcGfPUxAQGsgL5Ts=
        -----END CERTIFICATE-----

    [accounts/4a48fbf4-d029]
    name = johnd
    home_folder_path = C:/Users/JohnD
    ; One or more certificates used by the remote partner to sign the
    ; received files.
    as2_certificates = -----BEGIN CERTIFICATE-----
        MIICpTCCAg6gAwIBAgIIP8vt0MYYvNIwDQYJKoZIhvcNAQELBQAwRjELMAkGA1UE
        MORE CERTIFICATE CONTENT
        JZQaMjV9XxNTFOlNUTWswff3uE677wSVDPSuNkxo2FLRcGfPUxAQGsgL5Ts=
        -----END CERTIFICATE-----
        -----BEGIN CERTIFICATE-----
        MIICoDCCAgmgAwIBAgIIKk0/vqmeDb4wDQYJKoZIhvcNAQELBQAwODELMAkGA1UE
        MORE CERTIFICATE CONTENT
        6sXcntbQ8jyu8fNCjoVKGUe9gsgZOK2KapWxU7HzvulVQslcOcWG3mM=
        -----END CERTIFICATE-----

    [accounts/758185de-d029]
    name = janer
    home_folder_path = C:/Users/JaneR
    permissions =
        allow-full-control
        *.exe, deny-full-control

With the above configuration, files received via AS2 for account `johnd` are
temporarily stored in `C:/Users/JohnD/as2/pending`.
Once the AS2 transfer is complete, the files are moved to `C:/Users/JohnD/as2/receive`

The files received by the `janer` account are temporarily stored in `C:/Users/JaneR/as2/pending` and then moved into `C:/Users/JaneR/as2/receive`.

At the same time, any file with a name ending in `.exe` uploaded by account `janer` is rejected.

..  note::
    Encrypted received messages should be encrypted using an RSA key.
    DSA public key-based encryption is not supported.
    Contact us if you need to encrypt AS2 messages using DSA.

Non-authenticated AS2 messages are supported and the account name will match
the value of the `AS2-From` HTTP header.
You need to explicitly configure an account to not require HTTP authentication
for AS2 messages.

Below is an example in which the configuration will allow a partner with
ID ``AS2 Trade aMjV9XxNTFO`` to send AS2 messages without HTTP authentication.
It is highly recommend to restrict the source IP for this account,
as without HTTP authentication anyone can send messages for this account,
just by knowing the name of the trading partner::

    [accounts/4a48fbf4-d029]
        name = AS2 Trade aMjV9XxNTFO
    home_folder_path = C:/Users/JohnD

    as2_require_http_authentication = No
    source_ip_filter = allow 24.12.231.0/24

When filtering by source IP is not possible and your requirement is to
receive AS2 messages without authentication, we recommend to add a
long and hard to guess value for your trading partner.
This is why the above example uses the ``aMjV9XxNTFO`` value in the
``AS2 Trade aMjV9XxNTFO`` partner name.

When signed files are received, SFTPPlus will validate the configuration
using the public certificate configured in the `as2_certificates` option
in the user account.

When encrypted files are received, SFTPPlus will decrypt them using the
RSA private key defined at `as2_receive_key` or `as2_receive_certificate`.

When signed message disposition notifications (MDN) are requested,
SFTPPlus will sign them using the private key configured at `as2_private_key`
and the certificate configured at `as2_receive_certificate`.

The delivery for asynchronous(ASYNC) MDN is retried 5 times,
waiting 1 minutes for the first retry, they 2 minutes,
and waiting 1 minute more with each retry.

The async MDN HTTPS request is made using the same TLS methods and
ciphers configured for the HTTPS service over which the initial AS2 message
was received.

When the remote partner is requesting an async MDN over HTTPS, the remote
HTTPS connection is authenticated using the HTTPS SSL/TLS certificates
configured for the associated account as part of the `as2_async_mdn_ca`
configuration.

Our recommendation is to set up file transfers with your AS2 partner using
synchronous MDN. This simplify the network configuration and provides
improved security.

You can disable the support for async MDN by setting the
`as2_async_mdn_ca` to the empty value.

Asynchronous MDN response delivery errors will emit a dedicated failure event.

No extra event is emitted on the successful delivery of synchronous or
asynchronous MDNs,
other than the general event for the successful receiving of the AS2 message.


Public site
-----------

SFTPPlus can serve as a public file transfer server.
Visitors can access files on the server without prior authentication.
This is similar to the Anonymous mode available in the FTP server, with the
exception that no username is required.

To enable public access, you need to explicitly define an application account
to be used for handling the files via the public interface.

The account will define the path from where the public files are served and
the permissions used for each file.

The public site is not limited to read-only access.
Visitors of the public site will have the same access as defined in the
public account configuration.

The public file access is recorded in the audit log under the
configured account.
It is recommended to set up a dedicated account for the public access and
not to reuse an existing account.

Below is an example for a general download-only public root access,
which will deny downloading any ``.exe.`` file and
allow uploading files inside the ``/reports/`` folder.

The public files will be available at the
following URL: `https://example.tld/public-access`.

In this example, public access will no longer be available after the
23rd of March 2025, when the public account is set to expire.::

    [services/9ac4-1054-f0e4]
    name = HTTPS File Transfer Service
    type = https

    public_account_uuid = 92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4
    public_name = public-access

    [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
    name = public-http
    type = application
    description = Files available without password over HTTP.
    group = 95373161-b944-4d70-af5e-cab1976cc535

    home_folder_path = /local/path/to/public/files
    permissions =
        allow-read, allow-list
        *.exe, deny-full-control
        /reports/, allow-write

    expire_datetime: 2025-03-23

    [groups/95373161-b944-4d70-af5e-cab1976cc535]
    name = http-group
    virtual_folders: /shared, /ftp-files/shared

The `create_home_folder` and `home_folder_structure` account and group
configurations are ignored for the public HTTP access.


Authentication Process
----------------------

The HTTP file transfer service will use a single cookie to manage the
authentication process.

A single session cookie is used for all the file transfer operations.

The session cookie is set with `httpOnly` and `sameSite` options.
For the HTTPS service, cookies are set with the `secure` option.

For simple usage via the command line with tools like as cURL or Wget,
HTTP Basic Auth is available.

..  warning::
    HTTP Basic Auth will send credentials in a plain text encoding and it is
    not recommended to use HTTP Basic Auth over unsecured HTTP connections.


Usage Without Cookies
---------------------

While we recommend using the HTTP file transfer server from a browser which
allows cookies, SFTPPlus can be used without cookies.

The lack of availability of HTTP cookies will not affect the HTTP service
server-side functionalities.

To trigger the authentication process you will need to access the file
transfer service using the following URL::

    https://SERVER:PORT/home/?without-cookies

When HTTP cookies are not available,
the authentication in a web browser is done via HTTP Basic Auth.
The logout functionality is not available without cookies.


..  warning::
    HTTP Basic Auth will send credentials in a plain text encoding and it is
    not recommended to use HTTP Basic Auth over unsecured HTTP connections.


HTTP/1.1 100 Continue Status Code
---------------------------------

HTTP/HTTPS file transfer service can handle HTTP/1.1 client requests
made using the 100 (Continue) status.
This allows the client sending the request message with a given
request body to determine whether the origin server is willing to accept the
request (based on the request headers) before the client sends the request
body.

For example, it might be inappropriate or highly inefficient for the client to
send a large body if the server rejects it solely based on the body size.
