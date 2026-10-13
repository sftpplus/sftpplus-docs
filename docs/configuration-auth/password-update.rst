Password updates and recovery
=============================

Password changes require users to know their current valid password before
choosing a new one. The `allow_own_password_change` group permission controls
whether users can change their own passwords.

Password recovery lets users choose a new password without knowing the current
one. They must have access to an email address configured on their account and
to the recovery link sent to that address.

The `allow_password_recovery` group permission is independent of
`allow_own_password_change`. Disabling password changes does not disable
recovery, and disabling recovery does not prevent permitted password changes.
Both operations require the new password to meet the server's password policy.

Password recovery requirements
------------------------------

Email password recovery is available only for local application accounts with
passwords managed by SFTPPlus. It is not available for administrator accounts.

..  note::

   Accounts authenticated through external systems, such as Active Directory,
   LDAP, the operating system, or Microsoft Entra ID, cannot use SFTPPlus
   password recovery. SFTPPlus does not manage their passwords. Use the
   recovery method provided by the relevant external authentication system.

An account must meet all of these requirements:

* It is enabled and has a password.
* It belongs to valid, enabled groups and is not expired.
* Its primary group has the `allow_password_recovery` permission. A permission
  set on a secondary group does not grant recovery.
* It has at least one configured email address, and that address is not
  configured on another account.

Any email address configured on the account can be used for recovery.

Security and privacy during recovery
------------------------------------

..  warning::

   Enabling password recovery creates a security risk: anyone who can access an
   account's configured email address can request a link and replace its
   SFTPPlus password. Enable recovery only when this risk is acceptable.

To prevent account discovery, the recovery request page always shows the same
success confirmation after a request is accepted. It does not reveal whether
the email belongs to an account or whether a matching account is disabled or
otherwise ineligible. SFTPPlus checks eligibility and sends email in the
background. Service settings and rate limits can still prevent a request from
being accepted.

Recovery requests are kept in memory. Restarting the HTTP or HTTPS service, or
restarting SFTPPlus, invalidates outstanding links for the affected services.
Users can request a new link after a restart.

Each link expires after 15 minutes and can be used once. A new request
invalidates earlier links for that account. If a password is rejected by the
password policy, the user can retry with the same unexpired link. Each HTTP or
HTTPS service accepts up to ten recovery requests per source IP address in a
10-minute window. Further requests do not send email.

The recovery form does not show the current password policy, including
password length, strength, or allowed characters. This avoids exposing policy
details to people who have not authenticated. If a password does not meet the
policy, the form shows a general error and lets the user try again with the
same unexpired link. After authentication, users changing their own password
can see the current restrictions.

Password changes
----------------

Set `allow_own_password_change = Yes` on a group to let its users change their
own passwords using their current valid password. See :doc:`groups` for the
group permission.

Password recovery
-----------------

#. Configure the default :doc:`Email Client resource
   </configuration/email-client>` to deliver recovery emails.
#. On the account's primary group, set the `allow_password_recovery` group
   permission to `Yes`. Additional groups do not grant this permission. See
   :doc:`groups` for details.
#. Configure the HTTP or HTTPS service to use the latest Web Client UI
   generation and set `base_url` to the service's public address, for example
   `https://files.example.com`. Use HTTPS to protect recovery links and
   passwords in transit.
#. Set the service's `allow_password_recovery` option to `Yes` and restart the
   service. A missing or invalid `base_url` prevents the service from
   starting. See :doc:`/configuration-server/http-service` for the service
   options.

Recovery emails use the HTTP or HTTPS service's primary language, the first
entry in its `languages` option. If no language is configured, or a
translation is unavailable, the email uses English.

In the Web Manager, the account page displays its primary group's recovery
permission. The **Test** button next to the service's **Public URL** checks
access from your browser, including for public addresses the server cannot
reach from its own network. This public URL is used to create recovery links.

See :doc:`/operation/http` for the user workflow, link lifetime, and audit
logging.
