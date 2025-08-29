Locations
=========

..  contents:: :local:


Introduction
------------

Locations can be used to connect to various types of local or remote systems,
including local file systems, SFTP servers, FTP servers, HTTP servers,
and cloud storage services like Amazon S3 or Microsoft Azure Blob Storage.

Supported client-side protocols include:

- **Local Filesystem**: Access files stored on the local machine.
- **SFTP**: Secure File Transfer Protocol for encrypted file transfers.
- **FTP**: File Transfer Protocol for standard file transfers.
- **FTPS (Explicit/Implicit)**: FTP over SSL/TLS for secure transfers.
- **HTTP Pull**: Download files using HTTP requests.
- **WebDAV**: Web Distributed Authoring and Versioning for remote file access.
- **AS2**: Applicability Statement 2 for secure B2B data exchange.
- **Azure Blob/File**: Integrate with Microsoft Azure storage services.
- **SMB**: Server Message Block for network file sharing.
- **Exchange Online**: Connect to Microsoft Exchange for email and file access.
- **SMTP**: Send files via email using Simple Mail Transfer Protocol.

Locations are auto-started when a transfer or another component needs them and
the location is not started and connected.

They are also fault-tolerant, allowing retries for interrupted connections.

Transfers using a failed location will also fail and will
not trigger a new connection attempt for the location.
In this type of scenario, the failed location must be manually started first,
after resolving the initial error.


Adding a new location via Web Manager
-------------------------------------

A new location can be added or changed via Web Manager below.
Options will differ depending on which location type is used.

See below for an example of an initial configuration with the FTPES location.

..  image:: /static/gallery/gallery-add-ftps-location.png


Adding a new location via text configuration
--------------------------------------------

Adding a new location configuration is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``locations/`` and followed by
the location's UUID.

The location's UUID can be any unique string used to identify the location.
Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/introduction>`.

For example, to add a new location configuration of type `filesystem`
called ``Local file system``::

    [locations/b904e6h6-c295-4ccf-8abd-edcae4d3324f]
    name = Local file system
    description = File system accesses as service account.
    type = filesystem
