ssh_cipher_list
---------------

:Default value: `secure`
:Optional: Yes
:Values: * List of SSH algorithm names.
         * `all`
         * `secure`
         * `fips`
:From version: 3.11.0
:Description:
    This is configured as a comma-separated list of full name for each host public key, key exchange, HMAC or cipher.

    You can find all the names of the supported algorithms on
    :ref:`SSH cryptography page <standards-crypto-ssh>`.

    For SFTP services the configuration must include at least one algorithm from each of:

    * ciphers
    * HMACs
    * key exchanges

    For SFTP service, when no public key algorithm is configured, it will accept any algorithm.

    For SFTP locations the configuration must include at least one algorithm from each of:

    * public key
    * ciphers
    * HMACs
    * key exchanges

    For example,
    to only allow RSA host keys, AES256 in CTR mode with SHA256 HMAC hash and Diffie-Hellman group 14 key exchange with sha256 algorithms,
    the configuration is::

        ssh_cipher_list = ssh-rsa, aes256-ctr, hmac-sha2-256, diffie-hellman-group14-sha256

    The special keyword `secure` contains all the algorithms that we currently consider secure.

    We recommend using the latest version of SFTPPlus,
    for automatic enforcement of any newly-deprecated ciphers via the `secure` list.

    When we update this list of algorithms to exclude any newly-deprecated ciphers,
    your SFTPPlus installations automatically enforce our changes when upgraded
    to a version that contains the updated `secure` list of algorithms.

    The keyword `all` is available for configuring all the supported
    algorithms, including **weak ciphers**.
    This is provided mainly to help with backward compatibility.

    ..  warning::
        Configuring `all` ciphers also enables ciphers no
        longer considered secure by modern standards.

    A pre-defined set of FIPS 140-2 approved ciphers is available by using the
    special `fips` keyword in this configuration.
    When FIPS 140-s ciphers are enabled, any other configured cipher in the
    list is ignored.

    If an unsupported name is used, the component fails to start.

    When the `all` keyword is used, all other values are ignored.
    When the `secure` keyword is used, all other values are ignored,
    including `fips` and explicit ciphers.
    When the `fips` keyword is used, any explicit cipher configuration
    is ignored.

    Only one option from `all`, `secure`, or `fips` should be used at a
    single time.
