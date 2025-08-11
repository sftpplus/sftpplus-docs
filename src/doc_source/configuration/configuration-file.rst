Configuration file
==================

..  contents:: :local:


Introduction
------------

The server is distributed with a configuration file located by default
inside the server installation folder at `configuration/server.ini`.

The configuration file is generated during the initial installation process.

During the upgrade process, the configuration file is preserved.
Obsolete configuration values are automatically migrated.

SFTPPlus uses a single configuration file for all it's components.
A component in SFTPPlus can be a user configuration, a file transfer server,
an event handler, email server configuration, and many more.

This documentation page describes in detail how to configure SFTPPlus via the configuration file.


Manual configuration
--------------------

It is recommended to use the Web Manager web console to manage the server's configuration.
The web console provides guidance and always generates valid configuration files.

For various scenarios, such as automatic deployments,
managing the setup via manual changes to the configuration file might be necessary.

To manually change the server configuration, you need to edit the configuration file using a text editor.

For opening and editing the configuration file on Windows, we recommend avoiding Notepad and using WordPad or another advanced text editor instead.

Changes made by editing the configuration file are not applied to already started server processes.
To apply your changes, restart the SFTPPlus service.


INI file format
---------------

The configuration file uses the standard INI file format.

..  warning::
    With manual editing, you have full control of the file's content,
    which may result in an invalid INI file.
    The SFTPPlus server needs a valid INI configuration file to start.

Each new server configuration option needs a new line, and the name
of the option should be at the beginning of that line.
There should be no space or tab characters before its name.

The new line should look as follows::

    >option = value

and shouldn't have any space at the beginning, such as::

    >   option = value

We use `>` here as the graphical marker for a new line,
it must not be included in the configuration file.

.INI sections are used to group and organize related configurations.
Each component is defined in a separate .INI section.
A section starts with the name of the section, on a single line,
in square brackets.

For example, the main SFTPPlus process is defined inside the `[server]` section::

    [server]
    uuid = c1ca58b2-6d36-11f0-9b48-571d4666b214
    created = 2024-12-12 10:23:44
    changed = 2025-03-07 15:23:28
    name = SFTPPlus
    umask = 022

An account is configured in a section with a name starting with `accounts/` followed by the account unique ID::

    [accounts/bdb99c31-1119-4b8b-b609-63672a9a0b6f]
    name = test_user
    enabled = yes
    created = 2025-02-15 17:19:52
    changed = 2025-03-07 15:23:28

More information about the section name and available option is found on the configuration page dedicated to each component.


Creation and changed dates
--------------------------

When SFTPPlus creates the configuration for a new component,
it will automatically set the `created` configuration option to the current date and time.

..  note::
    When the .INI file is manged outside of the SFTPPlus process,
    for example when using *devops* tools,
    you will need to set and update the creation and change dates yourself.

Each component of SFTPPlus has separate creation and change configuration options::

    [accounts/bdb99c31-1119-4b8b-b609-63672a9a0b6f]
    name = test_user
    enabled = yes
    created = 2025-02-15 17:19:52
    changed = 2025-03-07 15:23:28

    [accounts/8beced6c-6d37-11f0-9196-8b226af66b5c]
    name = other_user
    enabled = yes
    created = 2024-12-12 10:23:44
    changed = 2025-03-07 15:23:28

The values are defined using a less strict version of the ISO 8601 format.
The timezone value is not included, and the values are considered as using the local timezone.
The `T` character that separates the date and time is not required and can be replaced by a space character.

You can define these values using only the date, omitting the time value::

    [accounts/8beced6c-6d37-11f0-9196-8b226af66b5c]
    name = other_user
    enabled = yes
    created = 2024-12-12


Overriding configuration
------------------------

It's possible to extend the options from the main configuration file,
located by default at `configuration/server.ini`, through an overriding
configuration file at `configuration/server.override.ini`.

The options defined in the main `configuration/server.ini` file are referred to as `configuration options`.

The options defined in the optional `configuration/server.override.ini` file are referred to as `instance variables`.

This setup makes it easier to share a common configuration between multiple SFTPPlus installations,
while allowing setting specific configuration options for each installation instance.

For example, you might have two SFTPPlus instances in a load balancer cluster.
You need a very similar configuration for both instances, but each node should have their own unique ID to be used as part of an audit process.

Another example is running SFTPPlus in separate testing and production environments,
where the testing and production environments have similar configurations,
but each environment has a specific log file.

Let's exemplify this second scenario with snippets from the common main configuration file and the overriding configuration files for both testing and production instances.

The testing environment keeps logs for 30 days, storing them at `log/server-testing.log`.
The production environment keeps logs for 120 days, storing them at `log/server-production.log`.

The content of the common `configuration/server.ini` file used in both instances::

    [event-handlers/DEFAULT-FILE]
    enabled = Yes
    name = Log File
    type = local-file

    path = log/server-TO-BE-OVERRIDEN.log

    # Rotate every day and keep logs for 120 days.
    rotate_on = 00:00 time-of-day
    rotate_count = 120


The content of the `configuration/server.override.ini` file used on the testing environment::

    [event-handlers/DEFAULT-FILE]
    path = log/server-testing.log
    # For testing, it's enough to keep logs for 30 days.
    rotate_count = 30

The content of the `configuration/server.override.ini` file used on the production environment::

    [event-handlers/DEFAULT-FILE]
    path = log/server-production.log


Configuration file reset
------------------------

You can force the generation of a new configuration file together with new
SSH keys and self-signed certificates.
Remove the existing configuration file, then create a fresh configuration using
one of the following commands.

On Windows::

    CMD> move configuration\server.ini configuration\server.ini.old
    CMD> ./bin/admin-commands.bat initialize

On Unix-like systems::

    # mv configuration/server.ini configuration/server.ini.old
    # ./bin/admin-commands.sh initialize
