.. container:: tags pull-left

    `server-side`
    `client-side`
    `security`


Supported Cryptographic Standards
#################################

This page describes the cryptography method, protocols, and algorithms
supported by SFTPPlus.

..  contents:: :local:


SFTPPlus provides an easy configuration option for both the `ssl_cipher_list`
and `ssl_cipher_list` with the value `secure`

This will keep the list of accepted cryptographic methods up to date with
modern security practices.

When using the `secure` configuration option for a SSL/TLS/SFTP/SCP client
and server-side transfer,
the list of accepted ciphers might change between SFTPPlus or OpenSSL upgrades.

Connections which are using cryptography which is no longer considers secured
will stop working between such updates.

..  note::
    If you are concerned about legacy connections and don't want to disturb
    existing transfers between updates, even when they are using weak
    encryption, don't use the `secure` value.
    Instead, configure an explicit list of ciphers.
    In this way, the configuration will stay the same between SFTPPlus updates.


SSL/TLS protocol family
=======================

The secure file transfer services implemented in FTPS and HTTPS are based on
the Transport Layer Security (TLS) protocol, which is the successor of the
Secure Sockets Layer (SSL) protocol.


Default secure SSL/SLS configuration
------------------------------------

When using the `secure` value for the `ssl_cipher_list`,
the following algorithms are enabled::

    HIGH:!PSK:!RSP:!eNULL:!aNULL:!RC4:!MD5:!DES:!3DES:!aDH:!kDH:!DSS

This list provides maximum compatibility with existing
deployments and does not contain ciphers which are considered weak.

SFTPPlus uses the OpenSSL library provided by the operating system,
with some exceptions, most notably Windows.
The OpenSSL version included in your operating system might not provide
all the ciphers which are required by older SSL/TLS versions of the standard.
This is valid especially for cryptographic methods which in recent years were
discovered to no longer be secured.
For example, SSLv3 is no longer provided at all.
While 3DES was considered secure at the beginning of 2016, in August 2016 it
was discovered that it is vulnerable to the SWEET32 attack.
Therefore, 3DES support is no longer included with latest updates for most
operating systems.

To verify the list of ciphers available for your operating system use::

    openssl ciphers -V


SSL/TLS versions
----------------

* SSL v3 (considered not secure)
* TLS v1.0
* TLS v1.1 (for OpenSSL 1.0.1 or newer)
* TLS v1.2 (for OpenSSL 1.0.1 or newer)

..  note::
    SSL version 2 is not supported. It was officially deprecated
    in 2011 by the RFC 6176.

    SSL version 3 is supported only to provide backward compatibility
    for older clients, but it is not recommended for new deployments.
    It was officially deprecated in June 2015 by the RFC 7568.


OpenSSL versions used in supported operating systems
----------------------------------------------------

Modern Unix-like systems are distributed with OpenSSL version 1.0.2 or
newer.

Microsoft Windows is distributed without including OpenSSL libraries
or a compatible alternative.
On Windows, SFTPPlus uses the embedded OpenSSL libraries version 1.1.1c.
Please keep your SFTPPlus deployments on Windows always updated, to benefit
from upstream security updates for the bundled OpenSSL libraries.

The OpenSSL version distributed with SLES 12 advertises that it supports
Elliptic Curve Diffie-Hellman (ECDH) as part of
Elliptic Curve Cryptography (ECC).
However, in the SLES 12 version tested by Pro:Atria,
there is a defect and ECDH is not usable.

For SUSE Linux Enterprise Server version 11, with or without the Security
Module, SFTPPlus uses the embedded OpenSSL libraries version 1.1.1c.
Please keep your SFTPPlus deployments on SLES 11 always updated, to benefit
from upstream security updates for the bundled OpenSSL libraries.

On Alpine Linux, SFTPPlus is built against the default-included
LibreSSL 2.5.x libraries.
The OpenSSL version available as a package is not supported.

For macOS 10.13 High Sierra and 10.14 Mojave, SFTPPlus is built to use
the LibreSSL 2.2.7 libraries, as provided by Apple with the operating system.

The above list is not comprehensive and comes with no guarantee. Please check
with support@proatria.com for further info.

Last updated for release 4.0.0 on April 26, 2019.


File formats
------------

TLS / X.509 certificates and keys can be stored and read by SFTPPlus in the
following formats:

* PKCS #8 / PEM
* PKCS #12 / PFX


Public-key cryptographic systems
--------------------------------

* DSS/DSA
* RSA

..  note::
    DSS/DSA key support is provided for backward compatibility.

    Newer deployments should be based on RSA, use a key size of 4096 or
    greater.

    DSS/DSA key support is scheduled to be removed/deprecated with
    the future release of TLS v1.3.


Hash functions
--------------

* MD5
* SHA-1 (FIPS 140-2 compatible)
* SHA-2 (for OpenSSL 0.9.8 or newer) (FIPS 140-2 compatible)

..  note::
    All modern operating systems, still supported by their vendors,
    provide newer versions of OpenSSL with support for SHA-2.


Encryption algorithms
---------------------

* 3DES (FIPS 140-2 compatible, vulnerable to SWEET32 attacks)
* AES 128 and AES 256 (FIPS 140-2 compatible)
* RC4
* Blowfish


SSH protocol family
===================

Only SSH version 2 is supported.

SFTP is implemented based on draft version 3.

SCP is not a standard protocol, therefore it was implemented based on the
public source code of OpenSSH's implementation.


Default SFTP/SCP secure configuration
-------------------------------------

When using the `secure` value for the `ssh_cipher_list`,
the following algorithms are enabled.
These are listed below according to preference::

    # Ciphers
    aes256-cbc aes256-ctr
    aes192-cbc aes192-ctr
    aes128-cbc aes128-ctr

    # MACs
    # SHA1 and MD5 might look weak, but the way they are used in SSH
    # does not allow for the possibility of a collision attack.
    hmac-sha2-256
    hmac-sha1
    hmac-md5

    # Key Exchanges
    # See RFC for current recommendation (check updates).
    # This is based on:
    # https://tools.ietf.org/id/draft-ietf-curdle-ssh-kex-sha2-09.html
    diffie-hellman-group-exchange-sha256
    diffie-hellman-group-exchange-sha1
    diffie-hellman-group14-sha1

This list provides maximum compatibility with existing
deployments and does not contain ciphers which are considered weak.


Ciphers
^^^^^^^

3DES is disabled due to SWEET32 attack:

* aes256-cbc aes256-ctr
* aes192-cbc aes192-ctr
* aes128-cbc aes128-ctr


HMACs
^^^^^

SHA1 and MD5 might have higher collision probabilities,
but the way they are used in SSH does not allow for the possibility of a
collision attack.

* hmac-sha2-256
* hmac-sha1
* hmac-md5


Key Exchanges
^^^^^^^^^^^^^

Based on the `IETF recommendation
<https://tools.ietf.org/id/draft-ietf-curdle-ssh-kex-sha2-09.html>`_
on the set of key exchange methods for use in the Secure Shell (SSH) protocol:

* diffie-hellman-group-exchange-sha256
* diffie-hellman-group14-sha1


Public-key cryptographic systems
--------------------------------

Here is the list of supported public-key cryptographic systems,
ordered on the preference of SFTPPlus during the negotiation phase:

* RSA
* DSS/DSA

..  warning::
    Newer deployments should be based on RSA with a key size of 4096 or
    greater.


SSH Key Exchange
----------------

Here is the list of supported SSH key exchanges,
ordered on the preference of SFTPPlus during the negotiation phase:

* diffie-hellman-group-exchange-sha256 (FIPS 140-2 compatible)
* diffie-hellman-group-exchange-sha1 (FIPS 140-2 compatible)
* diffie-hellman-group14-sha1 (FIPS 140-2 compatible)
* diffie-hellman-group1-sha1
  (FIPS 140-2 compatible, but no longer considered secure to modern standards)


Keyed-hash message authentication code (HMAC)
---------------------------------------------

Here is the list of supported HMAC,
ordered on the preference of SFTPPlus during the negotiation phase:

* hmac-sha2-256 (FIPS 140-2 compatible)
* hmac-sha1 (FIPS 140-2 compatible)
* hmac-md5


Symmetric encryption algorithms
-------------------------------

Here is the list of supported symmetric encryption algorithms,
ordered on the preference of SFTPPlus during the negotiation phase:

* aes256-ctr, aes256-cbc, aes192-ctr, aes192-cbc, aes128-ctr,
  aes128-cbc  (FIPS 140-2 compatible)
* cast128-ctr, cast128-cbc
* blowfish-ctr, blowfish-cbc
* 3des-ctr, 3des-cbc (FIPS 140-2 compatible, vulnerable to SWEET32 attacks)


OpenPGP protocol family
=======================

The OpenPGP encryption, as defined in RFC 2440 and RFC 4880,
provides a standard for encrypting and signing data and files.
PGP encrypted files can be transferred over any standard file transfer
protocol.

OpenPGP support in SFTPPlus is based on GnuPG version 1.4.

PGP is not supported in SLES 11 and Alpine Linux.


Public-key cryptographic systems
--------------------------------

* DSS/DSA
* RSA (RSA-E, RSA-S)
* ELG-E


Hash functions
--------------

* MD5
* SHA1
* RIPEMD160
* SHA256
* SHA384
* SHA512
* SHA224


Symmetric encryption algorithms
-------------------------------

* IDEA
* 3DES
* CAST5
* BLOWFISH
* AES (AES128)
* AES192
* AES256
* TWOFISH
* CAMELLIA128
* CAMELLIA192
* CAMELLIA256


Compression
-----------

* Uncompressed
* ZIP
* ZLIB


Two-factor / 2-step authentication
==================================


TOTP - Time-Based One-Time Passwords
------------------------------------

The Time-Based One-Time Password (TOTP) authentication method adds an
extra layer of security on top of the usual username/password credentials.

A unique code valid for a limited number of seconds is used for validation.

The code is generated using helper applications like Google Authenticator or
FreeOTP.

To use a unique password per session, this unique code has to be added
at the end of the regular password.
By appending the unique code to the regular password,
the new method of authentication is still compatible with the traditional
username and password authentication system.
No extra changes are required for the file transfer client.

SFTPPlus supports the TOTP algorithm as defined in
`RFC 6238 <https://tools.ietf.org/html/rfc6238>`_

The following parameters are supported:
* 6 digits
* 30 seconds interval
* SHA1

Two-factor authentication will succeed as long as the received token is within
one time step of 30 seconds (+/- 30s).

Authenticating twice with the same multi-factor authentication token will fail.
This prevents replay attacks.

..  warning::
    By itself, TOTP-based authentication is vulnerable to brute-force attacks.
    If you want more protection against attackers with stealed passwords,
    it is highly recommended to enable the `Ban IP for a time interval`
    authentication method.
    Brute-force mitigation is enabled by default in new SFTPPlus installations.
    If you are upgrading from an older version, make sure to enable it.


FIPS 140-2
==========

SFTPPlus does **not** have vendor certification for
:doc:`FIPS 140-2</standards/fips140-2>` compliance.
