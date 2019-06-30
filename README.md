Docker compose project base with Django, PosgreSQL , Nginx and Gunicorn. 

You can use this setup in both your development and production environments. Development setup uses python's webserver. Production setup uses gunicorn and nginx.

# Setup Project

Before starting to run this project ***docker*** and ***docker-compose*** should be installed on your computer.

## Installation

- Docker Installation: https://docs.docker.com/v17.12/install/
- Docker Compose Installation: https://docs.docker.com/compose/install/

## Configurations

- Change ***django_docker_setup*** your project's name
- Change ***sample_app*** with your app's name
- Change ***sample_database_name*** with your database name 

You can change these names by using search and replace feature in your IDE or editor.

## Run Project

### Run project for development environment

```
docker-compose up
```

### Run project for production environment

```
docker-compose -f docker-compose.prod.yml up
```