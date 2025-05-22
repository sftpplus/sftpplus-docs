Cluster synchronization
=======================

..  contents:: :local:


Introduction
------------

The `node-sync` resource handles the synchronization of multiple SFTPPlus instance that operate as part of a single SFTPPlus file transfer cluster.

The same `node-sync` resource is use to setup a cluster `controller` or one or more cluster `nodes`.

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


role_in_cluster
---------------

:Default value: `node`
:Optional: Yes
:Values: * `controller`
         * `node`
:From version: 5.13.0
:Description:
    Defines how this SFTPPlus instance will interact with other SFTPPlus instance as part of the cluster.

    When configured as `controller`, this SFTPPlus instance will allow remote SFTPPlus cluster nodes to pull their configuration and receive events and status from the remote cluster nodes.

    When configured as `node`, this SFTPPlus instance will pull its configuration from the cluster controller.
    You will need to configure the URL to the controller and the credentials for this node.
    Direct configuration is disabled.


sync_interval
-------------

:Default value: 60
:Optional: No
:Values: * Number of seconds greater than 0
:From version: 5.11.0
:Description:
    The interval in seconds between consecutive pulls of the configuration changes from the controller.

    It should be greater than 0.
    We don't recommend setting it to values lower than 60 seconds for production usage.
    Lower values can be used to help with testing.

    This is ignored when configured together with `role_in_cluster = node`.


sync_events
-----------

:Default value: Empty
:Optional: yes
:Values: * Event ID
         * Event group
         * Comma-separated list of event IDs
         * Comma-separated list of event groups
         * Comma-separated list of event IDs and event groups
         * `all`
:From version: 5.13.0
:Description:
    The nodes will always send to the controller authentication and security related events.

    This defined which additional events are sent from the cluster nodes to the cluster controller.

    When configured with an *empty* value, no extra events are sent.

    When you want to send all the events excepting some few events,
    you should prefix each event id or group name with the exclamation mark (!).

    When using cloud based or distributed Security information and event management (SIEM) systems you can leave this as *empty* value.
    The SIEM will take care of aggregating and managing the logs in a centralized way.


url
---

:Default value: ''
:Optional: Yes
:Values: * URL
:From version: 5.11.0
:Description:
    The URL of the remote controller from which this local node synchronizes its configuration,
    receives management commands, and reports status to.

    This is ignored when configured together with `role_in_cluster = controller`.


username
--------

:Default value: `None`
:Optional: No
:Values: * Text.
:From version: 5.11.0
:Description:
    The node of the node as configured on the controller.

    This is ignored when configured together with `role_in_cluster = controller`.


password
--------

:Default value: `None`
:Optional: No
:Values: * Plain text.
:From version: 5.11.0
:Description:
    This is the password used by this node to authenticate to the controller.

    This is ignored when configured together with `role_in_cluster = controller`.


.. include:: /configuration/ssl-client.include.rst
