Content check
=============

..  contents:: :local:

The `content-check` event handler is used to search a specific value inside the content of a file.
It can also be used to compute and emit an event with the digest of a file.

The generated event ID for a content rule is `20044`.

The generated event ID for the checksum is `20194`.

..  note::
    It only generates the message digest value (checksum).
    It can not be used to verify an existing digest value.
    Get in touch with our support team to check the availability of the validation functionality.

.. include:: /configuration-events/events-commons.include.rst


source_attribute
----------------

:Default value: 'real_path'
:Optional: Yes
:Values: * Text
:From version: 4.31.0
:Description:
    This is configured with the name of an event data member used to extract the path for which the digest is computed.


line_search
-----------

:Default value: `empty`
:Optional: Yes
:From version: 5.16.0
:Values: * Comma separated list of matching expression and matching description
         * Multiple matching expressions, one per line.
:Description:
    You can configure SFTPPlus to search each line of an **UTF-8 encoded text file**,
    based on a matching expression and emit an event with the matching description details.

    When multiple lines are matching the same expression,
    the event with that matching description is emitted only once.

    **Binary and non-UTF8** files are not supported.

    To emit an event with details ``Report OK`` for files that contain a line with content ``Last report 122344 received with success on 2025-08-23`` you can configure it as::

        [event-handlers/6a28d35e-7948-11f0-8336-5b7f17e6c51e]
        type = content-check
        line_search =
            *report * received with success*, Report OK
            *report * rejected*, Report Fail

    In the above example, when a file contains a line like ``Last report 122344 rejected on 2025-08-23``, an event is emitted with details ``Report Fail``.


digest_format
-------------

:Default value: `disabled`
:Optional: Yes
:From version: 4.31.0
:Values:
    * disabled
    * base64
    * gnu (Default before 5.16.0)
    * bsd
:Description:
    The format used to display the generated digest.

    Use `disabled` to disable the generation of the checksum.

    Use `base64` to only have the base64 representation of the digest,
    without any other text.

    Use `gnu` to have the output in GNU standard.
    This is the `hexadecimal` value followed by the name of the file.
    For example: `9c702f1c77c48a375ac14c987ed7579cbb91f6a2  README.rst`

    Use `bsd` to have the output in BSD tag standard.
    This is the algorithm name, followed by the filename in round brackets and followed by the `hexadecimal` value.
    For example: `SHA1 (README.rst) = 9c702f1c77c48a375ac14c987ed7579cbb91f6a2`


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
