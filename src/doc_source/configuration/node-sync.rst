Node synchronization
====================

The `node-sync` resource is handling the synchronization of the local SFTPPlus node with the remote SFTPPlus controller managing the cluster group.

The communication between nodes and the remote controller is done via HTTPS and thus protected using TLS.
The node synchronization has the standard configuration options of a TLS-based SFTPPlus component.

Once synchronized, a local node operates as an independent SFTPPlus file transfer service.
Even if the remote controller is offline, a local node continues to work using the last known configuration.
As soon as the controller is available again, local nodes update their configurations to be up to date with the controller's configuration.

When you stop or start a component on the main controller, a corresponding start or stop action on the synchronized nodes is automatically triggered.
You can enable or disable a component on the main controller to trigger a corresponding start or stop action on the nodes.

The configuration for the node synchronization resource itself is independent of the changes made on the controller node.

..  warning::
    In the current version, only the configuration changes stored in the main configuration file are synchronized.
    Certificates or SSH keys stored as external files are not synchronized.
    Encrypted SSH or TLS keys are not synchronized.
    The content of the `local-file` authentication method configuration file is not synchronized.


url
^^^

:Default value: ''
:Optional: Yes
:Values: * URL
:From version: 5.11.0
:Description:
    The URL of the remote controller from which this local node synchronizes its configuration,
    receives management commands, and reports status to.

    When left empty, SFTPPlus operates in stand-alone mode, without synchronizing with a remote controller.


username
^^^^^^^^

:Default value: `None`
:Optional: No
:Values: * Text.
:From version: 5.11.0
:Description:
    The universally unique identifier (UUID) allows this local node to be
    identified among other nodes as part of the controller's configuration.

    It can be any unique string, but we recommend using the UUID standard
    format.

    To generate a UUID value, please check the dedicated documentation for
    :ref:`admin-commands generate-uuid <generate-uuid>`.


password
^^^^^^^^

:Default value: `None`
:Optional: No
:Values: * Plain text.
:From version: 5.11.0
:Description:
    This is the password used by this node to authenticate to the controller.


sync_interval
^^^^^^^^^^^^^

:Default value: 60
:Optional: No
:Values: * Number of seconds greater than 0
:From version: 5.11.0
:Description:
    The interval in seconds between consecutive pulls of the configuration changes from the controller.

    It should be greater than 0.
    We don't recommend setting it to values lower than 60 seconds for production usage.
    Lower values can be used to help with testing.

.. include:: /configuration/ssl.include.rst
