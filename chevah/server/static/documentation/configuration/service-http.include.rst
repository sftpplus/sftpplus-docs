.. include:: /configuration/ssl.include.rst
.. include:: /configuration/service-commons.include.rst

..  note::
    When clients use a web browser, a single session might generate
    multiple connections (e.g. one for getting the HTML page,
    one for its images, another one for its CSS files, etc.)
    This is why `maximum_concurrent_connections` is not always equal to
    the maximum number of concurrent users/sessions/clients.
