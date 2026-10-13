SFTP / SCP Usage
================

..  contents:: :local:


Introduction
------------

This page contains information about using the SFTP / SCP file transfer
service.

Both SFTP and SCP operate over the Secure Shell (SSH) cryptographic
network protocol version 2.
Only SSH version 2 is supported by SFTPPlus.

The SCP implementation is based on reverse-engineering the `scp` command
tool provided by the OpenSSH project.

The SFTP implementation is based on the SSH File Transfer Protocol Draft 3
`draft-ietf-secsh-filexfer-3
<https://tools.ietf.org/html/draft-ietf-secsh-filexfer-03>`_ specification.

The SFTP and SCP protocols are layered on top of the generic SSH protocol for
which the general architecture is described in
`RFC 4251 <http://tools.ietf.org/html/rfc4251>`_

The following authentication methods are supported, as specified in
`RFC 4252 <http://tools.ietf.org/html/rfc4252>`_ : `password` and `publickey`.


File open mode
--------------

The SFTP protocol is more like a remote file system protocol and does not
provide high level commands for file `upload` or `download`.
Instead, it provides a wide range of primitive operations for remote files like
`open`, `read`, `write` and `close` commands.

When a file is opened or closed, the emitted event contains the opening mode of
the file.
The following modes are possible:

* `reading`
* `reading with append`
* `writing`
* `writing with append`
* `reading and writing`
* `reading and writing with append`

To help filtering the common operations, which are read and write,
dedicated event IDs are emitted when the file is closed while being opened
in read-only or write-only mode.


.. _operation-sftp-ssh-key-authentication:

SSH Key Authentication
----------------------

SFTPPlus supports SSH key authentication by reading SSH public keys in
OpenSSH format.

SSH keys are composed of the following 2 parts:

* `public`
* `private`

The server only needs to know about the `public` part of a SSH key.
As the name suggests, the `public` part can be shared with anyone and does
not require to be kept secret.
You can send it over unsecured communication channels like email (SMTP) or
HTTP.

The OpenSSH public key is defined in the following format::

    KEY-TYPE KEY-CONTENT [KEY-COMMENT]

* ``KEY-TYPE`` can be `ssh-dsa` or `ssh-rsa`
* ``KEY-COMMENT`` is an optional text and needs to be placed on the same line.

Example::

    ssh-rsa AAAAB3_CONTENT_OF_THE_KEY_OqLrL8bfLCu/ description

The private part should always stay on the client side and never be
sent to the server or to other parties.
In terms of protecting the private part, you should follow the same
procedures as for a plain text password.

Example of unencrypted OpenSSH private key::

    -----BEGIN RSA PRIVATE KEY-----
    MIICWwIBAAKBgQC4fV6tSakDSB6ZovygLsf1iC9P3tJHePTKAPkPAWzlu5BRHcmA
    MORE-KEY-CONTENT-HERE
    LqHYUobNanxB+7Msi4f3gYyuKdOGnWHqD2U4HcLdMQ==
    -----END RSA PRIVATE KEY-----

To improve security while moving private SSH keys, there is the option
to encrypt them, using a password.
Note that the password is only used for storing the key on disk.
When the key is used by an SSH application, it needs to be decrypted first.

For non-interactive SSH applications (e.g. SSH / SFTP / SCP server or automated
SSH / SFTP / SCP client), where there is no person to type the password from
memory, in order for the application to read the key, it needs access to the
plain text password.
Since the password is stored together with the associated encrypted key, this
leads to the same security level as the unencrypted key.

Example of encrypted OpenSSH private key::

    -----BEGIN RSA PRIVATE KEY-----
    Proc-Type: 4,ENCRYPTED
    DEK-Info: AES-128-CBC,BCD9AB5C68DD1924FF2A1A54BE2A7BF4

    RAHH7yMbPk/vrhT5jkSDGIUdH+nG0OQpeSWcQXd4JJ6pqdJh/cw/havtxlHFp1yz
    MORE-KEY-CONTENT-HERE
    Pkf+23OGZln2dLz/pkJkiRRzmsWgT2hUv/EK4NYRQq1kEAXLf3J6xZqLlR3ZBLJm
    -----END RSA PRIVATE KEY-----

In a secure environment, the client will generate the private and public
keys on the same machine which uses them, and it will send only the
public part to the server.
This way, the private part never leaves the machine on which it is used,
greatly reducing the risk of revealing the key.

Putty Key format (.PPK) and
`RFC 4716 format <https://tools.ietf.org/html/rfc4716>`_ are not directly
supported, but you can use the SSH key conversion tools provided by the
Web Manager to convert those keys into OpenSSH public key format.

Further details on :doc:`configuring SSH key-based authentication on the server
</configuration-server/ssh-service>` is available.


User password change
--------------------

You can configure an account to allow updating its own password.
When enabled, the user can change its password over the SSH protocol
using the `passwd` command.

To change its password, a user must provide the current password.

When changing the password, both current and new passwords are provided in
text format.

The SCP and SFTP protocols do not provide a standard method for changing
a password.
The password is changed using the `exec` request of the SSH protocol.

Once the process to change the password is finalized, the SSH connection is
closed.

The password can be changes using any SSH client by invoking the command
without requesting pseudo-terminal allocation (tty allocation).

Here is an example of changing the current password
`correcthorsebatterystaple` to new password `Ltime@go-inag~faaa!`,
for user ``johnd`` using the OpenSSH command from Linux::

    $ ssh johnd@sftp.example.com passwd
    Current password: correcthorsebatterystaple
    New password: Ltime@go-inag~faaa!
    Confirm new password: Ltime@go-inag~faaa!
    Password successfully updated.
    $ echo $?
    0

If the password was successfully updated, the SSH client process will be
terminated with exit code 0 (zero).
If the password fails to be updated, the SSH client process exits with a
non-zero exit code.

On Windows, you can change the password using PuTTY's plink command.
Below is an example in which changing the password fails and the process
ends with exit code `1`::

    > plink -t user@localhost passwd
    Current password: some-password
    New password: new-password
    Confirm new password: new-password
    Failed to update password.
    > echo %ERRORLEVEL%
    1

..  note::
    The password cannot contain leading or trailing space or tab characters.


.. _operation-sftp-transfer-performance:

Transfer performance
--------------------

SFTP and SCP transfer speeds depend on the client, network, and storage.
On connections with high latency, SSH flow control can limit transfer throughput
even when the network has enough bandwidth.

Uploads and downloads have separate receive limits.
The receiver chooses how much data the sender can send before waiting for permission to send more.
This allowance is called the receive window.

For uploads, the client sends file data to the server.
The SFTPPlus SFTP/SCP server sets the receive window and maximum SSH packet size,
using the `ssh_window_size` and `ssh_maximum_packet_size` service options.

..  note::
    The client controls the receive window and maximum SSH packet size for file **downloads**.
    The `ssh_window_size` and `ssh_maximum_packet_size` service options
    therefore only tune file **upload** speed.
    To tune **download** performance, use equivalent receive-window and packet-size settings on the client.

A larger window lets the sender transmit more data while waiting for a window update from the receiver.
This can reduce pauses on connections with high latency.
It can also allow more data to arrive while earlier data waits to be written to disk.
A window update grants permission to send more data;
it does not confirm that the received file data has been written to disk.

..  warning::
    Buffering more data can increase memory usage for each file upload,
    especially when a slow disk or a slow connection to network storage delays writes.

Increase the `ssh_window_size` option first, before changing `ssh_maximum_packet_size`.
With the recommended `ssh_maximum_packet_size = 32768`, set `ssh_window_size` to at least 64 times `ssh_maximum_packet_size` (2 MiB).
This lets the client send 64 maximum-sized SSH packets before waiting for a window update.
It can also accommodate 66 parallel packets if some are smaller or the server replenishes the window while they are sent.
To send 66 maximum-sized packets without an intervening window update, use a window of at least 66 times the packet size.
The effect of parallel SFTP requests is discussed below.

To try a larger 4 MiB window, set `ssh_window_size = 4194304`
for the SSH service and test upload performance with the clients using it.
Keep `ssh_maximum_packet_size` at its default of 32 KiB for compatibility with older clients.
Clients can continue to send smaller packets,
and outgoing packet sizes are determined by the client's advertised limit.


Estimating throughput
^^^^^^^^^^^^^^^^^^^^^

An optimistic estimate of the receive-window throughput limit is
`window size / round-trip time`.
Use the server's receive window for uploads and the client's receive window for downloads.
Round-trip time (RTT) includes the journey to the server and back;
it is not the one-way network delay.
For example, a 128 KiB window at 10 ms RTT gives
`0.125 MiB / 0.01 seconds = 12.5 MiB/s`.

The following values are calculated examples, not measured transfer speeds.

..  list-table:: Receive-window throughput estimates
    :header-rows: 1

    * - Receive window
      - Maximum SSH packet
      - 10 ms RTT
    * - 128 KiB
      - 32 KiB
      - 12.5 MiB/s
    * - 128 KiB
      - 64 KiB
      - 12.5 MiB/s
    * - 2 MiB
      - 32 KiB
      - 200 MiB/s
    * - 2 MiB
      - 256 KiB
      - 200 MiB/s
    * - 4 MiB
      - 32 KiB
      - 400 MiB/s

At 100 ms RTT, divide these throughput estimates by 10.
For example, the estimate for a 128 KiB window drops from 12.5 MiB/s to 1.25 MiB/s.

Increasing the maximum SSH packet size does not necessarily improve transfer performance.
For uploads, the client can send multiple chunks, each no larger than this limit,
without waiting for confirmation after each chunk, as long as the server's receive window allows it.
A larger receive window lets more data be in transit or buffered in server memory,
which can reduce pauses and improve throughput.

SFTP clients also control their file block size and the number of outstanding requests.
Outstanding requests are file operation requests for which the client has not yet received a reply.
For example:

* WinSCP defaults to a limit of 32 outstanding download requests and 64 upload requests.
  These can be changed with the `SFTPDownloadQueue` and `SFTPUploadQueue` settings.
* FileZilla starts with a limit of 16 outstanding download requests
  and adjusts it automatically during the transfer.
* OpenSSH sftp defaults to a limit of 64 outstanding requests for uploads and downloads.
  For example, `sftp -R 128 user@server` raises this limit to 128.

The optimistic throughput limit from these requests is
`outstanding requests * file block size / RTT`.
At 10 ms RTT, the following examples assume the SSH window is large enough:

..  list-table:: SFTP request throughput estimates at 10 ms RTT
    :header-rows: 1

    * - Outstanding requests
      - File block size
      - Throughput estimate
    * - 1
      - 32 KiB
      - 3.125 MiB/s
    * - 32
      - 4 KiB
      - 12.5 MiB/s
    * - 32
      - 32 KiB
      - 100 MiB/s
    * - 64
      - 32 KiB
      - 200 MiB/s

The smallest limit determines the result.
For example, an upload with 64 outstanding 32 KiB requests at 10 ms RTT
is still limited to about 12.5 MiB/s by the server's 128 KiB receive window.
A 2 MiB window raises that estimate to 200 MiB/s,
but a 100 Mbit/s network link allows less than 11.9 MiB/s of file data after overhead.

Clients that send only one request at a time pause after each uploaded file chunk
while waiting for the server to confirm receipt.
A larger receive window does not improve throughput when the existing window already accommodates that request.


Load Balancer
-------------

The SFTP/SCP services of SFTPPlus can be part of a load balancing solution.

SFTPPlus requires no extra configuration for SFTP/SCP services
when using a layer 4 TCP balancer or a DNS load balancer.

AWS Network Load Balancer and Azure Load Balancer are examples of layer 4
load balancers.

You can't use the SFTP/SCP service with an HTTP Layer 7 load balancer.
