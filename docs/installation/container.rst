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

The `pull-access` user has read-only access. It can download images and read the metadata, such as the list of available tags.

To download the image for a specific version, you can use the following command.
This will download the version based on Ubuntu 26.04, where you replace `5.X.Y` with your targeted version.::

    docker pull sftpplus.azurecr.io/sftpplus:5.X.Y-linux-x64

For the Ubuntu 26.04 ARM64 image use::

    docker pull sftpplus.azurecr.io/sftpplus:5.X.Y-linux-arm64

For the Alpine Linux 3.24 based image use::

    docker pull sftpplus.azurecr.io/sftpplus:5.X.Y-linux_musl-x64

We highly recommend copying this image into your own private registry.

For the full version, we don't have the "latest" image tag.

We encourage you to pin your deployment to a specific SFTPPlus version to avoid unexpected changes.


Kubernetes
----------

In Kubernetes, if you decide to use directly the SFTPPlus Azure Container Registry server you will need to setup access via a Kubernetes secret and use `imagePullSecrets`.

You can find more about Kubernetes `imagePullSecrets here <https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/>`_.

You can find example Kubernetes deployment manifests in our GitHub repository at `sftpplus/sftpplus-kubernetes <https://github.com/sftpplus/sftpplus-kubernetes>`_.

Helm chart
~~~~~~~~~~

The `SFTPPlus Helm chart <https://github.com/sftpplus/sftpplus-helm>`_ offers a simple Kubernetes installation with one controller, one or more workers, and shared storage.
For the full version, set the image to your licensed version in `sftpplus.azurecr.io` and give both workloads access through an image pull Secret.

Create the namespace and a registry Secret using the `pull-access` credentials supplied with your license::

    kubectl create namespace sftpplus
    registry_config_dir=$(mktemp -d)
    DOCKER_CONFIG="$registry_config_dir" docker login -u pull-access sftpplus.azurecr.io
    kubectl -n sftpplus create secret generic sftpplus-acr-pull \
      --from-file=.dockerconfigjson="$registry_config_dir/config.json" \
      --type=kubernetes.io/dockerconfigjson
    rm -rf "$registry_config_dir"

Kubernetes requires the image pull Secret to be in the same namespace as the Pods created by the Helm release.
Save the following values in a local `sftpplus-values.yaml` file, replacing `VERSION` with the licensed SFTPPlus version and `YOUR_SHARED_PVC` with an existing claim name:

..  code-block:: yaml

    image:
      repository: sftpplus.azurecr.io/sftpplus
      tag: VERSION-linux_musl-x64

    imagePullSecrets:
      - name: sftpplus-acr-pull

    storage:
      claimName: YOUR_SHARED_PVC

Use this file and two separate local password files to install the chart::

    helm repo add sftpplus https://helm.sftpplus.com/
    helm repo update sftpplus
    helm install sftpplus sftpplus/sftpplus \
      --namespace sftpplus \
      --values sftpplus-values.yaml \
      --set-file credentials.adminPassword=/path/to/admin-password.txt \
      --set-file credentials.workerPassword=/path/to/worker-password.txt

Select a different image tag suffix if you use another supported container variant.
Keep the password files outside source control, without trailing newlines, and delete them after confirming the installation works.
Sign in to Web Manager and change the initial `admin` password after installation.
The chart uses this password only when it first creates `server.ini`; changing the Helm value later does not change the password in an existing configuration.
Helm keeps the supplied initial passwords in its release record, so restrict access to that record as well.
An existing claim is optional; remove `storage.claimName` and configure `storage.claimSpec` with a storage class that supports access from all worker nodes to let the chart create one.
See the chart README for storage and external access options.
