Oracle Database
===============

An `oracle-db` location provides access to an Oracle Database instance.

..  contents:: :local:


Introduction
------------

This page covers the SFTPPlus configuration options for connecting to an Oracle Database server and mapping files to database rows.

Check the :doc:`Oracle Database Transfers </operation-client/oracle-database>` documentation, to find out more about how to configure Oracle Database transfers.

.. include:: /configuration-client/locations-commons.include.rst


address
-------

:Default value: Empty
:Optional: No
:Values: * Host name or IP address of the Oracle DB server.
:From version: 5.18.0
:Description:
    Address of the server. IP or host name.


port
----

:Default value: `1521`
:Optional: Yes
:Values: * Number, greater than 0.
:From version: 5.18.0
:Description:
    Port number to connect to the server.


username
--------

:Default value: Empty
:Optional: No
:From version: 5.18.0
:Values: * Text.
:Description:
    Username used to authenticate to the server.


password
--------

:Default value: Empty
:Optional: Yes
:From version: 5.18.0
:Values: * Plain text password.
         * Empty.
:Description:
    This option specifies the password used to connect to the server.


service_name
------------

:Default value: Empty
:Optional: No
:From version: 5.18.0
:Values: * Plain text.
         * Empty.
:Description:
    Name of the database/PDB to connect to.


sql_file_column_type
--------------------

:Default value: `CLOB`
:Optional: No
:From version: 5.18.0
:Values: * `CHAR`
         * `CLOB`
         * `BLOB`
         * `NCLOB`
:Description:
    The SQL column type used to store the file content.

    Use `CHAR` for `CHAR`, `VARCHAR2`, `NCHAR`, or `NVARCHAR2` columns.


sql_table_list
--------------

:Default value: All tables for current user.
:Optional: No
:From version: 5.18.0
:Values: * Single SQL statement.
:Description:
    SQL statement to execute against the database to retrieve the list of possible tables to be considered for the transfer.

    Used to detect which tables are available as source or destination for transfers.

    The statement should return a single column, of type string, with the table names.

    When left empty, it will default to this query::

        SELECT OWNER || '.' || OBJECT_NAME
        FROM ALL_OBJECTS
        WHERE OBJECT_TYPE = 'TABLE' AND OWNER = (SELECT USER FROM dual)


sql_file_list
-------------

:Default value: Empty
:Optional: No
:From version: 5.18.0
:Values: * Single SQL statement.
:Description:
    SQL statement to execute against the database to retrieve the list of possible files to be considered for the transfer.

    Used to detect which files needs to be transferred from a source database.

    Use to detect if there are any conflicts when sending files to a destination database.

    It should return four columns, in this exact order and with this exact data types:

    1. File ID (number)
    2. File modification time (Oracle timestamp / date and time)
    3. File size (number)
    4. File name (string)

    This is a single statement, without semicolon at the end.
    Any trailing semicolon will be removed automatically.

    The SQL statement can be defined on multiple lines.


sql_file_read
-------------

:Default value: Empty
:Optional: No
:From version: 5.18.0
:Values: * Single SQL statement.
:Description:
    SQL statement to execute to retrieve the content of a file.

    It should return a single column, of type string, BLOB or CLOB.

    The statement should contain the `:FILE_ID` SQL bind variable.
    It will be replaced with the actual file ID when executing the statement.


sql_file_delete
---------------

:Default value: Empty
:Optional: No
:From version: 5.18.0
:Values: * Single SQL statement.
:Description:
    SQL statement to execute to delete a file.

    The statement should contain the `:FILE_ID` SQL bind variable.
    It will be replaced with the actual file ID when executing the statement.


sql_file_write
--------------

:Default value: Empty
:Optional: No
:From version: 5.18.0
:Values: * Single SQL statement.
:Description:
    SQL statement to execute to write the content of a file.

    If if data is stored as `BLOB` or `CLOB`, use the  `empty_blob() / empty_clob()` *SQL function* to initialize the value, then return it via the `:CONTENT` bind variable.

    The following placeholders can be used in the statement, and will be replaced with actual values when executing the statement:
    - `:FILE_CONTENT`: The content of the file being written.
    - `:FILE_ID`: The ID of the file being written.
    - `:FILE_NAME`: The name of the file being written.
    - `:FILE_SIZE`: The size of the file being written.
    - `:FILE_MODIFIED`: The modification time of the file being written.
