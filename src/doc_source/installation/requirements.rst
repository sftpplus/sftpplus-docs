System Requirements
===================


Supported Operating Systems
---------------------------

* Windows 8, 10, 2012 Server, 2012R2 Server, 2016 Server, 2019 Server,
  2022 Server on x86_64.
  On request, we can provide an x86 build for 32-bit Windows.

* Red Hat Enterprise Linux 5, 6, 7, 8, 9 on x86_64.
  Version 5.11 (Final) is required on RHEL 5.
  Clones such as CentOS, Oracle Linux, Rocky Linux, etc. are also supported.
  On request, we provide builds for different architectures
  (x86, POWER8, S390x).
  Make sure the "libffi" package is installed on RHEL 8 and its clones.
  Make sure the "libxcrypt-compat" package is installed on RHEL 9
  and its clones.

* Amazon Linux AMI 2018.03, Amazon Linux 2, Amazon Linux 2022 on x86_64.
  Make sure the "libxcrypt-compat" package is installed on Amazon Linux 2022.

* Ubuntu Server 14.04 LTS, 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04 LTS on x86_64.
  Contact us if you need specific support for a different Ubuntu Linux version
  and/or another hardware platform.
  Alternatively, you can also try the generic Linux package
  featuring static OpenSSL libraries.

* Alpine Linux 3.12 and newer on x86_64.
  Contact us if you need support for an older Alpine Linux version
  and/or another hardware platform.
  This version is statically-built against required libraries,
  including OpenSSL 1.1.1.
  This package should work on other musl-based Linux distributions,
  provided musl 1.1.24 or newer is available.

* Generic Linux distributions on x86_64.
  This version is statically-built against required libraries,
  including OpenSSL 1.1.1.
  It is designed to work on any modern Linux distribution with
  glibc version 2.5 or newer:
  Ubuntu Server older than 14.04 LTS, non-LTS Ubuntu,
  SUSE Linux Enterprise Server (SLES) 11 and newer, OpenSUSE,
  Debian Linux, Slackware, Arch, etc.
  Contact us if you need support for a Linux distribution not based on
  either glibc or musl. Or for hardware platforms other than x86_64/amd64.
  Make sure the "libxcrypt-compat" package is installed on newer distributions
  such as current Arch Linux.

* Apple macOS 10.13 High Sierra or newer on x86_64.
  This version is statically-built against required libraries,
  including OpenSSL 1.1.1.
  macOS 10.12 Sierra is also known to work, but it's not supported.
  Contact us if you need support for an older Mac OS X version.

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

On Linux, the product typically uses the OpenSSL libraries available on the OS.
As such, we recommend that a recent version of the OpenSSL libraries
are installed to benefit from the latest security fixes.
However, the generic Linux package and the Alpine Linux one
are bundled with their own OpenSSL 1.1.1 libraries.

On macOS, there are no 3rd party dependencies, as the OpenSSL libraries
are distributed together with the installation package.


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
