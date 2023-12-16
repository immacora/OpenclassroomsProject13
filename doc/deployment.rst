Deployment Guide (DigitalOcean)
===============================

This section outlines the steps for deploying the OC-Lettings project on DigitalOcean using CircleCI for continuous integration and continuous deployment (CI/CD). It explains how each commit can be automatically tested, built, and deployed, ensuring a streamlined and efficient deployment process.


Overview of the Deployment Process
----------------------------------

Each commit to the repository initiates a series of automated actions:

- **Compilation, Linting, and Testing**: The CI/CD pipeline on CircleCI compiles, lints, and tests the application. It is mandatory for the test coverage to exceed 80%; otherwise, the job will fail.
- **Docker Image Building and Pushing**: If the commit is on the main branch and the previous jobs were successful, the pipeline builds a Docker image (tagged with the hash of the last commit) and pushes it to Docker Hub.
- **Deployment on DigitalOcean**: Following successful image creation, the pipeline initiates the deployment and production job on DigitalOcean.

Creating a Server on DigitalOcean
---------------------------------

To set up a server for deployment:

1. Sign up for a `DigitalOcean account <https://www.digitalocean.com/>`_.
2. Create a new Droplet with Ubuntu (23.10) and SSH Key Authentication.
   - Set up a `Firewall <https://docs.digitalocean.com/products/networking/firewalls/how-to/create/>`_ with SSH, HTTP, and HTTPS rules.
   - Install `docker <https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04>`_ and `docker-compose <https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04>`_ on your Droplet.

Creating a CI/CD Pipeline with CircleCI
---------------------------------------

To automate the deployment process:

1. Fork the `project <https://github.com/immacora/OpenclassroomsProject13>`_ on your GitHub account.
2. Create a `CircleCI account connected to GitHub <https://circleci.com/docs/first-steps/#sign-up-and-create-an-org>`_.
3. Set up a new project on the `CircleCI app <https://app.circleci.com/>`_ linked to your forked repository.
   - In the Project Settings, add an SSH Key and copy its Fingerprint to paste it in Environment Variables:

     .. code-block:: sh

        Hostname: YourServerPublicIPAddress; Private Key: YourServerPrivateSSHKey

   - Define environment variables in the Project Settings:

     .. code-block:: sh

        SECRET_KEY=YourDjangoSecretKey
        SENTRY_DSN=YourSentryProjectDSN
        ALLOWED_HOSTS=YourAllowedHosts
        DOCKERHUB_PASSWORD=YourDockerHubPassword
        DOCKERHUB_USERNAME=YourDockerHubUsername
        USER=YourServerLogginUsername
        IP=YourServerIP
        SERVER_SSH_FINGERPRINT=YourSSHFingerprint

This guide aims to provide a clear and detailed roadmap for deploying the OC-Lettings project on DigitalOcean, ensuring a smooth and reliable process.
