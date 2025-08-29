Server-side protocols
=====================

This section provides reference documentation for all supported
server-side protocols in SFTPPlus.

Each protocol can be configured individually to meet your security and
operational requirements. Configuration options include:

- Defining listening addresses and ports.
- Enabling or disabling specific protocols.
- Setting authentication methods and user access controls.
- Configuring encryption and certificate settings for FTPS and HTTPS.
- Specifying protocol-specific options, such as passive ports for FTP,
  or endpoint paths for HTTP/AS2.

Refer to the sub-sections below for detailed configuration instructions
for each protocol.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` Introduction
        :link-type: doc
        :link: ./introduction

        Learn how to add, remove, or modify services supported by SFTPPlus using the configuration file or the web-based interface.

    .. grid-item-card:: :octicon:`sliders` FTP / Explicit FTPS / Implicit FTPS
        :link-type: doc
        :link: ./ftp-service

        See the configuration options available for the FTP / FTPS service.

    .. grid-item-card:: :octicon:`sliders` SSH (SFTP and SCP)
        :link-type: doc
        :link: ./ssh-service

        See the available configuration options for the SSH service,
        which includes SFTP and SCP protocols.

    .. grid-item-card:: :octicon:`sliders` HTTP / HTTPS / AS2
        :link-type: doc
        :link: ./http-service

        This section provides details on how to configure the HTTP, HTTPS, and AS2 services.

    .. grid-item-card:: :octicon:`sliders` HTTP redirection
        :link-type: doc
        :link: ./http-redirection-service

        This section provides details on how to configure the HTTP redirection service.


..  toctree::
    :maxdepth: 1
    :hidden:

    introduction
    ftp-service
    ssh-service
    http-service
    http-redirection-service
