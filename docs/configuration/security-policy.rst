Security Policies
=================

..  contents:: :local:


Introduction
------------

A `security-policy` represents a set of security related configurations that are applied for the file transfer services.

This section describes the configuration options used to define security policies.

Multiple security policies can be created inside the SFTPPlus configuration.

File transfer services can use the default security policy or can be configured to use a specific security policy.

The `DEFAULT-SECURITY-POLICY` is always present in any SFTPPlus configuration,
and it can't be removed.
This is used by default by any file transfer service that is not configured with a specific security policy.


..  warning::
    Do not configure source IPs blocking, if SFTPPlus is behind a Proxy/Gateway or any other network device which does not preserve the source IP address of the
    initial authentication request or does not support Proxy Protocol v2.

    When SFTPPlus is behind a load balancer, make sure that Proxy Protocol version 2
    is enabled on both the load balancer and SFTPPlus file transfer services.
    Otherwise all the authentication requests will be made using the
    load balancer own IP address and not the client IP address.

    Check that your network is not vulnerable to
    `IP address spoofing <https://en.wikipedia.org/wiki/IP_address_spoofing>`_.


Adding a new security policy via Web Manager
--------------------------------------------

New security policies are added using the Web Manager via the `General -> Configuration` page.


Adding a new security policy via text configuration
---------------------------------------------------

Adding a new security policy is done by creating a new section inside the configuration
file.
The name of the section should be prefixed with ``security-policies/`` and followed by the policy's UUID.

The policy's UUID can be any unique string used to identify the policy.
Once defined, the UUID should not be changed.

For example, to add a new security policy named **Internal Access**::

    [security-policies/a805d3a6-4bbf-8abd-a59b]
    name = Internal Access
    description = Security policy designed for internal users.
    deny_usernames = ftp, admin, administrators
    source_ip_ban_after_count = 10
    source_ip_ban_interval = 600


Below you can find the configuration option available for security policies.


name
----

:Default value: ''
:Optional: No
:From version: 5.15.0
:Values: * Any text.
:Description:
    Human-readable short string used to identify this policy.


description
-----------

:Default value: ''
:Optional: Yes
:From version: 5.15.0
:Values: * Any character string.
:Description:
    Human-readable text that describes the purpose of this policy.


deny_usernames
--------------

:Default value: ''
:Optional: Yes
:Values: * Comma-separated list of usernames.
:From version: 5.15.0
:Description:
    Comma-separated list of usernames denied by this policy.

    The check is case-insensitive.

    Usernames should be defined in lower-case.

    Leave empty to not impose any restriction based on the names of users.

    This list is not used to deny access to the Web Manager console.


deny_administrators
-------------------

:Default value: ''
:Optional: Yes
:Values: * Comma-separated list of names.
:From version: 5.15.0
:Description:
    Comma-separated list of administrator names denied by this policy.

    The check is case-insensitive.

    Usernames should be defined in lower-case.

    This list is not used to deny access to the file transfer services.

    Leave this option empty to allow any username to authenticate as an administrator.
    In the INI file, an empty value (e.g., `deny_administrators =`) is treated as an empty list, thus not blocking any administrator.


source_ip_ban_after_count
-------------------------

:Default value: `5`
:Optional: Yes
:Values: * Number of failed attempts.
:From version: 5.15.0
:Description:
    Number of consecutive failed authentications which will result in blocking
    the source IP.

    Set to `0` to disable source IP brute force attack protection.


source_ip_ban_interval
----------------------

:Default value: `3600`
:Optional: Yes
:Values: * Number of seconds.
:From version: 5.15.0
:Description:
    Number of seconds for which authentication requests from the source IP
    are denied.

    Default interval is 1 hour.

    This configuration is ignored when `source_ip_ban_after_count = 0`.
