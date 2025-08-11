System Requirements
===================


Supported Operating Systems
---------------------------

* Windows 10, 11, 2016 Server, 2019 Server, 2022 Server, 2025 Server on x86_64.

* Red Hat Enterprise Linux 8 and 9 on x86_64.
  Clones such as Oracle Linux, Rocky Linux, AlmaLinux etc. are also supported.
  On request, we provide builds for different architectures
  (x86, POWER8, S390x).
  Make sure the "libxcrypt-compat" package is installed on RHEL 9
  and its clones.

* Amazon Linux 2 and Amazon Linux 2023 (formerly known as Amazon Linux 2022) on x86_64.
  Make sure the "libxcrypt-compat" package is installed on Amazon Linux 2023.

* Ubuntu Server 18.04 LTS, 20.04 LTS, 22.04, 24.04 LTS on x86_64.
  Contact us if you need specific support for a different Ubuntu Linux version
  and/or another hardware platform.

* Alpine Linux 3.13 and newer on x86_64.
  Contact us if you need support for an older Alpine Linux version
  and/or another hardware platform.
  This version is statically-built against required libraries, including OpenSSL.
  This package should work on other musl-based Linux distributions,
  provided musl 1.2 or newer is available.

* Generic Linux distributions on x86_64 and ARM64.
  This version is statically-built against required libraries, including OpenSSL.
  It is designed to work on any modern Linux distribution with
  glibc version 2.26 or newer:
  non-LTS Ubuntu,
  SUSE Linux Enterprise Server (SLES) 15 and newer, OpenSUSE,
  Debian Linux, Slackware, Arch, etc.
  Contact us if you need support for a Linux distribution not based on
  either glibc or musl, or for hardware platforms other than x86_64/amd64 and arm64.
  Make sure the "libxcrypt-compat" package is installed on newer distributions
  such as current Arch Linux.

* Apple macOS 11 Big Sur or newer on Apple Silicon.
  This version is statically-built against required libraries, including OpenSSL.
  Contact us if you need support for macOS on Intel-based Macs,
  including older versions.

Do contact us if your OS of choice is not listed here, we can provide support
for any Unix or Unix-like OS on almost any hardware platform as long as there
is substantial demand for it.

Virtual environments and virtual machines are supported for all platforms,
including: VMWare ESX, VirtualBox, OpenVZ, Docker, WPAR, vWPAR, zones, etc.

SFTPPlus does not include cluster-aware logic, but
it provides generic functionalities for implementing clustering.

We have customers deploying SFTPPlus resilience configuration on MSCS,
Red Hat Linux, and other type of clusters.
To read more about our approach to fault tolerance and zero redundancy
:doc:`deployments please see our guide</guides/fault-tolerant-environment>`.

On MSCS, SFTPPlus can be deployed as a Generic Service
Resource or a Generic Script Resource.


Software Requirements
---------------------

On Windows, there are no 3rd party dependencies, as the OpenSSL libraries
are distributed together with the installation package.
SFTPPlus on Windows should be installed on a path containing only ASCII characters,
and the folder names should be less than 256 characters.
The files handled by SFTPPlus can have longer path names and can include Unicode characters.
The restriction is only for the SFTPPlus installation path.

On Linux, there are some basic system dependencies,
most of which are typically installed by default.
The required OpenSSL libraries are distributed together with the installation package.
On some systems, extra dependencies are required,
for example "libxcrypt-compat" on newer distributions.
We strive to document these exceptions as comprehensive as possible.
The installation and backup paths for SFTPPlus should be on filesystems with support for file capabilities.
By default, both these paths reside in `/opt`.

On macOS, there are no 3rd party dependencies.
All needed libraries, including OpenSSL, are distributed together with the installation package.


Hardware Requirements
---------------------

:CPU:
    The server will run on any CPU released in the last decade.

    Since many of the encryption / decryption operations are CPU-intensive
    operations, using a modern system designed for
    server usage is recommended.

:Memory:
    Between 500 - 800 MB of RAM, depending on CPU architecture.

    Memory usage is approximately 100MB per CPU core.

    Memory usage will increase with the number of concurrent connections.
    No more than 1 MB will be used for a new connection.

:Disk usage:
    Installation size: 750 MB.

:Network usage:
    The server will try to use all available network bandwidth.
    This is normal for Ethernet/IP networks.

    The available bandwidth will be shared by all connections.

    Many of the cryptographic algorithms require a low network latency and
    a network delay not larger than 60 seconds.
