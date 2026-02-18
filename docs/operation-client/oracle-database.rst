Oracle Database Transfers
=========================

..  contents:: :local:


Overview
--------

This page describes how to configure SFTPPlus to manage files stored as rows in an Oracle Database.

The Oracle Database location is designed to adapt to a wide variety of table structures.
It is recommended to store the file content in a `CLOB`, `NCLOB` or `BLOB` column.
This will allow storing large files as streams, with reduced memory usage.
Optional file metadata like file name, file id or file modified time can be stored in separate columns.

If the file content is stored as `CHAR`, `VARCHAR2`, `NCHAR`, or `NVARCHAR2`,
the transfers are limited to small files, as the Oracle Database has limits on the size of these types.
The default limits are around 2 KB.
You can transfer up to a maximum of 32 KB, but this depends on the database configuration.

Most examples from this documentation use the following table structure::

    CREATE TABLE sftpplus.FilesCLOB (
        id VARCHAR2(50),
        modified TIMESTAMP(2),
        name VARCHAR2(250),
        parent_path VARCHAR2(250),
        content CLOB
    );

And the successful transfers are moved to an archive table,
with a similar structure::

    CREATE TABLE sftpplus.FilesCLOBArchive (
        id VARCHAR2(50),
        modified TIMESTAMP(3) WITH TIME ZONE,
        name VARCHAR2(250),
        parent_path VARCHAR2(250),
        content CLOB
    );


Limitations
-----------

* Oracle Database 12.1 or newer are supported without the need to install the Oracle Instant Client files.
* Oracle Database 9 or newer are supported by downloading and installing the
  Oracle Instant Client files.
* Alpine Linux is not supported.
* File names can't contain the forward slash (/) character.
* Files that don't have a parent, should not have the same name as one of the parents.
* Parent names can't contain the `NULL` value.
  Since Oracle Database does not support empty text values, and will convert them to `NULL`,
  when you want to store file in the root, without a parent, use the forward slash (/) character "magic value" as the name of the parent.
  Use the single forward slash character for files without a parent.
* Table names are handled case-insensitive.
  The `$`, `#` or space characters are not allowed. Contact our support if you need to interact with tables having these characters in the name.
* The content of the file must be stored in a CHAR, VARCHAR, CLOB or BLOB column.
* National character types like NCHAR, NVARCHAR, NCLOB are supported only for `AL16UTF16`.
* BFILE type is not supported.
* Each file must be stored in a single row, that is uniquely identified using a text value.
  You can use the `ROWID` pseudo-column if your table does not have a unique ID column.
* When sending text files to the database, the source file should be encoded in UTF-8.
  Other encodings are not supported. [#7199]
* When reading text files from the database, the content is written as UTF-8 encoded files.
  Other encodings are not supported.
* Only simple SQL statements are supported. PL/SQL is not supported. Contact us if you need PL/SQL support.


Database row to file path mapping
---------------------------------

SFTPPlus will try to map the file content stored as rows in Oracle DB tables to files in a directory structure.
The mapping is done using the following rules:

* Each table is considered to be a separate directory.
* The table name is used as the directory name.
* The file path and file name are retrieved from columns in the table,
  using the `sql_file_list` configuration option.
* The final file path is constructed as `/<table_name>/<parent>/<file_name>`.

When parent path is returned as forward slash (/), the file is considered to be in the root of the table.

The parent path column should not contain values that end or start with the forward slash character (/).
The parent path value can contain the forward slash character inside the value.
This can be used to simulate sub-directories.

Avoid using characters that are rejected by Windows or Linux filesystems,
such as:

* `<` (less than)
* `>` (greater than)
* `:` (colon)
* `"` (double quote)
* `\\` (backslash)
* `|` (vertical bar or pipe)
* `?` (question mark)
* `*` (asterisk)


Discovery of tables available for transfers
-------------------------------------------

As part of your Oracle Database server you might have many tables, not all of them being used for file transfers.
To help SFTPPlus discover which tables are available for transfers,
the `sql_table_list` configuration option is required.
It is configured with a SQL query that returns the list of tables names.

The default configuration will try to retrieve all the tables available for the current user.

It is recommended to provide a custom SQL query that will return only the tables used for file transfers.

For example, to only return the tables available to the current user that have `FILE_TRANSFERS` in their name, you can use this query::

    sql_table_list =
      SELECT OWNER || '.' || OBJECT_NAME
      FROM ALL_OBJECTS
      WHERE
        OBJECT_TYPE = 'TABLE'
        AND OWNER = (SELECT USER FROM dual)
        AND OBJECT_NAME LIKE '%FILE_TRANSFERS%'

Another example, to only return the tables owned by the current user,
regardless of name::

    sql_table_list =
      SELECT DISTINCT OBJECT_NAME
      FROM USER_OBJECTS WHERE OBJECT_TYPE = 'TABLE'


Discovery of parent paths
-------------------------

The files can be stored as rows with an optional `parent_path` column.
This can be used to filter the available files with a minimum performance impact.

For example, to show all the currently available parent paths you can use this query::

    sql_parent_list =
      SELECT UNIQUE(parent_path) FROM :TABLE_NAME

The above query only works when the table is already populated with rows that are assigned to parent paths.

To help SFTPPlus discover empty parent paths, you can create a row for each parent using the `NULL` value or single space character as the magic value for the *file name*.
The content of this file is ignored and the file will not be transferred.

You can even use static queries.
For example, to have `inbox`, `outbox`, and `archive` paths discoverable to SFTPPlus,
you can configure the following query::

    sql_parent_list =
      SELECT * FROM (VALUES ('inbox'), ('outbox'), ('archive'))
      AS AD_HOC_TABLE("parent_path")

..  note::
    Parent paths can contain the forward slash (/) path separator.
    SFTPPlus will list all the available sub-path, including recursive ones,
    as part of a single operation.


File listing
------------

As part of a transfer,
SFTPPlus will try to list/discover files stored in an Oracle Database by executing a SQL query.
The SQL query is used to retrieve the file metadata and it should return the columns in the following order:

* File unique ID.
  A number or text identifier for the file.
  You can use the `ROWID` pseudo-column if your table does not have a unique ID column.
* File modification timestamp.
  Oracle DB timestamp when the file was last modified.
  You can use a placeholder like `TO_TIMESTAMP('2000/12/28', 'YYYY/MM/DD')`
* File size.
  A number with the size of the file in bytes.
  You can use `0` value if you don't have this information.
* File name.
  The name of the file as text.

..  note::
    The SQL query can return more rows.
    The actual file that are transferred are based on the transfer configuration,
    which can filter files by name, age, or skip file that were already transferred.

Below is an example query can be used for file discovery.
All files are named with the `db-export-` prefix.
The table has no dedicated file ID, so we use the `ROWID` pseudo-column.
For this example,
the file modification time is stored using a date and time value like ``10-Sep-02 14:10:10.123000`` so we convert it to Unix timestamp::

    sql_file_list =
        SELECT
          ROWID,
          TO_TIMESTAMP(last_update, 'DD-Mon-RR HH24:MI:SS.FF'),
          DBMS_LOB.GetLength(content),
          parent_path,
          'db-export-' || name
        FROM :TABLE_NAME
        WHERE parent_path = :PARENT_PATH
        ORDER BY name
        FETCH FIRST 10 ROWS ONLY

This query is executed multiple times.
Make sure it is efficient and uses indexes if possible.

If you don't need to support sub-folders,
the parent name should be returned as a text value containing a **single forward slash** character.::

    sql_file_list =
        SELECT
          ROWID,
          insert_data,
          DBMS_LOB.GetLength(content),
          '/',
          name
        FROM sftpplus.FilesCLOB
        ORDER BY name
        FETCH FIRST 10 ROWS ONLY

..  note::
    Don't use an empty text value since this will cause Oracle DB to convert the empty space into the `NULL` value which will not match any parent text value.


File read / download
--------------------

When SFTPPlus needs to download a file from the Oracle Database,
it will execute a SQL query to retrieve the file content.
The query must return a single column with the file content as `CHAR` (or any CHAR variants), `CLOB` or `BLOB`.

The query must contain the `:FILE_ID` bind variable.
This variable will be replaced with the actual file ID, as returned by the `sql_file_list` query.

Below is an example query that can be used to read the file content::

    sql_file_read =
        SELECT content
        FROM sftpplus.FilesCLOB
        WHERE id = :FILE_ID


File delete
-----------

When SFTPPlus needs to delete a file from the Oracle Database,
it will execute a SQL query to delete the file.

The query must contain the `:FILE_ID` bind variable.
This placeholder will be replaced with the actual file ID, as returned by the `sql_file_list` query.

Below is an example query that can be used to delete a file::

    sql_file_delete =
        DELETE FROM :TABLE_NAME
        WHERE id = :FILE_ID


File write / upload
-------------------

When SFTPPlus needs to upload a file to the Oracle Database,
it will execute a SQL query to write the file content.

The format of the query depends on the type of column used to store the file content.
For `BLOB` columns, the `empty_blob()` SQL function must be used to initialize the value,
and the actual content is passed via the `:CONTENT` bind variable.
For `CLOB` or `NCLOB` columns, the `empty_clob()` SQL functions must be used to initialize the value.

The query can contain the following placeholders:

* `:FILE_CONTENT` **required**:  The content of the file to be uploaded.
* `:FILE_ID`: The unique identifier of the file.
  This value depends on the source location of the file.
  Not all source locations will provide a file ID.
  When not available, a unique `UUID4` text value is used.
* `:FILE_NAME`: The name of the file to be uploaded.
* `:PARENT_PATH`: The name of parent of the uploaded file,
  or empty text when the file is in the root path.
* `:FILE_SIZE`: The size of the file to be uploaded, in bytes.
* `:FILE_MODIFIED`: The modification time of the file to be uploaded, as Oracle timestamp.
  If not available, the value `0` is used.

Below is an example used to insert a new row of type CLOB::

    sql_file_column_type = clob
    sql_file_write =
      INSERT INTO sftpplus.FilesCLOB (id, modified, name, parent_path, content)
      VALUES (
          :FILE_ID,
          :FILE_MODIFIED,
          :FILE_NAME,
          :PARENT_PATH,
          empty_clob()
      )
      RETURNING content INTO :FILE_CONTENT

Below is an example query that can be used to insert a new row of type CHAR,
the file name is generated based on modified data and size.
The parent name is optional, and you don't have to use it::

    sql_file_column_type = char
    sql_file_write =
      INSERT INTO sftpplus.FilesVCHAR (id, modified, name, content)
      VALUES (
          :FILE_ID,
          :FILE_MODIFIED,
          :FILE_SIZE || :FILE_NAME,
          :FILE_CONTENT
      )

Below is an example query that can be used to update an existing BLOB::

    sql_file_column_type = blob
    sql_file_write =
        UPDATE sftpplus.FilesBLOB
        SET content = empty_blob()
        WHERE name = :FILE_NAME
        RETURNING content INTO :FILE_CONTENT


NCLOB values are initialized using the `empty_clob` function::

    sql_file_column_type = nclob
    sql_file_write =
        UPDATE sftpplus.FilesNCLOB
        SET content = empty_clob()
        WHERE name = :FILE_NAME
        RETURNING content INTO :FILE_CONTENT


Single table for multiple transfers
-----------------------------------

With SFTPPlus you can configure the same database table with multiple transfers.

To have files processed by a particular transfer you can use the transfer's `source_filter` configuration option.
For example, a payment order transfer will handle any file with the name matching `PAY_*.csv` while a receivable transfer will handle any file with name `REC_*.csv`.

To push/write rows in the same table from multiple transfers, you will need to make sure that each transfer will push files using a specific filename prefix.
This can be enforced using the `destination_path_actions` configuration option of a transfer.

This is a simple configuration and works for tables that don't have a large number of rows, as long as you follow the filename prefix convention.

When the database table contains a large number of rows, retrieving all files in each transfer and then filtering them outside of the database can cause performance issues.

In this case, it is recommended to keep in the database, an identifier that can associate a file to the desired transfer.

This can be implemented using a separate `parent_path` column.
The value of the `parent_path` column is represented in SFTPPlus as the parent folder of the file.

You will transfer the files as if a single table has multiple sub-paths, one path dedicated to each transfer.

..  note::
    The parent paths are created on demand as rows are added to the table.
    SFTPPlus will accept any parent path, without validating it against a predefined list of valid parents.


Oracle version 9, 10, and 11
----------------------------

In order to connect to Oracle Database servers running versions 9, 10 or 11,
the Oracle Instant Client files are required to be downloaded and copied together with the SFTPPlus installation files.

The `Oracle Instant Client can be downloaded from here <https://www.oracle.com/database/technologies/instant-client/downloads.html>`_.
Both **Basic Package** or **Basic Light Package** are compatible with SFTPPlus.

We recommend to copy the files inside the SFTPPlus `configuration` folder.
For example at `C:\\Program File\\SFTPPlus\\configuration\\instantclient`
or `/opt/sftpplus/configuration/instantclient`.

Use the `oracle_client_path` configuration option from the SFTPPlus Oracle Database location to specify the path where the Instant Client files are copied.

..  attention::
    When SFTPPlus was already connected to a newer Oracle Database server and you want to also connect to an older Oracle DB server,
    after configuring the Instant Client path.
    you will need to restart the whole SFTPPlus service process.
    Most of the time, the location is already stopped, so no extra steps are required,
    other than starting the location and attempt connecting to the Oracle Database server.

..  note::
    Since we are dealing with very old Oracle Database servers, that are no longer supported by Oracle, it is recommended to contact our support team to check the compatibility of SFTPPlus with your exact Oracle Database server.
