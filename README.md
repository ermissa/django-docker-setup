Docker compose project base with Django , PosgreSQL , Nginx , Gunicorn and Certbot. 

You can use this setup in both your development and production environments. Development setup uses python's webserver. Production setup uses gunicorn and nginx.

# Setup Project

Before starting to run this project ***docker*** and ***docker-compose*** should be installed on your computer.

## Installation

- Docker Installation: https://docs.docker.com/v17.12/install/
- Docker Compose Installation: https://docs.docker.com/compose/install/

## Configurations

- Replace ***django_docker_setup*** your project's name
- Replace ***sample_app*** with your app's name
- Replace ***sample_database_name*** with your database name 
- Replace ***example.com*** domain names in *data/nginx/conf_ssl.d/nginx.conf* and *init-letsencrypt* folders with your domain name(s).

You can replace these names by using search and replace feature in your IDE or editor.

## Run Project

### Run project for development environment 

```
docker-compose up
```

### Run project for production environment without Certbot

**In case you don't have domain or you don't want to get SSL certificates for your domain(s) yet**,run the command below.

```
docker-compose -f docker-compose.prod.yml up
```

### Run project for production environment with Certbot

You can get your SSL certificates from Let's Encrypt by running *init-letsencrypt.sh* script. 

First make the script executable by command below,

```
chmod u+x init-letsencrypt.sh 
```

Then run the script,

```
./init-letsencrypt.sh
```

This script will also start your containers. In case you down your containers, you can restart them by following command,

```
docker-compose -f docker-compose.prod.ssl up
```