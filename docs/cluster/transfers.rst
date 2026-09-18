Transfers with failover
=======================

..  contents:: :local:


Introduction
------------

You can configure multiple *cluster nodes* to have active transfers.
All these transfers will be active at the same time.

There are a few configuration options that need to be taken into account when implementing a transfer in a cluster.


Requirements
------------

In order to avoid conflicts with the same transfer being executed on multiple nodes,
there are a few restrictions in terms of how a transfer should be configured.

Below is the list of requirements:

* The source and destination for a transfer should be shared and accessible to all nodes.
* `delete_source_on_success` should always be enabled
* `overwrite_rule` is not supported for options `fail` or `skip`
* `transfer_memory_duration` should be disabled
* `ignore_duplicate_paths` is not supported
* `minimum_transfer_count` is not supported
* Batch transfers are not supported


Recommendations
---------------

Use separate pools for nodes that require different `failover_interval` values.
All nodes in one pool share the same failover delay.
The *primary node* should be configured with `failover_interval = 0`

For a *secondary node* it is recommended to configure a delay that is greater than the transfer duration for a single file.
For example, for small files, you can set this to 10 minutes `failover_interval = 600`
For *tertiary nodes* this can be set to 20 minutes or even 30 minutes.

When a transfer fails while a file is actively copied to the destination server,
the destination server might end up with a partially uploaded file.

It is recommended to set up the transfers to use `destination_temporary_suffix = .tmp`

In this way, on the destination server, the transferred file will be stored under the expected name only after the transfer was successful.

-------

For local files, make sure all the nodes have access to the files using a Windows Share or a Unix NFS share.
