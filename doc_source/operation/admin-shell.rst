Command-Line Administration-Shell
=================================

..  contents:: :local:


Introduction
------------

A command-line shell is provided to access the SFTPPlus management interface.

It is recommended to start the shell from the SFTPPlus installation folder.

On Unix-like systems, the `admin-shell` is available as::

    $ cd /opt/SFTPPlus
    $ ./bin/admin-shell.sh

On Windows systems, the `admin-shell` is available as::

    CMD> cd "C:\Program Files\SFTPPlus"
    CMD> admin-shell.bat

All Unix-like and Windows versions provide the
same command-line arguments and shell commands.
We use the generic `admin-shell` name for both types of executable files.

All commands to be executed in the administration's shell are prefixed with::

    >

The `admin-shell` script is provided as a tool to help with troubleshooting or
administrative tasks, without requiring an external tool.

In the case that you are using or planning to use `admin-shell` in
production, your feedback and comments are welcome.
They help us improve it and extend the scope of its usage.


Connecting to the management interface
--------------------------------------

The default `admin-shell` command will try to connect to the SFTPPlus
administration interface running at `https://localhost:10020` using the
default `configuration/self_signed_certificate.pem` certificate.

You can specify a different address for the SFTPPlus Local Manager interface
by setting it as a command line argument.

On Unix-like systems, the command would be::

    $ ./bin/admin-shell.sh -a https://sftp-mgmt.example.com:2020

On Windows systems, the command would be::

    CMD> bin\admin-shell.bat -a https://sftp-mgmt.example.com:2020

If the SFTPPlus Local Manager interface is not using the default
self-signed certificate, you can start `admin-shell` using a different
certificate. This can be the server's certificate itself or a Certificate
Authority's certificate.

    $ ./bin/admin-shell.sh -c /path/to/your/CA-or-server-cert.pem


Shell operation
---------------

When the `admin-shell` script is started, it will attempt to connect and
authenticate to the SFTPPlus management interface.

If no administrator name or password was provided as command line arguments,
`admin-shell` will ask for these details.

Upon a successful connection you will see a prompt such as::

    Administrator name: admin
    Password: PASSWORD-NOT-ECHOED
    Connecting to https://localhost:10020 as admin.
    Connected.
    SFTPPlus (3.47.0) command line administration shell
    >

After that, you can start entering `admin-shell` commands.
To show all available commands::

    > help

To find more details about a command::

    > help COMMAND_NAME

For example, to show more details about the command `show`::

    > help show


Scripting integration and password security
-------------------------------------------

The `admin-shell` can be integrated in scripts by having all the options and
command passed via the command line arguments.

It can read the password from the following sources:

* interactive without echo (safe): `admin-shell`
  (without any password argument)
* direct command line argument: `admin-shell -p YOUR-PASSWORD`
* file at a path defined via command line argument:
  `admin-shell -p /path/to/your/password/file`
* piped from another command: `echo YOUR-PASSWORD | admin-shell -p -`

You should replace `echo "YOUR-PASS"` with your password manager.
We used `echo` just as an example.

On Unix-like systems, the command would look like this. ::

    $ echo "YOUR PASS" | ./bin/admin-shell.sh -u admin -p - show failures
