Syslog
======

To configure an event handler which sends events to a Syslog server, use
the type `syslog`.

..  contents:: :local:


Introduction
------------

It can send logs to a local Unix socket, for example ``/dev/log``, or to a
remote ``IP:PORT`` address.

All messages are logged with the ``daemon`` facility and ``info`` severity.
They are formatted conforming to
`RFC 3164 <https://tools.ietf.org/html/rfc3164>`_, also known as syslog-bsd.
Messages can be plain 7-bit ASCII or UTF-8 encoded.

The process name used when formatting the message is configurable via the
[server] option.

When using TCP and the connection to the server is lost, it will try to
reconnect and will not handle any event until the connection is established.

.. include:: /configuration-events/events-commons.include.rst


url
---

:Default value: Empty
:Optional: Yes
:From version: 3.8.0
:Values: * `file://some-relative/path`
         * `file:///an/absolute/path`
         * `tcp://address:port`
         * `tcp://address`
         * `udp://address:port`
         * `udp://address`
:Description:
    This option specifies the location of the Syslog server.

    It supports local Unix domain sockets defined as relative or absolute paths,
    as well as TCP or UDP addresses.
    The `file://PATH` configuration is only supported on Linux and macOS.

    UDP support is implemented based on
    `RFC 5424 <https://tools.ietf.org/html/rfc5424>`_.
    When no port is specified for UDP, it will use `514` as the default port.

    TCP support is implemented based on
    `RFC 6587 <https://tools.ietf.org/html/rfc6587>`_
    When no port is specified for TCP, it will use `601` as the default port.
