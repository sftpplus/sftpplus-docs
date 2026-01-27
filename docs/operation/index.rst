Server guides
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

    .. grid-item-card:: :octicon:`shield-lock` Server-side TLS configuration
        :link-type: doc
        :link: ./server-side-tls

        In this section you will find more details about the TLS and mutual TLS
        server-side configuration options available in SFTPPlus.
        This includes information about configuring certificates,
        TLS versions, mutual TLS, and cipher suites, for protocols such as FTPS or HTTPS.

    .. grid-item-card:: :octicon:`sliders` Let's Encrypt Certificate Automation
        :link-type: doc
        :link: ./lets-encrypt

        Learn how to automate SSL certificate issuance and renewal using Let's Encrypt,
        including configuration steps and integration with SFTPPlus services.

    .. grid-item-card:: :octicon:`sliders` File system access
        :link-type: doc
        :link: ./filesystem-access

        Learn how SFTPPlus handles native file system access on both Unix-like and Windows platforms for the server-side operations.

    .. grid-item-card:: :octicon:`book` LDAP integration
        :link-type: doc
        :link: ./ldap

        This section provides information about configuring SFTPPlus to use
        LDAP for users and administrator authentication in various use cases.

..  toctree::
    :maxdepth: 1
    :hidden:

    authentication
    authorization
    ftp
    sftp
    http
    server-side-tls
    lets-encrypt
    filesystem-access
    ldap
