# Place this file in `extension/demo_event_handler.py`
# inside SFTPPlus' installation folder.
#
# For the event handler set
# type = extension
# entry_point = python:demo_event_handler.DemoEventHandler
#
import json


class DemoEventHandler(object):
    """
    An event handler which just emits another event with details of the
    received events.

    Events handler API extensions can emit the events:

    * 20174 - Emitted by SFTPPlus for critical errors.
              Should not be explicitly emitted by the extension.
    * 20000 - For debug messages.
    * 20200 - For normal messages.

    This is also used as a documentation for the API and is included in
    the automated regression testing process.

    TARGET_EVENTS defined the events for which this handler will be triggered.
    """

    TARGET_EVENTS = [
        '99', '100', '102',  # Custom event ID.
        '20156',  # Component started.
        '20157',  # Component stopped.
        ]

    def __init__(self):
        """
        Called when the event handler is initialized in each worker and
        in the main process.
        """
        self._configuration = None

    def onStart(self, parent):
        """
        Called in the main process when the event handler starts.

        `parent.configuration` is the Unicode string defined in the
        extension configuration option.

        Any exception raised here will stop the event handler from
        starting.
        """
        self._parent = parent
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

        It can be used as validation for the event,
        before handling the event in a separate CPU core.

        Return the configuration for the event as Unicode.

        Return `None` when the event handling should be skipped and the
        `handle` function will no longer be called for this emitted event.

        As advanced usage, it can return a `deferred` which will delay
        the execution of the event, without keeping a worker process busy.
        This mechanism can also be used for implementing a wait condition
        based on which the event is handled or not.
        """
        if event.id == '1234' or event.account.name == 'fail-user':
            # Any exception raised here will stop the handling of this
            # specific event instance by the extension.
            raise RuntimeError('Rejected event.')

        if event.account.name == 'skip-user':
            # When `None` is returned the handling is skipped and the
            # `handle` function will not be called.
            return None

        if event.account.name == 'skip-emit':
            # When skipping, you can trigger emitting an event with custom
            # message and attached data.
            return None, {'message': 'Handling skipped.', 'extra': 'skip-emit'}

        if event.account.name == 'error-user':
            # You can skip and emit an event ID dedicated to errors.
            return None, {
                'event_id': '20202',
                'message': 'Can be a generic description for the error case.',
                'details': (
                    'Can contain details specific to this error. '
                    'Example a path to a file.'
                    ),
                'tb': 'Can include option traceback info as text.',
                }

        if event.account.name == 'delay-user':
            # For username `delay-user` we delay processing of the event
            # for 0.5 seconds.
            return self._parent.delay(0.5, lambda: 'delayed-configuration')

        # Events can be triggered as part of the event handling configuration.
        # You can have one for more events.
        # Event can have custom ID or use default ID.
        events = [
            {'event_id': '20201', 'message': 'Handling started.'},
            {'message': 'Default ID is 20200 as informational.'},
            ]
        # There is also the option of returning just the configuration,
        # without any extra events.
        return self._configuration, events

    @staticmethod
    def handle(event, configuration):
        """
        Called in a separate process when it should handle the event.

        This is a static function that must work even when
        onStart and onStop were not called.

        `configuration` is the Unicode value returned by
        getConfiguration(event).

        If an exception is raised the processing is stopped for this event.
        Future events will continue to be processed.
        """
        # Output will overlap with the output from other events as each
        # event is handled in a separate thread.

        if event.account.name == 'inactive-user':
            # The extension can return a text that is logged as an event.
            return 'Extension is not active from this user.'

        if event.account.name == 'test@proatria.onmicrosoft.com':
            # The extension has access to the Entra ID OAuth2 token.
            return 'Entra ID token: {}'.format(event.account.token)

        if event.account.name == 'ignored-user':
            # Don't handle events from a certain username.
            # The extension can return without any value, and no
            # event is emitted.
            return

        # Here we get the full event, and then we sample a few fields.
        message = (
            'Received new event for DemoEventHandler\n'
            '{event_json}\n'
            '-----------------\n'
            'configuration: {configuration}\n'
            '-----------------\n'
            'id: {event.id}\n'
            'account: {event.account.name}\n'
            'at: {event.timestamp.timestamp:f}\n'
            'from: {event.component.name}\n'
            'data: {event_data_json}\n'
            '---\n'
            )
        output = message.format(
            event=event,
            event_json=json.dumps(event, indent=2),
            event_data_json=json.dumps(event.data, indent=2),
            configuration=configuration,
            )

        # Inform the handler to emit several events at the end.
        # For a single event, it is recommended to pass only a dictionary.
        return [
            # The "message" attribute is required.
            {'message': 'A simple message.'},
            # Other attributes are allowed.
            {'message': 'state', 'value': 'OK'},
            # Explicit Event ID is also supported
            # For this case the attributes should match the attributes
            # required by the requested Event ID.
            # Event '20201' requires the `message` attribute.
            # Any extra attributes are allowed.
            {'event_id': '20201', 'message': output, 'extra': configuration},
            ]
