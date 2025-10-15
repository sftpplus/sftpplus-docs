Client-side transfers
=====================

SFTPPlus supports a variety of client-side transfers to facilitate file
transfers and interactions with remote systems.

SFTPPlus uses ``locations`` to configure the remote systems and ``transfers`` to define how to connect to remote systems and manage file transfers.
Locations specify the connection details for remote servers, while transfers
define the rules for file transfers between these locations.

The sub-sections below will guide you through the available configuration options for setting up a client-side transfer, including examples and best practices.

Check the separate
:doc:`locations reference documentation </configuration-client/index>`,
which describes the configuration options for all the available transfer protocols.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` Transfer Configuration
        :link-type: doc
        :link: ./transfers

        Learn about file transfers and configuration options available.

    .. grid-item-card:: :octicon:`book` Transfers Operations
        :link-type: doc
        :link: ./operation

        This vast sub-section will guide you through SFTPPlus transfers,
        from their implementation, and capabilities to the configuration settings available for each transfer type.

    .. grid-item-card:: :octicon:`book` Transfers scheduling
        :link-type: doc
        :link: ./transfer-scheduling

        A transfer can be configured to be active all the time or be
        active based on a simple scheduler.


    .. grid-item-card:: :octicon:`stack` File system access
        :link-type: doc
        :link: ./filesystem-access

        Learn how SFTPPlus handles native file system access
        on both Unix-like and Windows platforms for the client-side operations.

    .. grid-item-card:: :octicon:`terminal` Command-Line Client-Shell
        :link-type: doc
        :link: ./client-shell

        A command-line shell is provided to access remote file transfer servers
        using an interactive interface. Learn how to upload, download,
        and manage file transfers using this shell.


..  toctree::
    :maxdepth: 1
    :hidden:

    transfers
    operation
    transfer-scheduling
    filesystem-access
    client-shell
