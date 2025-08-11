HTTP API User Authentication and Configuration
==============================================

..  contents:: :local:


Introduction
------------

The SFTPPlus HTTP API authentication method will make a single client-side
POST request each time the client credentials needs to be validated.
It will use the HTTP response to decide on the outcome of the validation
and the configuration used for an authenticated user.

The HTTP API works as a back-end process and can be used for authenticating
accounts for other protocols, like SFTP or HTTPS.

The remote server can reply in 3 major ways:

* 204 / 200 - For successful authentication
* 401 - Credentials could not be validated and should be sent to the
  next method in the authentication chain.
* 403 - Credentials are rejected and the whole authentication fails

The HTTP request and response, following authentication, are both Unicode
and encoded in UTF-8.

When the HTTP authentication method is started,
it will make a test authentication request to validate the configuration.


POST Request
------------

For a password-based authentication to the SFTP service from a remote client
originating at an IP address and port like ``12.442.23.34:2345``
and requesting authentication of the user
as ``kevin`` with password ``home-alone``.

Expected HTTP header request::

    > POST /remote/url
    > Content-Type: application/json; charset=utf-8

Expected HTTP request in JSON format::

    {
      "credentials": {
        "type": "password",
        "username": "kevin",
        "content": "home-alone",
        "peer": {
          "address": "12.442.23.34",
          "port": 2345",
          "family": "IPv4",
          "protocol": "TCP"
          },
        "creator": {
          "uuid": "dff314a6-c594-48dc-8e34-5270fd6cb635",
          "type": "ssh"
          }
        },
      "server": {
        "uuid": "cc5c804d-0a3c-4c4c-b651-eba6fc3b5902"
        }
      }
    }

For the same client, but this time using SSH keys authentication, the expected
header request will be::

    > POST /remote/url
    > Content-Type: application/json; charset=utf-8

Expected request in JSON::

    {
      "credentials": {
        "type": "ssh-key",
        "username": "kevin",
        "content": "AAAAB3NzaC1yc2EAAAADAQABAAABAQChBpRFG9wXkaKEY-CONTENT",
        "peer": {
          "address": "2006:4820:4060::8844",
          "port": 2345",
          "family": "IPv6",
          "protocol": "TCP"
          },
        "creator": {
          "uuid": "dff314a6-c594-48dc-8e34-5270fd6cb635",
          "type": "ssh"
          }
        },
      "server": {
        "uuid": "cc5c804d-0a3c-4c4c-b651-eba6fc3b5902"
        }
    }


For the same client, but this time using SSL certificate authentication, the
expected header request will be::

    > POST /remote/url
    > Content-Type: application/json; charset=utf-8

The expected request in JSON is::

    {
      "credentials": {
        "type": "ssl-certificate",
        "username": "kevin",
        "content": "-----BEGIN CERTIFICATE-----\\nMIIG8TCCBN-PEM-FORMAT",
        "peer": {
          "address": "12.442.23.34",
          "port": 2345",
          "family": "IPv4",
          "protocol": "TCP"
          },
        "creator": {
          "uuid": "dff314a6-c594-48dc-8e34-5270fd6cb635",
          "type": "https"
          }
        },
      "server": {
        "uuid": "cc5c804d-0a3c-4c4c-b651-eba6fc3b5902"
        }
    }


Success Response (204 / 200)
----------------------------

In the simplest form,
for a successful authentication the server should respond with
HTTP code `204`::

    Status: 204 Authenticated

This will accept the authentication request and will use the **default group**
configuration for the authenticated user.

The response can also include an optional body containing the specific
configuration for the authenticated user.

In this case, the response code should be `200`::

    Status: 200 OK

The expected response body is a JSON object with keys and values for each
configuration option::

    {
      "account": {
        "home_folder_path": "/local/path/for/account",
        "uuid": "ebfbee04-17be-4d9f-b7fc-20ffed6a61a8",
        "group": "536839f5-3b5c-42ac-ad67-b74478ff71a5",
        "email": "kevin@example.com, another.email@example.com"
        "create_home_folder": true,
        "create_home_folder_owner": "ude_team",
        "create_home_folder_group": "partners",
        "home_folder_structure": ["/some-child", "/another-child"],
        "virtual_folders":[
          ["/shared-sales", "/home/shared/sales"],
          ["/shared-teams/emea-uploads", "/home/shared/teams/emea"],
          ]
        "permissions": [
          ["allow-full-control"],
          ["*.PDF", "allow-read"]
          ]
        }
    }

All values are case-sensitive, and keys should be lower-case.

An error is flagged when a response contains unknown keys.

Below you can find the description of each member from the response.

----

:name: home_folder_path
:type: string
:optional: Yes
:default: Configuration from default group.
:description: Absolute path used as root folder for this account.

----

:name: uuid
:type: string
:optional: Yes
:default: Account/Username
:description: UUID of this account, can be used to track renamed accounts.

----

:name: email
:type: string
:optional: Yes
:default: Empty text.
:description: One or more comma-separated emails associated to this account.

----

:group: group
:type: string
:optional: Yes
:default: DEFAULT_GROUP.
:description: UUID of the SFTPPlus group associated with this account.

----

:name: create_home_folder
:type: boolean
:optional: Yes
:default: Configuration from default group.
:description: When `true`, it will create missing home folder.

----

:name: create_home_folder_owner
:type: string
:optional: Yes
:default: Configuration from default group.
:description: OS account used as owner for the new home folder.

----

:name: create_home_folder_group
:type: string
:optional: Yes
:default: Configuration from default group.
:description: OS group attached to the new home folder.

----

:name: home_folder_structure
:type: List of strings.
:optional: Yes
:default: Empty list.
:description: List of strings, each containing a relative path which should be created inside the home folder.

----

:name: virtual_folders
:type: List of lists.
:optional: Yes
:default: Empty list.
:description: List of lists, each contain two members, first is the virtual
  path and the second is the mapping to a real path on the local filesystem.

----

:name: permissions
:type: List of lists.
:optional: Yes
:default: Empty list.
:description: List of lists, each containing the permissions for account.
    First line is the list of general permissions.
    The following lines are the permissions bases on path expression.

    For more details, see
    :ref:`the permission <configuration-groups-permissions>` documentation
    described for the group.


Unknown user (401)
------------------

When an account or its credentials are not recognized by the HTTP API authentication method,
but can be authenticated using other methods,
the server should respond with the HTTP code `401` and a short error message::

    Status: 401 Unauthorized or Human readable text for the error.

The account is not authenticated by the HTTP API.
SFTPPlus will try to authenticate the credentials using one of the other configured authentication methods.


Failure Response (403)
----------------------

When an account or its credentials are rejected the response should be HTTP code `403` and contain a short error message::

    403 Forbidden

    or

    403 Human readable text for the error.

The response can also contain an optional body as text::

    403 Forbidden
    Username disabled. More details can be sent in the response body.

Or it can contain an optional body as JSON, that can contain an optional `message` member.
SFTPPlus can be configured to display the content of the `message` value to end users,
as the authentication error response::

    403 Forbidden
    {
      "code": 1234,
      "message": "Custom detailed public error message",
      "extra": "Any extra private value is found only in the audit logs",
      }

For programmatic interaction with SFTPPlus over the JSON API,
the response can contain the `public_response` key.
This value is advertised to HTTP clients.
The value of `public_response` is only available to end users over the SFTPPlus HTTP JSON API.
It is not available over the HTML web GUI.
Only the value of the `message` key is available over the web GUI.

When your HTTP authentication server returns this response::

    403 Forbidden
    {
      "code": 1234,
      "message": "Custom detailed public error message.",
      "public_response": {
        "customKey": "Any key/value, that it sent to clients over JSON API.",
        "anotherKey": {"key": "Nested JSON is allowed."}
      }

With the SFTPPlus HTTP server `public_error` configuration enabled,
end users will see the following authentication failed response::

    $ curl https://user:pass@sftpplus.server.com/home/
    {"errors": [{
      "message": "Custom detailed public error message.",
      "response": {
        "customKey": "Any key/value, that it sent to clients over JSON API.",
        "anotherKey": {"key": "Nested JSON is allowed."}
        },
      "title": "Unauthorized"
      }]


Other Response Codes
--------------------

When the remote HTTP server responds with a code that is not documented on this page,
SFTPPlus will consider the account `rejected`.

In this case, it will not try to authenticate the account using other methods.
The behavior is similar to a `403 Forbidden` response.


Connection failures and invalid response
----------------------------------------

When you cannot get a response from the remote HTTP server (such as network
failures or a remote resource not found),
SFTPPlus will consider the account `disallowed`.

In this case,
SFTPPlus will not try to authenticate the account using other methods.
The behavior is similar to an `403 Forbidden` response.


Redundant HTTP URL / Endpoints
------------------------------

An HTTP authentication method can be configured with more than one URL to
provide redundant event handling.


Below is an example of an authentication method configured with multiple URLs::

    [event-handlers/6d32ee50-b2d2-93e5-caf4-c70a7]
    type = http
    url = http://www.acme.io/auth, https://fallback.acme.io/auth

SFTPPlus will always send the HTTP requests to the first URL
(`http://www.acme.io/auth)`.
URL `https://fallback.acme.io/auth` is used only when the request
failed to be handled by the HTTP endpoint at URL `http://www.acme.io/auth`,

When the request fails for an URL, the usage of that URL will be suspended
and resumed after 5 minutes.


Authenticating the request itself
---------------------------------

In some cases you your HTTP endpoint / server will required that the
HTTP request made by SFTPPlus to be authenticated.

Note that this section handled the authentication happening between the
SFTPPlus Server and the external HTTP API endpoint.

This does not covers the authentication between an external client
and the SFTPPlus server.
This is covered by the request payload and was covered in the previous sections.

The HTTP request (and not the payload) might need authentication when
using an HTTP API Gateway which has a general authentication policy
or you want extra security to make sure that authentication requests
only originate from authorized SFTPPlus sources.

The request can be authenticated using HTTP Basic Authentication or with a custom `Authorization` header or any other HTTP header.

Below is an example using the HTTP Basic Auth in which all the request
from the configured SFTPPlus server are authenticated with a username and password::

    [event-handlers/6d32ee50-b2d2-93e5-caf4-c70a7]
    type = http
    url = http://www.acme.io/auth
    username = API-username
    password = API-passord-or-token


Another example is when the remote HTTP API endpoint requires an API key or some other type of authentication.
This can be implemented by configuring a custom header that is sent with
each HTTP authentication request::

    [event-handlers/6d32ee50-b2d2-93e5-caf4-c70a7]
    type = http
    url = http://www.acme.io/auth
    headers = Authorization: token YOUR-AUTH-API-KEY


Example: Using SFTPPlus HTTP API for authenticating with a web application
--------------------------------------------------------------------------

In the use case, the existing team needed to integrate their web application
with a file transfer software, in this case SFTPPlus.
In addition, the team was constrained in the web application domain and instead
opted to integrate using the SFTPPlus HTTP API.

The system involved internal partners using SFTP for authentication and an external customer base that is authenticating via the web application.

In this case, a server has been set up to act both as an SFTPPlus File Server -
this server covers the file transfer process for the internal systems that
authenticate via SFTP.
In addition, the server also acts as the HTTP Server which utilizes the HTTP
AUTH logic.
When the HTTP authentication is confirmed, the HTTP worker then processes the
files and fed into a database.
After processing, the data is made ready for retrieval by the external customer though an external-facing web page.
