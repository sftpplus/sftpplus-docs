Authentication methods introduction
===================================

..  contents:: :local:


Introduction
------------

You can define multiple authentication methods.
You can configure the order in which these methods are used.

It is important to note that authentication methods have different configuration options
for authenticating regular file transfer users compared to SFTPPlus administrators.

In addition, not all authentication method types support authenticating
administrators for the Web Manager service.


Adding a new authentication method via Web Manager
--------------------------------------------------

A new authentication method can be added or changed via Web Manager below.
Options will differ depending on which authentication method is used.

See below for an example starting configuration for the LDAP method of
authentication.

..  image:: /static/gallery/gallery-add-ldap-auth.png


Adding a new authentication method via text configuration
---------------------------------------------------------

Adding a new authentication method is done by creating a new section
inside the configuration file.
The name of the section should be prefixed with ``authentications/`` and
followed by the method's UUID.

The method's UUID can be any unique string used to identify the authentication
method. Once defined, the UUID should not be changed.

For more information, please see
:doc:`the dedicated UUID documentation </configuration/introduction>`.

For example, to add a new authentication method of type `http`
called ``First tier partners``::

    [authentications/b904ed23-a234]
    name = First tier partners
    description = Authentication based on the D.U.S.I. web application.
    type = http


Activating an authentication method
-----------------------------------

Once defined, an authentication method in not used unless activated.
To activate an authentication method, make sure it's added to the ordered list of
active authentication methods for the `server` authentication configuration option.

A custom list of activated authentication methods can also be configured for any service.

In this way, you can define multiple authentication methods for a service and set their priorities.
Once an account is successfully authenticated using a method, SFTPPlus allows the user in
without trying remaining methods in the ordered list of authentications.

The following example will define a configuration in which the
authentication with UUID ``b904ed23-a234`` is tried
first.
If the first method cannot authenticate the account, the server
will try to authenticate it using the method with UUID ``ed123e-4d4724f``.
This allows authenticating external partners using embedded SFTPPlus accounts,
and if the username is not found inside SFTPPlus configuration,
it will try to authenticate it against the internal LDAP server to check whether the username is one of the internal team members::

    [server]
    name = VP server
    description = Frontend for FG partners.

    authentications = b904ed23-a234, ed123e-4d4724f

    [authentications/b904ed23-a234]
    type = application
    name = UK Partners
    allowed_groups = uk-support, uk-sales

    [authentications/ed123e-4d4724f]
    type = ldap
    name = Active Directory LDAP

Stopped authentication methods are skipped.
Credentials are still authenticated against remaining configured authentication methods
until the user is authenticated or the ordered list of authentications is exhausted.

Failed or not yet operational authentication methods are not skipped.
When encountering a method in such a state, user authentication fails immediately.
Remaining configured methods are not tried.


Password Policy
---------------

In SFTPPlus you can define the password policy used when setting new passwords.

NIST's current password guidelines from 2018, as defined in
Special Publication 800-63-3 Digital Authentication Guidelines, include:

* Minimum password length should be 8 characters,
  with a maximum of no less than 64
* All ASCII and UNICODE characters should be allowed
* Check against a list of “known-bad” passwords
* Remove knowledge-based authentication
* Stop practice of regular password expiration
* Don’t allow password hints
* Remove composition rules
  (i.e., “your password needs to contain at least one upper and
  lowercase character and one special character”),
  and instead focus on longer passwords
* Passwords need to be hashed, salted and stretched

Below you can find how SFTPPlus matches the NIST recommendations:

* You can configure the minimum size for passwords, and SFTPPlus allows
  setting passwords as long as 200 characters.
* The default security policy requires a password of minimum 11 characters.
* When the password strength check is enabled,
  passwords are checked against a list of common, weak, or bad passwords.
  The check includes dates and usernames.
* All ASCII and Unicode characters are allowed.
* Knowledge-based authentication and password hints are not
  available in SFTPPlus.
* Passwords are hashed and salted before being stored,
  and these operations are repeated 80.000 times for each password.

The password policy used to check newly defined password is configured via
the following configuration options from the `[server]` section:

* `password_minimum_strength` - enforce a minimum strength
* `password_minimum_length` - enforce a minimum length
* `password_character_requirements` - enforce the character composition of the password
* `password_history` - enforce the number of unique new passwords before an
  old password can be reused.
* `password_hashing_scheme` - defines the function used to hash passwords.

The password strength policy is designed to replace the composite policy rules
that often fail both ways, allowing weak passwords (such as P@ssword1) and
disallowing strong passwords (such as Wow...doestcst).

To require a password policy with a minimum of 12 characters and
`strength` of `best` you can define it as::

    [server]
    password_minimum_strength = 4
    password_minimum_length = 12
    password_history = 10

The password strength is determined using the
`zxcvbn password strength estimator <https://blogs.dropbox.com/tech/2012/04/zxcvbn-realistic-password-strength-estimation/>`_
created by Daniel Lowe Wheeler from Dropbox Inc.


Emailing account credentials
----------------------------

An administrator can send over email the password and the TOTP code
for a new account.
For an existing account, the above can also be sent over email
when updating its credentials.

The following are required in order to send such emails:

* The `Email-Client` resource is configured with a valid email server.
* The account created or modified is defined with an email address as name
  or a dedicated email address is entered for it.

Passwords can only be emailed at account creation or
when updating an account's password.
No other scenario is supported.
This is because the server does not store passwords in a plain text format.
For security reasons,
passwords are stored in a format which makes it practically impossible
to retrieve plain text passwords, even if you have access to the stored values.
