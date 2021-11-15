Local Configuration Manager
===========================

..  contents:: :local:


Introduction
------------

The Local Configuration Manager (also known as Local Manager) is an
embedded service for handling the configuration of SFTPPlus.
It looks and behaves like a regular web application and works in any
modern web browser.

The configuration options are detailed in the
:doc:`Local Manager Configuration </configuration/local-manager>` page.

----

Below is a screenshot of the Local Manager authentication page, notice
that it is only available over **HTTPS**:

..  image:: /_static/operation/local-manager-login.png

----

Local Manager comes with a default administration account with username
`admin` and a password set during the configuration initialization.

While using the Local Manager graphical user interface, you have
access to integrated documentation, assistance, and validation which will
guide you through the configuration process.

The following actions are available from within the Local Manager:

* View current server configuration.
* Perform generic server configuration.
* Configure logging services.
* Configure the Local Manager itself.
* Add / remove / configure file transfer services with
  all supported protocols.
* Add / remove / configure local manager services.
* Add / remove / modify administrators, roles, accounts, groups etc.
* View audit trail / log entries stored in a database.
* Read and search these documentation pages.
* Convert SSH Keys from and to OpenSSH, SSH.com, Putty, etc format.

..  note::
    When applying changes from Local Manager, there might be a delay of 0.5
    seconds until the changes are actually applied.

..  note::
    When removing a component which is already running,
    from within the Local Manager, it will stop automatically.


Indicating errors
-----------------

The Local Manager indicates the state of a service, transfer, authentication
method, event handler or resource.
If there are issues that have risen in an attempt to start these, the Local
Manager can also provide details.

See below for an example of an error arising from an invalid SSL Cipher List
configuration for a service.

Hovering over a `Failed at start` state can also show the administrator
further details of the issue to help troubleshoot the problem.

..  image:: /_static/operation/http-invalid-cipher-list.png


Reviewing changes made in Local Manager
---------------------------------------

Prior to applying changes, administrators have the option of reviewing their
changes.

..  image:: /_static/gallery/gallery-addsftp-review.png

----

Some of these changes will require restarting the affected, changed or updated
components.

..  image:: /_static/gallery/gallery-addsftp-req-restart.png


Supported Web Browsers
----------------------

The Local Manager is implemented as a modern web application and in order
to use it, you will need a modern web browser.
The following browsers are tested and supported by Local Manager:

* Internet Explorer 9 or newer
* Firefox 20 or newer
* Chrome (Chromium) 20 or newer
* Safari 6 or newer
* Opera 12 or newer

Minimum screen resolution requirement: 1024 x 768.


Restrictions of Local Manager
-----------------------------

For security reasons, you cannot restart the whole server from within the
Local Manager, but you can restart or reload separate services such as SFTP
or FTP services, including the Local Manager service itself.

For technical reasons, the following actions are not available from
within the Local Manager:

* Change protocol type for an existing service.
* Change account type for an existing account.
* Change the UUID for any entity (service, account, group, etc.)
* Disable or stop the main local manager service itself. This can only be done
  by manually editing the configuration file.

When stopping a service, the Local Manager only prevents the service from
accepting new connections.
Connections that are already established continue to function until they are
terminated in a normal way and active clients are not forced to disconnect.


Development mode
----------------

For performance reasons, the Local Manager service uses minimized CSS and JS
files and instructs the local browser to cache CSS, JS and other resource files.

In order to make it easier to investigate support issues or audit web
requests made by the Local Manager, we provide a `development mode`.

When running in `development mode`, the Local Manager will force the browser
to always reload CSS and JS files while using un-minimized CSS and JS files.

This mode might come in handy if you experience caching problems, or you want
to audit Local Manager code.

Also, **experimental** features are only visible in Local Manager when the
development mode is enabled.

To enable the development mode, access the Local Manager using the
following URL::

    https://host:port/#/enable-dev-mode

where `host` and `port` should match your configuration.

..  note::
    If you are already on the ``https://host:port`` page, amending the URL
    will not automatically reload the page.
    In this case, refresh the page after amending the URL to force the browser
    to process the request.

Enabling the development mode is triggered by a hidden control, but
disabling it is much easier.
After successfully logging in to the Local Manager, check the page footer.
You should see a link to disable the development mode.
Clicking the link will disable the development mode and will reload the page.

You can also disable the development mode by accessing the Local Manager using
the following URL.
Replace `host` and `port` with your configuration::

    https://host:port/#/disable-dev-mode
