Configuration file
==================

The server is distributed with a configuration file, located
inside the server installation folder at `configuration/server.ini`.

The configuration file is generated during the installation process.

To change the server configuration, you will have to edit the
configuration file using a text editor.
The following documentation pages describe in detail how to configure the
server via the configuration file.

On Windows systems, we recommend using WordPad for opening and
editing the configuration file.

..  warning::
    The server will not automatically apply the changes from the configuration
    files.

    To apply the changes, you will need to restart the SFTPPlus service.

    In the case that you want to apply the changes without restarting
    the server, please use the Local Manager.

..  warning::
    Each new server configuration option needs a new line, and the name
    of the option should be at the beginning of that line.
    There should be no space or tab characters before its name.

    The new line should look as follows::

    >option = value

    and shouldn't have any space at the beginning, such as::

    >   option = value

    We use `>` here as the graphical marker for a new line, it must not be
    included in the configuration file.

You can force the generation of a new configuration file together with new
SSH keys and self-signed certificates.
Remove the existing configuration file, then create a fresh configuration using
one of the following commands.

On Windows::

    CMD> ./bin/admin-commands.bat initialize

On Unix-like systems::

    # ./bin/admin-commands.sh initialize
