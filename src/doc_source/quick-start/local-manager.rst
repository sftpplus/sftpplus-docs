Web Manager
===========

..  contents:: :local:


Introduction
------------

The Web Manager is an embedded service for handling the configuration of SFTPPlus.
It looks and behaves like a regular web application and works with any modern web browser.

The configuration options are detailed in the
:doc:`Web Manager Configuration </configuration/local-manager>` page.

----

Below is a screenshot of the Web Manager authentication page, notice
that it is only available over **HTTPS**:

..  image:: /_static/operation/local-manager-login.png

----

Web Manager comes with a default administration account with username
`admin` and a password set during the configuration initialization.

While using the Web Manager graphical user interface, you have
access to integrated documentation, assistance, and validation which will
guide you through the configuration process.

The following actions are available from within the Web Manager:

* View current server configuration.
* Perform generic server configuration.
* Configure logging services.
* Configure the Web Manager itself.
* Add / remove / configure file transfer services with
  all supported protocols.
* Add / remove / configure local manager services.
* Add / remove / modify administrators, roles, accounts, groups etc.
* View audit trail / log entries stored in a database.
* Read and search these documentation pages.
* Convert SSH Keys from and to OpenSSH, SSH.com, Putty, etc format.

..  note::
    When applying changes from Web Manager, there might be a delay of 0.5
    seconds until the changes are actually applied.

..  note::
    When removing a component which is already running,
    from within the Web Manager, it will stop automatically.


Indicating errors
-----------------

The Web Manager indicates the state of a service, transfer, authentication
method, event handler or resource.
If there are issues that have risen in an attempt to start these, the Local
Manager can also provide details.

See below for an example of an error arising from an invalid SSL Cipher List
configuration for a service.

Hovering over a `Failed at start` state can also show the administrator
further details of the issue to help troubleshoot the problem.

..  image:: /_static/operation/http-invalid-cipher-list.png


Reviewing changes made in Web Manager
-------------------------------------

Prior to applying changes, administrators have the option of reviewing their
changes.

..  image:: /_static/gallery/gallery-addsftp-review.png

----

Some of these changes will require restarting the affected, changed or updated
components.

..  image:: /_static/gallery/gallery-addsftp-req-restart.png


Supported Web Browsers
----------------------

The Web Manager is implemented as a modern web application and in order
to use it, you will need a modern web browser.
The following browsers are tested and supported by Web Manager:

* Internet Explorer 9 or newer
* Firefox 20 or newer
* Chrome (Chromium) 20 or newer
* Safari 6 or newer
* Opera 12 or newer

Minimum screen resolution requirement: 1024 x 768.


Restrictions of Web Manager
---------------------------

For security reasons, you cannot restart the whole server from within the
Web Manager, but you can restart or reload separate services such as SFTP
or FTP services, including the Web Manager service itself.

For technical reasons, the following actions are not available from
within the Web Manager:

* Change protocol type for an existing service.
* Change account type for an existing account.
* Change the UUID for any entity (service, account, group, etc.)
* Disable or stop the main local manager service itself. This can only be done
  by manually editing the configuration file.

When stopping a service, the Web Manager only prevents the service from
accepting new connections.
Connections that are already established continue to function until they are
terminated in a normal way and active clients are not forced to disconnect.
