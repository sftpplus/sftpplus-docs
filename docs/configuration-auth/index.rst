Users, accounts, groups, auth & policies
========================================

Accounts represent the users that are managed by SFTPPlus and are available to authenticate for file transfers.
This differentiate them from Active Directory users, LDAP users, or operating system users, which are managed by external systems and are not created or managed by SFTPPlus.
Both SFTPPlus accounts and externally authenticated users can be used to authenticate for file transfers.

Multiple accounts can be associated with a group, which allows for easier management of permissions and access control.

An authentication method configuration provides the required information to allow SFTPPlus to use a specific method in order to authenticate file transfer users and administrators.

..  note::
    Not all authentication method types support authenticating the
    administrators for the Web Manager service.


The sections below will guide you through the available authentication methods
and how to configure them.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` Introduction
        :link-type: doc
        :link: ./introduction

        This section shows you how to create a new authentication method using the Web Manager console or the configuration file.

    .. grid-item-card:: :octicon:`book` Security policies
        :link-type: doc
        :link: ./security-policy

        Enforce password security, prevent brute-force attacks and restrict or allow access based on source IP address using security policies.

    .. grid-item-card:: :octicon:`book` User authentication
        :link-type: doc
        :link: ./authentication

        Learn about password policies, authentication with Windows Domain users,
        and other authentication settings.

    .. grid-item-card:: :octicon:`shield-check` User authorization
        :link-type: doc
        :link: ./authorization

        Learn how account authorization controls access after authentication.

    .. grid-item-card:: :octicon:`shield-check` Path permissions
        :link-type: doc
        :link: ./path-permissions

        Configure server-side file permissions, path rules, and group inheritance for all file transfer protocols.

    .. grid-item-card:: :octicon:`book` Accounts configuration
        :link-type: doc
        :link: ./accounts

        Learn about the differences between application accounts and operating system accounts and the configuration options available for each.

    .. grid-item-card:: :octicon:`book` Groups
        :link-type: doc
        :link: ./groups

        Learn about the Default Group and how to add and manage new groups in SFTPPlus.

    .. grid-item-card:: :octicon:`book` Password updates and recovery
        :link-type: doc
        :link: ./password-update

        Learn how password changes differ from email password recovery and how to configure both options.

    .. grid-item-card:: :octicon:`sliders` SFTPPlus embedded authentication
        :link-type: doc
        :link: ./application

        An application authentication method can be used to authenticate users based on the accounts defined in the SFTPPlus main configuration.

    .. grid-item-card:: :octicon:`sliders` Operating system / Domain users
        :link-type: doc
        :link: ./os

        Authenticating OS users is possible in SFTPPlus using the `os` authentication method.
        This section covers how to configure it and the available options.

    .. grid-item-card:: :octicon:`sliders` HTTP web service
        :link-type: doc
        :link: ./http

        A remote HTTP web service can be used to authenticate users in SFTPPlus.
        This section covers how to configure the HTTP authentication method and the available options.

    .. grid-item-card:: :octicon:`sliders` External local file
        :link-type: doc
        :link: ./local-file

        The local file authentication method allows SFTPPlus to authenticate users defined in a separate configuration file.
        This section covers the available options for it.

    .. grid-item-card:: :octicon:`sliders` LDAP configuration
        :link-type: doc
        :link: ./ldap

        The LDAP authentication method allows SFTPPlus to authenticate users against an LDAP or Active Directory server.
        This section covers the available configuration options.

    .. grid-item-card:: :octicon:`book` LDAP / Active Directory integration
        :link-type: doc
        :link: ./ldap-integration

        This section provides information about configuring SFTPPlus to use
        LDAP for users and administrator authentication in various use cases.

    .. grid-item-card:: :octicon:`sliders` Microsoft Entra ID
        :link-type: doc
        :link: ./entra-id

        The Entra ID authentication method allows SFTPPlus to authenticate users against Microsoft Entra ID (formerly Azure Active Directory).
        This section covers the available configuration options and how to set it up.

    .. grid-item-card:: :octicon:`sliders` Google Identity
        :link-type: doc
        :link: ./google-identity

        The `google-identity` method is used to implement single sign-on authentication using the Google Identity service,
        allowing Google Workspace users to authenticate in SFTPPlus as administrator or file transfer users.

    .. grid-item-card:: :octicon:`sliders` Okta OpenID Connect
        :link-type: doc
        :link: ./okta-oidc

        The `okta-oidc` method is used to implement single sign-on authentication using the Okta OpenID Connect service,
        allowing Okta users to authenticate in SFTPPlus as administrators or file transfer users.

    .. grid-item-card:: :octicon:`sliders` RADIUS
        :link-type: doc
        :link: ./radius

        The radius authentication method can be used to authenticate application type users by delegating the authentication to a remote RADIUS UDP server.


..  toctree::
    :hidden:
    :maxdepth: 1

    introduction
    security-policy
    authentication
    authorization
    path-permissions
    accounts
    groups
    password-update
    application
    os
    http
    local-file
    ldap
    ldap-integration
    entra-id
    google-identity
    okta-oidc
    radius
