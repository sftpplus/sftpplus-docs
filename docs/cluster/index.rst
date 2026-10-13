Cluster deployment
==================

SFTPPlus can operate in a self-configured cluster to implement
a high-availability file transfer service, both server-side and client-side.

The SFTPPlus cluster only handles SFTPPlus configuration synchronization.
The actual files are not synchronized.
For local files, make sure all the nodes have access to the files using
a Windows Share, a Unix NFS share, or similar network attached storage.

This section describes how to set up SFTPPlus in **active-active** cluster mode.
Get in touch if you want to set up SFTPPlus in *active-passive* or
*disaster recovery* mode.

The deployment and provisioning of the actual VM and SFTPPlus software is
outside of the scope of the cluster configuration.
SFTPPlus can work with any automated provisioning tool like Amazon Cloud
Formation, Azure Resource Manager, Google Deployment Manager, or Ansible,
to name just a few.

..  note::
    The documentation from this section can be used to implement Kubernetes clusters.
    Get in touch if you plan to deploy SFTPPlus using Kubernetes.

..  note::
    The current cluster support in SFTPPlus is designed for clusters with a static number of nodes.
    Get in touch if you plan to use SFTPPlus with auto-scale VMs.


Prometheus monitoring is available for cluster deployments through each instance's Web Manager service.
Enable Web Manager on each instance you want to monitor and configure Prometheus to scrape its `/metrics` endpoint separately.
Each endpoint reports only the local process; the controller does not aggregate metrics from other nodes.
See :doc:`Prometheus metrics </developer/prometheus-metrics>` for configuration and access requirements.


.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` Introduction
        :link-type: doc
        :link: ./introduction

        This section provides information about cluster nodes, network and storage setup.

    .. grid-item-card:: :octicon:`book` Cluster synchronization
        :link-type: doc
        :link: ./node-sync

        Learn how cluster synchronization works and how to configure the `node-sync` resource.

    .. grid-item-card:: :octicon:`terminal` Pools definition
        :link-type: doc
        :link: ./pools

        Discover the security settings and access controls shared by the nodes in each cluster pool.

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
    pools
    operation
    transfers
