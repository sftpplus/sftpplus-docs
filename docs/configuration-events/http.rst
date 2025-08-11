HTTP POST / Webhooks
====================

The HTTP POST Event Handler is where you can integrate SFTPPlus with your
web resource.
To read more, please go to
:doc:`the Developer Documentation </developer/http-api-event-handler>`.

In this section you will find the configuration option available to the
`http` event handler.

..  contents:: :local:

.. include:: /configuration-events/events-commons.include.rst


url
---

:Default value: ''
:Optional: No
:Values: * `URL`
         * Comma separated list of URLs (Since 3.51.0)
:From version: 2.10.0
:Description:
    Full URL for a resource used to receive the event details.
    For example: ``http://www.acme.io/http-post-hook-url``

    You can define a fall-back/redundant URL using a comma separates list of
    URLs.
    The first URL from the list will be used. When failing to get a response
    for the first URL, the remaining URLs are tried.
    Since 3.51.0.


timeout
-------

:Default value: `120`
:Optional: Yes
:Values: * Number of seconds.
:From version: 4.16.0
:Description:
    Duration, in seconds, to wait for a response from the HTTP server.

    If a response is not received during this period, the event handling fails.


retry_count
-----------

:Default value: `2`
:Optional: Yes
:From version: 3.48.0
:Values:
    * 0
    * Positive integer
:Description:
    This is the number of times a failed request is retried.

    When set to `0`, requests are never retried.

    The HTTP POST request is retried on connection errors or when the server
    returns a 5XX HTTP code.


retry_increase
--------------

:Default value: `10`
:Optional: Yes
:From version: 3.48.0
:Values:
    * 0
    * Positive real number
:Description:
    Number of seconds to add to each wait period before retrying.

    This is also the value of the first retry wait period.

    When set to `0`, there will be no waiting time, a retry is performed
    right away.


username
--------

:Default value: ''
:Optional: yes
:From version: 3.30.0
:Values: * Text.
:Description:
    Username used to authenticate to the remote HTTP server.

    Leave this value empty in order to leave out HTTP Basic authentication.

    ..  warning::
        For now, only HTTP Basic authentication is supported.
        This will send the username and password in clear text.


password
--------

:Default value: ''
:Optional: Yes
:From version: 3.30.0
:Values: * Plain text password.
         * Empty.
:Description:
    Password associated with the configured `username`.


request_method
--------------

:Default value: `POST`
:Optional: Yes
:Values: * `GET`
         * `POST`
         * `PUT`
:From version: 4.31.0
:Description:
    The HTTP method to use when making the request to the remote server.

    You can configure it to values like `POST` or `PUT`, to make a request
    containing the event data in the body payload.
    The value is case-insensitive.

    When configured to `GET`, it will make an `HTTP GET` request with
    an empty HTTP body.


http_content_type
-----------------

:Default value: `json`
:Optional: Yes
:Values: * `custom`
         * `json`
         * `legacy-webadmin`
         * `soap`
         * `xml`
:From version: 3.0.0
:Description:
    Format used to send the event over HTTP.

    Use `custom` to send the event as a custom Jinja2 template formated value.

    Use `json` to send the event as JSON formated.

    Use `soap` to send the event as human readable XML SOAP envelope.

    Use `xml` to send the event as machine readable application/xml.

    Use `legacy-webadmin` to send the events to the SFTPPlus WebAdmin server.

.. include:: /configuration/ssl-client.include.rst
.. include:: /configuration/ssl.include.rst


expected_response
-----------------

:Default value: Empty
:Optional: Yes
:Values: * Empty
         * Matching expression (globbing or regular expression)
:From version: 4.2.0
:Description:
    If the result result of a web-hook is not returned by the
    server with the HTTP status header, but by the content of the
    response, you can use this configuration to define an
    expected expression for a valid response.

    You can read more about how to use this configuration
    :doc: `in the HTTP API Developer</developer/http-api-event-handler>`
    documentation page.

    Leave this configuration empty to accept any response.


headers
-------

:Default value: Empty
:Optional: Yes
:Values: * Header-Name: Header-Value
         * Multiple headers on separate lines
:From version: 4.2.0
:Description:
    This defines a set of extra headers which are sent with each HTTP request.


extra_data
----------

:Default value: Empty
:Optional: Yes
:Values: * JSON string with variables.
         * Text with newline as the only non-printable characters.
         * EMPTY
:From version: 3.38.0
:Description:

    When left empty the HTTP request is sent using the standard SFTPPlus format
    associated with each content type.

    When this is defined, it will be configured as a template used to send the
    body of the HTTP request.

    When defined for `json` content, it defines the extra JSON values to be
    included in the HTTP POST payload.

    The JSON can be nested and contain multiple objects/dictionaries.
    The root JSON object can't be an array.

    JSON key and values can contain variables which will be replaced based
    on the event's data.

    For example to send the event as an Slack Incoming WebHook message::

        [event-handlers/b904ed23-v254-4ccf-8abd-edcae4d3324f]
        url = https://hooks.slack.com/services/n2unjSpQQ4L6JIOrHoO9CKXl
        http_content_type = json
        extra_data = {
            "text": "{id} {message}"
            "username": "{account.name}"
            }

    To send the event as custom text message::

        [event-handlers/b904ed23-v254-4ccf-8abd-edcae4d3324f]
        url = https://hooks.slack.com/services/n2unjSpQQ4L6JIOrHoO9CKXl
        http_content_type = custom
        headers = Content-Type: text/plain
        extra_data = New event with ID {id} from {account.name}. {message}

    For more details and examples see the :doc:`HTTP API
    documentation.</developer/http-api-event-handler>`

    Below you can find all the available variables.

    .. include:: /configuration/event-context-variables.rst.include

    Not available for `http_content_type = legacy-webadmin`.

    You can define a fall-back/redundant URL using a comma separates list of
    URLs.
    The first URL from the list will be used. When failing to get a response
    for the first URL, the remaining URLs are tried.
