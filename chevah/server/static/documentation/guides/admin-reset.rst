.. container:: tags pull-left

    `server-side`
    `client-side`
    `security`


Resetting Local Manager username and password
=============================================

The Local Manager is a web-based administration interface, access-protected
through username and password credentials.

During initial installation, you are asked to define a username and a
corresponding password for the default administration account.

In the case in which you forget the username or password of the default
administration account, this page describes how to reset it.

Passwords used by SFTPPlus are stored in a protected format based on a
one-way hash function.
Recovering a password from this protected format is not possible.
The only option is to generate a new protected password to replace the
existing one.

To generate a new protected password, use the following command::

    admin-commands generate-password
    Enter password   (not echoed):
    Confirm password (not echoed):
    $5$rounds=80000$iv74TLS39uaogCZA$CfnjEwnGjAOGCnMcC5bD2gK.

Stop the SFTPPlus service, and modify the `configuration/server.ini` file
so that the `[administrators/DEFAULT-ADMINISTRATOR-UUID]` section has
the password generated from the previous step::

    [administrators/DEFAULT-ADMINISTRATOR-UUID]
    enabled = Yes
    name = YOUR-ADMIN-USERNAME
    password = $5$rounds=80000$iv74TLS39uaogCZA$CfnjEwnGjAOGCnMcC5bD2gK.

    role = DEFAULT-ROLE

Once the modified configuration file is saved, you can start the
SFTPPlus service.
You can then login to the Local Manager web page using the new credentials.
