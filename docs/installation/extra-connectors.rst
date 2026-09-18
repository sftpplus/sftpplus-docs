Extra connectors for Linux
==========================

Extract the extra-connectors archive into the root of your SFTPPlus installation,
then make the `bins` and `ibm-mq` directories owned by the SFTPPlus service user.
For the default installation at `/opt/sftpplus` and service user `sftpplus`,
stop SFTPPlus and run::

    sudo systemctl stop sftpplus-service
    sudo tar -xzf sftpplus-extra-connectors-linux-x64-1.0.tar.gz -C /opt/sftpplus
    sudo chown -R sftpplus:sftpplus /opt/sftpplus/bins
    sudo chown -R sftpplus:sftpplus /opt/sftpplus/ibm-mq

Use your installation path and service user if they differ from these defaults.
Complete the startup configuration below before restarting SFTPPlus.
For installations without systemd, use your usual service commands to stop and start SFTPPlus.

Starting with SFTPPlus 6.0.0, the IBM MQ C client and Microsoft Purview SDK libraries for Linux are distributed in a separate, optional archive.
This reduces the size of the main installation package and speeds up installation for customers who do not use these connectors.
Windows packages continue to include both sets of libraries.

Download `extra connectors 1.0 for Linux x64 <https://www.sftpplus.com/downloads/extra-connectors/sftpplus-extra-connectors-linux-x64-1.0.tar.gz>`_.
The archive version is independent of the SFTPPlus product version.
It is intended for Linux on x86_64 using glibc, and does not support ARM64 or Alpine Linux.

The archive creates `ibm-mq` and `bins` directly inside the installation directory.
It also includes a `README` with redistribution information and vendor licence notices.


Startup configuration
---------------------

For IBM MQ connections, the service must include the client library directories in `LD_LIBRARY_PATH`.
New SFTPPlus installations generate this setting automatically.
When upgrading an existing installation, update the installed systemd unit or other startup script.

For systemd, run `sudo systemctl edit sftpplus-service` and add::

    [Service]
    Environment="LD_LIBRARY_PATH=/opt/sftpplus/ibm-mq/lib64:/opt/sftpplus/ibm-mq/gskit9/lib64"

If your existing `LD_LIBRARY_PATH` contains other required directories,
retain those directories in the value.
Reload the service configuration and restart SFTPPlus::

    sudo systemctl daemon-reload
    sudo systemctl restart sftpplus-service

For a custom startup script, export the equivalent value before launching SFTPPlus::

    export LD_LIBRARY_PATH="/opt/sftpplus/ibm-mq/lib64:/opt/sftpplus/ibm-mq/gskit9/lib64"

SFTPPlus 5 installed the IBM MQ libraries under `/opt/sftpplus/lib/ibm-mq`.
SFTPPlus 6 uses `/opt/sftpplus/ibm-mq`.
Install the extra-connectors archive and replace references to the old paths before starting an IBM MQ location after the upgrade.

The Purview extension loads its SDK from `bins` and configures the SDK library path automatically.
See `bins/README-Purview` for an example extension configuration.
For IBM MQ configuration, see :doc:`/operation-client/ibm-mq`.


Updates
-------

The automated and assisted SFTPPlus update scripts leave `bins` and `ibm-mq` in place,
and keep them owned by the SFTPPlus service user.
These directories also remain in place when rolling back an update.
They are not included in the automatic installation backups.
The scripts do not download updates to the extra connectors.

When a new extra-connectors version is available,
stop SFTPPlus, back up the existing connector directories,
replace them with the contents of the new archive, and set their ownership again before restarting.
For a manual SFTPPlus upgrade to a different installation directory,
copy both connector directories and preserve their permissions and ownership.
