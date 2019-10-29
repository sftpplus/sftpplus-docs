System Requirements
===================


Supported Operating Systems
---------------------------

* Windows 8, 10, 2012 Server, 2012R2 Server, 2016 Server, 2019 Server.
  Full support on X86 and X86_64 architectures.

* Red Hat Enterprise Linux 7 on X86_64.
  On request, we provide builds for older versions (RHEL 5 or 6) or
  different architectures (x86, POWER8, S390x).
  Make sure the "libffi" package is installed.

* Amazon Linux 2 AWS on X86_64.
  For the older Amazon Linux AMI 2018.03 on X86_64, we support the use of
  the RHEL 7 package.

* SUSE Linux Enterprise Server 11 SP4 (with or without the Security Module)
  and 12 SP3 on X86_64.

* Debian Linux 9 on X86_64.
  Contact us if you need support for a different Debian Linux version
  and/or another hardware platform.

* Ubuntu Server 18.04 LTS on X86_64.
  Contact us if you need support for an older Ubuntu server version
  and/or another hardware platform.

* Alpine Linux 3.7 on X86_64.
  Contact us if you need support for a newer Alpine Linux version
  and/or another hardware platform.

* Apple macOS 10.13 High Sierra and 10.14 Mojave on x86_64.
  This version is built against OS-provided LibreSSL libraries version 2.2.7.
  Contact us if you need support for macOS 10.12 Sierra
  or for an older version of OS X.

Do contact us if your OS of choice is not listed here, we can provide support
for any Unix or Unix-like OS on almost any hardware platform as long as there
is substantial demand for it.

Virtual environments and virtual machines are supported for all platforms,
including: VMWare ESX, VirtualBox, OpenVZ, Docker, WPAR, vWPAR, zones, etc.

SFTPPlus does not include cluster-aware logic, but
it provides generic functionalities for implementing clustering.

We have customers deploying SFTPPlus resilience configuration on MSCS,
Red Hat Linux, and IBM AIX clusters.
To read more about our approach to fault tolerance and zero redundancy
`deployments please see our guide <guides/fault-tolerant-environment>`_.

On MSCS, SFTPPlus can be deployed as a Generic Service
Resource or a Generic Script Resource.


Software Requirements
---------------------

On Windows, there are no 3rd party dependencies, as the OpenSSL libraries
are distributed together with the installation package.

On Linux, the product typically uses the OpenSSL libraries
available on the OS.
As such, we recommend that a recent version of the OpenSSL libraries
are installed to benefit from the latest security fixes.

On macOS, you will need to install the OpenSSL 1.0.2 libraries
provided by the Homebrew community.


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
