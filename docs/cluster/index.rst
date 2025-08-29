Cluster deployment
==================

SFTPPlus can operate in a self-configured cluster to implement
a high-availability file transfer service, both server-side and client-side.

The SFTPPlus cluster only handles SFTPPlus configuration synchronization.
The actual files are not synchronized.
For local files, make sure all the nodes have access to the files using
a Windows Share, an Unix NFS share, or similar network attacked storage.

This section describes how to setup SFTPPlus in **active-active** cluster mode.
Get in touch if you want to setup SFTPPlus in *active-passive* or
*disaster recovery* mode.

The deployment and provisioning of the actual VM and SFTPPlus software is
outside of the scope of the cluster configuration.
SFTPPlus can work with any automated provisioning tool like Amazon Cloud
Formation, Azure Resource Manage, Google Deployment Manager, or Ansible,
to name just a few.

..  note::
    The documentation from this section can be used to implement Kubernetes clusters.
    Get in touch if you plan to deploy SFTPPlus using Kubernetes.

..  note::
    The current cluster support in SFTPPlus is designed for cluster with a static number of nodes.
    Get in touch if you plan to use SFTPPlus with auto-scale VMs.


.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` Introduction
        :link-type: doc
        :link: ./introduction

        This section provide information about cluster nodes, network and storage setup.

    .. grid-item-card:: :octicon:`book` Cluster synchronization
        :link-type: doc
        :link: ./node-sync

        Learn how cluster synchronization works and how to configure the `node-sync` resource.

    .. grid-item-card:: :octicon:`terminal` Nodes definition
        :link-type: doc
        :link: ./nodes

        Discover the security settings and access controls you can configure for cluster nodes.

    .. grid-item-card:: :octicon:`stack` Cluster operation
        :link-type: doc
        :link: ./operation

        This section explains the different cluster operation modes and provides guidance on their configuration.

    .. grid-item-card:: :octicon:`stack` Client-side transfers with failover
        :link-type: doc
        :link: ./transfers

        In this section you will find out how to configure client-side file transfers with failover support.


..  toctree::
    :maxdepth: 1
    :hidden:

    introduction
    node-sync
    nodes
    operation
    transfers
