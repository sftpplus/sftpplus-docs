Working with the source monitor
-------------------------------


Understanding the changes poll interval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the `changes_poll_interval` passes, the application will read all
files, folders, and attributes (size, last modification time, etc) found in
the monitored folder.
Each snapshot is then compared with the previous.

If there are changes between the snapshots, they are notified to the
application.

Before doing the actual notification, the application will wait for changes
to be considered stable as defined by another option, `stable_interval`.

    ..  note::
        Lower values help detect changes quicker, but increase the load, CPU,
        and network usage for local and remote servers.

The poll interval might drift.

For example, with a value of ``72000`` and a transfer started at ``15:35``,
the product might be busy at ``15:35``.
In this case, the check is done only at ``15:36`` and the next check will be
scheduled for ``17:36``.


Changing the file stable period settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a new file is created or a file starts to be modified, it is not
processed by SFTPPlus right away.
This allows an external program to finish handling the file.

If no other changes to the file are observed after this interval, it is
then processed.

Criteria for a file to be considered stable:

* Size is not changed.
* Last modified time attribute is not changed.
* The configured stable interval has elapsed.

After the last modification is observed, this interval is then allowed to pass.

Each change will reset the stable interval for the file itself since each
file has its own stable counter.

..  FIXME:2454:
    Smarter polling for stable_interval smaller than changes_poll_interval

Since changes can only be observed with a resolution defined by
`changes_poll_interval`, the `stable_interval` needs to be a multiple.

The following will check new files every hour and transfer stable files
after two hours, even if the `stable_interval` is lower::

    [transfers/b904e6a6-c29b-4ccf-8abd-edcae4d3324f]
    changes_poll_interval = 3600
    stable_interval = 60
