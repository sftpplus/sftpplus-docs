.. container:: tags pull-left

    `server-side`
    `client-side`
    `security`
    `configuration`


SSL / TLS / SSH protocols overview
==================================

..  contents:: :local:


Introduction
------------

FTPS / HTTPS and Local Manager protocols use the SSL v3 or TLS v1
cryptographic protocols.
SSL v3 is provided for backward compatibility with older endpoints.
TLS v1 should be used whenever possible.
TLS v1 is actually SSL v4, renamed before release.

SFTP and SCP protocols use the SSH v2 cryptographic protocol.

The SSH protocol is similar to the SSL/TLS protocols. At lower levels they all
employ the same cryptographic algorithms, yet the protocols are incompatible.

The server supports all FIPS-140 compliant cryptographic algorithms, as well
as other algorithms required by older or non FIPS-140 compliant endpoints.

To read more about the Public Key Infrastructure (PKI), please go to our
:doc:`dedicated section here </operation/pki>`.


Key Management
--------------

The default server installation will generate a self-signed SSL certificate,
and pairs of 2048-bit RSA and 1024-bit DSA private/public keys.

To change the certificates used by the SSL/TLS service, you need to generate
a new key and an associated certificate signing request.
This can be done with external tools such as the IIS Manager, OpenSSL tools,
or the Java KeyTool.

SSL certificates are stored in PEM format.

SSH keys are stored in OpenSSH format.

In the case that the SSH keys are breached, or you need to use keys with a
different size, you can generate new keys using the Local Manager or the
:ref:`command line tool <generate-ssh-key>` distributed with the server.

To manage public keys for SSH clients, please consult the documentation
dedicated to
:ref:`SSH Key Authentication <operation-sftp-ssh-key-authentication>`


Protecting private keys, public keys and certificates
-----------------------------------------------------

The server handles private/public keys and certificates as normal files
in the local file system.

The operating system's file system security features should be used to protect
private keys from being read by other parties.
Public keys and certificates can be readable by all operating system users,
as this does not pose any risk.

In general, they are stored as separate files, but you can have an SSL public
key stored together with the private key in a single file.

When transferred or stored over an unsecured medium, the private keys should be
encrypted with a password.

If private keys are breached, they can be used to impersonate the identity
of the endpoint associated to them.

If the server's private key is breached, it can be used to create a rogue
server instance, which will look identical to the original instance for any
remote endpoint.

Besides getting the private key, the attacker will also need to change the
TCP/IP routing or the DNS server in use for the endpoint, so that the rogue
server is accessible using the same IP or DNS name for the remote client.

If the client's private key is breached, it can be used to impersonate
the identity of the remote endpoint associated with that private key.


Private Key, Public Key, Certificate Backup / Recovery
------------------------------------------------------

Private keys, public keys and certificates can be backed up using regular
file backup systems.

Backup systems require read access to absolutely all of the files, so private
keys should be protected with a password.

For SSH keys, in the case that you lose the public key, you can recover it
using the private key.

For SSL/TLS keys, in the case that you lose the certificate, you can ask your
CA to send a copy of the certificate.
In a worst-case scenario, you can generate a new CSR (Certificate Signing
Request) for the same private key.

There is no method to recover private keys other than from backups.


Performance considerations
--------------------------

Symmetric encryption algorithms are fast on modern computers.
Private / public key asymmetric encryption and decryption are slow and require
many more resources to compute compared to conventional single-key algorithms.

SSL/TLS and SSH actually use symmetric encryption to encrypt exchanged data.
Asymmetric encryption is only used to exchange the (short-lived) symmetric
keys.

SFTPPlus can handle hundreds of parallel active connections
over a Gigabit Ethernet connection.
With thousands of connections, our performance tests indicate that the
bottleneck is not the CPU performing TLS/SSL/SSH cryptographic operations,
but rather the transfer speed of the disk or the network bandwidth.


Weak ciphers and protocols
--------------------------

TLS/SSL and SSH protocols were introduced a long time ago, SSL 3.0 being
introduced in 1996.
Over time, some of the protocols or cryptographic algorithms
proved to have design weaknesses or to be less secure.

The following cryptographic algorithms and protocols are not considered secure:

* SSL at any version
* RC4
* MD5 message-digest algorithm
* DES Data Encryption Standard symmetric-key algorithm
* Export grade algorithms.

SSL version 2.0 is not supported as it contains a number of security flaws
which ultimately led to the design of SSL version 3.0.

SSL version 3.0 is supported, but its usage is highly discouraged.
As of 2014, the 3.0 version of SSL is considered insecure.

RC4 in SSL and TLS was at one time considered secure but as of March 2013,
using RC4 in SSL and TLS is considered insecure.

The MD5 message-digest algorithm is a widely used cryptographic hash function,
but with modern computers the security of the MD5 hash function is severely
compromised.
The algorithm is not included in the list of approved FIPS 140-2 hash
functions.

The DES symmetric-key algorithm is vulnerable to brute force attack, and is not
considered secure.

While the 3DES algorithm is approved by FIPS 140-2,
it is no longer considered secure
due to the vulnerability associated with the SWEET32 attack

U.S. cryptography export regulations define a set of algorithms with the
intention of allowing them to be broken easily by the NSA, but not by other
organizations with fewer computing resources.
Nowadays, NSA capabilities from the 1990s can be matched by any personal
computer, making those algorithms insecure.

While for some, FIPS 140-2 compliance is the gold standard for security,
it was released in December 2002.
With the fast pace at which the computer security landscape is evolving,
a standard defined in 2002 should not be considered up to date.

FIPS 140-3 update was not yet released due to disagreement in the US
government and the updated document is not yet ready for consumption
as of this writing.
Meanwhile, use the guidance from PCI and ISO/IEC 24759:2017 standards.


NULL ciphers
------------

TLS/SSL can be used in non-authentication or non-encryption modes.
These modes are disabled by default as they provide degraded security.

Non-encryption mode (`eNULL`) can be used in special cases when the remote peer
is required to be authenticated, but the transmitted data is already encrypted
using another method like a PGP encrypted file.

Non-authentication mode (`aNULL`) is vulnerable to a "man in the middle" attack
and its use is highly discouraged.
In this mode, the connection will not validate the remote peer.
Data sent in this mode is encrypted.


Certificate Revocation List Loading
-----------------------------------

When the CRL fails to be loaded for the first time, it is considered a
critical failure and the component using the CRL is stopped.

This is done to help detecting configuration errors.

If the CRL was successfully loaded at least once, but then fails to be reloaded
at the scheduled date and time, the loading will be retried with a delay of
4 hours.

The current loaded CRL is still considered valid, as long as the
`Next Update` date and time is not reached.

If reloading the CRL still fails after the Next Update date and time is reached
the current cached CRL is no longer valid and a new CRL reloading is scheduled
in 4 hours.

In some special cases the current loaded CRL is considered invalid, even
if the `Next Update` is not reached.
The error messages will indicate whether the CRL is no longer valid.

When a service using SSL/TLS is started and CRL or CDP configuration is
defined it will try to pre-cache the CRL by loading the CRL, even if no
client has yet made a connection.
In this way, when a client will later initiate a connection, the connection is
not delayed while waiting for the CRL to be loaded.

A cached CRL is considered valid as long as the date and time
advertised in the `Next Update` is not reached.

Redirection is not supported for the CRL URLs in order to mitigate
redirection attacks or miss-configurations.
Administrator need to always configure the final location of a CRL.
