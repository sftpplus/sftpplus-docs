HTTP POST Event Handler
=======================

..  contents:: :local:


Introduction
------------

The *HTTP POST Event Handler* is where you can integrate SFTPPlus with your
web resource.
Simply create an event handler that will send an HTTP POST
request to your remote HTTP resource based on specified server event IDs.

In the Web Manager GUI, create a new Event Handler of type `Send as HTTP Post
request` or add the `url` in the configuration file for the
event-handlers UUID::

    [event-handlers/6d32ee50-b277-49e5-b2f4-c70eeea289a7]
    url = http://www.acme.io/http-post-hook-url

For an example configuration that targets the server event ID `40007` and
specifying that the JSON format be used to send the event in the HTTP body,
see below::

    [event-handlers/6d51ed1e-35ec-41d7-8b51-53e56c716212]
    enabled = True
    type = http
    name = Example file transfer hook for ACME
    description = Send an HTTP POST hook when the event is raised
    target = 40007
    url = http://www.acme.io/http-post-hook-url
    http_content_type = json


Request body
------------

When an HTTP or HTTPS handler is used, SFTPPlus will initiate an HTTP
client request to the configured URL with a body containing one or
more events, together with the identity of the server making the request.

The request body can be formatted as JSON, XML, or using a custom template.

The `events` array contains a list of `event` objects.

.. include:: /developer/event-object.include.rst

..  warning::
  The `server` member found in the root container is deprecated and will be
  removed in SFTPPlus v5.
  You should use the `server` attribute of each event.


Request and response example
----------------------------

Below is an example for a `POST` request containing two JSON events::

    POST /remote/url
    Content-Type: application/json

    {
      "events": [
        {
          "id": "10025",
          "timestamp": {
            "timestamp":  "1510742418.2341",
            "cwa_14051": "2017-11-15 10:40:18"
            },
          "data": {
            "path": "/path/of/file/as/seen/by/client",
            "details": "Some details about failure."
            },
          "account": {
            "uuid": "0c12a7f9-484a-45de-b622-8a5d96061328",
            "name": "mike",
            "peer": {
              "address": "12.442.23.34",
              "port": 2345,
              "family": "IPv4",
              "protocol": "TCP"
              }
            },
          "component": {
            "uuid": "dff314a6-c594-48dc-8e34-5270fd6cb635",
            "type": "ssh",
            "name": "SFTP-Internal"
            }

          },
        {
          "id": "20040",
          "timestamp": {
            "timestamp":  "1510742419.1245",
            "cwa_14051": "2017-11-15 10:40:19"
            },
          "data": {
            "subject": "event specific data."
            },
          "account": {
            "uuid": "0c12a7f9-484a-45de-b622-8a5d96061328",
            "name": "mike",
            "peer": {
              "address": "2006:4820:4060::8844",
              "port": 2355,
              "family": "IPv6",
              "protocol": "TCP"
              }
            },
          "component": {
            "uuid": "dff314a6-c594-48dc-8e34-5270fd6cb635",
            "type": "ssh",
            "name": "SFTP-Internal"
            }
          },
          "server": {
            "uuid": "cc5c804d-0a3c-4c4c-b651-eba6fc3b5902",
            "name": "AZWMPreProd01"
            }
        ]
    }

Below is an example for a `POST` request containing one XML SOAP event::

    POST /remote/url
    Content-Type: application/soap+xml; charset=utf-8

    <?xml version="1.0" ?>
    <soap:Envelope
      soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding"
      xmlns:soap="http://www.w3.org/2003/05/soap-envelope/">
      <soap:Body xmlns:m="http://www.sftpplus.com/event">
        <m:Events>
          <m:Event>
            <account>
              <peer>
                <protocol>TCP</protocol>
                <port>55216</port>
                <family>IPv6</family>
                <address>::ffff:127.0.0.1</address>
              </peer>
              <uuid>user_uuid</uuid>
              <name>user</name>
            </account>
            <created>1591402889.06</created>
            <timestamp>
              <cwa_14051>2020-06-06 01:21:29</cwa_14051>
              <timestamp>1591402889.06</timestamp>
              <iso_8601>2020-06-06T00:21:29Z</iso_8601>
              <iso_8601_fractional>
                2020-06-06T00:21:29.056312084198Z</iso_8601_fractional>
              <iso_8601_local>2020-06-06T01:21:29+01:00</iso_8601_local>
            </timestamp>
            <component>
              <type>http</type>
              <name>http</name>
              <uuid>http-1</uuid>
            </component>
            <server>
              <uuid>test-server-uuid</uuid>
              <name>test-server-name</name>
            </server>
            <message>
              Successfully uploaded file at &quot;/path/file.txt&quot;.
              Wrote 168691 bytes at 48227205.7845 bytes/second
              in 0.003497838974 seconds.
            </message>
            <data>
              <total_write>168691</total_write>
              <real_path>
                /srv/ftp/path/file.txt</real_path>
              <write_speed>48227205.7845</write_speed>
              <avatar>
                <peer>
                  <protocol>TCP</protocol>
                  <port>55216</port>
                  <family>IPv6</family>
                  <address>::ffff:127.0.0.1</address>
                </peer>
                <uuid>user_uuid</uuid>
                <name>user</name>
              </avatar>
              <duration>0.003497838974</duration>
              <path>/path/file.txt</path>
            </data>
            <id>40017</id>
          </m:Event>
        </m:Events>
      </soap:Body>
    </soap:Envelope>


Response codes
--------------

Once the server has successfully received and processed the events, it should
respond with HTTP code `200`::

    Status: 200 OK

HTTP code `204` is also a valid response code::

    Status: 204 No Content

When the remote HTTP server is busy and can't process more requests,
the response should display HTTP code `503` together with a `Retry-After`
header with a value expressed in seconds.
The current events are discarded.::

    Status: 503 Service Unavailable
    Retry-After: 3600

For any response code, other than `200` and `204`, SFTPPlus will consider that
the requests failed to be successfully processed by the remote HTTP endpoint.

Failed requests are not retried and the event handler will stop sending events
after the configured number of consecutive failures.

An event is emitted for every event which failed to be processed by the
remote HTTP server.
For example, when the event ID `40007` is triggered
(opening an existing folder) and its handling failed,
the server-side SFTPPlus log will specify the server return code.
In this case, `203` is the specified server return code:

    | 20174 2017-05-12 14:12:12 other-event-http-uuid Process 0.0.0.0:0
      Failed to handle event 40007 by "file-transfer-hooks".
      Server returned 203:Non-Authoritative Information


Response body
-------------

For remote servers which are sending the error inside an HTTP response with
code `200`, you can use the `expected_response` configuration to define
a matching expression to detect a successful response.
In the following example, SFTPPlus will treat the HTTP response as an error
if it doesn't contain the `<Status>OK</Status>` value anywhere in the body::

    [event-handlers/69fb02f4-a896-11ea-b3ee-134d4ef1f480]
    enabled: yes
    type: http
    name: file-transfer-hooks
    url: https://web-hooks.example.com/received-files.api

    expected_response=*<Status>OK</Status>*

You can use the negated regular expression to consider a success any
response which doesn't contain the `<Status>Error</Status>` value,
like in the following example::

    [event-handlers/69fb02f4-a896-11ea-b3ee-134d4ef1f480]
    enabled: yes
    type: http
    name: file-transfer-hooks
    url: https://web-hooks.example.com/received-files.api

    expected_response=e/.*<Status>Error</Status>.*/i

When using regular expressions to match a value that spans multiple lines,
you will need to explicitly include the newline characters.
This is not required for globbing expression, as the newline characters
are included in the `* (match anything)` glob.
Below is an example of defining multi lines expression::

    [event-handlers/69fb02f4-a896-11ea-b3ee-134d4ef1f480]
    enabled: yes
    type: http
    name: file-transfer-hooks
    url: https://web-hooks.example.com/received-files.api

    expected_response=e/.*<Status>.*\n.*Error.*\n.*</Status>.*/i

The above example which will consider the response a failure if the
body contains either of the values::

    <Status>Error</Status>

    or

    <Status>
      Error
    </Status>


Redundant HTTP URL / Endpoints
------------------------------

An HTTP POST event handler can be configured with more than one URL to
provide redundant event handling.

If handling of an event failed for an URL, SFTPPlus will re-try to handle
the event using the next URL from the list.

If handling of an event succeeded, SFTPPlus will not send the request to the
following URLs from the list.

Below is an example of an event handler configured with multiple URLs::

    [event-handlers/6d32ee50-b277-49e5-b2f4-c70eeea289a7]
    url = http://www.acme.io/events, https://fallback.acme.io/events

SFTPPlus will send the HTTP requests to URL `http://www.acme.io/events`.
URL `https://fallback.acme.io/events` is used only when the request
failed to be handled by the HTTP endpoint at URL `http://www.acme.io/events`

When the request fails for an URL, the usage of that URL will be suspended
and resumed after 5 minutes.

If all URLs are not available, SFTPPlus will emit an error informing that
processing the event via HTTP POST failed, not retrying the delivery.


Fault-tolerant / Resilient HTTP requests
----------------------------------------

It is possible for a request to the HTTP endpoint to return a failure
response.
SFTPPlus can be configure to retry the same URL on failure.

For example, the following configuration will make a first request to
``http://www.acme.io/events`` and if it fails, it will wait 0.5 second and
then try again.
If the request still fails, it will retry for 1 seconds before retrying for
a second try.
If the second request will fail, the request is considered as a permanent
failure and the request will not be sent again to the URL.

Below is the configuration for the retry scenario described above::

    [event-handlers/6d32ee50-b277-49e5-b2f4-c70eeea289a7]
    url = http://www.acme.io/events
    retry_count = 2
    retry_increase = 0.5

It is possible to comply the URL retry configuration with a fallback URL.
In this case, it will retry the first url twice and then will attempt the
same request on the next URL::

    [event-handlers/6d32ee50-b277-49e5-b2f4-c70eeea289a7]
    url = http://www.acme.io/events, https://fallback.acme.io/events
    retry_count = 2
    retry_increase = 0.5


Sending custom JSON data in HTTP POST request
---------------------------------------------

Each payload sent by the HTTP POST event handler contains the following
members, as documented in previous sections::

    {
      "events": [ EVENT_DATA ],
      "server": { SERVER_DATA }
    }

You can configure the event handler to add custom values to the payload.
The extra values are configured in JSON format and can be nested structures.

The keys and values can contain variables which are replaced with values based
on the event's data.

For example to send the event as a Slack Incoming WebHook message, you can
use this configuration::

    [event-handlers/b904ed23-v254-4ccf-8abd-edcae4d3324f]
    url = https://hooks.slack.com/services/n2unjSpQQ4L6JIOrHoO9CKXl
    extra_data = {
        "text": "{message}",
        "attachments": [
          {
          "pretext": "New event {id} SFTPPlus *MFT-023-QA*",
          "author_name": "{account.name}",
          "author_icon": "https://www.sftpplus.com/static/images/logo-80.png",
          "text": "{message}",
          "footer": "Sent by SFTPPlus HTTP Post Event",
          "mrkdwn_in": ["pretext"],
          "fields": [
            {"title": "IP", "value": "{account.peer.address}"},
            {"title": "Port", "value": "{account.peer.port}"},
            {"title": "Server ID", "value": 132},
            ]
          }
        ]}

Note the usage of `{id}` or `{message}` variables inside the key names or
string values.
In this case, they payload sent by the HTTP POST event handler contains the
following members::

    {
      "events": [ EVENT_DATA_AS_BEFORE ],
      "server": { SERVER_DATA_AS_BEFORE },
      "text": "Stopped authentication "AD DAP" of type ldap. Failed at start",
      "attachments": [
        {
        "pretext": "New event 20157 SFTPPlus *MFT-023-QA*",
        "author_name": "Process",
        "author_icon": "https://www.sftpplus.com/static/images/logo-80.png",
        "text": "Stopped authentication "AD DAP" of type ldap.",
        "footer": "Sent by SFTPPlus HTTP Post Event",
        "mrkdwn_in": ["pretext"],
        "fields": [
          {"title": "IP", "value": "182.12.31.21", "short": true},
          {"title": "Port", "value": "346", "short": true},
          {"title": "Server ID", "value": 132, "short: true"},
          ]
        }
    }

You will need to create the receiving URL on Slack,
by following the `Slack Incoming Webhooks <https://api.slack.com/messaging/webhooks>`_ documentation.

On Slack, the message will look something like this.

..  image:: /static/guides/http-event-slack.png
    :alt: HTTP Event as received on Slack.


Forward HTTP response headers to HTTP file uploads
--------------------------------------------------

For files uploaded over HTTP/HTTPS,
you can configure the SFTPPlus HTTP/HTTPS service to connect to an external HTTP API endpoint and forward the API response headers to the initial file upload request.

The request flow is as follows::

            /-upload-(1)--->\          /-HTTP-event-(2)--->\
    End User                  SFTPPlus>                     API Server
            \<-response-(4)-/          \<-API-response-(3)-/

With the following steps:

1. End users request a file upload to SFPPlus.
   SFTPPlus receives the file and store it on disk.
2. After the file was received, SFTPPlus sends an HTTP request to an external HTTP API endpoint
3. The external HTTP API endpoint will return a response and a set of response headers.
4. SFTPPlus will forward the API endpoint headers to the end user.

You can configure which headers are send to end users.

When the file is fully received, but SFTPPlus failed to get a valid response from the HTTP API endpoint,
you can configure SFTPPlus to forward to the end user a set of predefined headers.

The HTTP event handler that is designed to be used together with an HTTP file upload,
will receive events that will contain that `api_backend: yes` attribute:

You will configure the HTTP event handler with `target = 40017` and `data_filter = api_backend, yes`::

    [event-handlers/69ac315c-8026-11f0-864c-2fb5d87d556d]
    enabled = yes
    type = http
    name = Uploaded files backend API
    description = Used when files are uploaded, to notify our backend API

    url = https://10.12.0.12/internal-api

    target = 40017
    data_filter = api_backend, yes

The SFTPPlus HTTP/HTTPS file server used by end users is configured as::

  [services/d98653b8-8026-11f0-9ae2-936c37146441]
  enabled: Yes
  name: Customer Web UI
  type: http

  api_backend_uuid = 69ac315c-8026-11f0-864c-2fb5d87d556d
  api_passthrough_headers = filename, size
  api_partial_success_headers =
    error_message: File was received. No full name yet.
    filename: no-file-generated
    size: 0

With this configuration SFTPPlus will forward to end users the headers `filename` and `size`,
as received from the response from `https://10.12.0.12/internal-api`.

If the `https://10.12.0.12/internal-api` server is not available, end users will receive the following response::

    < HTTP/1.1 201 Created
    < Date: Sat, 23 Aug 2025 11:54:51 GMT
    < Server-Path: /path-as-request/by-end-user.txt
    < Filename: no-file-generated
    < Size: 0
    < Error_message: File was received. No full name yet.
