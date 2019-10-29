Services
========

..  contents:: :local:


Listening on ports below 1024 on Linux and macOS
------------------------------------------------

Under normal circumstances, the default configuration for a Unix-like operating
system is to only allow the root account to listen on ports below 1024.

Yet, with extra configuration it is possible for normal (non-root) accounts
to listen to ports below 1024.

One generic method which works on any Unix-like system is to set up
SFTPPlus to listen on a port above 1024 and then set up port-forwarding
in the firewall configuration.

Another method is to use the privileges framework provided by some
operating systems.
The required configuration is specific to each OS that has such a feature.
In this section, our goal is to guide you through this configuration process.
We do not aim to provide a comprehensive documentation for each operating
system.
For more details, please consult the dedicated documentation available for
your Linux distribution or macOS version.

..  note::

    Some operating systems don't provide any fine grained permissions
    configuration, so using the port-forwarding is the only option.

    In the case in which you know how to configure macOS to
    listen on a port below 1024 without firewall redirection, please let us
    know and we will improve this documentation.


Linux
^^^^^

The method based on which a non-root user is granted permissions to listen on
port 1024 is called `capabilities` and `cap_net_bind_service` is the
capability which controls the port listening permissions.

For more details, please see `man 7 capabilities` on your operating system.

The capabilities are associated to a process and a dedicated command line tool
is required to configure the capabilities for a process.

On some Linux distributions, you might need to install an extra package to have
these tools available.

To allow the SFTPPlus process to listen on ports below 1024, the command
will look similar to the following example::

    $ sudo setcap 'cap_net_bind_service=+ep' SFTPPLUS_INSTALL_PATH/bin/python

You can then start SFTPPlus as non-root user and listen on ports below 1024.


macOS
^^^^^

The method used is port-forwarding using `pf`.

Set up SFTPPlus to listen on a port above 1024 and configure the port
forwarding.


We will use the loopback interface to keep things simple,
but you should adapt and extend these firewall rules to account for
your own local configuration: different network interfaces,
IPs and other network traffic rules.

Step-by-step instructions on how to forward port 122 to 10022::

    Create a pf anchor file for sftpplus in /etc/pf.anchors/sftpplus
    with the following contents:
        rdr pass on lo0 inet proto tcp from any to 127.0.0.1
        port = 122 -> 127.0.0.1 port 10022
        (note the above 2 lines go into only one line, it has been
        split here for better readability)

    Reference anchor in /etc/pf.conf, add:
        rdr-anchor "sftpplus"
        load anchor "sftpplus" from "/etc/pf.anchors/sftpplus"

    Enable and reload pf manually:
        $ sudo pfctl -ef /etc/pf.conf

    Note: Updates to the OS may override the pf.conf file, make sure to
    make a backup of it.


Removing services while server is running
-----------------------------------------

A service can be removed while the server is running,
without affecting the other available services.

This can be done via the Local Manager.

When a service is removed and the service has been running, it is automatically
stopped.
