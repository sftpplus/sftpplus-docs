name
----

:Default value: ''
:Optional: Yes
:From version: 2.10.0
:Values: * Any text.
:Description:
    Human-readable short text used to identify this method.


description
-----------

:Default value: ''
:Optional: Yes
:From version: 2.10.0
:Values: * Any text.
:Description:
    Human-readable text that describes the purpose of this authentication
    method.


type
----

:Default value: ''
:Optional: No
:From version: 2.10.0
:Values: * `application` - Application accounts.
         * `os` - Accounts authenticated by the OS.
         * `http` - HTTP (unsecured).
         * `ip-time-ban` - Ban an IP address for a time interval.
         * `deny-username` - Deny authentication based on usernames.
         * `anonymous` - Anonymous account authentication.
         * `ldap` - Authenticate against an LDAP server.
         * `local-file` - Authenticate the accounts from a separate local file.
         * `radius` - Authenticate via a RADIUS server.
         * `entra-id` - Microsoft Entra ID
         * `google-identity` - Google Identity
:Description:
    This option specifies the type of the method. Each type has a set
    of specific configuration options
