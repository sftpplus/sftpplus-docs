HTTP File Transfer Service API
==============================

..  contents:: :local:


API Standards and Styles
------------------------

The HTTP file transfer service provides a set of different APIs
for managing files.

Some of the APIs are well standardized and documented by a multi-vendor group,
while others are just design principles without any standardization body.

The following variants of HTTP APIs are available:

* OpenAPI RESTful with JSON representation (not JSON-RPC).
* WebDAV, which is well-standardized.
* GET and POST with HTML integration, for managing files via any web browser.

The OpenAPI 3.0.3 file is available at the following URL `/____chsps__/openapi.yaml`.
You can test the SFTPPlus OpenAPI using the folling URL `/__chsps__/openapi.html`.
The URLs are relative to the SFTPPlus HTTP or HTTPS servers.

To have SFTPPlus respond via the JSON API, make the request using the
`Accept: application/json` header in your client.

Regardless of the used API,
URLs for folders should always end with a trailing forward slash (/).
Any URL without a trailing forward slash is considered a file URL.

All APIs are mapped to the same URL space.
This means that you can mix APIs by
making requests for different API types for the same URL.

Example of request headers::

    > GET /home/ HTTP/1.1
    > Host: acme.com:18080
    > Authorization: Basic dXNlcjpwYXNz
    > User-Agent: curl/7.53.1
    > Accept: */*
    > Content-Type: application/json; charset=utf-8

When responding to path-related requests, the response will contain the
following additional headers:

* ``server`` - Server name and version.
* ``server-path`` - Server path associated with the request.
  Making FTP or SFTP requests using this path will generate a request for the
  same file/folder.

Example of valid headers for a response::

    < HTTP/1.1 200 OK
    < Date: Sun, 14 May 2017 14:33:47 GMT
    < Server-Path: /
    < Content-Length: 350
    < Content-Type: application/json; charset=utf-8
    < Server: SFTPPlus/3.20.1
    < Set-Cookie: ACME_HTTP_SESSION=details_here; Path=/

This section of documentation is focused on available HTTP methods
and the format of requests and responses, as used by developers working
on integrating external processes with SFTPPlus.

The `__chsps__` URL fragment referenced in the sections below is used for
URL namespaces which overlap with the files of an SFTPPlus account.
This fragment's peculiar name was chosen to minimize the risk of
conflicts with file and folder names from an SFTPPlus account home path.


Response Content Type
---------------------

Responses sent by the HTTP file transfer service can be in HTML or JSON
format.

The default format is JSON.

HTTP `content negotiation <http://en.wikipedia.org/wiki/Content_negotiation>`_
is a complex mechanism.

To generate the response in HTML format,
you will need to either set the `Accept` or `Content-Type` header to
`text/html`.

As long as the content type of your request is
`application/json; charset=utf-8`,
the response will also be JSON-formatted and UTF-8 encoded.


Authenticating Requests
-----------------------

The HTTP file transfer service is designed to be used from any web browser,
including both modern and old browsers, as well as those with
disabled JavaScript or blocked cookies.

For modern web browsers with cookies enabled,
cookie-based authentication is used. This is persistent across multiple
requests.


Basic Authentication
^^^^^^^^^^^^^^^^^^^^

The HTTP file transfer service also supports Basic Authentication,
as defined in `RFC 2617 <http://www.ietf.org/rfc/rfc2617.txt>`_.

This is used for browsers that do not support or block
JavaScript or cookies.

Basic Authentication is also suitable for non-interactive usage
outside of a browser.

For example, when using the cURL command.
Each cURL request will trigger a new authentication call and
there is no need to make a special request for the HTTP service login page.

Basic authentication is less suitable for multiple requests
made as part of a transaction.
For such a scenario, we recommend using session-based authentication.

To get the list of all files and folders for user ``JohnD``, using the
JSON format::

    curl -u JohnD \
        -H "Accept: application/json" \
        https://localhost:10443/home/

    > {"content": [{"is_directory": true, "name": "test", "modified": 151476...

For requests with invalid credentials, the response will redirect to the
login page. Here we have the HTML format of the response.::

    curl -u JohnD -H 'Accept: text/html' \
        https://localhost:10443/home/

    < HTTP/1.1 302 Found
    < Content-Type: text/html; charset=utf-8
    < WWW-Authenticate: basic realm="Web files access"
        <html>
            <head>
                <meta http-equiv="refresh" content="0;URL=/__chsps__/login">
            </head>
            <body bgcolor="#FFFFFF" text="#000000">
            <a href="/__chsps__/login">Click here to continue.</a>
            </body>
        </html>


Session Authentication
^^^^^^^^^^^^^^^^^^^^^^

To use session authentication with our API, you will first need to
create a session token.
It can be requested as an URL-encoded form value or as JSON.

An URL-encoded request and the corresponding JSON response::

    curl --data 'username=JohnD' --data 'password=my-secret' \
        -H 'Accept: application/json' \
        https://localhost:10443/__chsps__/login
    > Content-Type: application/x-www-form-urlencoded

    < HTTP/1.1 200 OK
    < Content-Type: application/json
    {"results": [{"session": "8539cc3e424c0040bd87fba41e106d0c"}]}

A JSON-formatted request and the corresponding response::

    curl -H 'Content-Type: application/json' \
        -X POST \
        -H 'Accept: application/json' \
        -d '{"username":"JohnD","password":"my-secret"}' \
        https://localhost:10443/__chsps__/login

    < HTTP/1.1 200 OK
    < Content-Type: application/json
    {"results": [{"session": "8539cc3e424c0040bd87fba41e106d0c"}]}

If you don't specify that you want the response as JSON, the session will be returned as a web-browser compatible cookie header named `CHEVAH_HTTP_SESSION`::

    curl --data 'username=JohnD' --data 'password=my-secret' \
        -H 'Accept: application/json' \
        https://localhost:10443/__chsps__/login
    > Content-Type: application/x-www-form-urlencoded

    < HTTP/1.1 302 Found
    < Content-Type: text/html; charset=utf-8
    < Set-Cookie: CHEVAH_HTTP_SESSION=cbd162; Path=/; HttpOnly; SameSite=strict

For failed requests, the response might look as follows::

    curl -u JohnD \
        -H 'Accept: application/json' \
        https://localhost:10443/__chsps__/login

    < HTTP/1.1 401 Unauthorized
    < Content-Length: 175
    < Content-Type: application/json
    {"errors": [{"message": "You are not authenticated. Please try again
    using valid credentials or contact the system administrator for more
    details.", "title": "Unauthorized"}]}

Once you get the ID of the authenticated session, you can use it to make a
request with the `Authorization` headers, as exemplified below::

    curl -H 'authorization: session YOUR-SESSION-ID' \
        -H 'Accept: application/json' \
        https://localhost:10443/home/

    < HTTP/1.1 200 OK
    < Content-Type: application/json
    {"content": [{"is_directory": true, "name": "test", ....

When a session ID is no longer valid, the response will be::

    curl -H 'authorization: session YOUR-SESSION-ID' \
        -H 'Accept: application/json' \
        https://localhost:10443/home/

    < HTTP/1.1 401 Unauthorized
    < WWW-Authenticate: basic realm="Web files access"
    < WWW-Authenticate: session
    {"errors": [{"message": "You are not authenticated.
    Please try again using valid credentials or contact
    the system administrator for more details.", "title": "Unauthorized"}]}


Account Password Update
-----------------------

Users/clients of the HTTP file transfer service can update the password
associated with their account,
assuming that this functionality is enabled for their group of accounts.

In order to update the password, the following details are required:
* account name / username
* current password
* new password

When updating a password, the new one is validated against the
active password policy.

Passwords can be updated via the web browser interface or through the JSON API.

To update their password using a web browser, clients should first login
through the HTTP file transfer service. Pages for logged users will always
present an option to change the password situated close to the logout link.

Passwords can also be updated through the JSON-based API.
A successful authentication is needed first, using the current valid password.
Afterwards, a POST request of the following format should be sent::

    curl -X POST \
        -H 'Authorization: session YOUR-SESSION-ID' \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
        -d '{"current_password":"old-secret","new_password":"new-secret"}' \
        https://localhost:10443/home/__chsps__/password-update


RESTful JSON-based API
----------------------

RESTful web services allow the requesting systems to access and manipulate
textual representations of web resources by using a uniform and predefined
set of stateless operations.

The HTTP service provides a simple JSON-based API for accessing and managing
files over the HTTP protocol using a RESTful approach.

This is not a JSON-RPC API.
It is a lightweight version of the WebDAV protocol,
using JSON instead of XML.

Unlike WebDAV, there is no official standard for RESTful web APIs.
This is because REST is an architectural approach, while WebDAV is an extension
of the HTTP protocol defined in
`RFC 4918 <https://tools.ietf.org/html/rfc4918>`_.

Text in JSON-based requests and responses is always encoded using UTF-8.


Response to invalid headers or content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For requests with invalid headers or content, the response code is
`400 Bad Request`::

    < HTTP/1.1 400 Bad Request

The body will contain a message with JSON-formatted error details::

    {
      "errors": [
            {"message": "Problems parsing JSON"}
      ]
    }


Responses to valid headers/content that cannot be processed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For requests which have valid headers and valid content, but which cannot be
processed, the header response is::

    < HTTP/1.1 422 Unprocessable Entity

The response in JSON should be::

    {
      "errors": [
        {"message": "Text message describing the error."}
      ]
    }

..  note::
    When the URL for a folder request does not end with an `/`
    (forward slash character), the server will respond with
    a redirect towards the same URL with an appended forward slash.


GET and HEAD
^^^^^^^^^^^^

The file download request URL is structured as follows::

    https://sub.example.com:PORT/home/PATH/TO/FILE

In the above example, the URL will trigger a download request for
``/PATH/TO/FILE``.

Both `GET` and `HEAD` request methods are supported.

There is also support for the ``If-Modified-Since`` request header. The
server will reply with the standard ``304 Not Modified`` response header if
the file has not been modified since the requested date.

A file download header request would look like::

    > GET /home/PATH/TO/file HTTP/1.1

The header and content response from the server will be::

    < HTTP/1.1 200 OK
    < Server-Path: /PATH/TO/file

    FILE_CONTENT_HERE

The folder listing request URL is structured as follows::

    https://sub.example.com:PORT/home/PATH/TO/FOLDER/

In the above example, the URL will trigger a folder listing request for
``/PATH/TO/FOLDER``.

The default response content type is HTML.
To request the content as JSON, you should use::

    > GET /home/PATH/TO/FOLDER/ HTTP/1.1
    > Accept: application/json

The header response from the server will look like this::

    < HTTP/1.1 200 OK
    < Server-Path: /PATH/TO/FOLDER
    < Content-Type: application/json; charset=utf-8

The JSON formatted response shows that there are two files and two folders in
the given directory.::

    {"content": [
        {
            "name": "some-folder",
            "is_directory": true,
            "modified": 1427291663.52,
            "size": 0
            },
        {
            "name": "other-folder",
            "is_directory": true,
            "modified": 1427291076.37,
            "size": 0
            },
        {
            "name": "some-file.TXT",
            "is_directory": false,
            "modified": 1427291184.78,
            "size": 12133
            },
        {
            "name": "other.PDF",
            "is_directory": false,
            "modified": 1427291083.33,
            "size": 7073
            }
        ]
    }


..  note::
    `modified` field is in
    `POSIX/Unix time <http://en.wikipedia.org/wiki/Unix_time>`_ formatted as
    seconds with decimals representing the milliseconds.

..  note::
    If you consume this JSON in JavaScript, note that `Date()` is instantiated
    with milliseconds, so you will need to use `new Date(json_value * 1000)`.

To download as a ZIP archive an entire folder, including its sub-folders,
use the `Accept: application/zip` header in the request.

    > GET /home/PATH/TO/FOLDER/ HTTP/1.1
    > Accept: application/zip

Files inside the resulting ZIP archive are stored using their full paths.

Symbolic links are ignored when generating ZIP archives.


PUT
^^^

When using the PUT request for a file,
the file will be created if not existing
or overwritten if already existing.

Example for uploading a file named ``/reports/2018-12-10.CSV``::

    < PUT /home/reports/2018-12-10.CSV HTTP/1.1
    <
    < "SOME_CSV_HEADER", "OTHER_CSV_HEADER"
    >
    > HTTP/1.1 201 Created

When using the PUT request for a folder,
the folder will be created if not existing.
The PUT request will fail if the folder already exists
or if the parent folder does not exist.

Example for creating a new folder named ``accounting-2018-12-10``::

    < PUT /home/reports/accounting-2018-12-10/ HTTP/1.1
    > HTTP/1.1 201 Created


PUT with metadata header
^^^^^^^^^^^^^^^^^^^^^^^^

You can request uploading a file using a set of associated labels / tags /
metadata. This is done using the `metadata_fields` configuration option.

In the simplest configuration,
you define the name of an HTTP header from which to extract the
`key=value` metadata::

    [services/9ac4-1054-f0e4]
    name = HTTPS REST API
    type = https

    metadata_fields = x-labels

An HTTP header can contain multiple `key=value` metadata separated by commas.

You can also configure a list of expected metadata keys with associated
`optional` or `required` options.
In the following configuration, any REST upload request is required to contain
the `x-labels` header with a required ``tag`` metadata
while the ``project`` metadata is optional::

    [services/9ac4-1054-f0e4]
    name = HTTPS REST API
    type = https

    metadata_fields =
      x-labels, required
      tag, required
      project-*, optional

The request for uploading a file named ``/report.xml`` with associated labels
``tag=report``, ``tag=monthly``, ``project-name=ACME``, and ``project-class=A``
will be made like::

    < PUT /home/report.xml HTTP/1.1
    < X-Labels: tag=report, tag=monthly, project-name=ACME, project-class=A
    <
    < XML-CONTENT
    >
    > HTTP/1.1 201 Created

The requested HTTP header value is parsed as the following JSON structure
that is attached to data associated with the emitted events::

    {
    "tag": ["report", "monthly"],
    "project-name": ["ACME"],
    "project-class": ["A"],
    }

The the metadata is attached to the following events:

* 40017 - HTTP file uploaded with success.
* 40021 - Start uploading HTTP file.
* 40022 - HTTP file upload failed.


DELETE
^^^^^^

When using the DELETE request for a folder,
that folder will be removed recursively.

Example for deleting folder ``/reports`` together with any other folders
such as ``/reports/2017`` or ``/reports/2018``::

    < DELETE /home/reports/ HTTP/1.1
    > HTTP/1.1 204 No Content

When using the DELETE request For a file,
that file will be removed.

Example for deleting the file ``/reports/2018-12-10.CSV``::

    < DELETE /home/reports/2018-12-10.CSV HTTP/1.1
    > HTTP/1.1 204 No Content


POST
^^^^

The POST request is not supported for a file URL.

You can execute folder operations by sending a POST request with an
`application/json; charset=utf-8` content type for a folder path.

Below is the list of supported commands:

* delete
* create-folder
* create-folder-if-missing

If all commands are successful, the response will be::

    < HTTP/1.1 200 OK

If the request is not well formatted, the response will be `400` and no
action will be performed::

    < HTTP/1.1 400 Bad Request
    < Content-type: application-json; charset=utf-8
    <
    < {
    <   "errors": [
    <     {"message": "Details about what is not right."}
    <   ]
    < }

When at least one command fails, the response will contain a result combining
the results of all commands.
For successful commands, the `message` is `null`.
Besides the error message, each error will contain the associated `target`::

    < HTTP/1.1 422 Unprocessable Entity
    < Content-type: application-json; charset=utf-8
    <
    < {
    < "errors": [
    <     {"target": "child-file", "message": null},
    <     {"target": "child-folder", "message": "Invalid name 'child-folder'."},
    <     {"target": "other-file", "message": null},
    <     ]
    < }


Deleting / removing folders
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example will delete ``/home/path/to/folder/child-file``.

The request will look like::

    > POST /home/path/to/folder
    > Content-type: application-json; charset=utf-8
    >
    > {
    > "commands": [
    >     {
    >         "command": "delete",
    >         "target": "child-file"
    >         }
    >     ]
    > }

You can recursively remove folders.
The following example will delete a folder located at
``/home/path/to/folder/child-folder`` together with all its member contents
and child files/folders.

The request will look like::

    > POST /home/path/to/folder/
    > Content-type: application-json; charset=utf-8
    >
    > {
    > "commands": [
    >     {
    >         "command": "delete",
    >         "target": "child-folder"
    >         }
    >     ]
    > }


Creating new folders
~~~~~~~~~~~~~~~~~~~~

The following example will create a new folder
``/home/path/to/folder/new-folder-name``.

The request will look like::

    > POST /home/path/to/folder/
    > Content-type: application-json; charset=utf-8
    >
    > {
    > "commands": [
    >     {
    >         "command": "create-folder",
    >         "target": "new-folder-name"
    >         }
    >     ]
    > }


Creating a folder if missing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example will create a new folder at
``/home/path/to/folder/new-folder-name`` and will not raise an error if
the folder already exists.

The request will look like::

    > POST /home/path/to/folder/
    > Content-type: application-json; charset=utf-8
    >
    > {
    > "commands": [
    >     {
    >         "command": "create-folder-if-missing",
    >         "target": "new-folder-name"
    >         }
    >     ]
    > }


Triggering custom actions for members of a folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example will perform the `approve` custom trigger on
``/home/path/to/folder/some-file.txt`` and
``/home/path/to/folder/another-file.pdf``.

The request will look like::

    > POST /home/path/to/folder
    > Content-type: application-json; charset=utf-8
    >
    > {
    > "commands": [
    >     {
    >         "command": "YOUR-CUSTOM-TRIGGER-NAME",
    >         "target": ["some-file.txt", "another-file.pdf"]
    >         }
    >     ]
    > }


Combining requests
^^^^^^^^^^^^^^^^^^

You can combine multiple commands into a single request.

The request will look like::

    > POST /home/path/to/folder/
    > Content-type: application-json; charset=utf-8
    >
    > {
    > "commands": [
    >     {
    >         "command": "delete",
    >         "target": "child-file"
    >         },
    >     {
    >         "command": "create-folder",
    >         "target": "sibling-folder"
    >         },
    >     {
    >         "command": "YOUR-CUSTOM-TRIGGER-NAME",
    >         "target": ["some-file.txt", "another-file.pdf"]
    >         },
    >     {
    >         "command": "delete",
    >         "target": "other-file"
    >         }
    >     ]
    > }

..  note::
    Command names are case-sensitive.
    The command target is also case-sensitive, with the exception of files
    and folders stored on NTFS or other case-insensitive file systems.


HTTP WebDAV API
---------------

SFTPPlus HTTP service implements a subset of the WebDAV HTTP extension,
as defined in `RFC 4918 <https://tools.ietf.org/html/rfc4918>`_.

We are working to fully implement the WebDAV extensions as documented in the
RFC.

In this section, we document what is currently implemented server-side.
Anything that is not documented here can be considered as not yet implemented.
Get in contact with us if you want a WebDAV feature which is not yet
implemented.

A WebDAV client-side implementation is available in SFTPPlus as
: :doc:`a WebDAV location</configuration-client/webdav>`

In the context of the SFTPPlus server-side implementation,
the WebDAV collection resources are folders/directories
while non-collection resources are files.


GET and HEAD
^^^^^^^^^^^^

When requested for a file, it will return the content of the file.
It will behave similarly to the REST API.

HEAD has the same behaviour and will return the same response codes as for GET,
with the exception that the body is always empty.


MKCOL
^^^^^

When requested for a path which does not exist, it will create a new folder.

It will fail if the folder already exists or
if there is already a file with the same name.

It is not supported for file URLs.


PUT
^^^

In SFTPPlus, a PUT request in the context of WebDAV has the same behaviour as
the REST API.

The specification does not define the behaviour of the PUT method for
existing or non-existing folders. In SFTPPlus it will behave like the REST API.


DELETE
^^^^^^

As defined by the WebDAV specification, DELETE will remove/delete a file.
When requested for a folder, it will do a recursive delete for that folder.


Browser HTML API
----------------

The HTTP service provides a browser-friendly API for managing files using HTML.
The API is designed to be integrated with HTML FORM elements.

It is based on the GET, HEAD and POST HTTP methods.


GET and HEAD
^^^^^^^^^^^^

A GET request for a file will return the file content, while for a folder
it will return an HTML markup describing the members of that folder.

The following response codes are returned:

* 200 - when the request was successful
* 404 - when the request path doesn't exist
* 403 - when permission is denied
* 400 - on any other error

The HEAD request will return no content, and will have the same response code
as for GET.


POST
^^^^

The data for POST requests is encoded using multipart/form-data.

Here is an example of HTML code which can be used to upload a file,
create a new folder and select which files or folders to delete.::

    <form
      action=""
      method="POST"
      enctype="multipart/form-data"
      >
      <input
        name="upload-file"
        type="file"
        multiple="true"
        />
      <button
        type="submit"
        name="action"
        value="upload-file"
        >Upload files</button>

      <button
        type="submit"
        name="action"
        value="YOUR-CUSTOM-TRIGGER-NAME"
        >Custom trigger action</button>

      <input
        name="new-folder"
        type="text"
        />
      <button
        type="submit"
        name="action"
        value="create-folder"
        >Create new folder</button>

      <input
        type="checkbox"
        name="selected-members"
        value="Reports-2019-12-13"
        ></input>
      <input
        type="checkbox"
        name="selected-members"
        value="file-2.PDF"
        ></input>
      <input
        type="checkbox"
        name="selected-members"
        value="file-3.TXT"
        ></input>
      <input
        type="checkbox"
        name="selected-members"
        value="file-2.PDF"
        ></input>
      <button
        type="submit"
        name="action"
        value="delete-members"
        >Delete selected items</button>

Looking at the low level HTTP API,
the request to create a new folder with name `new-folder` is::

    > POST /home/path/to/folder/ HTTP/1.1
    > Content-type: multipart/form-data; boundary=----Browser4sDB61mTyhxl1VS9

    ------Browser4sDB61mTyhxl1VS9
    Content-Disposition: form-data; name="action"

    create-folder
    ------Browser4sDB61mTyhxl1VS9
    Content-Disposition: form-data; name="new-folder"

    test-folder
    ------Browser4sDB61mTyhxl1VS9--

To delete multiple members of the folder, the request would be::

    > POST /home/path/to/folder/ HTTP/1.1
    > Content-type: multipart/form-data; boundary=----BrowserDpxASFZnpR6imXgG


    ------BrowserDpxASFZnpR6imXgG
    Content-Disposition: form-data; name="action"

    delete-members
    ------BrowserDpxASFZnpR6imXgG
    Content-Disposition: form-data; name="selected-members"

    tmp0gdd8j.txt
    ------BrowserDpxASFZnpR6imXgG
    Content-Disposition: form-data; name="selected-members"

    tmp0t2rw4.pdf
    ------BrowserDpxASFZnpR6imXgG
    Content-Disposition: form-data; name="selected-members"

    tmp0t6kdr.csv
    ------BrowserDpxASFZnpR6imXgG--

To perform a custom trigger action on multiple members of the folder, the
request would look as follows.
(replace `YOUR-CUSTOM-TRIGGER-NAME` with the name of your trigger)::

    > POST /home/path/to/folder/ HTTP/1.1
    > Content-type: multipart/form-data; boundary=----BrowserDpxASFZnpR6imXgG


    ------BrowserDpxASFZnpR6imXgG
    Content-Disposition: form-data; name="action"

    YOUR-CUSTOM-TRIGGER-NAME
    ------BrowserDpxASFZnpR6imXgG
    Content-Disposition: form-data; name="selected-members"

    some-file.txt
    ------BrowserDpxASFZnpR6imXgG
    Content-Disposition: form-data; name="selected-members"

    another-actioned-file.pdf
    ------BrowserDpxASFZnpR6imXgG--


action
~~~~~~

Name of the requested action.

:type: string
:available values:
    * create-folder
    * upload-file
    * delete-members
    * download-members
    * CUSTOM-TRIGGER-NAME


new-folder
~~~~~~~~~~

Name of the folder requested to be created.

:type: string


upload-file
~~~~~~~~~~~

Content of the file requested for upload.

:type: file


selected-members[]
~~~~~~~~~~~~~~~~~~

List of member names requested for removal or bulk download.

:type: list
