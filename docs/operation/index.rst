Server Guides
=============

The instructions found in this section are targeted at system administrators or
application developers looking to use SFTPPlus' server-side capabilities
based on the available configuration and without the need to implement
custom components.

If you are looking to implement bespoken functionality, see the
:doc:`Developers documentation
</developer/index>`.

.. grid:: 1 1 2 1
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` Accounts authentication
        :link-type: doc
        :link: ./authentication

        Learn how password policies are implemented, about authenticating
        with Windows Domain accounts, anonymous authentication and other
        authentication settings.

    .. grid-item-card:: :octicon:`shield-check` Accounts authorization
        :link-type: doc
        :link: ./authorization

        Learn about the available permissions that can be applied to
        different files and folders.

    .. grid-item-card:: :octicon:`sliders` Identity and access management
        :link-type: doc
        :link: ./admin-authorization

        Discover the available permission targets defined through roles
        and how to associate them with administration accounts.

    .. grid-item-card:: :octicon:`sliders` Web Manager console
        :link-type: doc
        :link: ./admin-web-console

        Detailed guidance on configuring reverse proxy, integrating
        with API gateways, and securing Web Manager console access using examples
        such as NGINX and HAProxy.

    .. grid-item-card:: :octicon:`shield-check` Public Key Infrastructure (PKI)
        :link-type: doc
        :link: ./pki

        Learn about working with SSL certificates, PKI and CA, certificate chaining,
        and X509 certificate management.

    .. grid-item-card:: :octicon:`sliders` FTP/FTPS usage
        :link-type: doc
        :link: ./ftp

        Here you will find information about the server-side usage and behaviour
        of the FTP commands implemented by the FTP service/server.

    .. grid-item-card:: :octicon:`sliders` SFTP / SCP usage
        :link-type: doc
        :link: ./sftp

        This section contains information about using the SFTP / SCP
        file transfer service.

    .. grid-item-card:: :octicon:`paper-airplane` HTTP / HTTPS Service
        :link-type: doc
        :link: ./http

        This section contains information on the usage and behaviour
        of the HTTP and HTTPS file transfer services.

    .. grid-item-card:: :octicon:`sliders` Let's Encrypt Certificate Automation
        :link-type: doc
        :link: ./lets-encrypt

        Learn how to automate SSL certificate issuance and renewal using Let's Encrypt,
        including configuration steps and integration with SFTPPlus services.

    .. grid-item-card:: :octicon:`terminal` Command line administration
        :link-type: doc
        :link: ./command-line

        SFTPPlus can be administered also via a command line utility.
        In this section you'll find out how it can be used to generate passwords,
        SSH keys or self-signed certificates.

    .. grid-item-card:: :octicon:`sliders` File system access
        :link-type: doc
        :link: ./filesystem-access

        Learn how SFTPPlus handles native file system access on both Unix-like and Windows platforms for the server-side operations.

    .. grid-item-card:: :octicon:`workflow` Events, Event Handlers and the audit trail
        :link-type: doc
        :link: ../guides/event-handlers

        This section describes the logging and event handling capabilities of SFTPPlus.

    .. grid-item-card:: :octicon:`terminal` Command-Line Administration-Shell
        :link-type: doc
        :link: ./admin-shell

        Configuration and administrative tasks can be performed using the admin-shell.
        Learn about the available commands and how to use them.

..  toctree::
    :maxdepth: 1
    :hidden:

    authentication
    authorization
    admin-authorization
    admin-web-console
    pki
    ftp
    sftp
    http
    lets-encrypt
    command-line
    filesystem-access
    ../guides/event-handlers
    admin-shell
