Nodes definition
================

..  contents:: :local:


Introduction
------------

A cluster `node` represents the secure access of a cluster node to the remote cluster controller.
The configuration of the `node` is done via the remote cluster controller.

This section describes the secure access configuration options available to be used for the nodes from the cluster.

The cluster `node` configuration is defined as part of the SFTPPlus cluster `controller`. The configuration is not required on cluster `nodes`.

SFTPPlus cluster `node` instances are managed using the :doc:`node-sync resource </cluster/node-sync>`.
Check the documentation for the `node-sync` resource to see what configuration options are available for operating the cluster.


Adding a new node via Web Manager
---------------------------------

New node are added using the Web Manager via the `node-sync` resource.

You need to configure the `node-sync` resource with `role_in_cluster = controller`

After that, the UI will show the option to define the nodes from the cluster.


Adding a new node via text configuration
----------------------------------------

Adding a new node is done by creating a new section inside the configuration
file.
The name of the section should be prefixed with ``cluster-nodes/`` and followed by the
node's UUID.

The node's UUID can be any unique string used to identify the node.
Once defined, the UUID should not be changed.

For example, to add a new node named **node-A**::

    [cluster-nodes/a904e3a6-a59b-4bbf-8abd-edcae4d3774f]
    name = node-A
    enabled = Yes
    description = Node operating in data-center A.
    password = $5$DfjfEI8R1.fpGQg9$ADD-PASSWORD-IN-SECURE-STORE-FORMAT
    source_ip_filter =
        allow 10.0.0.0/8
        allow 172.16.0.0/12


Below you can find the configuration option available for cluster node.


enabled
-------

:Default value: `Yes`
:Optional: Yes
:From version: 5.13.0
:Values: * `Yes`
         * `No`
:Description:
    This option specifies whether or not this node is disabled.

    When a `node`` is disable any file transfer operations is disabled.
    When the `controller` is disabled, it will not allow connections from the remote nodes.


name
----

:Default value: ''
:Optional: No
:From version: 5.13.0
:Values: * Any text.
:Description:
    Human-readable short string used to identify this node.


description
-----------

:Default value: ''
:Optional: Yes
:From version: 5.13.0
:Values: * Any character string.
:Description:
    Human-readable text that describes the purpose of this node.


source_ip_filter
----------------

:Default value: Empty
:Optional: Yes
:From version: 5.13.0
:Values: * Source IP/CIDR access control rules
         * Empty

:Description:
    This option defines the source IPs from which access is allowed for this node.

    The node configuration option is similar to the group configuration.
    For more details, see the
    :doc:`group configuration </configuration-auth/groups>` documentation page.


failover_interval
-----------------

:Default value: 600
:Optional: Yes
:From version: 5.13.0
:Values: * Number of seconds
:Description:
    Number of seconds used to increase the `stable_interval` configuration option for all transfers and filesystem monitors on this node.

    This allows configuring *primary* and *secondary* nodes, in which the transfer are first executed on the primary node. If the primary node fails to transfer the files, the secondary node will try to transfer the files again with a delay configured via the `failover_interval`.

    You should set this to `0` for the *primary node*.

    For more details, see the
    :doc:`transfers cluster </cluster/transfers>` documentation page.


node_variables
--------------

:Default value: Empty
:Optional: Yes
:From version: 5.13.0
:Values: * INI text
:Description:
    The value from here is used to overwrite any configuration when applied to this remote node.
