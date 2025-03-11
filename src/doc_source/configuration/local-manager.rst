Web Manager console
===================

..  contents:: :local:


Introduction
------------

A web console is available for configuration and administration.
This service is available via the `local-manager` service.

The web console can be configured in a similar way to any other service provided by SFTPPlus.

This page describes configuring the Web Manager service. For information
about using the service, please see
(:doc:`the page on Web Manager operation </quick-start/local-manager>`).

The Web Manager service must be accessed over HTTPS and is enabled by
default on port ``10020`` of the local interface, thus being available only
for local connections, typically at ``https://127.0.0.1:10020``.

..  note::
    Since the HTTPS connection used by the Web Manager is secured using a
    self-signed SSL certificate; all web browsers will prompt to validate
    the server identity.

    You can configure the Web Manager to secure the HTTPS connection using
    a different SSL certificate, issued by a trusted
    certificate authority.

By default the Web Manager provides a dedicated administrator account
which is not tied to the operating system.
More administrator accounts can be created using the Web Manager or by
manually editing the configuration file, please see
(:doc:`the page on configuring administrators </configuration-identity/administrators>`).

..  note::
    The default account name is `admin` and the default password is `pass`.
    Details are in this dedicated section on
    :ref:`changing admin credentials <changing-admin-credentials>`.

..  warning::
    This default `admin` account is provided for testing and debugging purpose.
    For production usage, it is highly recommended to change the account
    name and password or to disable the account.

Besides allowing administrative access to the default application administrator
account, the default configuration also allows administrative access for all
users from the operating system's groups `Administrators` or `adm`, as these are
the default administrative groups for Windows or Unix-like operating systems.

The standard configuration file is pre-configured with a Web Manager
service having the `DEFAULT-MANAGER` UUID.
To prevent accidental removal, this service cannot be removed from the Local
Manager GUI.
You can still remove it by manually editing the configuration file.


Web Manager GUI vs text .ini configurations
-------------------------------------------

Everything that can be configured in the Web Manager GUI can also be
configured through the text file (`server.ini`).

A few of the features only available in the SFTPPlus Web Manager are
non-configuration related features, such as the visual status page or the
SSH / SSL management page.


Disable or stop the main Web Manager service
--------------------------------------------

SFTPPlus allows creating multiple instances of the Web Manager
service, as for any file transfer service.

To prevent accidentally deleting or disabling the main Web Manager service
with the `DEFAULT-MANAGER` UUID, these operations are restricted from the
Web Manager itself.

To disable the main Web Manager service, restart the server after amending
the configuration file to contain the following options::

    [services/DEFAULT-MANAGER]
    enabled = No

To re-enable the service, restart the server after amending
the configuration file as below::

    [services/DEFAULT-MANAGER]
    enabled = Yes

After authentication in the Web Manager, an administrator can
configure the Web Manager from within the web interface.

The rest of this page describes configuration options specific to the Local
Manager, as defined in the configuration file.

Web Manager is configured just like any other service provided by the
server, and configuration options are stored inside the
`configuration/server.ini` configuration file.

For general information about configuring a service, please see the
:doc:`services configuration page</configuration-server/index>`.

.. include:: /configuration-server/service-http.include.rst


base_url_path
-------------

:Default value: Empty
:Optional: Yes
:Values: * Absolute URL path
:From version: 4.30.0
:Description:
    When running behind a load balancer or a reverse proxy,
    you can configure your proxy to access an SFTPPlus HTTP/HTTPS service using a custom base URL.

    For example, with the default direct access, the SFTPPlus base URL is simply `/` (the root URL), and you access SFTPPlus as `https://localhost:10443/`

    When using a reverse proxy, you want to access SFTPPlus using a custom URL such as `https://localhost:10443/company/product/`.
    For this scenario, the configuration should be `base_url_path = /company/product`.

    Relative path values are not supported.
    This should be configured to an absolute path without trailing slashes.

    Leave it empty when SFTPPlus is not behind a load balancer or when the reverse proxy is mirroring the SFTPPlus path structure.

    ..  warning::
        When this value is configured, direct access outside of the load balancer or the reverse proxy is no longer supported.
        Once configured, the SFTPPlus manager console should only be accessed via the load balancer or proxy.


login_footnotes
---------------

:Default value: Empty
:Optional: Yes
:Values: * Text
:From version: 5.6.0
:Description:
    This configuration can be used to define a custom footnote with addition info on the login page.

    For example, it can be used to add a short "Terms of service" information.
