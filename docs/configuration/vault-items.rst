Vault items
===========

Vault items are used to store sensitive information, such as PGP keys, SSH keys, certificates, etc.

The content of a vault item can be stored inside the main .INI configuration file, or in separate external files.
This allows better security practices, such as setting stricter file permissions on the external files.

The vault items themselves can be stored in the main .INI configuration file under sections prefixed with `vault-items/` or in separate file that contains only one or multiple vault items.

You can also have a mix of both approaches, by storing some vault items inside the main configuration file,
and other vault items in separate external files.

..  note::
    It is important to ensure that both the main SFTPPlus .INI configuration file,
    as well as the external vault item files are secured and not accessible by unauthorized users.

This page focuses on configuration options for the vault items.
There is a separate page for the :doc:`vault resource </configuration/vault-resource>` configuration.
Refer to the dedicated
:doc:`Vault administration </administration/vault>` page to find out more on how vault items are used inside SFTPPlus and how to integrate with external key management systems.


Managing vault items via Web Manager
------------------------------------

Vault items can be added or changed via Web Manager using the `Keys and Certificates` section from the left menu.

You can generate new items or import existing ones.


Managing vault items via text configuration
-------------------------------------------

Adding a new vault item is done by creating a new section inside the configuration
file.
The name of the section should be prefixed with ``vault-items/`` and followed by the
item's UUID.

The item's UUID can be any unique string used to identify the item.
Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/introduction>`.

For example, to add a new vault item named **PGP Public Key**::

    [vault-items/7f9935e4-b36d-11f0-9023-2f74a73dcecc]
    name = Acme Inc PGP Public Key
    description = The public key used to encrypt files for Acme Inc partner.
    type = pgp
    content = -----BEGIN PGP PUBLIC KEY BLOCK-----
        mQGiBF6PHJoRBAD5netlVGrX5TKVQ9eoWKD67cwROI0LQHMJAAMxnrhcPogeNcIX
        mo8WY+heFg8onJ5aV+bAhzpMRmC2DcVR3Yvoq64eAx8hSUI6eW5lsc+CseakV8Jc
        ... MORE CONTENT ...
        4i34eph/pg==
        =9ybR
        -----END PGP PUBLIC KEY BLOCK-----


Configuration options
---------------------

Below you will find the available configuration options for vault items.


name
^^^^

:Default value: ''
:Optional: No
:From version: 5.20.0
:Values: * Any text.
:Description:
    Human-readable short string used to identify this item.


description
^^^^^^^^^^^

:Default value: ''
:Optional: Yes
:From version: 5.20.0
:Values: * Any character string.
:Description:
    Human-readable text that describes the purpose of this item.


type
^^^^

:Default value: ''
:Optional: No
:From version: 5.20.0
:Values: * `pgp-public`
         * `pgp-private`
         * `ssh-public`
         * `ssh-private`
:Description:
    The type of vault item.


content
^^^^^^^

:Default value: ''
:Optional: No
:From version: 5.20.0
:Values: * Text content specific to the item type.
         * File path to an external file containing the item content.
:Description:
    The actual content of the vault item.
    This is not exposed to the management API.
    This is used to store private keys, but also public keys or certificates.

    For `pgp-private` and `pgp-public` items,
    this should be the PGP key data in ASCII-armored text format.

    For `ssh-private` and `ssh-public` items,
    this should be the SSH key data in OpenSSH V1 PEM format.

    When configured with an external file path, the content should be prefixed with `external-file:`.
    The path can be either absolute or relative to the SFTPPlus working directory.
