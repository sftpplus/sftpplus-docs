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

The Local Manager GUI provides configuration options and status indications
to the state of the `http` or `https` service:

..  image:: /_static/operation/http-https-enabled.png


More resources about the HTTP / HTTPS service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For more details about the configuration options, please go to the dedicated
:doc:`HTTP/HTTPS configuration<../configuration/http-service>` page.

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


Custom Appearance
-----------------

The appearance of the HTTP service pages can be customized by
overwriting the default CSS of the HTTP service pages and executing
custom JavaScript code.

Using the `theme_path` configuration option you can instruct SFTPPlus to
load a custom theme for the HTTP pages.

The theme path should contain at least the `main.css` and `main.js` files.

If you don't need to customize the CSS or JavaScript leave the file empty.

The `main.css` file from the theme path is loaded as the last CSS file.
The `main.jss` file from the theme path is loaded at the end of the page as
the last JavaScript file.

The theme files are accessible inside the HTTP service as `/__chsps__/theme/`.

To load the theme files from ``C:\FTP-Service\Theme`` you need to configure
the service as::

    [services/9ac4-1054-f0e4]
    name = HTTPS File Transfer Service
    type = http

    theme_path = C:\File-Server\Theme

For example ``C:\FTP-Service\Theme\main.css`` can insert the company name
in the top navigation bar, and ``C:\FTP-Service\Theme\main.js`` can be
empty::

    .navbar-fixed-top:after {
        content: "ACME File Transfer Server";
        }

    .navbar-inner {
        min-height: 60px;
        }


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
    port = 10080

    accepted_origins = files.example.com, www.example.com:10443


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

Public access will no longer available after the 23rd of March 2020 as
the public account will expire.::

    [services/9ac4-1054-f0e4]
    name = HTTPS File Transfer Service
    type = https

    public_account_uuid = 92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4

    [accounts/92ad5b32-d8d7-4ed8-94e1-dbb9f01383f4]
    name = public-http
    type = application
    description = Files available without password over HTTP.
    group = 95373161-b944-4d70-af5e-cab1976cc535

    home_folder_path = /local/path/to/public/files
    permissions:
        allow-read, allow-list
        *.exe, deny-full-control
        /reports/, allow-write

    expire_datetime: 2020-03-23

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
