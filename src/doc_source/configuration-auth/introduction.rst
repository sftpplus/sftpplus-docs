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

    [authentications/b904ed23-a234-4ccf-8abd-edcae4d3324f]
    name = First tier partners
    description = Authentication based on the DUSI web application.
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
authentication with UUID ``b904ed23-a234-4ccf-8abd-edcae4d3324f`` is tried
first.
If the first method cannot authenticate the account, the server
will try to authenticate it using the method with UUID ``ed123e-4d4724f``::

    [server]
    name = VSP server
    description = Frontend for FG partners.

    authentications = b904ed23-a234-4ccf-8abd-edcae4d3324f, ed123e-4d4724f

Stopped authentication methods are skipped.
Credentials are still authenticated against remaining configured authentication methods
until the user is authenticated or the ordered list of authentications is exhausted.

Failed or not yet operational authentication methods are not skipped.
When encountering a method in such a state, user authentication fails immediately.
Remaining configured methods are not tried.
