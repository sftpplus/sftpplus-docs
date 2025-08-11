Changing the default log file configuration
-------------------------------------------

To prevent creating huge log files, the default configuration creates a log
file which is automatically rotated at the end of the day.

To prevent data loss, the default configuration doesn't delete any rotated
files.
If no action is taken on installations experiencing high transfer volumes,
this can lead to log files filling up available disk space.

For further details on changing the log configuration, please go to the
:doc:`Event Handlers </configuration-events/local-file>` section.

Please take the time to alter the log file configuration option to suit
your needs.
