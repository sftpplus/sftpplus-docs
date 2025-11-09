IBM MQ Channel
==============

..  contents:: :local:


Introduction
------------

An `ibm-mq` location provides access to queues hosted on an IBM MQ server,
using a specified channel.

This page is the reference documentation for the configuration options available for an `ibm-mq` location.
For more information about how to implement IBM MQ based transfers,
see the separate documentation page for :doc:`implementing IBM MQ based transfers</operation-client/ibm-mq>`.


name
----

:Default value: Empty
:Optional: No
:From version: 5.19.0
:Values: * Any text.
:Description:
    Human-readable short text used to identify this location.


description
-----------

:Default value: Empty
:Optional: Yes
:From version: 5.19.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this location.


address
-------

:Default value: Empty
:Optional: No
:Values: * Host name
         * IP address
:From version: 5.19.0
:Description:
    Address of the IBM MQ endpoint server. IP or DNS name.


port
----

:Default value: 1414
:Optional: Yes
:Values: * Number, greater than 0.
:From version: 5.19.0
:Description:
    Port number of the IBM MQ endpoint server.


queue_manager
-------------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 5.19.0
:Description:
    Name of the queue manager to connect to on the IBM MQ server.


channel
-------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 5.19.0
:Description:
    Name of the channel to use for accessing the queues on the IBM MQ server.

    The same channel can be used with multiple queues.

    In general, IBM MQ channel names are limited to 20 characters.


username
--------

:Default value: Empty
:Optional: No
:From version: 5.19.0
:Values: * Text.
:Description:
    Username used to authenticate to the IBM MQ server.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 5.19.0
:Values: * Plain text password.
         * Empty.
:Description:
    This option specifies the password used to connect to the IBM MQ server.
    It is provided in plain text.


file_name_template
------------------

:Default value: `{metadata.user_identifier}-{metadata.queue_name}-{now.timestamp}.ibmmq`
:Optional: No
:From version: 5.19.0
:Values: * Text
:Description:
    Template used to generate the file name for files received from the IBM MQ server.

    Check :doc:`IBM MQ transfers</operation-client/ibm-mq>` documentation page for more information about the available options and usage.


timeout
-------

:Default value: `120`
:Optional: Yes
:Values: * Number of seconds.
:From version: 5.19.0
:Description:
    Duration, in seconds, to wait for a response from the server.

    If a response is not received during this period, the connection is considered lost.

    This value is also used to configure the IBM MQ heartbeat interval (HBINT).
    The HBINT is negotiated to the larger value between the server's `SVRCONN` and this `timeout` client-side value.
    The default `HBINT` for IBM MQ servers is `300` seconds.
    This means that if `timeout` is less than the value configured on the server,
    this configuration option is ignored and the server timeout value is used instead.


idle_connection_timeout
-----------------------

:Default value: `300`
:Optional: Yes
:From version: 5.19.0
:Values: * Number of seconds
         * 0
:Description:
    Number of seconds to wait for messages to be received from the queue.
    If no message is received in the configured interval, the connection is closed.

    Set to `0` to disable the timeout and always keep the connection open.
    If the connection is lost, SFTPPlus will try to reconnect immediately.


idle_connection_keepalive_interval
----------------------------------

:Default value: `0`
:Optional: Yes
:From version: 5.19.0
:Values: * Number of seconds
:Description:
    How often to send a `PING` message to the IBM MQ server to help keep the connection alive.


connection_retry_count
----------------------

:Default value: `12`
:Optional: Yes
:From version: 5.19.0
:Values: * Number of retries
:Description:
    Number of times to retry connecting to the location.

    Set to `0` to not retry.

    When the connection still fails after all the retries,
    the location is marked as `failed` and no re-connections or transfers are attempted.
    An administrator needs to review the error, fix the issue, and manually restart the location.


connection_retry_interval
-------------------------

:Default value: `300`
:Optional: Yes
:From version: 5.19.0
:Values: * Number of seconds
:Description:
    Number of seconds to wait between connection attempts.

    Set to `0` to retry right away without any delay.


ssl_cipher_spec
---------------

:Default value: `ANY`
:Optional: Yes
:From version: 5.19.0
:Values: * IBM MQ cipher specification string.
         * `ANY`
         * `ANY_TLS12`
         * `ANY_TLS13`
         * `ANY_TLS12_OR_HIGHER`
         * `ANY_TLS13_OR_HIGHER`
:Description:
    This depends on the TLS cipher configured on the server.
    For more details see the `IBM MQ TLS CipherSpecs <https://www.ibm.com/docs/en/ibm-mq/9.4.x?topic=jms-tls-cipherspecs-ciphersuites-in-mq-classes>`_ documentation.

    As an example, you can use `ANY_TLS12` to accept only TLS 1.2 cipher,
    or use `ANY_TLS12_OR_HIGHER` to accept TLS 1.2 or 1.3.


ssl_trusted_certificates
------------------------

:Default value: Empty
:Optional: Yes
:From version: 5.19.0
:Values: * PEM encoded certificate authority.
         * Empty.
:Description:
    PEM encoded certificate authorities used to validate the server identity.

    You need to provide the full certification authority chain.

    For self-served certificates, provide the self-signed certificate.

    Leave this empty to not use TLS when communication with the IBM MQ server.


ssl_client_certificate
----------------------

:Default value: Empty
:Optional: Yes
:From version: 5.19.0
:Values: * PEM encoded client certificate and key.
         * Empty.
:Description:
    PEM encoded client certificate and client private key used for mutual TLS authentication.

    The private key should be configured without password encryption.

    Leave it empty to not use mutual TLS.
