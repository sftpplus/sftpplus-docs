Client-side protocols
=====================

SFTPPlus supports a variety of client-side protocols to facilitate file
transfers and interactions with remote systems.

These protocols include SFTP, FTP, FTPS (both explicit and implicit),
HTTP pull, WebDAV, AS2, Azure Blob Storage, Azure File Storage,
SMB, Exchange Online, and SMTP.

SFTPPlus uses ``locations`` and ``transfers`` to define how to connect to
remote systems and manage file transfers.
Locations specify the connection details for remote servers, while transfers
define the rules for file transfers between these locations.

The sub-sections below will guide you through the configuration of each
client-side protocol, including examples and best practices.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` Locations
        :link-type: doc
        :link: ./locations

        Learn how to create and configure locations for connecting to remote systems using SFTPPlus.

    .. grid-item-card:: :octicon:`book` Transfers
        :link-type: doc
        :link: ./transfers

        Learn about file transfers and configuration options available.

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


..  toctree::
    :maxdepth: 1
    :hidden:

    locations
    transfers
    local-filesystem
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
    smtp
