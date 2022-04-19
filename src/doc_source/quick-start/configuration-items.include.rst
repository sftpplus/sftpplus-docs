Configuration items
-------------------

Three different types of accounts are available in SFTPPlus:

* Manager accounts - only for management operations
* OS accounts - only for file transfer operations
* Application accounts  - only for file transfer operations

Accounts dedicated to file transfer operations have multiple
:doc:`Authentication Methods </operation/authentication>` by which
remote file transfer clients can be verified and given permission to perform
file transfer operations.

Note that, by default, SFTPPlus only allows operating system accounts
from the ``example-group1`` and ``example-group2`` OS groups.
You need to update the configuration to match your target group or
groups.
