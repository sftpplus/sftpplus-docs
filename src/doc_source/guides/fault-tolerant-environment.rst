.. container:: tags pull-left

    `server-side`
    `infrastructure`
    `administration`


Integrating with fault tolerant and resilient environments
==========================================================

..  contents:: :local:


Introduction
------------

The SFTPPlus software stands at the OSI Layer 7 or the TCP Layer 4
(application).
In order to have a fully fault tolerant system, you need to implement
resilience at all the other layers including the OS.
SFTPPlus can be integrated with external tools in order to meet the
requirements for a fault tolerant infrastructure.


Active-Passive Scenario
-----------------------

In this infrastructure scenario, the second system is offline and only
commences when the main SFTPPlus system is down.

Since the ``server.ini`` configuration is stored in a single file, you can
create a file copy task to keep the system configurations in sync.
Make sure to also transfer additional files that are required - such as SSH
keys, and SSL keys and certificates - to ensure a smooth transition.
When it is time to use the secondary system, the SFTPPlus instance will then
read the latest ``server.ini`` configuration file.


Active-Active Scenario
----------------------

In this infrastructure scenario, both SFTPPlus systems are receiving
and processing requests.
If one system goes down, the other will handle all the requests.

To implement SFTPPlus in this scenario, a simple file copy will not work.
This is because running SFTPPlus instances will not check changes in the local
file configuration (``server.ini``) in order to reconfigure.
In addition, there are other files that are also required - such as all SSH keys
in use and other related files, all SSL certificates required, any logs that
need to be kept for auditing purposes, any externally referenced scripts used in
pre- and post- transfer processing, and so on.

One method of achieving an active/active implementation is to manually set up
the 2 nodes to rely on a
:doc:`single external authentication </configuration-auth/index>` method
(HTTP, LDAP, or external file).
In this way, accounts are managed in the single external system, and
those accounts will be automatically available for both SFTPPlus instances.

Another method, is to have multiple instances sharing the same configuration
folder.
Each SFTPPlus instance will be executed on a separate VM, but they will have
the same configuration files.
Note that in this case you should make sure that you use the Web Manager
of only one instance to make configuration changes.
Once configuration changes were done, the other instances need to be
manually restarted.
Each SFTPPlus instance needs to have its own log file. To ensure that each
instance has its own log file, make sure that each instance has an unique name
and then set up the log file path using the `{host.name}` variable.
In this case, the local file event handler might look like the following
example::

        [event-handlers/b904ed23-a234-4ccf-8abd-edcae4d3324f]
        enabled = yes
        name = Log File
        type = local-file
        path = /var/logs/sftpplus-{host.name}.log
