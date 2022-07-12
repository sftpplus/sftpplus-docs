# Copyright (c) 2021 Adi Roiban.
# See LICENSE for details.
"""
Extensions to add custom MFA to SFTPPlus LDAP authentication.
"""
from __future__ import unicode_literals


class AuthLDAPNoop(object):
    """
    This is an LDAP authentication extension that has no extra functionality.

    It servers as a documentation for the extension interface.

    The extension is implicitly started at initialization.
    """

    def __init__(self, configuration):
        """
        Called when the associated LDAP authentication starts.

        :param configuration: A text which can be formatted as JSON.
            But each extension can parse it as it wants.
            JSON format is not required. It is only recommended.
        """

    def stop(self):
        """
        Called when the extension is no longer used.
        """

    def updateCredentials(self, credentials):
        """
        Called before BIND to allow mutating the credentials.

        This can be used to mutate the credentials to be used during the
        BIND operation.
        """

    def getExtraAttributes(self):
        """
        Return the list of extra LDAP attributes to be used during the entry
        search operation.
        """
        return []

    def augmentEntry(self, entry, credentials, ldap_client):
        """
        Called after BIND was successful and we got the LDAP entry for the
        account.

        Raises
            chevah.server.commons.exception.ServerException
            on any error condition, with a text containing the error details.

        :param entry: The LDAP entry that was just authenticated.
        :param credentials: Used for the authorization to LDAP server.
        :param ldap_client: A LDAP client that is already authenticated and
            that can be used for further LDAP operations.
        :param base_dn: The base_dn from which the account was authenticated.

        :return: The augmented LDAP entry on success.
        """
        return entry
