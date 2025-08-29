Developer Documentation
=======================

This section documents using the SFTPPlus API and integrate SFTPPlus with HTTP microservices or Python applications.

As part of the standard features, we provide public APIs to extend the identity
management, file access, audit functionality and more of the SFTPPlus
Server using HTTP-based micro-services / endpoints.

The HTTP APIs can be used to integrate file transfer processes with disparate
systems, such as web applications, that need to interface with SFTPPlus.

The Python API can be used to write custom event handlers.

We encourage developers to explore the API to see what is possible with the
current implementation.

If you are an existing customer or interested in developing with the API
beyond what is available in the documentation, please contact us for further
information including costs and conditions.

We currently have documentation for HTTP-based micro-services / endpoints and
Python-based event handlers.
Please contact us for C / Java code examples or for more HTTP / Python
examples.

.. grid:: 1 1 2 2
    :gutter: 2
    :padding: 0
    :class-container: surface

    .. grid-item-card:: :octicon:`book` HTTP File Transfer Service API
        :link-type: doc
        :link: ./http-api

        Find out the available APIs for the HTTP File Transfer Service.

    .. grid-item-card:: :octicon:`book` HTTP API User Authentication and Configuration
        :link-type: doc
        :link: ./http-api-authentication

        Learn how to manage user authentication and configuration using the HTTP API,
        including endpoints for user management and access control.

    .. grid-item-card:: :octicon:`terminal` HTTP POST Event Handler
        :link-type: doc
        :link: ./http-api-event-handler

        Learn how you can integrate SFTPPlus with your web resource using the HTTP POST Event Handler.

    .. grid-item-card:: :octicon:`stack` Python API Event Handler
        :link-type: doc
        :link: ./python-api-event-handler

        Custom event handlers can be written using the Python programming language.
        Explore the available information and examples.

    .. grid-item-card:: :octicon:`stack` Python API LDAP Authentication
        :link-type: doc
        :link: ./python-api-ldap-authentication

        SFTPPlus allows developers to write custom authentication handling code to augment the standard LDAP authentication functionality.

..  toctree::
    :maxdepth: 1
    :hidden:

    http-api
    http-api-authentication
    http-api-event-handler
    python-api-event-handler
    python-api-ldap-authentication
