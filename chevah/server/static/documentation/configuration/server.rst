Server's process
================

When launched, the server starts a series of file transfer services, using
various file transfer protocols.
It also starts the internal services used by all file transfer services;
for example, the authentication service and the log service.

All services are executed under a single server process.

This page describes general server configuration options and options
affecting all file transfer services.


..  contents:: :local:


Configuration for the main server process
-----------------------------------------

You can access the section via the 'Server' page in Local Manager.

..  image:: /_static/gallery/gallery-test-server.png

----

For text configuration, options affecting all services are grouped inside the
``server`` section.

Below is another sample for the ``server`` section as a text configuration::

    [server]
    uuid = 530019d0-92ce-11e2-9e96-0800200c9a66
    name = Short_Name_For_Server
    description = Long text describing the server
    account = sftpplus
    execute_at_startup = Disabled
    umask = 022
    authentications = 0022b17a-30a0-4b70, ffa17005-51c2-42f1
    manager_authentications = 65a1-41ce-fea1-8015


uuid
^^^^

:Default value: ``single-server-uuid``
:Optional: No
:Values: * An unique identifier among all servers active in a deployment
         * Alphanumeric and dash ('-') character.
           No space characters.
:From version: 2.0.0
:To version: None
:Description:
    The universally unique identifier (UUID) allows the server to be
    identified when multiple servers are active in the same deployment.

    It can be any unique string, but we recommend using the UUID standard
    format.

    When aggregating audit entries (logs) or authentication requests from
    multiple servers, the UUID is used to identify the source server.

    UUIDs are intended to be used for low-level server implementations.
    For a human-readable name, please use the `name` attribute.

..  note::
    Once a UUID is defined, it is not recommended to change it.

    To generate a UUID value, please check the dedicated documentation for
    :ref:`admin-commands generate-uuid <generate-uuid>`.

    For more details, please check `Wikipedia's article on UUID
    <http://en.wikipedia.org/wiki/Universally_unique_identifier>`_.


name
^^^^

:Default value: ``single-server-name``
:Optional: No
:Values: * Human-readable name for this server.
         * This may be a fully qualified domain name (FQDN).
         * Any text.
:From version: 2.0.0
:To version: None
:Description:
    This is a human-readable companion for the UUID.

    As long as the UUID is not changed, you can change the name at any time,
    and the server will still be recognized in a multiple deployment
    architecture.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:Values: * Free form text describing this server.
:From version: 2.0.0
:To version: None
:Description:
    This can be used for any free form text attached to this server.
    It can include contact information about the system administrator, comments
    or other details specific to the installation.


account
^^^^^^^

:Default value: ``sftpplus``
:Optional: Yes
:Values: * A user under which the server will operate.
         * `Disabled` - if the server should use the same user as the one
           used to launch the server process.
:From version: 1.6.0
:To version: None
:Description:
    This is a system account used by the server to run its main operations with
    restricted privileges on Unix-like systems.

    To disable running the server under a dedicated account, set this value
    to `Disabled`.

..  note::
    This option is ignored on Windows systems, where the server will operate
    under the same account as the one used for starting the server.


execute_at_startup
^^^^^^^^^^^^^^^^^^

:Default value: `Disabled`
:Optional: Yes
:Values: * Path to an external script or executable which will be called
           at server's start.
         * `Disabled` - no command will be executed.
:From version: 1.7.0
:To version: None
:Description:
    Specifies the external executable or script to be executed just after
    the server starts.

    Set it to `Disabled` not to run any command.

    This can be used, for example, on Windows operating systems, to map network
    drives.
    The server comes with an example script::

        [server]
        execute_at_startup = execute_at_startup.bat

    The command will be executed under the account launching the server and
    not under the account defined by the 'account' option.


umask
^^^^^

:Default value: ``022``
:Optional: Yes
:Values: * Filemask in octal format.
:From version: 1.7.0
:To version: None
:Description:

    User mask file permissions (filemask) used for creating
    new files and folders on the server.

    When creating new files, the server will use the 0666 mode, masked with
    the value of umask.

    When creating new folders, the server will use the 0777 mode, masked with
    the value of umask.

..  note::
    This option is ignored on Windows systems.


authentications
^^^^^^^^^^^^^^^

:Default value: `DEFAULT-AUTHENTICATION`
:Optional: Yes
:Values: * List of authentication UUIDs.
:From version: 2.10.0
:To version:
:Description:
    Comma-separated list of UUIDs with global authentication methods enabled on
    this server.

    The list should be ordered by priority.
    The server will try to use the first authentication from the list, and
    continue with the next method if the user is not accepted.

    When not present, it defaults to the SFTPPlus embedded authentication.

..  note::
    When a service defines its own authentication list, this global
    configuration is ignored.


manager_authentications
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `DEFAULT-AUTHENTICATION`
:Optional: Yes
:Values: * List of authentication UUIDs.
:From version: 3.37.0
:To version:
:Description:
    Comma-separated list of UUIDs with authentication methods to be used
    for authenticating the administrators for the Local Manager service.

    The list should be ordered by priority.
    The server will try to use the first authentication from the list, and
    continue with the next method if the user is not accepted.

    When not present, it defaults to the SFTPPlus embedded authentication.


password_minimum_strength
^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `4`
:Optional: Yes
:Values: * 0
         * 1
         * 2
         * 3
         * 4
:From version: 3.43.0
:To version:
:Description:
    This defines the minimum strength element of the password policy
    applied when setting passwords through Local Manager.

    This does not enforce the policy for already defined passwords or
    for passwords defined outside of SFTPPlus, such as OS passwords.

    The available values are from `0` to `4` where `0` is a weak password
    while `4` is a password which is considered strong.

    The following minimum lengths are defined for each strength level:

    * 0 - no length limit.
    * 1 - 4 characters
    * 2 - 7 characters
    * 3 - 9 characters
    * 4 - 11 characters


password_minimum_length
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `8`
:Optional: Yes
:Values: * Number
:From version: 3.43.0
:To version:
:Description:
    This defines the minimum length element of the password policy
    applied when setting passwords through Local Manager.

    This does not enforce the policy for already defined passwords or
    for passwords defined outside of SFTPPlus, such as OS passwords.

    Set it to `0` to disable password length checking.
