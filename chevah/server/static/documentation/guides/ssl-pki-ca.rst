.. container:: tags pull-left

    `client-side`
    `server-side`
    `security`


Working with SSL certificates, PKI and CA
#########################################

..  contents:: :local:


Supported country codes
-----------------------

SFTPPlus supports generated certificate signing requests using country
codes as specified by the
`ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_
standard codes.

`Exceptionally reserved
<https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Exceptional_reservations>`_
codes as assigned by ISO 3166/MA are also supported.

In case you require to generate a CSR using a country code not
currently supported by SFTPPlus, please contact us.


Generating self-signed certificate
----------------------------------

You can generate a self-signed certificate using the following command::

   openssl req \
     -x509 -nodes -days 365 \
     -newkey rsa:1024 -keyout certificate_key.pem -out certificate.pem

To generate a valid certificate, the Common Name (CN) fields should be set to
the server address (for server certificates) or the client username (for client
certificates).

The command will generate the following files:

 * ``certificate_key.pem`` - private key file, to be used only by the
   certificate holder.
 * ``certificate.pem`` - public certificate file that can be used by all peers
   who want to validate the certificate holder's identity.


Mutual authentication using only self-signed certificates
---------------------------------------------------------

First, you will need to create two pairs of self-signed certificates and keys
for the client and server.

You should have the following files:

 * ``server_key.pem`` - server private key
 * ``server_cert.pem`` - server self-signed certificate
 * ``client_key.pem`` - client private key
 * ``client_cert.pem`` - client self-signed certificate

To connect and validate the server, the client will use the following files:

 * ``client_cert.pem`` and client_key.pem for identifying the client to the
   server
 * ``server_cert.pem`` as the accepted Certificate Authority

To accept and validate the client, the server will use the following files:

 * ``server_cert.pem`` and server_key.pem for identifying the server to the
   client
 * ``client_cert.pem`` as the accepted Certificate Authority
