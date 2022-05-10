AS2 Location
============

An `as2` location allows sending files to a remote AS2 server.

The AS2 protocol can use HTTP or HTTPS (secure) connections.

The `as2` location can only be used for sending files over AS2.
If you need to receive files over the AS2 protocol, you will need to
configure the HTTP file transfer service.

Unlike a typical web browser connection, to protect an AS2 HTTPS connection
you will have to explicitly configure the list of trusted CAs and
the location of the CRLs.


url
---

:Default value: Empty
:Optional: No
:Values: * .
:From version: 4.5.0
:Description:
    Receiving URL for your partner.

    SFTPPlus will use this URL to send files to your AS2 partner.

    When this is defined as an `http://` URL, the SSL configuration options
    are ignored.


username
--------

:Default value: Empty
:Optional: Yes
:From version: 4.5.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote AS2 partner server.

    Leave it empty when the remote AS2 partner doesn't require authentication.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 4.5.0
:Values: * Plain text password.
         * Empty.
:Description:
    This option specifies the password used to connect to the remote
    AS2 partner server.

    It is ignored when `username` is empty.


as2_own_identifier
------------------

:Default value: Empty
:Optional: No
:From version: 4.5.0
:Values: * Text.
:Description:
    Identifier for your own local AS2 organization sending the files.


as2_own_certificate
-------------------

:Default value: 'General server SSL certificate'
:Optional: No
:From version: 4.5.0
:Values: * PEM certificate.
         * PEM certificate and PEM private key.
:Description:
    Certificate for your own local AS2 organization used when
    signing files sent to a remote AS2 partner.

    The certificate should be configured in PEM format.

    This configuration can also contain the private key associated to the
    certificate.

    This can be empty when sending unsigned files.


as2_own_private_key
-------------------

:Default value: 'General server SSL private key'
:Optional: No
:From version: 4.5.0
:Values: * PEM private key.
:Description:
    Certificate for your own local AS2 organization used when
    signing files sent to a remote AS2 partner.

    The certificate should be configured in PEM format.

    This configuration can also contain the private key associated to the
    certificate.


as2_partner_identifier
----------------------

:Default value: Empty
:Optional: No
:From version: 4.5.0
:Values: * Text.
:Description:
    Identifier for the remote AS2 partner receiving the files.


as2_partner_certificates
------------------------

:Default value: Empty
:Optional: No
:From version: 4.5.0
:Values: * PEM certificate
         * Multiple PEM certificates
:Description:
    Certificate in PEM format used to encrypt files sent to the AS2
    partner and to validate the received signed MDN.

    You can define multiple PEM certificates for the case in which the partner
    uses different certificates for signing and encryption.

    Old and new PEM certificates can be defined at the same time
    for a partner's certificate rollover.

    When sending encrypted files, the first configured PEM certificate will
    be used for the encryption operation.


as2_send_security
-----------------

:Default value: 'signed-and-encrypted'
:Optional: yes
:From version: 4.5.0
:Values: * `signed-and-encrypted`
         * `signed`
         * `encrypted`
         * `disabled`
:Description:
    This defines the method used to secure the file transfers on top of
    the standard security provided by the HTTPS protocol.

    When encrypting file content, the first certificate defined at
    `as2_partner_certificates` is used.

    When signing file content, the digest/hashing algorithm defined in
    `as2_signature_algorithm` is used.

    When defined as `disabled`, files are sent unsigned and unencrypted.


as2_mdn_receipt
---------------

:Default value: 'sync-signed'
:Optional: yes
:From version: 4.5.0
:Values: * `sync-signed`
         * `sync-unsigned`
         * `disabled`
:Description:
    This defines the method used to request the
    message disposition notifications (MDN) receipt.

    When requesting a signed MDN, it will make the request using the
    digest/hashing algorithm defined in `as2_signature_algorithm`.

    When defined as `disabled`, it will not request an MDN receipt.


as2_encryption_algorithm
------------------------

:Default value: 'aes256'
:Optional: yes
:From version: 4.5.0
:Values: * `3des`
         * `aes128`
         * `aes192`
         * `aes256`
:Description:
    Symmetric encryption algorithm used to encrypt sent files.

    All algorithms use the Cipher Block Chaining (CBC) mode and PKCS#1 v1.5
    padding.


as2_signature_algorithm
-----------------------

:Default value: 'sha256'
:Optional: yes
:From version: 4.5.0
:Values: * `md5`
         * `sha1`
         * `sha224`
         * `sha256`
         * `sha348`
         * `sha512`
:Description:
    Digest / Hashing algorithm used when signing sent files and
    requesting the MDN receipt.


as2_content_type
----------------

:Default value: 'application/octet-stream'
:Optional: Yes
:From version: 4.5.0
:Values: * MIME content type
:Description:
    MIME content type used when sending AS2 files.


.. include:: /configuration/ssl.include.rst
