Updates and upgrade
===================

There are 2 classes of software version changes for SFTPPlus:

* updates, where the same first digit in the version number is kept, and
* upgrades, where the first digit in the version number is incremented.

Updates add new functionality, fix defects, and improve security.

Upgrades include all of the above,
but also remove functionalities and introduce backward-incompatible changes.

The backward-incompatible changes introduced in upgrades are typically due to increased security standards.
However, for most such changes, there are backward-compatible options that can be manually enabled.

Upgrades are also used to remove support for obsolete protocols, outdated security mechanisms, and end-of-life versions of supported operating systems.

Before proceeding with an update or an upgrade, ensure that SFTPPlus
and all its file transfer services are stopped.

Then, make sure to backup the SFTPPlus configuration
located inside the "configuration" directory of the installation path.

The previous configuration is automatically updated to the newer version as needed.
Reinitializing the configuration or the service account and groups is not required.

Consult the :doc:`Server Release Notes<../release-notes>`,
as they contain detailed information on the steps required for updating between specific versions.

Below you can find update and upgrade instructions for all versions on every supported operating system.

..  toctree::
    :maxdepth: 1

    windows
    linux-and-macos
    upgrade-to-v5
    upgrade-to-v4
    upgrade-to-v3
    upgrade-to-v2
