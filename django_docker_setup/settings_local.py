# pull in the normal settings
from django_docker_setup.settings import *

# no debug for us
DEBUG = True
ALLOWED_HOSTS = ['*']
