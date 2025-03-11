RabbitMQ publisher
==================

The `rabbitmq` event handler is used to trigger an AMQP publish operation
based on an audit event.

It supports AMQP version 0-9-1.

..  contents:: :local:

.. include:: /configuration-events/events-commons.include.rst


url
---

:Default value: ''
:Optional: No
:Values: * `URL`
         * Comma separated list of URLs
:From version: 4.10.0
:Description:
    URL, without username and password for the RabbitMQ server.

    The username and password are configured as separate values for audit
    and security considerations.

    Use `amqp://host:port/virtual_host` for non-TLS connections.
    Use `amqps://host:port/virtual_host` for TLS connections.

    When `port` is not specified it will use port `5672` for non-TLS and
    port `5671` for TLS connections.

    When `virtual_host` is not specified, it will use the default virtual host.


username
--------

:Default value: ''
:Optional: No
:From version: 4.10.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote RabbitMQ server.


password
--------

:Default value: ''
:Optional: No
:From version: 4.10.0
:Values: * Plain text password.
:Description:
    Password associated with the configured `username`.


exchange
--------

:Default value: Empty
:Optional: Yes
:Values: * Text value
:From version: 4.10.0
:Description:
    The name of the exchange where messages are published.

    Leave it empty to use the default exchange.


routing_key
-----------

:Default value: Empty
:Optional: Yes
:Values: * Text value
:From version: 4.10.0
:Description:
    The value of the routing key used when publishing the message.

    In the most simple case, this is the name of a RabbitMQ queue.


payload_template
----------------

:Default value:
:Optional: No
:Values: * Static text value
         * Format string
:From version: 4.10.0
:Description:
    The payload of the published message itself.

    It can be a static text value used for all the events.

    You can also generate dynamic payloads based on event data.

    .. include:: /configuration/event-context-variables.rst.include


retry_count
-----------

:Default value: `2`
:Optional: Yes
:From version: 4.10.0
:Values:
    * 0
    * Positive integer
:Description:
    This is the number of times a failed connection or request or is retried.

    When set to `0`, requests are never retried.


retry_increase
--------------

:Default value: `10`
:Optional: Yes
:From version: 4.10.0
:Values:
    * 0
    * Positive real number
:Description:
    Number of seconds to add to each wait period before retrying.

    This is also the value of the first retry wait period.

    When set to `0`, there will be no waiting time, a retry is performed
    right away.


.. include:: /configuration/ssl-client.include.rst
.. include:: /configuration/ssl.include.rst
