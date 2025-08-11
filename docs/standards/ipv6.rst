.. container:: tags pull-left

    `server-side`
    `client-side`
    `configuration`


IPv6 Support
############

..  contents:: :local:


Introduction
============

SFTPPlus supports listening on IPv6 addresses for incoming SFTP, SCP, FTP,
FTPS, HTTP and HTTPS file transfer connections.

IPv6 addresses can also be used for the Web Manager GUI.

The types of IPv6 addresses that are supported are long form addresses::

    1111:2222:3333:4444:5555:6666:7777:888

And short form addresses such as::

    1111::7777:888


Server Side Connections
=======================

When a file transfer service is configured to listen on an IPv6 address,
it will only accept connections from IPv6 clients.

To support IPv6 and IPv4 clients, you will need to set up 2 separate services,
one for IPv6 and another one for IPv4.

..  FIXME:4811:
    Remove once IPv6 hostnames are supported.

For now, only IPv6 address literals are supported.
SFTPPlus cannot listen to FQDN resolving to an IPv6 address.
This is a known issue and will be fixed in the following releases.
Please get in touch if you need this functionality.

..  note:
    On some operating system, for example Linux,
    listening to `::` IPv6 will also enable support for transitional IPv4
    and will accept connections form IPv4 clients.


Transition from IPv4
====================

On certain operating systems such as Linux, when a service is listening on
the `::` IPv6 address, it will also accept IPv4 connections.
These connections are recorded in the audit log using an
IPv4-mapped to IPv6 an address.
For example, for a client connection from address 192.168.1.48 to port 53260,
the recorded peer would be `::ffff:192.168.1.48:53260`.
