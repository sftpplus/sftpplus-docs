IBM MQ Transfers
================

..  contents:: :local:


Overview
--------

This page describes how to configure SFTPPlus to transfer files
using IBM MQ channels.

Check the separate :doc:`reference documentation for IBM MQ</configuration-client/ibm-mq>`,
which describes all the configuration options available for a `ibm-mq` location.

A single location can be used with multiple queues,
including for sending or receiving files.

SFTPPlus will try to interact with an IBM MQ channel as it would with a file system.
Operation like listing queues, listing messages in a queue, uploading or downloading files are supported.

The IBM MQ location is designed to work with queues for which only the `PUT` or `GET` permissions are available.
The `BROWSE` permission is not required.

The current version of SFTPPlus only supports point-to-point scenarios.
Files can be sent to and received from a specific queue,
with the option of using separate queues for sending and receiving files.

The IBM MQ C Client version 9.4.3.1 is included with SFTPPlus.
You don't need to download or install it separately.


Limitations
-----------

* Only queues are supported.
  Sending and receiving messages using topics,
  in a publish/subscribe scenario are not yet supported.
  Get in touch with our support team if you need this feature.
* IBM MQ does not support streaming messages.
  The entire file content must fit into a single message.
  The maximum message size depends on the queue manager configuration.
  The default value is 4 MB.
  Check the `IBM MQ documentation <https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=queue-handling-messages-greater-than-4-mb>`_ ,
  or contact your IBM MQ administrator for more details.
* SFTPPlus uses the IBM MQ C Client library to connect to the queue manager.
  The error messages are limited to what is available from this library.
  For more detailed error messages, check the queue manager logs on the IBM MQ server.
* A unique queue should **only be accessed via a single location**.
  Accessing the same queue from multiple locations is not supported.
* Only Windows X64 and Linux X64 are supported.
* Windows Server Core or Windows Server Nano are not supported.
* File rename operation, creating or removing queues are not supported.
* All messages are transferred in binary mode, with persistence enabled.
* Messages are sent with CCSID set to 1208 (UTF-8).
  Contact us if you need support for other encodings. [#7221]
* All IBM MQ locations should use the same value for `idle_connection_timeout`.
  This is a limitation of the IBM MQ C Client library, that SFTPPlus uses.

.. _file-name-template:


Message queue to file path mapping
----------------------------------

SFTPPlus will try to map the file content stored in message queues to files in a directory structure.
The mapping is done using the following rules:

* Each queue is considered to be a separate directory.
* The queue name is used as the directory name.
* The file name is generated from a message property,
  using the `file_name_template` configuration option.
* The final file path is constructed as `<queue_name>\\<file_name>`, using Windows path separator. The Unix '/' separator is a valid character in queue names.
* The leading `\\` path separator should not be used in the queue name.
  The path should start with only the queue name.
* If the queue name contains the `/` (slash) character, it is replaced with the `-` (dash) character.
  This is to avoid generating sub-folders.

The following placeholders are available for the `file_name_template` configuration option:

* `{now.cwa_14051}` - Human readable date and time
* `{now.iso_8601}` - ISO 8601 date and time
* `{now.iso_8601_fractional}`
* `{now.iso_8601_local}`
* `{now.iso_8601_basic}`
* `{now.iso_8601_compact}` - ISO 8601 compatible with Windows file names
* `{now.timestamp}` - Unix timestamp
* `{metadata.message_id}`
* `{metadata.queue_name}` - Name of the queue over which the message was received.
* `{metadata.correlation_id}`
* `{metadata.priority}`
* `{metadata.user_identifier}`
* `{metadata.put_application_name}`
* `{metadata.put_date}`
* `{metadata.put_time}`
* `{metadata.reply_to_queue}`
* `{metadata.reply_to_queue_manager}`
* `{metadata.character_set}`

For example, with the default template value of:

  file_name_template = {metadata.user_identifier}-{metadata.queue_name}-{now.timestamp}.ibmmq

a message received from the `MY.QUEUE` queue,
by a remote application name `myapp` channel,
at Unix timestamp `1677621234`
will be handled as file name:

  myapp-MY.QUEUE-1677621234.ibmmq

When failing to generate the file name from the message metadata,
SFTPPlus will store the file using a temporary file name,
in the format `tmp-<UUID4>.tmp`.
By default, this file is available for automated transfer.

..  note::
    If you want to avoid transferring such files,
    configure the transfer to filter out files matching the `tmp-*.tmp` pattern.
    You will then need to manually investigate and rename such files before transferring them.


Discovery of queues available for transfers
-------------------------------------------

As part of your IBM MQ setup you might have many queues,
not all of them being used by SFTPPlus for file transfers.

You can use to directory listing operation on the root directory,
to discover all the queues available for the authenticated user.

You can also use generic queue names filter to show only a subset of the queues.
A generic name is a character string followed by an asterisk (`*`),
for example ``ABC*``, and it selects all objects having names that start with the selected character string.
An asterisk on its own matches all possible names, and is equivalent to not using a filter at all.


Receiving messages from a queue
-------------------------------

For receiving messages from the queue,
SFTPPlus is designed to work with queues for which only the `GET` permission is available.

This means that SFTPPlus will not try to `BROWSE` the messages in the queue.
When SFTPPlus tries to get a message from the queue,
the message is removed from the queue.

No content conversion is done on the message content.
The content is received as binary data.

Since the message can fail to be delivered to the final destination,
SFTPPlus will store the message in a temporary directory first,
before trying to deliver it to the destination location.

SFTPPlus will store up to **1500 messages** in the temporary directory,
before pausing to get more messages from the queue.
This is to avoid filling up the disk space on the server, and also to let the queue manager know that SFTPPlus can't process more messages at this time.

Once the messages are successfully delivered to the destination location and removed from the temporary directory,
SFTPPlus will *automatically* continue to get more messages from the queue.

The temporary directory is found in the SFTPPlus installation directory,
under the `run/<LOCATION_ID>` path.

..  warning::
    Files from the temporary directory are automatically removed only when the transfer is configured to delete the source file after a successful transfer.

    Otherwise, the files in the temporary directory are not automatically removed and you will need to manually remove them.

    If the location is removed, the temporary directory is removed, only if it is empty.


Sending messages to a queue
---------------------------

SFTPPlus will use the IBM MQ `PUT` operation to send messages to a queue.
The content of a message is not converted to a different encoding.
The encoding character set ID is set to `1208` (UTF-8).
Messages are sent with the persistence flag enabled.

The original file name is stored in the message `CorrelId` field.
Only the first 24 characters of the file name are used, as this is a limitation of the IBM MQ protocol.

Get in touch with our support team if you need to send messages using a different encoding or with different message properties.


IBM MQ server connection loss handling
--------------------------------------

When a connection loss is detected, based on the location's configuration,
SFTPPlus will attempt to reconnect to the IBM MQ server.

If the connection cannot be re-established after the maximum number of retries,
SFTPPlus will log an error and stop processing messages from the queue.

A person needs to investigate and resolve the connection issue,
and then manually restart the location from the SFTPPlus Web Manager.

There is a delay between the moment when the connection is lost
and the moment when SFTPPlus detects the connection loss.
This is defined by the IBM MQ heart beat mechanism, via the `HBINT` channel parameter,
since the IBM MQ protocol has it's own internal retry mechanism.

For SFTPPlus, the `HBINT` value is defined by the `timeout` configuration option.
The `HBINT` is defined by the IBM MQ server as part of the channel configuration.
The default value is usually 300 seconds (5 minutes).
You can check the value on your IBM MQ server using this command::

    DISPLAY CHANNEL(YOUR.CHANNEL.NAME) HBINT

The actual heartbeat interval used for the connection
is negotiated between the server and client,
being the larger value between the server's `SVRCONN` and the client's `timeout` value.
If the negotiated heartbeat interval is less than 60 seconds, the IBM MQ protocol will use a number of seconds double of that value to detect a timeout.
If the value is 60 seconds or more, the timeout detection interval is equal to the negotiated heartbeat interval plus 60 seconds.

You can read more about IBM MQ connection handling in the
`IBM documentation <https://www.ibm.com/docs/en/ibm-mq/9.2.x?topic=SSFKSJ_9.2.0/com.ibm.mq.con.doc/q015650_.html>`_.

..  note::
    Due to limitations of the IBM MQ C Client library,
    SFTPPlus can only detect a connection loss when trying to perform an operation.
    This means that if the connection is lost while SFTPPlus is idle,
    the connection loss will only be detected when SFTPPlus tries to get or put a message.
