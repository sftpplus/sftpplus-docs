.. container:: tags pull-left

    `client-side`
    `server-side`
    `testing`
    `debug`
    `advance`


Testing and Debugging
=====================

..  contents:: :local:


Validate server configuration
-----------------------------

When the configuration changes are done from withing the Local Manager the
changes are validated whey they are applied.
Invalid changes are not applied.

These steps are only needed when the configuration file was changes using
a text editor or external tools.

To validate the server configuration, use the following command::

    $ ./bin/admin-commands.sh validate (on Unix-like systems)
    CMD> admin-commands.bat validate (on Windows)

After the command is executed, it will list whether the
configuration is valid or not on standard output.

..  note::
    If the configuration is not valid, the exit code is 1.


Running in debug mode
---------------------

For testing the product or trying out various configuration options,
SFTPPlus can be launched in debug mode in order to provide quick feedback to
internal server operations.


While running in debug mode, the service will remain attached to the console
and will output all logging entries to the console.

..  note::
  When executed in debug mode, the server will send log files to the
  opened console as well as any other logging facility, unless configured
  otherwise.


Running the debug process on Unix-like systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The server can be started in debug mode by using the `-d` command argument
of the `bin/admin-commands.sh` command located in the SFTPPlus
installation folder.

To close the debug instance, press Ctrl+C.

For example, call the server as::

    $ ./bin/admin-commands.sh debug

..  note::
    If you want to launch the server using a configuration file from a
    specific location, use --config=/path/to/CONFIGURATION_FILE


Running the debug process on Windows systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The product can be started in debug mode by using the `service-debug.bat`
file located in the SFTPPlus installation folder.

To close the debug instance, close the command prompt window or press Ctrl+C.


Delay execution of SFTP commands
--------------------------------

The SFTP service can be configured to delay execution of a
folder listing or file reading and writing command.

Since these options are not intended to be used in production, they are not
visible in the normal configuration file.

To enable or change the delay, you will need to change the following values
at the end of this file::

    INSTALL_PATH/lib/python2.7/chevah/server/commons/constants.py


To disable the delay, set the values as::

    TEST_DELAY_EXECUTION = {
        'open_folder': 0,  # Used for folder listing operations.
        'open_file': 0,  # Used for file read and write operations.
    }

To enable a delay of 30 seconds for listing folder and a delay of 20
seconds for reading and writing files, set the values as::

    TEST_DELAY_EXECUTION = {
        'open_folder': 30,  # Used for folder listing operations.
        'open_file': 20,  # Used for file read and write operations.
    }
