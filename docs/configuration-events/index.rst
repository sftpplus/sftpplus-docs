Event handlers
==============

Event handlers play a critical role in ensuring smooth, secure,
and efficient operations, not only for file transfers but also
for system monitoring and administrative tasks in SFTPPlus.

They allow SFTPPlus to respond to various events that occur during
file transfers, system operations, or administrative tasks.
These handlers can be configured to perform specific actions
automatically when certain events occur, such as file uploads,
downloads, or system changes.

Each handler can perform specific actions such as logging, sending
notifications, executing external programs, or interacting with other systems.


.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`globe` Introduction
        :link-type: doc
        :link: ./introduction

        Learn how to create and configure an event handler using the Web Manager or the configuration file.

    .. grid-item-card:: :octicon:`paper-airplane` Local file
        :link-type: doc
        :link: ./local-file

        Discover how to configure an event handler that will store the event information as local text files.

    .. grid-item-card:: :octicon:`file-directory` File dispatcher
        :link-type: doc
        :link: ./file-dispatcher

        Learn how to automate file routing and processing using the file dispatcher handler.

    .. grid-item-card:: :octicon:`lock` HTTP POST/Webhooks
        :link-type: doc
        :link: ./http

        Configure HTTP POST and webhook handlers to integrate with external HTTP systems and automate notifications.

    .. grid-item-card:: :octicon:`server` Email sender
        :link-type: doc
        :link: ./email-sender

        Set up email messages, with optional attached files,
        for event alerts and automated messaging.

    .. grid-item-card:: :octicon:`globe` Windows Event Log
        :link-type: doc
        :link: ./windows-eventlog

        Log SFTPPlus events directly to the Windows Event Log for centralized monitoring.

    .. grid-item-card:: :octicon:`paper-airplane` Standard output stream
        :link-type: doc
        :link: ./standard-stream

        Output event information to the standard output stream for integration with 3rd party tools like Docker or Kubernetes.

    .. grid-item-card:: :octicon:`file-directory` Embedded database
        :link-type: doc
        :link: ./database

        Store and manage event data using the embedded database handler.

    .. grid-item-card:: :octicon:`lock` Syslog
        :link-type: doc
        :link: ./syslog

        Forward event logs to a Syslog server for centralized logging and analysis.

    .. grid-item-card:: :octicon:`server` Create archive/compress
        :link-type: doc
        :link: ./create-archive

        Automatically compress files or create archives in response to events.

    .. grid-item-card:: :octicon:`paper-airplane` Extract archive/uncompress
        :link-type: doc
        :link: ./extract-archive

        Set up handlers to extract or uncompress files when specific events occur.

    .. grid-item-card:: :octicon:`file-directory` Execute external script or program
        :link-type: doc
        :link: ./external-executable

        Trigger custom scripts or external programs in response to SFTPPlus events.

    .. grid-item-card:: :octicon:`lock` Encrypt/decrypt with OpenPGP /GPG
        :link-type: doc
        :link: ./openpgp

        Configure handlers to encrypt or decrypt files using OpenPGP/GPG as part of your workflows.

    .. grid-item-card:: :octicon:`server` RabbitMQ publisher
        :link-type: doc
        :link: ./rabbitmq

        Publish event messages to RabbitMQ queues for integration with messaging systems.

    .. grid-item-card:: :octicon:`server` File content checker and digest generator
        :link-type: doc
        :link: ./content-check

        Check file content and generate file checksums or digests.

    .. grid-item-card:: :octicon:`paper-airplane` Account interaction
        :link-type: doc
        :link: ./account-interaction

        Learn how to use the event handler in order to detect when one account operates on files that are accessible to another account.

    .. grid-item-card:: :octicon:`file-directory` Extension API
        :link-type: doc
        :link: ./extension

        Extend SFTPPlus functionality by developing custom event handler extensions.


..  toctree::
    :maxdepth: 1
    :hidden:

    introduction
    local-file
    file-dispatcher
    http
    email-sender
    windows-eventlog
    standard-stream
    database
    syslog
    create-archive
    extract-archive
    external-executable
    openpgp
    rabbitmq
    content-check
    account-interaction
    extension
