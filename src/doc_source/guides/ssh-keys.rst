.. container:: tags pull-left

    `client-side`
    `server-side`
    `security`


Generating and converting SSH keys
##################################

..  contents:: :local:


SSH and SFTPPlus
----------------

SFTPPlus, as well as other standard SFTP clients and servers, make use of SSH
DSA and RSA keys for implementing an authentication method that allows partners
to exchange credentials over insecure connections.

When SSH key authentication is used, the credentials are formed by associating
a username to an SSH key pair.
The SSH key pair contains a *public* part and a *private* part.

To exchange credentials, partners will each generate an SSH key pair on their
own computers and will send the *public* part of a key pair to their partner.
Their partner will then use it to configure SFTPPlus to only accept SFTP
clients that can prove they have the *private* part of the key pair.

An SFTP client that only holds the *public* key part of the key pair will not
be able to authenticate itself to SFTPPlus' SFTP service.

SFTP clients and servers can choose to store the SSH key pair in their own
format and unfortunately there is not a single format used by all SFTP software
for storing and managing SSH keys.

This documentation covers SSH key management for some of the most popular SFTP
software.


OpenSSH Project
---------------

The OpenSSH project provides a set of programs that implement encrypted
communication sessions over a computer network using the SSH protocol.
It was created as an open source alternative to the proprietary Secure Shell
software suite offered by SSH Communications Security and is available for many
operating systems such as Linux, macOS, Windows, and many more.

To generate an SSH RSA key pair in OpenSSH format, you will use the
**ssh-keygen** tool distributed together with the OpenSSH project::

    ssh-keygen -t rsa -C "KEY_COMMENT" -f KEY_FILENAME

..  note::
    **ssh-keygen** will ask you to provide a passphrase to be used for
    encrypting the newly generated SSH private key.
    If you enter an *empty* password and the SSH private key will be stored on
    the local disk in unencrypted format.

You can replace *rsa* with *dsa* to generate a DSA key pair.
You can replace ``KEY_COMMENT`` with any text that should help you identify
the key (more so, its purpose) at a later time.

This will generate the following files:

 * ``KEY_FILENAME`` containing the private part of the key
 * ``KEY_FILENAME.pub`` containing the public part of the key


PuTTY Client
------------

PuTTY is a free and open source application which acts as a client for the
SSH, SFTP, SCP, and Telnet protocols.
PuTTY is available on many Unix-like operating systems,
but is most commonly used on Windows.


Unix-like systems
^^^^^^^^^^^^^^^^^

To generate an SSH key pair, PuTTY provides the **puttygen** tool::

    puttygen -t rsa -C "KEY_COMMENT" -o KEY_FILENAME.ppk

..  note::
    ``puttygen`` will ask you to provide a passphrase to be used for
    encrypting the newly generated SSH private key.
    You can enter an *empty* password and the SSH private key will be stored
    on the local disk in unencrypted format.

You can replace *rsa* with *dsa* to generate a DSA key pair.
You can replace ``KEY_COMMENT`` with any text that should help you identify
the key (more so, its purpose) at a later time.

The command will create the ``KEY_FILENAME.ppk`` file that will contain both
the *public* and *private* part of the SSH key pair.

PuTTY stores SSH key pairs in a format that is not compatible with the
OpenSSH project or SFTPPlus.

The **puttygen** tool can be used for converting an SSH key stored in PuTTY
format to a key stored in OpenSSH format.

To extract the private part of an SSH key stored in PuTTY format and store
the result in OpenSSH format::

    puttygen PUTTY_FILE.ppk -O private-openssh -o OPENSSH_FILE

To extract the public part of an SSH key stored in PuTTY format and store
the result in OpenSSH format::

    puttygen PUTTY_FILE.ppk -O public-openssh -o OPENSSH_FILE.pub

The **puttygen** tool also allows converting the private part of an SSH key
stored in OpenSSH format to PuTTY format::

    puttygen OPENSSH_FILE -o PUTTY_FILE.ppk


Windows
^^^^^^^

Puttygen for Windows can be downloaded from::

    http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html

----

Open **puttygen**, select the type of key to generate and the number of bits for
the key.

..  image:: /_static/guides/puttygen-1.png
    :alt: PuttyGen main window

----

Click "Generate" and move your mouse over the blank area until the keys are
generated.

..  image:: /_static/guides/puttygen-2.png
    :alt: PuttyGen generate key process

----

Provide a passphrase to be used for encrypting the newly generated SSH private
key.
You can enter an empty password and the SSH private key will be stored
on the local disk in unencrypted format.

Add a comment that should help you identify the key (more so, its purpose) at a
later time.

..  image:: /_static/guides/puttygen-3.png
    :alt: PuttyGen generated key


Clicking one of the 'Save public key' or 'Save private key' button saves the
SSH key pair in a format that is not compatible with the OpenSSH project.

----

The **puttygen** tool can be used for converting an SSH key stored in PuTTY
format to a key stored in OpenSSH format.

To export an already opened key: Conversions -> Export OpenSSH key.

..  image:: /_static/guides/puttygen-4.png
    :alt: PuttyGen Export key in OpenSSH format

----

To export the public key in OpenSSH format, open a text editor and copy-paste
the contents of the "OpenSSH public key" text box.
Save it as a plain text file.

..  image:: /_static/guides/puttygen-5.png
    :alt: PuttyGen copy public key


Extracting the public key from a PKCS#12 format file
----------------------------------------------------

The *PKCS#12* format is either a .PFX or .P12 file which contains the private
key with its X.509 certificate and also optional CA certificates.

In this example, we will be using the .PEM extension for later use to extract
the OpenSSH public key.

Decrypt and save as .PEM::

    openssl pkcs12 -in certificate-and-key.p12 -nokeys -out certificate.pem

Using the X.509 .PEM encoded certificate, extract the public key by following
the instructions in the next section.


Extracting the public key from the X.509 Certificate
----------------------------------------------------

This section describes the method to extract the *PKCS#8* public key from an
X.509 .PEM encoded certificate using the **openssl** toolkit.
Following that, use the **ssh-keygen** toolkit to convert the OpenSSH public
key.

Use the command below to extract the public key from the X.509 certificate
stored as a .PEM file and save the key into a specified .PUB file::

    openssl x509 -pubkey -noout -in certificate.pem > pubcertkey.pub

The format should look like below in the .PUB file. Note that this is the
public key in *PKCS#8* format::

    -----BEGIN PUBLIC KEY-----
    CONTENT_OF_THE_PUBLIC_KEY
    -----END PUBLIC KEY-----

If the X.509 certificate is not stored as a *PKCS#1* .PEM format, then it is
stored in another format with common ones being .CRT, .CER and .KEY.

**Convert the PKCS#8 format to OpenSSH public format**

Use **ssh-keygen** to convert from *PKCS#8* format::

    ssh-keygen -i -m PKCS8 -f path-to-pcks8.pub

The *ssh-rsa* or *ssh-dss* output may look like below::

    ssh-rsa AAAAB3_CONTENT_OF_THE_KEY_OqLrL8bfLCu/ description

With this format, you can now associate the OpenSSH public key to the account
that requires it either in the Local Manager GUI or in the configuration file.


Obtaining the MD5 fingerprint from an OpenSSH public key
--------------------------------------------------------

To show the fingerprint, save the OpenSSH public key then run **-E md5**
using **ssh-keygen**::

    ssh-keygen -l -E md5 -f my_sshkey.pub

The fingerprint output should look like::

    2048 MD5:25:96:e2:88:0c:a7:49:46:s2:f9:c6:11:m8:3f:ce:e9 (RSA)


SSH Keys Management in SFTPPlus Local Manager
---------------------------------------------

Users can also generate new SSH keys and convert/read existing SSH keys via the
SFTPPlus Local Manager.

..  image:: /_static/gallery/gallery-key-management.png
