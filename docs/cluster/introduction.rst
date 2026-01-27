Introduction
============

..  contents:: :local:


Introduction
------------

The SFTPPlus software stands at the OSI Layer 7 or the TCP Layer 4 (application).
In order to have a fully fault tolerant system, you need to implement resilience at all the other layers including the OS.
SFTPPlus can be integrated with external tools, like load balancers or network storage, in order to meet the requirements for a fault tolerant infrastructure.


Cluster components
------------------

A common challenge with clustered environments is maintaining configuration consistency across all nodes.
SFTPPlus MFT solves this with a primary-secondary architecture for configuration management.

There are 2 types of SFTPPlus operation modes for the cluster:

* `controller` - Handles configuration management and can perform file transfers.
* `node` - Pulls configuration from the `controller` and performs file transfers.
  Can be configured only via the `controller`

Both the `controller` and the `node` are designed to operate independently.
The `node` will continue to perform file transfer operations even if the `controller` is not available, and vice versa.

You can configure various SFTPPlus components, like file transfers or event handlers, to be active only on the controller, only on nodes or only on a specific node.

You designate one SFTPPlus MFT instance as the **controller node**.
This is the single source of truth where you make all your configuration changes.
The other instances in the cluster act as **secondary nodes** and are configured to automatically synchronize their configuration from the primary node.
This is achieved through a `node-sync` resource defined in the configuration of the secondary nodes, which pulls the latest configuration from the primary.

A crucial aspect of this design is that a complete copy of the SFTPPlus MFT configuration is distributed to every member of the cluster.
This means that even if the **controller VM is offline**,
the secondary nodes continue to operate with their last known good configuration,
and the load balancer will continue to direct traffic to them.


Network and storage setup
-------------------------

There are 2 main area to handle the high availability:

* inbound connections - all SFTPPlus instances in the cluster will be actively handling inbound connections
* outbound connections - one SFTPPlus instance will be actively handling the outbound connections, while the other acting as failover in the case the main SFTPPlus instance fails to perform the client-side transfer.

For inbound connections you will need to use an external load balancer
that will forward the TCP/HTTP connection to the SFTPPlus services.

For outbound connections there are no requirements or dependencies on 3rd party network infrastructure.

The `controller` needs to allow **inbound** network connections to the Web Manager from the `node` instances.

The SFTPPlus cluster configuration is persisted as configuration files stored on the cluster *controller* instance.
You will need to make sure that the SFTPPlus configuration files are safely stored and included in your backup process.

The SFTPPlus cluster will only handle SFTPPlus configuration and events.
It doesn't handle storage.

All the nodes that perform file transfer operations should  have access to the files using a Windows Share, an Unix NFS share, or similar network attached storage.


Active-Passive Scenario
-----------------------

In this infrastructure scenario, the second system is offline and only
commences when the main SFTPPlus system is down.

Since the ``server.ini`` configuration is stored in a single file, you can
create a file copy task to keep the system configurations in sync.
Make sure to also transfer additional files that are required - such as SSH
keys, and SSL keys and certificates - to ensure a smooth transition.
When it is time to use the secondary system, the SFTPPlus instance will then
read the latest ``server.ini`` configuration file.


Active-Active Scenario
----------------------

In this infrastructure scenario, both SFTPPlus systems are receiving
and processing requests.
If one system goes down, the other will handle all the requests.

To implement SFTPPlus in this scenario, a simple file copy will not work.
This is because running SFTPPlus instances will not check changes in the local
file configuration (``server.ini``) in order to reconfigure.
In addition, there are other files that are also required - such as all SSH keys
in use and other related files, all SSL certificates required, any logs that
need to be kept for auditing purposes, any externally referenced scripts used in
pre- and post- transfer processing, and so on.

One method of achieving an active/active implementation is to manually set up
the 2 nodes to rely on a
:doc:`single external authentication </configuration-auth/index>` method
(HTTP, LDAP, or external file).
In this way, accounts are managed in the single external system, and
those accounts will be automatically available for both SFTPPlus instances.

Another method, is to have multiple instances sharing the same configuration
folder.
Each SFTPPlus instance will be executed on a separate VM, but they will have
the same configuration files.
Note that in this case you should make sure that you use the Web Manager
of only one instance to make configuration changes.
Once configuration changes were done, the other instances need to be
manually restarted.
Each SFTPPlus instance needs to have its own log file. To ensure that each
instance has its own log file, make sure that each instance has an unique name
and then set up the log file path using the `{host.name}` variable.
In this case, the local file event handler might look like the following
example::

        [event-handlers/b904ed23-a234-4ccf-8abd-edcae4d3324f]
        enabled = yes
        name = Log File
        type = local-file
        path = /var/logs/sftpplus-{host.name}.log
