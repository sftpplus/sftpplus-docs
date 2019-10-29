SFTPPlus Documentation
======================

Documentation is using ReStructuredText format.

It is converted into HTML using Python Sphinx.

We generate documentation for 2 use cases:

* website integrated into public website.
* standalone, include into distributable for offline and LM access.

For standalone version, static files (images, fonts, CSS) are copied from the
website package.
The integrated version is triggered by the publish process.
The standalone version is triggered by the distributable build process.

The following annotation classes are available:

* seealso - green
* tip - green
* note - blue
* danger - strong red
* warning - red
* attention - yellow
* admonition:: Since Version - no color yet

The following tags are available for guide pages:

* client-side - for client-side functionalities and operations
* server-side - for server-side functionalities and operations
* file-transfer - for file transfer related operations, regardless of
  client and server side
* security - for security related topics
* since-version - for informing when the functionality was added

You can build the documentation using the following command. Files are
generated in build/doc/html::

    $ ./paver.sh documentation_standalone

And then open it with::

    $ firefox build/doc/html/index.html

The version design to integrate into website can be generated using this
command, but it is much harder to test. To test, you will need to publish it::

    $ ./paver.sh documentation_website

You can check that documentation is successfully built using::

    $ ./paver.sh test_documentation
