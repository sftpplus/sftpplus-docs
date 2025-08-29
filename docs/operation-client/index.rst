Client Guides
=============

The instructions found in this section are targeted to system administrators
or application developers looking to use the client-side capabilities
of the SFTPPlus solely based on the available configuration.

The sub-sections below will guide you through the operation of each
client-side protocol, including examples and best practices.

.. grid:: 1 1 2 1
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` Client-Side Transfers Operations
        :link-type: doc
        :link: ./transfers

        This vast sub-section will guide you through SFTPPlus transfers,
        from their implementation, and capabilities to the configuration settings available for each transfer type.

    .. grid-item-card:: :octicon:`book` Transfers scheduling
        :link-type: doc
        :link: ./transfer-scheduling

        A transfer can be configured to be active all the time or be
        active based on a simple scheduler.

    .. grid-item-card:: :octicon:`terminal` Command-Line Client-Shell
        :link-type: doc
        :link: ./client-shell

        A command-line shell is provided to access remote file transfer servers
        using an interactive interface. Learn how to upload, download,
        and manage file transfers using this shell.

    .. grid-item-card:: :octicon:`stack` File system access
        :link-type: doc
        :link: ./filesystem-access

        Learn how SFTPPlus handles native file system access
        on both Unix-like and Windows platforms for the client-side operations.

    .. grid-item-card:: :octicon:`stack` FTP/FTPS Client Side Operation Mode
        :link-type: doc
        :link: ./ftp

        This section contains information about the usage and behaviour of the
        FTP commands implemented by the FTP location/client.

    .. grid-item-card:: :octicon:`stack` HTTP / HTTPS Client Operations
        :link-type: doc
        :link: ./http

        SFTPPlus can act as an HTTP/HTTPS client in both server-side related
        operation as well as client-side transfers ones. In this section you
        will learn about the HTTP/HTTPS client operations.

    .. grid-item-card:: :octicon:`stack` Send files over AS2
        :link-type: doc
        :link: ./as2-send

        Learn how to send files over AS2 using SFTPPlus, including
        configuration options and best practices.

    .. grid-item-card:: :octicon:`stack` SharePoint Online Sites
        :link-type: doc
        :link: ./sharepoint-online

        Learn how to configure Entra ID and SharePoint Online to allow
        SFTPPlus to manage files from SharePoint Online sites.


    .. grid-item-card:: :octicon:`stack` Exchange Online attachments
        :link-type: doc
        :link: ./exchange-online

        Learn how to configure Entra ID and Exchange Online to allow
        SFTPPlus to read or write emails.


..  toctree::
    :maxdepth: 1
    :hidden:

    transfers
    transfer-scheduling
    client-shell
    filesystem-access
    ftp
    http
    as2-send
    exchange-online
    sharepoint-online
