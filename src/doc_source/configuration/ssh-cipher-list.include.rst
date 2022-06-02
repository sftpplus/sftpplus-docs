ssh_cipher_list
---------------

:Default value: `secure`
:Optional: Yes
:Values: * List of accepted key exchanges, HMACs and cipher names.
         * `all`
         * `secure`
         * `fips`
:From version: 3.11.0
:To version: None
:Description:
    The full name for each key exchange, HMAC or cipher should be used
    as comma-separated values.

    You can find all the names of the supported algorithms on
    :ref:`SSH cryptography page <standards-crypto-ssh>`.

    The configuration must include at least one algorithm from each of:

    * ciphers
    * HMACs
    * key exchanges

    For example, to only allow AES256 in CTR mode with SHA1 HMAC hash and
    Diffie-hellman group 14 key exchange with sha256 algorithms,
    the configuration will be::

        ssh_cipher_list = aes256-ctr, hmac-sha1, diffie-hellman-group14-sha256

    The special keyword `secure` contains all the algorithms that we
    currently consider secure.
    Should this list of algorithms be updated to exclude any new ciphers
    that have been considered weak,
    SFTPPlus will need to be upgraded to the version that
    contains the updated `secure` list of algorithms.

    The keyword `all` is available for configuring all the supported
    algorithms.
    This is provided mainly to help with backward compatibility and will
    also enable **weak ciphers**.

    ..  warning::
        Configuring `all` ciphers will also enabled ciphers which are no
        longer considered secure by modern standards.

    A pre-defined set of FIPS 140-2 approved ciphers is available by using the
    special `fips` keyword in this configuration.
    When FIPS 140-s ciphers are enabled, any other configured cipher in the
    list is ignored.

    If an unsupported name is used, the component will fail to start.

    When the `all` keyword is used, all other values are ignored.
    When the `secure` keyword is used, all other values are ignored,
    including `fips` and explicit ciphers.
    When the `fips` keyword is used, any explicit cipher configuration
    is ignored.

    Only one option from `all`, `secure`, or `fips` should be used at a
    single time.
