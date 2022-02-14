Matching expressions
====================

..  contents:: :local:

`Globbing expression
<http://en.wikipedia.org/wiki/Glob_%28programming%29>`_ or
`regular expression <http://en.wikipedia.org/wiki/Regular_expression>`_
can be used to select or exclude file names in the SFTPPlus configuration.

Both glob and regex standards are designed to define inclusion rules.
In SFTPPlus, we have added glob and regex extensions to allow exclusion /
negation rules.

SFTPPlus supports multiple types of matching expression grammars/methods.
In order to instruct SFTPPlus how to match, we use the
`METHOD_ID/MATCHING_EXPRESSION/MODIFIERS` syntax.

`METHOD_ID` is a single letter defining the type of matching method to be used.
`MODIFIERS` are optional and specific to each method.
When no `METHOD_ID` is specified, the `globbing` method is used.


Globbing
--------

Globbing expressions provide a simple method for selecting values.
It is not suitable for excluding based on a certain pattern.

When globbing expressions are used, the values are matched using
case-insensitive matching and matching is done across multiple lines.

Valid globbing wildcards characters:

* `*` - matches everything
* `?` - matches any single character
* `[start-end]` - matches any character between start and end characters
* `[!seq]` - matches any character not in seq
* `|` - (vertical bar) - separates multiple expressions in a disjunction.
* `!` - excludes following expression(s) when used at the very beginning. This
  is the negation operation.

When using `|` (vertical bar) to match multiple expressions, but also using `!`
at the very beginning, the conjunction rule is used for exclusion.

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

To not match temporary files, you can exclude them with the following
configuration (this will match all files not ending with `.tmp`)::

    [services/1ee4337a-22f7-4a67-9a77-5c3a508a8158]
    source_filter = ! *.tmp

To exclude all files ending with either `.tmp` or `.filepart`, use the
exclamation mark only once, at the very beginning of the whole expression::

    [services/1ee4337a-22f7-4a67-9a77-5c3a508a8158]
    source_filter = ! *.tmp | *.filepart


For multi-line matching, you can for example use
`*<Response>*Success*</Response>*`
to match the following text::

    SOME OTHER TEXT
    <Response>
      Success
    </Response>
    MORE TEXT

You can also define a globbing pattern using the following explicit syntax::

    [services/1ee4337a-22f7-4a67-9a77-5c3a508a8158]
    source_filter = g/*.pdf | *.txt/


Date and time globbing expressions
----------------------------------

You can define a file pattern based on current date and time.

The rule for date- and time-based matching is case-insensitive.

This is useful if your files or values contain date- and time-related values,
and you want to filter them based on date (current or non-current) or based on
the relation to the current date and time.

The following date and time components are available.
Examples for the 7th of September 2009, at 16 hours, 5 minutes and 4
seconds AM:

* {year.decimal} - Year with century as a decimal number. Example: 2009
* {year.no_century} - Year without century as a zero-padded decimal number.
  Example: 09
* {month.decimal} - Month as a decimal number. Example: 9
* {month.padded} - Month as a zero-padded decimal number. Example: 09
* {month.name} - Month as locale’s full name. Example: September
* {month.abbreviated} - Month as locale’s abbreviated name. Example: Sep
* {day.padded} - Day of the month as a zero-padded decimal number.
  Example: 07
* {day.decimal} - Day of the month as a decimal number. Example: 7
* {day.of_year_padded} - Day of the year as a zero-padded decimal number.
  Example: 250
* {day.name} - Weekday as locale’s full name. Example: Friday
* {day.abbreviated} - Weekday as locale’s abbreviated name. Example: Fri
* {hour.padded_24} - Hour (24-hour clock) as a zero-padded decimal number.
  Example: 16
* {hour.decimal_24} - Hour (24-hour clock) as a decimal number. Example: 16
* {hour.padded_12} - Hour (12-hour clock) as a zero-padded decimal number.
  Example: 04
* {hour.decimal_12} - Hour (12-hour clock) as a decimal number. Example: 4
* {hour.am_pm} - Equivalent of either AM or PM.
* {minute.padded} - Minute as a zero-padded decimal number. Example: 05
* {minute.decimal} - Minute as a decimal number. Example: 5
* {second.padded} - Second as a zero-padded decimal number. Example: 04
* {second.decimal} - Second as a decimal number. Example: 4

For example, to select any .TXT file from the `/reports/` directory starting
with `acct_` for the current month, where files are in the format of
`acct_20_08.txt` for month of August 2020,
you can use the following expression::

    source_filter = t/*reports/acct_{year.no_century}-{month.padded}.txt/

The date and time substitution values are replaced with the current date and
time when the filtering rule is executed or applied.
Assuming that today is 8th of August 2020, the above rule will match the
following file: `acct_20_08.txt`. It will not match files like `acct_20_07.txt`
or `acct_19_08.txt`.

You can also filter based on the date and time of the previous day.
To do that use the following expression (note the `-1d` value at the end)::

    source_filter = t/*reports/acct_{year.no_century}-{month.padded}.txt/-1d


Regular Expressions
-------------------

To instruct the matching to be done using regular expressions,
the configured expression needs to be marked as ``m/EXPRESSION/``.

Enclosing the regular expressions inside the ``m/EXPRESSION/`` marker will
ensure that leading and trailing blank spaces are not ignored,
and are clearly identified when a person reads the configuration.

By default the regular expression have the following characteristics:

* case-sensitive
* single line matching
* search matching

To perform a **case-insensitive** matching,
enclose the regular expression inside the ``m/EXPRESSION/i`` marker.
Note the trailing ``i``, which triggers the case-insensitive behaviour.

To match across the **multiple lines** you need explicitly use the
`\n` character, as the dot regex matching does not include newlines.
For example you can use `m/<Back>.*\n.*Success.*\n</Back>`
if you have the following text::

    SOME OTHER TEXT
    <Back>
      Success
    </Back>
    MORE TEXT

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
    source_filter = m/.*\.pDf$/i

In the case that you want to transfer only PDF files whose file name
extensions are strictly ``*.pdf`` , use the following configuration::

    [services/27a31405-a963-4fb9-b4ee-09d415b1a30a]
    source_filter = m/.*\.pdf$/

To **exclude** all files with the .pdf extension you can use the leading
*e/* marker to negate the define expression.
This avoids using the regex look-around zero-length assertion rules::

    [services/27a31405-a963-4fb9-b4ee-09d415b1a30a]
    source_filter = e/.*\.pdf$/

Regular expression matchings, including the exclusion matching,
are executed as **search** functions.
That is, they will match any part of the targeted value.
When you want to do an **exact match**,
use the regex anchors for start-of-line and end-of-line.

For example, to match only values like
``report-1.pdf`` or ``report-2.pdf`` and don't match values like
``previous-report-1.pdf`` use the anchors to explicitly instruct an exact
match from start to end, like so::

    [services/27a31405-a963-4fb9-b4ee-09d415b1a30a]
    source_filter = m/^report-\d\.pdf$/
