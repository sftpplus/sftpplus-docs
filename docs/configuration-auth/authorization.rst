Account authorization
#####################

Authentication identifies an account and verifies its credentials.
Authorization determines which operations the authenticated account can perform.
SFTPPlus applies the account's configuration and associated groups when authorizing access to files and folders.

For server-side file access over SFTP, FTP, HTTP, and other file transfer protocols, see :doc:`path-permissions`.
That page describes default permissions, path matching, group inheritance, and the permissions required for individual operations.

For information about identifying accounts, see :doc:`authentication`.
For recording operations and responding to events, see :doc:`event handlers</administration/event-handlers>`.
