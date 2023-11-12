Local Development Guide
=======================

This section provides a comprehensive guide for setting up and managing the local development environment for the OC-Lettings project. It covers everything from cloning the project to running tests, aiming to make the setup process as smooth as possible for developers of all levels.

Clone the Project
-----------------

Start by cloning the project repository. This step is essential for obtaining the latest version of the source code:

.. code-block:: bash

   git clone https://github.com/immacora/OpenclassroomsProject13

Understanding this step:
- Cloning creates a local copy of the repository on your machine.
- Make sure Git is installed on your system before executing this command.

Retrieve the Project Image
--------------------------

To ensure a consistent development environment, use Docker to set up the project:

1. Install `Docker <https://docs.docker.com/get-docker/>`_ if not already installed.
2. Retrieve the `latest project image <https://hub.docker.com/r/immacora/oclettings/tags>`_ from Docker Hub.

Creating a Sentry Project
-------------------------

Sentry is used for error tracking and monitoring, which is crucial for maintaining the quality of the application:

1. Sign up for a `Sentry account <https://sentry.io/signup/>`_.
2. Follow these steps to create a new Sentry project:
   
   - Choose Django as the platform.
   - Name your project and complete the setup.
   - Copy the DSN (Data Source Name) provided by Sentry.

   Why this is important:
   - Sentry helps in identifying, tracking, and resolving issues efficiently.

Environment Setup
-----------------

Setting up the environment correctly is crucial for the application to run smoothly:

1. Create a .env file in the project's root directory.
2. Add the following environment variables with your specific values:

   .. code-block:: sh

      # django
      SECRET_KEY=YourDjangoSecretKey
      DEBUG=True

      # sentry
      SENTRY_DSN=YourSentryProjectDSN

   This step is vital for:
   - Configuring Django settings.
   - Integrating Sentry into the project.

Running the App with Docker
---------------------------

Docker simplifies the process of setting up and running the application:

.. code-block:: bash

   docker-compose up

Why Docker?
- It ensures that the app runs in an environment identical to other developers' setups.

Stopping and Removing Docker Containers
---------------------------------------

To stop and clean up after development, use:

.. code-block:: bash

   docker-compose down

Linting and Code Quality
------------------------

Maintaining code quality is vital. Run linting using:

.. code-block:: bash

   docker-compose exec web flake8

Testing the Application
-----------------------

Regular testing ensures the application's reliability:

.. code-block:: bash

   docker-compose exec web pytest

Coverage Reporting
------------------

To generate a coverage report, follow these steps:

.. code-block:: bash

   docker-compose exec web coverage run -m pytest
   docker-compose exec web coverage report -m

Why Coverage Reports?
- They provide insights into the effectiveness of tests and areas needing more coverage.
