Administration, admins and roles
================================

The instructions found in this section are targeted at system administrators or
application developers looking to integrate SFTPPlus deployments with DevOps practices.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`sliders` Web manager console
        :link-type: doc
        :link: ./admin-web-console

        Detailed guidance on configuring reverse proxy, integrating
        with API gateways, and securing Web manager console access using examples
        such as NGINX and HAProxy.

    .. grid-item-card:: :octicon:`sliders` Identity and access management
        :link-type: doc
        :link: ./admin-authorization

        Discover the available permission targets defined through roles
        and how to associate them with administration accounts.

    .. grid-item-card:: :octicon:`book` Administrators
        :link-type: doc
        :link: ./administrators

        Administrators are users that can manage the SFTPPlus server and its configuration using the Web Manager console.
        This section covers how to create and manage administrators.

    .. grid-item-card:: :octicon:`book` Roles
        :link-type: doc
        :link: ./roles

        Roles are used to define permissions for administrators.
        Learn how to create a new role and the available configuration options.

    .. grid-item-card:: :octicon:`terminal` Log management
        :link-type: doc
        :link: ./log-management

        In this section you will learn about managing logs in SFTPPlus,
        including log rotation and retention.

    .. grid-item-card:: :octicon:`shield-check` Public Key Infrastructure (PKI)
        :link-type: doc
        :link: ./pki

        Learn about working with SSL certificates, PKI and CA, certificate chaining,
        and X509 certificate management.


    .. grid-item-card:: :octicon:`shield-check` Vault administration
        :link-type: doc
        :link: ./vault

        Learn about managing sensitive information using the `vault` resource and `vault-items`.

    .. grid-item-card:: :octicon:`workflow` Events, event handlers and the audit trail
        :link-type: doc
        :link: ./event-handlers

        Events and event group represent the way SFTPPlus logs the operations.
        Event Handlers allow you to implement custom file management processes.
        Use Activity Log and Account Activity to view and filter logs.

    .. grid-item-card:: :octicon:`terminal` Command line administration
        :link-type: doc
        :link: ./command-line

        SFTPPlus can be administered also via a command line utility.
        In this section you'll find out how it can be used to generate passwords,
        SSH keys or self-signed certificates.

    .. grid-item-card:: :octicon:`terminal` Administration shell
        :link-type: doc
        :link: ./admin-shell

        Configuration and administrative tasks can be performed using the command line `admin-shell`.
        Learn about the available commands and how to use them.

    .. grid-item-card:: :octicon:`book` Hardening SFTPPlus Deployments
        :link-type: doc
        :link: ./hardening

        Find out about best practices for hardening SFTPPlus deployments,
        including recommended configuration options, security controls,
        and operational guidelines to minimize risks and improve the
        overall security posture of your SFTPPlus environment.


..  toctree::
    :maxdepth: 1
    :hidden:

    admin-web-console
    admin-authorization
    administrators
    roles
    log-management
    pki
    vault
    command-line
    event-handlers
    admin-shell
    hardening
