.. container:: tags pull-left

    `client-side`
    `security`
    `since-version:3.20.0`


Using WebDAV
============

..  contents:: :local:


About this Guide
----------------

We created this Users Guide as the starting resource for those interested in
using SFTPPlus for file transfers involving WebDAV over HTTPS.

For new users, the SFTPPlus client-side implementation now supports WebDAV over
HTTPS.
To get started, contact us to obtain the latest release of SFTPPlus,
follow the :doc:`getting started guide </quick-start/getting-started>`
and read the :doc:`client-shell </operation-client/client-shell>`
documentation to gain an idea of the client-side implementation.

The product roadmap will include further support for more WebDAV features.

Please see the :doc:`WebDAV operations </operation/http>` page for the current
features in detail.

If there is a particular scenario or guide that is not addressed here, please
feel free to contact us.


Connecting via the client-shell
-------------------------------

WebDAV over HTTPS is currently only available on the client-side implementation
of SFTPPlus.

To connect to the Sharepoint server in the `client-shell` with your
credentials.

    | $ client-shell webdavs://user@acme.onmicrosoft.com@acme.sharepoint.com -p
      'password'
       > connect

After connecting, you are able to execute some of the commands available in
the :doc:`Command-Line Client-Shell page </operation-client/client-shell>`.

Please note that not all `client-shell` commands are supported in `webdav`.


Connecting with locations under proxy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A WebDAV :doc:`resource </configuration/resources>` location under a proxy is
supported.

Add the proxy details either in the `webdavs` location's configuration in the
Local Manager or in the text configuration file::

    [locations/b9787c72-2c8b-4725-a049-ee628aa0abc1]
    name = webdavs
    proxy = connect://localhost:8899

To ensure that the connection is not refused by the other side, the proxy
configuration should match your network's correct proxy configuration.

To connect in the `client-shell`, please append after your Sharepoint
credentials::

    --proxy=connect://address:port


Troubleshooting audit events
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SFTPPlus audit events will provide details in regards to WebDAV
transfer failures.

In most cases, the details are brief as this is what is advertised by the
remote server.
To obtain more details, you will need to contact the team/person in charge of
the remote team and ask for the server-side activity/logs.

As you can observe in the example below,
only the error or status code is provided by the server,
which shows the ``409:CONFLICT`` status code::

    | 60036 2017-05-29 17:45:07 Process Process 0.0.0.0:0 Failed to close
      "/ACME/Documents/report.doc" on location "webdavs". Was opened for
      writing. Failed to upload. (/ACME/Documents/report.doc) 409:CONFLICT


Example of a transfer configuration
-----------------------------------

To get you started using the SFTPPlus
:doc:`transfers </configuration/transfers>` functionality, we have included
example transfer configurations using WebDAV as the location.
The SFTPPlus Local Manager can be used to configure transfers, but there is
a text :doc:`configuration </configuration/configuration-file>` file available.
The examples below can be added in the configuration file or modified in the
Local Manager.

The example below will create a new ``webdavs`` location using the Sharepoint
Online credentials at the specified Sharepoint Online address and port::

    [locations/b9787c72-2c8b-4725-a049-ee628aa0abc1]
    name = webdavs-acme-location
    description = Location for the Sharepoint Online server.
    type = webdavs
    address = acme.sharepoint.com
    port = 443
    username = user@acme.onmicrosoft.com
    password = password
    authentication_method = sharepoint-online
    connection_retry_count = 0
    connection_retry_interval = 30

The example below will set up an automatic transfer to move files from a local
disk as indicated by the `source_path` to a remote SharePoint online folder
as indicated by the `destination_path`.
This example references the previously created location UUID from the above
example, called ``webdavs-acme-location``::

    [transfers/e16af067-8974-4c0d-ae89-eb5f3d59fd65]
    enabled = yes
    name = webdavs-move-non-recursive
    recursive = No
    source_uuid =
    source_path = ./acme/webdav-transfers/shared
    destination_uuid = webdavs-acme-location
    destination_path = /acme-webdav/Shared/HR-Department
    stable_interval = 0.5
    changes_poll_interval = 5

For further details about the rest of the transfer configuration options
available in SFTPPlus, please go to the dedicated
:doc:`Transfers page </configuration/transfers>`.


Securing connection to SharePoint Online
----------------------------------------

SFTPPlus will not automatically trust the certificates presented by any HTTPS
server and this includes the SharePoint server.

You need to manually instruct SFTPPlus to validate the certificates against a
list of certificate authorities (CA) which you trust.

The CDP X.509 extension is not yet supported for HTTPS client-side connections
so if you want to use CRL, you need to manually configure them.

Here is a sample configuration for SharePoint online::

    [locations/0ef580fe-45cb-47e0-b434-c0e44557b364]
    ssl_certificate_authority = ${MICROSOFT_IT_CA}
    ssl_certificate_revocation_list = ${MICROSOFT_IT_CRL}
