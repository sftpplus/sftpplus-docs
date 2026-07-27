Security Policies
=================

..  contents:: :local:


Introduction
------------

A `security-policy` represents a set of security-related configurations that are applied for the file transfer services.

This section describes the configuration options used to define security policies.

Multiple security policies can be created inside the SFTPPlus configuration.

File transfer services can use the default security policy or can be configured to use a specific security policy.

..  warning::
    Do not configure source IP blocking, if SFTPPlus is behind a Proxy/Gateway or any other network device which does not preserve the source IP address of the
    initial authentication request or does not support Proxy Protocol v2.

    When SFTPPlus is behind a load balancer, make sure that Proxy Protocol version 2
    is enabled on the load balancer.
    Otherwise all the authentication requests will be made using the
    load balancer's own IP address and not the client IP address.

    Check that your network is not vulnerable to
    `IP address spoofing <https://en.wikipedia.org/wiki/IP_address_spoofing>`_.


Default security policy
-----------------------

The `DEFAULT-SECURITY-POLICY` is always present in any SFTPPlus configuration,
and it can't be removed.
This is used by default by any file transfer service that is not configured with a specific security policy.

You can reconfigure a specific file transfer service/protocol to use a different security policy, other than the default one, by setting the `security_policy = OTHER-SECURITY-UUID` option in the service's configuration section.

You can change the configuration options of the default security policy, and it will automatically apply to all file transfer services that don't have an explicit security policy applied.

You can't create a new security policy and assign it as the default security policy.
Update the existing default security policy instead.


Security policies lifecycle
---------------------------

The security policies are automatically started when a file transfer service needs to use them.

You can manually stop a security policy, but it will be automatically started again when a file transfer service needs to use it.

Some configuration changes on the security policies require a restart of the security policy itself, and administrators will have to manually restart the policy.
It is not automatically restarted when a file transfer service needs to use it.


Adding a new security policy via Web Manager
--------------------------------------------

New security policies are added using the Web Manager via the `General -> Configuration` page.


Adding a new security policy via text configuration
---------------------------------------------------

Adding a new security policy is done by creating a new section inside the configuration
file.
The name of the section should be prefixed with `security-policies/` and followed by the policy's UUID.

The policy's UUID can be any unique string used to identify the policy.
Once defined, the UUID should not be changed.

For example, to add a new security policy named **Internal Access**,
where ``78.153.3.0/24`` might be the range of VPN users that are not allowed::

    [security-policies/a805d3a6-4bbf-8abd-a59b]
    name = Internal Access
    description = Security policy designed for internal users.
    deny_usernames = ftp, admin, administrators
    source_ip_filter =
      allow 10.0.0.0/8
      deny 78.153.3.0/24
    source_ip_ban_after_count = 10
    source_ip_ban_interval = 600

Once the security policy is created you can assign it as the security policy for a specific file transfer service::

    [services/1cdff34f-76bc-11f1-a8f3-04cf4b0c43dd]
    name = SFTP server
    type = sftp
    security_policy = a805d3a6-4bbf-8abd-a59b


Source IP filter behavior
-------------------------

When `source_ip_filter` is configured, rules are evaluated in order.
The first matching rule is used and the remaining rules are ignored.

* `allow`:
  access is allowed for the matching source IP/CIDR and all security policy
  checks are suspended, including brute force attack prevention
  (`source_ip_ban_after_count` / `source_ip_ban_interval`).
* `deny`:
  access is denied immediately for the matching source IP/CIDR.

When rules are configured and no rule matches, no explicit source IP decision
is made and the remaining security policy checks continue unchanged.

A matching `deny` rule is also treated as blocked source IP at
connection-time checks.

When `source_ip_filter` is empty, no allow/deny decision is made based on
source IP and all other security policy checks apply for every source IP.

-----

Below you can find the configuration options available for security policies.


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

    Administrator names should be defined in lower-case.

    This list is not used to deny access to the file transfer services.

    Leave this option empty to allow any username to authenticate as an administrator.
    In the INI file, an empty value (e.g., `deny_administrators =`) is treated as an empty list, thus not blocking any administrator.


source_ip_filter
----------------

:Default value: ''
:Optional: Yes
:Values: * List of rules in `action target` format, one rule per line.
         * allow/deny followed by a space-separated valid IP address or CIDR.
:From version: 5.25.0
:Description:
    Source IP access control rules for this policy.
    Each rule uses `allow` or `deny`, followed by a valid IP address or CIDR.
    Example: `allow 192.0.2.10`, `deny 192.0.2.0/24`,
    `allow 2001:db8::10`, `deny 2001:db8::/32`.
    Leave empty to disable source IP based allow/deny rules.


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
