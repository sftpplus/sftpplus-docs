Container deployment
====================

..  contents:: :local:


Overview
--------

The SFTPPlus full version / production images are published via our private Azure Container Registry server.

The SFTPPlus trial version images are published via our Docker Hub public registry.
No authentication is required to pull the trial images.

For production usage, we recommend to create custom images based on our provided `Dockerfile`,
and to host them in your own private container registry.
Check the :doc:`Docker container image</installation/docker>` documentation page,
to learn how to create a custom image.

You can find out more about building a custom SFTPPlus container images in our GitHub repository at `sftpplus/sftpplus-docker <https://github.com/sftpplus/sftpplus-docker>`_.


Trial Image
-----------

Read more about the SFTPPlus trial image usage and deployment options in our `Docker Hub page <https://hub.docker.com/r/proatria/sftpplus-trial>`_.

You can pull the SFTPPlus trial image from Docker Hub using the following command::

    docker pull proatria/sftpplus-trial:latest


Production Image
----------------

To authenticate to the SFTPPlus Azure Container Registry server you need to use the following credentials, with the password provided as part of your license purchase.
The command will ask to type the password.::

    docker login -u pull-access sftpplus.azurecr.io

..  note::
    As a security best practice, the password is not passed via the command line.
    If you must use a non-interactive login (for example, in CI),
    you can pass the password on the command line with `docker login -u pull-access -p PASSWORD sftpplus.azurecr.io`.
    This is strongly discouraged because the password may be exposed in process listings, shell history, or logs.

To download the image for a specific version, you can use the following command.
This will download the version based on Ubuntu 22.04, where you replace `5.X.Y` with your targeted version.::

    docker pull sftpplus.azurecr.io/sftpplus:5.X.Y-linux

For the Alpine Linux 3.16 based image use::

    docker pull sftpplus.azurecr.io/sftpplus:5.X.Y-linux_musl

We highly recommend copying this image into your own private registry.

For the full version, we don't have the "latest" image tag.

We encourage you to pin your deployment to a specific SFTPPlus version to avoid unexpected changes.


Kubernetes
----------

In Kubernetes, if you decide to use directly the SFTPPlus Azure Container Registry server you will need to setup access via a Kubernetes secret and use `imagePullSecrets`.

You can find more about Kubernetes `imagePullSecrets here <https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/>`_.

You can find example Kubernetes deployment manifests in our GitHub repository at `sftpplus/sftpplus-kubernetes <https://github.com/sftpplus/sftpplus-kubernetes>`_.
