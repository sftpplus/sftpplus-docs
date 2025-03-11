Installation Validation and Troubleshooting
===========================================

..  contents:: :local:

This page provides information which should help in identifying problems
with starting or operating the server.


Testing your configuration
--------------------------

The simplest test to see if the server is running is just to log in to the
:doc:`Web Manager </quick-start/local-manager>` at `https://localhost:10020`.

It may take a few iterations of your specific use case to get everything
configured perfectly.
If you would like help in configuring your instance,
please feel free to contact us.


Starting in debug mode
----------------------

If you encounter problems while launching or operating the server,
you can try launching the server in `debug` mode.

On Unix-like systems::

    cd /opt/sftpplus
    ./bin/admin-commands.sh debug -c configuration/server.ini

On Windows, you can either start it using the shortcut provided inside the
*Start menu*, or from the command prompt::

    CMD> cd 'c:\Program Files\SFTPPlus'
    CMD> debug.bat


Service start
-------------

On all supported operating systems (Windows / Linux / macOS), the SFTPPlus
service will only fail on critical errors.
In the case that the application has been started, but a service or event
handler is not working, please check the `Failed at start` entries in the
Web Manager Status page or in the audit logs.


Logging system problems
-----------------------

When started in debug mode, the server will send all audit logs to the console /
standard output.
This can help you investigate issues related to the
logging system, for example a missing log file or bad permissions for the log
file.

In the case that the server has been successfully started, but you don't see any
log message, use the Web Manager Status page and check for any event
handers with a status of `Failed at start`.


Windows service start errors
----------------------------

If the SFTPPlus service fails to start on Windows, you can check the
Event Viewers to investigate Windows Eventlog created at startup.
The application emit events using the `sftpplus-service` source inside the
'Application' category.

On failure, the server will emit multiple event logs; make sure you check both
`Information` and `Error` event types.
