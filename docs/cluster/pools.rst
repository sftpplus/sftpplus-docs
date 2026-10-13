Pools definition
================

..  contents:: :local:


Introduction
------------

A cluster pool defines the credentials and configuration shared by one or more SFTPPlus nodes.
Pools are configured on the cluster controller.
Every node in a pool connects to the controller using the same pool name and pool sync password.

SFTPPlus cluster nodes are managed using the :doc:`node-sync resource </cluster/node-sync>`.
Configure each node with `role_in_cluster = node`, the controller URL, the `pool_name`, and the pool sync password.
Each node also advertises its `node_name`, which defaults to the local operating system's hostname.
The advertised name is limited to the first 40 characters and stored as `instance_name` in the activity log.
Forwarded activity log entries include the pool name, pool UUID, and node name in their extra data and JSON view.


Adding a new pool via Web Manager
---------------------------------

Open the `node-sync` resource and configure it with `role_in_cluster = controller`.
Use **Add cluster pool** to define the pool name, pool sync password, and source IP access rules.
Use **Generate and copy password** to create a random password and copy it to the clipboard.
Before saving, you can use **Show password** to reveal the new value or **Copy password** to copy it again.
The saved password cannot be retrieved, shown, or copied when you reopen the pool.
Configure each node that belongs to the pool with these shared credentials.


Adding a new pool via text configuration
----------------------------------------

Create a new section in the controller's configuration file.
Prefix the section name with `cluster-pools/`, followed by the pool's UUID.

The UUID can be any unique string used to identify the pool.
Once defined, the UUID should not be changed.

For example, to add a pool named **pool-A**::

    [cluster-pools/a904e3a6-a59b-4bbf-8abd-edcae4d3774f]
    name = pool-A
    enabled = Yes
    description = Nodes operating in data center A.
    password = $5$DfjfEI8R1.fpGQg9$ADD-PASSWORD-IN-SECURE-STORE-FORMAT
    source_ip_filter =
        allow 10.0.0.0/8
        allow 172.16.0.0/12

The configuration options below apply to all nodes in the pool.
Their names and values are unchanged from the former cluster node configuration.


enabled
-------

:Default value: `Yes`
:Optional: Yes
:From version: 5.13.0
:Values: * `Yes`
         * `No`
:Description:
    Specifies whether nodes in this pool can connect to the controller.

    Disabling the pool prevents its nodes from authenticating to the controller.
    Nodes continue to operate using their last synchronized configuration.


name
----

:Default value: Empty
:Optional: No
:From version: 5.13.0
:Values: * Any text.
:Description:
    A short name that identifies this pool.

    Configure this value as the `pool_name` of the `node-sync` resource on every node in the pool.


description
-----------

:Default value: Empty
:Optional: Yes
:From version: 5.13.0
:Values: * Any text.
:Description:
    Text that describes the purpose of this pool.


source_ip_filter
----------------

:Default value: Empty
:Optional: Yes
:From version: 5.13.0
:Values: * Source IP/CIDR access control rules
         * Empty
:Description:
    Defines the source IP addresses from which nodes in this pool can connect.

    Leave empty to allow connections from any source IP address.
    For the access rule syntax, see the :doc:`group configuration </configuration-auth/groups>` documentation.


failover_interval
-----------------

:Default value: 600
:Optional: Yes
:From version: 5.13.0
:Values: * Number of seconds
:Description:
    Number of seconds added to the `stable_interval` configuration option for all transfers and filesystem monitors on nodes in this pool.

    Use separate pools to configure different failover delays for primary and secondary nodes.
    Set this to `0` for a pool containing the primary node.
    All nodes in the same pool use the same delay.

    For more details, see the :doc:`transfers cluster </cluster/transfers>` documentation.


node_variables
--------------

:Default value: Empty
:Optional: Yes
:From version: 5.13.0
:Values: * INI text
:Description:
    Configuration overrides applied to every node in this pool.

    The option retains the name `node_variables` for compatibility.
