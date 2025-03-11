Azure BLOB Service
==================

An `azure-blob` location provides access over HTTPS to the
Azure BLOB Service of an Azure Storage account.

..  contents:: :local:

.. include:: /configuration-client/locations-azure-storage.include.rst

.. include:: /configuration-client/locations-commons.include.rst


Limitation
----------

The Azure BLOB service is designed to work as an `object` storage system,
and not as a file-system.

The main difference between Azure BLOB and other file storage systems,
is the lack of support for folders / directories.

The directory hierarchy is created by using a naming convention,
in which the file name contains a directory delimiter character.
Files are still stored in a flat structure.

A major implication, is that there are no empty folders.
Folders are generated based on section of a file name,
thus you can't just have a folder without a file.

At the same time, getting the files from a folder is implemented by searching for all the files for which their names start with that folder name.
This means that when you list a folder that doesn't exist the result is an empty list.


Keeping the source directory
----------------------------

When a transfer is configured with an Azure container as source
and configured to delete the source file on a success transfer,
the source folder might end up being empty.

In Azure BLOB, empty folders don't exist,
and SFTPPlus will generate an error when the source folder of a transfer doesn't exists.

To keep the source folder in Azure BLOB, it is recommend to always keep a file in the source directory.

You can configure the SFTPPlus transfer to ignore that file.

For example, you can create a file name ``.keep`` and configure a transfer to ignored it as::

    source_path = /manual-container/source/folder
    source_filter: ! .keep
