Vault administration
====================

..  contents:: :local:


Introduction
------------

The `vault` resource together with the configured `vault-items` provides a secure way to handle sensitive configuration and operation values.

A `vault-item` stores any sensitive information such as a password, SSL / SSH / PGP
keys, or a key for at-rest file encryption.

This page focuses on vault administration and operation.
Refer to the dedicated
:doc:`Vault configuration </configuration/vault-items>` page to find all the available configuration options.


Vault content storage
---------------------

With all the sensitive information stored as separate `vault-items`,
it is much easier to audit and isolate access to that information.

By using a separate `vault-item` to configure sensitive information,
such as passwords, certificates, or private keys,
you can reduce the administrative overhead when such sensitive information needs to be changed.
For example, if a certificate is used in multiple places inside the configuration,
you only need to update the certificate once in the corresponding `vault-item`.

With the default configuration the `vault-items` are stored unencrypted in the main
.INI configuration file.

For example, this is an example of a **PGP Public Key** that is used for PGP encryption, for which it's safe to store in unencrypted form::

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

To improve security, the content of vault items can be stored in separate external files.
This allows setting stricter file permissions on the external files.
For example, you can store the content of the vault item as a Kubernetes secret
and mount it as a file inside the container where SFTPPlus is running.
The path to that file is specified in the `content` configuration option,
prefixed by `external-file:`.
For example, ``/etc/secrets/acme_inc_pgp_private.key`` is a path where a Kubernetes secret is mounted::

    [vault-items/7f9935e4-b36d-11f0-9023-2f74a73dcecc]
    name = Acme Inc PGP Private Key
    description = The private key used to decrypt files for Acme Inc partner.
    type = pgp
    content = external-file:/etc/secrets/acme_inc_pgp_private.key

The content of the external file will contain only the vault item content.
For example, the content will be only the PGP private, SSH private key or certificate,
without any additional meta-data information like name or descriptions.

When the content of that vault item is updated via the Web manager,
the new content is stored inside the main configuration file,
and not in the external file.


Managing vault items via Web manager
------------------------------------

When using the Web manager to add a new vault item,
the new vault item is stored inside the main configuration file.

When using the Web manager to update the content of vault items,
the new content is stored inside the main configuration file as well.

Vault items stored in an external fault files are read-only inside the Web manager.

SFTPPlus will not update the content of the external files.
The external files are designed to be read-only files,
such as Kubernetes secrets or files mounted inside a container.

You can update the path to the external file via the Web manager.
To do that, use the `Import` functionality and enter the new path inside the textbox,
using the value in the `external-file:NEW/PATH`.
That is, the new path must also be prefixed by `external-file:`.
Then save the changes **without** pressing the `Check content` button.


Trusted certificates
--------------------

When creating or updating a vault item of type `trusted-certificates`,
the imported certificates are added to any existing trusted certificates.

The GUI provides the option to delete one or more certificates from the trusted certificates vault item.

SFTPPlus is distributed with a default set of trusted certificates vault items.
These items can't be deleted or modified.
The content of these vault items are automatically updated when updating SFTPPlus to a newer version.

From the **Web manager**, you can import certificates as text PEM files either by pasting the content or by uploading a file.

You can also import trusted certificates from bundled PFX/P12/PKCS#12 files.
When importing from a PFX/PKCS#12 file, you need to provide the password used to protect the file.


Private certificates
--------------------

The `private-certificate` vault item type is used to store private certificates or certificate signing requests (CSR),
together with their corresponding private keys and optionally the full certificate chain.

When creating or updating a vault item of type `private-certificate`,
you can import the content as PEM or as PFX/P12 files.

The `private-certificate` vault item can only store **a single** private key or CSR.

It can be used to store multiple certificates.
The first configured certificate should be the one corresponding to the private key.
The other certificates are used to build the full certificate chain.

The `private-certificate` vault item can only store **a single** non certification authority certificate. All the other certificates must be certification authority (CA) certificates.

If you need to store multiple certificates that are not CA certificates and which have the same private key,
you need to create multiple `private-certificate` vault items.

If you need to store multiple certificates without private keys,
use the `trusted-certificates` vault item type.

From the **Web manager**, you can import certificates together with their private keys as text PEM format or as PFX/P12/PKCS#12 files.
When importing from a PFX/PKCS#12 file, you need to provide the password used to protect the file.


Self-signed certificate
-----------------------

In SFTPPlus, the self-signed certificate are handled as `private-certificate` vault items.

To generate a new self-signed certificate via the Web manager,
create a new vault item of type `private-certificate` and then use the `Generate` functionality.

You can import self-signed certificates from PEM files or from PFX/P12/PKCS#12 files as well, as part of the `private-certificate` vault item type `Import` functionality.


Certificate signing request (CSR)
---------------------------------

In SFTPPlus, the certificate signing requests (CSR) are handled as `private-certificate` vault items.

To generate a new CSR via the Web manager,
create a new vault item of type `private-certificate` and then use the
`Generate` functionality.

After the CSR is generated you can export the CSR from the Web manager in PEM text format
and send it to a certificate authority (CA) to obtain a signed certificate.

Once you received the signed certificate from the CA,
you can import it back into the same `private-certificate` vault item via the Web manager using the `Import` functionality and delete the CSR content.

Unless the signed certificate is imported back into the same `private-certificate` vault item,
the private certificate can't be used for SSL/TLS connections.


Loading vault items from an external file
-----------------------------------------

Via the `vault` resource configuration,
you can specify an external file from where to load multiple vault items.

..  note::
    Loading vault items from an external file is not designed to be managed using the Web manager GUI.
    This is useful when using container or Kubernetes secrets to store the vault items in a read-only file.

Below is an example of a `vault` resource configuration that loads vault items from an external file at `/etc/secrets/vault-items.ini`::

    [resources/DEFAULT-VAULT]
    type = vault
    name = SFTPPlus Vault
    description = Stores sensitive information such as PGP keys, SSH keys...

    external_vault_file = /etc/secrets/vault-items.ini

The content of the external file is .INI formatted and can contain multiple vault items.
It's important that each vault item section name is prefixed with `vault-items/` and has a unique identifier.

For example, the content of the external file `/etc/secrets/vault-items.ini` could be::

    [vault-items/fe05dc22-c3e2-11f0-b316-7fa98849d3b3]
    name: SSH Private Key
    type: ssh-private

    content:
    -----BEGIN OPENSSH PRIVATE KEY-----
    b3BlbnNzaC1rZXktdjEA...
    yc4Zi4pnCXMUALY98psnAAAACmFkaUBpbnMtMTMBAgM=
    -----END OPENSSH PRIVATE KEY-----

    [vault-items/s1e5e4888-c3e3-11f0-9af6-17be09719478]
    name: SSH Public Key
    type: ssh-public
    content:
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINlQ5nF5gyy2i4pnCXMUALY98psn sftp@vm1
