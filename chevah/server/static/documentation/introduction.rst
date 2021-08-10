Introduction
============

SFTPPlus allows, from the server perspective, remote file transfer clients to
be securely authenticated and authorized for accessing files located on local
file systems or remote file systems (CIFS/NFS) used by the operating system
running SFTPPlus.

From the client perspective, it connects to remote file transfer servers to
perform file transfer operations.

SFTPPlus is specially designed to run on multiple operating system
platforms.
In the case that you are looking for an operating system not listed
in the :doc:`Supported Operating Systems<installation/requirements>` section,
please let us know.
It is very probable that SFTPPlus already works on that OS.
SFTPPlus is built on top of
`C Python 2.7 <http://en.wikipedia.org/wiki/CPython>`_ and
`Twisted Matrix <http://twistedmatrix.com>`_.

It is designed to be totally automated, prompt-less, and without interaction.
Once installed and configured properly, it should operate in the
background and need no direct attention from the user or the administrator.

SFTPPlus is now what is called a Managed File Transfer (:ref:`MFT<term-mft>`)
software.
Formerly it was a client/server setup with two separate downloads / installs /
configurations.
This change occurred at version 3.0.0 (current version: |version|).
You can read about the changes in the software over the course of time in the
:doc:`Release Notes</release-notes>`.

When interacting with file transfer clients, SFTPPlus implements
standardized and de-facto file transfer protocols.
The server can interact with any file transfer client that is compliant with
one of the supported file transfer protocols:

* FTP
* FTPS Explicit (AUTH TLS/SSL)
* FTPS Implicit
* SFTP
* SCP (see note)
* HTTP
* HTTPS

All standard file management operations are implemented (upload, download,
delete file, delete folder, create file) across all supported protocols.
The server also provides protocol-specific commands, as described in
the protocol's standard specifications (RFCs).


Guidance for reading the documentation
--------------------------------------

We use the following methods for highlights:

A note supplements and highlights additional information.
When ignored, the information presented here will not have any
negative consequences.
Below is an example of a note message.

..  note::
    It is highly recommended to define an explicit group
    (other than the `DEFAULT_GROUP`) for each application account.
    This will make the configuration file much easier to understand by removing
    any implicit behaviour associated with an unspecified group.

A warning is information which should not be ignored.
The information should be understood, as otherwise it can lead to
irreversible actions and undesirable consequences.
Below is an example of a note message.

..  warning::
    Depending on your architecture, this could change the service to make the
    default administrative account accessible over the Internet.
    Care must be taken to ensure that the default administrative account is
    altered or deleted.

You will notice certain terms will be colour-coded `grey` or ``blue``.

`Verbatim` values represent terms which should be used exactly as documented.
For example, a configuration option such as `home_folder_path` is a verbatim
value.
It also describes fixed values like `disabled`, `yes` or `no`.


The ``Input`` values serve as an example and we expect them to be altered
before being used in a certain configuration.

For example, ``c:\Path\${USER}`` is expected to be modified to suit the
environment used by a specific deployment, like **E:\FTP-Files\${USER}**.

In the documentation you will find scripts,
text configuration examples and commands to
provide further guidance to our readers.

Example of system administrator commands::

    $ ./bin/admin-commands.sh start --configuration non-root-server.ini
    # ./bin/admin-commands.sh start --configuration root-server.ini
    CMD> service-start.bat --configuration windows-server.ini

Example of a single configuration option defined inside our configuration
file::

    [section-name/03288e36-cf6b-4bd5-a9be-f421372f17e6]
    rotate_count = 5

Example of a command sent to our interactive client shell::

    > set username mary

Example of code in the developer documentation::

    {
      "account": {
        "home_folder_path": "/local/path/for/account",
        "uuid": "ebfbee04-17be-4d9f-b7fc-20ffed6a61a8",
        "create_home_folder": true,
        "create_home_folder_owner": "ude_team",
        "create_home_folder_group": "partners"
        "home_folder_structure": [['/some-child'], ['/another-child']]
        }
    }


Product development
-------------------

For the SFTPPlus development operations, security, correctness, easy-of-use, and
high functionality are all important factors and we focus on them in this
order.

To assure correct functionality of SFTPPlus, we are continually re-building
the product after each change and run an automated test suite.
The software is tested at the source code level as well as at the system level
on all supported operating systems and hardware architectures.

..  note::
    We are constantly updating our Python distribution to include both security
    and performance fixes.

    Please get in touch with us if you want to know specific details about
    your OS or consider an upgrade critical and we haven't provided it.
