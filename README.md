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
  <a href="https://about.readthedocs.com/">
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
- Paste the code into your terminal to get project image: `docker pull immacora/oclettings:1.0.0`

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

### Run server
`docker-compose up`

### Access
`http://localhost:8000/`

`http://localhost:8000/admin/`

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
