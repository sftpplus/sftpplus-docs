.. _events-management:


Administration action events
============================


50000
^^^^^

:Message: Request does not contains an session id.
:Groups: session, failure, failure-specific, local-manager
:From version: 2.1.0
:Description: None



50001
^^^^^

:Message: Authentication failed. %(details)s
:Groups: session, failure, local-manager
:From version: 2.1.0
:Description: None



50002
^^^^^

:Message: Process state read for "%(path)s" from manager API.
:Groups: administration, informational, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :path: The part of the process that was accessed.





50003
^^^^^

:Message: Internal error while applying the requested change from local manager. "%(details)s".
:Groups: administration, failure, failure-critical, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :details: Details about the error.





50004
^^^^^

:Message: Internal JSON-RPC error: %(details)s
:Groups: operational, administration, failure, failure-critical, local-manager
:From version: 2.1.0
:Description: None



50005
^^^^^

:Message: All requested changes successfully applied. Changes: %(changes)s. Results: %(results)s.
:Groups: administration, operational, success, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :changes: List of changes applied.


  :results: List of results after applying changes.





50006
^^^^^

:Message: Not all requested changes successfully applied. Changes: %(changes)s. Results: %(results)s.
:Groups: operational, administration, failure, failure-specific, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :changes: List of changes applied.


  :results: List of results after applying changes.





50007
^^^^^

:Message: %(kind)s administrator "%(name)s" logged in local manager as role "%(role)s".
:Groups: administration, success, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :kind: The type of the authenticated administrator.


  :name: Name of administrator that was authenticated.


  :role: Name of the role associated with this administrator.





50009
^^^^^

:Message: Administrative operation denied. %(details)s
:Groups: administration, failure, local-manager
:From version: 4.15.0
:Description: None



50010
^^^^^

:Message: Administrator logged out from local manager.
:Groups: administration, informational, local-manager
:From version: 2.1.0
:Description: None



50011
^^^^^

:Message: Bad format for requested changes: %(changes)s. %(details)s
:Groups: administration, failure, failure-high, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :changes: Changes are requested by local-manager.





50012
^^^^^

:Message: Failed to apply requested change: "%(details)s".
:Groups: administration, failure, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :details: Details about the error.





50013
^^^^^

:Message: Failed to process action for runnable with UUID %(uuid)s: %(details)s
:Groups: session, failure, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :details: More details about the error.


  :uuid: UUID of the requested runnable.





50014
^^^^^

:Message: Web Manager request failed. %(details)s
:Groups: operational, authenticated, failure, local-manager
:From version: 4.0.0
:Description: None



50015
^^^^^

:Message: Internal error. Failed processing the action for runnable with UUID: %(uuid)s. %(details)s
:Groups: session, failure, failure-critical, local-manager
:From version: 2.1.0
:Description: None
:Data:
  :uuid: UUID of the requested runnable.





50016
^^^^^

:Message: Failed to get content of database "%(database_uuid)s". %(details)s
:Groups: operational, authenticated, failure, failure-high, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :details: Error details.





50017
^^^^^

:Message: Configuration synchronization from node.
:Groups: administration, success, local-manager
:From version: 4.14.0
:Description: None



50018
^^^^^

:Message: Failed to apply the "%(operation)s" configuration change for "%(target)s": %(details)s
:Groups: operational, administration, failure, failure-high, local-manager
:From version: 4.27.0
:Description: None
:Data:
  :operation: The configuration operation that was performed,


  :target: The identification of the component for which the configuration was attempted.





50019
^^^^^

:Message: Failed to get configuration for database "%(database_uuid)s". Source: %(source)s. %(details)s
:Groups: operational, authenticated, failure, failure-high, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :details: Error details.


  :source: Data source name





50020
^^^^^

:Message: Failed to get %(source)s data since database "%(database_uuid)s" is not started.
:Groups: operational, authenticated, informational, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :source: Data source name





50021
^^^^^

:Message: Failed to get data. Unknown source: "%(source)s".
:Groups: operational, authenticated, informational, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :source: Data source name.





50022
^^^^^

:Message: Failed to get %(source)s database configuration for: "%(database_uuid)s".
:Groups: operational, authenticated, informational, local-manager
:From version: 2.6.0
:Description: None.
:Data:
  :database_uuid: UUID of the database.


  :source: Data source name





50023
^^^^^

:Message: Failed to process the management action. %(details)s
:Groups: operational, authenticated, failure, failure-high, local-manager
:From version: 2.9.0
:Description: None



50024
^^^^^

:Message: Failed to generate SSH key or SSL key/csr. %(details)s
:Groups: operational, authenticated, failure, failure-high, local-manager
:From version: 2.12.0
:Description: None



50025
^^^^^

:Message: Internal error. Failed processing database entries. %(details)s
:Groups: operational, authenticated, failure, local-manager
:From version: 3.0.0
:Description: None



50026
^^^^^

:Message: Successfully generated CSV logs from %(database_uuid)s.
:Groups: operational, authenticated, success, local-manager
:From version: 3.1.0
:Description: None
:Data:
  :database_uuid: UUID of the database.





50027
^^^^^

:Message: Error occurred while generating CSV logs from %(database_uuid)s. %(details)s
:Groups: operational, authenticated, failure, local-manager
:From version: 3.1.0
:Description: None
:Data:
  :database_uuid: UUID of the database.


  :tb: Debug information with the error trace.





50028
^^^^^

:Message: Embedded database "%(db_uuid)s" operation took %(duration)s seconds to retrieve %(size)s results.
:Groups: informational, authenticated, local-manager
:From version: 4.31.0
:Description: None
:Data:
  :db_uuid: UUID of the database.


  :duration: Number of seconds it took to perform the operation.


  :size: Number of rows returned.


