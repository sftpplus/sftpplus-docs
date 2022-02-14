HTTP / HTTPS Service
====================

..  contents:: :local:


General description
-------------------

The `http` / `https` service allows the same level of file access as the
other available file transfer services, such as FTPS or SFTP.

When configured for a ``some.example.com`` address and the ``18080`` port, the
service will be available at the URL ``http://some.example.com:18080``, and it
will redirect users to the start URL ``http://some.example.com:18080/home/``.

As this page focuses on configuration options, please refer to the dedicated
:doc:`HTTP/HTTPS operations</operation/http>` page.


Configuration options
---------------------

Below you can find the list of available configuration options.


languages
^^^^^^^^^

:Default value: `en`
:Optional: Yes
:Values: * Language ISO code
:From version: 4.14.0
:Description:
    This configures the language for the web file transfer
    client user interface.

    The available languages are:
    * `en` - English

    When left empty, it will default to English.


ui_version
^^^^^^^^^^

:Default value: ui-gen-1
:Optional: Yes
:Values: * ui-gen-1
         * ui-gen-2
:From version: 4.16.0
:Description:
    This defined the UI variant to be used for the web file manager.

    The latest version is `ui-gen-2`.

    To use the legacy UI found in SFTPPlus version 4.15.0 or older, set this
    to `ui-gen-1`.


theme_path
^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Absolute path on the local filesystem.
:From version: 3.42.0
:Description:
    Absolute path to a local directory containing the files required to
    customize the HTTP transfer service.

    The folder needs to contain at least the 'main.css' and `main.js` files.

    Leave it empty when you don't want to customize the appearance of the
    HTTP file transfer service.

    You can find more information on the usage of a theme path on the
    :doc:`HTTP/HTTPS operations</operation/http>` page.

    ..  note::
        The `theme_path` configuration option is only valid with the legacy
        web UI version `ui-gen-1`.
        For any other configuration option, it is ignored.


public_account_uuid
^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * UUID to application account.
         * Empty.
:From version: 3.40.0
:Description:
    This configuration option can be used to make a set of files available
    over HTTP/HTTPS without requiring an username or password.

    The files for this account will be available under the `/public/` URL
    or another suffix of your choosing, as configured for `public_name`.

    Leave it empty to not allow public access.
    Trying to access the '/public/' URL will result in
    `404 Page Not Found` error.

    Credentials will still be required when accessing the '/home/' URL,
    which is dedicated to the private/protected access.

    Using a dedicated application account to configure public access allows
    you to set fine grained access to the public files.
    The public files are not limited to read-only access.

    Only application accounts defined in the main configuration are
    supported.
    OS accounts or external application accounts are not supported.


public_name
^^^^^^^^^^^

:Default value: `public`
:Optional: Yes
:Values: * Name of the URL fragment.
         * `ROOT`
:From version: 4.3.0
:Description:
    This defines the URL name under which the public files are available.

    For example, when `public_name = public-access`, public files are
    available under an URL ending with `/public-access`, such as
    `https://www.domain.com/public-access`.

    Set it to `ROOT` to have nothing special appended to the URL
    corresponding to the root of the HTTP/HTTPS file transfer service.

    When this is empty, the default value of `public` is used.

    This configuration is ignored when `public_account_uuid` is not defined.


as2_receive_name
^^^^^^^^^^^^^^^^

:Default value: `as2receive`
:Optional: Yes
:Values: * Name of the URL fragment for AS2 receive requests.
:From version: 4.5.0
:Description:
    This defines the URL name used to receive AS2 requests.

    For example, when `as2_receive_name = as2receive`, AS2 files should be
    sent to URL like: `https://www.domain.com/as2receive`.


as2_receive_path
^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Path to a directory in the user's home folder.
         * Empty
:From version: 4.5.0
:Description:
    This defines the path used to store the files received via AS2 for each
    user.

    This is a path relative to the home path of each user.

    For example, when `as2_receive_path = /as2/receive`,
    and an account has `home_folder_path = C:/Users/JohnD`,
    files received through AS2 are stored in `C:/Users/JohnD/as2/receive`.

    Leave it empty to store the files in the account's root home directory.


as2_default_filename
^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Fixed name for a file
         * Template for filename.
:From version: 4.14.0
:Description:
    This defines the file name used to store the received AS2 data when
    there are no AS2 request headers for the file name.

    When this configuration is empty, and the AS2 request doesn't include a
    filename, the data is stored using a file named
    `as2-received-file.TIMESTAMP`.

    This can also be configured as a file name template.
    For example, with the following configuration the actual file name created
    to store the received data will look like `john_d-20210902T174910.xml`,
    where `john_d` is the name of the account uploading the file::

        as2_default_filename = {account.name}-{timestamp.iso_8601_compact}.xml

    The following variables (case-insensitive) are provided as context data
    containing information about the event being triggered:

    * `uuid`
    * `account.name`
    * `account.peer.address`
    * `account.peer.port`
    * `account.peer.protocol`
    * `account.uuid`
    * `timestamp.cwa_14051`
    * `timestamp.iso_8601`
    * `timestamp.iso_8601_fractional`
    * `timestamp.iso_8601_local`
    * `timestamp.iso_8601_basic`
    * `timestamp.iso_8601_compact`
    * `timestamp.timestamp`


as2_receive_certificate
^^^^^^^^^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Certificate key in PEM format.
         * Empty
:From version: 4.5.0
:Description:
    This defines the certificate associated with the private key used to
    sign the message disposition notification (MDN) response.

    This configuration option can also contain the private key associated
    with this certificate.

    Leave it empty to use the general server certificate.


as2_receive_key
^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * RSA private key in PEM format.
         * Empty
:From version: 4.5.0
:Description:
    This defines the private key used to decrypt the files received via AS2
    and to sign the message disposition notification (MDN) responses.

    Leave it empty to use the general server private key.


triggers
^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Comma-separated values.
         * Action name, Button Colour, Optional Group UUID
:From version: 3.54.0
:Description:
    This configuration allows defining one or more custom buttons for the
    client web interface.

    You can define multiple trigger buttons, one definition per line.

    The first value is the name of the trigger and the text shown on the
    button.
    The second value is the type of the button and is defined as a button
    colour.

    The third value is optional and defines the group of users for which
    the trigger is available.
    When not defined, the trigger is available to all groups.

    Leave it empty to not show any additional buttons in the client web
    interface.

    You can find more information on the usage of trigger buttons on the
    :doc:`HTTP/HTTPS operations</operation/http>` page.


metadata_fields
^^^^^^^^^^^^^^^

:Default value: Empty
:Optional: Yes
:Values: * Empty
         * Name of HTTP header.
         * key name matching expression, list of options
:From version: 4.15.0
:Description:
    This is used to configure the expected metadata header used making an
    HTTP API requests.

    This is configured as a multi-line option.

    The first line contains the name of the header used to extract the
    associated metadata and an optional list of header options.

    The following lines contain comma separated definitions for the expected
    key/value metadata.

    The first value on each line is the name of the metadata key
    or a matching expression for the metadata key.

    The other values from the line are one of the following options:

    * optional - request is processed even if metadata is missing
    * required - request fails if metadata is not provided in the request

    Leave it empty to not process any metadata for file operations.

    When the metadata header name is configured without any key/value
    specification the request will accept any provided metadata and will
    handle them as optional.

    The requested HTTP header value should be a
    `key=value` `comma separated values (CSV)
    <https://datatracker.ietf.org/doc/html/rfc4180>`_ list.
    For example the following HTTP header::

        X-Metadata: tag=report, tag=monthly, project-owner=John Doe

    is parsed as the following JSON structure::

        {
        "tag": ["report", "monthly"],
        "project-owner": ["John Doe"]
        }

    The simplest configuration in which any value from the `x-sftpplus`
    header is accessible is::

        metadata_fields = x-sftpplus

    A more complex configuration example in which:

    * the `x-metadata` header is required and expected to have
      the `tag` key/value fields, and
    * keys starting with `project-` are accepted but optional.

    The request will succeed if the `x-metadata` header is not provided,
    as by default the processing of the header is optional::

        metadata_fields =
          x-metadata
          tag, required
          project-*, optional

    If you require a set of predefined keys but also accept any arbitrary
    keys, you can configure it as below.
    This will fail if the `x-metadata` HTTP header is not provided.
    This will fail if the `tag` metadata is not provided in the header's value
    and will accept any other extra metadata::

        metadata_fields =
          x-metadata, required,
          tag, required
          *, optional

    You can find more information on API requests with a metadata header on the
    :doc:`HTTP REST API</developer/http-api>` page.


announce_session_authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default value: `yes`
:Optional: Yes
:Values: * `yes`
         * `no`
:From version: 3.40.0
:Description:
    When set to `no` the session authentication is still available, but it
    will not be advertised as part of the `www-authenticate` header.


..  note::
    SSL-specific options are only available for the `https` service type.

..  warning::
    When the `ssl_certificate_authority` configuration option is enabled,
    web browsers should include an SSL certificate signed by the same
    certificate authority.

.. include:: /configuration/service-http.include.rst
