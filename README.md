Docker compose project base with Django, PosgreSQL , Nginx and Gunicorn. 

You can use this setup in both your development and production environments.

To use:

- Change ***sample_app*** names in docker-compose and docker-compose.prod.yml with your app's name
- Change ***sample_app*** name in settings.INSTALLED_APPS with your app's name
- Change ***project_name*** name in docker-compose.prod.yml with your project's name 
- Change ***project_name*** name in *nginx/conf.d/nginx.conf* with your project's name.
- Change ***sample_database_name*** name in settings.DATABASES with your database name 

You can change these names with using search & replace feature in your IDE or editor. I have listed all necessary changes in order to give an idea about the structure of the project.

I will create a file for environment variables soon, so you will not need to make those changes.


### Start project for development environment

```
docker-compose up
```

### Start project for production environment

```
docker-compose -f docker-compose.prod.yml up
```