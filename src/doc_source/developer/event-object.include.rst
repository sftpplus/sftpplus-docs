..  This file is included in multiple places where we need to document the
..  event object

The overall structure of the event object is presented below.

..  include:: /configuration/event-context-variables.rst.include

The members of `data` are specific to each event.
See :doc:`Events page</events/index>` for more details regarding the
data available for each event.

Many events have `data.path` and `data.real_path`, together with the
associated `data.file_name`, `data.directory_name`, `data.real_file_name`, and
`data.real_directory_name`.

Below is the description for the main members of the event object.

----

:name: id
:type: string
:optional: No
:description: ID of this event.
    See :doc:`Events page</events/index>` for the list of all available
    events.

----

:name: message
:type: string
:optional: No
:description: A human readable description of this event.

----

The `timestmap` contains the following attributes:

----

:name: timestamp
:type: string
:optional: No
:description: Date and time at which this event was created, as Unix timestamp
    with milliseconds.

----

:name: cwa_14051
:type: string
:optional: No
:description: Date and time in CWA 14051 at which this event was emitted.

----

The `account` contains the following attributes:

----

:name: uuid
:type: string
:optional: No
:description: UUID of the account emitting this event.
    In case no account is associated with the event, this will be the special
    `process account`.
    In case the associated account is not yet authenticated this will be the
    special `peer account`.

----

:name: name
:type: string
:optional: No
:description: Name of the account emitting this event.

----

:name: token
:type: string
:optional: Yes
:description: For Windows local or domain accounts a token that can be use to impersonate the account.
    For Azure AD accounts, when extra `api_scopes` are configured,
    this is the latest OAuth2 token that can be use to obtain acccess to an extra API
    or refresh a token.

----

:name: peer
:type: JSON Object
:optional: No
:description: Address of the peer attached to this account.
    This might be a local or remote address, depending on whether the account
    is used for client side or server side interaction.

----

The `peer` contains the following attributes:

----

:name: address
:type: string
:optional: No
:description: IP address of this connection.

----

:name: port
:type: integer
:optional: No
:description: Port number of this connection.

----

:name: protocol
:type: string
:optional: No
:description: OSI Layer 4 transport layer protocol used for this connection in
    the form of either `TCP` or `UDP`.

----

The `component` contains the following attributes:

----

:name: uuid
:type: string
:optional: No
:description: UUID of the component (service or transfer) emitting this event.

----

:name: type
:type: string
:optional: No
:description: Type of the component emitting this event.

----

The `server` contains the following attributes:

----

:name: uuid
:type: string
:optional: No
:description: UUID of the server emitting this event.

----

:name: type
:type: string
:optional: No
:description: Type of the server emitting this event.
