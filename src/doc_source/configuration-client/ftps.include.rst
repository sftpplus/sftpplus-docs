ftps_reuse_session
------------------

:Default value: No
:Optional: Yes
:Values: * Yes
         * No
:From version: 4.34.0
:Description:
    When set to `yes`, SFTPPlus sets up and requests the data connection to use the same TLS session as the control connection.

    Set it to `no` to disable TLS session enforcement, which would prevent reusing the TLS session set by the data connection.
    Most FTPS servers support TLS session resumption.
    Some FTPS servers might fail when a TLS session is resumed this way. If this is the case, you can set this option to `no`.
    Even when set to `no`, SFTPPlus uses the same server-side certificate for both the command connection and the data connection.
