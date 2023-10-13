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

When using the `secure` configuration option for an SSL/TLS/SFTP/SCP client
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

This list provides maximum compatibility with existing deployments while avoiding deprecated ciphers.

SFTPPlus uses the OpenSSL library provided by the Python `cryptography` module.
To benefit from upstream security updates for the bundled OpenSSL library,
keep your SFTPPlus deployments always updated.
This OpenSSL version might not provide
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
* TLS v1.3 (for OpenSSL 1.1.1 or newer)

..  note::
    SSL version 2 is not supported. It was officially deprecated
    in 2011 by the RFC 6176.

    SSL version 3 is supported only to provide backward compatibility
    for older clients, but it is not recommended for new deployments.
    It was officially deprecated in June 2015 by the RFC 7568.


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

    Newer deployments should be based on RSA with a key size of 3072 or
    greater.

    DSS/DSA key support is scheduled to be removed/deprecated with
    the future release of TLS v1.3.


Key agreement algorithms
------------------------

* DHE, EDH, DH - ephemeral prime factorization Diffie-Hellman (DH)
  key agreement
* EECDH, ECDHE, ECDH - ephemeral elliptic curve Diffie-Hellman (ECDH)
  key agreement

For the DH key agreement, SFTPPlus uses a DH parameter for the `2` generator
with a size of 2048 bits.
Contact us if you require a different DH parameter for your configuration.


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


.. _standards-crypto-ssh:

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
    aes256-ctr
    aes192-ctr
    aes128-ctr

    # MACs
    # SHA1 and MD5 might look weak, but the way they are used in SSH
    # does not allow for the possibility of a collision attack.
    hmac-sha2-256
    hmac-sha2-512
    hmac-sha1

    # Key Exchanges
    # See RFC for current recommendation (check updates).
    # This is based on:
    # https://tools.ietf.org/id/draft-ietf-curdle-ssh-kex-sha2-09.html
    curve25519-sha256 (with OpneSSL 1.1.1 or newer)
    curve25519-sha256@libssh.org (with OpneSSL 1.1.1 or newer)
    ecdh-sha2-nistp521
    ecdh-sha2-nistp384
    ecdh-sha2-nistp256
    diffie-hellman-group-exchange-sha256
    diffie-hellman-group18-sha512
    diffie-hellman-group17-sha512
    diffie-hellman-group16-sha512
    diffie-hellman-group15-sha512
    diffie-hellman-group14-sha256

This list provides maximum compatibility with existing deployments while avoiding deprecated ciphers.


Public-key cryptographic systems
--------------------------------

Here is the list of supported public-key cryptographic systems
ordered by SFTPPlus' preference during the negotiation phase:

* Ed25519 (with OpenSSL 1.1.1 or newer)
* ECDSA (ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, ecdsa-sha2-nistp521)
* RSA
* DSS/DSA

..  warning::
    Newer deployments should use Ed25519 when available,
    or RSA with a key size of at least 3072.


SSH Key Exchange
----------------

Here is the list of supported SSH key exchanges,
ordered on the preference of SFTPPlus during the negotiation phase:

* curve25519-sha256
* curve25519-sha256\@libssh.org
* ecdh-sha2-nistp521
* ecdh-sha2-nistp384
* ecdh-sha2-nistp256
* diffie-hellman-group-exchange-sha256 (FIPS 140-2 compatible)
* diffie-hellman-group-exchange-sha1 (FIPS 140-2 compatible)
* diffie-hellman-group14-sha1 (FIPS 140-2 compatible)
* diffie-hellman-group1-sha1
  (FIPS 140-2 compatible, but no longer considered secure to modern standards)
* diffie-hellman-group14-sha256 (RFC 8268 for transition to newer group sizes)
* diffie-hellman-group15-sha512 (RFC8268)
* diffie-hellman-group16-sha512 (RFC8268)
* diffie-hellman-group17-sha512 (RFC8268)
* diffie-hellman-group18-sha512 (RFC8268)

The fixed group prime numbers are the one specified in RFC3526.


Keyed-hash message authentication code (HMAC)
---------------------------------------------

Here is the list of supported HMAC,
ordered on the preference of SFTPPlus during the negotiation phase:

* hmac-sha2-512 (FIPS 140-2 compatible)
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


AS2 protocol family
===================

SFTPPlus can transfer files using the AS2 protocol as defined in the
`RFC 4130 <https://tools.ietf.org/html/rfc4130>`_
MIME-Based Secure Peer-to-Peer Business Data Interchange Using HTTP,
Applicability Statement 2 (AS2) standard.

Signing and encrypting AS2 messages is implemented as defined in the
`RFC 5652 <https://tools.ietf.org/html/rfc5652>`_
Cryptographic Message Syntax (CMS) standard.

Signing and verifying Message Disposition Notification (MDN) is implemented
as defined in the `RFC 3798 <https://tools.ietf.org/html/rfc3798>`_ standard.

Asynchronous MDN is not yet supported. It will be available in a future
version.

Only the RSA asymmetric algorithm is supported.
If you need support for DSA or ECDSA get in touch with our support team.

The following digest algorithms are supported:

* MD5
* SHA1
* SHA224
* SHA256
* SHA384
* SHA512

Messages are signed using the PCKS#1 v1.5 (rsassa_pkcs1v15) padding.
PCKS#1 v2.1 (rsassa_pss) Probabilistic Signature Scheme (PSS) padding is not
yet supported.

The following symmetric encryption algorithm are supported, all using
PKCS7 padding and cipher block chaining (CBC) mode:

* 3DES
* AES128
* AES192
* AES256

When setting up an AS2 transfer both your organization and your remote partner
will have a set of private keys and public certificates.

You should never share your private key with your remote partner.
No AS2 operation on your partner remote AS2 sending service needs the
private key of your organization.
Only your public certificate should be shared with your partner.

You will never need the private key of your partner.
Only the public partner certificate is needed.
No AS2 operation insider your SFTPPlus AS2 receiving service needs the
private key of your partner.


OpenPGP protocol family
=======================

The OpenPGP encryption, as defined in RFC 2440 and RFC 4880,
provides a standard for encrypting and signing data and files.
PGP encrypted files can be transferred over any standard file transfer
protocol.

OpenPGP support in SFTPPlus is based on GnuPG version 1.4.

PGP is not supported on Alpine Linux.


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

The Time-Based One-Time Password (TOTP) authentication method adds an extra layer of security on top of the usual username/password credentials.

A unique code valid for a limited number of seconds is used for validation.

The code is generated using helper applications like Google Authenticator or FreeOTP.

To use a unique password per session, this unique code has to be added at the end of the regular password.
By appending the unique code to the regular password,
the new method of authentication is still compatible with the traditional
username and password authentication system.
No extra changes are required for the file transfer client.

This implements a two factor authentication method (2FA) in which both the password and the unique code are used to authenticate the connection.

..  note::
    Once a unique TOTP code is used to authenticate successfully, it is
    no longer valid. This prevents replay attacks.
    Therefore, FTPS clients using concurrent connections will not be able
    to open a second connection using the same password and TOTP credentials.
    If your FTPS client cannot ask for new credentials for every connection,
    you should configure it to not open more than one connection at a time to
    a SFTPPPlus FTPS server requiring TOTP authentication.
    Please contact the Pro:Atria Support team if you need help with this.

SFTPPlus supports the TOTP algorithm as defined in
`RFC 6238 <https://tools.ietf.org/html/rfc6238>`_

The following parameters are supported:
* 6 digits
* 30 seconds interval
* SHA1

Two-factor authentication will succeed as long as the received token is within
one time step of 30 seconds (+/- 30s).

..  note::
    If using the `Authy` authentication application you might observe that
    the authentication still works, even when the server and the client
    clocks are out of sync.
    This is because Authy is not using the phone clock.
    It uses an external clock to generate the code.

Authenticating twice with the same multi-factor authentication token will fail.
This prevents replay attacks.

..  warning::
    By itself, TOTP-based authentication is vulnerable to brute-force attacks.
    If you want more protection against attackers with stealed passwords,
    it is highly recommended to enable the `Ban IP for a time interval`
    authentication method.
    Brute-force mitigation is enabled by default in new SFTPPlus installations.
    If you are upgrading from an older version, make sure to enable it.


Password-based authentication
=============================

For file transfer services, SFTPPlus receives passwords from
remote clients and forwards them to the configured authentication method.

SFTPPlus has its own user database ready to use as a standalone solution for
authenticating users based on username and password credentials.

Usernames longer than 150 characters are not allowed.

Passwords longer than 150 characters are not allowed at all by SFTPPlus.
The limit applies to both SFTPPlus accounts
and accounts authenticated via OS, LDAP, HTTP API,
or other methods.

These limits prevent denial of service attacks and mitigate other types of attacks.

We recommend using passwords no longer than 128 characters.
This allows using TOTP and other multi-factor authentication methods
on top of an existing password.

Please contact us if you need longer passwords.


Modular Crypt Password Hashing
==============================

The password for the file transfer accounts and administrator accounts
managed by SFTPPlus are stored using a standard password hash algorithm.
They are not stored in clear text.

The SHA512-Crypt password hash algorithm is used by default.

The modular crypt format is a loose standard for password hash strings which
started life under the Unix operating system.

The basic format is `PREFIX + HASH`.
For example, a PBKDF2 password with a salt of 8 characters::

    $pbkdf2-sha256$8000$XAuBMIYQ$tRRlz8hYn63B9LYiCd6PRo6FMiunY9ozmMMI3srxeRE

It has also been adopted by a number of application-specific
hash algorithms used outside of the Unix/Linux operating systems.

SFTPPlus supports the following password hash standards with the
corresponding modular prefixes / Scheme ID:

* `crypt-sha256` - prefix `$5$` - Standard Unix SHA-256 Crypt
* `crypt-sha512` - prefix `$6$` - Standard Unix SHA-512 Crypt
* `pbkdf2_sha256` - prefix `$pbkdf2-sha256$` - RSA PKCS#5 based on SHA-256
* `pbkdf2_sha512` - prefix `$pbkdf2-sha512$` - RSA PKCS#5 based on SHA-512

All variants are publicly documented and widely reviewed algorithms.

The PBKDF2 (Password-Based Key Derivation Function 2) key derivation function
is standardized in `RFC 8018 <https://tools.ietf.org/html/rfc8018>`_ as
part of the RSA Lab PKCS #5 Password-Based Cryptography Specification
Version 2.1 document. RFC 2898 is an older version of the same standard.


FIPS 140-2
==========

SFTPPlus does **not** have vendor certification for
:doc:`FIPS 140-2</standards/fips140-2>` compliance.
