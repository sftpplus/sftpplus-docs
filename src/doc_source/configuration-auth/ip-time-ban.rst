Banning IP addresses
====================

An `ip-time-ban` authentication method can be used to block/deny
authentication requests coming from a specific IP address if they generate
a number of consecutive authentication failures.
This option can be used to help mitigate DDOS attempts to SFTPPlus services.

..  contents:: :local:


Introduction
------------

The ban is active for a time interval, after which authentication requests
made from the IP address are accepted again.

When the authentication method is restarted it will reset its internal
record of source IP addressed which have previously generated failed
authentication requests.

When the same authentication method is used for multiple file transfer services
and the Local Manager services, it will use a single internal state for
each username.
Multiple consecutive authentication failures for different services have the
same effect as multiple consecutive authentication failures for the same
service.

..  note::
    Add this authentication method as the first one in the list of
    active authentication methods to make sure the users are not
    accepted earlier by other authentication methods.

..  warning::
    SFTPPlus is behind a load balancer, make sure that Proxy Protocol version 2
    is enabled on both the load balancer and SFTPPlus file transfer services.
    Otherwise all the authentication requests will be made using the
    load balancer own IP address and not the client IP address.

..  warning::
    Do not use this method if SFTPPlus is behind a Proxy/Gateway or any other
    network device which does not preserve the source IP address of the
    initial authentication request or does not support Proxy Protocol v2

    The ban applies to the source IP address used to initiate the
    authentication requests.

    If SFTPPlus server is behind a Proxy/Gateway, all requests will come from
    the gateway's own IP address.

    Check that your network is not vulnerable to
    `IP address spoofing <https://en.wikipedia.org/wiki/IP_address_spoofing>`_
    .

.. include:: /configuration-auth/authentication-commons.include.rst


ban_interval
------------

:Default value: `3600`
:Optional: Yes
:Values: * Number of seconds.
:From version: 3.2.0
:Description:
    Number of seconds for which authentication requests from the source IP
    are denied.

    Default interval is 1 hour.


ban_after_count
---------------

:Default value: `5`
:Optional: Yes
:Values: * Number of failed attempts.
:From version: 3.2.0
:Description:
    Number of consecutive failed authentications which will result in blocking
    the source IP.
