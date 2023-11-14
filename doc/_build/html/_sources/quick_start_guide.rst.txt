Quick Start Guide
=================

This Quick Start Guide is designed to help you get the OC-Lettings application up and running on your local machine as quickly as possible. Follow these steps to start using the application.

Prerequisites
-------------

Before you begin, ensure you have the following installed:

- Python 3.12
- Docker 4.24.2
- Git

Step 1: Clone the Repository
----------------------------

Clone the OC-Lettings repository to your local machine:

.. code-block:: bash

   git clone https://github.com/immacora/OpenclassroomsProject13

Step 2: Set Up Your Environment
-------------------------------

Create a `.env` file in the project's root directory and add the necessary environment variables:

.. code-block:: sh

   # django
   SECRET_KEY=YourDjangoSecretKey
   DEBUG=True

   # sentry
   SENTRY_DSN=YourSentryProjectDSN

Step 3: Run the Application Using Docker Compose
------------------------------------------------

Navigate to the root directory of the project and start the application using Docker Compose:

.. code-block:: bash

   docker-compose up

Step 4: Access the Application
------------------------------

Once the application is running, access it via:

- Localhost Main Page: `http://localhost:8000/ <http://localhost:8000/>`_
- Admin Panel: `http://localhost:8000/admin/ <http://localhost:8000/admin/>`_

Credentials for Admin Access:

- Username: `admin`
- Password: `Abc1234!`

Congratulations! You have successfully set up and started the OC-Lettings application locally. For detailed information on deployment, testing, and other aspects, please refer to the respective sections in this documentation.
