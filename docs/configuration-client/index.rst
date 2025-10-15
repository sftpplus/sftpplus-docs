Client-side protocols
=====================


Introduction
------------

SFTPPlus supports a variety of client-side protocols to facilitate file
transfers and interactions with remote systems.

Locations are used to connect to various types of local or remote systems,
including local file systems, SFTP servers, FTP servers, HTTP servers,
and cloud storage services like Amazon S3 or Microsoft Azure Blob Storage.


Locations are auto-started when a transfer or another component needs them and
the location is not started and connected.

They are also fault-tolerant, allowing retries for interrupted connections.

Transfers using a failed location will also fail and will
not trigger a new connection attempt for the location.
In this type of scenario, the failed location must be manually started first,
after resolving the initial error.

SFTPPlus uses `locations` and :doc:`transfers </transfer/transfers>` to define how to connect to
remote systems and manage file transfers.
Locations specify the connection details for remote servers, while transfers
define the rules for file transfers between these locations.

The sub-sections below will guide you through the configuration of each
client-side protocol, including examples and best practices.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`sliders` SFTP
        :link-type: doc
        :link: ./sftp

        See the available configuration options for the SFTP location.

    .. grid-item-card:: :octicon:`sliders` FTP
        :link-type: doc
        :link: ./ftp

        Learn how to configure FTP for straightforward, legacy file transfers where encryption is not required.

    .. grid-item-card:: :octicon:`sliders` Explicit FTPS
        :link-type: doc
        :link: ./ftps-explicit

        This section provides details on how to configure the connection to an Explicit FTPS server.

    .. grid-item-card:: :octicon:`sliders` Implicit FTPS
        :link-type: doc
        :link: ./ftps-implicit

        This section provides details on how to configure the connection to an Implicit FTPS server.

    .. grid-item-card:: :octicon:`sliders` HTTP(S) file download
        :link-type: doc
        :link: ./http-pull

        This section provides details on how to configure the HTTP(S) pull location for downloading files from HTTP or HTTPS servers.

    .. grid-item-card:: :octicon:`sliders` SharePoint Online
        :link-type: doc
        :link: ./sharepoint-online

        Learn how to configure the SharePoint Online client protocols for accessing SharePoint sites hosted in the Azure Cloud.
        For on-premise SharePoint sites, use the `webdav` location.

    .. grid-item-card:: :octicon:`sliders` WebDAV / On-premise SharePoint
        :link-type: doc
        :link: ./webdav

        Learn how to configure the WebDAV and on-premise SharePoint client protocols for accessing remote files and folders.

    .. grid-item-card:: :octicon:`sliders` AS2
        :link-type: doc
        :link: ./as2

        Learn how to configure the AS2 client to send files to your AS2 trading partners.

    .. grid-item-card:: :octicon:`sliders` Azure BLOB Service
        :link-type: doc
        :link: ./azure-blob

        This section provides details on how to configure the Azure Blob location.

    .. grid-item-card:: :octicon:`sliders` Azure File Service
        :link-type: doc
        :link: ./azure-file

        This section provides details on how to configure the Azure File location.

    .. grid-item-card:: :octicon:`sliders` SMB/Windows Share
        :link-type: doc
        :link: ./smb

        Learn how to configure an SMB location to provide access to an SMB server over TCP.

    .. grid-item-card:: :octicon:`sliders` Oracle Database SQL
        :link-type: doc
        :link: ./oracle-database

        Learn how to configure an Oracle Database location to send and receive files using SQL statements, with data stored in the database.

    .. grid-item-card:: :octicon:`sliders` Exchange Online Mailbox
        :link-type: doc
        :link: ./exchange-online

        This section provides details on how to configure the Exchange Online location for downloading attached files in an Exchange Online mailbox.

    .. grid-item-card:: :octicon:`sliders` Send files as email attachments
        :link-type: doc
        :link: ./smtp

        This section provides details on how to send files as email attachments using the SMTP protocol.

    .. grid-item-card:: :octicon:`sliders` Local Filesystem
        :link-type: doc
        :link: ./local-filesystem

        See the available configuration options for the Local Filesystem location.


Adding a new location via Web Manager
-------------------------------------

A new location can be added or changed via Web Manager below.
Options will differ depending on which location type is used.

See below for an example of an initial configuration with the FTPES location.

..  image:: /static/gallery/gallery-add-ftps-location.png


Adding a new location via text configuration
--------------------------------------------

Adding a new location configuration is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``locations/`` and followed by
the location's UUID.

The location's UUID can be any unique string used to identify the location.
Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/introduction>`.

For example, to add a new location configuration of type `filesystem`
called ``Local file system``::

    [locations/b904e6h6-c295-4ccf-8abd-edcae4d3324f]
    name = Local file system
    description = File system accesses as service account.
    type = filesystem


..  toctree::
    :maxdepth: 1
    :hidden:

    sftp
    ftp
    ftps-explicit
    ftps-implicit
    http-pull
    webdav
    as2
    azure-blob
    azure-file
    smb
    exchange-online
    sharepoint-online
    oracle-database
    smtp
    local-filesystem
