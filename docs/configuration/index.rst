General Configuration
=====================

SFTPPlus offers a wide range of configuration options to tailor both client-side and server-side transfers to your specific needs.

You can configure SFTPPlus using either a configuration file or a web-based interface.

The configuration file provides a direct and scriptable way to manage all settings,
offering fine-grained control and versioning capabilities.
This method is ideal for automated deployments and advanced users who prefer a text-based approach.
The documentation for the configuration file is comprehensive, covering all available options and their usage.

The web-based interface offers a user-friendly environment for configuring SFTPPlus.
It provides an intuitive way to manage settings, monitor performance, and perform administrative tasks.
This method is suitable for users who prefer a visual interface and require real-time monitoring.

The sub-sections below will guide you through the initial server setup, including configuring essential settings, managing resources, and understanding available options.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` SFTPPlus Configuration Overview
        :link-type: doc
        :link: ./introduction

        Understand the main concepts and approaches for configuring SFTPPlus.

    .. grid-item-card:: :octicon:`book` Terminology
        :link-type: doc
        :link: ./terminology

        Get familiar with the key terms and concepts used in SFTPPlus.

    .. grid-item-card:: :octicon:`file-code` Configuration file
        :link-type: doc
        :link: ./configuration-file

        Discover how to configure SFTPPlus using the configuration file,
        including syntax and structure.

    .. grid-item-card:: :octicon:`browser` Web Manager console
        :link-type: doc
        :link: ./local-manager

        Learn how to use and configure the Web Manager console.

    .. grid-item-card:: :octicon:`book` General configuration
        :link-type: doc
        :link: ./server

        Learn about the general server configuration and options affecting all file transfer services

    .. grid-item-card:: :octicon:`book` Matching expressions
        :link-type: doc
        :link: ./matching-expression

        Discover how regular expressions and globbing can be used to match files and directories in SFTPPlus.

    .. grid-item-card:: :octicon:`book` Resources
        :link-type: doc
        :link: ./resources

        Discover the available resources in SFTPPlus and how to configure them.

    .. grid-item-card:: :octicon:`sliders` Local File System monitor
        :link-type: doc
        :link: ./monitor-resource

        Learn how to setup a monitored path in the local file system and available configuration options.

    .. grid-item-card:: :octicon:`sliders` Email client
        :link-type: doc
        :link: ./email-client

        Learn about the email client resource and the available configuration options.

    .. grid-item-card:: :octicon:`sliders` Analytics and alerts
        :link-type: doc
        :link: ./analytics

        SFTPPlus allows setting up different alarms based on user-defined criteria,
        and provides a way to monitor the server's performance.

    .. grid-item-card:: :octicon:`sliders` Let's Encrypt client / CertBot
        :link-type: doc
        :link: ./lets-encrypt

        The Let's Encrypt resource allows SFTPPlus to automatically request SSL / X.509 certificates from Let's Encrypt's Certificate Authority.
        This covers the available configuration options.

    .. grid-item-card:: :octicon:`database` SQLite database
        :link-type: doc
        :link: ./sqlite

        Learn about the SQLite database resource and how to configure it.


..  toctree::
    :maxdepth: 1
    :hidden:

    introduction
    terminology
    configuration-file
    local-manager
    server
    security-policy
    matching-expression
    resources
    monitor-resource
    email-client
    analytics
    lets-encrypt
    sqlite
