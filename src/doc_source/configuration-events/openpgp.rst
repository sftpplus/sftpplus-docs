Encrypt / decrypt using OpenPGP
===============================

The `openpgp` event handler can be configured to encrypt or decrypt
files using the OpenPGP standard.

All files with the `.pgp` or `.gpg` extensions are decrypted,
all the other files are encrypted.

Encrypted files will have the `.pgp` extension appended to their filename.

The handler can be associated with events containing a list of files.
It will try to handle each file associated with the event and will stop at
the first failure.

..  contents:: :local:

.. include:: /configuration-events/events-commons.include.rst


encryption_public_keys
----------------------

:Default value: ''
:Optional: Yes
:Values: * ASCII armored public PGP keys
:From version: 4.0.0
:Description:
    Lists of public PGP keys used for the encryption operation.

    It can contain one or multiple public PGP keys in printable ASCII format.

    Leave it empty if you don't want to use asymmetric encryption.


decryption_private_keys
-----------------------

:Default value: ''
:Optional: Yes
:Values: * ASCII armored private PGP keys
:From version: 4.0.0
:Description:
    Lists of private PGP keys used for the decryption operation.

    It can contain one or multiple private PGP keys in printable ASCII format.

    Leave it empty if you don't want to use asymmetric encryption.


passphrase
----------

:Default value: Empty
:Optional: No
:Values: * Text
:From version: 4.0.0
:Description:
    Passphrase/password for encrypting/decrypting files using
    symmetric OpenPGP cryptography.

    Leave it empty if you don't want to use symmetric encryption.


encryption_extension
--------------------

:Default value: `.pgp`
:Optional: Yes
:Values: * Text to be appended after the file name.
:From version: 4.0.0
:Description:
    File extension used for the files encrypted by the handler.

    Encrypted files will have the configured text appended
    to the original name.

    This value is case-sensitive.


encryption_cipher
-----------------

:Default value: AES128
:Optional: Yes
:Values: * AES128
         * AES192
         * AES256
         * CAST5
         * 3DES
:From version: 4.0.0
:Description:
    Cipher used for symmetric encryption.

    This value is not used when `passphrase` is not defined,
    as that is required for symmetric encryption.

    This value is case-insensitive.


source_attribute
----------------

:Default value: ``real_path``
:Optional: Yes
:Values: * Event data member name.
:From version: 4.0.0
:Description:
    Name of the event's structured data member
    used to get the path to be handled.

    This is a case-insensitive value.


destination_path
----------------

:Default value: empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
:From version: 4.0.0
:Description:
    The path where the resulting files are encrypted/decrypted.

    Leave it empty to perform file operations in the path of the source files.


overwrite_rule
--------------

:Default value: `fail`
:Optional: Yes
:From version: 4.7.0
:Values:
    * `fail` - abort transfer if destination file already exists.
    * `overwrite` - always overwrite existing files with the content
      of the new source files.
    * `disable` - don't check for existing file and always try to transfer the
      file.
    * `skip` - don't transfer the source file when destination exists.

:Description:
    Rule used to decide how to handle the overwriting of an
    existing file at the destination.

    When set to `overwrite` it will emit an event when the destination
    file is overwritten.

    When set to `skip` it will not handle the file and the source file
    is not removed.
    An event is emitted to inform that the file was skipped.


delete_source_on_success
------------------------

:Default value: `Yes`
:Optional: yes
:Values: * `Yes`
         * `No`
:From version: 4.0.0
:Description:
    Whether to delete the source file after a successful operation.

    If encrypting/decrypting the source file fails, the source is
    not removed, even when this is set to `Yes`.
