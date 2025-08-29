User's Guides
=============

This section includes various stand-alone articles which document the
server and client side functionalities, and contain specific usage examples.

.. grid:: 1 1 2 1
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` TLS Client Configuration
        :link-type: doc
        :link: ./tls-client

        This section explains how to configure TLS clients for connecting
        to SFTPPlus servers.

    .. grid-item-card:: :octicon:`book` SSL / TLS / SSH protocols overview
        :link-type: doc
        :link: ./security

        Learn about SSL/TLS/SSH protocols and their usage in SFTPPlus.

    .. grid-item-card:: :octicon:`book` Hardening SFTPPlus Deployments
        :link-type: doc
        :link: ./hardening

        Find out about best practices for hardening SFTPPlus deployments,
        including recommended configuration options, security controls,
        and operational guidelines to minimize risks and improve the
        overall security posture of your SFTPPlus environment.

    .. grid-item-card:: :octicon:`key` Resetting Web Manager username and password
        :link-type: doc
        :link: ./admin-reset

        Learn how to reset the Web Manager username and password, including the
        steps required to regain access if you have lost or forgotten your credentials.
        This guide provides detailed instructions for safely resetting the username
        and password for the SFTPPlus Web Manager.

    .. grid-item-card:: :octicon:`shield-lock` Auditing the encryption used for FTPS,
        SFTP, SCP and HTTPS connections
        :link-type: doc
        :link: ./connection-security-audit

        This section provides information how you can audit the encryption
        used for the client and server side connection protected using TLS and SSH.

    .. grid-item-card:: :octicon:`file-directory` File Dispatcher Event Handler
        :link-type: doc
        :link: ./file-dispatcher

        This section explains how to use the File Dispatcher event handler
        to automate actions on files managed by SFTPPlus.

    .. grid-item-card:: :octicon:`book` Docker Deployment
        :link-type: doc
        :link: ./docker

        SFTPPlus can be deployed as a Docker container. Learn more about the
        deployment process and best practices in this section.

    .. grid-item-card:: :octicon:`key` Generating and converting SSH keys
        :link-type: doc
        :link: ./ssh-keys

        This section provides information about generating and converting SSH keys
        for use with SFTPPlus.

    .. grid-item-card:: :octicon:`key` Using PGP/GPG encryption and decryption
        :link-type: doc
        :link: ./gpg-usage

        Learn about symmetrical and asymmetrical encryption methods using GPG and how to generate key pairs using the Web Console.

    .. grid-item-card:: :octicon:`shield-lock` Interoperability with anti-viruses
        :link-type: doc
        :link: ./antivirus

        This section provides information about integrating SFTPPlus with antivirus software to scan files during transfers.

    .. grid-item-card:: :octicon:`mail` Sending notification/alerts over emails
        :link-type: doc
        :link: ./email-notifications

        SFTPPlus can be configured to send email notifications for various events,
        in this section you will find all the information about this topic.

    .. grid-item-card:: :octicon:`workflow` Events, Event Handlers and the audit trail
        :link-type: doc
        :link: ./event-handlers

        Events and event group represent the way SFTPPlus logs the operations.
        Event Handlers allow you to implement custom file management processes.
        Use Activity Log and Account Activity to view and filter logs.

    .. grid-item-card:: :octicon:`terminal` Log management
        :link-type: doc
        :link: ./log-management

        In this section you will learn about managing logs in SFTPPlus,
        including log rotation and retention.

    .. grid-item-card:: :octicon:`browser` Using WebDAV and SharePoint
        :link-type: doc
        :link: ./webdav

        More indepth information about using WebDAV and SharePoint with SFTPPlus.

    .. grid-item-card:: :octicon:`git-branch` Group inheritance for permissions
        :link-type: doc
        :link: ./group-inheritance

        This section provides information about the group inheritance feature in
        SFTPPlus, which allows for easier management of user permissions.

    .. grid-item-card:: :octicon:`book` Integrating with an LDAP Server
        :link-type: doc
        :link: ./ldap

        This section provides information about configuring SFTPPlus to use
        LDAP for user authentication.

    .. grid-item-card:: :octicon:`server` Integrating with fault tolerant
        and resilient environments
        :link-type: doc
        :link: ./fault-tolerant-environment

        This section provides information about integrating SFTPPlus
        with external tools in order to meet the requirements for a fault tolerant
        infrastructure.

    .. grid-item-card:: :octicon:`file-code` WinSCP and SFTPPlus integration
        :link-type: doc
        :link: ./winscp-sftpplus-guide

        This section provides information about using WinSCP with SFTPPlus,
        including how to configure WinSCP to connect to SFTPPlus servers.

    .. grid-item-card:: :octicon:`file-code` FileZilla and SFTPPlus integration
        :link-type: doc
        :link: ./filezilla-sftpplus-server

        SFTPPlus server can interact with an array of 3-rd party clients,
        like FileZilla Client. Here is a quick user guide about how to
        use FileZilla with SFTPPlus server.

    .. grid-item-card:: :octicon:`terminal` Testing and Debugging
        :link-type: doc
        :link: ./testing

        SFTPPlus can be configured to run in debug mode, allowing
        for more detailed logging and easier troubleshooting.


..  toctree::
    :maxdepth: 1
    :hidden:

    tls-client
    security
    hardening
    admin-reset
    connection-security-audit
    file-dispatcher
    docker
    ssh-keys
    gpg-usage
    antivirus
    email-notifications
    event-handlers
    log-management
    webdav
    group-inheritance
    ldap
    fault-tolerant-environment
    winscp-sftpplus-guide
    filezilla-sftpplus-server
    testing
