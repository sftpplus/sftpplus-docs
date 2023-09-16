File message digest generator
=============================

The `file-digest` event handler is used to compute and emit an event with the digest of a file.

The generated event has ID `20194`.

..  note::
    It only generates the message digest value (checksum).
    It can not be used to verify an existing digest value.
    Get in touch with our support team to check the availability of the validation functionality.

..  contents:: :local:

.. include:: /configuration-events/events-commons.include.rst


source_attribute
----------------

:Default value: 'real_path'
:Optional: Yes
:Values: * Text
:From version: 4.31.0
:Description:
    This is configured with the name of an event data member used to extract the path for which the digest is computed.


digest_algorithm
----------------

:Default value: `sha512`
:Optional: Yes
:From version: 4.31.0
:Values:
    * md5
    * sha1
    * sha224
    * sha256
    * sha348
    * sha512
:Description:
    This is the name of the digest algorithm to be used when generating the digest value.


output_format
-------------

:Default value: `gnu`
:Optional: Yes
:From version: 4.531.0
:Values:
    * base64
    * gnu
    * bsd
:Description:
    The format used to display the generated digest.

    Use `base64` to only have the base64 representation of the digest,
    without any other text.

    Use `gnu` to have the output in GNU standard.
    This is the `hexadecimal`` value followed by the name of the file.
    For example: `9c702f1c77c48a375ac14c987ed7579cbb91f6a2  README.rst`

    Use `bsd` to have the output in BSD tag standard.
    This is the algorithm name, followed by the filename in round brackets and followed by the `hexadecimal`` value.
    For example: `SHA1 (README.rst) = 9c702f1c77c48a375ac14c987ed7579cbb91f6a2`
