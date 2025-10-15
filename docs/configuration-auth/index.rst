Authentication, users and admins
================================

An authentication method configuration provides the required information to
allow SFTPPlus to use a specific method in order to authenticate
file transfer accounts and administration account.


..  note::
    Not all authentication method types support authenticating the
    administrators for the Web Manager service.

The identity configuration defines the users, groups, administrators and
roles created as part of the SFTPPlus application.

For these users and administrators the full life-cycle is managed by SFTPPlus.

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

    .. grid-item-card:: :octicon:`book` Accounts
        :link-type: doc
        :link: ./accounts

        Learn about the differences between application accounts and operating system accounts and the configuration options available for each.

    .. grid-item-card:: :octicon:`book` Groups
        :link-type: doc
        :link: ./groups

        Learn about the Default Group and how to add and manage new groups in SFTPPlus.

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

    .. grid-item-card:: :octicon:`sliders` SFTPPlus embedded users
        :link-type: doc
        :link: ./application

        An application authentication method can be used to authenticate users based on accounts defined in the configuration file of SFTPPlus.

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

    .. grid-item-card:: :octicon:`sliders` LDAP / Active Directory
        :link-type: doc
        :link: ./ldap

        The LDAP authentication method allows SFTPPlus to authenticate users against an LDAP or Active Directory server.
        This section covers its limitations and available configuration options.


    .. grid-item-card:: :octicon:`sliders` Microsoft Entra ID
        :link-type: doc
        :link: ./entra-id

        The Entra ID authentication method allows SFTPPlus to authenticate users against Microsoft Entra ID (formerly Azure Active Directory).
        This section covers the available configuration options and how to set it up.

    .. grid-item-card:: :octicon:`sliders` Google Identity
        :link-type: doc
        :link: ./google-identity

        The `google-identity` method is used to implement single sign-on authentication using the Google Identity service,
        allowing Google Workspace accounts to authenticate in SFTPPlus as administrator or file transfer accounts.

    .. grid-item-card:: :octicon:`sliders` Okta OpenID Connect
        :link-type: doc
        :link: ./okta-oidc

        The `okta-oidc` method is used to implement single sign-on authentication using the Okta OpenID Connect service,
        allowing Okta accounts to authenticate in SFTPPlus as administrators or file transfer accounts.

    .. grid-item-card:: :octicon:`sliders` RADIUS
        :link-type: doc
        :link: ./radius

        The radius authentication method can be used to authenticate application type accounts by delegating the authentication to a remote RADIUS UDP server.

    .. grid-item-card:: :octicon:`sliders` Banning users (DEPRECATED)
        :link-type: doc
        :link: ./deny-username

        This is provided for backward compatibility.
        Use the **security policies** to restrict access based on username.
        This authentication method can be used to block/deny authentication for a configured list of users or administrators.

    .. grid-item-card:: :octicon:`sliders` Banning IP addresses (DEPRECATED)
        :link-type: doc
        :link: ./ip-time-ban

        This is provided for backward compatibility.
        Use the **security policies** to restrict access based on source IP.
        This authentication method can be used to block/deny authentication requests coming from a specific IP address helping to mitigate DDOS attempts to SFTPPlus services.

    .. grid-item-card:: :octicon:`sliders` Anonymous authentication (LEGACY)
        :link-type: doc
        :link: ./anonymous

        This is provided for legacy FTP compatibility.
        This method can be used to authenticate a specific *application* account by ignoring the provided password or any other credential.


..  toctree::
    :hidden:
    :maxdepth: 1

    introduction
    accounts
    groups
    administrators
    roles
    application
    os
    http
    local-file
    ldap
    entra-id
    google-identity
    okta-oidc
    radius
    deny-username
    ip-time-ban
    anonymous
