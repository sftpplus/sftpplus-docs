Command-line client-shell
=========================

..  contents:: :local:


Introduction
------------

A command-line shell is provided to access remote file transfer servers using
an interactive interface.

On Unix-like systems, the `client-shell` is available as::

    $ ./bin/client-shell.sh

On Windows systems, the `client-shell` is available as::

    CMD> client-shell.bat

All Unix-like and Windows versions provide the
same command-line arguments and shell commands.
We use the generic `client-shell` name for both types of executable files.

All commands to be executed in the client's shell are prefixed with::

    >

The focus of our product is on providing tools for non-interactive
file transfers.
The `client-shell` is provided as a tool to help with troubleshooting or
administrative tasks, without requiring an external tool.

In the case that you are using or planning to use the `client-shell` for
production, your feedback and comments are welcome.
They help us improve the `client-shell` and extend the scope of its usage.

If you need an interactive file transfer client with a graphical user interface,
we suggest trying a better suited FTP/FTPS/SFTP/SCP client such as FileZilla,
WinSCP or Cyberduck.


Limitations
-----------

The `client-shell` is not intended for high-performance file transfers or large-scale operations.
It is designed to help with troubleshooting and implement simple batch scripts.

For full automation of file transfers you should use the automated SFTPPlus *transfers*.

Below is the list of current limitations:

* Only a single connection to a remote server is supported at a time.
* There is no support for remote to remote transfers.
* The SSH keys or TLS keys should be loaded without password protection.
* When connecting to a remote SFTP server, only a single server identity is supported.


Command-line arguments and shell options
----------------------------------------

The configuration options required to connect to a remote server (IP, port,
username, password, etc.) are available in the shell as `options` and on
the command-line as `arguments`.

To open a connection for user ``john`` outside the `client-shell`::

    client-shell --username john

To show all available command-line arguments outside the `client-shell`::

    client-shell --help

To set the username as ``john`` inside the `client-shell`::

    > set username john

To show all available options inside the `client-shell`::

    > show


Keyboard shortcuts
------------------

The following keyboard shortcuts are available. They try to follow the same conventions as the other Linux command-line tools:

* `Ctrl + r` - search the command history
* `Ctrl + w` - delete the word before the cursor
* `Ctrl + u` - delete the entire line before the cursor
* `Ctrl + k` - delete the entire line after the cursor
* `Ctrl + l` - clear the screen
* `Ctrl + d` - exit the shell (if the current line is empty)
* `Ctrl + a` - move the cursor to the beginning of the line
* `Ctrl + e` - move the cursor to the end of the line
* `Tab` - auto-complete commands and file paths
* `Up` - show the previous command in the history
* `Down` - show the next command in the history
* `Left` - move the cursor left
* `Right` - move the cursor right


Loading a configuration file
----------------------------

You can load the configuration for a location via the SFTPPlus main configuration file.

To load from the configuration file, you will need to provide the path to the configuration file and the UUID of the location::

    client-shell --config configuration/server.ini a5eacec-92f1-11f0-815a-bfa45

When loading from the configuration file, the following settings are reset:

* `connection_retry_count = 0`

Once the `client-shell` is started and the configuration is loaded, you can change the configuration options via the normal `set OPTION` command::

    client-shell --config configuration/server.ini a5eacec-92f1-11f0-815a-bfa45
    > show connection_retry_count
    0
    > set connection_retry_count 1
    > show connection_retry_count
    1

The `client-shell` is not an editor for the configuration file.
Changes made via the `set OPTION` command are not saved back to the configuration file.


Shell operation
---------------

When the `client-shell` is started, you will see a prompt such as::

    SFTPPlus (3.0.0) file transfer client shell
    >

After that, you can start entering `client-shell` commands.
To show all available commands, use::

    > help

To find more details about a command, use::

    > help COMAND_NAME

For example, to show more details about the command `open`, use::

    > help open

Command names are *case-insensitive*.
You can abbreviate the command names, as long as the abbreviation does not
conflict with another command name.
Shell options are *case-sensitive*.

For example, the following inputs will trigger the same command, namely
`connect`::

    > connect
    > CONNECT
    > Connect
    > con

When an abbreviation matches multiple commands, you will get an error::

    > c
    Abbreviation has multiple commands: close connect

Connections to remote servers are started using the `open` command and
closed using the `close` command.
After a connection is made, the shell can be used to issue file transfer
commands, such as `mkdir`, `rmdir`, `rm`, `mv`, `put`, `get`, etc.

Let's exemplify a connection to a SFTP server using connection options
specified as command-line arguments.
The following will open the connection, list the content of a folder, close the
connection, and then exit the `client-shell`::

    client-shell sftp://john@sftp-acct1.example.com:10022 \
    --ssh-server-fingerprint=06:cb:46:2b:9a:9a:c4:10:54:f0:ea:2f:b6:05:cb:a0 \
    --ssh-private-key=test_data/ssh/test-ssh-rsa-1024
    > open
    > ls
    > close
    > exit

The next example shows the same connection, with connection options
specified using `shell options`::

    client-shell
    > set protocol sftp
    > set address sftp-acct1.example.com
    > set port 10022
    > set username john
    > set ssh_private_key test_data/ssh/test-ssh-rsa-1024
    > set ssh_server_identity 06:cb:46:2b:9a:9a:c4:10:54:f0:ea:2f:b6:05:cb
    > open
    > ls
    > close
    > exit


File paths with spaces
----------------------

To handle paths with spaces, quote them using single quotes (`'`).
Double quotes (`''`) and backslash escaping (like ``some\\ space``) are not
supported.

Below is an example for moving a file between paths with spaces::

    client-shell
    > # Don't forget to set connection options.
    > open
    > mv 'source dir/source file' 'destination dir/target file'
    > close
    > exit


File upload / download operations
---------------------------------

The `client-shell` provides the equivalent `put` / `upload` commands for
uploading a file and the corresponding `get` / `download` commands for
downloading a file::


    client-shell
    > set protocol sftp
    > set address sftp-acct1.example.com
    > set port 10022
    > set username john
    > set password pass-for-johnny
    > set ssh_server_identity 6KCf6ey2Wp9pcaKVMFUd25PeHdP/O+xSAWnJYSgaS9Q=
    > open
    >
    > # Uploading a local file with a new name on the remote destination.
    > put path/to/local.file destination/remote.file
    > # Uploading a local file with the same name on the remote destination.
    > upload path/to/local.file
    >
    > # Downloading a remote file with a new name on the local destination.
    > get path/to/remote.file destination/local.file
    > # Downloading a remote file with the same name on the local destination.
    > download path/to/remote.file
    > close
    > exit


Connecting to multiple servers
------------------------------

During a `client-shell` session, you can issue commands to connect to more than
one server.
But only a single connection is active at one time.
Opening a new connection will automatically close a previous connection.

The next example shows a single shell session inside which two connections are
made to different servers::

    client-shell
    > set protocol sftp
    > set address sftp-acct1.example.com
    > set port 10022
    > set username john
    > set ssh_private_key test_data/ssh/test-ssh-rsa-1024
    > set ssh_server_identity gm1FRm5gr5gSFIXy80r4d+FLrgQ=
    > open
    > ls
    > close
    > set protocol sftp
    > set address sftp-vendors2.example.com
    > set port 22
    > set username actpd
    > set password sd!ds21p
    > open
    > ls
    > close

After the `client-shell` is started with a configuration file,
you can also switch the configuration for another location::

    client-shell --config configuration/server.ini a5eacec-92f1-11f0-815a-bfa45
    > show protocol
    protocol: sftp
    > set uuid e88f45a6-92f3-11f0-9bb6-63760a893d3f
    > show protocol
    protocol: sharepoint-online


Batch mode
----------

The `client-shell` can read commands and options from a plain text file.
We call this a `batch file`.

Each command in a batch file should be put on a separate line.
Lines starting with `#` are considered comments and ignored.
Empty lines are also ignored.

After processing the last line, the `client-shell` will exit.

Here is an example of a batch file to connect to a remote server and
list the content of its root directory::

    # Server for accounting. This is a comment.
    set protocol sftp
    set address sftp-acct1.example.com
    set port 10022
    set username john
    set ssh_private_key test_data/ssh/test-ssh-rsa-1024
    set ssh_server_identity 06:cb:46:2b:9a:9a:c4:10:54:f0:ea:2f:b6:05:cb

    open
    # List root directory. A comment which is ignored.
    ls
    close

To run the `client-shell` in batch mode, use::

    client-shell --batch path/to/batch/file


Reading client-side events
--------------------------

The SFTPPlus client-side implementation will emit all events relating to the
client-side activity.
The events can be used for logging or for hooks in other managed file transfer
workflows.

See below for client-side events relating to a file that does not exist::

    | > get file_does_not_exist.pdf
      60053 2017-08-14 14:06:43 Process Process 0.0.0.0:0 Successfully opened
      "file_does_not_exist.pdf" for reading on "ftp".
    | 60036 2017-08-14 14:06:43 Process Process 0.0.0.0:0 Failed to close
      "file_does_not_exist.pdf" on location "ftp". Was opened for reading.
      ['550 File not found']

See below for the corresponding server-side events from a third-party server::

    | (000020)8/14/2017 14:06:43 PM - support_team (127.0.0.1)>
      RETR file_does_not_exist.pdf
    | (000020)8/14/2017 14:06:43 PM - support_team (127.0.0.1)>
      550 File not found


Azure Files, Sharepoint, and other cloud services
-------------------------------------------------

The Azure Files cloud storage service is accessed over HTTPS using the fixed
port 443 and an address automatically generated based on the account name.

Below is an example of connecting the storage account named ``stciv1`` using
a password which is securely entered at runtime::

    $ ./bin/client-shell.sh azure-file://stciv1@address-ignored -p

    Password: ENTER YOUR PASSWORD HERE

    SFTPPlus file transfer client shell
    > connect

SharePoint Online always uses the HTTPS protocol.
The URL is configured to your SharePoint Online site or sub-site::

    $ ./bin/client-shell.sh sharepoint-online://YOUR-DOMAIN.sharepoint.com/sites/YOUR-SITE/OR-SUBSITE
