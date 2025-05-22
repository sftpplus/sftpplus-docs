Cluster deployment
==================

..  contents:: :local:

Below are the configuration reference pages for the `node-sync` resource and the cluster `node` access control.

..  toctree::
    :maxdepth: 1

    node-sync
    nodes
    operation
    transfers


Introduction
------------

SFTPPlus can operate in self-configured cluster to implement a high-availability file transfer service, both server-side and client-side.

The SFTPPlus cluster only handles SFTPPlus configuration synchronization.
The actual files are not synchronized.
For local files, make sure all the nodes have access to the files using a Windows Share, an Unix NFS share, or similar network attacked storage.

This section describes how to setup SFTPPlus in **active-active** cluster mode.
Get in touch if you want to setup SFTPPlus in *active-passive* or *disaster recovery* mode.

The deployment and provisioning of the actual VM and SFTPPlus software is outside of the scope of the cluster configuration.
SFTPPlus can work with any automated provisioning tool like Amazon Cloud Formation,
Azure Resource Manage, Google Deployment Manager, or Ansible, to name just a few.

..  note::
    The documentation from this section can be used to implement Kubernetes clusters.
    Get in touch if you plan to deploy SFTPPlus using Kubernetes.

..  note::
    The current cluster support in SFTPPlus is designed for cluster with a static number of nodes.
    Get in touch if you plan to use SFTPPlus with auto-scale VMs.


Cluster components
------------------

There are 2 types of SFTPPlus operation modes for the cluster:

* `controller` - Handles configuration management and can perform file transfers.
* `node` - Pulls configuration from the `controller` and performs file transfers.
  Can be configured only via the `controller`

Both the `controller` and the `node` are designed to operate independently.
The `node` will continue to perform file transfer operations even if the `controller` is not available, and vice versa.

You can configure various SFTPPlus components, like file transfers or event handlers, to be active only on the controller, only on nodes or only on a specific node.


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
