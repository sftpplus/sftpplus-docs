cluster_activation
------------------

:Default value: 'all'
:Optional: No
:From version: 5.13.0
:Values: * `all`
         * `controller`
         * `node`
         * Pool UUID
:Description:
    When clustering is enabled, it determines on which SFTPPlus instance this component is enabled.

    When configured with `all`, it will be active on any SFTPPlus instance, including the controller and all nodes.

    When configured with `controller`, it will only be active on the SFTPPlus controller instance.

    When configured with `node`, it will be active on all SFTPPlus node instances.

    Configure it with the UUID of a pool to make it active on all nodes in that pool.

    ..  note::
        The `enabled` configuration is not ignored. When configured with `enabled = No` this will not be active,
        regardless of the `cluster_activation` configuration.
