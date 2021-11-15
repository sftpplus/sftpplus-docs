Python API Event Handler
========================

..  contents:: :local:


Introduction
------------

SFTPPlus allows developers to write custom event handlers using the
Python programming language.

The handlers are execute in separate independent processes / CPU cores,
without shared memory.
This is why the `handle()` method of the extension needs to be a
`@staticmethod` and always received the configuration.

The handler is initialized multiple time.
One instance is created in the main process and extra instances are created
for each CPU.

A single extension instance can have the `onStart(configuration)` / `onStop()`
method called multiple times during its lifetime.
`onStart(configuration)` and `onStop()` methods are only called for the
instance running in the main process.

The code for the event handler needs to be placed in a Python file (module)
inside the `extension/` folder from the SFTPPlus installation folder.

You can find an extensive example inside the `extension/demo_event_handler.py`
folder of the default SFTPPlus installation.
Below is a brief example::

    class DemoEventHandler(object):
        """
        An event handler which just prints to standard output the ID of the
        received events.
        """

        def __init__(self):
            """
            Called when the event handler is started in each worker and
            in the main process.
            """

        def onStart(self, parent):
            """
            Called in the main process when the event handler starts.

            `parent.configuration` is the Unicode string defined in the
            extension configuration option.

            Any exception raised here will stop the event handler from
            starting.
            """
            self._configuration = parent.configuration

        def onStop(self):
            """
            Called in the main process when the event handler stops.
            """
            self._configuration = None

        def getConfiguration(self, event):
            """
            Called in the main process before dispatching the event to
            the worker process.

            Return the configuration for the event as Unicode.

            It can be used as validation for the event,
            before handling the event in a separate CPU core    .

            Any exception raised here will stop the handling of this
            specific event instance by the extension.
            """
            return self._configuration

        @staticmethod
        def handle(event, configuration):
            """
            Called in a separate process when it should handle the event.

            This function should work even when onStart and onStop were not
            called.

            `configuration` is the Unicode value returned by
            getConfiguration(event).
            """
            print(b'Configuration %s' % (configuration,))
            print(b'Received %s' % (event.id,))


This event handler can be configured as::

    [event-handlers/56df1d0a-78c6-11e9-a2ff-137be4dbb9a8]
    enabled = yes
    type = extension
    name = python-extension

    entry_point = python:extensions.demo_event_handler.DemoEventHandler

    configuration = some-free-text-configuration


Execution queue
---------------

SFTPPlus will only handle in parallel N events, where N is based on
the number of CPUs available to the OS.

All the other events required to be handled by the extensions are placed
into a queue.

The extension is called to handle the event only when there are free CPUs.

To prevent misconfiguration, there is a hard limit of 10 minutes for how long
an event can stay in the queue and for processing the event.


Event data members
------------------

The event object received in the handler has the following structure.

.. include:: /developer/event-object.rst.include
