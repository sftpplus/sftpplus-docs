Extension API
=============

The `extension` event handler can be configured to allow the creation of custom event handlers implemented using the SFTPPlus API.

The extension code will be placed inside the `extension` folder located in the SFTPPlus base installation folder.

This event handler is targeted toward application developers.

..  contents:: :local:


Sample extensions
-----------------

SFTPPlus is distributed with a set of extensions designed to provide functionalities with very specific use cases.

Most probably, these extension are not useful for general usage.
If you think that any of them might help with your requirements, get in touch with our support team.

Below is are some extensions included in SFTPPlus:

* Delete the last line of a file
* Implement TOTP MFA authentication for an LDAP server that has no native TOTP support.
* Read / Write Microsoft Purview label for uploaded files. Required MPI SDK.

.. include:: /configuration-events/events-commons.include.rst


entry_point
-----------

:Default value: empty
:Optional: No
:Values: * ``python:dotted.path.EntryClassHandler``
:From version: 3.28.0
:Description:
    The API entry point is defined in the format `LANGUAGE:DOTTED.ENTRY.POINT`,

    `LANGUAGE` is the name of the language in which the extension is
    written.

    `DOTTED.ENTRY.POINT` is an expression defining the package, module, and class name which will receive the event.

    ..  note::
        At this moment, the event handler API supports the development of
        custom handlers based on the Python programming language.

    As an example, for the file ``extension/demo_event_handler.py`` defining the ``DemoEventHandler`` class, the configuration will be::

        entry_point = python:demo_event_handler.DemoEventHandler

    See :doc:`Python API Event Handler</developer/python-api-event-handler>` developer documentation for more details about how to use the event handler.


configuration
-------------

:Default value: empty
:Optional: Yes
:Values: * Free text
:From version: 4.0.0
:Description:
    A text value which is passed to the event handler together with each event.

    You can set it as JSON for structured data or BASE64 for binary data and decode it in the event handler.
