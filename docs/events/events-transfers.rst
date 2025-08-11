.. _events-transfers:


Automated file transfers events
===============================


60000
^^^^^

:Message: File "%(path)s" was modified in monitored path.
:Groups: transfer, informational, client-side
:From version: 2.6.0
:Description: None.



60001
^^^^^

:Message: File "%(from_path)s" was renamed in monitored path to "%(to_path)s".
:Groups: transfer, informational, client-side
:From version: 2.6.0
:Description: None
:Data:
  :from_path: Initial path.


  :to_path: Final path.





60002
^^^^^

:Message: Command failed: %(details)s
:Groups: authenticated, failure, failure-critical, client-side
:From version: 3.0.0
:Description: None



60003
^^^^^

:Message: File "%(path)s" was created in monitored path.
:Groups: transfer, informational, client-side
:From version: 2.6.0
:Description: None



60004
^^^^^

:Message: File "%(path)s" exists in the monitored path and will be transferred.
:Groups: transfer, informational, client-side
:From version: 3.6.0
:Description: None



60005
^^^^^

:Message: Error occurred while taking a snapshot for "%(path)s". Retrying %(retries_left)s more times after %(delay)s seconds. %(details)s
:Groups: location-operation, failure, client-side
:From version: 3.19.0
:Description: None



60006
^^^^^

:Message: File "%(path)s" added to batch. %(details)s
:Groups: transfer, informational, client-side
:From version: 3.36.0
:Description: None
:Data:
  :path: Path to the file for which a transfer was delayed.





60007
^^^^^

:Message: Executing command "%(name)s" for "%(path)s".
:Groups: transfer-job, informational, client-side
:From version: 2.7.0
:Description: None
:Data:
  :destination_path: Path to destination file.


  :source_path: Path to source file.





60008
^^^^^

:Message: Command "%(name)s" was successful for "%(path)s". Output "%(output)s". Error "%(error)s". Exit code "%(exit_code)s".
:Groups: transfer-job, success, client-side
:From version: 2.7.0
:Description: None
:Data:
  :destination_path: Path to destination file.


  :error: Error text produced by the command.


  :exit_code: Exit code of the command


  :output: Output text produced by the command.


  :source_path: Path to source file.





60009
^^^^^

:Message: Command "%(name)s" failed for "%(path)s". Output "%(output)s". Error "%(error)s". Exit code "%(exit_code)s". %(details)s
:Groups: transfer-job, failure, client-side
:From version: 2.7.0
:Description: None
:Data:
  :destination_path: Path to destination file.


  :error: Error text produced by the command.


  :exit_code: Exit code of the command


  :output: Output text produced by the command.


  :source_path: Path to source file.





60010
^^^^^

:Message: Source and destination ready. Start %(transfer_type)s for "%(path)s" with a size of %(size)s bytes. Content action: %(content_action)s.
:Groups: transfer-job, informational, client-side
:From version: 2.9.0
:Description: None
:Data:
  :content_action: The action done to change the content of the file during the transfer.


  :size: Size of the source file in bytes.


  :transfer_type: Describe if this is a upload/push, download/pull or local-to-local transfer.





60011
^^^^^

:Message: Failed to transfer "%(path)s". Will retry %(count)s more. Next try after %(wait)s seconds. %(details)s
:Groups: transfer-job, failure, client-side, file-operation
:From version: 3.0.0
:Description: None
:Data:
  :count: Number of times the transfer will be retried from now on.


  :wait: Number of seconds to wait before retrying.





60012
^^^^^

:Message: Successful %(transfer_type)s for file "%(path)s" to "%(destination_path)s" with a size of %(size)s bytes of which %(transferred_size)s bytes were transferred in %(duration)s seconds at %(speed)s kB/s.
:Groups: transfer-job, success, client-side, file-operation
:From version: 2.9.0
:Description: None
:Data:
  :destination_path: Path on the destination location.


  :source_path: Path on the source location.





60013
^^^^^

:Message: Error occurred while %(transfer_type)s for file "%(path)s" of %(size)s bytes of which %(transferred_size)s bytes were transferred in %(duration)s seconds at %(speed)s kB/s. %(details)s
:Groups: transfer-job, failure, client-side, file-operation
:From version: 2.9.0
:Description: None



60014
^^^^^

:Message: Failed to open source file "%(path)s" for reading. %(details)s
:Groups: transfer-job, failure, client-side, file-operation
:From version: 2.9.0
:Description: None



60015
^^^^^

:Message: Failed to open destination file "%(path)s" for writing. %(details)s
:Groups: transfer-job, failure, client-side, file-operation
:From version: 2.9.0
:Description: None



60016
^^^^^

:Message: Transfer job failed at %(step_name)s after all retries. The following files failed: %(failed_paths)s. The following files succeeded: %(success_paths)s. %(skip_paths)s
:Groups: transfer-job, failure, failure-high, failure-specific, client-side
:From version: 2.9.0
:Description: None
:Data:
  :failed_list: List of paths which failed.


  :failed_paths: Comma separated paths which failed.


  :step_name: Name of the step at which transfer failed.


  :success_list: List of path which were successfully transferred to the destination.


  :success_paths: Comma separated paths which were successfully transferred to the destination.





60017
^^^^^

:Message: Transfer succeeded for source %(paths)s to %(destination_paths)s. %(skip_paths)s
:Groups: transfer-job, success, client-side
:From version: 2.9.0
:Description: None
:Data:
  :destination_paths: List of destination paths which were transferred.


  :paths: Comma-separated source paths which were transferred to the destination.


  :skip_paths: Comma-separated list of files that were skipped.


  :success_list: List of source paths which were transferred.





60018
^^^^^

:Message: Internal error. Failed executing transfer for "%(path)s" at "%(step_name)s". %(details)s
:Groups: transfer-job, failure, failure-critical, client-side
:From version: 2.9.0
:Description: None



60019
^^^^^

:Message: Less than %(minimum_count)s files were successfully transferred in the last %(success_interval)s seconds. Transfer count: %(transfer_count)s.
:Groups: transfer, failure, failure-specific, client-side
:From version: 5.1.0
:Description: None
:Data:
  :minimum_count: The configured minimum transferred files.


  :success_interval: Time interval in seconds used to count the transferred files.


  :transfer_count: Number of files successfully transferred in the configured interval.





60020
^^^^^

:Message: Action "%(action)s" scheduled  in "%(seconds)s" seconds by "%(date)s" for transfer "%(name)s".
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :action: Name of the scheduled action.


  :date: Date and time at which the action was scheduled.


  :name: Name of the transfer for which the action was scheduled.





60021
^^^^^

:Message: Transfer "%(name)s" started in "%(state)s" state.
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the started transfer.


  :state: The name of the state in which the transfer was started.





60022
^^^^^

:Message: Scheduled action "%(action)s" executed for transfer "%(name)s".
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :action: Name of the scheduled action.


  :name: Name of the transfer for which the action was scheduled.





60023
^^^^^

:Message: Transfer "%(name)s" has detected a "%(action)s" action scheduled for "%(expected_date)s", but its execution time has already passed. It was re-scheduled for now.
:Groups: transfer, failure, failure-specific, client-side
:From version: 3.0.0
:Description: None
:Data:
  :action: Name of the scheduled action.


  :expected_date: Date and time at which the action was scheduled in ISO format.


  :name: Name of the transfer for which the action was scheduled.





60024
^^^^^

:Message: Keep alive call failed for resource "%(name)s" . %(details)s
:Groups: authenticated, failure, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the resource for which the keep alive was called.





60025
^^^^^

:Message: Failed to archive "%(path)s" as "%(archive_path)s". %(details)s
:Groups: transfer-job, failure, client-side
:From version: 2.10.0
:Description: None
:Data:
  :archive_path: Destination path of the archive.





60026
^^^^^

:Message: File "%(path)s" was successfully archived as "%(archive_path)s".
:Groups: transfer-job, success, client-side
:From version: 2.10.0
:Description: None
:Data:
  :archive_path: Destination path of the archive.





60027
^^^^^

:Message: Invalid overwrite rule configuration "%(details)s" for transfer "%(name)s".
:Groups: transfer-job, failure, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the transfer with invalid configuration.





60028
^^^^^

:Message: Fail to transfer file "%(path)s" for "%(name)s". File already exists on the destination and transfer is not configured to overwrite it.
:Groups: transfer-job, failure, failure-specific, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the transfer associated with this event.





60029
^^^^^

:Message: Remote file "%(path)s" is going to be overwritten for transfer "%(name)s".
:Groups: transfer-job, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the transfer associated with this event.





60030
^^^^^

:Message: Remote file "%(existing_path)s" was renamed to "%(path)s" to prevent overwriting it for "%(name)s".
:Groups: transfer-job, success, client-side
:From version: 3.0.0
:Description: None
:Data:
  :existing_path: Previous path of the existing file on the destination.


  :name: Name of the transfer associated with this event.


  :path: New path of the existing file, after rename operation.





60031
^^^^^

:Message: File "%(path)s" is going to be transfered as "%(destination_path)s" for "%(name)s" as a file with same name already exists on the destination.
:Groups: transfer-job, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :destination_path: Path on the destination where file will be transferred.


  :name: Name of the transfer associated with this event.





60032
^^^^^

:Message: Start collecting files for batch transfer "%(name)s" with an interval of %(seconds)s seconds starting with "%(path)s".
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the transfer.


  :seconds: Number of seconds used for batch interval.





60033
^^^^^

:Message: Added to the execution queue the %(kind)s transfer for "%(name)s" with %(count)s files: %(files)s.
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :count: Number of files in the batch.


  :files: Human readable list of the scheduled files


  :kind: The type of this transfer


  :name: Name of the transfer.


  :queue: List of the scheduled files





60034
^^^^^

:Message: Canceled execution of batch transfer for "%(name)s" with %(count)s files.
:Groups: transfer, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :count: Number of files in the batch.


  :name: Name of the transfer.





60035
^^^^^

:Message: Closed with success "%(path)s" on "%(location)s" after opening for %(mode)s. Read: %(read_size)s. Write: %(write_size)s
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.





60036
^^^^^

:Message: Closed with failure "%(path)s" on "%(location)s" after opening for %(mode)s. %(details)s
:Groups: failure, failure-high, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.





60037
^^^^^

:Message: Failed to read "%(path)s" on "%(location)s" after opening for %(mode)s. %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.





60038
^^^^^

:Message: Failed to write "%(path)s" on "%(location)s" after opening for %(mode)s. %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :mode: How the file handler was created.





60039
^^^^^

:Message: Started monitoring %(recursive)s"%(path)s" on "%(location)s" every %(changes_poll_interval)ss (stable %(stable_interval)ss/%(failover_interval)ss).
:Groups: success, authenticated, client-side
:From version: 3.0.0
:Description: None
:Data:
  :changes_poll_interval: Seconds at which path is monitored.


  :failover_interval: Second after which failover is triggered in cluster operations


  :location: Name of the location on which this operation was performed.


  :recursive: Flag to signal if monitoring is recursive.


  :stable_interval: Seconds after which actions are triggered for unchanged files.





60040
^^^^^

:Message: Stopped monitoring "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60041
^^^^^

:Message: Operation to check the existence of "%(path)s" was successful on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60042
^^^^^

:Message: Failed to check that "%(path)s" exists on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60043
^^^^^

:Message: Successfully renamed "%(from)s" to "%(to)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :path: The new name of the file.


  :to: The new name of the file.





60044
^^^^^

:Message: Failed to rename "%(from)s" to "%(to)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :path: The new name of the file.


  :to: The new name of the file.





60045
^^^^^

:Message: Successfully deleted file "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60046
^^^^^

:Message: Failed to delete file "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60047
^^^^^

:Message: Successfully deleted directory (recursive %(recursive)s) "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :recursive: `True` when a recursive request was made





60048
^^^^^

:Message: Failed to delete directory (recursive %(recursive)s) "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


  :recursive: `True` when a recursive request was made





60049
^^^^^

:Message: Successfully created directory "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60050
^^^^^

:Message: Failed to create directory "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60051
^^^^^

:Message: Successfully listed directory "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60052
^^^^^

:Message: Failed to list directory "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60053
^^^^^

:Message: Successfully opened "%(path)s" for reading on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60054
^^^^^

:Message: Failed to open file "%(path)s" for reading on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60055
^^^^^

:Message: Successfully opened "%(path)s" for writing on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60056
^^^^^

:Message: Failed to open file "%(path)s" for writing on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60057
^^^^^

:Message: Successfully opened "%(path)s" for appending on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60058
^^^^^

:Message: Failed to open file "%(path)s" for appending on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60059
^^^^^

:Message: Successfully touched "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60060
^^^^^

:Message: Failed to touch "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60061
^^^^^

:Message: Successfully copied local "%(path)s" to local "%(to)s" (overwrite %(overwrite)s) on "%(location)s".
:Groups: success, file-operation, location-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :overwrite: True if copy operation was done with overwrite enabled.


  :path: Old name of the file.


  :to: The new name of the file.





60062
^^^^^

:Message: Failed to copy local "%(path)s" to local "%(to)s" on "%(location)s". %(details)s
:Groups: location-operation, failure, file-operation, client-side
:From version: 3.0.0
:Description: None
:Data:
  :from: Old name of the file.


  :location: Name of the location on which this operation was performed.


  :overwrite: True if copy operation was done with overwrite enabled.


  :path: Old name of the file.


  :to: The new name of the file.





60063
^^^^^

:Message: Sending keep alive call for resource "%(name)s".
:Groups: authenticated, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the resource for which the keep alive was called.





60064
^^^^^

:Message: Executing "%(condition)s" commands on destination for "%(name)s".
:Groups: transfer-job, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :condition: Condition for which the commands are executed.


  :name: Name of the transfer for which the commands are executed.





60065
^^^^^

:Message: Successfully executed "%(condition)s" commands on destination for "%(name)s".
:Groups: transfer-job, success, client-side
:From version: 3.0.0
:Description: None
:Data:
  :condition: Condition for which the commands are executed.


  :name: Name of the transfer for which the commands are executed.





60066
^^^^^

:Message: Failed to execute "%(condition)s" commands on destination for "%(name)s". %(details)s
:Groups: transfer-job, failure, client-side
:From version: 3.0.0
:Description: None
:Data:
  :condition: Condition for which the commands are executed.


  :name: Name of the transfer for which the commands are executed.





60067
^^^^^

:Message: Disconnecting as resource "%(name)s" was idle for %(seconds)s seconds.
:Groups: authenticated, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the resource associated with this event.


  :seconds: Number of seconds after which resource is configured to disconnect on idle.





60068
^^^^^

:Message: Reconnecting as resource "%(name)s" is configured to always keep the connection alive.
:Groups: authenticated, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :name: Name of the resource associated with this event.





60069
^^^^^

:Message: Failed to close source "%(path)s" after failing to open destination "%(destination_path)s". %(details)s
:Groups: transfer-job, file-operation, failure, failure-high, client-side
:From version: 3.12.0
:Description: None
:Data:
  :destination_path: Path of the destination file which failed to be opened.


  :source_path: Path of the source file which failed to be closed.





60070
^^^^^

:Message: Transfer temporarily paused for file "%(path)s" at %(step_name)s as %(location)s is not yet available. All the other files are paused waiting for the location automatic (re)connection.
:Groups: transfer-job, informational, client-side
:From version: 3.10.0
:Description: None



60071
^^^^^

:Message: Successfully got attributes for "%(path)s" on "%(location)s".
:Groups: success, location-operation, client-side
:From version: 3.20.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60072
^^^^^

:Message: Failed to get attributes for "%(path)s" on "%(location)s". %(details)s
:Groups: failure, location-operation, client-side
:From version: 3.20.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.





60073
^^^^^

:Message: Start executing transfer for "%(name)s" with %(count)s files: %(files)s.
:Groups: transfer-job, informational, client-side
:From version: 3.0.0
:Description: None
:Data:
  :count: Number of files in the batch.


  :files: List of the scheduled files


  :name: Name of the transfer.


  :type: The type of this transfer





60074
^^^^^

:Message: Snapshot with %(total_files)s files and %(total_directories)s directories for "%(path)s".
:Groups: transfer, informational, client-side
:From version: 3.48.0
:Description: None
:Data:
  :path: Path which was listed


  :total_directories: Number of directories which were detected.


  :total_files: Number of files which were detected and were matching the filter.





60075
^^^^^

:Message: Not transferring file "%(path)s" in the monitored path. %(reason)s
:Groups: transfer, informational, client-side
:From version: 4.0.0
:Description: None
:Data:
  :reason: Event which triggered the attempt to transfer this file.





60076
^^^^^

:Message: Transfer skipped for source "%(path)s". %(reason)s
:Groups: transfer-job, informational, client-side
:From version: 4.0.0
:Description: None
:Data:
  :path: Source path of the file that was skipped.


  :reason: Reason why the file was skipped.





60077
^^^^^

:Message: Successfully removed archived file "%(path)s" older than %(days)s days.
:Groups: transfer, informational, client-side
:From version: 3.51.0
:Description: None



60078
^^^^^

:Message: Transfer job canceled for "%(path)s" at "%(step_name)s".
:Groups: transfer-job, failure, failure-specific, client-side
:From version: 4.3.0
:Description: None



60079
^^^^^

:Message: Conflicting content detected for source file "%(path)s". Consider increasing the 'stable_interval' configuration. %(details)s
:Groups: transfer, failure, client-side
:From version: 4.3.0
:Description: None
:Data:
  :reason: Event which triggered the attempt to transfer this file.





60080
^^^^^

:Message: Removing file from transfer queue "%(path)s" as it was removed from the source location.
:Groups: transfer, informational, client-side
:From version: 4.3.0
:Description: None



60081
^^^^^

:Message: Transfer failed for "%(path)s" at "%(step_name)s". %(details)s
:Groups: transfer-job, failure, client-side
:From version: 4.3.0
:Description: None



60082
^^^^^

:Message: Location %(location)s for %(step_name)s is now available to transfer "%(path)s".
:Groups: transfer-job, informational, client-side
:From version: 4.4.0
:Description: None



60083
^^^^^

:Message: Configured "stable_interval" ignored as it is smaller than "changes_poll_interval". %(stable_interval)s seconds used instead.
:Groups: transfer, failure, failure-specific, client-side
:From version: 4.4.0
:Description: None



60084
^^^^^

:Message: Failed to delete parent directory %(path)s for a source file. %(details)s
:Groups: transfer, failure, client-side
:From version: 4.10.0
:Description: None



60085
^^^^^

:Message: Failed to start monitoring "%(path)s" on "%(location)s". Will automatically retry when the location is connected. %(details)s
:Groups: failure, transfer, client-side
:From version: 4.23.0
:Description: None
:Data:
  :location: Name of the location on which this operation was performed.


