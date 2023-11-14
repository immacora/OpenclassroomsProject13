# OpenclassroomsProject13
Minimize the technical debt of the existing web app, Orange County Lettings, and deploy it.
The process is defined in the specifications (documentation directory).

<p align="center">
  <img src="static/assets/img/logo_light.png#gh-light-mode-only" alt="logo-light" />
  <img src="static/assets/img/logo_dark.png#gh-dark-mode-only" alt="logo-dark" />
</p>

### Tech & Tools
<p align="center">
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=FFD43B" alt="python-badge">
  </a>
  <a href="https://www.djangoproject.com">
    <img src="https://img.shields.io/badge/Django-4.2.6-092E20?style=for-the-badge&logo=django&logoColor=green" alt="django-badge">
  </a>
  <a href="https://docs.docker.com/">
    <img src="https://img.shields.io/badge/docker-4.24.2-086DD7?style=for-the-badge&logo=docker&logoColor=white" alt="docker-badge">
  </a>
  <a href="https://circleci.com/">
    <img src="https://img.shields.io/badge/circleci-2.1-049b4a?style=for-the-badge&logo=circleci&logoColor=black" alt="circleci-badge">
  </a>
  <a href="https://openclassroomsproject13.readthedocs.io/en/latest/">
    <img src="https://img.shields.io/badge/readthedocs-white?style=for-the-badge&logo=readthedocs" alt="readthedocs-badge">
  </a>
  <a href="https://sentry.io/">
    <img src="https://img.shields.io/badge/sentry-584674?style=for-the-badge&logo=sentry&logoColor=white" alt="sentry-badge">
  </a>

</p>

## Local development

### Clone Project
`git clone https://github.com/immacora/OpenclassroomsProject13`

### Retrieve project image
- Get [Docker](https://docs.docker.com/get-docker/)
- Retrieve [newest project image](https://hub.docker.com/r/immacora/oclettings/tags)

### Create Sentry project
- Create your [Sentry account](https://sentry.io/signup/)
- Select Projects and Create a new Sentry project:
  - Select Django
  - Enter your project name and create the project
  - Copy your dsn to paste it in your .env file as described below

### Settings and Environment Variables
Create a .env file in the project's root folder and paste the following variables with your own values:
```sh
# django
SECRET_KEY=YourDjangoSecretKey
DEBUG=True

# sentry
SENTRY_DSN=YourSentryProjectDSN
```

### Run app in Docker containers
`docker-compose up`

### Stops and removes Docker containers
`docker-compose down`

### Access
http://localhost:8000/

http://localhost:8000/admin/

### Admin Login:
* username : `admin`
* password : `Abc1234!`

### Linting
`docker-compose exec web flake8`

### Run tests
`docker-compose exec web pytest`

### Generate coverage report
- `docker-compose exec web coverage run -m pytest`
- `docker-compose exec web coverage report -m`


## Deployment (DigitalOcean)

### Description
Each commit triggers the compilation, linting and testing of the application, which must have coverage greater than 80%, via the CI/CD pipeline on your CircleCi account.

If the commit is done on the main branch and the previous job was successful, the pipeline builds the Docker image (tag: hash of last commit) and pushes it to Docker Hub. If the previous jobs was successful, deployment and production job on DigitalOcean is executed.

### Create server
- Create your [DigitalOcean account](https://www.digitalocean.com/)
- Create a new Droplet with Ubuntu (23.10) server and SSH Key Authentication Method
  - Create a [Firewall](https://docs.digitalocean.com/products/networking/firewalls/how-to/create/) with SSH, HTTP and HTTPS rules
  - Add [docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04) and [docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04)

### Create pipeline CI/CD (CircleCi)
- Fork the [project](https://github.com/immacora/OpenclassroomsProject13) on your github account
- Create your [CircleCI account connected to GitHub](https://circleci.com/docs/first-steps/#sign-up-and-create-an-org)
- Create New Project on [CircleCI app](https://app.circleci.com/) with GitHub connexion to your forked repository
  - Add an additional SSH Keys in the Project Settings and copy the Fingerprint to paste it in Environment Variables:
    ```sh
    Hostname: YourServerPublicIPAddress ; Private Key: YourServerPrivateSSHKey
    ```
  - Add Environment Variables in the Project Settings:
    ```sh
    Name: SECRET_KEY ; Value: YourDjangoSecretKey
    Name: SENTRY_DSN ; Value: YourSentryProjectDSN
    Name: ALLOWED_HOSTS ; Value: YourAllowedHosts
    Name: DOCKERHUB_PASSWORD ; Value: YourDockerHubPassword
    Name: DOCKERHUB_USERNAME ; Value: YourDockerHubUsername
    Name: USER ; Value: YourServerLogginUsername
    Name: IP ; Value: YourServerIP
    Name: SERVER_SSH_FINGERPRINT ; Value: YourSSHFingerprint
    ```
  Exemple for this project:

  [![CircleCI Build Status](https://dl.circleci.com/status-badge/img/gh/immacora/OpenclassroomsProject13/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/immacora/OpenclassroomsProject13/tree/main)


## Access
http://165.22.64.201/

http://165.22.64.201/admin/


## Documentation

For comprehensive information about the setup, features, and usage of this project, please refer to our official documentation. The documentation provides detailed instructions, explanations, and insights into the project's structure and capabilities.

You can access the full documentation here: [OC-Lettings Project Documentation](https://openclassroomsproject13.readthedocs.io/en/latest/).
