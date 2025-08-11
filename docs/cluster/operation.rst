Cluster operation
=================

..  contents:: :local:


Introduction
------------

The SFTPPlus cluster can be deployed to operate in one the following modes:

* primary - secondary
* controller - nodes

There are 2 main components used to configure a cluster:

* `node-sync` resource defined on both `controller` and each `node` - Handles the synchronization of the configuration
* `cluster-nodes` - defined only on the `controller`. Handles the secure access of nodes to the `controller`

The `node-sync` resource needs to be running on any SFTPPlus instance,
in order for the cluster operations to be active.

To allow external SFTPPlus instances to access and synchronize the configuration,
the SFTPPlus instance that acts as the controller needs to have the `node-sync` resource running and configured with `role_in_cluster = controller`.
This is done to prevent accidentally triggering synchronizations between nodes.
The synchronization should always be performed between the `controller` and a `node`.
*Node to node* synchronization is not supported.

SFTPPlus cluster management is designed to handle the case in which an SFTPPlus instance is offline for maintenance for a short period of time.

When the `controller` instance is offline, the cluster will continue to operate.
Configuration changes are not allowed.
Once the `controller` is back online, configuration changes are available.

..  FIXME:7096:
    Update once cert are updated.

..  note::
    When a new SFTPPlus `node` is started it will automatically get the TLS certificate from the `controller`.
    If, at a later time, the TLS certificate for the Web Console is changed on the `controller`, you need to manually update the certificate on the `nodes`.


Primary - Secondary
-------------------

In the *primary - secondaries* mode, all SFTPPlus installation will perform file transfers.
One SFTPPlus installation will be designated as the *primary* instance and will act as the cluster **controller**.

Any configuration change should be done using the Web Manager interface of the *primary* instance.

One or multiple SFTPPlus installation will be considered *secondary* instances.
The configuration for all the *secondary* instances is pulled from the *primary* SFPPlus installation.

The Web Manager interface is still available on each secondary instance, but any configuration change will be discarded and replaced with the configuration found on the primary instance.

They will act as **nodes** in the cluster.

The *primary - secondaries* is suitable for simple load-balancer deployment, on VMs without autoscaling.

Both the primary and the secondary VMs will be added to the load balancer.

**Note:** The Web Manager service on the primary SFTPPlus installation should not be added to the load balancer.

You can implement a high-availability file transfer service using only 2 SFTPPlus instances.

Autoscaling can be implemented by auto-scaling the secondary instances.

The *secondary* instance will continue to operate even when the *primary* instance is offline.
The secondary instance can be restarted while the primary instance is **offline**.
It will operate based on the last configuration obtained from the primary instance.


Controller - Nodes
------------------

In the *controller - nodes* mode, with the exception of the *controller* instance, all SFTPPlus installations will perform file transfers.

One SFTPPlus installation will be designated as the *controller* instance and will act as the cluster **controller**.
No file transfers are active on the *controller*.

All the configuration changes are done using the Web Manager interface of the *controller*.

The controller instance will **not be added to the load balancer**.

One or multiple SFTPPlus installations will have the **node** role in the cluster.
They will pull the configuration from the *controller* and will perform file transfer operations.

The *node* instances can be configured with static VMs, auto-scaling, or pods in a Kubernetes cluster.

All node instances should be added to the load balancer.

To implement a high-availability file transfer service you will need at least 3 SFTPPlus instances:

* one controller
* two or more nodes


Cluster activation
------------------

With multiple SFTPPlus instances running in the cluster you might want to be control which file transfers or event handlers are available on particular SFTPPlus instances.

The *cluster activation* functionality allows you to control the following components:

* server-side transfers
* client-side transfer
* any event handler
* filesystem monitor resource

You can configure the following cluster operation modes:

* available on all SFTPPlus instances in the cluster
* only on controller instance
* on any node, any non-controller instance
* only on a specific node

To configure an HTTPS service to only be available on the controller SFTPPlus instance,
the configuration will look like this::

    [services/c1db1fcc-30a9-11f0-9b54-d3005de3007c]
    enabled: yes

    cluster_activation: controller

    name: Internal Portal
    type: https
    address: 0.0.0.0
    port: 10443

The actual service configuration is also replicated to all the other SFTPPlus instances,
but the service will be kept in a stopped state.
This makes it easy to convert the cluster roles for any existing SFTPPlus instance from the cluster.

The Let's Encrypt resource can only be active on the controller.

..  note::
    If you reconfigure a component to no longer be active on the controller,
    you will need to manually stop that component on the controller.


Disaster recovery
-----------------

The full SFTPPlus configuration is stored on the SFTPPlus controller and is replicated to any of the nodes from the cluster.


Convert a node to a controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the controller is no longer available you can restore the cluster by reconfiguring one of the nodes as the controller.
This can be done using the Web Manager or via text file.
As long as the configuration includes `role_in_cluster = controller`,
that SFPPlus installation will be the controller::

    [resources/DEFAULT-NODE-SYNC]
    enabled = yes
    role_in_cluster = controller

You will have to update the DNS or IP addressed to point to the new controller,
or update the URL configuration on all the other nodes to point to the URL of the new controller.

If the controller is also the primary instance, you will also need to reset the `failover_interval = 0` as part of the general server configuration.
The configuration file will be updated to::

    [server]
    failover_interval = 0


Temporary enable controller components on nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some SFTPPlus components (server-side or client-side transfer and event handlers) can be configured to only be active on the *controller* instance.

If the controller instance is no longer available, those components are not running in the cluster.

You can temporarily enable a component on one of the nodes by logging in as an administrator to the SFTPPlus Web Manager of that node and manually starting that component.

All administrators that are available on the controller are also available to login on any cluster node.

Note that if the *controller* instance is back online, the component that is configured to only run on the *controller* and which was manually started on the *node* will be automatically stopped on that node.


Web Manager on Nodes
--------------------

The Web Manager administration console is available each node (not only on the controller).
All administrators that are available on the controller are also available on the nodes.

You can connect to the Web Manager and make changes.
This is intended to be used in the following scenarios:

* Remove a node from the cluster
* Convert a node to a controller
* Controller is temporarily unavailable for a longer period of time and you want the node to take over some of the controller tasks.

..  note::
    As long as the node is configured to get the configuration from the controller,
    any manual changes done on the node will be discarded next time the node synchronization process is completed.
    This means that you can make configuration changes.
    As long as the controller is not available, those changes are kept on the node.
    As soon as the controller is available again, those changes are discarded.


Audit events
------------

The *nodes* of the cluster will send audit and security events to the cluster *controller*.

The nodes can be configured to send all their events or selected events, based on event IDs or event groups.

The events received on the controller can be used as part of the event handlers defined on the controller.

The following event groups are always sent:

* `analytics`
* `authentication`
* `component-activation`
* `failure-high`
* `failure-critical`

The events that are sent by nodes are configured as part of the *controller's* `node-sync` resource.
To configure the cluster to send all events from the group `transfer-job` or `file-operation` but exclude the events with ID `10037` you can configure the controller as::

    [resources/DEFAULT-NODE-SYNC]
    enabled = yes
    type = node-sync
    name = Cluster A
    role_in_cluster = controller

    sync_events = !10037, transfer-job, file-operation

You can configure the nodes to send all their events using the following configuration option `sync_events = all`.
Enabling this can significantly increase the load on the remote central controller SFTPPlus instance.

If you don't want the nodes to send events to the controller, you can configure this to `sync_events = disabled`.
This should be used only for testing.
Disabling all events will impact some security functionalities like detection of brute force attacks.
