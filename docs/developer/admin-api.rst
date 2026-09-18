Web Manager API
===============

The Web Manager provides a JSON-RPC 2.0 API for reading configuration, applying changes, and operating SFTPPlus components.
It uses the same administrator accounts and :doc:`role permissions </administration/admin-authorization>` as the Web Manager console.

Send HTTP POST requests to `/json` on the :doc:`Web Manager service </configuration/local-manager>`.
For example, use `https://sftpplus.example.com:10020/json`, replacing the host and port with those of your installation.
If the service has a `base_url_path`, add it before `/json`.


Requests and responses
----------------------

Send a JSON object with these members and the `Content-Type: application/json` header:

* `jsonrpc`: `"2.0"`.
* `id`: A request identifier, returned in the response.
* `method`: One of the method names documented below.
* `params`: An object containing named parameters, or an array of positional parameters.
  Use `{}` for methods without parameters.
* `session_id`: The session ID returned by `login`, when using session authentication without cookies.

The examples use named parameters.
Send one method call per request.

Responses contain `id`, `jsonrpc`, `result`, and `error`.
The server returns the numeric value `2.0` for `jsonrpc` and uses the content type `application/json-rpc`.
On success, `error` is `null` and `result` contains the method's return value.
On failure, `result` is `null` and `error` describes the failure.
Check `error` even when the HTTP status is 200.

Errors usually contain `code`, `message`, and `data`.
Some SFTPPlus operation errors use an event `id` instead of `code`, with details in `data`.
Common error codes are `50000` for a missing or expired session, `50001` for failed authentication, `-32601` for an unknown method, and `-32602` for invalid parameters.
The `apply` method also reports errors separately for each change, as described below.


Login and sessions
------------------

Call `login` with an administrator's username and password:

.. code-block:: shell

    curl 'https://sftpplus.example.com:10020/json' \
      --header 'Content-Type: application/json' \
      --data '{
        "jsonrpc": "2.0",
        "id": 1,
        "method": "login",
        "params": {"username": "admin", "password": "YOUR_PASSWORD"}
      }'

A successful response has this form:

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 1,
      "result": {"session_id": "YOUR_SESSION_ID"},
      "error": null
    }

Copy the returned session ID into the top-level `session_id` member of subsequent requests:

.. code-block:: shell

    curl 'https://sftpplus.example.com:10020/json' \
      --header 'Content-Type: application/json' \
      --data '{
        "jsonrpc": "2.0",
        "id": 2,
        "session_id": "YOUR_SESSION_ID",
        "method": "get_property",
        "params": {"path": "/configuration/server/"}
      }'

Clients that retain and resend the session cookie set during login can omit `session_id`.
Requests refresh the session's inactivity timeout.
Call `logout` when finished, or log in again if the session expires.
Only `login` and `is_valid_session` can be called without an authenticated session.


login
^^^^^

`login(username, password)`

Authenticates an administrator and returns an object containing `session_id`.


logout
^^^^^^

`logout()`

Expires the current session and returns `true`.


is_valid_session
^^^^^^^^^^^^^^^^

`is_valid_session()`

Returns `{"is_valid": false}` when there is no authenticated session.
For a valid session, returns `is_valid: true`, `username`, the administrator's `uuid`, and `roles_uuid`.


ping
^^^^

`ping()`

Keeps the session active and returns `"pong"`.


Configuration and status
------------------------

The property tree contains `configuration`, `runnables` for component runtime properties, and `status` for server status.
Configuration sections contain components keyed by their UUIDs.
Configuration option names and structure match the :doc:`configuration reference </configuration/index>`.
For example, a service's `port` is directly under `/configuration/services/SERVICE_UUID/`.
Use JSON values such as numbers, booleans, strings, arrays, and objects for the corresponding properties.


get_index
^^^^^^^^^

`get_index()`

Returns the process property tree, including configuration and runtime properties, filtered by the administrator's read permissions.


get_property
^^^^^^^^^^^^

`get_property(path)`

Returns the readable properties below a branch of the tree.
Use an absolute path with a trailing slash, such as `/`, `/configuration/services/`, or `/runnables/`.
Read a component's branch to retrieve its individual option values.
Properties without read permission are omitted; some parent branches may remain as empty objects.


apply
^^^^^

`apply(changes)`

Applies configuration changes and saves the configuration.
Returns the readable process property tree with an additional `results` object keyed by the supplied change IDs.

The `changes` parameter of `apply` is an object keyed by client-selected change IDs.
Each change must contain `operation`, `path`, and `value`:

* `update`: Set the option at `path` to `value`.
* `create`: Create a component in the section at `path`, using an object of configuration options as `value`.
  The change result is the new component's UUID.
  New runnable components start automatically if enabled.
* `delete`: Remove the component at `path`.
  Include `value: null`.

Paths for `apply` are relative to `configuration`, without a leading slash.
For example, this request changes a service's port:

.. code-block:: json

    {
      "jsonrpc": "2.0",
      "id": 3,
      "session_id": "YOUR_SESSION_ID",
      "method": "apply",
      "params": {
        "changes": {
          "change-1": {
            "operation": "update",
            "path": "services/SERVICE_UUID/port",
            "value": 10022
          }
        }
      }
    }

Replace `SERVICE_UUID` with a UUID returned by `get_index` or `get_property`.
For each entry in `result.results`, check `error`: `null` means success; otherwise it contains the change's error details.
The entry's `result` contains the operation's return value, such as a new component's UUID.
Changes are processed individually, so successful changes are kept when another change fails.
A failure to save the configuration is also reported in `results`.

For the port update above, a successful response contains the following result.
The process property tree is omitted from these two response examples; only `results` is shown within `result`.

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 3,
      "result": {
        "results": {
          "change-1": {
            "result": null,
            "error": null
          }
        }
      },
      "error": null
    }

If the administrator lacks update permission for the port, the response instead contains this per-change error.
The top-level `error` remains `null`, and the port is unchanged.
The timestamp is an example Unix timestamp.

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 3,
      "result": {
        "results": {
          "change-1": {
            "result": null,
            "error": {
              "id": "50009",
              "timestamp": 1789430400.0,
              "data": {
                "details": "Action \"update\" denied for \"/configuration/services/SERVICE_UUID/port/\"."
              }
            }
          }
        }
      },
      "error": null
    }


Component operations
--------------------

For these methods, `family` identifies the component collection, such as `services`, `locations`, `resources`, `transfers`, or `event_handlers`.
Use the collection name and component `uuid` from `runnables` in the property tree.
Operating a component requires update permission for its operation path.


runnable_start
^^^^^^^^^^^^^^

`runnable_start(family, uuid)`

Starts the component and returns its runtime properties.

For example, start an existing, stopped SFTP service using its UUID in place of `SERVICE_UUID`.
The service must already have a valid configuration, including its SSH host key and listening address.

.. code-block:: json

    {
      "jsonrpc": "2.0",
      "id": 4,
      "session_id": "YOUR_SESSION_ID",
      "method": "runnable_start",
      "params": {
        "family": "services",
        "uuid": "SERVICE_UUID"
      }
    }

A successful response includes the following runtime properties; other properties are omitted here.

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 4,
      "result": {
        "uuid": "SERVICE_UUID",
        "state": "Started"
      },
      "error": null
    }


runnable_stop
^^^^^^^^^^^^^

`runnable_stop(family, uuid)`

Stops the component and returns its runtime properties.


runnable_restart
^^^^^^^^^^^^^^^^

`runnable_restart(family, uuid)`

Restarts the component and returns its runtime properties.


runnable_check
^^^^^^^^^^^^^^

`runnable_check(family, configuration)`

Tests the supplied configuration object and returns the component's check result, or an error if the check fails.
Include `uuid` when checking changes to an existing component; omit it for a new component.
A check can temporarily start a component or connect to an external service.


location_browse
^^^^^^^^^^^^^^^

`location_browse(uuid, path)`

Lists a directory at `path` on the location identified by `uuid`.
Returns the location's directory listing, including its `members`.
Requires read permission for the location's browse operation.

For example, list `/incoming` on a running location, replacing `LOCATION_UUID` with its UUID.

.. code-block:: json

    {
      "jsonrpc": "2.0",
      "id": 5,
      "session_id": "YOUR_SESSION_ID",
      "method": "location_browse",
      "params": {
        "uuid": "LOCATION_UUID",
        "path": "/incoming"
      }
    }

For an empty directory on a location rooted at `/`, a successful response is:

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 5,
      "result": {
        "path": "/incoming",
        "root": "/",
        "parent": "/",
        "members": []
      },
      "error": null
    }


Database queries
----------------


db_fetch
^^^^^^^^

`db_fetch(page=0, limit=100, criteria=null, sorting=null, db_uuid=null)`

Returns `{"data": [...]}` containing matching database rows.
`page` is a zero-based page number and `limit` is the maximum number of rows returned.
Set `db_uuid` to a database event handler's UUID, or omit it to query the default analytics database.
The selected database must be running.
Access requires read permission for the selected log or for reports when using the analytics database.

Use `sorting`, for example `{"id": "DESC"}`, to choose a column and an `ASC` or `DESC` order.
Use `criteria` to filter rows, for example `[[["message", "contains", "login"]]]`.
Each condition contains a column name, an operator, and a value.
Conditions within a group are combined with OR; the groups are combined with AND.
Supported operators are `=`, `!=`, `<`, `>`, `<=`, `>=`, and, for text columns, `contains` and `!contains`.
Column names depend on the selected database.
Omit `criteria` to return unfiltered rows.


Blocked IP addresses
--------------------

For these methods, `uuid` identifies a security policy.
Listing requires read permission for the policy's operation path; removing entries requires update permission.


get_blocked_ips
^^^^^^^^^^^^^^^

`get_blocked_ips(uuid, pattern)`

Returns entries containing `source_ip`, `failure_count`, and `last_failure`.
A pattern of at least three characters matches addresses containing that text.
A shorter pattern, including an empty string, returns up to ten of the most recently blocked addresses.

For example, find addresses containing `192.0.2`, replacing `POLICY_UUID` with the security policy UUID.

.. code-block:: json

    {
      "jsonrpc": "2.0",
      "id": 6,
      "session_id": "YOUR_SESSION_ID",
      "method": "get_blocked_ips",
      "params": {
        "uuid": "POLICY_UUID",
        "pattern": "192.0.2"
      }
    }

A successful response with one matching address is shown below.
`last_failure` is a Unix timestamp; the count and timestamp depend on recorded authentication failures.

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 6,
      "result": [
        {
          "source_ip": "192.0.2.10",
          "failure_count": 5,
          "last_failure": 1789430400.0
        }
      ],
      "error": null
    }


delete_blocked_ip
^^^^^^^^^^^^^^^^^

`delete_blocked_ip(uuid, host)`

Removes the failure record for the IP address in `host`.
Returns `true` if a record was removed, otherwise `false`.


clear_blocked_ips
^^^^^^^^^^^^^^^^^

`clear_blocked_ips(uuid)`

Clears the policy's recorded IP failures.
Returns `true` if any records were removed, otherwise `false`.


Keys, certificates, and vault items
-----------------------------------

Optional parameters below show their defaults.
Key sizes are in bits.

For methods accepting `upload_uuid`, pass `null` (Python `None`) and supply the text in `import_content`.
The `upload_uuid` parameter is required and is reserved for internal use by the Web Manager when uploading binary files.
Use `import_password` to decrypt protected input.

These generation and import methods return content for use in a subsequent configuration change.
Use `apply` to save it in a vault item.


ssh_key_generate
^^^^^^^^^^^^^^^^

`ssh_key_generate(type="rsa", size=3072)`

Generates an SSH key and returns `content` and `attributes`, including the public key and fingerprints.

For example, generate a 3072-bit RSA key:

.. code-block:: json

    {
      "jsonrpc": "2.0",
      "id": 7,
      "session_id": "YOUR_SESSION_ID",
      "method": "ssh_key_generate",
      "params": {
        "type": "rsa",
        "size": 3072
      }
    }

A successful response has the following form, with only selected attributes shown.
The key strings are abbreviated with `...`; the actual response contains the complete generated private and public keys.

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 7,
      "result": {
        "content": "-----BEGIN OPENSSH PRIVATE KEY-----\n...\n-----END OPENSSH PRIVATE KEY-----",
        "attributes": {
          "is_public": false,
          "is_encrypted": false,
          "key_type": "RSA",
          "key_size": 3072,
          "public_content": "ssh-rsa ..."
        }
      },
      "error": null
    }


ssh_key_export
^^^^^^^^^^^^^^

`ssh_key_export(upload_uuid, import_content="", import_password="")`

Reads an SSH key and returns its OpenSSH `content`, `attributes`, and detected `import_format`.

Set `upload_uuid` to `null` (Python `None`); binary file upload IDs are reserved for internal Web Manager use.


pgp_key_generate
^^^^^^^^^^^^^^^^

`pgp_key_generate(name, email, comment, type="rsa", size=3072, expire=0)`

Generates an OpenPGP key and returns `attributes` plus armored `public_content` and `private_content`.
Supply at least one nonempty `name` or `email`; `comment` can be empty.
`expire` is the number of months until expiration, or `0` for no expiration.

For example, generate an RSA key for file encryption with no expiration:

.. code-block:: json

    {
      "jsonrpc": "2.0",
      "id": 8,
      "session_id": "YOUR_SESSION_ID",
      "method": "pgp_key_generate",
      "params": {
        "name": "File Transfer",
        "email": "files@example.com",
        "comment": "File encryption",
        "type": "rsa",
        "size": 3072,
        "expire": 0
      }
    }

A successful response has the following form, with only selected attributes shown.
The armored key strings are abbreviated with `...`; retain the complete `private_content` value to use in the import example below.

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 8,
      "result": {
        "attributes": {
          "is_public": false,
          "is_encrypted": false,
          "key_type": "RSA",
          "key_size": 3072,
          "name": "File Transfer",
          "email": "files@example.com",
          "comment": "File encryption",
          "expires_at": ""
        },
        "public_content": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n...\n-----END PGP PUBLIC KEY BLOCK-----",
        "private_content": "-----BEGIN PGP PRIVATE KEY BLOCK-----\n...\n-----END PGP PRIVATE KEY BLOCK-----"
      },
      "error": null
    }


pgp_key_export
^^^^^^^^^^^^^^

`pgp_key_export(upload_uuid, import_content="", import_password=null)`

Reads an OpenPGP key and returns `attributes` plus armored `public_content` and `private_content`.

Set `upload_uuid` to `null` (Python `None`); binary file upload IDs are reserved for internal Web Manager use.
For example, import the private key generated above.
Replace `YOUR_PRIVATE_KEY_CONTENT` with the complete `private_content` string from that response, encoding its line breaks as `\\n` in JSON.

.. code-block:: json

    {
      "jsonrpc": "2.0",
      "id": 9,
      "session_id": "YOUR_SESSION_ID",
      "method": "pgp_key_export",
      "params": {
        "upload_uuid": null,
        "import_content": "YOUR_PRIVATE_KEY_CONTENT",
        "import_password": null
      }
    }

A successful response has the following form, with only selected attributes shown and armored key strings abbreviated with `...`.

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 9,
      "result": {
        "attributes": {
          "is_public": false,
          "is_encrypted": false,
          "key_type": "RSA",
          "key_size": 3072
        },
        "public_content": "-----BEGIN PGP PUBLIC KEY BLOCK-----\n...\n-----END PGP PUBLIC KEY BLOCK-----",
        "private_content": "-----BEGIN PGP PRIVATE KEY BLOCK-----\n...\n-----END PGP PRIVATE KEY BLOCK-----"
      },
      "error": null
    }


trusted_certificates_export
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`trusted_certificates_export(upload_uuid, import_content="", import_password="", item_uuid="")`

Reads trusted certificates and returns their `attributes` and PEM `public_content`.
If `item_uuid` is supplied, appends that vault item's existing content to the returned content.
Requires read permission for the referenced vault item when `item_uuid` is supplied.


pinned_keys_export
^^^^^^^^^^^^^^^^^^

`pinned_keys_export(upload_uuid, import_content="", item_uuid="")`

Reads pinned keys and returns their `attributes` and `public_content`.
If `item_uuid` is supplied, appends that vault item's existing content to the returned content.
Requires read permission for the referenced vault item when `item_uuid` is supplied.


private_certificate_export
^^^^^^^^^^^^^^^^^^^^^^^^^^

`private_certificate_export(upload_uuid, import_content="", import_password="", item_uuid="")`

Reads private certificate material and returns `attributes` and PEM `private_content`.
If `item_uuid` is supplied, appends that vault item's existing content to the returned content.
Requires read permission for the referenced vault item when `item_uuid` is supplied.


vault_item_export
^^^^^^^^^^^^^^^^^

`vault_item_export(uuid, export_password="", export_format="")`

Exports a private SSH key, OpenPGP key, or certificate from an existing vault item as a string.
Requires read permission for the vault item.
Use `export_password` to encrypt the exported private material.
`export_format` selects the SSH key format; an empty value uses the default OpenSSH format.


vault_item_part_delete
^^^^^^^^^^^^^^^^^^^^^^

`vault_item_part_delete(uuid, part_index)`

Deletes one part of a trusted certificate, private certificate, or pinned key vault item and returns the updated item properties.
`part_index` is a zero-based index into the item's parts.
Requires update permission for the vault item.


Certificate generation
----------------------

Both certificate generation methods require `common_name` and accept these optional parameters:

.. list-table::
    :header-rows: 1
    :widths: 25 15 60

    * - Parameter
      - Default
      - Description
    * - `size`
      - `3072`
      - Private key size in bits.
    * - `alternative_name`
      - `null`
      - Subject alternative names, for example `DNS:files.example.com,DNS:backup.example.com`.
    * - `constraints`
      - `""`
      - Basic certificate constraints.
    * - `key_usage`
      - `""`
      - Certificate key usage.
    * - `email`
      - `null`
      - Subject email address.
    * - `organization`, `organization_unit`
      - `null`
      - Subject organization and organizational unit.
    * - `locality`, `state`, `country`
      - `null`
      - Subject locality, state, and two-letter country code.
    * - `sign_algorithm`
      - `"sha256"`
      - Signature hash algorithm.


generate_csr
^^^^^^^^^^^^

`generate_csr(common_name, ...)`

Generates a new private key and certificate signing request (CSR).
Returns `attributes` and `private_content` containing the CSR and private key in PEM format.


generate_self_signed_certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`generate_self_signed_certificate(common_name, ...)`

Generates a new private key and self-signed certificate.
Returns `attributes` and `private_content` containing the certificate and private key in PEM format.


Email
-----


send_email
^^^^^^^^^^

`send_email(to, subject, body, attachments=null)`

Sends an email through the default email client and returns `null` on success.
`to` is an array of recipient addresses; an empty array uses the client's configured recipients.
`subject` and `body` are strings.
`attachments` is an optional object mapping file names to Base64-encoded content.

For example, send a message using the configured default email client.
Replace the example recipient with the intended email address.

.. code-block:: json

    {
      "jsonrpc": "2.0",
      "id": 10,
      "session_id": "YOUR_SESSION_ID",
      "method": "send_email",
      "params": {
        "to": [
          "operator@example.com"
        ],
        "subject": "SFTPPlus API test",
        "body": "This message was sent using the Web Manager API."
      }
    }

A successful response is:

.. code-block:: json

    {
      "jsonrpc": 2.0,
      "id": 10,
      "result": null,
      "error": null
    }
