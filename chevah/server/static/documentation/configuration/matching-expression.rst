Matching expressions
====================

..  contents:: :local:

`Globbing expression
<http://en.wikipedia.org/wiki/Glob_%28programming%29>`_ or
`regular expression <http://en.wikipedia.org/wiki/Regular_expression>`_
can be used to select or exclude file names in the SFTPPlus configuration.


Globbing
--------

Globbing expressions provide a simple method for selecting values.
It is not suitable for excluding based on a certain pattern.

When globbing expressions are used, the values are matched using
case-insensitive matching.

Valid globbing wildcards characters:

* `*` - matches everything
* `?` - matches any single character
* `[seq]` - matches any character in seq
* `[!seq]` - matches any character not in seq
* `|` - (vertical bar) - separates multiple expression in a disjunction.

To match a meta-character, please wrap it in brackets.
For example, `[?]` matches the character `?`.

To only match PDF files, use the following configuration::

    [services/1ee4337a-22f7-4a67-9a77-5c3a508a8158]
    source_filter = *.pdf

You can define multiple globbing expression which will match if any of the
sub-expression is a match.
To match both PDF or TXT files, use the following configuration.
This will match both files like ``report.pdf`` or `summary.txt`::

    [services/1ee4337a-22f7-4a67-9a77-5c3a508a8158]
    source_filter = *.pdf | *.txt


Regular Expression
------------------

Regular expressions are case-sensitive by default.
They can be configured to perform case-insensitive matching.

To instruct the matching to be done using regular expressions,
the configured expression needs to be marked as ``m/EXPRESSION/``.

Enclosing the regular expressions inside the ``m/EXPRESSION/`` marker will
ensure that leading and trailing blank spaces are not ignored,
and are clearly identified when a person reads the configuration.

To perform a case-insensitive matching,
enclose the regular expression inside the ``m/EXPRESSION/i`` marker.
Note the trailing ``i``, which triggers the case-insensitive behaviour.

Regular expression syntax is implemented using the
`Python RE module <https://docs.python.org/2/library/re.html>`_,
which is modeled after the
`Perl <http://en.wikipedia.org/wiki/Perl>`_ implementation.

You can test the expression online using
`the Python section of RegexPlanet.com
<http://www.regexplanet.com/advanced/python/index.html>`_ (leave out
the leading ``*m/*`` and trailing ``*/*`` markers).

For example, to only match PDF files whose file names extensions are
either  ``*.pdf*`` or ``*.PDF*`` , use the following configuration::

    [services/27a31405-a963-4fb9-b4ee-09d415b1a30a]
    source_filter = m/.*\.pDf/i

In the case that you want to transfer only PDF files whose file name
extensions are strictly ``*.pdf*`` , use the following configuration::

    [services/27a31405-a963-4fb9-b4ee-09d415b1a30a]
    source_filter = m/.*\.pdf/

To exclude all files with the .pdf extension you can use the leading
*e/* marker to negate the define expression.
This avoids using the regex look-around zero-length assertion rules::

    [services/27a31405-a963-4fb9-b4ee-09d415b1a30a]
    source_filter = e/.*\.pdf/

The regular expression matching, including the exclude matching, are executed
as a **search** function.
That is, they will match any part of the targeted value.
When you want to do an example match, used the regex anchors for start of line
and end of line.

For example, to match only values like
``report-1.pdf`` or ``report-2.pdf`` and don't match values like
``previous-report-1.pdf`` use the anchors to explicitly instruct an exact
match from start to end, like so::

    [services/27a31405-a963-4fb9-b4ee-09d415b1a30a]
    source_filter = m/^report-\d\.pdf$/
