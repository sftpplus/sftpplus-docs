.. container:: tags pull-left

    `server-side`
    `client-side`
    `containers`
    `deployment`


Deploying file transfers with Docker containers
###############################################

This page describes how you can deploy your SFTPPlus instance as a Docker
container.

..  contents:: :local:


Introduction
============

The SFTPPlus application can be executed in a Docker container
without losing any functionality.

At this time, this guide targets the Docker Linux containers.
SFTPPlus can also be executed in Windows Server native container and we will
update this documentation soon.

As the Docker container environment is a bit different than a normal Unix
daemon, minor configuration changes are required to make full use of the
infrastructure provided by a Docker container.

The SFTPPlus process can be started in the foreground,
in order to behave like an application designed for Docker.

    $ ./bin/admin-commands start-in-foreground

..  note::
    `start-in-foreground` is only supported on Linux.
    Support for Windows will be added soon, allowing to run SFTPPlus in
    Windows Server native containers.

We recommend that you enable the `standard-stream` event hander to send the
audit trail to standard output and be made available in the
`docker logs` tool.

The `standard-stream` behaves like any event handler.
You can filter what events are logged and you can configure the format
used to produce the logs.


Image Generation
================

We provide a `Dockerfile` and a set of scripts to help you get started
with creating a Docker image for SFTPPlus to suit your environment.

The files are available as a `public Git repository hosted on GitHub
<https://github.com/proatria/sftpplus-docker>`_.

Contact us if you need help with setting up an image for your
environment.


Docker Logging
==============

SFTPPlus can be integrated with the `json-file` Docker log driver and make
the log out available to the `docker log` command.

Use the `standard-stream` event handler available in SFTPPlus to send the
logs to the standard output (stdout).
As with any event handler you can filter the events which are logged.

For example, to log with `docker log` only targeting critical failures,
you can define the following event handler::

    [event-handlers/f040be6a-e158]
    enabled = Yes
    name = Standard Output Logger
    type = standard-stream
    target = 10092, 20024, 20033, 20058, 20059, 20102, 20106

Leave `target` empty to log all events.
Check out the :doc:`Event Handler Configuration</configuration/event-handlers>`
for more details about the available filters.


Docker Storages
===============

Dedicated Docker volumes should be used for storing user files and configuration
outside of the SFTPPlus container.
This allows the data to persist when the container no longer exists,
and also eases access to the data from outside of the container.
For example, given the `sftpplus_config` and `sftpplus_storage` Docker volumes,
a typical command to mount them in an SFTPPlus container would be::

    docker run --detach --name sftpplus \
        --publish 10020:10020 \
        --publish 10443:10443 \
        --publish 10022:10022 \
        --publish 10021:10021 \
        --publish 10900-10910:10900-10910 \
        --mount source=sftpplus_config,target=/opt/sftpplus/configuration \
        --mount source=sftpplus_storage,target=/srv/storage \
        sftpplus:4.0.0


Container and Service-Oriented Architecture (SOA)
=================================================

SFTPPlus is designed to be flexible and adaptable to any existing
infrastructure.
Inherently, this leads to many ways in which you can set up a Docker image.
In this section, we describe the key components to deploy SFTPPlus in a
Docker environment.

One of the core strengths for SFTPPlus is the ease of integration as
a service-oriented architecture (SOA).

You can utilize SFTPPlus to handle all the file transfer logic and issue it
as the central node for file transfers.
It can perform file transfer operations over a wide range of protocols to
adapt to the requirements or the constraints required by your partners.

In addition to being able to send files over HTTPS, your partners can use
the same account and credentials to send files over SFTP or FTPS.
These files are placed in the same storage, regardless of the file transfer
protocol used.

While SFTPPlus provides its own user identity management system and log
management system, in a SOA deployment you might already have an HTTP-based
API service for authentication and logging.
SFTPPlus fully supports HTTP-based API for authentication and auditing,
making use of your existing services.

Check out our :doc:`Developer Documentation</developer/index>` for more
details about how to use the HTTP API.

By using Docker Compose, you can create special purpose
containers with specialized instances listed below:

* SFTPPlus instance - Handle file transfers over SFTP / FTPS / WebDAV.
  Data storage is backed by a volume.

* Authentication and Authorization instance - Respond to authentication and
  authorization requests over HTTP.
  You can use this instance to authenticate other services inside
  your deployment.

* Audit instance - Receive, over HTTP, events and logs generated
  by SFTPPlus.
  Use this instance to process logs and events from other services.

* File Processor instance - Receives events over HTTP in order to
  further process them based on the rules specified by your
  business logic.
